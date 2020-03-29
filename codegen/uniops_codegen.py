#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for math operators with one variable.
# Language: Python 3.4
# Date:     18-Mar-2018
#
###############################################################################
#
#   Copyright 2014 - 2020    Michael Griffin    <m12.griffin@gmail.com>
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

import itertools

import codegen_common

# ==============================================================================

uniops_head = """//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   %(funclabel)s.c
// Purpose:  Calculate the %(funclabel)s of values in an array.
// Language: C
// Date:     15-Nov-2017.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2020    Michael Griffin    <m12.griffin@gmail.com>
//
//   Licensed under the Apache License, Version 2.0 (the "License");
//   you may not use this file except in compliance with the License.
//   You may obtain a copy of the License at
//
//       http://www.apache.org/licenses/LICENSE-2.0
//
//   Unless required by applicable law or agreed to in writing, software
//   distributed under the License is distributed on an "AS IS" BASIS,
//   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//   See the License for the specific language governing permissions and
//   limitations under the License.
//
//------------------------------------------------------------------------------

/*--------------------------------------------------------------------------- */
// This must be defined before "Python.h" in order for the pointers in the
// argument parsing functions to work properly. 
#define PY_SSIZE_T_CLEAN

#include "Python.h"

#include <limits.h>
#include <math.h>

#include "arrayerrs.h"
#include "arrayparams_base.h"
#include "arrayparams_onesimd.h"

#include "simddefs.h"

#ifdef AF_HASSIMD_X86
#include "%(funclabel)s_simd_x86.h"
#endif

#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
#include "arm_neon.h"
#endif

#if defined(AF_HASSIMD_ARMv7_32BIT)
#include "%(funclabel)s_simd_armv7.h"
#endif

#if defined(AF_HASSIMD_ARM_AARCH64)
#include "%(funclabel)s_simd_armv8.h"
#endif

/*--------------------------------------------------------------------------- */

"""

# ==============================================================================

# For floating point.
uniops_op_float = """
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int %(funclabel)s_%(funcmodifier)s(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data, %(arraytype)s *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;

%(simd_call)s
	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = %(copname)s;
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = %(copname)s;
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = %(copname)s;
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = %(copname)s;
				if (!isfinite(data[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
	}

	return ARR_NO_ERR;

}

"""
# ==============================================================================



# ==============================================================================

# For negating signed integer.
uniops_neg_int = """
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int %(funclabel)s_%(funcmodifier)s(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data, %(arraytype)s *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;

%(simd_call)s
	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = -data[x];
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				if (data[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
				dataout[x] = -data[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if (data[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
				data[x] = -data[x];
			}
		}
	}

	return ARR_NO_ERR;

}

"""
# ==============================================================================

# ==============================================================================

# For absolute value of a signed integer.
uniops_abs_int = """
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int %(funclabel)s_%(funcmodifier)s(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data, %(arraytype)s *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;

%(simd_call)s
	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				if (data[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if (data[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
				data[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		}
	}

	return ARR_NO_ERR;

}

"""
# ==============================================================================


# ==============================================================================

# The operations using SIMD.
ops_simdsupport = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
*/
// param_arr_none
%(simdplatform)s
void %(funclabel)s_%(funcmodifier)s_1_simd(Py_ssize_t arraylen, %(arraytype)s *data) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft;
	%(vsignparam)s


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = %(simdop)s;
		// Store the result.
		%(vstinstr1)s &data[index], %(vstinstr2)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data[index] = %(simdcleanup)s;
	}

}
#endif


// param_arr_arr
%(simdplatform)s
void %(funclabel)s_%(funcmodifier)s_2_simd(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s *dataout) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft;
	%(vsignparam)s


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = %(simdop)s;
		// Store the result.
		%(vstinstr1)s &dataout[index], %(vstinstr2)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		dataout[index] = %(simdcleanup)s;
	}

}
#endif

