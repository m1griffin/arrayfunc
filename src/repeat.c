//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   repeat.c
// Purpose:  Fill an array with a specified value.
// Language: C
// Date:     04-May-2014.
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

#include "arrayfunc.h"
#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// Provide a struct for returning data from parsing Python arguments.
struct args_param {
	char array1type;
	char paramtype;
	char error;
};

/*--------------------------------------------------------------------------- */

// Auto-generated code goes below.

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_signed_char(Py_ssize_t arraylen, signed char *data, signed char fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_signed_short(Py_ssize_t arraylen, signed short *data, signed short fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_signed_int(Py_ssize_t arraylen, signed int *data, signed int fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_signed_long(Py_ssize_t arraylen, signed long *data, signed long fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_float(Py_ssize_t arraylen, float *data, float fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_double(Py_ssize_t arraylen, double *data, double fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

/* Parse the Python arguments to objects, and then extract the object parameters
 * to determine their types. This lets us handle different data types as 
 * parameters.
 * This version expects the following parameters:
 * 	dataobj (array) = An array of any type.
 * 	paramobj (integer or float) = An integer or floating point (double) 
 * 		parameter which is the array fill value.
 * Returns a structure containing the results of each parameter.
*/
struct args_param parsepyargs_parm(PyObject *args) {

	PyObject *dataobj, *paramobj;
	struct args_param argtypes = {' ', ' ', 0};
	struct arrayparamstypes arr1type = {0, 0, ' '};


	/* Import the raw objects. */
	if (!PyArg_ParseTuple(args, "OO|:repeat", &dataobj, &paramobj)) {
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


	// Get the parameter type code.
	argtypes.paramtype = paramtypecode(paramobj->ob_type->tp_name);

	return argtypes;

}


/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */


/* The wrapper to the underlying C function */
static PyObject *
py_repeat(PyObject *self, PyObject *args)
{


	// The array of data we work on. 
	union dataarrays data;

	// The input buffers are arrays of bytes.
	Py_buffer datapy;

	// The length of the data array.
	Py_ssize_t databufflength;

	// Codes indicating the type of array and the operation desired.
	char itemcode;

	// How long the array is.
	Py_ssize_t arraylength;

	// The parameter version is available in all possible types.
	struct paramsvals param1py;

	// PyArg_ParseTuple does not match directly to the array codes. We need to
	// use some temporary variables of alternate types to parse the parameter 
	// data.
	// PyArg_ParseTuple does not check for overflow of unsigned parameters.
	signed long param1tmp_l;


	// This is used to hold the results from inspecting the Python args.
	struct args_param argtypes;


	// -------------------------------------------------------------------------

	// Check the parameters to see what they are.
	argtypes = parsepyargs_parm(args);


	// There was an error reading the parameter types.
	if (argtypes.error) {
		ErrMsgParameterError();
		return NULL;
	}



	// Check if the array and parameter types are compatible.
	if (!paramcompatok(argtypes.array1type, argtypes.paramtype)) {
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
			if (!PyArg_ParseTuple(args, "y*l|:repeat", &datapy, &param1tmp_l)) {
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
			if (!PyArg_ParseTuple(args, "y*l|:repeat", &datapy, &param1tmp_l)) {
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
			if (!PyArg_ParseTuple(args, "y*h|:repeat", &datapy, &param1py.h)) {
				return NULL;
			}
			break;
		}
		// unsigned short
		case 'H' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*l|:repeat", &datapy, &param1tmp_l)) {
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
			if (!PyArg_ParseTuple(args, "y*i|:repeat", &datapy, &param1py.i)) {
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
				if (!PyArg_ParseTuple(args, "y*l|:repeat", &datapy, &param1tmp_l)) {
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
				if (!PyArg_ParseTuple(args, "y*I|:repeat", &datapy, &param1py.I)) {
					return NULL;
				}
			}
			break;
		}
		// signed long
		case 'l' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*l|:repeat", &datapy, &param1py.l)) {
				return NULL;
			}
			break;
		}
		// unsigned long
		case 'L' : {
			// The format codes do NOT match the array codes for this type.
			if (!PyArg_ParseTuple(args, "y*k|:repeat", &datapy, &param1py.L)) {
				return NULL;
			}
			break;
		}
		// signed long
		case 'q' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*L|:repeat", &datapy, &param1py.q)) {
				return NULL;
			}
			break;
		}
		// unsigned long
		case 'Q' : {
			// The format codes do NOT match the array codes for this type.
			if (!PyArg_ParseTuple(args, "y*K|:repeat", &datapy, &param1py.Q)) {
				return NULL;
			}
			break;
		}
		// float
		case 'f' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*f|:repeat", &datapy, &param1py.f)) {
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
			if (!PyArg_ParseTuple(args, "y*d|:repeat", &datapy, &param1py.d)) {
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


	/* Call the C function */
	switch(itemcode) {
		// signed char
		case 'b' : {
			repeat_signed_char(arraylength, data.b, param1py.b);
			break;
		}
		// unsigned char
		case 'B' : {
			repeat_unsigned_char(arraylength, data.B, param1py.B);
			break;
		}
		// signed short
		case 'h' : {
			repeat_signed_short(arraylength, data.h, param1py.h);
			break;
		}
		// unsigned short
		case 'H' : {
			repeat_unsigned_short(arraylength, data.H, param1py.H);
			break;
		}
		// signed int
		case 'i' : {
			repeat_signed_int(arraylength, data.i, param1py.i);
			break;
		}
		// unsigned int
		case 'I' : {
			repeat_unsigned_int(arraylength, data.I, param1py.I);
			break;
		}
		// signed long
		case 'l' : {
			repeat_signed_long(arraylength, data.l, param1py.l);
			break;
		}
		// unsigned long
		case 'L' : {
			repeat_unsigned_long(arraylength, data.L, param1py.L);
			break;
		}
		// signed long long
		case 'q' : {
			repeat_signed_long_long(arraylength, data.q, param1py.q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			repeat_unsigned_long_long(arraylength, data.Q, param1py.Q);
			break;
		}
		// float
		case 'f' : {
			repeat_float(arraylength, data.f, param1py.f);
			break;
		}
		// double
		case 'd' : {
			repeat_double(arraylength, data.d, param1py.d);
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


	// Everything was successful.
	Py_RETURN_NONE;


}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(repeat__doc__,
"Fill an array with a specified value.\n\
\n\
repeat(dataarray, value)\n\
\n\
* dataarray - The output array.\n\
* value - The value to use to fill the array.");


/* A list of all the methods defined by this module. 
 "repeat" is the name seen inside of Python. 
 "py_repeat" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef repeat_methods[] = {
	{"repeat",  py_repeat, METH_VARARGS, repeat__doc__}, {NULL, NULL}
};


static struct PyModuleDef repeatmodule = {
    PyModuleDef_HEAD_INIT,
    "repeat",
    NULL,
    -1,
    repeat_methods
};

PyMODINIT_FUNC PyInit_repeat(void)
{
    return PyModule_Create(&repeatmodule);
};

/*--------------------------------------------------------------------------- */
