//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   amapi.c
// Purpose:  Iterate math operations over an array.
// Language: C
// Date:     09-Apr-2014
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2015    Michael Griffin    <m12.griffin@gmail.com>
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

#include "amap_common.h"
#include "arrayerrs.h"
#include "arrayfunc.h"

/*--------------------------------------------------------------------------- */

// Provide a struct for returning data from parsing Python arguments.
struct args_param {
	char array1type;
	char paramtype;
	char error;
};

// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist[] = {"opcode", "data", "param", "disovfl", "maxlen", NULL};

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* Parse the Python arguments to objects, and then extract the object parameters
 * to determine their types. This lets us handle different data types as 
 * parameters.
 * This version expects the following parameters:
 * args (PyObject) = The positional arguments.
 * keywds (PyObject) = The keyword arguments.
 * Returns a structure containing the results of each parameter.
*/
struct args_param parsepyargs_parm(PyObject *args, PyObject *keywds) {

	PyObject *dataobj;

	// We need to initialise the optional parameter to a known value, so we
	// can test if it was changed.
	PyObject *paramobj = NULL;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	struct args_param argtypes = {' ', ' ', 0};
	struct arrayparamstypes arr1type = {0, 0, ' '};
	signed int opcode;

	unsigned int disableovfl = 0;


	/* Import the raw objects. */
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "iO|Oin:amapi", kwlist, &opcode, &dataobj, 
							&paramobj, &disableovfl, &arraymaxlen)) {
		argtypes.error = 1;
		return argtypes;
	}


	// Test if the second parameter is an array or bytes.
	arr1type = paramarraytype(dataobj);
	if (!arr1type.isarray) {
		argtypes.error = 2;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.array1type = arr1type.arraycode;
	}


	// The parameter is optional, so we have to test if it was set.
	if (paramobj != NULL) {
		argtypes.paramtype = paramtypecode(paramobj->ob_type->tp_name);
	} else {
		argtypes.paramtype = 'z';
	}

	return argtypes;

}


/*--------------------------------------------------------------------------- */


