#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for math functions which accept a single 
#			parameter.
# Language: Python 3.4
# Date:     08-Dec-2017
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

mathfunc1_template = """//------------------------------------------------------------------------------
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
%(MSVSCcompat)s
#include <math.h>

#include "arrayerrs.h"
#include "arrayparams_base.h"

%(includeoptions)s

%(arithcalcs)s

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int %(funclabel)s_float(Py_ssize_t arraylen,%(nosimddecl)s float *data, float *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


%(simd_call_f)s
	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = %(floatfunc)s;
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = %(floatfunc)s;
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = %(floatfunc)s;
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = %(floatfunc)s;
				if (!isfinite(data[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
	}

	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int %(funclabel)s_double(Py_ssize_t arraylen,%(nosimddecl)s double *data, double *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


%(simd_call_d)s
	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {
			for (x = 0; x < arraylen; x++) {
				dataout[x] = %(doublefunc)s;
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = %(doublefunc)s;
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {
			for (x = 0; x < arraylen; x++) {
				dataout[x] = %(doublefunc)s;
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = %(doublefunc)s;
				if (!isfinite(data[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
	}
	return ARR_NO_ERR;

}

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
		// float
		case 'f' : {
			resultcode = %(funclabel)s_float(arraydata.arraylength,%(nosimdparam)s arraydata.array1.f, arraydata.array2.f, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}
		// double
		case 'd' : {
			resultcode = %(funclabel)s_double(arraydata.arraylength,%(nosimdparam)s arraydata.array1.d, arraydata.array2.d, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}
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
%(helpsimd1)s\\n\\
\\n\\
* array1 - The first input data array to be examined. If no output \\n\\
  array is provided the results will overwrite the input data. \\n\\
* outparray - The output array. This parameter is optional. \\n\\
* maxlen - Limit the length of the array used. This must be a valid  \\n\\
  positive integer. If a zero or negative length, or a value which is \\n\\
  greater than the actual length of the array is specified, this \\n\\
  parameter is ignored. \\n\\
* matherrors - If true, arithmetic error checking is disabled. The \\n\\
  default is false. \\n\\
%(helpsimd2)s");


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
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(simdload)s(&data[x]);
		// The actual SIMD operation. 
		datasliceleft = %(simdop)s;
		// Store the result.
		%(simdstore)s(&data[x], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data[x] = %(simdcleanup)s;
	}

}



// param_arr_arr
void %(funclabel)s_%(funcmodifier)s_2_simd(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(simdload)s(&data[x]);
		// The actual SIMD operation. 
		datasliceleft = %(simdop)s;
		// Store the result.
		%(simdstore)s(&dataout[x], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		dataout[x] = %(simdcleanup)s;
	}

}
#endif

"""

# ==============================================================================


# ==============================================================================

# This has to somehow handle both x86 and ARM, which have different occurances.
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



# The following are used to fill in template data which handles whether
# a function requires SIMD related template data or not. 
helpsimd1_template = '    %(funclabel)s(array, nosimd=False) \\n\\'

helpsimd2_template = '''* nosimd - If True, SIMD acceleration is disabled. This parameter is \\n\\
  optional. The default is FALSE.  \\n\\\n'''


# ==============================================================================

# Constants to use for degrees to radians and radians to degrees.
degtorad = """
/*--------------------------------------------------------------------------- */

// Used to calculate degrees to radians.
#define DEGTORAD_D M_PI / 180.0
#define DEGTORAD_F (float) (M_PI / 180.0)

/*--------------------------------------------------------------------------- */
"""

radtodeg = """
/*--------------------------------------------------------------------------- */

// Used to calculate radians to degrees.
#define RADTODEG_D 180.0 / M_PI
#define RADTODEG_F (float) (180.0 / M_PI)

/*--------------------------------------------------------------------------- */
"""


# Constants to use for degrees to radians and radians to degrees in vector format.
degtorad_vec_x86 = """
/*--------------------------------------------------------------------------- */

#ifdef AF_HASSIMD_X86
// Used to calculate degrees to radians for x86-64.
const v2df DEGTORAD_D_VEC = {DEGTORAD_D, DEGTORAD_D};
const v4sf DEGTORAD_F_VEC = {DEGTORAD_F, DEGTORAD_F, DEGTORAD_F, DEGTORAD_F};
#endif

/*--------------------------------------------------------------------------- */
"""

