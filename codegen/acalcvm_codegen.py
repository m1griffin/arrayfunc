#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for acalc.
# Language: Python 3.4
# Date:     15-Jan-2016
#
###############################################################################
#
#   Copyright 2014 - 2016    Michael Griffin    <m12.griffin@gmail.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
##############################################################################

# ==============================================================================

import codegen_common

# ==============================================================================

func_template = '''
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   codearraylen = The length of the byte code array.
   codearray = The array of byte codes.
   varoffsetsarray = The array of variable offsets.
   vararray = The array of variable values.
   constarray = The array of constant values.
   vmstack = The array used for the stack.
   vmstacksize = The maximum size of the stack provided.
   vmstacksegments = The number of stack "segments" used when interating in "chunks".
   disableovfl = If true, disable arithmetic overflow checking (default is false).
   Return = 0 if OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int exequation_%(funcnamemodifier)s(Py_ssize_t arraylen, %(arrayvartype)s *data, %(arrayvartype)s *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, %(arrayvartype)s *vararray, %(arrayvartype)s *constarray,
			%(arrayvartype)s *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl) {


	// Index into op code array.
	unsigned int opindex = 0;
	// Index into data array.
	Py_ssize_t dataindex = 0;
	// Keep track of number of loop iterations.
	Py_ssize_t looptarget, loopremainder;
	// The number of times through the outer loop.
	Py_ssize_t stridecounter = 0;


	unsigned int stackpointer, slicestride, x;

%(ovtmp)s
%(errflag)s

	stackpointer = 0;

	// Number of full iterations through the outer loop required.
	looptarget = arraylen / vmstacksegments;
	// Number of array elements left over for the end of the array if the
	// array size is not evenly divisible.
	loopremainder = arraylen %% vmstacksegments;


	// The outer loop covers the entire data array.
	while(dataindex < arraylen) {

		// Reset the op code index and stack pointer for the next iteration.
		opindex = 0;
		stackpointer = 0;

		// The number of elements we go through in the inner loop may be differnt
		// during the last iteration.
		if (stridecounter < looptarget) { 
			slicestride = vmstacksegments; 
		} else {
			slicestride = (unsigned int) loopremainder;
		}


		// We go through the bytes codes once in sequence.
		// The middle loop goes through the interpreter instructions.
		while(opindex < codearraylen) {

			switch (codearray[opindex]) {
'''


# ==============================================================================

# Stack variables. These are substituted into the templates.
S0_Stack = 'vmstack[stackpointer + x]'
S1_Stack = 'vmstack[stackpointer + vmstacksegments + x]'

# ==============================================================================



# Temporary variables are only needed for some types.
ovtmp_signed_template = """	%(arrayvartype)s dataouttmp;	// Used for overflow calculations.
"""

ovtmp_unsigned_template = """	%(arrayvartype)s ovtmp1;	// Used for overflow calculations.
"""

intparamtmp_template = """	int paramtmp;	// Used for temporary type conversion calculations.
"""


# This is a special template for an unknown opcode.
unknown_template = '''				// %(comment)s
				case CALCOP_%(caselabeltype)s_%(labelname)s: {
					return CALC_ERR_UNKNOWNOP;
					}
'''


# This is a special template for an invalid opcode.
invalid_template = '''				// %(comment)s
				case CALCOP_%(caselabeltype)s_%(labelname)s: {
					return CALC_ERR_INVALIDOP;
					}
'''


# This is for operations which do not need overflow checking.
basic_template = '''				// %(comment)s
				case CALCOP_%(caselabeltype)s_%(labelname)s: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = %(operation)s;
					}
					break;
					}
'''


# This is for operations which do not need overflow checking AND do not
# consume stack positions.
basicneutral_template = '''				// %(comment)s
				case CALCOP_%(caselabeltype)s_%(labelname)s: {
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = %(operation)s;
					}
					break;
					}
'''


# This is for operations which consume stack elements. That is, the operation
# uses two stack levels and outputs one.
floatstackconsume_template = '''				// %(comment)s
				case CALCOP_FLOAT_%(labelname)s: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = %(operation)s;
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = %(operation)s;
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
'''


# This is for operations which only operates on the top of the stack and replaces
# it with the new value.
floatstackneutral_template = '''				// %(comment)s
				case CALCOP_FLOAT_%(labelname)s: { %(unsupportedop1)s
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = %(operation)s;
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = %(operation)s;
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; %(unsupportedop2)s
					}
'''

# ==============================================================================


# The basic template for each operator with or without overflow checking.
template_ovfl_begin = '''				// %(comment)s
				case CALCOP_%(caselabeltype)s_%(labelname)s: {%(paramcount)s
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = %(operation)s;
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = %(operation)s;
'''
template_ovfl_end = '''
						}
					}
					break;
					}
'''


