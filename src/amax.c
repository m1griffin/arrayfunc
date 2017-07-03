//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   amax.c
// Purpose:  Find the maximum value in an array.
// Language: C
// Date:     04-May-2014
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

#include <limits.h>
#include <float.h>

#include "arrayfunc.h"
#include "arrayerrs.h"
#include "simddefs.h"

#ifdef AF_HASSIMD
#include "amax_simd_x86.h"
#endif

/*--------------------------------------------------------------------------- */

// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist[] = {"data", "maxlen", "nosimd", NULL};

/*--------------------------------------------------------------------------- */

// Auto-generated code goes below.


/*--------------------------------------------------------------------------- */
/* For array code: b
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
signed char amax_signed_char(Py_ssize_t arraylen, signed char *data, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	signed char maxfound;


#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
		return amax_signed_char_simd(arraylen, data);
	}
#endif

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: B
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
unsigned char amax_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned char maxfound;


#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
		return amax_unsigned_char_simd(arraylen, data);
	}
#endif

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: h
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
signed short amax_signed_short(Py_ssize_t arraylen, signed short *data, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	signed short maxfound;


#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
		return amax_signed_short_simd(arraylen, data);
	}
#endif

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: H
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
unsigned short amax_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned short maxfound;


#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
		return amax_unsigned_short_simd(arraylen, data);
	}
#endif

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: i
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
signed int amax_signed_int(Py_ssize_t arraylen, signed int *data, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	signed int maxfound;


#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
		return amax_signed_int_simd(arraylen, data);
	}
#endif

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: I
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
unsigned int amax_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned int maxfound;


#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
		return amax_unsigned_int_simd(arraylen, data);
	}
#endif

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: l
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
signed long amax_signed_long(Py_ssize_t arraylen, signed long *data, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long maxfound;

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: L
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
unsigned long amax_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long maxfound;

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: q
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
signed long long amax_signed_long_long(Py_ssize_t arraylen, signed long long *data, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long long maxfound;

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: Q
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
unsigned long long amax_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long long maxfound;

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: f
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
float amax_float(Py_ssize_t arraylen, float *data, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	float maxfound;


#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (FLOATSIMDSIZE * 2))) {
		return amax_float_simd(arraylen, data);
	}
#endif

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: d
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
double amax_double(Py_ssize_t arraylen, double *data, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	double maxfound;


#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (DOUBLESIMDSIZE * 2))) {
		return amax_double_simd(arraylen, data);
	}
#endif

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* The wrapper to the underlying C function */
static PyObject *py_amax(PyObject *self, PyObject *args, PyObject *keywds) {


	// The raw object so we can examine what it is. 
	PyObject *dataobj;

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
	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	// The parameter version is available in all possible types.
	struct paramsvals resultfound;
	struct arrayparamstypes arr1type = {0, 0, ' '};

	// If true, disable using SIMD.
	unsigned int nosimd = 0;

	// -------------------------------------------------------------------------


	/* Import the raw objects. */
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "O|ni:amax", kwlist, 
			&dataobj, &arraymaxlen, &nosimd)) {
		ErrMsgParameterError();
		return NULL;
	}


	// Test if the parameter is an array or bytes.
	arr1type = paramarraytype(dataobj);
	if (!arr1type.isarray) {
		ErrMsgArrayorBytesExpected();
		return NULL;
	} else {
		// Get the array code type character.
		itemcode = arr1type.arraycode;
	}


	// Now we will fetch the actual data.
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "y*|ni:amax", kwlist, 
			&datapy, &arraymaxlen, &nosimd)) {
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
			resultfound.b = amax_signed_char(arraylength, data.b, nosimd);
			PyBuffer_Release(&datapy);
			return PyLong_FromLong(resultfound.b);
		}
		// unsigned char
		case 'B' : {
			resultfound.B = amax_unsigned_char(arraylength, data.B, nosimd);
			PyBuffer_Release(&datapy);
			return PyLong_FromUnsignedLong(resultfound.B);
		}
		// signed short
		case 'h' : {
			resultfound.h = amax_signed_short(arraylength, data.h, nosimd);
			PyBuffer_Release(&datapy);
			return PyLong_FromLong(resultfound.h);
		}
		// unsigned short
		case 'H' : {
			resultfound.H = amax_unsigned_short(arraylength, data.H, nosimd);
			PyBuffer_Release(&datapy);
			return PyLong_FromUnsignedLong(resultfound.H);
		}
		// signed int
		case 'i' : {
			resultfound.i = amax_signed_int(arraylength, data.i, nosimd);
			PyBuffer_Release(&datapy);
			return PyLong_FromLong(resultfound.i);
		}
		// unsigned int
		case 'I' : {
			resultfound.I = amax_unsigned_int(arraylength, data.I, nosimd);
			PyBuffer_Release(&datapy);
			return PyLong_FromUnsignedLong(resultfound.I);
		}
		// signed long
		case 'l' : {
			resultfound.l = amax_signed_long(arraylength, data.l, nosimd);
			PyBuffer_Release(&datapy);
			return PyLong_FromLong(resultfound.l);
		}
		// unsigned long
		case 'L' : {
			resultfound.L = amax_unsigned_long(arraylength, data.L, nosimd);
			PyBuffer_Release(&datapy);
			return PyLong_FromUnsignedLong(resultfound.L);
		}
		// signed long long
		case 'q' : {
			resultfound.q = amax_signed_long_long(arraylength, data.q, nosimd);
			PyBuffer_Release(&datapy);
			return PyLong_FromLongLong(resultfound.q);
		}
		// unsigned long long
		case 'Q' : {
			resultfound.Q = amax_unsigned_long_long(arraylength, data.Q, nosimd);
			PyBuffer_Release(&datapy);
			return PyLong_FromUnsignedLongLong(resultfound.Q);
		}
		// float
		case 'f' : {
			resultfound.f = amax_float(arraylength, data.f, nosimd);
			PyBuffer_Release(&datapy);
			return PyFloat_FromDouble(resultfound.f);
		}
		// double
		case 'd' : {
			resultfound.d = amax_double(arraylength, data.d, nosimd);
			PyBuffer_Release(&datapy);
			return PyFloat_FromDouble(resultfound.d);
		}
		// We don't know this code.
		default: {
			PyBuffer_Release(&datapy);
			ErrMsgUnknownArrayType();
			return NULL;
		}
	}


}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(amax__doc__,
"Returns the maximum value in the array.\n\
\n\
x = amax(inparray)\n\
x = amax(inparray, maxlen=y)\n\
x = amax(inparray, maxlen=y, nosimd=true)\n\
\n\
* inparray - The input data array to be examined.\n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored.\n\
* nosimd - If true, use of SIMD is disabled.\n\
* x - The maximum value.");


/* A list of all the methods defined by this module. 
 "amax" is the name seen inside of Python. 
 "py_amax" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef amax_methods[] = {
	{"amax",  (PyCFunction) py_amax, METH_VARARGS | METH_KEYWORDS, amax__doc__}, 
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef amaxmodule = {
    PyModuleDef_HEAD_INIT,
    "amax",
    NULL,
    -1,
    amax_methods
};

PyMODINIT_FUNC PyInit_amax(void)
{
    return PyModule_Create(&amaxmodule);
};

/*--------------------------------------------------------------------------- */
