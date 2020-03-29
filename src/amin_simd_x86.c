//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   amin_simd_x86.c
// Purpose:  Calculate the amin of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     16-Apr-2019
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

#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// Auto generated code goes below.

/*--------------------------------------------------------------------------- */
/* For array code: b
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The minimum value found.
*/
#if defined(AF_HASSIMD_X86)
signed long long amin_signed_char_simd(Py_ssize_t arraylen, signed char *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	signed char minfound;

	signed char minvals[CHARSIMDSIZE];
	v16qi minslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Initialise the comparison values.
	minslice = (v16qi) __builtin_ia32_lddqu((char *) &data[0]);

	// Use SIMD.
	for(x = CHARSIMDSIZE; x < alignedlength; x += CHARSIMDSIZE) {
		dataslice = (v16qi) __builtin_ia32_lddqu((char *) &data[x]);
		minslice = __builtin_ia32_pminsb128 (minslice, dataslice);
	}

	// Find the min within the slice.
	__builtin_ia32_storedqu((char *) minvals,   minslice);
	minfound = minvals[0];
	for (y = 1; y < CHARSIMDSIZE; y++) {
		if (minvals[y] < minfound) {
			minfound = minvals[y];
		}
	}

	// Get the min value within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		if (data[x] < minfound) {
			minfound = data[x];
		}
	}

	return (signed long long) minfound;
}
#endif
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: B
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The minimum value found.
*/
#if defined(AF_HASSIMD_X86)
unsigned long long amin_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	unsigned char minfound;

	unsigned char minvals[CHARSIMDSIZE];
	v16qi minslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Initialise the comparison values.
	minslice = (v16qi) __builtin_ia32_lddqu((char *) &data[0]);

	// Use SIMD.
	for(x = CHARSIMDSIZE; x < alignedlength; x += CHARSIMDSIZE) {
		dataslice = (v16qi) __builtin_ia32_lddqu((char *) &data[x]);
		minslice = __builtin_ia32_pminub128 (minslice, dataslice);
	}

	// Find the min within the slice.
	__builtin_ia32_storedqu((char *) minvals,   minslice);
	minfound = minvals[0];
	for (y = 1; y < CHARSIMDSIZE; y++) {
		if (minvals[y] < minfound) {
			minfound = minvals[y];
		}
	}

	// Get the min value within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		if (data[x] < minfound) {
			minfound = data[x];
		}
	}

	return (unsigned long long) minfound;
}
#endif
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: h
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The minimum value found.
*/
#if defined(AF_HASSIMD_X86)
signed long long amin_signed_short_simd(Py_ssize_t arraylen, signed short *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	signed short minfound;

	signed short minvals[SHORTSIMDSIZE];
	v8hi minslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Initialise the comparison values.
	minslice = (v8hi) __builtin_ia32_lddqu((char *) &data[0]);

	// Use SIMD.
	for(x = SHORTSIMDSIZE; x < alignedlength; x += SHORTSIMDSIZE) {
		dataslice = (v8hi) __builtin_ia32_lddqu((char *) &data[x]);
		minslice = __builtin_ia32_pminsw128 (minslice, dataslice);
	}

	// Find the min within the slice.
	__builtin_ia32_storedqu((char *) minvals, (v16qi)  minslice);
	minfound = minvals[0];
	for (y = 1; y < SHORTSIMDSIZE; y++) {
		if (minvals[y] < minfound) {
			minfound = minvals[y];
		}
	}

	// Get the min value within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		if (data[x] < minfound) {
			minfound = data[x];
		}
	}

	return (signed long long) minfound;
}
#endif
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: H
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The minimum value found.
*/
#if defined(AF_HASSIMD_X86)
unsigned long long amin_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	unsigned short minfound;

	unsigned short minvals[SHORTSIMDSIZE];
	v8hi minslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Initialise the comparison values.
	minslice = (v8hi) __builtin_ia32_lddqu((char *) &data[0]);

	// Use SIMD.
	for(x = SHORTSIMDSIZE; x < alignedlength; x += SHORTSIMDSIZE) {
		dataslice = (v8hi) __builtin_ia32_lddqu((char *) &data[x]);
		minslice = __builtin_ia32_pminuw128 (minslice, dataslice);
	}

	// Find the min within the slice.
	__builtin_ia32_storedqu((char *) minvals, (v16qi)  minslice);
	minfound = minvals[0];
	for (y = 1; y < SHORTSIMDSIZE; y++) {
		if (minvals[y] < minfound) {
			minfound = minvals[y];
		}
	}

	// Get the min value within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		if (data[x] < minfound) {
			minfound = data[x];
		}
	}

	return (unsigned long long) minfound;
}
#endif
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: i
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The minimum value found.
*/
#if defined(AF_HASSIMD_X86)
signed long long amin_signed_int_simd(Py_ssize_t arraylen, signed int *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	signed int minfound;

	signed int minvals[INTSIMDSIZE];
	v4si minslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Initialise the comparison values.
	minslice = (v4si) __builtin_ia32_lddqu((char *) &data[0]);

	// Use SIMD.
	for(x = INTSIMDSIZE; x < alignedlength; x += INTSIMDSIZE) {
		dataslice = (v4si) __builtin_ia32_lddqu((char *) &data[x]);
		minslice = __builtin_ia32_pminsd128 (minslice, dataslice);
	}

	// Find the min within the slice.
	__builtin_ia32_storedqu((char *) minvals, (v16qi)  minslice);
	minfound = minvals[0];
	for (y = 1; y < INTSIMDSIZE; y++) {
		if (minvals[y] < minfound) {
			minfound = minvals[y];
		}
	}

	// Get the min value within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		if (data[x] < minfound) {
			minfound = data[x];
		}
	}

	return (signed long long) minfound;
}
#endif
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: I
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The minimum value found.
*/
#if defined(AF_HASSIMD_X86)
unsigned long long amin_unsigned_int_simd(Py_ssize_t arraylen, unsigned int *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	unsigned int minfound;

	unsigned int minvals[INTSIMDSIZE];
	v4si minslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Initialise the comparison values.
	minslice = (v4si) __builtin_ia32_lddqu((char *) &data[0]);

	// Use SIMD.
	for(x = INTSIMDSIZE; x < alignedlength; x += INTSIMDSIZE) {
		dataslice = (v4si) __builtin_ia32_lddqu((char *) &data[x]);
		minslice = __builtin_ia32_pminud128 (minslice, dataslice);
	}

	// Find the min within the slice.
	__builtin_ia32_storedqu((char *) minvals, (v16qi)  minslice);
	minfound = minvals[0];
	for (y = 1; y < INTSIMDSIZE; y++) {
		if (minvals[y] < minfound) {
			minfound = minvals[y];
		}
	}

	// Get the min value within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		if (data[x] < minfound) {
			minfound = data[x];
		}
	}

	return (unsigned long long) minfound;
}
#endif
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: f
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The minimum value found.
*/
#if defined(AF_HASSIMD_X86)
double amin_float_simd(Py_ssize_t arraylen, float *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	float minfound;

	float minvals[FLOATSIMDSIZE];
	v4sf minslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Initialise the comparison values.
	minslice = (v4sf) __builtin_ia32_loadups( &data[0]);

	// Use SIMD.
	for(x = FLOATSIMDSIZE; x < alignedlength; x += FLOATSIMDSIZE) {
		dataslice = (v4sf) __builtin_ia32_loadups( &data[x]);
		minslice = __builtin_ia32_minps (minslice, dataslice);
	}

	// Find the min within the slice.
	__builtin_ia32_storeups( minvals, (v4sf)  minslice);
	minfound = minvals[0];
	for (y = 1; y < FLOATSIMDSIZE; y++) {
		if (minvals[y] < minfound) {
			minfound = minvals[y];
		}
	}

	// Get the min value within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		if (data[x] < minfound) {
			minfound = data[x];
		}
	}

	return (double) minfound;
}
#endif
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: d
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The minimum value found.
*/
#if defined(AF_HASSIMD_X86)
double amin_double_simd(Py_ssize_t arraylen, double *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	double minfound;

	double minvals[DOUBLESIMDSIZE];
	v2df minslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Initialise the comparison values.
	minslice = (v2df) __builtin_ia32_loadupd( &data[0]);

	// Use SIMD.
	for(x = DOUBLESIMDSIZE; x < alignedlength; x += DOUBLESIMDSIZE) {
		dataslice = (v2df) __builtin_ia32_loadupd( &data[x]);
		minslice = __builtin_ia32_minpd (minslice, dataslice);
	}

	// Find the min within the slice.
	__builtin_ia32_storeupd( minvals, (v2df)  minslice);
	minfound = minvals[0];
	for (y = 1; y < DOUBLESIMDSIZE; y++) {
		if (minvals[y] < minfound) {
			minfound = minvals[y];
		}
	}

	// Get the min value within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		if (data[x] < minfound) {
			minfound = data[x];
		}
	}

	return (double) minfound;
}
#endif
/*--------------------------------------------------------------------------- */