"""


# SIMD call template.
SIMD_call = '''\n%(simdplatform)s
	// SIMD version.
	if (ignoreerrors && !nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		if (hasoutputarray) {
			%(funclabel)s_%(funcmodifier)s_2_simd(arraylen, data, dataout);
		} else {
			%(funclabel)s_%(funcmodifier)s_1_simd(arraylen, data);
		}
		return ARR_NO_ERR;
	}
#endif\n'''


# ==============================================================================


# ==============================================================================

# This is the set of function calls used to call each operator function.
opscall = """
		// %(funcmodifier)s
		case '%(arraycode)s' : {
			resultcode = %(funclabel)s_%(funcmodifier)s(arraydata.arraylength, arraydata.nosimd, arraydata.array1.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}
"""



uniops_params = """

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;

	// This is used to hold the parsed parameters.
	struct args_params_1 arraydata = ARGSINIT_ONE;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_one(self, args, keywds, 1, "%(funclabel)s");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}

	// Call the C function.
	switch(arraydata.arraytype) {
%(opscall)s
		// We don't know this code.
		default: {
			releasebuffers_one(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_one(arraydata);


	// Signal the errors.
	if (resultcode == ARR_ERR_ARITHMETIC) {
		ErrMsgArithCalc();
		return NULL;
	}

	if (resultcode == ARR_ERR_OVFL) {
		ErrMsgArithOverflowCalc();
		return NULL;
	}


	// Everything was successful.
	Py_RETURN_NONE;

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(%(funclabel)s__doc__,
"%(funclabel)s \\n\\
_____________________________ \\n\\
\\n\\
Calculate %(funclabel)s over the values in an array.  \\n\\
\\n\\
======================  ============================================== \\n\\
Equivalent to:          [%(opcodedocs)s for x in array1] \\n\\
======================  ============================================== \\n\\
\\n\\
======================  ============================================== \\n\\
Array types supported:  %(supportedarrays)s \\n\\
Exceptions raised:      %(matherrors)s \\n\\
======================  ============================================== \\n\\
\\n\\
Call formats: \\n\\
\\n\\
    %(funclabel)s(array1) \\n\\
    %(funclabel)s(array1, outparray) \\n\\
    %(funclabel)s(array1, maxlen=y) \\n\\
    %(funclabel)s(array1, matherrors=False)) \\n\\
    %(funclabel)s(array1, nosimd=False) \\n\\
\\n\\
* array1 - The first input data array to be examined. If no output \\n\\
  array is provided the results will overwrite the input data. \\n\\
* outparray - The output array. This parameter is optional. \\n\\
* maxlen - Limit the length of the array used. This must be a valid \\n\\
  positive integer. If a zero or negative length, or a value which is \\n\\
  greater than the actual length of the array is specified, this \\n\\
  parameter is ignored. \\n\\
* matherrors - If true, arithmetic error checking is disabled. The \\n\\
  default is false. \\n\\
* nosimd - If True, SIMD acceleration is disabled. This parameter is \\n\\
  optional. The default is FALSE.  \\n\\
");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "%(funclabel)s" is the name seen inside of Python. 
 "py_%(funclabel)s" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef %(funclabel)s_methods[] = {
	{"%(funclabel)s",  (PyCFunction)py_%(funclabel)s, METH_VARARGS | METH_KEYWORDS, %(funclabel)s__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef %(funclabel)smodule = {
    PyModuleDef_HEAD_INIT,
    "%(funclabel)s",
    NULL,
    -1,
    %(funclabel)s_methods
};

PyMODINIT_FUNC PyInit_%(funclabel)s(void)
{
    return PyModule_Create(&%(funclabel)smodule);
};

/*--------------------------------------------------------------------------- */

"""


# ==============================================================================


# ==============================================================================


# The SIMD operations used for each function.
# For x86-64.
vsimdop_x86 = {
'b' : {'abs_' : '__builtin_ia32_pabsb128(datasliceleft)', 'neg' : '__builtin_ia32_psignb128(datasliceleft, vsignparam)'},
'h' : {'abs_' : '__builtin_ia32_pabsw128(datasliceleft)', 'neg' : '__builtin_ia32_psignw128(datasliceleft, vsignparam)'},
'i' : {'abs_' : '__builtin_ia32_pabsd128(datasliceleft)', 'neg' : '__builtin_ia32_psignd128(datasliceleft, vsignparam)'},
}


# These are needed for neg for x86 only, as otherwise the vector literal just gets too long.
vsignparam_x86 = {
'b' : {'abs_' : '', 'neg' : 'v16qi vsignparam = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};'},
'h' : {'abs_' : '', 'neg' : 'v8hi vsignparam = {-1, -1, -1, -1, -1, -1, -1, -1};'},
'i' : {'abs_' : '', 'neg' : 'v4si vsignparam = {-1, -1, -1, -1};'},
}


# Various SIMD instruction information which varies according to array type.
# For x86-64.

simdattr_x86 = {
	'b' : 'v16qi', 
	'h' : 'v8hi', 
	'i' : 'v4si', 
}

vldinstr_x86 = {
	'b' : '(v16qi) __builtin_ia32_lddqu((char *) ', 
	'h' : '(v8hi) __builtin_ia32_lddqu((char *) ', 
	'i' : '(v4si) __builtin_ia32_lddqu((char *) ', 
}

vstinstr1_x86 = {
	'b' : '__builtin_ia32_storedqu((char *) ',
	'h' : '__builtin_ia32_storedqu((char *) ',
	'i' : '__builtin_ia32_storedqu((char *) ',
}

vstinstr2_x86 = {
	'b' : '',
	'h' : '(v16qi) ',
	'i' : '(v16qi) ',
}


# Total list of which array types are supported by x86 SIMD instructions.
SIMD_x86_support = simdattr_x86.keys()

# ==============================================================================


# For ARM NEON ARMv7 32 bit.
vsimdop_armv7 = {
'b' : {'abs_' : 'vabs_s8(datasliceleft)', 'neg' : 'vneg_s8(datasliceleft)'},
'h' : {'abs_' : 'vabs_s16(datasliceleft)', 'neg' : 'vneg_s16(datasliceleft)'},
'i' : {'abs_' : 'vabs_s32(datasliceleft)', 'neg' : 'vneg_s32(datasliceleft)'},
}

vsignparam_armv7 = {
'b' : {'abs_' : '', 'neg' : ''},
'h' : {'abs_' : '', 'neg' : ''},
'i' : {'abs_' : '', 'neg' : ''},
}



# For ARM NEON ARMv7 32 bit.
simdattr_armv7 = {
	'b' : 'int8x8_t', 
	'h' : 'int16x4_t', 
	'i' : 'int32x2_t', 
}


vldinstr_armv7 = {
	'b' : 'vld1_s8(', 
	'h' : 'vld1_s16(', 
	'i' : 'vld1_s32(', 
}

vstinstr1_armv7 = {
	'b' : 'vst1_s8(',
	'h' : 'vst1_s16(',
	'i' : 'vst1_s32(',
}

vstinstr2_armv7 = {
	'b' : '',
	'h' : '',
	'i' : '',
}

# Total list of which array types are supported by ARM SIMD instructions.
SIMD_armv7_support = simdattr_armv7.keys()



# ==============================================================================


# For ARM NEON armv8 64 bit.
vsimdop_armv8 = {
'b' : {'abs_' : 'vabsq_s8(datasliceleft)', 'neg' : 'vnegq_s8(datasliceleft)'},
'h' : {'abs_' : 'vabsq_s16(datasliceleft)', 'neg' : 'vnegq_s16(datasliceleft)'},
'i' : {'abs_' : 'vabsq_s32(datasliceleft)', 'neg' : 'vnegq_s32(datasliceleft)'},
'f' : {'abs_' : 'vabsq_f32(datasliceleft)', 'neg' : 'vnegq_f32(datasliceleft)'},
}

vsignparam_armv8 = {
'b' : {'abs_' : '', 'neg' : ''},
'h' : {'abs_' : '', 'neg' : ''},
'i' : {'abs_' : '', 'neg' : ''},
'f' : {'abs_' : '', 'neg' : ''},
}



# For ARM NEON armv8 64 bit.
simdattr_armv8 = {
	'b' : 'int8x16_t', 
	'h' : 'int16x8_t', 
	'i' : 'int32x4_t', 
	'f' : 'float32x4_t', 
}


vldinstr_armv8 = {
	'b' : 'vld1q_s8(', 
	'h' : 'vld1q_s16(', 
	'i' : 'vld1q_s32(', 
	'f' : 'vld1q_f32(', 
}

vstinstr1_armv8 = {
	'b' : 'vst1q_s8(',
	'h' : 'vst1q_s16(',
	'i' : 'vst1q_s32(',
	'f' : 'vst1q_f32(',
}

vstinstr2_armv8 = {
	'b' : '',
	'h' : '',
	'i' : '',
	'f' : '',
}

# Total list of which array types are supported by ARM SIMD instructions.
SIMD_armv8_support = simdattr_armv8.keys()


# ==============================================================================

# This is used to finish up array elements which were left over at the
# end of the SIMD operation.
simdcleanup = {'abs_' : 'data[index] >= 0 ? data[index] : -data[index]', 'neg' : '-data[index]'}


# Width of array elements.
simdwidth = {'b' : 'CHARSIMDSIZE',
		'B' : 'CHARSIMDSIZE',
		'h' : 'SHORTSIMDSIZE',
		'H' : 'SHORTSIMDSIZE',
		'i' : 'INTSIMDSIZE',
		'I' : 'INTSIMDSIZE',
		'f' : 'FLOATSIMDSIZE',
		}

# ==============================================================================

# These get substituted into function call templates.
SIMD_platform_x86 = '#if defined(AF_HASSIMD_X86)'
SIMD_platform_x86_ARM = '#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)'
SIMD_platform_x86_ARMv8 = '#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)'
SIMD_platform_ARMv7 = '#if defined(AF_HASSIMD_ARMv7_32BIT)'
SIMD_platform_ARM64v8 = '#if defined(AF_HASSIMD_ARM_AARCH64)'


# ==============================================================================

# Return the platform SIMD enable C macro. 
# This is for the platform independent file, and not the plaform specific
# SIMD files.
def findsimdplatform(arraycode):

	hasx86 = arraycode in SIMD_x86_support
	hasarmv7 = arraycode in SIMD_armv7_support
	hasarmv8 = arraycode in SIMD_armv8_support

	# Only the platforms combinations which are used currently are defined here.
	if hasx86 and hasarmv7 and hasarmv8:
		return SIMD_platform_x86_ARM
	elif hasx86 and (not hasarmv7) and (not hasarmv8):
		return SIMD_platform_x86
	elif hasx86 and (not hasarmv7) and hasarmv8:
		return SIMD_platform_x86_ARMv8
	elif (not hasx86) and (not hasarmv7) and hasarmv8:
		return SIMD_platform_ARM64v8
	else:
		return 'Error: Template error, this should not be here.'

# ==============================================================================

# Which opstemplate is valid for which operation. Each math operation requires
# different templates for signed int, unsigned int, and float.
opstemplates = {'neg' : uniops_neg_int,
			'abs_' : uniops_abs_int}

supportedtypes = (codegen_common.signedint + codegen_common.floatarrays)

# ==============================================================================

# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.

funclist = [x for x in oplist if x['c_code_template'] in ['template_uniop']]

# ==============================================================================


for func in funclist:

	# Function name.
	funcname = func['funcname']

	# Create the source code based on templates.
	filename = funcname + '.c'
	with open(filename, 'w') as f:
		funcdata = {'funclabel' : funcname}

		f.write(uniops_head % funcdata)
		opscalltext = []


		# Check each array type. The types of arrays supported must be looked up.
		for arraycode in supportedtypes:
			funcdata['funcmodifier'] = codegen_common.arraytypes[arraycode].replace(' ', '_')
			funcdata['arraytype'] = codegen_common.arraytypes[arraycode]
			funcdata['intminvalue'] = codegen_common.minvalue[arraycode]


			# Some array types have SIMD support.
			if arraycode in (set(SIMD_x86_support) | set(SIMD_armv7_support) | set(SIMD_armv8_support)):
				simd_call_vals = {'simdwidth' : simdwidth[arraycode], 
					'funclabel' : funcdata['funclabel'], 
					'funcmodifier' : funcdata['funcmodifier'],
					'simdplatform' : findsimdplatform(arraycode)}
				funcdata['simd_call'] = SIMD_call % simd_call_vals
			else:
				funcdata['simd_call'] = ''


			if arraycode == 'f':
				funcdata['copname'] = func['c_operator_f']
				ops_calc = uniops_op_float
			elif arraycode == 'd':
				funcdata['copname'] = func['c_operator_d']
				ops_calc = uniops_op_float
			elif arraycode in codegen_common.signedint:
				funcdata['copname'] = func['c_operator_i']
				ops_calc = opstemplates[funcname]
			else:
				print('Error - Unsupported array code.', arraycode)


			f.write(ops_calc % funcdata)

			# This is the call to the functions for this array type. This
			# is inserted into another template below.
			funcdata['arraycode'] = arraycode
			opscalltext.append(opscall % funcdata)


		supportedarrays = codegen_common.FormatDocsArrayTypes(func['arraytypes'])

		f.write(uniops_params % {'funclabel' : funcname, 
				'opcodedocs' : func['opcodedocs'], 
				'supportedarrays' : supportedarrays,
				'matherrors' : ', '.join(func['matherrors'].split(',')),
				'opscall' : ''.join(opscalltext)})

# ==============================================================================


# ==============================================================================

# This outputs the SIMD version for x86-64.
simdcodedate = '22-Mar-2019'
simdfilename = '_simd_x86'

# This outputs the SIMD version.

for func in funclist:

	outputlist = []

	funcname = func['funcname']

	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname


	# Output the generated code.
	for arraycode in SIMD_x86_support:

		arraytype = codegen_common.arraytypes[arraycode]

		# The compare_ops symbols is the same for integer and floating point.
		datavals = {'funclabel' : funcname,
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'simdwidth' : simdwidth[arraycode],
					'simdplatform' : SIMD_platform_x86,
					'simdop' : vsimdop_x86[arraycode][funcname],
					'vsignparam' : vsignparam_x86[arraycode][funcname],
					'simdcleanup' : simdcleanup[funcname],
					'simdattr' : simdattr_x86[arraycode],
					'vldinstr' : vldinstr_x86[arraycode],
					'vstinstr1' : vstinstr1_x86[arraycode],
					'vstinstr2' : vstinstr2_x86[arraycode],
					}


		# Start of function definition.
		outputlist.append(ops_simdsupport % datavals)



	# This outputs the SIMD version.
	codegen_common.OutputSourceCode(funcname + simdfilename + '.c', outputlist, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate,
		'', ['simddefs'])


	# Output the .h header file.
	headedefs = codegen_common.GenSIMDCHeaderText(outputlist, funcname)

	# Write out the file.
	codegen_common.OutputCHeader(funcname + simdfilename + '.h', headedefs, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate)

# ==============================================================================


# ==============================================================================

# This outputs the SIMD version for ARM NEON ARMv7 32 bit.

simdcodedate = '08-Oct-2019'
simdfilename = '_simd_armv7'

# This outputs the SIMD version.

for func in funclist:

	outputlist = []

	funcname = func['funcname']

	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname


	# Output the generated code.
	for arraycode in SIMD_armv7_support:

		arraytype = codegen_common.arraytypes[arraycode]

		# The compare_ops symbols is the same for integer and floating point.
		datavals = {'funclabel' : funcname,
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'simdwidth' : simdwidth[arraycode],
					'simdplatform' : SIMD_platform_ARMv7,
					'simdop' : vsimdop_armv7[arraycode][funcname],
					'vsignparam' : vsignparam_armv7[arraycode][funcname],
					'simdcleanup' : simdcleanup[funcname],
					'simdattr' : simdattr_armv7[arraycode],
					'vldinstr' : vldinstr_armv7[arraycode],
					'vstinstr1' : vstinstr1_armv7[arraycode],
					'vstinstr2' : vstinstr2_armv7[arraycode],
					}


		# Start of function definition.
		outputlist.append(ops_simdsupport % datavals)



	# This outputs the SIMD version.
	codegen_common.OutputSourceCode(funcname + simdfilename + '.c', outputlist, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate,
		'', ['simddefs', 'simdmacromsg_armv7'])


	# Output the .h header file.
	headedefs = codegen_common.GenSIMDCHeaderText(outputlist, funcname)

	# Write out the file.
	codegen_common.OutputCHeader(funcname + simdfilename + '.h', headedefs, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate)

# ==============================================================================


# ==============================================================================

# This outputs the SIMD version for ARM NEON ARMv8 64 bit.

simdcodedate = '25-Mar-2020'
simdfilename = '_simd_armv8'

# This outputs the SIMD version.

for func in funclist:

	outputlist = []

	funcname = func['funcname']

	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname


	# Output the generated code.
	for arraycode in SIMD_armv8_support:

		arraytype = codegen_common.arraytypes[arraycode]

		# The compare_ops symbols is the same for integer and floating point.
		datavals = {'funclabel' : funcname,
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'simdwidth' : simdwidth[arraycode],
					'simdplatform' : SIMD_platform_ARM64v8,
					'simdop' : vsimdop_armv8[arraycode][funcname],
					'vsignparam' : vsignparam_armv8[arraycode][funcname],
					'simdcleanup' : simdcleanup[funcname],
					'simdattr' : simdattr_armv8[arraycode],
					'vldinstr' : vldinstr_armv8[arraycode],
					'vstinstr1' : vstinstr1_armv8[arraycode],
					'vstinstr2' : vstinstr2_armv8[arraycode],
					}


		# Start of function definition.
		outputlist.append(ops_simdsupport % datavals)



	# This outputs the SIMD version.
	codegen_common.OutputSourceCode(funcname + simdfilename + '.c', outputlist, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate,
		'', ['simddefs', 'simdmacromsg_armv8'])


	# Output the .h header file.
	headedefs = codegen_common.GenSIMDCHeaderText(outputlist, funcname)

	# Write out the file.
	codegen_common.OutputCHeader(funcname + simdfilename + '.h', headedefs, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate)

# ==============================================================================
