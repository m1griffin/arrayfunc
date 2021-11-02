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

mathops_head = """//------------------------------------------------------------------------------
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

"""

# ==============================================================================

ops_template = """
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


%(simdplatform)s
	signed int errorstate;

	// SIMD version. 
	if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			if (hasoutputarray) {		
				%(funclabel)s_%(funcmodifier)s_2_simd(arraylen, data, dataout);
			} else {
				%(funclabel)s_%(funcmodifier)s_1_simd(arraylen, data);
			}
		} else {
		// Math error checking enabled.
			if (hasoutputarray) {		
				errorstate = %(funclabel)s_%(funcmodifier)s_2_simd_ovfl(arraylen, data, dataout);
				if (errorstate) {return ARR_ERR_ARITHMETIC;}
			} else {
				errorstate = %(funclabel)s_%(funcmodifier)s_1_simd_ovfl(arraylen, data);
				if (errorstate) {return ARR_ERR_ARITHMETIC;}
			}
		}

	} else {
#endif

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

%(simdplatform)s
	}
#endif

	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */

"""

# ==============================================================================

mathops_params = """
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
			resultcode = %(funclabel)s_float(arraydata.arraylength, arraydata.nosimd, arraydata.array1.f, arraydata.array2.f, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}
		// double
		case 'd' : {
			resultcode = %(funclabel)s_double(arraydata.arraylength, arraydata.nosimd, arraydata.array1.d, arraydata.array2.d, arraydata.ignoreerrors, arraydata.hasoutputarray);
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
    %(funclabel)s(array, nosimd=False) \\n\\
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
* nosimd - If True, SIMD acceleration is disabled. This parameter is \\n\\
  optional. The default is FALSE.  \\n\\\n\\
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
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

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
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

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

# The operations using SIMD.
ops_simdsupport_ovfl = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   Returns 1 if overflow occurred, else returns 0.
*/
// param_arr_none
%(simdplatform)s
char %(funclabel)s_%(funcmodifier)s_1_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, checkslice;

	%(arraytype)s checkvecresults[%(simdwidth)s];
	%(arraytype)s checksliceinit[%(simdwidth)s] = {0.0};


	// This is used to check for errors by accumulating non-finite values.
	checkslice = %(simdload)s (checksliceinit);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(simdload)s(&data[x]);
		// The actual SIMD operation. 
		datasliceleft = %(simdop)s;
		// Store the result.
		%(simdstore)s(&data[x], datasliceleft);

		// Check the result. None-finite errors should accumulate.
		checkslice = %(simdmul)s(checkslice, datasliceleft);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	%(simdstore)s (checkvecresults, checkslice);
	for (x = 0; x < %(simdwidth)s; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data[x] = %(simdcleanup)s;
		if (!isfinite(data[x])) {return 1;}
	}

	// Everything was OK.
	return 0;

}



// param_arr_arr
char %(funclabel)s_%(funcmodifier)s_2_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, checkslice;

	%(arraytype)s checkvecresults[%(simdwidth)s];
	%(arraytype)s checksliceinit[%(simdwidth)s] = {0.0};


	// This is used to check for errors by accumulating non-finite values.
	checkslice = %(simdload)s (checksliceinit);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(simdload)s(&data[x]);
		// The actual SIMD operation. 
		datasliceleft = %(simdop)s;
		// Store the result.
		%(simdstore)s(&dataout[x], datasliceleft);

		// Check the result. None-finite errors should accumulate.
		checkslice = %(simdmul)s(checkslice, datasliceleft);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	%(simdstore)s (checkvecresults, checkslice);
	for (x = 0; x < %(simdwidth)s; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		dataout[x] = %(simdcleanup)s;
		if (!isfinite(dataout[x])) {return 1;}
	}

	// Everything was OK.
	return 0;

}
#endif

"""


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


# Multiplication, used for checking for math errors.
simdmulop_x86 = {'f' : '__builtin_ia32_mulps', 
				'd' : '__builtin_ia32_mulpd'}


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

