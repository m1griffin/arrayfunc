//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   amax_simd_armv7.c
// Purpose:  Calculate the amax of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     08-Oct-2019
// Ver:      27-Mar-2020.
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

#include "simddefs.h"
#ifdef AF_HASSIMD_ARMv7_32BIT
#include "arm_neon.h"
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
#if defined(AF_HASSIMD_ARMv7_32BIT)
signed long long amax_signed_char_simd(Py_ssize_t arraylen, signed char *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	signed char maxfound;

	signed char maxvals[CHARSIMDSIZE];
	int8x8_t maxslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Initialise the comparison values.
	maxslice = vld1_s8( &data[0]);

	// Use SIMD.
	for(x = CHARSIMDSIZE; x < alignedlength; x += CHARSIMDSIZE) {
		dataslice = vld1_s8( &data[x]);
		maxslice = vmax_s8 (maxslice, dataslice);
	}

	// Find the max within the slice.
	vst1_s8( maxvals,   maxslice);
	maxfound = maxvals[0];
	for (y = 1; y < CHARSIMDSIZE; y++) {
		if (maxvals[y] > maxfound) {
			maxfound = maxvals[y];
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (signed long long) maxfound;
}
#endif
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: B
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
unsigned long long amax_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	unsigned char maxfound;

	unsigned char maxvals[CHARSIMDSIZE];
	uint8x8_t maxslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Initialise the comparison values.
	maxslice = vld1_u8( &data[0]);

	// Use SIMD.
	for(x = CHARSIMDSIZE; x < alignedlength; x += CHARSIMDSIZE) {
		dataslice = vld1_u8( &data[x]);
		maxslice = vmax_u8 (maxslice, dataslice);
	}

	// Find the max within the slice.
	vst1_u8( maxvals,   maxslice);
	maxfound = maxvals[0];
	for (y = 1; y < CHARSIMDSIZE; y++) {
		if (maxvals[y] > maxfound) {
			maxfound = maxvals[y];
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (unsigned long long) maxfound;
}
#endif
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: h
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
signed long long amax_signed_short_simd(Py_ssize_t arraylen, signed short *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	signed short maxfound;

	signed short maxvals[SHORTSIMDSIZE];
	int16x4_t maxslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Initialise the comparison values.
	maxslice = vld1_s16( &data[0]);

	// Use SIMD.
	for(x = SHORTSIMDSIZE; x < alignedlength; x += SHORTSIMDSIZE) {
		dataslice = vld1_s16( &data[x]);
		maxslice = vmax_s16 (maxslice, dataslice);
	}

	// Find the max within the slice.
	vst1_s16( maxvals,   maxslice);
	maxfound = maxvals[0];
	for (y = 1; y < SHORTSIMDSIZE; y++) {
		if (maxvals[y] > maxfound) {
			maxfound = maxvals[y];
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (signed long long) maxfound;
}
#endif
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: H
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
unsigned long long amax_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	unsigned short maxfound;

	unsigned short maxvals[SHORTSIMDSIZE];
	uint16x4_t maxslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Initialise the comparison values.
	maxslice = vld1_u16( &data[0]);

	// Use SIMD.
	for(x = SHORTSIMDSIZE; x < alignedlength; x += SHORTSIMDSIZE) {
		dataslice = vld1_u16( &data[x]);
		maxslice = vmax_u16 (maxslice, dataslice);
	}

	// Find the max within the slice.
	 vst1_u16( maxvals,   maxslice);
	maxfound = maxvals[0];
	for (y = 1; y < SHORTSIMDSIZE; y++) {
		if (maxvals[y] > maxfound) {
			maxfound = maxvals[y];
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (unsigned long long) maxfound;
}
#endif
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: i
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
signed long long amax_signed_int_simd(Py_ssize_t arraylen, signed int *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	signed int maxfound;

	signed int maxvals[INTSIMDSIZE];
	int32x2_t  maxslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Initialise the comparison values.
	maxslice = vld1_s32( &data[0]);

	// Use SIMD.
	for(x = INTSIMDSIZE; x < alignedlength; x += INTSIMDSIZE) {
		dataslice = vld1_s32( &data[x]);
		maxslice = vmax_s32 (maxslice, dataslice);
	}

	// Find the max within the slice.
	vst1_s32( maxvals,   maxslice);
	maxfound = maxvals[0];
	for (y = 1; y < INTSIMDSIZE; y++) {
		if (maxvals[y] > maxfound) {
			maxfound = maxvals[y];
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (signed long long) maxfound;
}
#endif
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: I
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
unsigned long long amax_unsigned_int_simd(Py_ssize_t arraylen, unsigned int *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	unsigned int maxfound;

	unsigned int maxvals[INTSIMDSIZE];
	uint32x2_t maxslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Initialise the comparison values.
	maxslice = vld1_u32( &data[0]);

	// Use SIMD.
	for(x = INTSIMDSIZE; x < alignedlength; x += INTSIMDSIZE) {
		dataslice = vld1_u32( &data[x]);
		maxslice = vmax_u32 (maxslice, dataslice);
	}

	// Find the max within the slice.
	vst1_u32( maxvals,   maxslice);
	maxfound = maxvals[0];
	for (y = 1; y < INTSIMDSIZE; y++) {
		if (maxvals[y] > maxfound) {
			maxfound = maxvals[y];
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (unsigned long long) maxfound;
}
#endif
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: f
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
double amax_float_simd(Py_ssize_t arraylen, float *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	float maxfound;

	float maxvals[FLOATSIMDSIZE];
	float32x2_t maxslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Initialise the comparison values.
	maxslice = vld1_f32( &data[0]);

	// Use SIMD.
	for(x = FLOATSIMDSIZE; x < alignedlength; x += FLOATSIMDSIZE) {
		dataslice = vld1_f32( &data[x]);
		maxslice = vmax_f32 (maxslice, dataslice);
	}

	// Find the max within the slice.
	vst1_f32( maxvals,   maxslice);
	maxfound = maxvals[0];
	for (y = 1; y < FLOATSIMDSIZE; y++) {
		if (maxvals[y] > maxfound) {
			maxfound = maxvals[y];
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return (double) maxfound;
}
#endif
/*--------------------------------------------------------------------------- */