degtorad_vec_armv7 = """
/*--------------------------------------------------------------------------- */

#ifdef AF_HASSIMD_ARMv7_32BIT
// Used to calculate degrees to radians for ARM NEON for 32 bit ARMv7.
const float32x2_t DEGTORAD_F_VEC = {DEGTORAD_F, DEGTORAD_F};
#endif

/*--------------------------------------------------------------------------- */
"""

degtorad_vec_armv8 = """
/*--------------------------------------------------------------------------- */

#ifdef AF_HASSIMD_ARM_AARCH64
// Used to calculate degrees to radians for ARM NEON for 64 bit ARMv8.
const float32x4_t DEGTORAD_F_VEC = {DEGTORAD_F, DEGTORAD_F, DEGTORAD_F, DEGTORAD_F};
#endif

/*--------------------------------------------------------------------------- */
"""


radtodeg_vec_x86 = """
/*--------------------------------------------------------------------------- */

#ifdef AF_HASSIMD_X86
// Used to calculate radians to degrees in vector format for x86-64.
const v2df RADTODEG_D_VEC = {RADTODEG_D, RADTODEG_D};
const v4sf RADTODEG_F_VEC = {RADTODEG_F, RADTODEG_F, RADTODEG_F, RADTODEG_F};
#endif

/*--------------------------------------------------------------------------- */
"""

radtodeg_vec_armv7 = """
/*--------------------------------------------------------------------------- */

#ifdef AF_HASSIMD_ARMv7_32BIT
// Used to calculate radians to degrees in vector format ARM NEON for 32 bit ARMv7.
const float32x2_t RADTODEG_F_VEC = {RADTODEG_F, RADTODEG_F};
#endif

/*--------------------------------------------------------------------------- */
"""

radtodeg_vec_armv8 = """
/*--------------------------------------------------------------------------- */

#ifdef AF_HASSIMD_ARM_AARCH64
// Used to calculate radians to degrees in vector format ARM NEON for 64 bit ARMv8.
const float32x4_t RADTODEG_F_VEC = {RADTODEG_F, RADTODEG_F, RADTODEG_F, RADTODEG_F};
#endif

/*--------------------------------------------------------------------------- */
"""


degrad = {'degrees' : radtodeg, 'radians' : degtorad}

degrad_vec_x86 = {'degrees' : radtodeg_vec_x86, 'radians' : degtorad_vec_x86}

degrad_vec_armv7 = {'degrees' : radtodeg_vec_armv7, 'radians' : degtorad_vec_armv7}
degrad_vec_armv8 = {'degrees' : radtodeg_vec_armv8, 'radians' : degtorad_vec_armv8}


# For MSVS compatibility for Windows.
MSVSCmath = """
// This _USE_MATH_DEFINES is required for MSVC 2010 compatibility to enable
// the M_PI constant. This must be immediately above <math.h>.
#define _USE_MATH_DEFINES
#include <math.h>

"""

degradmsvc = {'degrees' : MSVSCmath, 'radians' : MSVSCmath}

# ==============================================================================

# Functions without SIMD.
includeoptions_nosimd = '#include "arrayparams_one.h"'

# Functions with both x86 and ARM SIMD.
includeoptions_simd_x86_arm = '''#include "arrayparams_onesimd.h"

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
#endif'''

# Funcitons with x86 only SIMD.
includeoptions_simd_x86 = '''#include "arrayparams_onesimd.h"

#include "simddefs.h"

#ifdef AF_HASSIMD_X86
#include "%(funclabel)s_simd_x86.h"
#endif'''


# ==============================================================================

# This provides tje correct template for the C library function or
# C operator equation for the appropriate style of function.
cfunctmpl = {'template_mathfunc_1' : '%(c_operator)s(data[x])',
	'template_mathfunc_1simd' : '%(c_operator)s(data[x])',
	'template_mathfunc_1s' : '%(c_operator)s'
}

# ==============================================================================


# Various SIMD instruction information which varies according to array type.
simdvalues_x86 = {
'f' : {'simdattr' : 'v4sf', 'simdload' : '__builtin_ia32_loadups', 'simdstore' : '__builtin_ia32_storeups'},
'd' : {'simdattr' : 'v2df', 'simdload' : '__builtin_ia32_loadupd', 'simdstore' : '__builtin_ia32_storeupd'},
}


