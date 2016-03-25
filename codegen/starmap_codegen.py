#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for starmap and starmapi.
# Language: Python 3.4
# Date:     02-Jul-2014
#
###############################################################################
#
#   Copyright 2014 - 2015    Michael Griffin    <m12.griffin@gmail.com>
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
/* opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   data2 = The second input data array.
   dataout = The output data array.
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int starmap_%(funcnamemodifier)s(signed int opcode, Py_ssize_t arraylen, %(arrayvartype)s *data, %(arrayvartype)s *data2, %(arrayvartype)s *dataout, unsigned int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
%(tmpvars)s
%(errflag)s

	switch(opcode) {

'''


# The basic template for each operator.
basic_template = '''	// %(comment)s
	case OP_%(labelname)s: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = %(operation)s;
		}
		return ARR_NO_ERR;
	}
'''


template_ovfl_begin = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = %(operation)s;
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = %(operation)s;
'''
template_ovfl_end = '''
			}
		}
		return ARR_NO_ERR;
	}
'''


# The basic template for each operator with no overflow checking.
template_ovfl_none = template_ovfl_begin + template_ovfl_end
# The basic template for each operator with integer post operation flag overflow checking.
template_ovfl_int = template_ovfl_begin + '\t\t\t\tif (errflag != 0) return ARR_ERR_OVFL;' + template_ovfl_end
# The basic template for each operator with integer post operation flag overflow checking.
template_ovfl_float = template_ovfl_begin + '\t\t\t\tif (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}' + template_ovfl_end


# ==============================================================================


# The template for compare operators.
compare_template = '''	// %(comment)s
	case OP_%(labelname)s: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (%(arrayvartype)s) (%(operation)s);
		}
		return ARR_NO_ERR;
	}
'''

# ==============================================================================

# This template is a special one to handle ldexp which has mixed parameter types.
template_ldexp = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (!isfinite(data2[x]) || (data2[x] > INT_MAX) || (data2[x] < INT_MIN)) {
					return ARR_ERR_OVFL;
				}
				dataout[x] = %(operation)s(data[x], (int) data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (!isfinite(data2[x]) || (data2[x] > INT_MAX) || (data2[x] < INT_MIN)) {
					return ARR_ERR_OVFL;
				}
				dataout[x] = %(operation)s(data[x], (int) data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
'''


# ==============================================================================


# Special purpose arithmetic templates with improved overflow checking.

# Division for unsigned integers.
template_ovfl_div_usigned = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data[x] / data2[x];
		}
		return ARR_NO_ERR;
	}
'''

# Division for unsigned integers with reversed parameters.
template_ovfl_div_r_usigned = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data2[x] / data[x];
		}
		return ARR_NO_ERR;
	}
'''

# Division for signed integers.
template_ovfl_div_signed = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] / data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((data2[x] == -1) && (data[x] == %(minint)s)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] / data2[x]; 
			}
		}
		return ARR_NO_ERR;
	}
'''

# Division for signed integers with reversed parameters.
template_ovfl_div_r_signed = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data2[x] / data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((data2[x] == %(minint)s) && (data[x] == -1)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data2[x] / data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
'''


# Floor division for signed integers.
template_ovfl_floordiv_signed = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (data2tmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = datatmp / data2tmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (data2tmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((data2tmp == -1) && (datatmp == %(minint)s)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = datatmp / data2tmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		}
		return ARR_NO_ERR;
	}
'''


# Floor division for signed integers with reversed parameters.
template_ovfl_floordiv_r_signed = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = data2tmp / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * datatmp) != data2tmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((datatmp == -1) && (data2tmp == %(minint)s)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = data2tmp / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * datatmp) != data2tmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		}
		return ARR_NO_ERR;
	}
'''


# Modulus for unsigned integers.
template_ovfl_mod_usigned = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data[x] %% data2[x];
		}
		return ARR_NO_ERR;
	}
'''

# Modulus for unsigned integers with reversed parameters.
template_ovfl_mod_r_usigned = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data2[x] %% data[x];
		}
		return ARR_NO_ERR;
	}
'''

# Modulus for signed integers.
template_ovfl_mod_signed = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			data2tmp = data2[x];
			if (data2tmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataouttmp = datatmp / data2tmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = datatmp - data2tmp * dataouttmp;
		}
		return ARR_NO_ERR;
	}
'''

# Modulus for signed integers with reversed parameters.
template_ovfl_mod_r_signed = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			data2tmp = data2[x];
			if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataouttmp = data2tmp / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * datatmp) != data2tmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = data2tmp - datatmp * dataouttmp;
		}
		return ARR_NO_ERR;
	}
'''


# Negation for signed integers.
template_ovfl_negate = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == %(minint)s) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = -data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
'''


# Absolute value for signed integers.
template_ovfl_abs = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] >= 0 ? data[x] : -data[x]; 
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == %(minint)s) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] >= 0 ? data[x] : -data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
'''



# Addition for unsigned integers.
template_ovfl_add_unsigned = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] > (%(maxint)s - data2[x])) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] + data2[x]; 
			}
		}
		return ARR_NO_ERR;
	}
'''



# Addition for signed integers.
template_ovfl_add_signed = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] > 0) && (data[x] > (%(maxint)s - data2[x]))) {return ARR_ERR_OVFL;}
				if ((data2[x] < 0) && (data[x] < (%(minint)s - data2[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] + data2[x];
			}
		}
		return ARR_NO_ERR;
	}
'''

# Subtraction for unsigned integers.
template_ovfl_sub_unsigned = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] < data2[x]) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] - data2[x]; 
			}
		}
		return ARR_NO_ERR;
	}
'''



# Subtraction for unsigned integers with reversed parameters.
template_ovfl_sub_r_unsigned = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < data[x]) {return ARR_ERR_OVFL;}
				dataout[x] = data2[x] - data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
'''



# Subtraction for signed integers.
template_ovfl_sub_signed = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] > 0) && (data[x] < (%(minint)s + data2[x]))) {return ARR_ERR_OVFL;}
				if ((data2[x] < 0) && (data[x] > (%(maxint)s + data2[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] - data2[x];
			}
		}
		return ARR_NO_ERR;
	}
'''



# Subtraction for signed integers with reversed parameters.
template_ovfl_sub_r_signed = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > 0) && (data2[x] < (%(minint)s + data[x]))) {return ARR_ERR_OVFL;}
				if ((data[x] < 0) && (data2[x] > (%(maxint)s + data[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data2[x] - data[x];
			}
		}
		return ARR_NO_ERR;
	}
'''



# Multiplication for unsigned integers.
template_ovfl_mult_unsigned = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] != 0) && (data[x] > (%(maxint)s / data2[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] * data2[x];
			}
		}
		return ARR_NO_ERR;
	}
'''


# Multiplication for signed integers.
template_ovfl_mult_signed = '''	// %(comment)s
	case OP_%(labelname)s: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * data2[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] > 0) && ((data[x] > (%(maxint)s / data2[x])) || (data[x] < (%(minint)s / data2[x])))) {return ARR_ERR_OVFL;}
				if ((data2[x] < -1) && ((data[x] < (%(maxint)s / data2[x])) || (data[x] > (%(minint)s / data2[x])))) {return ARR_ERR_OVFL;}
				if ((data2[x] == -1) && (data[x] == %(minint)s)) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] * data2[x];
			}
		}
		return ARR_NO_ERR;
	}
'''


# Code templates.
code_templates = {'basic_template' : basic_template,
			'compare_template' : compare_template,
			'template_ovfl_none' : template_ovfl_none,
			'template_ovfl_int' : template_ovfl_int,
			'template_ovfl_float' : template_ovfl_float,
			'template_ovfl_abs' : template_ovfl_abs,
			'template_ovfl_add_signed' : template_ovfl_add_signed,
			'template_ovfl_add_unsigned' : template_ovfl_add_unsigned,
			'template_ovfl_div_r_signed' : template_ovfl_div_r_signed,
			'template_ovfl_div_r_usigned' : template_ovfl_div_r_usigned,
			'template_ovfl_div_signed' : template_ovfl_div_signed,
			'template_ovfl_div_usigned' : template_ovfl_div_usigned,
			'template_ovfl_floordiv_r_signed' : template_ovfl_floordiv_r_signed,
			'template_ovfl_floordiv_signed' : template_ovfl_floordiv_signed,
			'template_ovfl_mod_r_signed' : template_ovfl_mod_r_signed,
			'template_ovfl_mod_r_usigned' : template_ovfl_mod_r_usigned,
			'template_ovfl_mod_signed' : template_ovfl_mod_signed,
			'template_ovfl_mod_usigned' : template_ovfl_mod_usigned,
			'template_ovfl_mult_signed' : template_ovfl_mult_signed,
			'template_ovfl_mult_unsigned' : template_ovfl_mult_unsigned,
			'template_ovfl_negate' : template_ovfl_negate,
			'template_ovfl_sub_r_signed' : template_ovfl_sub_r_signed,
			'template_ovfl_sub_r_unsigned' : template_ovfl_sub_r_unsigned,
			'template_ovfl_sub_signed' : template_ovfl_sub_signed,
			'template_ovfl_sub_unsigned' : template_ovfl_sub_unsigned,
			'template_ldexp' : template_ldexp,
}

# ==============================================================================


functionclosetemplate = '''
	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */


