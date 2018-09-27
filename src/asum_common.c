//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   asum_common.c
// Purpose:  Sum all the values in an array.
//           Common platform independent code.
// Language: C
// Date:     15-May-2014
// Ver:      19-Jun-2018.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2018    Michael Griffin    <m12.griffin@gmail.com>
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

#include "simddefs.h"
#ifdef AF_HASSIMD
#include "asum_simd_x86.h"
#endif

#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// Auto generated code goes below.
/*--------------------------------------------------------------------------- */
/* For array code: b
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
signed long asum_signed_char(Py_ssize_t arraylen, signed char *data, signed int *errflag, signed int ignoreerrors) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors) {
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
/* For array code: B
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
unsigned long asum_unsigned_char(Py_ssize_t arraylen, unsigned char *data, signed int *errflag, signed int ignoreerrors) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors) {
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
/* For array code: h
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
signed long asum_signed_short(Py_ssize_t arraylen, signed short *data, signed int *errflag, signed int ignoreerrors) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors) {
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
/* For array code: H
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
unsigned long asum_unsigned_short(Py_ssize_t arraylen, unsigned short *data, signed int *errflag, signed int ignoreerrors) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors) {
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
/* For array code: i
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
signed long asum_signed_int(Py_ssize_t arraylen, signed int *data, signed int *errflag, signed int ignoreerrors) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors) {
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
/* For array code: I
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
unsigned long asum_unsigned_int(Py_ssize_t arraylen, unsigned int *data, signed int *errflag, signed int ignoreerrors) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors) {
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
/* For array code: l
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
signed long asum_signed_long(Py_ssize_t arraylen, signed long *data, signed int *errflag, signed int ignoreerrors) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors) {
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
/* For array code: L
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
unsigned long asum_unsigned_long(Py_ssize_t arraylen, unsigned long *data, signed int *errflag, signed int ignoreerrors) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors) {
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
/* For array code: q
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
signed long long asum_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed int *errflag, signed int ignoreerrors) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors) {
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


#ifdef AF_HASSIMD
	// SIMD version. Only use this if overflow checking is disabled.
	if (ignoreerrors && !nosimd && (arraylen >= (FLOATSIMDSIZE * 2))) {
		return asum_float_simd(arraylen, data);
	}
#endif


	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors) {
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


#ifdef AF_HASSIMD
	// SIMD version. Only use this if overflow checking is disabled.
	if (ignoreerrors && !nosimd && (arraylen >= (DOUBLESIMDSIZE * 2))) {
		return asum_double_simd(arraylen, data);
	}
#endif


	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors) {
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
