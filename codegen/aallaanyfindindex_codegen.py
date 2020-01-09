#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for aall, aany, findindex.
# Language: Python 3.4
# Date:     11-Jun-2014
#
###############################################################################
#
#   Copyright 2014 - 2019    Michael Griffin    <m12.griffin@gmail.com>
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

allany_head = """//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   %(funclabel)s.c
// Purpose:  Calculate the %(funclabel)s of values in an array.
// Language: C
// Date:     15-Nov-2017.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2019    Michael Griffin    <m12.griffin@gmail.com>
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
#include "arrayops.h"

#include "arrayparams_allany.h"

#include "simddefs.h"

#ifdef AF_HASSIMD_X86
#include "%(funclabel)s_simd_x86.h"
#endif

#ifdef AF_HASSIMD_ARM
#include "arm_neon.h"
#include "%(funclabel)s_simd_arm.h"
#endif

/*--------------------------------------------------------------------------- */
"""

# ==============================================================================

# The basic template for the non-SIMD version of aall.
ops_aall = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
signed int aall_%(opcode)s_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s param1) { 
	// array index counter.
	Py_ssize_t index;

	for (index = 0; index < arraylen; index++) {
		if (!(data[index] %(compare_ops)s param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}
	return 1;

}
"""


# The basic template for the SIMD version of aall. x86-64 version.
ops_aall_simd_x86 = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_X86)
signed int aall_%(opcode)s_%(funcmodifier)s_simd(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s param1) { 

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
		compvals[y] = param1;
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
		datasliceleft = %(vldinstr)s &data[index]);
		%(SIMD_x86_ops)s
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] %(compare_ops)s param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif

"""


# The basic template for the SIMD version of aall. ARM version
ops_aall_simd_arm = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM)
signed int aall_%(opcode)s_%(funcmodifier)s_simd(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = %(vldinstr)s( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		datasliceleft = %(vldinstr)s( &data[index]);
		// The actual SIMD operation. 
		resultslice = %(SIMD_ARM_comp)s(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (%(vresult)s) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] %(compare_ops)s param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif

"""


# ==============================================================================

# The basic template for the non-SIMD version of aany.
ops_aany = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
signed int aany_%(opcode)s_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s param1) { 
	// array index counter.
	Py_ssize_t index;

	for (index = 0; index < arraylen; index++) {
		if (data[index] %(compare_ops)s param1) {
			return 1;
		}
	}
	return ARR_ERR_NOTFOUND;

}
"""

# The basic template for the SIMD version of aany. x86 version.
ops_aany_simd_x86 = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_%(opcode)s_%(funcmodifier)s_simd(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s param1) { 

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
		compvals[y] = param1;
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
		datasliceleft = %(vldinstr)s &data[index]);
		%(SIMD_x86_ops)s
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] %(compare_ops)s param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif

"""



# The basic template for the SIMD version of aany. ARM version.
ops_aany_simd_arm = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARM)
signed int aany_%(opcode)s_%(funcmodifier)s_simd(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = %(vldinstr)s( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		datasliceleft = %(vldinstr)s( &data[index]);
		// The actual SIMD operation. 
		resultslice = %(SIMD_ARM_comp)s(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (%(vresult)s) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] %(compare_ops)s param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif

"""


# ==============================================================================

# The basic template for the non-SIMD version of findindex.
ops_findindex = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_%(opcode)s_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] %(compare_ops)s param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}
"""



# The basic template for the SIMD version of findindex. x86 version.
ops_findindex_simd_x86 = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
Py_ssize_t findindex_%(opcode)s_%(funcmodifier)s_simd(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright;
	%(simdattr)s resultslice%(SIMD_x86_compslice)s;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param1;
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
		datasliceleft = %(vldinstr)s &data[index]);
		%(SIMD_x86_ops)s
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] %(compare_ops)s param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] %(compare_ops)s param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif

"""


# The basic template for the SIMD version of findindex. ARM version.
ops_findindex_simd_arm = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARM)
Py_ssize_t findindex_%(opcode)s_%(funcmodifier)s_simd(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright;
	%(simdrsltattr)s resultslice;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param1;
	}
	datasliceright = %(vldinstr)s( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		datasliceleft = %(vldinstr)s( &data[index]);
		// The actual SIMD operation. 
		resultslice = %(SIMD_ARM_comp)s(datasliceleft, datasliceright);
		if (%(vresult)s) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] %(compare_ops)s param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] %(compare_ops)s param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif

"""


# ==============================================================================

case_ops = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
%(resultcode)s %(funclabel)s_select_%(funcmodifier)s(signed int opcode, Py_ssize_t arraylen, unsigned int nosimd, %(arraytype)s *data, %(arraytype)s param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
%(simd_call_eq)s
			return %(funclabel)s_eq_%(funcmodifier)s(arraylen, data, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
%(simd_call_gt)s
			return %(funclabel)s_gt_%(funcmodifier)s(arraylen, data, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
%(simd_call_ge)s
			return %(funclabel)s_ge_%(funcmodifier)s(arraylen, data, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
%(simd_call_lt)s
			return %(funclabel)s_lt_%(funcmodifier)s(arraylen, data, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
%(simd_call_le)s
			return %(funclabel)s_le_%(funcmodifier)s(arraylen, data, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
%(simd_call_ne)s
			return %(funclabel)s_ne_%(funcmodifier)s(arraylen, data, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */
"""


# ==============================================================================


# ==============================================================================


allany_params = """
/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	%(resultcode)s resultcode = 0;

	// This is used to hold the parsed parameters.
	struct args_params_allany arraydata = ARGSINIT_ALLANY;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_allany(self, args, keywds, "%(funclabel)s");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}


	// The length of the data array.
	if (arraydata.arraylength < 1) {
		// Release the buffers. 
		releasebuffers_allany(arraydata);
		ErrMsgArrayLengthErr();
		return NULL;
	}



	/* Call the C function */
	switch(arraydata.arraytype) {
		// signed char
		case 'b' : {
			resultcode = %(funclabel)s_select_signed_char(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.b, arraydata.param.b);
			break;
		}
		// unsigned char
		case 'B' : {
			resultcode = %(funclabel)s_select_unsigned_char(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.B, arraydata.param.B);
			break;
		}
		// signed short
		case 'h' : {
			resultcode = %(funclabel)s_select_signed_short(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.h, arraydata.param.h);
			break;
		}
		// unsigned short
		case 'H' : {
			resultcode = %(funclabel)s_select_unsigned_short(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.H, arraydata.param.H);
			break;
		}
		// signed int
		case 'i' : {
			resultcode = %(funclabel)s_select_signed_int(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.i, arraydata.param.i);
			break;
		}
		// unsigned int
		case 'I' : {
			resultcode = %(funclabel)s_select_unsigned_int(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.I, arraydata.param.I);
			break;
		}
		// signed long
		case 'l' : {
			resultcode = %(funclabel)s_select_signed_long(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.l, arraydata.param.l);
			break;
		}
		// unsigned long
		case 'L' : {
			resultcode = %(funclabel)s_select_unsigned_long(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.L, arraydata.param.L);
			break;
		}
		// signed long long
		case 'q' : {
			resultcode = %(funclabel)s_select_signed_long_long(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.q, arraydata.param.q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultcode = %(funclabel)s_select_unsigned_long_long(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.Q, arraydata.param.Q);
			break;
		}
		// float
		case 'f' : {
			resultcode = %(funclabel)s_select_float(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.f, arraydata.param.f);
			break;
		}
		// double
		case 'd' : {
			resultcode = %(funclabel)s_select_double(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.d, arraydata.param.d);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_allany(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_allany(arraydata);


	// Signal the errors.
	if (resultcode == ARR_ERR_INVALIDOP) {
		ErrMsgOperatorNotValidforthisFunction();
		return NULL;
	}


%(return_result)s

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
Equivalent to:          %(opcodedocs)s \\n\\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \\n\\
Exceptions raised:      None \\n\\
======================  ============================================== \\n\\
\\n\\
Call formats: \\n\\
\\n\\
  result = %(funclabel)s(opstr, array, param) \\n\\
  result = %(funclabel)s(opstr, array, param, maxlen=y) \\n\\
  result = %(funclabel)s(opstr, array, param, nosimd=False) \\n\\
\\n\\
* opstr - The arithmetic comparison operation as a string. \\n\\
          These are: '==', '>', '>=', '<', '<=', '!='. \\n\\
* array - The input data array to be examined. \\n\\
* param - A non-array numeric parameter. \\n\\
* maxlen - Limit the length of the array used. This must be a valid \\n\\
  positive integer. If a zero or negative length, or a value which is \\n\\
  greater than the actual length of the array is specified, this \\n\\
  parameter is ignored. \\n\\
* nosimd - If True, SIMD acceleration is disabled if present. \\n\\
  The default is False (SIMD acceleration is enabled if present). \\n\\
* %(resultdoc)s \\n\\
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



# Template for the return of the result code for aall or aany.
allany_return = '''
	// Return whether compare was OK.
	if (resultcode == ARR_ERR_NOTFOUND) {
		Py_RETURN_FALSE;
	} else {
		Py_RETURN_TRUE;
	}
'''

# Template for the return of the index position for findindex.
findindex_return = '''
	// Adjust the result code if the data was not found, so that we don't leak
	// internal error codes to user space (and cause problems if they change).
	if (resultcode < 0) {
		resultcode = -1;
	}

	// Return the number of items filtered through.
	return PyLong_FromSsize_t(resultcode);
'''


return_templates = {'aall' : allany_return, 
			'aany' : allany_return, 
			'findindex' : findindex_return
}


# The template used to call SIMD operations.
simd_call_template = '''%(simdplatform)s
			// SIMD version.
			if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
				return %(funclabel)s_%(opcode)s_%(funcmodifier)s_simd(arraylen, data, param1);
			}
#endif'''


# ==============================================================================


# These get substituted into function call templates.
SIMD_platform_x86 = '#if defined(AF_HASSIMD_X86)'
SIMD_platform_x86_ARM = '#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM)'
SIMD_platform_ARM = '#if defined(AF_HASSIMD_ARM)'


# ==============================================================================


# ==============================================================================


# SIMD code for x86. These handle the comparison operations. This must be
# done in a round about way for x86 due to the way it works on that platform.
# This set covers unsigned integer operations only.

# For aall
# param_arr_num
SIMD_x86_uint_aall_templates = {
'eq' : '''// Compare the slices.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return ARR_ERR_NOTFOUND;
		}''',
'ge' : '''// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return ARR_ERR_NOTFOUND;
		}''',
'gt' : '''// Make sure they're not equal.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return ARR_ERR_NOTFOUND;
		}
		// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return ARR_ERR_NOTFOUND;
		}''',
'le' : '''// Find the maximum values. 
		compslice = %(vmaxinstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return ARR_ERR_NOTFOUND;
		}''',
'lt' : '''// Make sure they're not equal.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return ARR_ERR_NOTFOUND;
		}
		// Find the maximum values. 
		compslice = %(vmaxinstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return ARR_ERR_NOTFOUND;
		}''',
'ne' : '''// Compare for equality.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return ARR_ERR_NOTFOUND;
		}''',
}


# SIMD code for x86. This set covers signed integer operations only.

# param_arr_num
SIMD_x86_int_aall_templates = {
'eq' : '''// Compare the slices.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return ARR_ERR_NOTFOUND;
		}''',
'ge' : '''// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then the test
		// has failed.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return ARR_ERR_NOTFOUND;
		}''',
'gt' : '''// Compare the slices.
		resultslice = %(vgtinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return ARR_ERR_NOTFOUND;
		}''',
'le' : '''// Compare the slices.
		resultslice = %(vgtinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return ARR_ERR_NOTFOUND;
		}''',
'lt' : '''// Make sure they're not equal.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return ARR_ERR_NOTFOUND;
		}
		// Make sure they're not greater than.
		resultslice = %(vgtinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return ARR_ERR_NOTFOUND;
		}''',
'ne' : '''// Compare for equality.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return ARR_ERR_NOTFOUND;
		}''',
}


# ==============================================================================

# This set covers unsigned integer operations only.
# For aany.

# param_arr_num
SIMD_x86_uint_aany_templates = {
'eq' : '''// Compare the slices.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}''',
'ge' : '''// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then a least.
		// one value is less than.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}''',
'gt' : '''// Find the maximum values. 
		compslice = %(vmaxinstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is greater than. 
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}''',
'le' : '''// Find the maximum values. 
		compslice = %(vmaxinstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is less than or equal to.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}''',
'lt' : '''// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is less than.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}''',
'ne' : '''// Compare for equality.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}''',
}


# SIMD code for x86. This set covers signed integer operations only.

# For aany.

# param_arr_num
SIMD_x86_int_aany_templates = {
'eq' : '''// Compare the slices.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}''',
'ge' : '''// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is greater than or equal to.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}''',
'gt' : '''// Compare the slices.
		resultslice = %(vgtinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}''',
'le' : '''// Compare the slices.
		resultslice = %(vgtinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}''',
'lt' : '''// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is less than.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}''',
'ne' : '''// Compare for equality.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}''',
}


# ==============================================================================

# This set covers unsigned integer operations only.
# For findindex.

# param_arr_num
SIMD_x86_uint_findindex_templates = {
'eq' : '''// Compare the slices.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {''',
'ge' : '''// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is greater than or equal to.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {''',
'gt' : '''// Find the maximum values. 
		compslice = %(vmaxinstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is greater than. 
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {''',
'le' : '''// Find the maximum values. 
		compslice = %(vmaxinstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is less than or equal to.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {''',
'lt' : '''// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is less than.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {''',
'ne' : '''// Compare for equality.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {''',
}


# SIMD code for x86. This set covers signed integer operations only.

# For findindex.

# param_arr_num
SIMD_x86_int_findindex_templates = {
'eq' : '''// Compare the slices.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {''',
'ge' : '''// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is greater than or equal to.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {''',
'gt' : '''// Compare the slices.
		resultslice = %(vgtinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {''',
'le' : '''// Compare the slices.
		resultslice = %(vgtinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {''',
'lt' : '''// Find the minimum values. 
		compslice = %(vmininstr)s(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is less than.
		resultslice = %(veqinstr)s(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {''',
'ne' : '''// Compare for equality.
		resultslice = %(veqinstr)s(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {''',
}

# ==============================================================================

# SIMD code for x86. This set covers single and double floating point 
# operations only. On x86, floating point SIMD operations are much
# more regular and complete than for integer operations.

SIMD_x86_float_aall_template = '''// Compare the slices.
		resultslice = %(vcmpinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return ARR_ERR_NOTFOUND;
		}'''


SIMD_x86_float_aany_template = '''// Compare the slices.
		resultslice = %(vcmpinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}'''

SIMD_x86_float_findindex_template = '''// Compare the slices.
		resultslice = %(vcmpinstr)s(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {'''

# ==============================================================================

# SIMD templates for x86. These make the compare decisions and are 
# substituted into the main SIMD template.
SIMD_x86_SIMD_int_templates = {
	'b' : {'aall' : SIMD_x86_int_aall_templates, 
			'aany' : SIMD_x86_int_aany_templates,
			'findindex' : SIMD_x86_int_findindex_templates},
	'B' : {'aall' : SIMD_x86_uint_aall_templates, 
			'aany' : SIMD_x86_uint_aany_templates,
			'findindex' : SIMD_x86_uint_findindex_templates},
	'h' : {'aall' : SIMD_x86_int_aall_templates, 
			'aany' : SIMD_x86_int_aany_templates,
			'findindex' : SIMD_x86_int_findindex_templates},
	'H' : {'aall' : SIMD_x86_uint_aall_templates, 
			'aany' : SIMD_x86_uint_aany_templates,
			'findindex' : SIMD_x86_uint_findindex_templates},
	'i' : {'aall' : SIMD_x86_int_aall_templates, 
			'aany' : SIMD_x86_int_aany_templates,
			'findindex' : SIMD_x86_int_findindex_templates},
	'I' : {'aall' : SIMD_x86_uint_aall_templates, 
			'aany' : SIMD_x86_uint_aany_templates,
			'findindex' : SIMD_x86_uint_findindex_templates},
}

# SIMD templates for x86. These are the floating point equivalents to the above.
SIMD_x86_SIMD_float_templates = {
	'aall' : SIMD_x86_float_aall_template, 
	'aany' : SIMD_x86_float_aany_template,
	'findindex' : SIMD_x86_float_findindex_template,
}



# x86 SIMD attributes.
x86_simdattr = {
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
x86_vldinstr = {
	'b' : '(v16qi) __builtin_ia32_lddqu((char *) ', 
	'B' : '(v16qi) __builtin_ia32_lddqu((char *) ', 
	'h' : '(v8hi) __builtin_ia32_lddqu((char *) ', 
	'H' : '(v8hi) __builtin_ia32_lddqu((char *) ', 
	'i' : '(v4si) __builtin_ia32_lddqu((char *) ', 
	'I' : '(v4si) __builtin_ia32_lddqu((char *) ', 
	'f' : '(v4sf) __builtin_ia32_loadups( ', 
	'd' : '(v2df) __builtin_ia32_loadupd( ', 
}


SIMD_x86_veqinstr = {
	'b' : '__builtin_ia32_pcmpeqb128',
	'B' : '__builtin_ia32_pcmpeqb128',
	'h' : '__builtin_ia32_pcmpeqw128',
	'H' : '__builtin_ia32_pcmpeqw128',
	'i' : '__builtin_ia32_pcmpeqd128',
	'I' : '__builtin_ia32_pcmpeqd128',
}

SIMD_x86_vmininstr = {
	'b' : '__builtin_ia32_pminsb128',
	'B' : '__builtin_ia32_pminub128',
	'h' : '__builtin_ia32_pminsw128',
	'H' : '__builtin_ia32_pminuw128',
	'i' : '__builtin_ia32_pminsd128',
	'I' : '__builtin_ia32_pminud128',
}

SIMD_x86_vmaxinstr = {
	'b' : '__builtin_ia32_pmaxsb128',
	'B' : '__builtin_ia32_pmaxub128',
	'h' : '__builtin_ia32_pmaxsw128',
	'H' : '__builtin_ia32_pmaxuw128',
	'i' : '__builtin_ia32_pmaxsd128',
	'I' : '__builtin_ia32_pmaxud128',
}

SIMD_x86_vgtinstr = {
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

# For aall
SIMD_x86_compslice_uint_aall = {
'eq' : '',
'ge' : compslice,
'gt' : compslice,
'le' : compslice,
'lt' : compslice,
'ne' : ''
}

SIMD_x86_compslice_int_aall = {
'eq' : '',
'ge' : compslice,
'gt' : '',
'le' : '',
'lt' : '',
'ne' : ''
}

# For aany.
SIMD_x86_compslice_uint_aany = {
'eq' : '',
'ge' : compslice,
'gt' : compslice,
'le' : compslice,
'lt' : compslice,
'ne' : ''
}

SIMD_x86_compslice_int_aany = {
'eq' : '',
'ge' : compslice,
'gt' : '',
'le' : '',
'lt' : compslice,
'ne' : ''
}

# For Findindex.
SIMD_x86_compslice_uint_findindex = {
'eq' : '',
'ge' : compslice,
'gt' : compslice,
'le' : compslice,
'lt' : compslice,
'ne' : ''
}

SIMD_x86_compslice_int_findindex = {
'eq' : '',
'ge' : compslice,
'gt' : '',
'le' : '',
'lt' : compslice,
'ne' : ''
}



SIMD_x86_compslice = {
	'b' : {'aall' : SIMD_x86_compslice_int_aall, 
			'aany' : SIMD_x86_compslice_int_aany,
			'findindex' : SIMD_x86_compslice_int_findindex},
	'B' : {'aall' : SIMD_x86_compslice_uint_aall, 
			'aany' : SIMD_x86_compslice_uint_aany, 
			'findindex' : SIMD_x86_compslice_uint_findindex},
	'h' : {'aall' : SIMD_x86_compslice_int_aall, 
			'aany' : SIMD_x86_compslice_int_aany, 
			'findindex' : SIMD_x86_compslice_int_findindex},
	'H' : {'aall' : SIMD_x86_compslice_uint_aall, 
			'aany' : SIMD_x86_compslice_uint_aany, 
			'findindex' : SIMD_x86_compslice_uint_findindex},
	'i' : {'aall' : SIMD_x86_compslice_int_aall, 
			'aany' : SIMD_x86_compslice_int_aany, 
			'findindex' : SIMD_x86_compslice_int_findindex},
	'I' : {'aall' : SIMD_x86_compslice_uint_aall, 
			'aany' : SIMD_x86_compslice_uint_aany, 
			'findindex' : SIMD_x86_compslice_uint_findindex},
}



# Floating point operations are more regular and complete than integer ones.
SIMD_x86_float_ops = {
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

# ==============================================================================

# Total list of which array types are supported by x86 SIMD instructions.
SIMD_x86_support = x86_simdattr.keys()

# Total list of which integer array types are supported by x86 SIMD instructions.
SIMD_x86_int_support = SIMD_x86_veqinstr.keys()

# Total list of which floating point array types are supported by x86 SIMD instructions.
SIMD_x86_float_support = SIMD_x86_float_ops.keys()



# ==============================================================================


# ==============================================================================

# For ARM NEON.
# Benchmarking has shown that some SIMD operations are slower than the
# non-SIMD versions and so are not used here.

arm_simdattr = {
	'b' : 'int8x8_t',
	'B' : 'uint8x8_t',
	'h' : 'int16x4_t',
	'H' : 'uint16x4_t',
}


arm_simdrsltattr = {
	'b' : 'uint8x8_t',
	'B' : 'uint8x8_t',
	'h' : 'uint16x4_t',
	'H' : 'uint16x4_t',
}

# Load values to SIMD registers.
arm_vldinstr = {
	'b' : 'vld1_s8',
	'B' : 'vld1_u8',
	'h' : 'vld1_s16',
	'H' : 'vld1_u16',
}


# Compare result to see if OK. This depends both on size and also
# 'ne' must be handled differently. 

# aall
arm_vresult_8_aall = 'vreinterpret_u64_u8(resultslice) != 0xffffffffffffffff'
arm_vresult_16_aall = 'vreinterpret_u64_u16(resultslice) != 0xffffffffffffffff'
arm_vresult_8_ne_aall = 'vreinterpret_u64_u8(resultslice) != 0x0000000000000000'
arm_vresult_16_ne_aall = 'vreinterpret_u64_u16(resultslice) != 0x0000000000000000'

arm_vreslt_8_total_aall = {
		'eq' : arm_vresult_8_aall,
		'ge' : arm_vresult_8_aall,
		'gt' : arm_vresult_8_aall,
		'le' : arm_vresult_8_aall,
		'lt' : arm_vresult_8_aall,
		'ne' : arm_vresult_8_ne_aall,
		}

arm_vreslt_16_total_aall = {
		'eq' : arm_vresult_16_aall,
		'ge' : arm_vresult_16_aall,
		'gt' : arm_vresult_16_aall,
		'le' : arm_vresult_16_aall,
		'lt' : arm_vresult_16_aall,
		'ne' : arm_vresult_16_ne_aall,
		}

# aany
arm_vresult_8_aany = 'vreinterpret_u64_u8(resultslice) != 0x0000000000000000'
arm_vresult_16_aany = 'vreinterpret_u64_u16(resultslice) != 0x0000000000000000'
arm_vresult_8_ne_aany = 'vreinterpret_u64_u8(resultslice) != 0xffffffffffffffff'
arm_vresult_16_ne_aany = 'vreinterpret_u64_u16(resultslice) != 0xffffffffffffffff'

arm_vreslt_8_total_aany = {
		'eq' : arm_vresult_8_aany,
		'ge' : arm_vresult_8_aany,
		'gt' : arm_vresult_8_aany,
		'le' : arm_vresult_8_aany,
		'lt' : arm_vresult_8_aany,
		'ne' : arm_vresult_8_ne_aany,
		}

arm_vreslt_16_total_aany = {
		'eq' : arm_vresult_16_aany,
		'ge' : arm_vresult_16_aany,
		'gt' : arm_vresult_16_aany,
		'le' : arm_vresult_16_aany,
		'lt' : arm_vresult_16_aany,
		'ne' : arm_vresult_16_ne_aany,
		}

# findindex
arm_vresult_8_findindex = 'vreinterpret_u64_u8(resultslice) != 0x0000000000000000'
arm_vresult_16_findindex = 'vreinterpret_u64_u16(resultslice) != 0x0000000000000000'
arm_vresult_8_ne_findindex = 'vreinterpret_u64_u8(resultslice) != 0xffffffffffffffff'
arm_vresult_16_ne_findindex = 'vreinterpret_u64_u16(resultslice) != 0xffffffffffffffff'

arm_vreslt_8_total_findindex = {
		'eq' : arm_vresult_8_findindex,
		'ge' : arm_vresult_8_findindex,
		'gt' : arm_vresult_8_findindex,
		'le' : arm_vresult_8_findindex,
		'lt' : arm_vresult_8_findindex,
		'ne' : arm_vresult_8_ne_findindex,
		}

arm_vreslt_16_total_findindex = {
		'eq' : arm_vresult_16_findindex,
		'ge' : arm_vresult_16_findindex,
		'gt' : arm_vresult_16_findindex,
		'le' : arm_vresult_16_findindex,
		'lt' : arm_vresult_16_findindex,
		'ne' : arm_vresult_16_ne_findindex,
		}



arm_vresult = {
	'b' : {'aall' : arm_vreslt_8_total_aall, 
			'aany' : arm_vreslt_8_total_aany,
			'findindex' : arm_vreslt_8_total_findindex},
	'B' : {'aall' : arm_vreslt_8_total_aall, 
			'aany' : arm_vreslt_8_total_aany, 
			'findindex' : arm_vreslt_8_total_findindex},
	'h' : {'aall' : arm_vreslt_16_total_aall, 
			'aany' : arm_vreslt_16_total_aany, 
			'findindex' : arm_vreslt_16_total_findindex},
	'H' : {'aall' : arm_vreslt_16_total_aall, 
			'aany' : arm_vreslt_16_total_aany, 
			'findindex' : arm_vreslt_16_total_findindex},
}



# The ARM SIMD ops for compare. The NE op must be combined with a 
# different vresult as there is no actual not equal op.
arm_simdops = {
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
SIMD_arm_support = arm_simdattr.keys()


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

# Return the platform SIMD enable C macro. 
# This is for the platform independent file, and not the plaform specific
# SIMD files.
def findsimdplatform(arraycode):

	# The calls to SIMD support code are platform dependent.
	if (arraycode in SIMD_x86_support) and (arraycode not in SIMD_arm_support):
		return SIMD_platform_x86
	elif (arraycode in SIMD_x86_support) and (arraycode in SIMD_arm_support):
		return SIMD_platform_x86_ARM
	else:
		return 'Error: Template error, this should not be here.'

# ==============================================================================

# ==============================================================================


maindescription = 'Returns True if all elements in an array meet the selected criteria.'

# The original date of the platform independent C code.
ccodedate = '08-May-2014'

# The original date of the SIMD C code.
simdcodedate = '01-May-2017'


# The functions which are implemented by this program.
completefuncnames = ('aall', 'aany', 'findindex')

# The non-SIMD implementation of the operation. 
ops_calls = {'aall' : ops_aall, 
			'aany' : ops_aany, 
			'findindex' : ops_findindex
}

# The SIMD implementation of the operation for x86-64. 
ops_calls_simd_x86 = {'aall' : ops_aall_simd_x86, 
			'aany' : ops_aany_simd_x86, 
			'findindex' : ops_findindex_simd_x86
}


# The SIMD implementation of the operation for arm. 
ops_calls_simd_arm = {'aall' : ops_aall_simd_arm, 
			'aany' : ops_aany_simd_arm, 
			'findindex' : ops_findindex_simd_arm
}


# The return codes for each function.
resultcodetemplates = {'aall' : 'signed int', 
			'aany' : 'signed int', 
			'findindex' : 'Py_ssize_t'
}

# The comparison operator names and symbols.
operations = (('eq', '=='), ('gt', '>'), ('ge', '>='), ('lt', '<'), ('le', '<='), ('ne', '!='))


# Used for the help text in the function.
aany_docs = '''* result - A boolean value corresponding to the result of all the \\n\\
  comparison operations. If any comparison operations result in true, \\n\\
  the return value will be true. If all of them result in false, the \\n\\
  return value will be false.'''

aall_docs = '''* result - A boolean value corresponding to the result of all the \\n\\
  comparison operations. If all comparison operations result in true, \\n\\
  the return value will be true. If any of them result in false, the \\n\\
  return value will be false.'''

findindex_docs = '* result - The resulting index. This will be negative if no match was found.'

resultdoc = {'aall' : aany_docs, 
			'aany' : aall_docs, 
			'findindex' : findindex_docs
}

opcodedocs = {'aall' : 'all([(x > param) for x in array])', 
			'aany' : 'any([(x > param) for x in array])', 
			'findindex' : '[x for x,y in enumerate(array) if y > param][0]'
}


# ==============================================================================



# ==============================================================================
# This outputs the non-SIMD version.
# Output the generated code.


# Output the functions which implement the individual non-SIMD 
# implementation functions.
for funcname in completefuncnames:

	filename = funcname + '.c'

	# Select the implementation template for the current function.
	optemplate = ops_calls[funcname]

	with open(filename, 'w') as f:
		f.write(allany_head % {'funclabel' : funcname})

		# Each type of array.
		for arraycode in codegen_common.arraycodes:
			arraytype = codegen_common.arraytypes[arraycode]
			funcmodifier = arraytype.replace(' ', '_')

			# Each compare operation.
			for opcode, compareop in operations:

				f.write(optemplate % {'arraycode' : arraycode, 
							'arraytype' : arraytype, 
							'funcmodifier' : funcmodifier, 
							'opcode' : opcode,
							'compare_ops' : compareop})
		
			# Prepare the SIMD templates.
			if (arraycode in SIMD_x86_support) or (arraycode in SIMD_arm_support):

				simd_call_base = {'simdwidth' : simdwidth[arraycode], 
						'funclabel' : funcname, 
						'opcode' : '', 
						'funcmodifier' : funcmodifier,
						'simdplatform' : findsimdplatform(arraycode)}


				simd_call_base.update({'opcode' : 'eq'})
				simd_call_eq = simd_call_template % simd_call_base
				simd_call_base.update({'opcode' : 'gt'})
				simd_call_gt = simd_call_template % simd_call_base
				simd_call_base.update({'opcode' : 'ge'})
				simd_call_ge = simd_call_template % simd_call_base
				simd_call_base.update({'opcode' : 'lt'})
				simd_call_lt = simd_call_template % simd_call_base
				simd_call_base.update({'opcode' : 'le'})
				simd_call_le = simd_call_template % simd_call_base
				simd_call_base.update({'opcode' : 'ne'})
				simd_call_ne = simd_call_template % simd_call_base
			else:
				simd_call_eq = ''
				simd_call_gt = ''
				simd_call_ge = ''
				simd_call_lt = ''
				simd_call_le = ''
				simd_call_ne = ''


			# Select the individual operation via a dictionary.
			f.write(case_ops % {'arraycode' : arraycode, 
								'arraytype' : arraytype, 
								'funclabel' : funcname,
								'funcmodifier' : arraytype.replace(' ', '_'), 
								'resultcode' : resultcodetemplates[funcname],
								'simd_call_eq' : simd_call_eq,
								'simd_call_gt' : simd_call_gt,
								'simd_call_ge' : simd_call_ge,
								'simd_call_lt' : simd_call_lt,
								'simd_call_le' : simd_call_le,
								'simd_call_ne' : simd_call_ne,
								})

		#####

		# The program entry point and parameter parsing and code.
		f.write(allany_params % {'funclabel' : funcname,
								'return_result' : return_templates[funcname],
								'opcodedocs' : opcodedocs[funcname],
								'resultdoc' : resultdoc[funcname],
								'resultcode' : resultcodetemplates[funcname],
								})



# ==============================================================================

# ==============================================================================

# This outputs the SIMD version for x86-64.

# The original date of the SIMD C code.
simdcodedate = '16-Apr-2019'
simdfilename = '_simd_x86'

for funcname in completefuncnames:

	outputlist = []


	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname



	# Select the implementation template for the current function.
	optemplate = ops_calls_simd_x86[funcname]

	# Output the generated code for supported x86 SIMD instructions.
	for arraycode in SIMD_x86_support:


		arraytype = codegen_common.arraytypes[arraycode]

		# Each compare operation.
		for opcode, compareop in operations:

			# Data for both integer and floating point.
			simddata = {'arraycode' : arraycode, 
						'arraytype' : arraytype, 
						'funcmodifier' : arraytype.replace(' ', '_'), 
						'opcode' : opcode,
						'compare_ops' : compareop,
						'simdwidth' : simdwidth[arraycode],
						'simdattr' : x86_simdattr[arraycode],
						'vldinstr' : x86_vldinstr[arraycode],
						}

			# For integer arrays only.
			if arraycode in SIMD_x86_int_support:

				# This fetches the individual SIMD instructions.
				template_instr = {'veqinstr' : SIMD_x86_veqinstr[arraycode],
								'vmininstr' : SIMD_x86_vmininstr[arraycode],
								'vmaxinstr' : SIMD_x86_vmaxinstr[arraycode],
								'vgtinstr' : SIMD_x86_vgtinstr[arraycode],
								}

				simddata['SIMD_x86_ops'] = SIMD_x86_SIMD_int_templates[arraycode][funcname][opcode] % template_instr
				simddata['SIMD_x86_compslice'] = SIMD_x86_compslice[arraycode][funcname][opcode]


			# Handle floating point operations.
			elif (arraycode in SIMD_x86_float_support):

				template_instr = {'vcmpinstr' : SIMD_x86_float_ops[arraycode][opcode]}
				template_float = SIMD_x86_SIMD_float_templates[funcname] % template_instr

				simddata['SIMD_x86_ops'] = template_float
				simddata['SIMD_x86_compslice'] = ''



			# Add the completed template to the accumulated list.
			outputlist.append(optemplate % simddata)



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

# This outputs the SIMD version for ARM NEON.

# The original date of the SIMD C code.
simdcodedate = '07-Oct-2019'
simdfilename = '_simd_arm'

for funcname in completefuncnames:

	outputlist = []


	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname



	# Select the implementation template for the current function.
	optemplate = ops_calls_simd_arm[funcname]

	# Output the generated code.
	for arraycode in SIMD_arm_support:

		arraytype = codegen_common.arraytypes[arraycode]

		# Each compare operation.
		for opcode, compareop in operations:

			# The compare_ops symbols is the same for integer and floating point.
			datavals = {'funclabel' : funcname,
						'arraytype' : arraytype, 
						'funcmodifier' : arraytype.replace(' ', '_'),
						'simdwidth' : simdwidth[arraycode],
						'arraycode' : arraycode,
						'arraytype' : codegen_common.arraytypes[arraycode],
						'opcode' : opcode,
						'compare_ops' : compareop,
						'simdattr' : arm_simdattr[arraycode],
						'simdrsltattr' : arm_simdrsltattr[arraycode],
						'vldinstr' : arm_vldinstr[arraycode],
						'vresult' : arm_vresult[arraycode][funcname][opcode],
						'SIMD_ARM_comp' : arm_simdops[arraycode][opcode],
						}

			# Start of function definition.
			outputlist.append(optemplate % datavals)



	# This outputs the SIMD version.
	codegen_common.OutputSourceCode(funcname + simdfilename + '.c', outputlist, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate,
		'', ['simddefs', 'simdmacromsg_arm'])


	# Output the .h header file.
	headedefs = codegen_common.GenSIMDCHeaderText(outputlist, funcname)

	# Write out the file.
	codegen_common.OutputCHeader(funcname + simdfilename + '.h', headedefs, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate)

# ==============================================================================