'''


# Temporary variables are only needed for some types.
tmpvardeclaration = '\t%(arrayvartype)s datatmp, data2tmp, dataouttmp;'

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


	cop = c_operator % {'X' : 'data[x]', 'Y' : 'data2[x]', 
			'itype' : codegen_common.arraytypes[arraycode].replace(' ', '_')}

	return cop



def CreateFunction(csvdata, arraycode):
	"""Create C code for a single array type.
	"""
	# The type of unit test assert we use for testing the results depends on
	# whether we are comparing floating point or integer values.
	if arraycode in codegen_common.signedint:
		opdata = [x for x in csvdata if x['c_code_template_i_signed'] != '' and x['#params'] != '0']

	elif arraycode in codegen_common.unsignedint:
		opdata = [x for x in csvdata if x['c_code_template_i_unsigned'] != '' and x['#params'] != '0']

	elif arraycode in codegen_common.floatarrays:
		opdata = [x for x in csvdata if x['c_code_template_float'] != '' and x['#params'] != '0']

	else:
		print('Unknow array code %s' % arraycode)


	codeoutput = []

	for op in opdata:
		# Avoid changing the original record.
		testrec = {}
		testrec['typecode'] = arraycode

		testrec.update(testrec)

		# Get the template.
		optemplate = GetTemplate(op, arraycode)


		# Build up the data to substitute into the template.
		opvalues = {}
		opvalues['comment'] = op['opcodename']


		# This forms part of the case label.
		opvalues['labelname'] = op['opcodename'].upper().replace(' ', '_')

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


# ==============================================================================

############################################################

# Read in the data from the CSV spreadsheet which holds the configuration.
csvdata = codegen_common.ReadCSVData('arrayfunc.csv')


with open('starmap_code.txt', 'w') as f:
	# Output the generated code.
	for funtypes in codegen_common.arraycodes:
		# Only use error flags for integer arrays.
		if funtypes in codegen_common.intarrays:
			errflagcode = '	char errflag = 0;\n'
		else:
			errflagcode = ''

		# Temporary variables used for integer arrays.
		if funtypes in codegen_common.signedint:
			tmpvars = tmpvardeclaration % {'arrayvartype' : codegen_common.arraytypes[funtypes]}
		else:
			tmpvars = ''
			
		# Create the function declaration for an array type.
		f.write(func_template % {'funcnamemodifier' : codegen_common.arraytypes[funtypes].replace(' ', '_'), 
				'arrayvartype' : codegen_common.arraytypes[funtypes], 
				'errflag' : errflagcode, 'tmpvars' : tmpvars})
		# Create the C code for the function.
		f.write(CreateFunction(csvdata, funtypes))
		# Close off the end of the function.
		f.write(functionclosetemplate)



