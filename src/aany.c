//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   aany.c
// Purpose:  Returns True if any element in an array meets the selected criteria.
// Language: C
// Date:     04-May-2014
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2018    Michael Griffin    <m12.griffin@gmail.com>
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
#include "aany_common.h"

/*--------------------------------------------------------------------------- */


// Provide a struct for returning data from parsing Python arguments.
struct args_param {
	char array1type;
	char param1type;
	char error;
};

// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist[] = {"op", "data", "param", "maxlen", "nosimd", NULL};


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

	PyObject *dataobj, *param1obj, *opstr;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	struct args_param argtypes = {' ', ' ', 0};
	char arraycode;
	unsigned int nosimd = 0;


	/* Import the raw objects. */
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "UOO|ni:aany", kwlist, 
			&opstr, &dataobj, &param1obj, &arraymaxlen, &nosimd)) {
		argtypes.error = 1;
		return argtypes;
	}

	// Test if the second parameter is an array.
	arraycode = lookuparraycode(dataobj);
	if (!arraycode) {
		argtypes.error = 2;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.array1type = arraycode;
	}


	// Get the parameter type codes.
	argtypes.param1type = paramtypecode(param1obj);


	return argtypes;

}



/*--------------------------------------------------------------------------- */


/* The wrapper to the underlying C function */
static PyObject *py_aany(PyObject *self, PyObject *args, PyObject *keywds)
{


	// The array of data we work on. 
	union dataarrays data;

	// The input buffers are arrays of bytes.
	Py_buffer datapy;

	// The length of the data array.
	Py_ssize_t databufflength;

	// Codes indicating the type of array and the operation desired.
	char itemcode;
	signed int opcode;
	PyObject *opstr;

	// How long the array is.
	Py_ssize_t arraylength;
	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

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
	signed int resultcode;

	// If true, disable using SIMD.
	unsigned int nosimd = 0;

	// -------------------------------------------------------------------------


	// Check the parameters to see what they are.
	argtypes = parsepyargs_parm(args, keywds);



	// There was an error reading the parameter types.
	if (argtypes.error) {
		ErrMsgParameterError();
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
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*l|ni:aany", kwlist, 
					&opstr, &datapy, &param1tmp_l, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(issignedcharrange(param1tmp_l))) {
				PyBuffer_Release(&datapy);
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
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*l|ni:aany", kwlist, 
					&opstr, &datapy, &param1tmp_l, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isunsignedcharrange(param1tmp_l))) {
				PyBuffer_Release(&datapy);
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
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*h|ni:aany", kwlist, 
					&opstr, &datapy, &param1py.h, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			break;
		}
		// unsigned short
		case 'H' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*l|ni:aany", kwlist, 
					&opstr, &datapy, &param1tmp_l, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isunsignedshortrange(param1tmp_l))) {
				PyBuffer_Release(&datapy);
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
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*i|ni:aany", kwlist, 
					&opstr, &datapy, &param1py.i, &arraymaxlen, &nosimd)) {
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
				if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*l|ni:aany", kwlist, 
						&opstr, &datapy, &param1tmp_l, &arraymaxlen, &nosimd)) {
					return NULL;
				}
				// Check the data range manually.
				if (!(isunsignedintrange(param1tmp_l))) {
					PyBuffer_Release(&datapy);
					ErrMsgArithOverflowParam();
					return NULL;
				} else {
					param1py.I = (unsigned int) param1tmp_l;
				}
			} else {
				// The format string and parameter names depend on the expected data types.
				if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*I|ni:aany", kwlist, 
						&opstr, &datapy, &param1py.I, &arraymaxlen, &nosimd)) {
					return NULL;
				}
			}
			break;
		}
		// signed long
		case 'l' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*l|ni:aany", kwlist, 
					&opstr, &datapy, &param1py.l, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			break;
		}
		// unsigned long
		case 'L' : {
			// The format string and parameter names depend on the expected data types.
			// We don't have a guaranteed data size larger than unsigned long, so
			// we can't manually range check it.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*k|ni:aany", kwlist, 
					&opstr, &datapy, &param1py.L, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			break;
		}
		// signed long long
		case 'q' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*L|ni:aany", kwlist, 
					&opstr, &datapy, &param1py.q, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			break;
		}
		// unsigned long long
		case 'Q' : {
			// The format string and parameter names depend on the expected data types.
			// We don't have a guaranteed data size larger than unsigned long, so
			// we can't manually range check it.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*K|ni:aany", kwlist, 
					&opstr, &datapy, &param1py.Q, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			break;
		}
		// float
		case 'f' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*f|ni:aany", kwlist, 
					&opstr, &datapy, &param1py.f, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isfinite(param1py.f))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			}
			break;
		}
		// double
		case 'd' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "Uy*d|ni:aany", kwlist, 
					&opstr, &datapy, &param1py.d, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isfinite(param1py.d))) {
				PyBuffer_Release(&datapy);
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
		ErrMsgOperatorNotValidforthisFunction();
		return NULL;
	}

	// Assign the buffer to a union which lets us get at them as typed data.
	data.buf = datapy.buf;

	// The length of the data array.
	databufflength = datapy.len;
	arraylength = calcarraylength(itemcode, databufflength);
	if (arraylength < 1) {
		// Release the buffers. 
		PyBuffer_Release(&datapy);
		ErrMsgArrayLengthErr();
		return NULL;
	}


	// Adjust the length of array being operated on, if necessary.
	arraylength = adjustarraymaxlen(arraylength, arraymaxlen);


	/* Call the C function */
	switch(itemcode) {
		// signed char
		case 'b' : {
			resultcode = aany_signed_char(opcode, arraylength, data.b, param1py.b, nosimd);
			break;
		}
		// unsigned char
		case 'B' : {
			resultcode = aany_unsigned_char(opcode, arraylength, data.B, param1py.B);
			break;
		}
		// signed short
		case 'h' : {
			resultcode = aany_signed_short(opcode, arraylength, data.h, param1py.h, nosimd);
			break;
		}
		// unsigned short
		case 'H' : {
			resultcode = aany_unsigned_short(opcode, arraylength, data.H, param1py.H);
			break;
		}
		// signed int
		case 'i' : {
			resultcode = aany_signed_int(opcode, arraylength, data.i, param1py.i, nosimd);
			break;
		}
		// unsigned int
		case 'I' : {
			resultcode = aany_unsigned_int(opcode, arraylength, data.I, param1py.I);
			break;
		}
		// signed long
		case 'l' : {
			resultcode = aany_signed_long(opcode, arraylength, data.l, param1py.l);
			break;
		}
		// unsigned long
		case 'L' : {
			resultcode = aany_unsigned_long(opcode, arraylength, data.L, param1py.L);
			break;
		}
		// signed long long
		case 'q' : {
			resultcode = aany_signed_long_long(opcode, arraylength, data.q, param1py.q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultcode = aany_unsigned_long_long(opcode, arraylength, data.Q, param1py.Q);
			break;
		}
		// float
		case 'f' : {
			resultcode = aany_float(opcode, arraylength, data.f, param1py.f, nosimd);
			break;
		}
		// double
		case 'd' : {
			resultcode = aany_double(opcode, arraylength, data.d, param1py.d, nosimd);
			break;
		}
		// We don't know this code.
		default: {
			PyBuffer_Release(&datapy);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}


	// Release the buffers. 
	PyBuffer_Release(&datapy);

	// Signal the errors.
	if (resultcode == ARR_ERR_INVALIDOP) {
		ErrMsgOperatorNotValidforthisFunction();
		return NULL;
	}

	// Return whether found or not.
	if (resultcode == ARR_ERR_NOTFOUND) {
		Py_RETURN_FALSE;
	} else {
		Py_RETURN_TRUE;
	}



}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(aany__doc__,
"Returns True if any element in an array meets the selected criteria.\n\
\n\
x = aany(op, inparray, rparam)\n\
x = aany(op, inparray, rparam, maxlen=y)\n\
\n\
* op - The arithmetic comparison operation.\n\
* inparray - The input data array to be examined.\n\
* rparam - The parameter to be applied to 'op'. \n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored. \n\
* nosimd - If true, disable SIMD. \n\
* x - The boolean result.");


/* A list of all the methods defined by this module. 
 "aany" is the name seen inside of Python. 
 "py_aany" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef aany_methods[] = {
	{"aany",  (PyCFunction) py_aany, METH_VARARGS | METH_KEYWORDS, aany__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef aanymodule = {
    PyModuleDef_HEAD_INIT,
    "aany",
    NULL,
    -1,
    aany_methods
};

PyMODINIT_FUNC PyInit_aany(void)
{
    return PyModule_Create(&aanymodule);
};

/*--------------------------------------------------------------------------- */
