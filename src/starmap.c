//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   starmap.c
// Purpose:  Iterate math operations over an array using a second array.
// Language: C
// Date:     11-May-2014.
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

#include "starmap_common.h"
#include "arrayerrs.h"
#include "arrayfunc.h"

/*--------------------------------------------------------------------------- */

// Provide a struct for returning data from parsing Python arguments.
struct args_param {
	char array1type;
	char array2type;
	char array3type;
	char error;
};

// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist[] = {"opcode", "data", "data2", "dataout", "disovfl", "maxlen", NULL};

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

	PyObject *dataobj, *data2obj, *dataoutobj;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	struct args_param argtypes = {' ', ' ', ' ', 0};
	struct arrayparamstypes arr1type = {0, 0, ' '};
	struct arrayparamstypes arr2type = {0, 0, ' '};
	struct arrayparamstypes arr3type = {0, 0, ' '};
	signed int opcode;
	unsigned int disableovfl = 0;


	/* Import the raw objects. */
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "iOOO|in:starmap", kwlist, &opcode, &dataobj, 
							&data2obj, &dataoutobj, &disableovfl, &arraymaxlen)) {
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


	// Test if the third parameter is an array or bytes.
	arr2type = paramarraytype(data2obj);
	if (!arr2type.isarray) {
		argtypes.error = 3;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.array2type = arr2type.arraycode;
	}


	// Test if the fourth parameter is an array or bytes.
	arr3type = paramarraytype(dataoutobj);
	if (!arr3type.isarray) {
		argtypes.error = 4;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.array3type = arr3type.arraycode;
	}


	return argtypes;

}


/*--------------------------------------------------------------------------- */


