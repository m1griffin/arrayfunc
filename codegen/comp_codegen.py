#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for math operations. 
# Language: Python 3.4
# Date:     30-Dec-2017
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
#include <math.h>

#include "arrayerrs.h"

#include "arrayparams_base.h"

#include "arrayparams_comp.h"

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

# The actual compare operations (non-SIMD).
ops_comp = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
char %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data1, %(arraytype)s param) {

	// array index counter.
	Py_ssize_t x;
%(simd_call_1)s
	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] %(copname)s param)) { return 0; }
	}

	return 1;

}


// param_num_arr
char %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, int nosimd, %(arraytype)s param, %(arraytype)s *data2) {

	// array index counter.
	Py_ssize_t x;
%(simd_call_3)s
	for (x = 0; x < arraylen; x++) {
		if (!(param %(copname)s data2[x])) { return 0; }
	}

	return 1;

}


// param_arr_arr
char %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data1, %(arraytype)s *data2) {

	// array index counter.
	Py_ssize_t x;
%(simd_call_5)s
	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] %(copname)s data2[x])) { return 0; }
	}

	return 1;

}

"""


# ==============================================================================


# ==============================================================================




# The actual compare operations using SIMD operations for x86-64.
ops_simdsupport_x86 = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num for array code: %(arraycode)s
#if defined(AF_HASSIMD_X86)
char %(funclabel)s_%(funcmodifier)s_1_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright;
	%(simdattr)s resultslice%(SIMD_x86_compslice)s;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param;
	}
	datasliceright = %(vldinstr)s compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		datasliceleft = %(vldinstr)s &data1[index]);
		%(SIMD_x86_arr_num)s
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] %(compare_ops)s param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char %(funclabel)s_%(funcmodifier)s_3_simd(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright;
	%(simdattr)s resultslice%(SIMD_x86_compslice)s;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param;
	}
	datasliceleft = %(vldinstr)s compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		datasliceright = %(vldinstr)s &data2[index]);
		%(SIMD_x86_num_arr)s
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(param %(compare_ops)s data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char %(funclabel)s_%(funcmodifier)s_5_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright;
	%(simdattr)s resultslice%(SIMD_x86_compslice)s;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		datasliceleft = %(vldinstr)s &data1[index]);
		datasliceright = %(vldinstr)s &data2[index]);
		%(SIMD_x86_arr_arr)s
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] %(compare_ops)s data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif

/*--------------------------------------------------------------------------- */

"""


# The actual compare operations using SIMD operations for ARMv7 NEON 32 bit.
ops_simdsupport_armv7 = """

/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#if defined(AF_HASSIMD_ARMv7_32BIT)
char %(funclabel)s_%(funcmodifier)s_1_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright;
	%(simdrsltattr)s resultslice;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param;
	}
	datasliceright = %(vldinstr)s( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		datasliceleft = %(vldinstr)s( &data1[index]);
		// The actual SIMD operation. 
		resultslice = %(SIMD_ARM_comp)s(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(%(vresult)s)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] %(compare_ops)s param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char %(funclabel)s_%(funcmodifier)s_3_simd(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright;
	%(simdrsltattr)s resultslice;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param;
	}
	datasliceleft = %(vldinstr)s( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		datasliceright = %(vldinstr)s( &data2[index]);
		// The actual SIMD operation. 
		resultslice = %(SIMD_ARM_comp)s(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(%(vresult)s)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(param %(compare_ops)s data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char %(funclabel)s_%(funcmodifier)s_5_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright;
	%(simdrsltattr)s resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		datasliceleft = %(vldinstr)s( &data1[index]);
		datasliceright = %(vldinstr)s( &data2[index]);
		// The actual SIMD operation. 
		resultslice = %(SIMD_ARM_comp)s(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(%(vresult)s)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] %(compare_ops)s data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */

"""


