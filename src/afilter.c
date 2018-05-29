//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   afilter.c
// Purpose:  Filter based on a test condition.
// Language: C
// Date:     09-May-2014
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2017    Michael Griffin    <m12.griffin@gmail.com>
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
#include "afilter_common.h"

/*--------------------------------------------------------------------------- */


// Provide a struct for returning data from parsing Python arguments.
struct args_param {
	char array1type;
	char array2type;
	char param1type;
	char error;
};

// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist[] = {"op", "data", "dataout", "param", "maxlen", NULL};

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

/* Parse the Python arguments to objects, and then extract the object parameters
 * to determine their types. This lets us handle different data types as 
 * parameters.
 * This version expects the following parameters:
 * args (PyObject) = The positional arguments.
 * Returns a structure containing the results of each parameter.
*/
struct args_param parsepyargs_parm(PyObject *args, PyObject *keywds) {

	PyObject *dataobj, *dataoutobj, *param1obj, *opstr;


	struct args_param argtypes = {' ', ' ', ' ', 0};
	char array1code, array2code;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;


	/* Import the raw objects. */
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "UOOO|n:afilter", kwlist, 
			&opstr, &dataobj, &dataoutobj, &param1obj, &arraymaxlen)) {
		argtypes.error = 1;
		return argtypes;
	}


	// Test if the second parameter is an array.
	array1code = lookuparraycode(dataobj);
	if (!array1code) {
		argtypes.error = 2;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.array1type = array1code;
	}


	// Test if the third parameter is an array.
	array2code = lookuparraycode(dataoutobj);
	if (!array2code) {
		argtypes.error = 3;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.array2type = array2code;
	}


	// Get the parameter type codes.
	argtypes.param1type = paramtypecode(param1obj);


	return argtypes;

}


/*--------------------------------------------------------------------------- */