/* The wrapper to the underlying C function */
static PyObject *py_amapi(PyObject *self, PyObject *args, PyObject *keywds) {


	// The array of data we work on. 
	union dataarrays data;

	// The input buffers are arrays of bytes.
	Py_buffer datapy;

	// The length of the data array.
	Py_ssize_t databufflength;

	// The parameter version is available in all possible types.
	struct paramsvals param1py;

	// PyArg_ParseTuple does not match directly to the array codes. We need to
	// use some temporary variables of alternate types to parse the parameter 
	// data.
	// PyArg_ParseTuple does not check for overflow of unsigned parameters.
	signed long param1tmp_l = 0;

	// This is used to hold the results from inspecting the Python args.
	struct args_param argtypes;

	// Codes indicating the type of array and the operation desired.
	char itemcode;
	signed int opcode;
	// If true, *disabled* overflow checking.
	unsigned int disableovfl = 0;

	// How long the array is.
	Py_ssize_t arraylength;
	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	// The number of parameters present.
	unsigned int paramcount;


	// The error code returned by the function.
	signed int resultcode;



	// -----------------------------------------------------


	// Check the parameters to see what they are.
	argtypes = parsepyargs_parm(args, keywds);

	// There was an error reading the parameter types.
	if (argtypes.error) {
		ErrMsgParameterError();
		return NULL;
	}


	// Check if the array and parameter types are compatible.
	// The second parameter (step) was not specified.
	if (argtypes.paramtype == 'z') {
		paramcount = 0;

		param1py.b = 1;
		param1py.B = 1;
		param1py.h = 1;
		param1py.H = 1;
		param1py.i = 1;
		param1py.I = 1;
		param1py.l = 1;
		param1py.L = 1;
		param1py.q = 1;
		param1py.Q = 1;
		param1py.f = 1.0;
		param1py.d = 1.0;


	} else {
		// The parameter was specified. 
		if (!paramcompatok(argtypes.array1type, argtypes.paramtype)) {
			ErrMsgArrayAndParamMismatch();
			return NULL;
		}
		paramcount = 1;
	}


	itemcode = argtypes.array1type;

	// Now we will fetch the actual data depending on the array type.
	switch (itemcode) {
		// signed char
		case 'b' : {
			// There does not seem to be a format string for signed char, so we must use a larger type
			// and check it manually. 
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*|lin:amapi", kwlist, 
					&opcode, &datapy, &param1tmp_l, &disableovfl, &arraymaxlen)) {
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
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*|lin:amapi", kwlist, 
					&opcode, &datapy, &param1tmp_l, &disableovfl, &arraymaxlen)) {
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
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*|hin:amapi", kwlist, 
					&opcode, &datapy, &param1py.h, &disableovfl, &arraymaxlen)) {
				return NULL;
			}
			break;
		}
		// unsigned short
		case 'H' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*|lin:amapi", kwlist, 
					&opcode, &datapy, &param1tmp_l, &disableovfl, &arraymaxlen)) {
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
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*|iin:amapi", kwlist, 
					&opcode, &datapy, &param1py.i, &disableovfl, &arraymaxlen)) {
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
				if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*|lin:amapi", kwlist, 
						&opcode, &datapy, &param1tmp_l, &disableovfl, &arraymaxlen)) {
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
				if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*|Iin:amapi", kwlist, 
						&opcode, &datapy, &param1py.I, &disableovfl, &arraymaxlen)) {
					return NULL;
				}
			}
			break;
		}
		// signed long
		case 'l' : {
			// The format codes do NOT match the array codes for this type.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*|lin:amapi", kwlist, 
					&opcode, &datapy, &param1py.l, &disableovfl, &arraymaxlen)) {
				return NULL;
			}
			break;
		}
		// unsigned long
		case 'L' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*|kin:amapi", kwlist, 
					&opcode, &datapy, &param1py.L, &disableovfl, &arraymaxlen)) {
				return NULL;
			}
			break;
		}
		// signed long long
		case 'q' : {
			// The format codes do NOT match the array codes for this type.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*|Lin:amapi", kwlist, 
					&opcode, &datapy, &param1py.q, &disableovfl, &arraymaxlen)) {
				return NULL;
			}
			break;
		}
		// unsigned long long
		case 'Q' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*|Kin:amapi", kwlist, 
					&opcode, &datapy, &param1py.Q, &disableovfl, &arraymaxlen)) {
				return NULL;
			}
			break;
		}
		// float
		case 'f' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*|fin:amapi", kwlist, 
					&opcode, &datapy, &param1py.f, &disableovfl, &arraymaxlen)) {
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
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*|din:amapi", kwlist, 
					&opcode, &datapy, &param1py.d, &disableovfl, &arraymaxlen)) {
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


	resultcode = -1;

	/* Call the C function */
	switch(itemcode) {
		// signed char
		case 'b' : {
			resultcode = map_signed_char(opcode, arraylength, data.b, data.b, param1py.b, paramcount, disableovfl);
			break;
		}
		// unsigned char
		case 'B' : {
			resultcode = map_unsigned_char(opcode, arraylength, data.B, data.B, param1py.B, paramcount, disableovfl);
			break;
		}
		// signed short
		case 'h' : {
			resultcode = map_signed_short(opcode, arraylength, data.h, data.h, param1py.h, paramcount, disableovfl);
			break;
		}
		// unsigned short
		case 'H' : {
			resultcode = map_unsigned_short(opcode, arraylength, data.H, data.H, param1py.H, paramcount, disableovfl);
			break;
		}
		// signed int
		case 'i' : {
			resultcode = map_signed_int(opcode, arraylength, data.i, data.i, param1py.i, paramcount, disableovfl);
			break;
		}
		// unsigned int
		case 'I' : {
			resultcode = map_unsigned_int(opcode, arraylength, data.I, data.I, param1py.I, paramcount, disableovfl);
			break;
		}
		// signed long
		case 'l' : {
			resultcode = map_signed_long(opcode, arraylength, data.l, data.l, param1py.l, paramcount, disableovfl);
			break;
		}
		// unsigned long
		case 'L' : {
			resultcode = map_unsigned_long(opcode, arraylength, data.L, data.L, param1py.L, paramcount, disableovfl);
			break;
		}
		// signed long long
		case 'q' : {
			resultcode = map_signed_long_long(opcode, arraylength, data.q, data.q, param1py.q, paramcount, disableovfl);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultcode = map_unsigned_long_long(opcode, arraylength, data.Q, data.Q, param1py.Q, paramcount, disableovfl);
			break;
		}
		// float
		case 'f' : {
			resultcode = map_float(opcode, arraylength, data.f, data.f, (float) param1py.f, paramcount, disableovfl);
			break;
		}
		// double
		case 'd' : {
			resultcode = map_double(opcode, arraylength, data.d, data.d, param1py.d, paramcount, disableovfl);
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
	switch (resultcode) {
		case ARR_ERR_INVALIDOP : {
			ErrMsgOperatorNotValidforthisFunction();
			return NULL;
		}
		case ARR_ERR_PLATFORM : {
			ErrMsgOperatorNotValidforthisPlatform();
			return NULL;
		}
		case ARR_ERR_OVFL : {
			ErrMsgArithOverflowCalc();
			return NULL;
		}
		case ARR_ERR_ARITHMETIC : {
			ErrMsgArithCalc();
			return NULL;
		}
		case ARR_ERR_VALUE_ERR: {
			ErrMsgParameterNotValidforthisOperation();
			return NULL;
		}
		case ARR_ERR_PARAMMISSING : {
			ErrMsgParameterMissing();
			return NULL;
		}
	}


	// Everything was successful.
	Py_RETURN_NONE;

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(amapi__doc__,
"Apply an operator to each element of an array, together with an \n\
optional second parameter (for operators taking two parameters). The \n\
results are written to the input array.\n\
\n\
amapi(op, inparray, rparam)\n\
amapi(op, inparray, rparam, disovfl=True)\n\
amapi(op, inparray, rparam, disovfl=True, maxlen=y)\n\
\n\
* op - The arithmetic comparison operation.\n\
* inparray - The input data array to be examined.\n\
* rparam - The parameter to be applied to 'op'. This is an optional \n\
  parameter.\n\
* disovfl - If this keyword parameter is True, integer overflow checking \n\
  will be disabled. This is an optional parameter.\n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored.");

/*--------------------------------------------------------------------------- */


/* A list of all the methods defined by this module. 
 "amapi" is the name seen inside of Python. 
 "py_amapi" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef amapi_methods[] = {
	{"amapi",  (PyCFunction)py_amapi, METH_VARARGS | METH_KEYWORDS, amapi__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef amapimodule = {
    PyModuleDef_HEAD_INIT,
    "amapi",
    NULL,
    -1,
    amapi_methods
};

PyMODINIT_FUNC PyInit_amapi(void)
{
    return PyModule_Create(&amapimodule);
};


/*--------------------------------------------------------------------------- */
