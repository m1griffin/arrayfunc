//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   asum.c
// Purpose:  Calculate the asum of values in an array.
// Language: C
// Date:     15-Nov-2017.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2022    Michael Griffin    <m12.griffin@gmail.com>
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

#include "arrayparams_asum.h"

#include "simddefs.h"

#include "asum_defs.h"

#ifdef AF_HASSIMD_X86
#include "asum_simd_x86.h"
#endif


#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
#include "arm_neon.h"
#endif

#ifdef AF_HASSIMD_ARMv7_32BIT
#include "asum_simd_armv7.h"
#endif

#ifdef AF_HASSIMD_ARM_AARCH64
#include "asum_simd_armv8.h"
#endif


/*--------------------------------------------------------------------------- */

/* These are for use with the integer versions of asum to optimize overflow
   checking performance by determining if an array is short enough that there
   is no risk that the accumulated sum may overflow when summing that data type. 
   Each value represents the maximum number of array elements for which it is 
   safe to skip overflow checks without risk of integer overflow even if the 
   array is full of the largest values for that type. 
   These are defined for known architectures as there seems to be no platform
   independent means of determining whether it is being compiled for 32 or 64
   bits. Array indexes are limited to a value related to Py_ssize_t. However
   Py_ssize_t will vary depending on whether Python is compiled for 32 or 64 
   bits. There is currently no means of determining the size of Py_ssize_t
   at compile time due to the way it is defined.
*/

#if defined( __x86_64__ ) ||  defined( __i386__ ) ||  defined( __ARM_64BIT_STATE ) ||  defined( __ARM_32BIT_STATE )

// 64 bit architectures.
#if defined( __x86_64__ ) ||  defined( __ARM_64BIT_STATE )

// Array codes B, b
#define CHARSKIPOVFLCHECK 72057594037927936LL
// Array codes H, h
#define SHORTSKIPOVFLCHECK 281474976710656LL
// Array codes I, i
#define INTSKIPOVFLCHECK 4294967296

#endif


// 32 bit architectures.
#if defined( __i386__ ) ||  defined( __ARM_32BIT_STATE )

// Array codes B, b
#define CHARSKIPOVFLCHECK 2147483648
// Array codes H, h
#define SHORTSKIPOVFLCHECK 2147483648
// Array codes I, i
#define INTSKIPOVFLCHECK 2147483648

#endif


#else
// Default values for unknown architectures which don't trigger the optimization. 

// Array codes B, b
#define CHARSKIPOVFLCHECK 0
// Array codes H, h
#define SHORTSKIPOVFLCHECK 0
// Array codes I, i
#define INTSKIPOVFLCHECK 0

#endif

// Skip overflow checks for b and B arrays.
#define charskipovflcheck(arraylen) (arraylen <= CHARSKIPOVFLCHECK)
// Skip overflow checks for h and H arrays.
#define shortskipovflcheck(arraylen) (arraylen <= SHORTSKIPOVFLCHECK)
// Skip overflow checks for i and I arrays.
#define intskipovflcheck(arraylen) (arraylen <= INTSKIPOVFLCHECK)