# The basic template for each operator with integer post operation flag overflow checking.
template_ovfl_int = template_ovfl_begin + '\t\t\t\t\t\t\tif (errflag != 0) return CALC_ERR_ARITHMETIC;' + template_ovfl_end


# ==============================================================================

# Used when the function is not supported by some compilers.
template_unsupportedop1 = '''
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else
'''

template_unsupportedop2 = '''
					#endif
'''


# ==============================================================================


# Absolute value for signed integers.
template_ovfl_abs = '''				// %(comment)s
				case CALCOP_%(caselabeltype)s_%(labelname)s: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + x] >= 0 ? vmstack[stackpointer + x] : -vmstack[stackpointer + x]; 
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == %(minint)s) {return CALC_ERR_ARITHMETIC;}		// Overflow check.
							vmstack[stackpointer + x] = vmstack[stackpointer + x] >= 0 ? vmstack[stackpointer + x] : -vmstack[stackpointer + x]; 
						}
					}
					break;
					}
'''



# This operation does nothing. E.g. abs() for unsigned integers.
template_null_op = '''				// %(comment)s
				case CALCOP_%(caselabeltype)s_%(labelname)s: {
					break;
					}
'''


# ==============================================================================


# This template is a special one to handle ldexp which has mixed parameter types.
template_ldexp = '''				// %(comment)s
				case CALCOP_FLOAT_%(labelname)s: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = %(operation)s;
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > INT_MAX) || (vmstack[stackpointer + x] < INT_MIN)) {
								return CALC_ERR_OVFL;
							}
							vmstack[stackpointer + x] = %(operation)s;
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
'''

# ==============================================================================


# This is for operations which consume stack elements. That is, the operation
# uses two stack levels and outputs one.
intstackconsume_template = '''				// %(comment)s
				case CALCOP_INT_%(labelname)s: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = %(operation)s;
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = %(operation)s;
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
'''


# ==============================================================================


# Addition for signed integers.
template_ovfl_add_signed = '''				// %(comment)s
				case CALCOP_INT_%(labelname)s: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > 0) && (vmstack[stackpointer + vmstacksegments + x] > (%(maxint)s - vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] < 0) && (vmstack[stackpointer + vmstacksegments + x] < (%(minint)s - vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					}
					break;
					}
'''

# Addition for unsigned integers.
template_ovfl_add_unsigned = '''				// %(comment)s
				case CALCOP_INT_%(labelname)s: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + vmstacksegments + x] > (%(maxint)s - vmstack[stackpointer + x])) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					}
					break;
					}
'''


# ==============================================================================

# Subtraction for signed integers.
template_ovfl_sub_signed = '''				// %(comment)s
				case CALCOP_INT_%(labelname)s: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > 0) && (vmstack[stackpointer + vmstacksegments + x] < (%(minint)s + vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] < 0) && (vmstack[stackpointer + vmstacksegments + x] > (%(maxint)s + vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					}
					break;
					}
'''



# Subtraction for unsigned integers.
template_ovfl_sub_unsigned = '''				// %(comment)s
				case CALCOP_INT_%(labelname)s: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + vmstacksegments + x] < vmstack[stackpointer + x]) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					}
					break;
					}
'''

# ==============================================================================

# Multiplication for signed integers.
template_ovfl_mult_signed = '''				// %(comment)s
				case CALCOP_INT_%(labelname)s: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > 0) && ((vmstack[stackpointer + vmstacksegments + x] > (%(maxint)s / vmstack[stackpointer + x])) || (vmstack[stackpointer + vmstacksegments + x] < (%(minint)s / vmstack[stackpointer + x])))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] < -1) && ((vmstack[stackpointer + vmstacksegments + x] < (%(maxint)s / vmstack[stackpointer + x])) || (vmstack[stackpointer + vmstacksegments + x] > (%(minint)s / vmstack[stackpointer + x])))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] == -1) && (vmstack[stackpointer + vmstacksegments + x] == %(minint)s)) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					}
					break;
					}
'''

# Multiplication for unsigned integers.
template_ovfl_mult_unsigned = '''				// %(comment)s
				case CALCOP_INT_%(labelname)s: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] != 0) && (vmstack[stackpointer + vmstacksegments + x] > (%(maxint)s / vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					}
					break;
					}
'''


# ==============================================================================

# Division for signed integers.
template_ovfl_div_signed = '''				// %(comment)s
				case CALCOP_INT_%(labelname)s: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						// Cannot disable divide by zero checking because this causes a crash.
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							if ((vmstack[stackpointer + x] == -1) && (vmstack[stackpointer + vmstacksegments + x] == %(minint)s)) {return CALC_ERR_OVFL;}		// Overflow check.
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						}
					}
					break;
					}
'''

