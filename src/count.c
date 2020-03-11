//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   count.c
// Purpose:  Fill an array with evenly spaced values using a start and step values.
// Language: C
// Date:     04-Jun-2019.
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

#include "arrayparams_cntcycrep.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For arraycode: b
   * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * hasstep = If true, use the provided step value, otherwise use a default step.
*/
void count_signed_char(Py_ssize_t arraylen, signed char *data, signed char startvalue, signed char stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x; 
	signed char increment, step;

	increment = startvalue;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1;
	}

	// Count down.
	for(x = 0; x < arraylen; x++) {
		data[x] = increment;
		increment = increment + step;
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: B
   * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * hasstep = If true, use the provided step value, otherwise use a default step.
*/
void count_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char startvalue, signed char stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned char increment, step;

	increment = startvalue;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue >= 0 ? stepvalue : -stepvalue;
	} else {
		step = 1;
	}

	if (hasstep && (stepvalue < 0)) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: h
   * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * hasstep = If true, use the provided step value, otherwise use a default step.
*/
void count_signed_short(Py_ssize_t arraylen, signed short *data, signed short startvalue, signed short stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x; 
	signed short increment, step;

	increment = startvalue;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1;
	}

	// Count down.
	for(x = 0; x < arraylen; x++) {
		data[x] = increment;
		increment = increment + step;
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: H
   * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * hasstep = If true, use the provided step value, otherwise use a default step.
*/
void count_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short startvalue, signed short stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned short increment, step;

	increment = startvalue;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue >= 0 ? stepvalue : -stepvalue;
	} else {
		step = 1;
	}

	if (hasstep && (stepvalue < 0)) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: i
   * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * hasstep = If true, use the provided step value, otherwise use a default step.
*/
void count_signed_int(Py_ssize_t arraylen, signed int *data, signed int startvalue, signed int stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x; 
	signed int increment, step;

	increment = startvalue;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1;
	}

	// Count down.
	for(x = 0; x < arraylen; x++) {
		data[x] = increment;
		increment = increment + step;
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: I
   * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * hasstep = If true, use the provided step value, otherwise use a default step.
*/
void count_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int startvalue, signed int stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned int increment, step;

	increment = startvalue;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue >= 0 ? stepvalue : -stepvalue;
	} else {
		step = 1;
	}

	if (hasstep && (stepvalue < 0)) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: l
   * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * hasstep = If true, use the provided step value, otherwise use a default step.
*/
void count_signed_long(Py_ssize_t arraylen, signed long *data, signed long startvalue, signed long stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long increment, step;

	increment = startvalue;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1;
	}

	// Count down.
	for(x = 0; x < arraylen; x++) {
		data[x] = increment;
		increment = increment + step;
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: L
   * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * hasstep = If true, use the provided step value, otherwise use a default step.
*/
void count_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long startvalue, signed long stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long increment, step;

	increment = startvalue;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue >= 0 ? stepvalue : -stepvalue;
	} else {
		step = 1;
	}

	if (hasstep && (stepvalue < 0)) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: q
   * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * hasstep = If true, use the provided step value, otherwise use a default step.
*/
void count_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long startvalue, signed long long stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long long increment, step;

	increment = startvalue;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1;
	}

	// Count down.
	for(x = 0; x < arraylen; x++) {
		data[x] = increment;
		increment = increment + step;
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: Q
   * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * hasstep = If true, use the provided step value, otherwise use a default step.
*/
void count_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long startvalue, signed long long stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long long increment, step;

	increment = startvalue;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue >= 0 ? stepvalue : -stepvalue;
	} else {
		step = 1;
	}

	if (hasstep && (stepvalue < 0)) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: f
   * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * hasstep = If true, use the provided step value, otherwise use a default step.