# The SIMD operations used for each function for x86-64.
simdop_x86 = {
'f' : {'ceil' : '__builtin_ia32_roundps (datasliceleft, 0b10)', 
		'floor' : '__builtin_ia32_roundps (datasliceleft, 0b01)',
		'trunc' : '__builtin_ia32_roundps (datasliceleft, 0b11)',
		'degrees' : '__builtin_ia32_mulps (datasliceleft, RADTODEG_F_VEC)',
		'radians' : '__builtin_ia32_mulps (datasliceleft, DEGTORAD_F_VEC)',
		'sqrt' : '__builtin_ia32_sqrtps(datasliceleft)',
		},
'd' : {'ceil' : '__builtin_ia32_roundpd (datasliceleft, 0b10)', 
		'floor' : '__builtin_ia32_roundpd (datasliceleft, 0b01)',
		'trunc' : '__builtin_ia32_roundpd (datasliceleft, 0b11)',
		'degrees' : '__builtin_ia32_mulpd (datasliceleft, RADTODEG_D_VEC)',
		'radians' : '__builtin_ia32_mulpd (datasliceleft, DEGTORAD_D_VEC)',
		'sqrt' : '__builtin_ia32_sqrtpd(datasliceleft)',
		},
}


# Which functions support x86 SIMD.
x86_simdfuncnames = set(itertools.chain.from_iterable([x.keys() for x in simdop_x86.values()]))
SIMD_x86_support = simdop_x86.keys()

# ==============================================================================

# This is the ARM version. This is for single precision float only.
simdvalues_armv7 = {'simdattr' : 'float32x2_t', 'simdload' : 'vld1_f32', 'simdstore' : 'vst1_f32'}


# The SIMD operations used for each function for ARM NEON.
# This currently covers ARMv7 only.
simdop_armv7 = {'degrees' : 'vmul_f32 (datasliceleft, RADTODEG_F_VEC)',
		'radians' : 'vmul_f32 (datasliceleft, DEGTORAD_F_VEC)',
		}

# Which functions support ARM SIMD.
armv7_simdfuncnames = list(simdop_armv7.keys())

SIMD_armv7_support = ('f', )

# ==============================================================================

# This is the ARM version. This is for single precision float only.
simdvalues_armv8 = {'simdattr' : 'float32x4_t', 'simdload' : 'vld1q_f32', 'simdstore' : 'vst1q_f32'}


# The SIMD operations used for each function for ARM NEON.
# This currently covers ARMv7 only.
simdop_armv8 = {'degrees' : 'vmulq_f32 (datasliceleft, RADTODEG_F_VEC)',
		'radians' : 'vmulq_f32 (datasliceleft, DEGTORAD_F_VEC)',
		}

# Which functions support ARM SIMD.
armv8_simdfuncnames = list(simdop_armv8.keys())

SIMD_armv8_support = ('f', )

# ==============================================================================

# SIMD width depends on array type.
simdwidth = {'f' : 'FLOATSIMDSIZE', 'd' : 'DOUBLESIMDSIZE'}


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
def findsimdplatform(arraycode, funcname):

	hasx86 = (arraycode in SIMD_x86_support) and (funcname in x86_simdfuncnames)
	hasarmv7 = arraycode in SIMD_armv7_support and (funcname in armv7_simdfuncnames)
	hasarmv8 = arraycode in SIMD_armv8_support and (funcname in armv8_simdfuncnames)

	# Only the platforms combinations which are used currently are defined here.
	if hasx86 and hasarmv7 and hasarmv8:
		return SIMD_platform_x86_ARM
	elif hasx86 and (not hasarmv7) and (not hasarmv8):
		return SIMD_platform_x86
	elif hasx86 and (not hasarmv7) and hasarmv8:
		return SIMD_platform_x86_ARMv8
	else:
		return 'Error: Template error, this should not be here.'


# ==============================================================================

# Return the include options, which depend on the function name.
def findincludeoptions(funcname):

	hasx86 = funcname in x86_simdfuncnames
	hasarmv7 = funcname in armv7_simdfuncnames
	hasarmv8 = funcname in armv8_simdfuncnames

	if hasx86 and (hasarmv7 or hasarmv8):
		return includeoptions_simd_x86_arm % {'funclabel' : funcname}
	elif hasx86 and not(hasarmv7 or hasarmv8):
		return includeoptions_simd_x86 % {'funclabel' : funcname}
	else:
		return 'Error - funcs1_codegen simd support selection error.'