/*--------------------------------------------------------------------------- */
/*--------------------------------------------------------------------------- */
/* For array code: b
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
long long asum_signed_char(Py_ssize_t arraylen, signed char *data, signed int *errflag, signed int ignoreerrors, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	long long partialsum = 0;

	*errflag = 0;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)

	// SIMD version. 
	if (!nosimd && enoughforsimd(arraylen, CHARSIMDSIZE)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			partialsum = asum_signed_char_simd(arraylen, data);
		} else {
			partialsum = asum_signed_char_simd_ovfl(arraylen, data, errflag);
		}
	} else {
#endif

		// Overflow checking disabled.
		if (ignoreerrors || charskipovflcheck(arraylen)) {
			for (x = 0; x < arraylen; x++) {
				partialsum = partialsum + data[x];
			}
		} else {
			// Overflow checking enabled.
			for (x = 0; x < arraylen; x++) {
				if (loop_willoverflow_signed(data[x], partialsum)) {
					*errflag = ARR_ERR_OVFL;
					return partialsum; 
				} else {
					partialsum = partialsum + data[x];
				}
			}
		}

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	}
#endif

	return partialsum;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: B
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
unsigned long long asum_unsigned_char(Py_ssize_t arraylen, unsigned char *data, signed int *errflag, signed int ignoreerrors, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long long partialsum = 0;

	*errflag = 0;

#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)

	// SIMD version. 
	if (!nosimd && enoughforsimd(arraylen, CHARSIMDSIZE)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			partialsum = asum_unsigned_char_simd(arraylen, data);
		} else {
			partialsum = asum_unsigned_char_simd_ovfl(arraylen, data, errflag);
		}
	} else {
#endif

		// Overflow checking disabled.
		if (ignoreerrors || charskipovflcheck(arraylen)) {
			for (x = 0; x < arraylen; x++) {
				partialsum = partialsum + data[x];
			}
		} else {
			// Overflow checking enabled.
			for (x = 0; x < arraylen; x++) {
				if (loop_willoverflow_unsigned(data[x], partialsum)) {
					*errflag = ARR_ERR_OVFL;
					return partialsum; 
				} else {
					partialsum = partialsum + data[x];
				}
			}
		}

#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	}
#endif

	return partialsum;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: h
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
long long asum_signed_short(Py_ssize_t arraylen, signed short *data, signed int *errflag, signed int ignoreerrors, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	long long partialsum = 0;

	*errflag = 0;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)

	// SIMD version. 
	if (!nosimd && enoughforsimd(arraylen, SHORTSIMDSIZE)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			partialsum = asum_signed_short_simd(arraylen, data);
		} else {
			partialsum = asum_signed_short_simd_ovfl(arraylen, data, errflag);
		}
	} else {
#endif

		// Overflow checking disabled.
		if (ignoreerrors || shortskipovflcheck(arraylen)) {
			for (x = 0; x < arraylen; x++) {
				partialsum = partialsum + data[x];
			}
		} else {
			// Overflow checking enabled.
			for (x = 0; x < arraylen; x++) {
				if (loop_willoverflow_signed(data[x], partialsum)) {
					*errflag = ARR_ERR_OVFL;
					return partialsum; 
				} else {
					partialsum = partialsum + data[x];
				}
			}
		}

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	}
#endif

	return partialsum;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: H
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
unsigned long long asum_unsigned_short(Py_ssize_t arraylen, unsigned short *data, signed int *errflag, signed int ignoreerrors, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long long partialsum = 0;

	*errflag = 0;

#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)

	// SIMD version. 
	if (!nosimd && enoughforsimd(arraylen, SHORTSIMDSIZE)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			partialsum = asum_unsigned_short_simd(arraylen, data);
		} else {
			partialsum = asum_unsigned_short_simd_ovfl(arraylen, data, errflag);
		}
	} else {
#endif

		// Overflow checking disabled.
		if (ignoreerrors || shortskipovflcheck(arraylen)) {
			for (x = 0; x < arraylen; x++) {
				partialsum = partialsum + data[x];
			}
		} else {
			// Overflow checking enabled.
			for (x = 0; x < arraylen; x++) {
				if (loop_willoverflow_unsigned(data[x], partialsum)) {
					*errflag = ARR_ERR_OVFL;
					return partialsum; 
				} else {
					partialsum = partialsum + data[x];
				}
			}
		}

#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	}
#endif

	return partialsum;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: i
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
long long asum_signed_int(Py_ssize_t arraylen, signed int *data, signed int *errflag, signed int ignoreerrors, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	long long partialsum = 0;

	*errflag = 0;

#if defined(AF_HASSIMD_X86)

	// SIMD version. 
	if (!nosimd && enoughforsimd(arraylen, INTSIMDSIZE)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			partialsum = asum_signed_int_simd(arraylen, data);
		} else {
			partialsum = asum_signed_int_simd_ovfl(arraylen, data, errflag);
		}
	} else {
#endif

		// Overflow checking disabled.
		if (ignoreerrors || intskipovflcheck(arraylen)) {
			for (x = 0; x < arraylen; x++) {
				partialsum = partialsum + data[x];
			}
		} else {
			// Overflow checking enabled.
			for (x = 0; x < arraylen; x++) {
				if (loop_willoverflow_signed(data[x], partialsum)) {
					*errflag = ARR_ERR_OVFL;
					return partialsum; 
				} else {
					partialsum = partialsum + data[x];
				}
			}
		}

#if defined(AF_HASSIMD_X86)
	}
#endif

	return partialsum;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: I
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
unsigned long long asum_unsigned_int(Py_ssize_t arraylen, unsigned int *data, signed int *errflag, signed int ignoreerrors) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors || intskipovflcheck(arraylen)) {
		for (x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for (x = 0; x < arraylen; x++) {
			if (loop_willoverflow_unsigned(data[x], partialsum)) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			} else {
				partialsum = partialsum + data[x];
			}
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: l
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
long long asum_signed_long(Py_ssize_t arraylen, signed long *data, signed int *errflag, signed int ignoreerrors) { 

	// array index counter. 
	Py_ssize_t x; 
	long long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for (x = 0; x < arraylen; x++) {
			if (loop_willoverflow_signed(data[x], partialsum)) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			} else {
				partialsum = partialsum + data[x];
			}
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: L
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
unsigned long long asum_unsigned_long(Py_ssize_t arraylen, unsigned long *data, signed int *errflag, signed int ignoreerrors) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for (x = 0; x < arraylen; x++) {
			if (loop_willoverflow_unsigned(data[x], partialsum)) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			} else {
				partialsum = partialsum + data[x];
			}
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: q
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
long long asum_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed int *errflag, signed int ignoreerrors) { 

	// array index counter. 
	Py_ssize_t x; 
	long long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for (x = 0; x < arraylen; x++) {
			if (loop_willoverflow_signed(data[x], partialsum)) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			} else {
				partialsum = partialsum + data[x];
			}
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: Q
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
unsigned long long asum_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, signed int *errflag, signed int ignoreerrors) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for (x = 0; x < arraylen; x++) {
			if (loop_willoverflow_unsigned(data[x], partialsum)) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			} else {
				partialsum = partialsum + data[x];
			}
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */


/* This function is used to overcome what appears to be a compiler bug in 
   x86 32 bit platforms. When two maximum float (32 bit floating point numbers) 
   values were added together they would result in a value which should have 
   been infinity, but instead were twice the maximum value (6.805646932770577e+38).
   Passing the result into and out of this function seems to force the correct 
   result of "inf" to be produced. A variety of different fixes and tweaks were 
   tried, but this was the simpliest that worked.
*/
#ifdef AF_FIXFLOAT_i386
float fixfloatfinite(float inval) {
	return inval;
}
#endif

/*--------------------------------------------------------------------------- */
/* For array code: f
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   nosimd = If true, disable SIMD.
   Returns: The sum of the array.
*/
float asum_float(Py_ssize_t arraylen, float *data, signed int *errflag, signed int ignoreerrors, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	float partialsum = 0.0;

	*errflag = 0;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version. 
	if (!nosimd && enoughforsimd(arraylen, FLOATSIMDSIZE)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			partialsum = asum_float_simd(arraylen, data);
		} else {
			partialsum = asum_float_simd_ovfl(arraylen, data, errflag);
		}
	} else {
#endif

		// Non-SIMD version.
		// Overflow checking disabled.
		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				partialsum = partialsum + data[x];
			}
#ifdef AF_FIXFLOAT_i386
			partialsum = fixfloatfinite(partialsum);
#endif

		} else {
			// Overflow checking enabled.
			for (x = 0; x < arraylen; x++) {
				partialsum = partialsum + data[x];
			}
			// Non-finite data will propagate through the sum, so we
			// only have to check it when we are all done.
			if (!isfinite(partialsum)) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
		}
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	}
#endif

	return partialsum;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: d
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   nosimd = If true, disable SIMD.
   Returns: The sum of the array.
*/
double asum_double(Py_ssize_t arraylen, double *data, signed int *errflag, signed int ignoreerrors, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	double partialsum = 0.0;

	*errflag = 0;

#if defined(AF_HASSIMD_X86)
	// SIMD version. 
	if (!nosimd && enoughforsimd(arraylen, DOUBLESIMDSIZE)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			partialsum = asum_double_simd(arraylen, data);
		} else {
			partialsum = asum_double_simd_ovfl(arraylen, data, errflag);
		}
	} else {
#endif

		// Non-SIMD version.
		// Overflow checking disabled.
		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				partialsum = partialsum + data[x];
			}

		} else {
			// Overflow checking enabled.
			for (x = 0; x < arraylen; x++) {
				partialsum = partialsum + data[x];
			}
			// Non-finite data will propagate through the sum, so we
			// only have to check it when we are all done.
			if (!isfinite(partialsum)) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
		}
#if defined(AF_HASSIMD_X86)
	}