# The actual compare operations using SIMD operations for ARMv8 NEON 64 bit.
ops_simdsupport_armv8 = """

/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#if defined(AF_HASSIMD_ARM_AARCH64)
char %(funclabel)s_%(funcmodifier)s_1_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright;
	%(simdrsltattr)s resultslice;
	%(arraytype)s compvals[%(simdwidth)s];
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param;
	}
	datasliceright = %(vldinstr)s( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		datasliceleft = %(vldinstr)s( &data1[index]);
		// The actual SIMD operation. 
		resultslice = %(SIMD_ARM_comp)s(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = %(veccombine)s(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != %(resultmask)s) || (highresult != %(resultmask)s)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] %(compare_ops)s param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char %(funclabel)s_%(funcmodifier)s_3_simd(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright;
	%(simdrsltattr)s resultslice;
	%(arraytype)s compvals[%(simdwidth)s];
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param;
	}
	datasliceleft = %(vldinstr)s( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		datasliceright = %(vldinstr)s( &data2[index]);
		// The actual SIMD operation. 
		resultslice = %(SIMD_ARM_comp)s(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = %(veccombine)s(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != %(resultmask)s) || (highresult != %(resultmask)s)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(param %(compare_ops)s data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char %(funclabel)s_%(funcmodifier)s_5_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright;
	%(simdrsltattr)s resultslice;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		datasliceleft = %(vldinstr)s( &data1[index]);
		datasliceright = %(vldinstr)s( &data2[index]);
		// The actual SIMD operation. 
		resultslice = %(SIMD_ARM_comp)s(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = %(veccombine)s(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != %(resultmask)s) || (highresult != %(resultmask)s)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] %(compare_ops)s data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */

"""

# ==============================================================================

# This is the set of function calls used to call each operator function.
compcall = """
		// %(funcmodifier)s
		case '%(arraycode)s' : {
			switch (arraydata.paramcat) {
				case param_arr_num : {
					resultcode = %(funclabel)s_%(funcmodifier)s_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.%(arraycode)s, arraydata.param.%(arraycode)s);
					break;
				}
				case param_num_arr : {
					resultcode = %(funclabel)s_%(funcmodifier)s_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.%(arraycode)s, arraydata.array2.%(arraycode)s);
					break;
				}
				case param_arr_arr : {
					resultcode = %(funclabel)s_%(funcmodifier)s_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.%(arraycode)s, arraydata.array2.%(arraycode)s);
					break;
				}
			}
			break;
		}
"""


# ==============================================================================

