//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   count.c
// Purpose:  Fill an array with a series of values.
// Language: C
// Date:     04-May-2014
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
	char param1type;
	char param2type;
	char error;
};

/*--------------------------------------------------------------------------- */

// Auto-generated code goes below.

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_signed_char(Py_ssize_t arraylen, signed char *data, signed char startvalue, signed char stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	signed char increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char startvalue, unsigned char stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned char increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_signed_short(Py_ssize_t arraylen, signed short *data, signed short startvalue, signed short stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	signed short increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short startvalue, unsigned short stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned short increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_signed_int(Py_ssize_t arraylen, signed int *data, signed int startvalue, signed int stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	signed int increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int startvalue, unsigned int stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned int increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_signed_long(Py_ssize_t arraylen, signed long *data, signed long startvalue, signed long stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long startvalue, unsigned long stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long startvalue, signed long long stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long long increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long startvalue, unsigned long long stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long long increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_float(Py_ssize_t arraylen, float *data, float startvalue, float stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	float increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_double(Py_ssize_t arraylen, double *data, double startvalue, double stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	double increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

/* Parse the Python arguments to objects, and then extract the object parameters
 * to determine their types. This lets us handle different data types as 
 * parameters.
 * This version expects the following parameters:
 * args (PyObject) = The positional arguments.
 * Returns a structure containing the results of each parameter.
*/
struct args_param parsepyargs_parm(PyObject *args) {

	PyObject *dataobj, *param1obj;

	// We need to initialise the optional parameter to a known value, so we
	// can test if it was changed.
	PyObject *param2obj = NULL;


	struct args_param argtypes = {' ', ' ', 0};
	struct arrayparamstypes arr1type = {0, 0, ' '};

	/* Import the raw objects. */
	if (!PyArg_ParseTuple(args, "OO|O:count", &dataobj, &param1obj, &param2obj)) {
		argtypes.error = 1;
		return argtypes;
	}

	// Test if the first parameter is an array or bytes.
	arr1type = paramarraytype(dataobj);
	if (!arr1type.isarray) {
		argtypes.error = 2;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.array1type = arr1type.arraycode;
	}


	// We don't bother checking the second parameter type, because the
	// parsing format strings will handle that for us.

	// The third parameter is optional, so we have to test if it was set.
	if (param2obj != NULL) {
		argtypes.param2type = paramtypecode(param2obj->ob_type->tp_name);
	} else {
		argtypes.param2type = 'z';
	}



	return argtypes;

}



/*--------------------------------------------------------------------------- */


/* The wrapper to the underlying C function */
static PyObject *
py_count(PyObject *self, PyObject *args)
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
	struct paramsvals param1py, param2py;

	// PyArg_ParseTuple does not match directly to the array codes. We need to
	// use some temporary variables of alternate types to parse the parameter 
	// data.
	// PyArg_ParseTuple does not check for overflow of unsigned parameters.
	signed long param1tmp_l;

	signed long param2tmp_l;

	signed long long param2tmp_q;


	// If true, count down with the step value.
	int countdown = 0;

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

	// We base our next actions based on the array type.
	itemcode = argtypes.array1type;

	// The second parameter (step) was not specified.
	if (argtypes.param2type == 'z') {
		param2py.b = 1;
		param2py.B = 1;
		param2py.h = 1;
		param2py.H = 1;
		param2py.i = 1;
		param2py.I = 1;
		param2py.l = 1;
		param2py.L = 1;
		param2py.f = 1.0;
		param2py.d = 1.0;
		param2tmp_l = 1;
		param2tmp_q = 1;
	}


	// Now we will fetch the actual data depending on the array type.
	switch (itemcode) {
		// signed char
		case 'b' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*l|l:count", &datapy, &param1tmp_l, &param2tmp_l)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(issignedcharrange(param1tmp_l) && issignedcharrange(param2tmp_l))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			} else {
				param1py.b = (signed char) param1tmp_l;
				param2py.b = (signed char) abs(param2tmp_l);
				countdown = (param2tmp_l < 0);
			}
			break;
		}
		// unsigned char
		case 'B' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*l|l:count", &datapy, &param1tmp_l, &param2tmp_l)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isunsignedcharrange(param1tmp_l) && issignedcharrange(param2tmp_l))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			} else {
				param1py.B = (unsigned char) param1tmp_l;
				param2py.B = (signed char) abs(param2tmp_l);
				countdown = (param2tmp_l < 0);
			}
			break;
		}
		// signed short
		case 'h' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*h|h:count", &datapy, &param1py.h, &param2py.h)) {
				return NULL;
			}
			countdown = (param2py.h < 0);
			param2py.h = abs(param2py.h);
			break;
		}
		// unsigned short
		case 'H' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*l|l:count", &datapy, &param1tmp_l, &param2tmp_l)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isunsignedshortrange(param1tmp_l) && issignedshortrange(param2tmp_l))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			} else {
				param1py.H = (unsigned short) param1tmp_l;
				param2py.H = (unsigned short) abs(param2tmp_l);
				countdown = (param2tmp_l < 0);
			}
			break;
		}
		// signed int
		case 'i' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*i|i:count", &datapy, &param1py.i, &param2py.i)) {
				return NULL;
			}
			countdown = (param2py.i < 0);
			param2py.i = abs(param2py.i);
			break;
		}
		// unsigned int
		case 'I' : {
			// With architectures where signed long is larger than unsigned int, we
			// can use the larger signed value to test for overflow. If they are the
			// same size, then we cannot check for overflow.
			if (sizeof(signed long) > sizeof(unsigned int)) {
				// The format string and parameter names depend on the expected data types.
				if (!PyArg_ParseTuple(args, "y*l|l:count", &datapy, &param1tmp_l, &param2tmp_l)) {
					return NULL;
				}
				// Check the data range manually.
				if (!(isunsignedintrange(param1tmp_l) && issignedintrange(param2tmp_l))) {
					PyBuffer_Release(&datapy);
					ErrMsgArithOverflowParam();
					return NULL;
				} else {
					param1py.I = (unsigned int) param1tmp_l;
				}
			} else {
				// The format string and parameter names depend on the expected data types.
				if (!PyArg_ParseTuple(args, "y*I|l:count", &datapy, &param1py.I, &param2tmp_l)) {
					return NULL;
				}
			}
			param2py.I = abs(param2tmp_l);
			countdown = (param2tmp_l < 0);
			break;
		}
		// signed long
		case 'l' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*l|l:count", &datapy, &param1py.l, &param2py.l)) {
				return NULL;
			}
			countdown = (param2py.l < 0);
			param2py.l = labs(param2py.l);
			break;
		}
		// unsigned long
		case 'L' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*k|l:count", &datapy, &param1py.L, &param2tmp_l)) {
				return NULL;
			}
			countdown = (param2tmp_l < 0);
			param2py.L = (unsigned long) labs(param2tmp_l);
			break;
		}
		// signed long long
		case 'q' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*L|L:count", &datapy, &param1py.q, &param2tmp_q)) {
				return NULL;
			}
			countdown = (param2tmp_q < 0);
			param2py.q = llabs(param2tmp_q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*K|L:count", &datapy, &param1py.Q, &param2tmp_q)) {
				return NULL;
			}
			countdown = (param2tmp_q < 0);
			param2py.Q = (unsigned long long) llabs(param2tmp_q);
			break;
		}
		// float
		case 'f' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*f|f:count", &datapy, &param1py.f, &param2py.f)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isfinite(param1py.f) && isfinite(param2py.f))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			}
			countdown = (param2py.f < 0.0);
			param2py.f = fabsf(param2py.f);
			break;
		}
		// double
		case 'd' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*d|d:count", &datapy, &param1py.d, &param2py.d)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isfinite(param1py.d) && isfinite(param2py.d))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			}
			countdown = (param2py.d < 0.0);
			param2py.d = fabsf(param2py.d);
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
			count_signed_char(arraylength, data.b, param1py.b, param2py.b, countdown);
			break;
		}
		// unsigned char
		case 'B' : {
			count_unsigned_char(arraylength, data.B, param1py.B, param2py.B, countdown);
			break;
		}
		// signed short
		case 'h' : {
			count_signed_short(arraylength, data.h, param1py.h, param2py.h, countdown);
			break;
		}
		// unsigned short
		case 'H' : {
			count_unsigned_short(arraylength, data.H, param1py.H, param2py.H, countdown);
			break;
		}
		// signed int
		case 'i' : {
			count_signed_int(arraylength, data.i, param1py.i, param2py.i, countdown);
			break;
		}
		// unsigned int
		case 'I' : {
			count_unsigned_int(arraylength, data.I, param1py.I, param2py.I, countdown);
			break;
		}
		// signed long
		case 'l' : {
			count_signed_long(arraylength, data.l, param1py.l, param2py.l, countdown);
			break;
		}
		// unsigned long
		case 'L' : {
			count_unsigned_long(arraylength, data.L, param1py.L, param2py.L, countdown);
			break;
		}
		// signed long long
		case 'q' : {
			count_signed_long_long(arraylength, data.q, param1py.q, param2py.q, countdown);
			break;
		}
		// unsigned long long
		case 'Q' : {
			count_unsigned_long_long(arraylength, data.Q, param1py.Q, param2py.Q, countdown);
			break;
		}
		// float
		case 'f' : {
			count_float(arraylength, data.f, param1py.f, param2py.f, countdown);
			break;
		}
		// double
		case 'd' : {
			count_double(arraylength, data.d, param1py.d, param2py.d, countdown);
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
PyDoc_STRVAR(count__doc__,
"Fill an array with evenly spaced values using a start and step values. \n\
The function continues until the end of the array. The function does \n\
not check for integer overflow.\n\
\n\
count(dataarray, start, step) \n\
\n\
* dataarray - The output array.\n\
* start - The numeric value to start from.\n\
* step - The value to increment by when creating each element. This \n\
  parameter is optional. If it is omitted, a value of 1 is assumed. A \n\
  negative step value will cause the function to count down.");


/* A list of all the methods defined by this module. 
 "count" is the name seen inside of Python. 
 "py_count" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef count_methods[] = {
	{"count",  py_count, METH_VARARGS, count__doc__}, {NULL, NULL}
};

static struct PyModuleDef countmodule = {
    PyModuleDef_HEAD_INIT,
    "count",
    NULL,
    -1,
    count_methods
};

PyMODINIT_FUNC PyInit_count(void)
{
    return PyModule_Create(&countmodule);
};

/*--------------------------------------------------------------------------- */