# ==============================================================================

# ==============================================================================

# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.
funclist = [x for x in oplist if x['c_code_template'] in ('template_mathfunc_1', 'template_mathfunc_1s', 'template_mathfunc_1simd')]

simdlist = [x for x in funclist if x['c_code_template'] in ('template_mathfunc_1s', 'template_mathfunc_1simd')]

# ==============================================================================

for func in funclist:

	funcname = func['funcname']
	filename = funcname + '.c'


	c_code_template = func['c_code_template']

	# This flags which templates support SIMD.
	hassimd = c_code_template in ('template_mathfunc_1s', 'template_mathfunc_1simd')


	# Template data for functions with SIMD.
	if hassimd:
		nosimdparam = ' arraydata.nosimd,'
		nosimddecl = ' int nosimd,'
		helpsimd1 = helpsimd1_template % {'funclabel' : funcname}
		helpsimd2 = helpsimd2_template

		# ARM NEON does not support all the same functions as x86 SIMD.
		# We assume that if the function supports ARM NEON, then it
		# also supports x86 SIMD.
		includeoptions = findincludeoptions(funcname)

		# For single precision floating point.
		arraytype = codegen_common.arraytypes['f']
		simdfunccall = {'simdwidth' : simdwidth['f'], 
			'funclabel' : funcname,
			'funcmodifier' : arraytype.replace(' ', '_'),
			'simdplatform' : findsimdplatform('f', funcname)}
		simd_call_f = SIMD_call % simdfunccall

		# For double precision floating point.
		arraytype = codegen_common.arraytypes['d']
		simdfunccall = {'simdwidth' : simdwidth['d'], 
			'funclabel' : funcname,
			'funcmodifier' : arraytype.replace(' ', '_'),
			'simdplatform' : SIMD_platform_x86}
		simd_call_d = SIMD_call % simdfunccall


	else:
		nosimdparam = ''
		nosimddecl = ''
		helpsimd1 = ''
		helpsimd2 = ''
		simd_call_f = ''
		simd_call_d = ''
		includeoptions = includeoptions_nosimd


	# Get the correct C template for the calculation, filled out for the appropriate type. 
	floatfunc = cfunctmpl.get(c_code_template) % {'c_operator' : func['c_operator_f']}
	doublefunc = cfunctmpl.get(c_code_template) % {'c_operator' : func['c_operator_d']}


	supportedarrays = codegen_common.FormatDocsArrayTypes(func['arraytypes'])

	funcdata = {'funclabel' : funcname, 
			'funcfloatname' : func['c_operator_f'], 
			'funcdoublename' : func['c_operator_d'],
			'nosimdparam' : nosimdparam,
			'nosimddecl' : nosimddecl,
			'floatfunc' : floatfunc, 
			'doublefunc' : doublefunc,
			'opcodedocs' : func['opcodedocs'], 
			'supportedarrays' : supportedarrays,
			'matherrors' : ', '.join(func['matherrors'].split(',')),
			'arithcalcs' : degrad.get(funcname, ''),
			'MSVSCcompat' : degradmsvc.get(funcname, ''),
			'includeoptions' : includeoptions,
			'simd_call_f' : simd_call_f,
			'simd_call_d' : simd_call_d,
			'helpsimd1' : helpsimd1,
			'helpsimd2' : helpsimd2,
			}	


	with open(filename, 'w') as f:
		f.write(mathfunc1_template % funcdata)


# ==============================================================================



# The original date of the SIMD C code.
simdcodedate = '24-Mar-2019'
simdfilename = '_simd_x86'

# This outputs the SIMD version for x86-64.

