//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   amax_common.c
// Purpose:  Find the maximum value in an array.
//           Common platform independent code.
// Language: C
// Date:     04-May-2014
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
#include "amax_simd_x86.h"
#endif

#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// Auto generated code goes below.

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

