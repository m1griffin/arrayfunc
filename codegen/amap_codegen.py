#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for amap and amapi.
# Language: Python 3.4
# Date:     24-May-2014
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
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   paramcount = The number of valid parameters (normally 0 or 1).
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int map_%(funcnamemodifier)s(signed int opcode, Py_ssize_t arraylen, %(arrayvartype)s *data, %(arrayvartype)s *dataout, %(arrayvartype)s param1, unsigned int paramcount, unsigned int disableovfl) {

	// array index counter.
	Py_ssize_t x;

%(errflag)s
%(ovtmp)s

	switch(opcode) {

'''

# Temporary variables are only needed for some types.
ovtmp_signed_template = """	%(arrayvartype)s ovtmp1, ovtmp2, datatmp, dataouttmp;	// Used for overflow calculations.
"""

ovtmp_unsigned_template = """	%(arrayvartype)s ovtmp1;	// Used for overflow calculations.
"""

intparamtmp_template = """	int paramtmp;	// Used for temporary type conversion calculations.
"""


# The basic template for each operator.
basic_template = '''	// %(comment)s
	case OP_%(labelname)s: {%(paramcount)s %(unsupportedop1)s
		for(x = 0; x < arraylen; x++) {
			dataout[x] = %(operation)s;
		}
		return ARR_NO_ERR; %(unsupportedop2)s
	}
'''



# The basic template for each operator with or without overflow checking.
template_ovfl_begin = '''	// %(comment)s
	case OP_%(labelname)s: {%(paramcount)s %(unsupportedop1)s
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
		return ARR_NO_ERR; %(unsupportedop2)s
	}
'''


# The basic template for each operator with no overflow checking.
template_ovfl_none = template_ovfl_begin + template_ovfl_end
# The basic template for each operator with integer post operation flag overflow checking.
template_ovfl_int = template_ovfl_begin + '\t\t\t\tif (errflag != 0) return ARR_ERR_OVFL;' + template_ovfl_end
# The basic template for each operator with integer post operation flag overflow checking.
template_ovfl_float = template_ovfl_begin + '\t\t\t\tif (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}' + template_ovfl_end


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


# The template for compare operators.
compare_template = '''	// %(comment)s
	case OP_%(labelname)s: {%(paramcount)s
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
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		if ((param1 > INT_MAX) || (param1 < INT_MIN)) {
			return ARR_ERR_OVFL;
		}
		paramtmp = (int) param1;
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = %(operation)s(data[x], paramtmp);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = %(operation)s(data[x], paramtmp);
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
	case OP_%(labelname)s: {%(paramcount)s
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] / param1;
		}
		return ARR_NO_ERR;
	}
'''

# Division for unsigned integers with reversed parameters.
template_ovfl_div_r_usigned = '''	// %(comment)s
	case OP_%(labelname)s: {%(paramcount)s
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = param1 / data[x];
		}
		return ARR_NO_ERR;
	}
'''

# Division for signed integers.
template_ovfl_div_signed = '''	// %(comment)s
	case OP_%(labelname)s: {%(paramcount)s
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] / param1;
			}
		} else {
		// Overflow checking enabled.
			ovtmp1 = (param1 == -1);		// Overflow check.
			for(x = 0; x < arraylen; x++) {
				if (ovtmp1 && (data[x] == %(minint)s)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] / param1; 
			}
		}
		return ARR_NO_ERR;
	}
'''

# Division for signed integers with reversed parameters.
template_ovfl_div_r_signed = '''	// %(comment)s
	case OP_%(labelname)s: {%(paramcount)s
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = param1 / data[x];
			}
		} else {
		// Overflow checking enabled.
			ovtmp1 = (param1 == %(minint)s);		// Overflow check.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if (ovtmp1 && (data[x] == -1)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = param1 / data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
'''


# Floor division for signed integers.
template_ovfl_floordiv_signed = '''	// %(comment)s
	case OP_%(labelname)s: {%(paramcount)s
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				dataouttmp = datatmp / param1;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * param1) != datatmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				if ((param1 == -1) && (datatmp == %(minint)s)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = datatmp / param1;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * param1) != datatmp)) { 
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
	case OP_%(labelname)s: {%(paramcount)s
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = param1 / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * datatmp) != param1)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((datatmp == -1) && (param1 == %(minint)s)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = param1 / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * datatmp) != param1)) { 
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
	case OP_%(labelname)s: {%(paramcount)s
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] %% param1;
		}
		return ARR_NO_ERR;
	}
'''

# Modulus for unsigned integers with reversed parameters.
template_ovfl_mod_r_usigned = '''	// %(comment)s
	case OP_%(labelname)s: {%(paramcount)s
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = param1 %% data[x];
		}
		return ARR_NO_ERR;
	}
'''

# Modulus for signed integers.
template_ovfl_mod_signed = '''	// %(comment)s
	case OP_%(labelname)s: {%(paramcount)s
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			dataouttmp = datatmp / param1;
			// This check is required for floor division.
			if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * param1) != datatmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = datatmp - param1 * dataouttmp;
		}
		return ARR_NO_ERR;
	}