/* The wrapper to the underlying C function */
static PyObject *py_starmap(PyObject *self, PyObject *args, PyObject *keywds) {


	// The array of data we work on. 
	union dataarrays data, data2, dataout;

	// The input buffers are arrays of bytes.
	Py_buffer datapy, data2py, dataoutpy;

	// The length of the data array.
	Py_ssize_t databufflength, data2bufflength, dataoutbufflength;

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

	// All array types must be the same.
	if ((argtypes.array1type != argtypes.array2type) || (argtypes.array1type != argtypes.array3type)) {
		ErrMsgArrayTypeMismatch();
		return NULL;
	}


	// The item code tells us what data type we are handling.
	itemcode = argtypes.array1type;


	// Since all the parameters are either arrays or known data types, we
	// can parse all the different parameter types with one format string.
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*y*y*|in:starmap", kwlist, 
			&opcode, &datapy, &data2py, &dataoutpy, &disableovfl, &arraymaxlen)) {
		return NULL;
	}


	// Assign the buffer to a union which lets us get at them as typed data.
	data.buf = datapy.buf;
	data2.buf = data2py.buf;
	dataout.buf = dataoutpy.buf;


	// The length of the data array.
	databufflength = datapy.len;
	data2bufflength = data2py.len;
	dataoutbufflength = dataoutpy.len;
	arraylength = calcarraylength(itemcode, databufflength);
	if (arraylength < 1) {
		// Release the buffers. 
		PyBuffer_Release(&datapy);
		PyBuffer_Release(&data2py);
		PyBuffer_Release(&dataoutpy);
		ErrMsgArrayLengthErr();
		return NULL;
	}

	// Check to make sure the input and output arrays are of equal length.
	if ((databufflength != data2bufflength) || (databufflength != dataoutbufflength)) {
		// Release the buffers. 
		PyBuffer_Release(&datapy);
		PyBuffer_Release(&data2py);
		PyBuffer_Release(&dataoutpy);
		ErrMsgArrayLengthMismatch();
		return NULL;
	}


	// Adjust the length of array being operated on, if necessary.
	arraylength = adjustarraymaxlen(arraylength, arraymaxlen);


	resultcode = -1;

	/* Call the C function */
	switch(itemcode) {
		// signed char
		case 'b' : {
			resultcode = starmap_signed_char(opcode, arraylength, data.b, data2.b, dataout.b, disableovfl);
			break;
		}
		// unsigned char
		case 'B' : {
			resultcode = starmap_unsigned_char(opcode, arraylength, data.B, data2.B, dataout.B, disableovfl);
			break;
		}
		// signed short
		case 'h' : {
			resultcode = starmap_signed_short(opcode, arraylength, data.h, data2.h, dataout.h, disableovfl);
			break;
		}
		// unsigned short
		case 'H' : {
			resultcode = starmap_unsigned_short(opcode, arraylength, data.H, data2.H, dataout.H, disableovfl);
			break;
		}
		// signed int
		case 'i' : {
			resultcode = starmap_signed_int(opcode, arraylength, data.i, data2.i, dataout.i, disableovfl);
			break;
		}
		// unsigned int
		case 'I' : {
			resultcode = starmap_unsigned_int(opcode, arraylength, data.I, data2.I, dataout.I, disableovfl);
			break;
		}
		// signed long
		case 'l' : {
			resultcode = starmap_signed_long(opcode, arraylength, data.l, data2.l, dataout.l, disableovfl);
			break;
		}
		// unsigned long
		case 'L' : {
			resultcode = starmap_unsigned_long(opcode, arraylength, data.L, data2.L, dataout.L, disableovfl);
			break;
		}
		// signed long long
		case 'q' : {
			resultcode = starmap_signed_long_long(opcode, arraylength, data.q, data2.q, dataout.q, disableovfl);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultcode = starmap_unsigned_long_long(opcode, arraylength, data.Q, data2.Q, dataout.Q, disableovfl);
			break;
		}
		// float
		case 'f' : {
			resultcode = starmap_float(opcode, arraylength, data.f, data2.f, dataout.f, disableovfl);
			break;
		}
		// double
		case 'd' : {
			resultcode = starmap_double(opcode, arraylength, data.d, data2.d, dataout.d, disableovfl);
			break;
		}
		// We don't know this code.
		default: {
			PyBuffer_Release(&datapy);
			PyBuffer_Release(&data2py);
			PyBuffer_Release(&dataoutpy);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	PyBuffer_Release(&datapy);
	PyBuffer_Release(&data2py);
	PyBuffer_Release(&dataoutpy);


	// Signal the errors.
	switch (resultcode) {
		case ARR_ERR_INVALIDOP : {
			ErrMsgOperatorNotValidforthisFunction();
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
	}


	// Everything was successful.
	Py_RETURN_NONE;

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(starmap__doc__,
"Apply an operator to each element of an array, using the corresponding \n\
element from a second array as the second parameter The results are \n\
written to a third array.\n\
All valid operators and math functions must take a second parameter.\n\
\n\
starmap(op, inparray1, inparray2, outparray)\n\
starmap(op, inparray1, inparray2, outparray, disovfl=True)\n\
starmap(op, inparray1, inparray2, outparray, disovfl=True, maxlen=y)\n\
\n\
* op - The arithmetic comparison operation.\n\
* inparray1 - The first input data array to be examined.\n\
* inparray2 - The second input data array to be examined.\n\
* outparray - The output array.\n\
* disovfl - If this keyword parameter is True, integer overflow checking \n\
  will be disabled. This is an optional parameter.\n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored.");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "starmap" is the name seen inside of Python. 
 "py_starmap" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef starmap_methods[] = {
	{"starmap",  (PyCFunction)py_starmap, METH_VARARGS | METH_KEYWORDS, starmap__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef starmapmodule = {
    PyModuleDef_HEAD_INIT,
    "starmap",
    NULL,
    -1,
    starmap_methods
};

PyMODINIT_FUNC PyInit_starmap(void)
{
    return PyModule_Create(&starmapmodule);
};

/*--------------------------------------------------------------------------- */