# Calls to parameter parseing and the implementing functions.
comp_params = """
/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	char resultcode = 0;

	// This is used to hold the parsed parameters.
	struct args_params_comp arraydata = ARGSINIT_COMP;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_comp(self, args, keywds, "%(funclabel)s");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}

	// Call the C function.
	switch(arraydata.arraytype) {
%(opscall)s
		// Wrong array type code.
		default: {
			releasebuffers_comp(arraydata);
			ErrMsgTypeExpectFloat();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_comp(arraydata);


	// Return whether compare was OK.
	if (resultcode) {
		Py_RETURN_TRUE;
	} else {
		Py_RETURN_FALSE;
	}

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
Equivalent to:          all([x %(compare_ops)s param for x in array1]) \\n\\
or                      all([param %(compare_ops)s x for x in array1]) \\n\\
or                      all([x %(compare_ops)s y for x,y in zip(array1, array2)]) \\n\\
======================  ============================================== \\n\\
\\n\\
======================  ============================================== \\n\\
Array types supported:  %(supportedarrays)s \\n\\
======================  ============================================== \\n\\
\\n\\
Call formats: \\n\\
\\n\\
  result = %(funclabel)s(array1, param) \\n\\
  result = %(funclabel)s(param, array1) \\n\\
  result = %(funclabel)s(array1, array2) \\n\\
  result = %(funclabel)s(array1, param, maxlen=y) \\n\\
  result = %(funclabel)s(array1, param, nosimd=False) \\n\\
\\n\\
* array1 - The first input data array to be examined. If no output  \\n\\
  array is provided the results will overwrite the input data.  \\n\\
* param - A non-array numeric parameter.  \\n\\
* array2 - A second input data array. Each element in this array is  \\n\\
  applied to the corresponding element in the first array.  \\n\\
* maxlen - Limit the length of the array used. This must be a valid  \\n\\
  positive integer. If a zero or negative length, or a value which is  \\n\\
  greater than the actual length of the array is specified, this  \\n\\
  parameter is ignored.  \\n\\
* nosimd - If True, SIMD acceleration is disabled if present.  \\n\\
  The default is False (SIMD acceleration is enabled if present). \\n\\
* result - A boolean value corresponding to the result of all the \\n\\
  comparison operations. If all comparison operations result in true, \\n\\
  the return value will be true. If any of them result in false, the \\n\\
  return value will be false. \\n\\
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

# SIMD call, version 1.
SIMD_calltemplate_1 = '''\n%(simdplatform)s
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		return %(funclabel)s_%(funcmodifier)s_1_simd(arraylen, data1, param);
	}
#endif\n'''

# SIMD call, version 3.
SIMD_calltemplate_3 = '''\n%(simdplatform)s
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		return %(funclabel)s_%(funcmodifier)s_3_simd(arraylen, param, data2);
	}
#endif\n'''


# SIMD call, version 5.
SIMD_calltemplate_5 = '''\n%(simdplatform)s
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		return %(funclabel)s_%(funcmodifier)s_5_simd(arraylen, data1, data2);
	}
#endif\n'''


# ==============================================================================


# ==============================================================================


# SIMD code for x86. These handle the comparison operations. This must be
# done in a round about way for x86 due to the way it works on that platform.
# This set covers unsigned integer operations only.

# param_arr_num
SIMD_x86_uint_arr_num = {
'eq' : '''// Compare the slices.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'ge' : '''// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if ((__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff)) {
			return 0;
		}''',
'gt' : '''// Make sure they're not equal.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}
		// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if ((__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff)) {
			return 0;
		}''',
'le' : '''// Find the maximum values. 
		compslice = %(vmaxinstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if ((__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff)) {
			return 0;
		}''',
'lt' : '''// Make sure they're not equal.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}
		// Find the maximum values. 
		compslice = %(vmaxinstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if ((__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff)) {
			return 0;
		}''',
'ne' : '''// Compare for equality.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}''',
}


# param_num_arr
SIMD_x86_uint_num_arr = {
'eq' : '''// Compare the slices.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'ge' : '''// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'gt' : '''// Make sure they're not equal.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}
		// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'le' : '''// Find the maximum values. 
		compslice = %(vmaxinstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'lt' : '''// Make sure they're not equal.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}
		// Find the maximum values. 
		compslice = %(vmaxinstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'ne' : '''// Compare for equality.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}''',
}


# param_arr_arr
SIMD_x86_uint_arr_arr = {
'eq' : '''// Compare the slices.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'ge' : '''// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'gt' : '''// Make sure they're not equal.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}
		// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'le' : '''// Find the maximum values. 
		compslice = %(vmaxinstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'lt' : '''// Make sure they're not equal.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}
		// Find the maximum values. 
		compslice = %(vmaxinstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'ne' : '''// Compare for equality.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}''',
}


# ==============================================================================


# SIMD code for x86. This set covers signed integer operations only.

# param_arr_num
SIMD_x86_int_arr_num = {
'eq' : '''// Compare the slices.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'ge' : '''// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if ((__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff)) {
			return 0;
		}''',
'gt' : '''// Compare the slices.
		resultslice = %(vgtinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'le' : '''// Compare the slices.
		resultslice = %(vgtinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}''',
'lt' : '''// Make sure they're not equal.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}
		// Make sure they're not greater than.
		resultslice = %(vgtinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}''',
'ne' : '''// Compare for equality.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}''',
}


# param_num_arr
SIMD_x86_int_num_arr = {
'eq' : '''// Compare the slices.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'ge' : '''// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'gt' : '''// Compare the slices.
		resultslice = %(vgtinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'le' : '''// Compare the slices.
		resultslice = %(vgtinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}''',
'lt' : '''// Make sure they're not equal.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}
		// Make sure they're not greater than.
		resultslice = %(vgtinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}''',
'ne' : '''// Compare for equality.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}''',
}


# param_arr_arr
SIMD_x86_int_arr_arr = {
'eq' : '''// Compare the slices.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'ge' : '''// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'gt' : '''// Compare the slices.
		resultslice = %(vgtinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}''',
'le' : '''// Compare the slices.
		resultslice = %(vgtinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}''',
'lt' : '''// Make sure they're not equal.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}
		// Make sure they're not greater than.
		resultslice = %(vgtinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}''',
'ne' : '''// Compare for equality.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0x0000)) {
			return 0;
		}''',
}


# ==============================================================================


# Templates for x86 SIMD.
x86_unsigned_templates = {'arr_num' : SIMD_x86_uint_arr_num,
			'num_arr' : SIMD_x86_uint_num_arr,
			'arr_arr' : SIMD_x86_uint_arr_arr}

x86_signed_templates = {'arr_num' : SIMD_x86_int_arr_num,
			'num_arr' : SIMD_x86_int_num_arr,
			'arr_arr' : SIMD_x86_int_arr_arr}


SIMD_x86_SIMD_templates = {
	'b' : x86_signed_templates,
	'B' : x86_unsigned_templates,
	'h' : x86_signed_templates,
	'H' : x86_unsigned_templates,
	'i' : x86_signed_templates,
	'I' : x86_unsigned_templates,
}

# x86 SIMD attributes.
simdattr_x86 = {
	'b' : 'v16qi',
	'B' : 'v16qi',
	'h' : 'v8hi',
	'H' : 'v8hi',
	'i' : 'v4si',
	'I' : 'v4si',
	'f' : 'v4sf',
	'd' : 'v2df',
}

# x86 SIMD load instructions.
vldinstr_x86 = {
	'b' : '(v16qi) __builtin_ia32_lddqu((char *) ', 
	'B' : '(v16qi) __builtin_ia32_lddqu((char *) ', 
	'h' : '(v8hi) __builtin_ia32_lddqu((char *) ', 
	'H' : '(v8hi) __builtin_ia32_lddqu((char *) ', 
	'i' : '(v4si) __builtin_ia32_lddqu((char *) ', 
	'I' : '(v4si) __builtin_ia32_lddqu((char *) ', 
	'f' : '(v4sf) __builtin_ia32_loadups( ', 
	'd' : '(v2df) __builtin_ia32_loadupd( ', 
}


veqinstr_x86 = {
	'b' : '__builtin_ia32_pcmpeqb128',
	'B' : '__builtin_ia32_pcmpeqb128',
	'h' : '__builtin_ia32_pcmpeqw128',
	'H' : '__builtin_ia32_pcmpeqw128',
	'i' : '__builtin_ia32_pcmpeqd128',
	'I' : '__builtin_ia32_pcmpeqd128',
}

vmininstr_x86 = {
	'b' : '__builtin_ia32_pminsb128',
	'B' : '__builtin_ia32_pminub128',
	'h' : '__builtin_ia32_pminsw128',
	'H' : '__builtin_ia32_pminuw128',
	'i' : '__builtin_ia32_pminsd128',
	'I' : '__builtin_ia32_pminud128',
}

vmaxinstr_x86 = {
	'b' : '__builtin_ia32_pmaxsb128',
	'B' : '__builtin_ia32_pmaxub128',
	'h' : '__builtin_ia32_pmaxsw128',
	'H' : '__builtin_ia32_pmaxuw128',
	'i' : '__builtin_ia32_pmaxsd128',
	'I' : '__builtin_ia32_pmaxud128',
}

vgtinstr_x86 = {
	'b' : '__builtin_ia32_pcmpgtb128',
	'B' : '',
	'h' : '__builtin_ia32_pcmpgtw128',
	'H' : '',
	'i' : '__builtin_ia32_pcmpgtd128',
	'I' : '',
}


# Which compare operations need an additional vector for intermediate results.
# This depends both upon array type and function.

compslice = ', compslice'
compslice_uint_x86 = {
'eq' : '',
'ge' : compslice,
'gt' : compslice,
'le' : compslice,
'lt' : compslice,
'ne' : ''
}

compslice_int_x86 = {
'eq' : '',
'ge' : compslice,
'gt' : '',
'le' : '',
'lt' : '',
'ne' : ''
}


SIMD_x86_compslice = {
	'b' : compslice_int_x86,
	'B' : compslice_uint_x86,
	'h' : compslice_int_x86,
	'H' : compslice_uint_x86,
	'i' : compslice_int_x86,
	'I' : compslice_uint_x86,
}



# ==============================================================================

# SIMD code for x86. This set covers single and double floating point 
# operations only. On x86, floating point SIMD operations are much
# more regular and complete than for integer operations.


SIMD_x86_float = '''// Compare the slices.
		resultslice = %(vcmpinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}'''


vfloat_ops_x86 = {
	'f' : {
		'eq' : '__builtin_ia32_cmpeqps',
		'ge' : '__builtin_ia32_cmpgeps',
		'gt' : '__builtin_ia32_cmpgtps',
		'le' : '__builtin_ia32_cmpleps',
		'lt' : '__builtin_ia32_cmpltps',
		'ne' : '__builtin_ia32_cmpneqps'
		},
	'd' :  {
		'eq' : '__builtin_ia32_cmpeqpd',
		'ge' : '__builtin_ia32_cmpgepd',
		'gt' : '__builtin_ia32_cmpgtpd',
		'le' : '__builtin_ia32_cmplepd',
		'lt' : '__builtin_ia32_cmpltpd',
		'ne' : '__builtin_ia32_cmpneqpd'
		}
}


# ==============================================================================

# Total list of which array types are supported by x86 SIMD instructions.
SIMD_x86_support = simdattr_x86.keys()

# ==============================================================================


# ==============================================================================

# For ARM NEON ARMv7 32 bit.
# Benchmarking has shown that some SIMD operations are slower than the
# non-SIMD versions and so are not used here.

simdattr_armv7 = {
	'b' : 'int8x8_t',
	'B' : 'uint8x8_t',
	'h' : 'int16x4_t',
	'H' : 'uint16x4_t',
}


simdrsltattr_armv7 = {
	'b' : 'uint8x8_t',
	'B' : 'uint8x8_t',
	'h' : 'uint16x4_t',
	'H' : 'uint16x4_t',
}

# Load values to SIMD registers.
vldinstr_armv7 = {
	'b' : 'vld1_s8',
	'B' : 'vld1_u8',
	'h' : 'vld1_s16',
	'H' : 'vld1_u16',
}


# Compare result to see if OK. This depends both on size and also
# 'ne' must be handled differently. 
vresult_8_armv7 = 'vreinterpret_u64_u8(resultslice) == 0xffffffffffffffff'
vresult_16_armv7 = 'vreinterpret_u64_u16(resultslice) == 0xffffffffffffffff'
vresult_8_ne_armv7 = 'vreinterpret_u64_u8(resultslice) == 0x0000000000000000'
vresult_16_ne_armv7 = 'vreinterpret_u64_u16(resultslice) == 0x0000000000000000'
vreslt_8_total_armv7 = {
		'eq' : vresult_8_armv7,
		'ge' : vresult_8_armv7,
		'gt' : vresult_8_armv7,
		'le' : vresult_8_armv7,
		'lt' : vresult_8_armv7,
		'ne' : vresult_8_ne_armv7,
		}

vresult_16_total_armv7 = {
		'eq' : vresult_16_armv7,
		'ge' : vresult_16_armv7,
		'gt' : vresult_16_armv7,
		'le' : vresult_16_armv7,
		'lt' : vresult_16_armv7,
		'ne' : vresult_16_ne_armv7,
		}

# The above combined so we can look it up.
vresult_armv7 = {
	'b' : vreslt_8_total_armv7,
	'B' : vreslt_8_total_armv7,
	'h' : vresult_16_total_armv7,
	'H' : vresult_16_total_armv7,
}



# The ARM SIMD ops for compare. The NE op must be combined with a 
# different vresult as there is no actual not equal op.
vsimdops_armv7 = {
	'b' : {
		'eq' : 'vceq_s8',
		'ge' : 'vcge_s8',
		'gt' : 'vcgt_s8',
		'le' : 'vcle_s8',
		'lt' : 'vclt_s8',
		'ne' : 'vceq_s8'
		},
	'B' :  {
		'eq' : 'vceq_u8',
		'ge' : 'vcge_u8',
		'gt' : 'vcgt_u8',
		'le' : 'vcle_u8',
		'lt' : 'vclt_u8',
		'ne' : 'vceq_u8'
		},
	'h' : {
		'eq' : 'vceq_s16',
		'ge' : 'vcge_s16',
		'gt' : 'vcgt_s16',
		'le' : 'vcle_s16',
		'lt' : 'vclt_s16',
		'ne' : 'vceq_s16'
		},
	'H' :  {
		'eq' : 'vceq_u16',
		'ge' : 'vcge_u16',
		'gt' : 'vcgt_u16',
		'le' : 'vcle_u16',
		'lt' : 'vclt_u16',
		'ne' : 'vceq_u16'
		},
}

# ==============================================================================


# Total list of which array types are supported by ARM SIMD instructions.
SIMD_armv7_support = simdattr_armv7.keys()


# ==============================================================================

# For ARM NEON armv8 64 bit.
# Benchmarking has shown that some SIMD operations are slower than the
# non-SIMD versions and so are not used here.

vsimdattr_armv8 = {
	'b' : 'int8x16_t',
	'B' : 'uint8x16_t',
	'h' : 'int16x8_t',
	'H' : 'uint16x8_t',
	'i' : 'int32x4_t',
	'I' : 'uint32x4_t',
	'f' : 'float32x4_t',
}


vsimdrsltattr_armv8 = {
	'b' : 'uint8x16_t',
	'B' : 'uint8x16_t',
	'h' : 'uint16x8_t',
	'H' : 'uint16x8_t',
	'i' : 'uint32x4_t',
	'I' : 'uint32x4_t',
	'f' : 'uint32x4_t',
}

# Load values to SIMD registers.
vldinstr_armv8 = {
	'b' : 'vld1q_s8',
	'B' : 'vld1q_u8',
	'h' : 'vld1q_s16',
	'H' : 'vld1q_u16',
	'i' : 'vld1q_s32',
	'I' : 'vld1q_u32',
	'f' : 'vld1q_f32',
}

# Combine the result vectors into two 64 bit vectors.
veccombine_armv8 = {
	'b' : 'vreinterpretq_u64_u8',
	'B' : 'vreinterpretq_u64_u8',
	'h' : 'vreinterpretq_u64_u16',
	'H' : 'vreinterpretq_u64_u16',
	'i' : 'vreinterpretq_u64_u32',
	'I' : 'vreinterpretq_u64_u32',
	'f' : 'vreinterpretq_u64_u32',
}

# Compare result to see if OK. This depends both on size and also
# 'ne' must be handled differently. 

vresultmask_ops_armv8 = '0xffffffffffffffff'
vresultmask_ne_armv8 = '0x0000000000000000'

vresultmask_armv8 = {
		'eq' : vresultmask_ops_armv8,
		'ge' : vresultmask_ops_armv8,
		'gt' : vresultmask_ops_armv8,
		'le' : vresultmask_ops_armv8,
		'lt' : vresultmask_ops_armv8,
		'ne' : vresultmask_ne_armv8,
		}



# The ARM SIMD ops for compare. The NE op must be combined with a 
# different vresult as there is no actual not equal op.
vsimdops_armv8 = {
	'b' : {
		'eq' : 'vceqq_s8',
		'ge' : 'vcgeq_s8',
		'gt' : 'vcgtq_s8',
		'le' : 'vcleq_s8',
		'lt' : 'vcltq_s8',
		'ne' : 'vceqq_s8'
		},
	'B' :  {
		'eq' : 'vceqq_u8',
		'ge' : 'vcgeq_u8',
		'gt' : 'vcgtq_u8',
		'le' : 'vcleq_u8',
		'lt' : 'vcltq_u8',
		'ne' : 'vceqq_u8'
		},
	'h' : {
		'eq' : 'vceqq_s16',
		'ge' : 'vcgeq_s16',
		'gt' : 'vcgtq_s16',
		'le' : 'vcleq_s16',
		'lt' : 'vcltq_s16',
		'ne' : 'vceqq_s16'
		},
	'H' :  {
		'eq' : 'vceqq_u16',
		'ge' : 'vcgeq_u16',
		'gt' : 'vcgtq_u16',
		'le' : 'vcleq_u16',
		'lt' : 'vcltq_u16',
		'ne' : 'vceqq_u16'
		},
	'i' : {
		'eq' : 'vceqq_s32',
		'ge' : 'vcgeq_s32',
		'gt' : 'vcgtq_s32',
		'le' : 'vcleq_s32',
		'lt' : 'vcltq_s32',
		'ne' : 'vceqq_s32'
		},
	'I' : {
		'eq' : 'vceqq_u32',
		'ge' : 'vcgeq_u32',
		'gt' : 'vcgtq_u32',
		'le' : 'vcleq_u32',
		'lt' : 'vcltq_u32',
		'ne' : 'vceqq_u32'
		},
	'f' : {
		'eq' : 'vceqq_f32',
		'ge' : 'vcgeq_f32',
		'gt' : 'vcgtq_f32',
		'le' : 'vcleq_f32',
		'lt' : 'vcltq_f32',
		'ne' : 'vceqq_f32'
		},
}


# ==============================================================================

# Total list of which array types are supported by ARM SIMD instructions.
SIMD_armv8_support = vsimdattr_armv8.keys()


# ==============================================================================

# Width of array elements.
simdwidth = {'b' : 'CHARSIMDSIZE',
		'B' : 'CHARSIMDSIZE',
		'h' : 'SHORTSIMDSIZE',
		'H' : 'SHORTSIMDSIZE',
		'i' : 'INTSIMDSIZE',
		'I' : 'INTSIMDSIZE',
		'f' : 'FLOATSIMDSIZE',
		'd' : 'DOUBLESIMDSIZE',
		}

# ==============================================================================

# Compare operations.
compare_ops = {
	'eq' : '==',
	'ge' : '>=',
	'gt' : '>',
	'le' : '<=',
	'lt' : '<',
	'ne' : '!='
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
	else:
		return 'Error: Template error, this should not be here.'

# ==============================================================================


# ==============================================================================


# Read in the op codes.
opdata = codegen_common.ReadINI('affuncdata.ini')

# Filter out the desired math functions.
funclist = [(x,dict(y)) for x,y in opdata.items() if y.get('c_code_template') == 'template_comp']

# ==============================================================================

# Output the main code body.
for funcname, func in funclist:


	# Create the source code based on templates.
	filename = funcname + '.c'
	with open(filename, 'w') as f:
		funcdata = {'funclabel' : funcname}
		f.write(mathops_head % {'funclabel' : funcname})
		opscalltext = []


		# Check each array type.
		for arraycode in codegen_common.arraycodes:
			funcdata['funcmodifier'] = codegen_common.arraytypes[arraycode].replace(' ', '_')
			funcdata['arraytype'] = codegen_common.arraytypes[arraycode]

			if arraycode == 'f':
				funcdata['copname'] = func['c_operator_f']
			elif arraycode == 'd':
				funcdata['copname'] = func['c_operator_d']
			elif arraycode in codegen_common.intarrays:
				 funcdata['copname'] = func['c_operator_i']
			else:
				print('Error - Unsupported array code.', arraycode)


			# Each call to an SIMD function comes in three different versions due
			# to there being three different parameter formats.
			if arraycode in (set(SIMD_x86_support) | set(SIMD_armv7_support) | set(SIMD_armv8_support)):
				simdfunccall = {'simdwidth' : simdwidth[arraycode], 
					'funclabel' : funcdata['funclabel'],
					'funcmodifier' : funcdata['funcmodifier'],
					'simdplatform' : findsimdplatform(arraycode),}

				simd_call_1 = SIMD_calltemplate_1 % simdfunccall
				simd_call_3 = SIMD_calltemplate_3 % simdfunccall
				simd_call_5 = SIMD_calltemplate_5 % simdfunccall
			else:
				simd_call_1 = ''
				simd_call_3 = ''
				simd_call_5 = ''


			funcdata['simd_call_1'] = simd_call_1
			funcdata['simd_call_3'] = simd_call_3
			funcdata['simd_call_5'] = simd_call_5

			f.write(ops_comp % funcdata)

			# This is the call to the functions for this array type. This
			# is inserted into another template below.
			funcdata['arraycode'] = arraycode
			opscalltext.append(compcall % funcdata)

		supportedarrays = codegen_common.FormatDocsArrayTypes(func['arraytypes'])

		f.write(comp_params % {'funclabel' : funcname, 
				'opcodedocs' : func['opcodedocs'], 
				'compare_ops' : compare_ops[funcname], 
				'supportedarrays' : supportedarrays,
				'matherrors' : ', '.join(func['matherrors'].split(',')),
				'opscall' : ''.join(opscalltext),
				'simd_call_1' : simd_call_1,
				'simd_call_3' : simd_call_3,
				'simd_call_5' : simd_call_5})



# ==============================================================================

# ==============================================================================

# The original date of the SIMD C code.
simdcodedate = '16-Jan-2018'
simdfilename = '_simd_x86'

# This outputs the SIMD version for x86-64.

for funcname, func in funclist:

	outputlist = []


	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname


	# Output the generated code.
	# Handle integer operations.
	for arraycode in SIMD_x86_SIMD_templates:

		arraytype = codegen_common.arraytypes[arraycode]


		# This fetches the individual SIMD instructions.
		template_instr = {'veqinstr' : veqinstr_x86[arraycode],
						'vmininstr' : vmininstr_x86[arraycode],
						'vmaxinstr' : vmaxinstr_x86[arraycode],
						'vgtinstr' : vgtinstr_x86[arraycode],
						}

		# These templates put the SIMD instructions together for the
		# final template.
		template_arr_num = SIMD_x86_SIMD_templates[arraycode]['arr_num'][funcname] % template_instr
		template_num_arr = SIMD_x86_SIMD_templates[arraycode]['num_arr'][funcname] % template_instr
		template_arr_arr = SIMD_x86_SIMD_templates[arraycode]['arr_arr'][funcname] % template_instr

		# The compare_ops symbols is the same for integer and floating point.
		datavals = {'funclabel' : funcname,
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'arraycode' : arraycode,
					'compare_ops' : compare_ops[funcname],
					'simdwidth' : simdwidth[arraycode],
					'simdattr' : simdattr_x86[arraycode],
					'vldinstr' : vldinstr_x86[arraycode],
					'SIMD_x86_compslice' : SIMD_x86_compslice[arraycode][funcname],
					'SIMD_x86_arr_num' : template_arr_num,
					'SIMD_x86_num_arr' : template_num_arr,
					'SIMD_x86_arr_arr' : template_arr_arr
					}


		# Start of function definition.
		outputlist.append(ops_simdsupport_x86 % datavals)


	# Handle floating point operations.
	for arraycode in vfloat_ops_x86:

		arraytype = codegen_common.arraytypes[arraycode]

		template_instr = {'vcmpinstr' : vfloat_ops_x86[arraycode][funcname]}
		template_float = SIMD_x86_float % template_instr

		# The compare_ops symbols is the same for integer and floating point.
		datavals = {'funclabel' : funcname,
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'arraycode' : arraycode,
					'compare_ops' : compare_ops[funcname],
					'simdwidth' : simdwidth[arraycode],
					'simdattr' : simdattr_x86[arraycode],
					'vldinstr' : vldinstr_x86[arraycode],
					'SIMD_x86_compslice' : '',
					'SIMD_x86_arr_num' : template_float,
					'SIMD_x86_num_arr' : template_float,
					'SIMD_x86_arr_arr' : template_float
					}


		# Start of function definition.
		outputlist.append(ops_simdsupport_x86 % datavals)


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

# The original date of the SIMD C code.
simdcodedate = '06-Oct-2019'
simdfilename = '_simd_armv7'

# This outputs the SIMD version for ARM NEON ARMv7 32 bit.

for funcname, func in funclist:

	outputlist = []


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
					'arraycode' : arraycode,
					'arraytype' : codegen_common.arraytypes[arraycode],
					'compare_ops' : compare_ops[funcname],
					'simdattr' : simdattr_armv7[arraycode],
					'simdrsltattr' : simdrsltattr_armv7[arraycode],
					'vldinstr' : vldinstr_armv7[arraycode],
					'vresult' : vresult_armv7[arraycode][funcname],
					'SIMD_ARM_comp' : vsimdops_armv7[arraycode][funcname],
					}


		# Start of function definition.
		outputlist.append(ops_simdsupport_armv7 % datavals)



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

# The original date of the SIMD C code.
simdcodedate = '22-Mar-2020'
simdfilename = '_simd_armv8'

# This outputs the SIMD version for ARM NEON ARMv8 64 bit.

for funcname, func in funclist:

	outputlist = []


	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname


	# Output the generated code.
	for arraycode in codegen_common.arraycodes:

		if arraycode in SIMD_armv8_support:
			arraytype = codegen_common.arraytypes[arraycode]

			# The compare_ops symbols is the same for integer and floating point.
			datavals = {'funclabel' : funcname,
						'arraytype' : arraytype, 
						'funcmodifier' : arraytype.replace(' ', '_'),
						'simdwidth' : simdwidth[arraycode],
						'arraycode' : arraycode,
						'arraytype' : codegen_common.arraytypes[arraycode],
						'compare_ops' : compare_ops[funcname],
						'simdattr' : vsimdattr_armv8[arraycode],
						'simdrsltattr' : vsimdrsltattr_armv8[arraycode],
						'veccombine' : veccombine_armv8[arraycode],
						'resultmask' : vresultmask_armv8[funcname],
						'vldinstr' : vldinstr_armv8[arraycode],
						'SIMD_ARM_comp' : vsimdops_armv8[arraycode][funcname],
						}


			# Start of function definition.
			outputlist.append(ops_simdsupport_armv8 % datavals)



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