*/
void count_float(Py_ssize_t arraylen, float *data, float startvalue, float stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x; 
	float increment, step;

	increment = startvalue;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1.0;
	}

	// Count down.
	for(x = 0; x < arraylen; x++) {
		data[x] = increment;
		increment = increment + step;
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: d
   * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * hasstep = If true, use the provided step value, otherwise use a default step.
*/
void count_double(Py_ssize_t arraylen, double *data, double startvalue, double stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x; 
	double increment, step;

	increment = startvalue;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1.0;
	}

	// Count down.
	for(x = 0; x < arraylen; x++) {
		data[x] = increment;
		increment = increment + step;
	}

}

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_count(PyObject *self, PyObject *args, PyObject *keywds) {


	// This is used to hold the parsed parameters.
	struct args_params_cntcycrep arraydata = ARGSINIT_CNTCYCREP;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_count(self, args, keywds, "count");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}


	// The length of the data array.
	if (arraydata.arraylength < 1) {
		// Release the buffers. 
		releasebuffers_cntcycrep(arraydata);
		ErrMsgArrayLengthErr();
		return NULL;
	}



	/* Call the C function */
	switch(arraydata.arraytype) {
		// signed char
		case 'b' : {
			count_signed_char(arraydata.arraylength, arraydata.array1.b, arraydata.param1.b, arraydata.param2.b, arraydata.hasparam2);
			break;
		}
		// unsigned char
		case 'B' : {
			count_unsigned_char(arraydata.arraylength, arraydata.array1.B, arraydata.param1.B, arraydata.param2.b, arraydata.hasparam2);
			break;
		}
		// signed short
		case 'h' : {
			count_signed_short(arraydata.arraylength, arraydata.array1.h, arraydata.param1.h, arraydata.param2.h, arraydata.hasparam2);
			break;
		}
		// unsigned short
		case 'H' : {
			count_unsigned_short(arraydata.arraylength, arraydata.array1.H, arraydata.param1.H, arraydata.param2.h, arraydata.hasparam2);
			break;
		}
		// signed int
		case 'i' : {
			count_signed_int(arraydata.arraylength, arraydata.array1.i, arraydata.param1.i, arraydata.param2.i, arraydata.hasparam2);
			break;
		}
		// unsigned int
		case 'I' : {
			count_unsigned_int(arraydata.arraylength, arraydata.array1.I, arraydata.param1.I, arraydata.param2.i, arraydata.hasparam2);
			break;
		}
		// signed long
		case 'l' : {
			count_signed_long(arraydata.arraylength, arraydata.array1.l, arraydata.param1.l, arraydata.param2.l, arraydata.hasparam2);
			break;
		}
		// unsigned long
		case 'L' : {
			count_unsigned_long(arraydata.arraylength, arraydata.array1.L, arraydata.param1.L, arraydata.param2.l, arraydata.hasparam2);
			break;
		}
		// signed long long
		case 'q' : {
			count_signed_long_long(arraydata.arraylength, arraydata.array1.q, arraydata.param1.q, arraydata.param2.q, arraydata.hasparam2);
			break;
		}
		// unsigned long long
		case 'Q' : {
			count_unsigned_long_long(arraydata.arraylength, arraydata.array1.Q, arraydata.param1.Q, arraydata.param2.q, arraydata.hasparam2);
			break;
		}
		// float
		case 'f' : {
			count_float(arraydata.arraylength, arraydata.array1.f, arraydata.param1.f, arraydata.param2.f, arraydata.hasparam2);
			break;
		}
		// double
		case 'd' : {
			count_double(arraydata.arraylength, arraydata.array1.d, arraydata.param1.d, arraydata.param2.d, arraydata.hasparam2);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_cntcycrep(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_cntcycrep(arraydata);

	// Everything was successful.
	Py_RETURN_NONE;


}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(count__doc__,
"count \n\
_____________________________ \n\
\n\
Fill an array with evenly spaced values using a start and step values. \n\
\n\
======================  ============================================== \n\
Equivalent to:          itertools.count(start, len(array))\n\
or                      itertools.count(start, len(array), step)\n\
======================  ============================================== \n\
\n\
======================  ============================================== \n\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
  count(array, start, step). \n\
\n\
* array - The output array. \n\
* start - The numeric value to start from. \n\
* step - The value to increment by when creating each element. This \n\
  parameter is optional. If it is omitted, a value of 1 is assumed. A \n\
  negative step value will cause the function to count down.");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "count" is the name seen inside of Python. 
 "py_count" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef count_methods[] = {
	{"count",  (PyCFunction)py_count, METH_VARARGS | METH_KEYWORDS, count__doc__}, 
	{NULL, NULL, 0, NULL}
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

