//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   amax.c
// Purpose:  Calculate the amax of values in an array.
// Language: C
// Date:     12-May-2019.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2020    Michael Griffin    <m12.griffin@gmail.com>
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
#include <math.h>

#include "arrayerrs.h"

#include "arrayparams_base.h"

#include "arrayparams_booloutsimd.h"

#include "simddefs.h"


#ifdef AF_HASSIMD_X86
#include "amax_simd_x86.h"
#endif

#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
#include "arm_neon.h"
#endif

#if defined(AF_HASSIMD_ARMv7_32BIT)
#include "amax_simd_armv7.h"
#endif

#if defined(AF_HASSIMD_ARM_AARCH64)
#include "amax_simd_armv8.h"
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: b
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
signed long long amax_signed_char(Py_ssize_t arraylen, signed char *data) { 

	// array index counter. 
	Py_ssize_t x; 
	signed char maxfound;

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (signed long long) maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: b
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
signed long long amax_signed_char_select(Py_ssize_t arraylen, int nosimd, signed char *data) { 

	#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
		return amax_signed_char_simd(arraylen, data);
	} else {
	#endif
		return amax_signed_char(arraylen, data);
	#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	}
	#endif

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: B
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
unsigned long long amax_unsigned_char(Py_ssize_t arraylen, unsigned char *data) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned char maxfound;

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (unsigned long long) maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: B
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
unsigned long long amax_unsigned_char_select(Py_ssize_t arraylen, int nosimd, unsigned char *data) { 

	#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
		return amax_unsigned_char_simd(arraylen, data);
	} else {
	#endif
		return amax_unsigned_char(arraylen, data);
	#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	}
	#endif

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: h
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
signed long long amax_signed_short(Py_ssize_t arraylen, signed short *data) { 

	// array index counter. 
	Py_ssize_t x; 
	signed short maxfound;

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (signed long long) maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: h
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
signed long long amax_signed_short_select(Py_ssize_t arraylen, int nosimd, signed short *data) { 

	#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
		return amax_signed_short_simd(arraylen, data);
	} else {
	#endif
		return amax_signed_short(arraylen, data);
	#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	}
	#endif

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: H
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
unsigned long long amax_unsigned_short(Py_ssize_t arraylen, unsigned short *data) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned short maxfound;

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (unsigned long long) maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: H
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
unsigned long long amax_unsigned_short_select(Py_ssize_t arraylen, int nosimd, unsigned short *data) { 

	#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
		return amax_unsigned_short_simd(arraylen, data);
	} else {
	#endif
		return amax_unsigned_short(arraylen, data);
	#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	}
	#endif

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: i
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
signed long long amax_signed_int(Py_ssize_t arraylen, signed int *data) { 

	// array index counter. 
	Py_ssize_t x; 
	signed int maxfound;

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (signed long long) maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: i
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
signed long long amax_signed_int_select(Py_ssize_t arraylen, int nosimd, signed int *data) { 

	#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
		return amax_signed_int_simd(arraylen, data);
	} else {
	#endif
		return amax_signed_int(arraylen, data);
	#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	}
	#endif

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: I
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
unsigned long long amax_unsigned_int(Py_ssize_t arraylen, unsigned int *data) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned int maxfound;

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (unsigned long long) maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: I
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
unsigned long long amax_unsigned_int_select(Py_ssize_t arraylen, int nosimd, unsigned int *data) { 

	#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
		return amax_unsigned_int_simd(arraylen, data);
	} else {
	#endif
		return amax_unsigned_int(arraylen, data);
	#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	}
	#endif

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: l
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
signed long long amax_signed_long(Py_ssize_t arraylen, signed long *data) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long maxfound;

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (signed long long) maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: L
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
unsigned long long amax_unsigned_long(Py_ssize_t arraylen, unsigned long *data) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long maxfound;

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (unsigned long long) maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: q
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
signed long long amax_signed_long_long(Py_ssize_t arraylen, signed long long *data) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long long maxfound;

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (signed long long) maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: Q
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
unsigned long long amax_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long long maxfound;

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (unsigned long long) maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: f
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
double amax_float(Py_ssize_t arraylen, float *data) { 

	// array index counter. 
	Py_ssize_t x; 
	float maxfound;

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (double) maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: f
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
double amax_float_select(Py_ssize_t arraylen, int nosimd, float *data) { 

	#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	if (!nosimd && (arraylen >= (FLOATSIMDSIZE * 2))) {
		return amax_float_simd(arraylen, data);
	} else {
	#endif
		return amax_float(arraylen, data);
	#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	}
	#endif

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: d
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
double amax_double(Py_ssize_t arraylen, double *data) { 

	// array index counter. 
	Py_ssize_t x; 
	double maxfound;

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (double) maxfound;
}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: d
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
double amax_double_select(Py_ssize_t arraylen, int nosimd, double *data) { 

	#if defined(AF_HASSIMD_X86)
	if (!nosimd && (arraylen >= (DOUBLESIMDSIZE * 2))) {
		return amax_double_simd(arraylen, data);
	} else {
	#endif
		return amax_double(arraylen, data);
	#if defined(AF_HASSIMD_X86)
	}
	#endif

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_amax(PyObject *self, PyObject *args, PyObject *keywds) {


	// This is used to hold the parsed parameters.
	struct args_params_booloutsimd arraydata = ARGSINIT_BOOLOUTSIMD;


	// The parameter version is available in all possible types.
	signed long long resultq;
	unsigned long long resultQ;
	double resultd;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_booloutsimd(self, args, keywds, "amax");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}


	// The length of the data array.
	if (arraydata.arraylength < 1) {
		// Release the buffers. 
		releasebuffers_booloutsimd(arraydata);
		ErrMsgArrayLengthErr();
		return NULL;
	}



	/* Call the C function */
	switch(arraydata.arraytype) {
		// signed char
		case 'b' : {
			resultq = amax_signed_char_select(arraydata.arraylength, arraydata.nosimd, arraydata.array1.b);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromLongLong(resultq);
			break;
		}
		// unsigned char
		case 'B' : {
			resultQ = amax_unsigned_char_select(arraydata.arraylength, arraydata.nosimd, arraydata.array1.B);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromUnsignedLongLong(resultQ);
			break;
		}
		// signed short
		case 'h' : {
			resultq = amax_signed_short_select(arraydata.arraylength, arraydata.nosimd, arraydata.array1.h);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromLongLong(resultq);
			break;
		}
		// unsigned short
		case 'H' : {
			resultQ = amax_unsigned_short_select(arraydata.arraylength, arraydata.nosimd, arraydata.array1.H);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromUnsignedLongLong(resultQ);
			break;
		}
		// signed int
		case 'i' : {
			resultq = amax_signed_int_select(arraydata.arraylength, arraydata.nosimd, arraydata.array1.i);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromLongLong(resultq);
			break;
		}
		// unsigned int
		case 'I' : {
			resultQ = amax_unsigned_int_select(arraydata.arraylength, arraydata.nosimd, arraydata.array1.I);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromUnsignedLongLong(resultQ);
			break;
		}
		// signed long
		case 'l' : {
			resultq = amax_signed_long(arraydata.arraylength, arraydata.array1.l);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromLongLong(resultq);
			break;
		}
		// unsigned long
		case 'L' : {
			resultQ = amax_unsigned_long(arraydata.arraylength, arraydata.array1.L);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromUnsignedLongLong(resultQ);
			break;
		}
		// signed long long
		case 'q' : {
			resultq = amax_signed_long_long(arraydata.arraylength, arraydata.array1.q);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromLongLong(resultq);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultQ = amax_unsigned_long_long(arraydata.arraylength, arraydata.array1.Q);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromUnsignedLongLong(resultQ);
			break;
		}
		// float
		case 'f' : {
			resultd = amax_float_select(arraydata.arraylength, arraydata.nosimd, arraydata.array1.f);
			releasebuffers_booloutsimd(arraydata);
			return PyFloat_FromDouble(resultd);
			break;
		}
		// double
		case 'd' : {
			resultd = amax_double_select(arraydata.arraylength, arraydata.nosimd, arraydata.array1.d);
			releasebuffers_booloutsimd(arraydata);
			return PyFloat_FromDouble(resultd);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_booloutsimd(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_booloutsimd(arraydata);


}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(amax__doc__,
"amax \n\
_____________________________ \n\
\n\
Calculate amax over the values in an array.  \n\
\n\
======================  ============================================== \n\
Equivalent to:          max(x) \n\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
  result = amax(array) \n\
  result = amax(array, maxlen=y) \n\
  result = amax(array, nosimd=False) \n\
\n\
* array - The input data array to be examined. \n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored. \n\
* nosimd - If True, SIMD acceleration is disabled if present. \n\
  The default is False (SIMD acceleration is enabled if present). \n\
* result = The  maximum of all the values in the array. \n\
");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "amax" is the name seen inside of Python. 
 "py_amax" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef amax_methods[] = {
	{"amax",  (PyCFunction)py_amax, METH_VARARGS | METH_KEYWORDS, amax__doc__}, 
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