# Multiplication, used for checking for math errors.
simdmulop_armv7 = 'vmul_f32'

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

# Multiplication, used for checking for math errors.
simdmulop_armv8 = 'vmulq_f32'

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
opdata = codegen_common.ReadINI('affuncdata.ini')

# Filter out the desired math functions.
funclist = [(x,dict(y)) for x,y in opdata.items() if y.get('c_code_template') in ('template_mathfunc_1s', 'template_mathfunc_1simd')]


# ==============================================================================


def CreateHeader(funcname):
	''' The header and related code. This is returned as a block of text.
	'''
	funcdata = {'funclabel' : funcname, 
				'includeoptions' : findincludeoptions(funcname),
				'MSVSCcompat' : degradmsvc.get(funcname, ''),
				'arithcalcs' : degrad.get(funcname, ''),
				}


	headtext = mathops_head % funcdata


	return headtext

# ==============================================================================

def CreateCallCCode(arraycode, funcname, func):
	''' Conventional C code for a single data type.
	This covers the C code for the non-SIMD operations as well as
	the calls to the SIMD functions.
	This returns the data to be written later.
	It returns as a block of text.
	'''
	arraytype = codegen_common.arraytypes[arraycode]
	funcmodifier = arraytype.replace(' ', '_')

	# Get the correct C template for the calculation, filled out for the appropriate type. 
	c_code_template = func['c_code_template']

	if arraycode == 'f':
		copfunc = cfunctmpl.get(c_code_template) % {'c_operator' : func['c_operator_f']}
	else:
		copfunc = cfunctmpl.get(c_code_template) % {'c_operator' : func['c_operator_d']}

	funcdata = {'funclabel' : funcname, 
			'funcmodifier' : funcmodifier,
			'arraytype' : arraytype,
			'arraycode' : arraycode,
			'simdwidth' : simdwidth[arraycode], 
			'simdplatform' : findsimdplatform(arraycode, funcname),
			'copname' : copfunc,
			}

	return ops_template % funcdata


# ==============================================================================

def CreateParamBlock(funcname, funcdata):
	'''This code handles getting the parameters and then calling the
	code which does the calculations.
	
	'''
	supportedarrays = codegen_common.FormatDocsArrayTypes(func['arraytypes'])

	funcdata = {'funclabel' : funcname, 
			'matherrors' : ', '.join(func['matherrors'].split(',')),
			'opcodedocs' : func['opcodedocs'], 
			'supportedarrays' : supportedarrays,
			}

	return mathops_params % funcdata


# ==============================================================================


# Create the SIMD code.
def CreateSIMDCode(arraycode, simdplatform, funcname, func, SIMDdata, simdop, simdmul):
	'''Create the SIMD code. This will go in a separate set of files
	from the main code file.
	The results are returned as a block of text.
	'''
	arraytype = codegen_common.arraytypes[arraycode]
	funcmodifier = arraytype.replace(' ', '_')

	# Get the correct C template for the calculation, filled out for the appropriate type. 
	c_code_template = func['c_code_template']

	# Get the correct C template for the calculation, filled out for the appropriate type. 
	if arraycode == 'f':
		copfunc = cfunctmpl.get(c_code_template) % {'c_operator' : func['c_operator_f']}
	else:
		copfunc = cfunctmpl.get(c_code_template) % {'c_operator' : func['c_operator_d']}

	# Select the correct SIMD platform for this file. Each file is specific
	# to one plaform type.
	platformoptions = {
	'x86' : SIMD_platform_x86,
	'armv7' : SIMD_platform_ARMv7,
	'armv8' : SIMD_platform_ARM64v8,
	}

	funcdata = {'funclabel' : funcname, 
			'funcmodifier' : funcmodifier,
			'arraytype' : arraytype,
			'arraycode' : arraycode,
			'simdwidth' : simdwidth[arraycode], 
			'simdplatform' : platformoptions[simdplatform],
			'simdattr' : SIMDdata['simdattr'],
			'simdload' : SIMDdata['simdload'],
			'simdstore' : SIMDdata['simdstore'],
			'simdmul' : simdmul,
			'simdop' : simdop[funcname],
			'simdcleanup' : copfunc,
			}
	
	ops = ops_simdsupport % funcdata
	ops_ovfl = ops_simdsupport_ovfl % funcdata

	return ops + ops_ovfl



