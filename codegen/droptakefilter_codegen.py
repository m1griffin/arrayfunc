#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for afilter, dropwhile, and takewhile.
# Language: Python 3.5
# Date:     10-May-2014
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

import codegen_common

# ==============================================================================


droptakefilter_head = """//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   %(funclabel)s.c
// Purpose:  %(opcodedocs1)s
//           %(opcodedocs2)s
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

#include "arrayerrs.h"
#include "arrayparams_base.h"
#include "arrayops.h"

#include "arrayparams_droptakefilter.h"

/*--------------------------------------------------------------------------- */
"""

# ==============================================================================


# The basic template for dropwhile.
ops_dropwhile = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t dropwhile_%(opcode)s_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s *dataout, %(arraytype)s param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] %(compare_ops)s param1)) {
			break;
		}
	}
	for(; index < arraylen; index++) {
		dataout[outindex] = data[index];
		outindex++;
	}
	return outindex;

}
"""

# The basic template for takewhile.
ops_takewhile = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_%(opcode)s_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s *dataout, %(arraytype)s param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] %(compare_ops)s param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}
"""


# The basic template for afilter.
ops_afilter = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t afilter_%(opcode)s_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s *dataout, %(arraytype)s param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	for(index = 0; index < arraylen; index++) {
		if (data[index] %(compare_ops)s param1) {
			dataout[outindex] = data[index];
			outindex++;
		}
	}
	return outindex;

}
"""

# ==============================================================================


# ==============================================================================

case_ops = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t %(funclabel)s_select_%(funcmodifier)s(signed int opcode, Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s *dataout, %(arraytype)s param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return %(funclabel)s_eq_%(funcmodifier)s(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return %(funclabel)s_gt_%(funcmodifier)s(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return %(funclabel)s_ge_%(funcmodifier)s(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return %(funclabel)s_lt_%(funcmodifier)s(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return %(funclabel)s_le_%(funcmodifier)s(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return %(funclabel)s_ne_%(funcmodifier)s(arraylen, data, dataout, param1);
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


droptakefilter_params = """
/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	Py_ssize_t resultcode = 0;

	// This is used to hold the parsed parameters.
	struct args_params_droptakefilter arraydata = ARGSINIT_DROPTAKEFILTER;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_droptakefilter(self, args, keywds, "%(funclabel)s");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}


	// The length of the data array.
	if (arraydata.arraylength < 1) {
		// Release the buffers. 
		releasebuffers_droptakefilter(arraydata);
		ErrMsgArrayLengthErr();
		return NULL;
	}



	/* Call the C function */
	switch(arraydata.arraytype) {
		// signed char
		case 'b' : {
			resultcode = %(funclabel)s_select_signed_char(arraydata.opcode, arraydata.arraylength, arraydata.array1.b, arraydata.array2.b, arraydata.param.b);
			break;
		}
		// unsigned char
		case 'B' : {
			resultcode = %(funclabel)s_select_unsigned_char(arraydata.opcode, arraydata.arraylength, arraydata.array1.B, arraydata.array2.B, arraydata.param.B);
			break;
		}
		// signed short
		case 'h' : {
			resultcode = %(funclabel)s_select_signed_short(arraydata.opcode, arraydata.arraylength, arraydata.array1.h, arraydata.array2.h, arraydata.param.h);
			break;
		}
		// unsigned short
		case 'H' : {
			resultcode = %(funclabel)s_select_unsigned_short(arraydata.opcode, arraydata.arraylength, arraydata.array1.H, arraydata.array2.H, arraydata.param.H);
			break;
		}
		// signed int
		case 'i' : {
			resultcode = %(funclabel)s_select_signed_int(arraydata.opcode, arraydata.arraylength, arraydata.array1.i, arraydata.array2.i, arraydata.param.i);
			break;
		}
		// unsigned int
		case 'I' : {
			resultcode = %(funclabel)s_select_unsigned_int(arraydata.opcode, arraydata.arraylength, arraydata.array1.I, arraydata.array2.I, arraydata.param.I);
			break;
		}
		// signed long
		case 'l' : {
			resultcode = %(funclabel)s_select_signed_long(arraydata.opcode, arraydata.arraylength, arraydata.array1.l, arraydata.array2.l, arraydata.param.l);
			break;
		}
		// unsigned long
		case 'L' : {
			resultcode = %(funclabel)s_select_unsigned_long(arraydata.opcode, arraydata.arraylength, arraydata.array1.L, arraydata.array2.L, arraydata.param.L);
			break;
		}
		// signed long long
		case 'q' : {
			resultcode = %(funclabel)s_select_signed_long_long(arraydata.opcode, arraydata.arraylength, arraydata.array1.q, arraydata.array2.q, arraydata.param.q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultcode = %(funclabel)s_select_unsigned_long_long(arraydata.opcode, arraydata.arraylength, arraydata.array1.Q, arraydata.array2.Q, arraydata.param.Q);
			break;
		}
		// float
		case 'f' : {
			resultcode = %(funclabel)s_select_float(arraydata.opcode, arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.param.f);
			break;
		}
		// double
		case 'd' : {
			resultcode = %(funclabel)s_select_double(arraydata.opcode, arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.param.d);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_droptakefilter(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_droptakefilter(arraydata);


	// Return the number of items filtered through.
	return PyLong_FromSsize_t(resultcode);


}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(%(funclabel)s__doc__,
"%(funclabel)s \\n\\
_____________________________ \\n\\
\\n\\
%(opcodedocs1)s \\n\\
%(opcodedocs2)s \\n\\
\\n\\
======================  ============================================== \\n\\
Equivalent to:          %(equivdoc)s \\n\\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \\n\\
Exceptions raised:      None \\n\\
======================  ============================================== \\n\\
\\n\\
Call formats: \\n\\
\\n\\
  result = %(funclabel)s(opstr, array, outparray, param) \\n\\
  result = %(funclabel)s(opstr, array, outparray, param, maxlen=y) \\n\\
\\n\\
* opstr - The arithmetic comparison operation as a string. \\n\\
          These are: '==', '>', '>=', '<', '<=', '!='. \\n\\
* array - The input data array to be examined. \\n\\
* outparray - The output array. \\n\\
* param - A non-array numeric parameter. \\n\\
* maxlen - Limit the length of the array used. This must be a valid \\n\\
  positive integer. If a zero or negative length, or a value which is \\n\\
  greater than the actual length of the array is specified, this \\n\\
  parameter is ignored. \\n\\
* result - An integer count of the number of items filtered into outparray. \\n\\
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


maindescription = 'Copy values from an array, starting from where a condition fails to the end.'

# The original date of the platform independent C code.
ccodedate = '10-May-2014'


# The functions which are implemented by this program.
completefuncnames = ('dropwhile', 'takewhile', 'afilter')


# The implementation of the operation. 
ops_calls = {'dropwhile' : ops_dropwhile, 
			'takewhile' : ops_takewhile,
			'afilter' : ops_afilter
}

# The comparison operator names and symbols.
operations = (('eq', '=='), ('gt', '>'), ('ge', '>='), ('lt', '<'), ('le', '<='), ('ne', '!='))

# The description used in the help function.
opcodedocs1 = {'dropwhile' : 'Select values from an array starting from where a selected criteria', 
			'takewhile' : 'Select values from an array starting from the beginning and stopping',
			'afilter' : 'Select values from an array based on a boolean criteria.'
}

opcodedocs2 = {'dropwhile' : 'fails and proceeding to the end.', 
			'takewhile' : 'when the criteria fails.',
			'afilter' : ''
}



# Documentation for the equivalent function.
equivdoc = {'dropwhile' : 'itertools.dropwhile(lambda x: x < param, array)', 
			'takewhile' : 'itertools.takewhile(lambda x: x < param, array)',
			'afilter' : 'filter(lambda x: x < param, array)'
}

# ==============================================================================

# Output the functions which implement the individual  
# implementation functions.
for funcname in completefuncnames:

	filename = funcname + '.c'

	# Select the implementation template for the current function.
	optemplate = ops_calls[funcname]

	with open(filename, 'w') as f:
		f.write(droptakefilter_head % {'funclabel' : funcname,
									'opcodedocs1' : opcodedocs1[funcname],
									'opcodedocs2' : opcodedocs2[funcname]})

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
		

			# Select the individual operation via a switch.
			f.write(case_ops % {'arraycode' : arraycode, 
								'arraytype' : arraytype, 
								'funclabel' : funcname,
								'funcmodifier' : arraytype.replace(' ', '_'), 
								})

		#####

		# The program entry point and parameter parsing and code.
		f.write(droptakefilter_params % {'funclabel' : funcname,
								'opcodedocs1' : opcodedocs1[funcname],
								'opcodedocs2' : opcodedocs2[funcname],
								'equivdoc' : equivdoc[funcname]
								})



# ==============================================================================