# Division for unsigned integers.
template_ovfl_div_usigned = '''				// %(comment)s
				case CALCOP_INT_%(labelname)s: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
					}
					break;
					}
'''


# ==============================================================================


# Floor division for signed integers.
template_ovfl_floordiv_signed = '''				// %(comment)s
				case CALCOP_INT_%(labelname)s: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							dataouttmp = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
							// This check is required for floor division.
							if (((vmstack[stackpointer + vmstacksegments + x] < 0) != (vmstack[stackpointer + x] < 0)) && ((dataouttmp * vmstack[stackpointer + x]) != vmstack[stackpointer + vmstacksegments + x])) { 
								vmstack[stackpointer + x] = dataouttmp - 1; 
							} else {
								vmstack[stackpointer + x] = dataouttmp;
							}
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							if ((vmstack[stackpointer + x] == -1) && (vmstack[stackpointer + vmstacksegments + x] == %(minint)s)) {return CALC_ERR_OVFL;}		// Overflow check.
							dataouttmp = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
							// This check is required for floor division.
							if (((vmstack[stackpointer + vmstacksegments + x] < 0) != (vmstack[stackpointer + x] < 0)) && ((dataouttmp * vmstack[stackpointer + x]) != vmstack[stackpointer + vmstacksegments + x])) { 
								vmstack[stackpointer + x] = dataouttmp - 1; 
							} else {
								vmstack[stackpointer + x] = dataouttmp;
							}
						}
					}
					break;
					}
'''


# ==============================================================================

# Modulus for signed integers.
template_ovfl_mod_signed = '''				// %(comment)s
				case CALCOP_INT_%(labelname)s: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						dataouttmp = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						// This check is required for floor division.
						if (((vmstack[stackpointer + vmstacksegments + x] < 0) != (vmstack[stackpointer + x] < 0)) && ((dataouttmp * vmstack[stackpointer + x]) != vmstack[stackpointer + vmstacksegments + x])) { 
							dataouttmp = dataouttmp - 1;
						}
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x] * dataouttmp;
					}
					break;
					}
'''

# Modulus for unsigned integers.
template_ovfl_mod_usigned = '''				// %(comment)s
				case CALCOP_INT_%(labelname)s: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] %% vmstack[stackpointer + x];
					}
					break;
					}
'''

# ==============================================================================

# Unary subtraction. This is valid for signed integers only.
template_ovfl_usub = '''				// %(comment)s
				case CALCOP_INT_%(labelname)s: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = -vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == %(minint)s) {return CALC_ERR_OVFL;}		// Overflow check.
							vmstack[stackpointer + x] = -vmstack[stackpointer + x];
						}
					}
					break;
					}
'''

# Unary subtraction. This is valid for signed integers only.
template_ovfl_uadd = '''				// %(comment)s
				case CALCOP_INT_%(labelname)s: {
					// No overflow checking required for this.
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = +vmstack[stackpointer + x];
					}
					break;
					}
'''

# ==============================================================================

# Code templates.
code_templates = {'basic_template' : basic_template,
			'basicneutral_template' : basicneutral_template,
			'unknown_template' : unknown_template,
			'invalid_template' : invalid_template,
			'template_ldexp' : template_ldexp,
			'floatstackconsume_template' : floatstackconsume_template,
			'floatstackneutral_template' : floatstackneutral_template,
			'template_ovfl_add_signed' : template_ovfl_add_signed,
			'template_ovfl_add_unsigned' : template_ovfl_add_unsigned,
			'template_ovfl_sub_signed' : template_ovfl_sub_signed,
			'template_ovfl_sub_unsigned' : template_ovfl_sub_unsigned,
			'template_ovfl_mult_signed' : template_ovfl_mult_signed,
			'template_ovfl_mult_unsigned' : template_ovfl_mult_unsigned,
			'template_ovfl_div_signed' : template_ovfl_div_signed,
			'template_ovfl_div_usigned' : template_ovfl_div_usigned,
			'template_ovfl_floordiv_signed' : template_ovfl_floordiv_signed,
			'template_ovfl_mod_signed' : template_ovfl_mod_signed,
			'template_ovfl_mod_usigned' : template_ovfl_mod_usigned,
			'template_ovfl_usub' : template_ovfl_usub,
			'intstackconsume_template' : intstackconsume_template,
			'template_ovfl_uadd' : template_ovfl_uadd,
			'template_ovfl_int' : template_ovfl_int,
			'template_ovfl_abs' : template_ovfl_abs,
			'template_null_op' : template_null_op,
}


# ==============================================================================


# Used when the parameter is required and must be checked for.
template_paramcount = '\n\t\tif (paramcount < 1) {return ARR_ERR_PARAMMISSING;}'