for func in simdlist:

	outputlist = []

	funcname = func['funcname']
	c_code_template = func['c_code_template']

	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname

	# Add the additional math and constant information required for
	# degrees and radians.
	outputlist.append(degradmsvc.get(funcname, ''))
	outputlist.append(degrad.get(funcname, ''))
	outputlist.append(degrad_vec_x86.get(funcname, ''))


	# Get the correct C template for the calculation, filled out for the appropriate type. 
	floatfunc = cfunctmpl.get(c_code_template) % {'c_operator' : func['c_operator_f']}
	doublefunc = cfunctmpl.get(c_code_template) % {'c_operator' : func['c_operator_d']}


	# Output the generated code.
	for arraycode in codegen_common.floatarrays:

		arraytype = codegen_common.arraytypes[arraycode]

		if arraycode == 'f':
			c_operator = floatfunc % {'c_operator' : func['c_operator_f']}
		else:
			c_operator = doublefunc % {'c_operator' : func['c_operator_d']}



		# The compare_ops symbols is the same for integer and floating point.
		datavals = {'funclabel' : funcname,
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'arraycode' : arraycode,
					'arraytype' : codegen_common.arraytypes[arraycode],
					'simdop' : simdop_x86[arraycode][funcname],
					'simdcleanup' : c_operator,
					'simdplatform' : SIMD_platform_x86,
					'simdwidth' : simdwidth[arraycode],
					}


		# Start of function definition.
		datavals.update(simdvalues_x86[arraycode])
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


# The original date of the SIMD C code.
simdcodedate = '02-Oct-2019'
simdfilename = '_simd_armv7'

# This outputs the SIMD version for ARM NEON ARMv7 32 bit.

armsimdlist = [x for x in simdlist if x['funcname'] in armv7_simdfuncnames]


for func in armsimdlist:
	
	outputlist = []

	funcname = func['funcname']
	c_code_template = func['c_code_template']

	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname

	# Add the additional math and constant information required for
	# degrees and radians.
	outputlist.append(degradmsvc.get(funcname, ''))
	outputlist.append(degrad.get(funcname, ''))
	outputlist.append(degrad_vec_armv7.get(funcname, ''))


	# Get the correct C template for the calculation, filled out for the appropriate type. 
	floatfunc = cfunctmpl.get(c_code_template) % {'c_operator' : func['c_operator_f']}


	# Output the generated code.
	arraycode = 'f'

	arraytype = codegen_common.arraytypes[arraycode]

	c_operator = floatfunc % {'c_operator' : func['c_operator_f']}


	# The compare_ops symbols is the same for integer and floating point.
	datavals = {'funclabel' : funcname,
				'arraytype' : arraytype, 
				'funcmodifier' : arraytype.replace(' ', '_'),
				'arraycode' : arraycode,
				'arraytype' : codegen_common.arraytypes[arraycode],
				'simdop' : simdop_armv7[funcname],
				'simdcleanup' : c_operator,
				'simdplatform' : SIMD_platform_ARMv7,
				'simdwidth' : simdwidth['f'],
				}
				

	# Start of function definition.
	datavals.update(simdvalues_armv7)
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



# The original date of the SIMD C code.
simdcodedate = '26-Mar-2020'
simdfilename = '_simd_armv8'

# This outputs the SIMD version for ARM NEON ARMv8 64 bit.

armsimdlist = [x for x in simdlist if x['funcname'] in armv8_simdfuncnames]


for func in armsimdlist:
	
	outputlist = []

	funcname = func['funcname']
	c_code_template = func['c_code_template']

	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname

	# Add the additional math and constant information required for
	# degrees and radians.
	outputlist.append(degradmsvc.get(funcname, ''))
	outputlist.append(degrad.get(funcname, ''))
	outputlist.append(degrad_vec_armv8.get(funcname, ''))


	# Get the correct C template for the calculation, filled out for the appropriate type. 
	floatfunc = cfunctmpl.get(c_code_template) % {'c_operator' : func['c_operator_f']}


	# Output the generated code.
	arraycode = 'f'

	arraytype = codegen_common.arraytypes[arraycode]

	c_operator = floatfunc % {'c_operator' : func['c_operator_f']}


	# The compare_ops symbols is the same for integer and floating point.
	datavals = {'funclabel' : funcname,
				'arraytype' : arraytype, 
				'funcmodifier' : arraytype.replace(' ', '_'),
				'arraycode' : arraycode,
				'arraytype' : codegen_common.arraytypes[arraycode],
				'simdop' : simdop_armv8[funcname],
				'simdcleanup' : c_operator,
				'simdplatform' : SIMD_platform_ARM64v8,
				'simdwidth' : simdwidth['f'],
				}
				

	# Start of function definition.
	datavals.update(simdvalues_armv8)
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