'''

# Modulus for signed integers with reversed parameters.
template_ovfl_mod_r_signed = '''	// %(comment)s
	case OP_%(labelname)s: {%(paramcount)s
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataouttmp = param1 / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * datatmp) != param1)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = param1 - datatmp * dataouttmp;
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
	case OP_%(labelname)s: {%(paramcount)s
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + param1;
			}
		} else {
		// Overflow checking enabled.
			ovtmp1 = %(maxint)s - param1;		// Overflow check.
			for(x = 0; x < arraylen; x++) {
				if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] + param1; 
			}
		}
		return ARR_NO_ERR;
	}
'''



# Addition for signed integers.
template_ovfl_add_signed = '''	// %(comment)s
	case OP_%(labelname)s: {%(paramcount)s
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = data[x]; 
				}
			}
			if (param1 > 0) {
				ovtmp1 = %(maxint)s - param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] + param1; 
				}
			}
			if (param1 < 0) {
				ovtmp1 = %(minint)s - param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] < ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] + param1; 
				}
			}
		}
		return ARR_NO_ERR;
	}
'''

# Subtraction for unsigned integers.
template_ovfl_sub_unsigned = '''	// %(comment)s
	case OP_%(labelname)s: {%(paramcount)s
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1;
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] < param1) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] - param1; 
			}
		}
		return ARR_NO_ERR;
	}
'''



# Subtraction for unsigned integers with reversed parameters.
template_ovfl_sub_r_unsigned = '''	// %(comment)s
	case OP_%(labelname)s: {%(paramcount)s
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (param1 < data[x]) {return ARR_ERR_OVFL;}
				dataout[x] = param1 - data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
'''



# Subtraction for signed integers.
template_ovfl_sub_signed = '''	// %(comment)s
	case OP_%(labelname)s: {%(paramcount)s
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = data[x]; 
				}
			}
			if (param1 > 0) {
				ovtmp1 = %(minint)s + param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] < ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] - param1; 
				}
			}
			if (param1 < 0) {
				ovtmp1 = %(maxint)s + param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] - param1; 
				}
			}
		}
		return ARR_NO_ERR;
	}
'''



# Subtraction for signed integers with reversed parameters.
template_ovfl_sub_r_signed = '''	// %(comment)s
	case OP_%(labelname)s: {%(paramcount)s
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x];
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					if (data[x] == %(minint)s) {return ARR_ERR_OVFL;}
					dataout[x] = -data[x]; 
				}
			}
			if (param1 > 0) {
				ovtmp1 = param1 - %(maxint)s;
				for(x = 0; x < arraylen; x++) {
					if (data[x] < ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = param1 - data[x]; 
				}
			}
			if (param1 < 0) {
				ovtmp1 = param1 - %(minint)s;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = param1 - data[x]; 
				}
			}
		}
		return ARR_NO_ERR;
	}
'''



# Multiplication for unsigned integers.
template_ovfl_mult_unsigned = '''	// %(comment)s
	case OP_%(labelname)s: {%(paramcount)s
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = 0; 
				}
			} else {
				ovtmp1 = %(maxint)s / param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] * param1; 
				}
			}
		}
		return ARR_NO_ERR;
	}
'''


# Multiplication for signed integers.
template_ovfl_mult_signed = '''	// %(comment)s
	case OP_%(labelname)s: {%(paramcount)s
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = 0; 
				}
			} else {
				// Signed integers do not have a symetrical range (e.g. -128 to 127). 
				if (param1 == -1) {
					for(x = 0; x < arraylen; x++) {
						if (data[x] == %(minint)s) {return ARR_ERR_OVFL;}
						dataout[x] = data[x] * param1; 
					}
				} else {
					ovtmp1 = %(maxint)s / param1;
					ovtmp2 = %(minint)s / param1;
					if (param1 > 0) {
						for(x = 0; x < arraylen; x++) {
							if ((data[x] > ovtmp1) || (data[x] < ovtmp2)) {return ARR_ERR_OVFL;}
							dataout[x] = data[x] * param1; 
						}
					}
					if (param1 < -1) {
						for(x = 0; x < arraylen; x++) {
							if ((data[x] < ovtmp1) || (data[x] > ovtmp2)) {return ARR_ERR_OVFL;}
							dataout[x] = data[x] * param1; 
						}
					}
				}
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


# Used when the parameter is required and must be checked for.
template_paramcount = '\n\t\tif (paramcount < 1) {return ARR_ERR_PARAMMISSING;}'


functionclosetemplate = '''
	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
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


	cop = c_operator % {'X' : 'data[x]', 'Y' : 'param1', 
			'itype' : codegen_common.arraytypes[arraycode].replace(' ', '_')}
	
	return cop



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



############################################################

# Read in the data from the CSV spreadsheet which holds the configuration.
csvdata = codegen_common.ReadCSVData()

with open('amap_code.txt', 'w') as f:
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
		elif funtypes in codegen_common.unsignedint:
			ovtmp = ovtmp_unsigned_template % {'arrayvartype' : codegen_common.arraytypes[funtypes]}
		elif funtypes in codegen_common.floatarrays:
			ovtmp = intparamtmp_template
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