functionclosetemplate = '''
			}
			// Increment the op code index to the next instruction.
			opindex++;
		}

		// Store the calculation result.
		for(x = 0; x < slicestride; x++) {
			dataout[dataindex + x] = vmstack[stackpointer + x];
		}

		// Increment the data index array.
		dataindex = dataindex + vmstacksegments;

		// Count up the number of outer loops we need to go through.
		stridecounter++;

	}


	return CALC_NO_ERR;

}
/*--------------------------------------------------------------------------- */

'''

# ==============================================================================

############################################################
def GetTemplate(op, arraycode):
	"""Get the required template type.
	"""
	if arraycode in codegen_common.signedint:
		template = code_templates[op['c_code_template_i_signed']]

	elif arraycode in codegen_common.unsignedint:
		template = code_templates[op['c_code_template_i_unsigned']]

	elif arraycode in codegen_common.floatarrays:
		template = code_templates[op['c_code_template_float']]

	else:
		print('Unknow array code %s' % arraycode)

	return template


############################################################
def GetCOperator(opdata, arraycode):
	"""Create C code for a single op.
	"""
	# The type specific data to subsitute in.
	if arraycode in codegen_common.intarrays:
		c_operator = opdata['c_operator_i']
	elif arraycode == 'f':
		c_operator = opdata['c_operator_f']
	else:
		c_operator = opdata['c_operator_d']


	cop = c_operator % {'S0' : S0_Stack, 'S1' : S1_Stack, 
			'itype' : codegen_common.arraytypes[arraycode].replace(' ', '_')}
	
	return cop



############################################################
def CreateFunction(csvdata, arraycode):
	"""Create C code for a single array type.
	"""
	# The type of unit test assert we use for testing the results depends on
	# whether we are comparing floating point or integer values.
	if arraycode in codegen_common.signedint:
		opdata = [x for x in csvdata if x['c_code_template_i_signed'] != '']

	elif arraycode in codegen_common.unsignedint:
		opdata = [x for x in csvdata if x['c_code_template_i_unsigned'] != '']

	elif arraycode in codegen_common.floatarrays:
		opdata = [x for x in csvdata if x['c_code_template_float'] != '']

	else:
		print('Unknow array code %s' % arraycode)


	if arraycode in codegen_common.intarrays:
		caselabeltype = 'INT'
	else:
		caselabeltype = 'FLOAT'


	codeoutput = []

	for op in opdata:

		# Get the template.
		optemplate = GetTemplate(op, arraycode)


		# Build up the data to substitute into the template.
		opvalues = {}
		opvalues['comment'] = op['opcodename']

		opvalues['caselabeltype'] = caselabeltype

		if op['#params'] != '0':
			opvalues['paramcount'] = template_paramcount
		else:
			opvalues['paramcount'] = ''


		# Some compilers do not support some math functions.
		if op['msvs_has'] == '0':
			opvalues['unsupportedop1'] = template_unsupportedop1
			opvalues['unsupportedop2'] = template_unsupportedop2
		else:
			opvalues['unsupportedop1'] = ''
			opvalues['unsupportedop2'] = ''


		# This forms part of the case label.
		opvalues['labelname'] = op['opcodename'].upper().replace(' ', '_').upper().replace('.', '_')

		# The basic equation.
		opvalues['operation'] = GetCOperator(op, arraycode)

		# We have special templates for handling integer operations where we need
		# to check for overflow. These are too complex to fit into the standard
		# templates.
		opvalues['maxint'] = codegen_common.maxvalue[arraycode]
		opvalues['minint'] = codegen_common.minvalue[arraycode]

		# This gives the array data type.
		opvalues['arrayvartype'] = codegen_common.arraytypes[arraycode]

		# Create the code.
		codeoutput.append(optemplate % opvalues)

	return ''.join(codeoutput)



############################################################

# Read in the data from the CSV spreadsheet which holds the configuration.
csvdata = codegen_common.ReadCSVData('arraycalc.csv')

with open('acalcvm_code.txt', 'w') as f:
	# Output the generated code.
	for funtypes in codegen_common.arraycodes:
		# Only use error flags for integer arrays.
		if funtypes in codegen_common.intarrays:
			errflagcode = '	char errflag = 0;\n'
		else:
			errflagcode = ''


		# Temporary variables used for integer arrays.
		if funtypes in codegen_common.signedint:
			ovtmp = ovtmp_signed_template % {'arrayvartype' : codegen_common.arraytypes[funtypes]}
		else:
			ovtmp = ''


		# Create the function declaration for an array type.
		f.write(func_template % {'funcnamemodifier' : codegen_common.arraytypes[funtypes].replace(' ', '_'), 
				'arrayvartype' : codegen_common.arraytypes[funtypes], 
				'errflag' : errflagcode, 'ovtmp' : ovtmp})
		# Create the C code for the function.
		f.write(CreateFunction(csvdata, funtypes))
		# Close off the end of the function.
		f.write(functionclosetemplate)


############################################################


