//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   cycle.c
// Purpose:  Fill an array with a series of values, repeating as necessary.
// Language: C
// Date:     07-May-2014
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
	char param3type;
	char error;
};

/*--------------------------------------------------------------------------- */

// Auto-generated code goes below.

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   Returns nothing (void).
*/
void cycle_signed_char(Py_ssize_t arraylen, signed char *data, signed char startvalue, signed char stopvalue, signed char stepvalue) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	signed char increment;

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   Returns nothing (void).
*/
void cycle_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char startvalue, unsigned char stopvalue, unsigned char stepvalue) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	unsigned char increment;

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   Returns nothing (void).
*/
void cycle_signed_short(Py_ssize_t arraylen, signed short *data, signed short startvalue, signed short stopvalue, signed short stepvalue) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	signed short increment;

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   Returns nothing (void).
*/
void cycle_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short startvalue, unsigned short stopvalue, unsigned short stepvalue) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	unsigned short increment;

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   Returns nothing (void).
*/
void cycle_signed_int(Py_ssize_t arraylen, signed int *data, signed int startvalue, signed int stopvalue, signed int stepvalue) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	signed int increment;

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   Returns nothing (void).
*/
void cycle_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int startvalue, unsigned int stopvalue, unsigned int stepvalue) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	unsigned int increment;

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   Returns nothing (void).
*/
void cycle_signed_long(Py_ssize_t arraylen, signed long *data, signed long startvalue, signed long stopvalue, signed long stepvalue) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	signed long increment;

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   Returns nothing (void).
*/
void cycle_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long startvalue, unsigned long stopvalue, unsigned long stepvalue) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	unsigned long increment;

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   Returns nothing (void).
*/
void cycle_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long startvalue, signed long long stopvalue, signed long long stepvalue) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	signed long long increment;

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   Returns nothing (void).
*/
void cycle_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long startvalue, unsigned long long stopvalue, unsigned long long stepvalue) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	unsigned long long increment;

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   Returns nothing (void).
*/
void cycle_float(Py_ssize_t arraylen, float *data, float startvalue, float stopvalue, float stepvalue) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	float increment;

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   Returns nothing (void).
*/
void cycle_double(Py_ssize_t arraylen, double *data, double startvalue, double stopvalue, double stepvalue) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	double increment;

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
			if (increment < stopvalue) {
				increment = startvalue;
			}
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

	PyObject *dataobj, *param1obj, *param2obj;

	// We need to initialise the optional parameter to a known value, so we
	// can test if it was changed.
	PyObject *param3obj = NULL;


	struct args_param argtypes = {' ', ' ', ' ', 0};
	struct arrayparamstypes arr1type = {0, 0, ' '};


	/* Import the raw objects. */
	if (!PyArg_ParseTuple(args, "OOO|O:cycle", &dataobj, &param1obj, &param2obj, &param3obj)) {
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


	// Get the parameter type codes.
	argtypes.param1type = paramtypecode(param1obj->ob_type->tp_name);
	argtypes.param2type = paramtypecode(param2obj->ob_type->tp_name);

	// The third parameter is optional, so we have to test if it was set.
	if (param3obj != NULL) {
		argtypes.param3type = paramtypecode(param3obj->ob_type->tp_name);
	} else {
		argtypes.param3type = 'z';
	}


	return argtypes;

}


/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */


/* The wrapper to the underlying C function */
static PyObject *py_cycle(PyObject *self, PyObject *args)
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
	struct paramsvals param1py, param2py, param3py;

	// PyArg_ParseTuple does not match directly to the array codes. We need to
	// use some temporary variables of alternate types to parse the parameter 
	// data.
	signed long param1tmp_l, param2tmp_l, param3tmp_l;

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
	if (!paramcompatok(argtypes.array1type, argtypes.param1type)) {
		ErrMsgArrayAndParamMismatch();
		return NULL;
	}

	// We base our next actions based on the array type.
	itemcode = argtypes.array1type;


	// The last parameter (step) was not specified.
	param3tmp_l = 1;
	if (argtypes.param3type == 'z') {
		param3py.b = 1;
		param3py.B = 1;
		param3py.h = 1;
		param3py.H = 1;
		param3py.i = 1;
		param3py.I = 1;
		param3py.l = 1;
		param3py.L = 1;
		param3py.q = 1;
		param3py.Q = 1;
		param3py.f = 1.0;
		param3py.d = 1.0;
	}



	// Now we will fetch the actual data depending on the array type.
	switch (itemcode) {
		// signed char
		case 'b' : {
			// There does not seem to be a format string for signed char, so we must use a larger type
			// and check it manually. 
			if (!PyArg_ParseTuple(args, "y*ll|l:cycle", &datapy, &param1tmp_l, &param2tmp_l, &param3tmp_l)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(issignedcharrange(param1tmp_l) && issignedcharrange(param2tmp_l) && issignedcharrange(param3tmp_l))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			} else {
				param1py.b = (signed char) param1tmp_l;
				param2py.b = (signed char) param2tmp_l;
				// Step must be positive.
				param3py.b = (signed char) abs(param3tmp_l);
			}
			break;
		}
		// unsigned char
		case 'B' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*ll|l:cycle", &datapy, &param1tmp_l, &param2tmp_l, &param3tmp_l)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isunsignedcharrange(param1tmp_l) && isunsignedcharrange(param2tmp_l) && isunsignedcharrange(param3tmp_l))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			} else {
				param1py.B = (unsigned char) param1tmp_l;
				param2py.B = (unsigned char) param2tmp_l;
				param3py.B = (unsigned char) param3tmp_l;
			}
			break;
		}
		// signed short
		case 'h' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*hh|h:cycle", &datapy, &param1py.h, &param2py.h, &param3py.h)) {
				return NULL;
			}
			// Step must be positive.
			param3py.h = abs(param3py.h);
			break;
		}
		// unsigned short
		case 'H' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*ll|l:cycle", &datapy, &param1tmp_l, &param2tmp_l, &param3tmp_l)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isunsignedshortrange(param1tmp_l) && isunsignedshortrange(param2tmp_l) && isunsignedshortrange(param3tmp_l))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			} else {
				param1py.H = (unsigned short) param1tmp_l;
				param2py.H = (unsigned short) param2tmp_l;
				param3py.H = (unsigned short) param3tmp_l;
			}
			break;
		}
		// signed int
		case 'i' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*ii|i:cycle", &datapy, &param1py.i, &param2py.i, &param3py.i)) {
				return NULL;
			}
			// Step must be positive.
			param3py.i = abs(param3py.i);
			break;
		}
		// unsigned int
		case 'I' : {
			// With architectures where signed long is larger than unsigned int, we
			// can use the larger signed value to test for overflow. If they are the
			// same size, then we cannot check for overflow.
			if (sizeof(signed long) > sizeof(unsigned int)) {
				// The format string and parameter names depend on the expected data types.
				if (!PyArg_ParseTuple(args, "y*ll|l:cycle", &datapy, &param1tmp_l, &param2tmp_l, &param3tmp_l)) {
					return NULL;
				}
				// Check the data range manually.
				if (!(isunsignedintrange(param1tmp_l) && isunsignedintrange(param2tmp_l) && isunsignedintrange(param3tmp_l))) {
					PyBuffer_Release(&datapy);
					ErrMsgArithOverflowParam();
					return NULL;
				} else {
					param1py.I = (unsigned int) param1tmp_l;
					param2py.I = (unsigned int) param2tmp_l;
					param3py.I = (unsigned int) param3tmp_l;
				}
			} else {
				// The format string and parameter names depend on the expected data types.
				if (!PyArg_ParseTuple(args, "y*II|I:cycle", &datapy, &param1py.I, &param2py.I, &param3py.I)) {
					return NULL;
				}
			}
			break;
		}
		// signed long
		case 'l' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*ll|l:cycle", &datapy, &param1py.l, &param2py.l, &param3py.l)) {
				return NULL;
			}
			// Step must be positive.
			param3py.l = labs(param3py.l);
			break;
		}
		// unsigned long
		case 'L' : {
			// The format codes do NOT match the array codes for this type.
			if (!PyArg_ParseTuple(args, "y*kk|k:cycle", &datapy, &param1py.L, &param2py.L, &param3py.L)) {
				return NULL;
			}
			break;
		}
		// signed long long
		case 'q' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*LL|L:cycle", &datapy, &param1py.q, &param2py.q, &param3py.q)) {
				return NULL;
			}
			// Step must be positive.
			param3py.q = llabs(param3py.q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			// The format codes do NOT match the array codes for this type.
			if (!PyArg_ParseTuple(args, "y*KK|K:cycle", &datapy, &param1py.Q, &param2py.Q, &param3py.Q)) {
				return NULL;
			}
			break;
		}
		// float
		case 'f' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*ff|f:cycle", &datapy, &param1py.f, &param2py.f, &param3py.f)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isfinite(param1py.f) && isfinite(param2py.f) && isfinite(param3py.f))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			}
			// Step must be positive.
			param3py.f = fabsf(param3py.f);
			break;
		}
		// double
		case 'd' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTuple(args, "y*dd|d:cycle", &datapy, &param1py.d, &param2py.d, &param3py.d)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isfinite(param1py.d) && isfinite(param2py.d) && isfinite(param3py.d))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			}
			// Step must be positive.
			param3py.d = fabs(param3py.d);
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
			cycle_signed_char(arraylength, data.b, param1py.b, param2py.b, param3py.b);
			break;
		}
		// unsigned char
		case 'B' : {
			cycle_unsigned_char(arraylength, data.B, param1py.B, param2py.B, param3py.B);
			break;
		}
		// signed short
		case 'h' : {
			cycle_signed_short(arraylength, data.h, param1py.h, param2py.h, param3py.h);
			break;
		}
		// unsigned short
		case 'H' : {
			cycle_unsigned_short(arraylength, data.H, param1py.H, param2py.H, param3py.H);
			break;
		}
		// signed int
		case 'i' : {
			cycle_signed_int(arraylength, data.i, param1py.i, param2py.i, param3py.i);
			break;
		}
		// unsigned int
		case 'I' : {
			cycle_unsigned_int(arraylength, data.I, param1py.I, param2py.I, param3py.I);
			break;
		}
		// signed long
		case 'l' : {
			cycle_signed_long(arraylength, data.l, param1py.l, param2py.l, param3py.l);
			break;
		}
		// unsigned long
		case 'L' : {
			cycle_unsigned_long(arraylength, data.L, param1py.L, param2py.L, param3py.L);
			break;
		}
		// signed long long
		case 'q' : {
			cycle_signed_long_long(arraylength, data.q, param1py.q, param2py.q, param3py.q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			cycle_unsigned_long_long(arraylength, data.Q, param1py.Q, param2py.Q, param3py.Q);
			break;
		}
		// float
		case 'f' : {
			cycle_float(arraylength, data.f, param1py.f, param2py.f, param3py.f);
			break;
		}
		// double
		case 'd' : {
			cycle_double(arraylength, data.d, param1py.d, param2py.d, param3py.d);
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
PyDoc_STRVAR(cycle__doc__,
"Fill an array with evenly spaced values using a start, stop, and step \n\
values, and repeat until the array is filled.\n\
\n\
cycle(dataarray, start, stop, step)\n\
\n\
* dataarray - The output array.\n\
* start - The numeric value to start from.\n\
* stop - The value at which to stop incrementing. If stop is less than \n\
  start, cycle will count down. \n\
* step - The value to increment by when creating each element. This \n\
  parameter is optional. If it is omitted, a value of 1 is assumed. The\n\
  sign is ignored and the absolute value used when incrementing.");



/* A list of all the methods defined by this module. 
 "cycle" is the name seen inside of Python. 
 "py_cycle" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef cycle_methods[] = {
	{"cycle",  py_cycle, METH_VARARGS, cycle__doc__}, {NULL, NULL}
};


static struct PyModuleDef cyclemodule = {
    PyModuleDef_HEAD_INIT,
    "cycle",
    NULL,
    -1,
    cycle_methods
};

PyMODINIT_FUNC PyInit_cycle(void)
{
    return PyModule_Create(&cyclemodule);
};

/*--------------------------------------------------------------------------- */
