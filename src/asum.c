//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   asum.c
// Purpose:  Find the maximum value in an array.
// Language: C
// Date:     15-May-2014
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

#include <limits.h>

#include "arrayfunc.h"
#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */

// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist[] = {"data", "disovfl", "maxlen", NULL};

/*--------------------------------------------------------------------------- */

// Auto-generated code goes below.

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   disableovfl = If true, arithmetic overflow checking is disabled.
	Returns: The sum of the array.
*/
signed long asum_signed_char(Py_ssize_t arraylen, signed char *data, signed int *errflag, signed int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (disableovfl) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((partialsum > 0) && (data[x] > (LONG_MAX - partialsum))) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			if ((partialsum < 0) && (data[x] < (LONG_MIN - partialsum))) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			partialsum = partialsum + data[x];
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   disableovfl = If true, arithmetic overflow checking is disabled.
	Returns: The sum of the array.
*/
unsigned long asum_unsigned_char(Py_ssize_t arraylen, unsigned char *data, signed int *errflag, signed int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (disableovfl) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
			if (data[x] > (ULONG_MAX - partialsum)) { 
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			partialsum = partialsum + data[x];
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   disableovfl = If true, arithmetic overflow checking is disabled.
	Returns: The sum of the array.
*/
signed long asum_signed_short(Py_ssize_t arraylen, signed short *data, signed int *errflag, signed int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (disableovfl) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((partialsum > 0) && (data[x] > (LONG_MAX - partialsum))) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			if ((partialsum < 0) && (data[x] < (LONG_MIN - partialsum))) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			partialsum = partialsum + data[x];
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   disableovfl = If true, arithmetic overflow checking is disabled.
	Returns: The sum of the array.
*/
unsigned long asum_unsigned_short(Py_ssize_t arraylen, unsigned short *data, signed int *errflag, signed int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (disableovfl) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
			if (data[x] > (ULONG_MAX - partialsum)) { 
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			partialsum = partialsum + data[x];
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   disableovfl = If true, arithmetic overflow checking is disabled.
	Returns: The sum of the array.
*/
signed long asum_signed_int(Py_ssize_t arraylen, signed int *data, signed int *errflag, signed int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (disableovfl) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((partialsum > 0) && (data[x] > (LONG_MAX - partialsum))) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			if ((partialsum < 0) && (data[x] < (LONG_MIN - partialsum))) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			partialsum = partialsum + data[x];
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   disableovfl = If true, arithmetic overflow checking is disabled.
	Returns: The sum of the array.
*/
unsigned long asum_unsigned_int(Py_ssize_t arraylen, unsigned int *data, signed int *errflag, signed int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (disableovfl) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
			if (data[x] > (ULONG_MAX - partialsum)) { 
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			partialsum = partialsum + data[x];
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   disableovfl = If true, arithmetic overflow checking is disabled.
	Returns: The sum of the array.
*/
signed long asum_signed_long(Py_ssize_t arraylen, signed long *data, signed int *errflag, signed int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (disableovfl) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((partialsum > 0) && (data[x] > (LONG_MAX - partialsum))) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			if ((partialsum < 0) && (data[x] < (LONG_MIN - partialsum))) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			partialsum = partialsum + data[x];
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   disableovfl = If true, arithmetic overflow checking is disabled.
	Returns: The sum of the array.
*/
unsigned long asum_unsigned_long(Py_ssize_t arraylen, unsigned long *data, signed int *errflag, signed int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (disableovfl) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
			if (data[x] > (ULONG_MAX - partialsum)) { 
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			partialsum = partialsum + data[x];
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   disableovfl = If true, arithmetic overflow checking is disabled.
	Returns: The sum of the array.
*/
signed long long asum_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed int *errflag, signed int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (disableovfl) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((partialsum > 0) && (data[x] > (LLONG_MAX - partialsum))) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			if ((partialsum < 0) && (data[x] < (LLONG_MIN - partialsum))) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			partialsum = partialsum + data[x];
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   disableovfl = If true, arithmetic overflow checking is disabled.
	Returns: The sum of the array.
*/
unsigned long long asum_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, signed int *errflag, signed int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (disableovfl) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
			if (data[x] > (ULLONG_MAX - partialsum)) { 
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			partialsum = partialsum + data[x];
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   disableovfl = If true, arithmetic overflow checking is disabled.
	Returns: The sum of the array.
*/
float asum_float(Py_ssize_t arraylen, float *data, signed int *errflag, signed int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	float partialsum = 0.0;

	*errflag = 0;
	// Overflow checking disabled.
	if (disableovfl) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
			if (!isfinite(partialsum)) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   disableovfl = If true, arithmetic overflow checking is disabled.
	Returns: The sum of the array.
*/
double asum_double(Py_ssize_t arraylen, double *data, signed int *errflag, signed int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	double partialsum = 0.0;

	*errflag = 0;
	// Overflow checking disabled.
	if (disableovfl) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
			if (!isfinite(partialsum)) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */


/* The wrapper to the underlying C function */
static PyObject *py_asum(PyObject *self, PyObject *args, PyObject *keywds)
{


	// The array of data we work on. 
	union dataarrays data;

	// The input buffers are arrays of bytes.
	Py_buffer datapy;

	// The length of the data array.
	Py_ssize_t databufflength;

	// The raw object so we can examine what it is, plus the final result. 
	PyObject *dataobj, *sumreturn;


	// Codes indicating the type of array and the operation desired.
	char itemcode;

	// Indicates an error.
	signed int errflag = 0;
	// If true, disable integer overflow checking.
	signed int disableovfl = 0;

	// How long the array is.
	Py_ssize_t arraylength;
	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	// The parameter version is available in all possible types.
	struct paramsvals resultfound;
	struct arrayparamstypes arr1type = {0, 0, ' '};


	// -------------------------------------------------------------------------


	/* Import the raw objects. */
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "O|in:asum", kwlist, &dataobj, &disableovfl, &arraymaxlen)) {
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
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "y*|in:asum", kwlist, 
			&datapy, &disableovfl, &arraymaxlen)) {
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
			resultfound.l = asum_signed_char(arraylength, data.b, &errflag, disableovfl);
			sumreturn = PyLong_FromLong(resultfound.l);
			break;
		}
		// unsigned char
		case 'B' : {
			resultfound.L = asum_unsigned_char(arraylength, data.B, &errflag, disableovfl);
			sumreturn = PyLong_FromUnsignedLong(resultfound.L);
			break;
		}
		// signed short
		case 'h' : {
			resultfound.l = asum_signed_short(arraylength, data.h, &errflag, disableovfl);
			sumreturn = PyLong_FromLong(resultfound.l);
			break;
		}
		// unsigned short
		case 'H' : {
			resultfound.L = asum_unsigned_short(arraylength, data.H, &errflag, disableovfl);
			sumreturn = PyLong_FromUnsignedLong(resultfound.L);
			break;
		}
		// signed int
		case 'i' : {
			resultfound.l = asum_signed_int(arraylength, data.i, &errflag, disableovfl);
			sumreturn = PyLong_FromLong(resultfound.l);
			break;
		}
		// unsigned int
		case 'I' : {
			resultfound.L = asum_unsigned_int(arraylength, data.I, &errflag, disableovfl);
			sumreturn = PyLong_FromUnsignedLong(resultfound.L);
			break;
		}
		// signed long
		case 'l' : {
			resultfound.l = asum_signed_long(arraylength, data.l, &errflag, disableovfl);
			sumreturn = PyLong_FromLong(resultfound.l);
			break;
		}
		// unsigned long
		case 'L' : {
			resultfound.L = asum_unsigned_long(arraylength, data.L, &errflag, disableovfl);
			sumreturn = PyLong_FromUnsignedLong(resultfound.L);
			break;
		}
		// signed long long
		case 'q' : {
			resultfound.q = asum_signed_long_long(arraylength, data.q, &errflag, disableovfl);
			sumreturn = PyLong_FromLongLong(resultfound.q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultfound.Q = asum_unsigned_long_long(arraylength, data.Q, &errflag, disableovfl);
			sumreturn = PyLong_FromUnsignedLongLong(resultfound.Q);
			break;
		}
		// float
		case 'f' : {
			resultfound.f = asum_float(arraylength, data.f, &errflag, disableovfl);
			sumreturn = PyFloat_FromDouble((double) resultfound.f);
			break;
		}
		// double
		case 'd' : {
			resultfound.d = asum_double(arraylength, data.d, &errflag, disableovfl);
			sumreturn = PyFloat_FromDouble(resultfound.d);
			break;
		}
		// We don't know this code.
		default: {
			// Release the buffers.
			PyBuffer_Release(&datapy);
			ErrMsgUnknownArrayType();
			return NULL;
		}
	}


	// Release the buffers.
	PyBuffer_Release(&datapy);

	if (errflag == ARR_ERR_OVFL) {
		ErrMsgArithOverflowCalc();
		return NULL;
	}

	return sumreturn;

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(asum__doc__,
"Calculate the arithmetic sum of an array. \n\
\n\
For integer arrays, the intermediate sum is accumulated in the largest \n\
corresponding integer size. Signed integers are accumulated in the  \n\
equivalent to an 'l' array type, and unsigned integers are accumulated \n\
in the equivalent to an 'L' array type. This means that integer arrays \n\
using smaller integer word sizes cannot overflow unless extremenly \n\
large arrays are used (and may be impossible due to limits on array \n\
indices in the array module). \n\
\n\
x = asum(inparray)\n\
x = asum(inparray, disovfl=True, maxlen=y)\n\
\n\
* inparray - The array to be summed.\n\
* disovfl - If this keyword parameter is True, integer overflow checking \n\
  will be disabled. This is an optional parameter.\n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored.");



/* A list of all the methods defined by this module. 
 "asum" is the name seen inside of Python. 
 "py_asum" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef asum_methods[] = {
	{"asum",  (PyCFunction)py_asum, METH_VARARGS | METH_KEYWORDS, asum__doc__}, 
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef asummodule = {
    PyModuleDef_HEAD_INIT,
    "asum",
    NULL,
    -1,
    asum_methods
};

PyMODINIT_FUNC PyInit_asum(void)
{
    return PyModule_Create(&asummodule);
};

/*--------------------------------------------------------------------------- */