# ==============================================================================


def WriteSIMDCode(funcname, simdplatform, simdfilename, simdcodedate, outputlist):
	'''This writes out the SIMD code to the .c and .h files.
	'''
	# The SIMD options to select the additional file header info.
	simdoptions = {
	'x86' : ['simddefs'],
	'armv7' : ['simddefs', 'simdmacromsg_armv7'],
	'armv8' : ['simddefs', 'simdmacromsg_armv8'],
	}


	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname

	# This outputs the SIMD version.
	codegen_common.OutputSourceCode(funcname + simdfilename + '.c', outputlist, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate,
		'', simdoptions[simdplatform])


	# Output the .h header file.
	headedefs = codegen_common.GenSIMDCHeaderText(outputlist, funcname)

	# Write out the file.
	codegen_common.OutputCHeader(funcname + simdfilename + '.h', headedefs, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate)


# ==============================================================================


# Create the files for each function.
for funcname, func in funclist:

	# Accumulate the blocks of text.
	textblock = list()

	# The text at the top of the main file, including the copyright notice
	# and include statements.
	headtext = CreateHeader(funcname)
	textblock.append(headtext)

	# The actual math functions.
	for arraycode in codegen_common.floatarrays:
		copstext = CreateCallCCode(arraycode, funcname, func)
		textblock.append(copstext)

	# The parameter parsing, dispatching, help text, and extension boilerplate.
	paramtext = CreateParamBlock(funcname, func)
	textblock.append(paramtext)

	# Write out the main file.
	filename = funcname + '.c'
	with open(filename, 'w') as f:
		f.write(''.join(textblock))


	# SIMD Files.

	# Add the additional math and constant information required for
	# degrees and radians.
	arithcalcs = degradmsvc.get(funcname, '') + degrad.get(funcname, '')

	# For x86_64.
	simdtextblock = list()
	simdtextblock.append(arithcalcs)
	simdtextblock.append(degrad_vec_x86.get(funcname, ''))

	for arraycode in codegen_common.floatarrays:
		simdtext = CreateSIMDCode(arraycode, 'x86', funcname, func, simdvalues_x86[arraycode], simdop_x86[arraycode], simdmulop_x86[arraycode])
		simdtextblock.append(simdtext)

	# Write out the SIMD file.
	simdcodedate = '24-Mar-2019'
	simdfilename = '_simd_x86'
	WriteSIMDCode(funcname, 'x86', simdfilename, simdcodedate, simdtextblock)

	# For ARMv7.
	if funcname in armv7_simdfuncnames:
		simdtextblock = list()

		simdtextblock.append(arithcalcs)
		simdtextblock.append(degrad_vec_armv7.get(funcname, ''))

		simdtext = CreateSIMDCode('f', 'armv7', funcname, func, simdvalues_armv7, simdop_armv7, simdmulop_armv7)
		simdtextblock.append(simdtext)

		# Write out the SIMD file.
		simdcodedate = '02-Oct-2019'
		simdfilename = '_simd_armv7'
		WriteSIMDCode(funcname, 'armv7', simdfilename, simdcodedate, simdtextblock)


	# For ARMv8.
	if funcname in armv8_simdfuncnames:
		simdtextblock = list()

		simdtextblock.append(arithcalcs)
		simdtextblock.append(degrad_vec_armv8.get(funcname, ''))

		simdtext = CreateSIMDCode('f', 'armv8', funcname, func, simdvalues_armv8, simdop_armv8, simdmulop_armv8)
		simdtextblock.append(simdtext)

		# Write out the SIMD file.
		simdcodedate = '26-Mar-2020'
		simdfilename = '_simd_armv8'
		WriteSIMDCode(funcname, 'armv8', simdfilename, simdcodedate, simdtextblock)


# ==============================================================================

