#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for aall, aany, findindex.
# Language: Python 3.4
# Date:     11-Jun-2014
#
###############################################################################
#
#   Copyright 2014 - 2017    Michael Griffin    <m12.griffin@gmail.com>
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

#ifdef AF_HASSIMD
#include "%(funclabel)s_simd_x86.h"
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

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] %(compare_ops)s param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}
	return 1;

}
"""


# The basic template for the SIMD version of aall.
ops_aall_simd = """
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
#ifdef AF_HASSIMD
signed int aall_%(opcode)s_%(funcmodifier)s_simd(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright, resultslice;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param1;
	}
	datasliceright = (%(simdattr)s) %(simdload)s(%(simdcast)scompvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += %(simdwidth)s) {
		datasliceleft = (%(simdattr)s) %(simdload)s(%(simdcast)s&data[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft %(compare_ops)s datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data[index] %(compare_ops)s param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif

"""


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

	for(index = 0; index < arraylen; index++) {
		if (data[index] %(compare_ops)s param1) {
			return 1;
		}
	}
	return ARR_ERR_NOTFOUND;

}
"""

# The basic template for the SIMD version of aany.
ops_aany_simd = """
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
#ifdef AF_HASSIMD
signed int aany_%(opcode)s_%(funcmodifier)s_simd(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright, resultslice;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param1;
	}
	datasliceright = (%(simdattr)s) %(simdload)s(%(simdcast)scompvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += %(simdwidth)s) {
		datasliceleft = (%(simdattr)s) %(simdload)s(%(simdcast)s&data[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft %(compare_ops)s datasliceright;
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (data[index] %(compare_ops)s param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif

"""


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

		for(index = 0; index < arraylen; index++) {
			if (data[index] %(compare_ops)s param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}
"""


# The basic template for the SIMD version of findindex.
ops_findindex_simd = """
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
#ifdef AF_HASSIMD
Py_ssize_t findindex_%(opcode)s_%(funcmodifier)s_simd(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright, resultslice;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param1;
	}
	datasliceright = (%(simdattr)s) %(simdload)s(%(simdcast)scompvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += %(simdwidth)s) {
		datasliceleft = (%(simdattr)s) %(simdload)s(%(simdcast)s&data[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft %(compare_ops)s datasliceright;
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			// Home in on the exact location.
			for(fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] %(compare_ops)s param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
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
simd_call_template = '''#ifdef AF_HASSIMD
			// SIMD version.
			if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
				return %(funclabel)s_%(opcode)s_%(funcmodifier)s_simd(arraylen, data, param1);
			}
#endif'''


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

# The SIMD implementation of the operation. 
ops_calls_simd = {'aall' : ops_aall_simd, 
			'aany' : ops_aany_simd, 
			'findindex' : ops_findindex_simd
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

# Various SIMD instruction information which varies according to array type.
simdvalues = {
'b' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v16qi', 'simdwidth' : 'CHARSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu'},
'B' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v16qi', 'simdwidth' : 'CHARSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu'},
'h' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v8hi', 'simdwidth' : 'SHORTSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu'},
'H' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v8hi', 'simdwidth' : 'SHORTSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu'},
'i' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v4si', 'simdwidth' : 'INTSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu'},
'I' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v4si', 'simdwidth' : 'INTSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu'},
'l' : {'hassimd' : False},
'L' : {'hassimd' : False},
'q' : {'hassimd' : False},
'Q' : {'hassimd' : False},
'f' : {'hassimd' : True, 'simdcast' : '', 'simdattr' : 'v4sf', 'simdwidth' : 'FLOATSIMDSIZE', 'simdload' : '__builtin_ia32_loadups'},
'd' : {'hassimd' : True, 'simdcast' : '', 'simdattr' : 'v2df', 'simdwidth' : 'DOUBLESIMDSIZE', 'simdload' : '__builtin_ia32_loadupd'},
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
			if simdvalues[arraycode]['hassimd']:
				simd_call_base = {'simdwidth' : simdvalues[arraycode]['simdwidth'], 
						'funclabel' : funcname, 
						'opcode' : '', 
						'funcmodifier' : funcmodifier}
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


			# Select the individual operation via a switch.
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
# This outputs the SIMD version.

# The original date of the SIMD C code.
simdcodedate = '16-Apr-2019'
simdfilename = '_simd_x86'

# This outputs the SIMD version.

for funcname in completefuncnames:

	outputlist = []


	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname



	# Select the implementation template for the current function.
	optemplate = ops_calls_simd[funcname]

	# Output the generated code.
	for arraycode in codegen_common.arraycodes:

		arraytype = codegen_common.arraytypes[arraycode]

		if simdvalues[arraycode]['hassimd']:

			# Each compare operation.
			for opcode, compareop in operations:

				outputlist.append(optemplate % {'arraycode' : arraycode, 
							'arraytype' : arraytype, 
							'funcmodifier' : arraytype.replace(' ', '_'), 
							'opcode' : opcode,
							'compare_ops' : compareop,
							'simdattr' : simdvalues[arraycode]['simdattr'],
							'simdwidth' : simdvalues[arraycode]['simdwidth'],
							'simdload' : simdvalues[arraycode]['simdload'],
							'simdcast' : simdvalues[arraycode]['simdcast'],
							})



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