/* The wrapper to the underlying C function */
static PyObject *py_afilter(PyObject *self, PyObject *args, PyObject *keywds) {


	// The array of data we work on. 
	union dataarrays data, dataout;

	// The input buffers are arrays of bytes.
	Py_buffer datapy, dataoutpy;

	// The length of the data array.
	Py_ssize_t databufflength, dataoutbufflength;


	// Codes indicating the type of array and the operation desired.
	char itemcode;
	signed int opcode;
	PyObject *opstr;


	// The parameter version is available in all possible types.
	struct paramsvals param1py;

	// PyArg_ParseTuple does not match directly to the array codes. We need to
	// use some temporary variables of alternate types to parse the parameter 
	// data.
	// PyArg_ParseTuple does not check for overflow of unsigned parameters.
	signed long param1tmp_l;

	// This is used to hold the results from inspecting the Python args.
	struct args_param argtypes;

	// The error code returned by the function.
	Py_ssize_t resultcode;

	// How long the array is.
	Py_ssize_t arraylength;
	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	// -------------------------------------------------------------------------


	// Check the parameters to see what they are.
	argtypes = parsepyargs_parm(args, keywds);



	// There was an error reading the parameter types.
	if (argtypes.error) {
		ErrMsgParameterError();
		return NULL;
	}

	// Both array types must be the same.
	if (argtypes.array1type != argtypes.array2type) {
		ErrMsgArrayTypeMismatch();
		return NULL;
	}

	// Check if the array and parameter types are compatible.
	if (!paramcompatok(argtypes.array1type, argtypes.param1type)) {
		ErrMsgArrayAndParamMismatch();
		return NULL;
	}

	itemcode = argtypes.array1type;

	// Now we will fetch the actual data depending on the array type.
	switch (itemcode) {
		// signed char
		case 'b' : {
			// There does not seem to be a format string for signed char, so we must use a larger type
			// and check it manually. 
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*y*l|n:afilter", kwlist, 
					&opstr, &datapy, &dataoutpy, &param1tmp_l, &arraymaxlen)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(issignedcharrange(param1tmp_l))) {
				PyBuffer_Release(&datapy);
				PyBuffer_Release(&dataoutpy);
				ErrMsgArithOverflowParam();
				return NULL;
			} else {
				param1py.b = (signed char) param1tmp_l;
			}
			break;
		}
		// unsigned char
		case 'B' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*y*l|n:afilter", kwlist, 
					&opstr, &datapy, &dataoutpy, &param1tmp_l, &arraymaxlen)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isunsignedcharrange(param1tmp_l))) {
				PyBuffer_Release(&datapy);
				PyBuffer_Release(&dataoutpy);
				ErrMsgArithOverflowParam();
				return NULL;
			} else {
				param1py.B = (unsigned char) param1tmp_l;
			}
			break;
		}
		// signed short
		case 'h' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*y*h|n:afilter", kwlist, 
					&opstr, &datapy, &dataoutpy, &param1py.h, &arraymaxlen)) {
				return NULL;
			}
			break;
		}
		// unsigned short
		case 'H' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*y*l|n:afilter", kwlist, 
					&opstr, &datapy, &dataoutpy, &param1tmp_l, &arraymaxlen)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isunsignedshortrange(param1tmp_l))) {
				PyBuffer_Release(&datapy);
				PyBuffer_Release(&dataoutpy);
				ErrMsgArithOverflowParam();
				return NULL;
			} else {
				param1py.H = (unsigned short) param1tmp_l;
			}
			break;
		}
		// signed int
		case 'i' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*y*i|n:afilter", kwlist, 
					&opstr, &datapy, &dataoutpy, &param1py.i, &arraymaxlen)) {
				return NULL;
			}
			break;
		}
		// unsigned int
		case 'I' : {
			// With architectures where signed long is larger than unsigned int, we
			// can use the larger signed value to test for overflow. If they are the
			// same size, then we cannot check for overflow.
			if (sizeof(signed long) > sizeof(unsigned int)) {
				// The format string and parameter names depend on the expected data types.
				if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*y*l|n:afilter", kwlist, 
						&opstr, &datapy, &dataoutpy, &param1tmp_l, &arraymaxlen)) {
					return NULL;
				}
				// Check the data range manually.
				if (!(isunsignedintrange(param1tmp_l))) {
					PyBuffer_Release(&datapy);
					PyBuffer_Release(&dataoutpy);
					ErrMsgArithOverflowParam();
					return NULL;
				} else {
					param1py.I = (unsigned int) param1tmp_l;
				}
			} else {
				// The format string and parameter names depend on the expected data types.
				if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*y*I|n:afilter", kwlist, 
						&opstr, &datapy, &dataoutpy, &param1py.I, &arraymaxlen)) {
					return NULL;
				}
			}
			break;
		}
		// signed long
		case 'l' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*y*l|n:afilter", kwlist, 
					&opstr, &datapy, &dataoutpy, &param1py.l, &arraymaxlen)) {
				return NULL;
			}
			break;
		}
		// unsigned long
		case 'L' : {
			// The format codes do NOT match the array codes for this type.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*y*k|n:afilter", kwlist, 
					&opstr, &datapy, &dataoutpy, &param1py.L, &arraymaxlen)) {
				return NULL;
			}
			break;
		}
		// signed long long
		case 'q' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*y*L|n:afilter", kwlist, 
					&opstr, &datapy, &dataoutpy, &param1py.q, &arraymaxlen)) {
				return NULL;
			}
			break;
		}
		// unsigned long long
		case 'Q' : {
			// The format codes do NOT match the array codes for this type.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*y*K|n:afilter", kwlist, 
					&opstr, &datapy, &dataoutpy, &param1py.Q, &arraymaxlen)) {
				return NULL;
			}
			break;
		}
		// float
		case 'f' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*y*f|n:afilter", kwlist, 
					&opstr, &datapy, &dataoutpy, &param1py.f, &arraymaxlen)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isfinite(param1py.f))) {
				PyBuffer_Release(&datapy);
				PyBuffer_Release(&dataoutpy);
				ErrMsgArithOverflowParam();
				return NULL;
			}
			break;
		}
		// double
		case 'd' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*y*d|n:afilter", kwlist, 
					&opstr, &datapy, &dataoutpy, &param1py.d, &arraymaxlen)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isfinite(param1py.d))) {
				PyBuffer_Release(&datapy);
				PyBuffer_Release(&dataoutpy);
				ErrMsgArithOverflowParam();
				return NULL;
			}
			break;
		}
		// We don't know this code.
		default: {
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}


	// Convert the command string to an integer.
	opcode = opstrdecode(opstr);

	// Check if the command string is valid.
	if (opcode < 0) {
		// Release the buffers. 
		PyBuffer_Release(&datapy);
		PyBuffer_Release(&dataoutpy);
		ErrMsgOperatorNotValidforthisFunction();
		return NULL;
	}


	// Assign the buffer to a union which lets us get at them as typed data.
	data.buf = datapy.buf;
	dataout.buf = dataoutpy.buf;

	// The length of the data array.
	databufflength = datapy.len;
	dataoutbufflength = dataoutpy.len;
	arraylength = calcarraylength(itemcode, databufflength);

	if (arraylength < 1) {
		// Release the buffers. 
		PyBuffer_Release(&datapy);
		PyBuffer_Release(&dataoutpy);
		ErrMsgArrayLengthErr();
		return NULL;
	}


	if (databufflength != dataoutbufflength) {
		// Release the buffers. 
		PyBuffer_Release(&datapy);
		PyBuffer_Release(&dataoutpy);
		ErrMsgArrayLengthMismatch();
		return NULL;
	}


	// Adjust the length of array being operated on, if necessary.
	arraylength = adjustarraymaxlen(arraylength, arraymaxlen);



	/* Call the C function */
	switch(itemcode) {
		// signed char
		case 'b' : {
			resultcode = afilter_signed_char(opcode, arraylength, data.b, dataout.b, param1py.b);
			break;
		}
		// unsigned char
		case 'B' : {
			resultcode = afilter_unsigned_char(opcode, arraylength, data.B, dataout.B, param1py.B);
			break;
		}
		// signed short
		case 'h' : {
			resultcode = afilter_signed_short(opcode, arraylength, data.h, dataout.h, param1py.h);
			break;
		}
		// unsigned short
		case 'H' : {
			resultcode = afilter_unsigned_short(opcode, arraylength, data.H, dataout.H, param1py.H);
			break;
		}
		// signed int
		case 'i' : {
			resultcode = afilter_signed_int(opcode, arraylength, data.i, dataout.i, param1py.i);
			break;
		}
		// unsigned int
		case 'I' : {
			resultcode = afilter_unsigned_int(opcode, arraylength, data.I, dataout.I, param1py.I);
			break;
		}
		// signed long
		case 'l' : {
			resultcode = afilter_signed_long(opcode, arraylength, data.l, dataout.l, param1py.l);
			break;
		}
		// unsigned long
		case 'L' : {
			resultcode = afilter_unsigned_long(opcode, arraylength, data.L, dataout.L, param1py.L);
			break;
		}
		// signed long long
		case 'q' : {
			resultcode = afilter_signed_long_long(opcode, arraylength, data.q, dataout.q, param1py.q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultcode = afilter_unsigned_long_long(opcode, arraylength, data.Q, dataout.Q, param1py.Q);
			break;
		}
		// float
		case 'f' : {
			resultcode = afilter_float(opcode, arraylength, data.f, dataout.f, param1py.f);
			break;
		}
		// double
		case 'd' : {
			resultcode = afilter_double(opcode, arraylength, data.d, dataout.d, param1py.d);
			break;
		}
		// We don't know this code.
		default: {
			PyBuffer_Release(&datapy);
			PyBuffer_Release(&dataoutpy);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}


	// Release the buffers. 
	PyBuffer_Release(&datapy);
	PyBuffer_Release(&dataoutpy);

	// Signal the errors.
	if (resultcode == ARR_ERR_INVALIDOP) {
		ErrMsgOperatorNotValidforthisFunction();
		return NULL;
	}

	// Return the number of items filtered through.
	return PyLong_FromSsize_t(resultcode);


}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(afilter__doc__,
"Select values from an array based on a boolean criteria.\n\
\n\
x = afilter(op, inparray, outparray, rparam)\n\
x = afilter(op, inparray, outparray, rparam, maxlen=y)\n\
\n\
* op - The arithmetic comparison operation.\n\
* inparray - The input data array to be filtered.\n\
* outparray - The output array.\n\
* rparam - The parameter to be applied to 'op'. \n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored. \n\
* x - An integer count of the number of items filtered into outparray.");


/* A list of all the methods defined by this module. 
 "afilter" is the name seen inside of Python. 
 "py_afilter" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef afilter_methods[] = {
	{"afilter",  (PyCFunction) py_afilter, METH_VARARGS | METH_KEYWORDS, afilter__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef afiltermodule = {
    PyModuleDef_HEAD_INIT,
    "afilter",
    NULL,
    -1,
    afilter_methods
};

PyMODINIT_FUNC PyInit_afilter(void)
{
    return PyModule_Create(&afiltermodule);
};

/*--------------------------------------------------------------------------- */
