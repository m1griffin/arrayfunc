#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for findindices.
# Language: Python 3.5
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

findindices_head = """//------------------------------------------------------------------------------
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

#include "arrayparams_findindices.h"


/*--------------------------------------------------------------------------- */
"""

# ==============================================================================

# The basic template for the non-SIMD version of findindex.
ops_findindices = """
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
Py_ssize_t findindices_%(opcode)s_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, signed long long *dataout, %(arraytype)s param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] %(compare_ops)s param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

}
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
Py_ssize_t findindices_select_%(funcmodifier)s(signed int opcode, Py_ssize_t arraylen, %(arraytype)s *data, signed long long *dataout, %(arraytype)s param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return findindices_eq_%(funcmodifier)s(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return findindices_gt_%(funcmodifier)s(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return findindices_ge_%(funcmodifier)s(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return findindices_lt_%(funcmodifier)s(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return findindices_le_%(funcmodifier)s(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return findindices_ne_%(funcmodifier)s(arraylen, data, dataout, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */
"""


# ==============================================================================



findindices_params = """
/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	Py_ssize_t resultcode = 0;

	// This is used to hold the parsed parameters.
	struct args_params_findindices arraydata = ARGSINIT_FINDINDICES;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_findindices(self, args, keywds, "%(funclabel)s");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}


	// The length of the data array.
	if (arraydata.arraylength < 1) {
		// Release the buffers. 
		releasebuffers_findindices(arraydata);
		ErrMsgArrayLengthErr();
		return NULL;
	}



	/* Call the C function */
	switch(arraydata.arraytype) {
		// signed char
		case 'b' : {
			resultcode = findindices_select_signed_char(arraydata.opcode, arraydata.arraylength, arraydata.array1.b, arraydata.array2.q, arraydata.param.b);
			break;
		}
		// unsigned char
		case 'B' : {
			resultcode = findindices_select_unsigned_char(arraydata.opcode, arraydata.arraylength, arraydata.array1.B, arraydata.array2.q, arraydata.param.B);
			break;
		}
		// signed short
		case 'h' : {
			resultcode = findindices_select_signed_short(arraydata.opcode, arraydata.arraylength, arraydata.array1.h, arraydata.array2.q, arraydata.param.h);
			break;
		}
		// unsigned short
		case 'H' : {
			resultcode = findindices_select_unsigned_short(arraydata.opcode, arraydata.arraylength, arraydata.array1.H, arraydata.array2.q, arraydata.param.H);
			break;
		}
		// signed int
		case 'i' : {
			resultcode = findindices_select_signed_int(arraydata.opcode, arraydata.arraylength, arraydata.array1.i, arraydata.array2.q, arraydata.param.i);
			break;
		}
		// unsigned int
		case 'I' : {
			resultcode = findindices_select_unsigned_int(arraydata.opcode, arraydata.arraylength, arraydata.array1.I, arraydata.array2.q, arraydata.param.I);
			break;
		}
		// signed long
		case 'l' : {
			resultcode = findindices_select_signed_long(arraydata.opcode, arraydata.arraylength, arraydata.array1.l, arraydata.array2.q, arraydata.param.l);
			break;
		}
		// unsigned long
		case 'L' : {
			resultcode = findindices_select_unsigned_long(arraydata.opcode, arraydata.arraylength, arraydata.array1.L, arraydata.array2.q, arraydata.param.L);
			break;
		}
		// signed long long
		case 'q' : {
			resultcode = findindices_select_signed_long_long(arraydata.opcode, arraydata.arraylength, arraydata.array1.q, arraydata.array2.q, arraydata.param.q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultcode = findindices_select_unsigned_long_long(arraydata.opcode, arraydata.arraylength, arraydata.array1.Q, arraydata.array2.q, arraydata.param.Q);
			break;
		}
		// float
		case 'f' : {
			resultcode = findindices_select_float(arraydata.opcode, arraydata.arraylength, arraydata.array1.f, arraydata.array2.q, arraydata.param.f);
			break;
		}
		// double
		case 'd' : {
			resultcode = findindices_select_double(arraydata.opcode, arraydata.arraylength, arraydata.array1.d, arraydata.array2.q, arraydata.param.d);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_findindices(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_findindices(arraydata);


	// Signal the errors.
	if (resultcode == ARR_ERR_INVALIDOP) {
		ErrMsgOperatorNotValidforthisFunction();
		return NULL;
	}


	// Adjust the result code if the data was not found, so that we don't leak
	// internal error codes to user space (and cause problems if they change).
	if (resultcode < 0) {
		resultcode = -1;
	}

	// Return the number of items filtered through.
	return PyLong_FromSsize_t(resultcode);

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(%(funclabel)s__doc__,
"%(funclabel)s \\n\\
_____________________________ \\n\\
\\n\\
Searches an array for the array indices which meet the specified \\n\\
criteria and writes the results to a second array. Also returns the \\n\\
number of matches found. \\n\\
\\n\\
======================  ============================================== \\n\\
Equivalent to:          [x for x,y in enumerate(inparray) if y == param] \\n\\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \\n\\
======================  ============================================== \\n\\
\\n\\
Call formats: \\n\\
\\n\\
  result = %(funclabel)s(opstr, array, arrayout, param) \\n\\
  result = %(funclabel)s(opstr, array, arrayout, param, maxlen=y) \\n\\
\\n\\
* opstr - The arithmetic comparison operation as a string. \\n\\
          These are: '==', '>', '>=', '<', '<=', '!='. \\n\\
* array - The input data array to be examined. \\n\\
* arrayout - The output array. This must be an integer array of array \\n\\
  type 'q' (signed long long). \\n\\
* param - A non-array numeric parameter. \\n\\
* maxlen - Limit the length of the array used. This must be a valid \\n\\
  positive integer. If a zero or negative length, or a value which is \\n\\
  greater than the actual length of the array is specified, this \\n\\
  parameter is ignored. \\n\\
* result - An integer indicating the number of matches found. \\n\\
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


# The comparison operator names and symbols.
operations = (('eq', '=='), ('gt', '>'), ('ge', '>='), ('lt', '<'), ('le', '<='), ('ne', '!='))

# ==============================================================================

funcname = 'findindices'

filename = funcname + '.c'


with open(filename, 'w') as f:
	f.write(findindices_head % {'funclabel' : funcname})

	# Each type of array.
	for arraycode in codegen_common.arraycodes:
		arraytype = codegen_common.arraytypes[arraycode]
		funcmodifier = arraytype.replace(' ', '_')

		# Each compare operation.
		for opcode, compareop in operations:

			f.write(ops_findindices % {'arraycode' : arraycode, 
						'arraytype' : arraytype, 
						'funcmodifier' : funcmodifier, 
						'opcode' : opcode,
						'compare_ops' : compareop})

		# Select the individual operation via a switch.
		f.write(case_ops % {'arraycode' : arraycode, 
							'arraytype' : arraytype, 
							'funclabel' : funcname,
							'funcmodifier' : funcmodifier, 
							})

	#####

	# The program entry point and parameter parsing and code.
	f.write(findindices_params % {'funclabel' : funcname})

# ==============================================================================