#endif

	return partialsum;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_asum(PyObject *self, PyObject *args, PyObject *keywds) {


	// This is used to hold the parsed parameters.
	struct args_params_asum arraydata = ARGSINIT_ASUM;

	// The sum of the array, as a python object.
	PyObject *sumreturn;

	// Indicates an error.
	signed int errflag = 0;

	// Results are different types.
	long long resultll = 0;
	unsigned long long resultull = 0;
	double resultd = 0.0;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_asum(self, args, keywds, "asum");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}


	// The length of the data array.
	if (arraydata.arraylength < 1) {
		// Release the buffers. 
		releasebuffers_asum(arraydata);
		ErrMsgArrayLengthErr();
		return NULL;
	}



	/* Call the C function */
	switch(arraydata.arraytype) {
		// signed char
		case 'b' : {
			resultll = asum_signed_char(arraydata.arraylength, arraydata.array1.b, &errflag, arraydata.ignoreerrors, arraydata.nosimd);
			sumreturn = PyLong_FromLongLong(resultll);
			break;
		}
		// unsigned char
		case 'B' : {
			resultull = asum_unsigned_char(arraydata.arraylength, arraydata.array1.B, &errflag, arraydata.ignoreerrors, arraydata.nosimd);
			sumreturn = PyLong_FromUnsignedLongLong(resultull);
			break;
		}
		// signed short
		case 'h' : {
			resultll = asum_signed_short(arraydata.arraylength, arraydata.array1.h, &errflag, arraydata.ignoreerrors, arraydata.nosimd);
			sumreturn = PyLong_FromLongLong(resultll);
			break;
		}
		// unsigned short
		case 'H' : {
			resultull = asum_unsigned_short(arraydata.arraylength, arraydata.array1.H, &errflag, arraydata.ignoreerrors, arraydata.nosimd);
			sumreturn = PyLong_FromUnsignedLongLong(resultull);
			break;
		}
		// signed int
		case 'i' : {
			resultll = asum_signed_int(arraydata.arraylength, arraydata.array1.i, &errflag, arraydata.ignoreerrors, arraydata.nosimd);
			sumreturn = PyLong_FromLongLong(resultll);
			break;
		}
		// unsigned int
		case 'I' : {
			resultull = asum_unsigned_int(arraydata.arraylength, arraydata.array1.I, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromUnsignedLongLong(resultull);
			break;
		}
		// signed long
		case 'l' : {
			resultll = asum_signed_long(arraydata.arraylength, arraydata.array1.l, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromLongLong(resultll);
			break;
		}
		// unsigned long
		case 'L' : {
			resultull = asum_unsigned_long(arraydata.arraylength, arraydata.array1.L, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromUnsignedLongLong(resultull);
			break;
		}
		// signed long long
		case 'q' : {
			resultll = asum_signed_long_long(arraydata.arraylength, arraydata.array1.q, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromLongLong(resultll);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultull = asum_unsigned_long_long(arraydata.arraylength, arraydata.array1.Q, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromUnsignedLongLong(resultull);
			break;
		}
		// float
		case 'f' : {
			resultd = (double) asum_float(arraydata.arraylength, arraydata.array1.f, &errflag, arraydata.ignoreerrors, arraydata.nosimd);
			sumreturn = PyFloat_FromDouble(resultd);
			break;
		}
		// double
		case 'd' : {
			resultd = asum_double(arraydata.arraylength, arraydata.array1.d, &errflag, arraydata.ignoreerrors, arraydata.nosimd);
			sumreturn = PyFloat_FromDouble(resultd);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_asum(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_asum(arraydata);


	// Signal the errors.

	if (errflag == ARR_ERR_OVFL) {
		ErrMsgArithOverflowCalc();
		return NULL;
	}


	return sumreturn;

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(asum__doc__,
"asum \n\
_____________________________ \n\
\n\
Calculate the arithmetic sum of an array.  \n\
\n\
======================  ============================================== \n\
Equivalent to:          sum() \n\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
  result = asum(array) \n\
  result = asum(array, maxlen=y) \n\
  result = asum(array, nosimd=False) \n\
  result = asum(array, matherrors=False) \n\
\n\
* array - The input data array to be examined. \n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored. \n\
* nosimd - If True, SIMD acceleration is disabled if present. \n\
  The default is False (SIMD acceleration is enabled if present). \n\
* matherrors - If True, checks for numerical errors including integer \n\
  overflow are ignored. \n\
* result - The sum of the array. \n\
");


/*--------------------------------------------------------------------------- */

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

