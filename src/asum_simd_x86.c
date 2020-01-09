//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   asum_simd_x86.c
// Purpose:  Calculate the asum of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     05-May-2017
// Ver:      02-Jan-2020.
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
/* For array code: f
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   nosimd = If true, disable SIMD.
   Returns: The sum of the array.
*/
#ifdef AF_HASSIMD_X86
double asum_float_simd(Py_ssize_t arraylen, float *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	float partialsum = 0.0;

	float sumvals[FLOATSIMDSIZE];
	v4sf sumslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Initialise the sum values.
	sumslice = (v4sf) __builtin_ia32_loadups(data);

	// Use SIMD.
	for (x = FLOATSIMDSIZE; x < alignedlength; x += FLOATSIMDSIZE) {
		dataslice = (v4sf) __builtin_ia32_loadups(&data[x]);
		sumslice = __builtin_ia32_addps(sumslice, dataslice);
	}

	// Add up the values within the slice.
	__builtin_ia32_storeups(sumvals, (v4sf) sumslice);
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		partialsum = partialsum + sumvals[y];
	}

	// Add the values within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}


	return (double) partialsum;
}
#endif
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
#ifdef AF_HASSIMD_X86
double asum_double_simd(Py_ssize_t arraylen, double *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	double partialsum = 0.0;

	double sumvals[DOUBLESIMDSIZE];
	v2df sumslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Initialise the sum values.
	sumslice = (v2df) __builtin_ia32_loadupd(data);

	// Use SIMD.
	for (x = DOUBLESIMDSIZE; x < alignedlength; x += DOUBLESIMDSIZE) {
		dataslice = (v2df) __builtin_ia32_loadupd(&data[x]);
		sumslice = __builtin_ia32_addpd(sumslice, dataslice);
	}

	// Add up the values within the slice.
	__builtin_ia32_storeupd(sumvals, (v2df) sumslice);
	for (y = 0; y < DOUBLESIMDSIZE; y++) {
		partialsum = partialsum + sumvals[y];
	}

	// Add the values within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}


	return partialsum;
}
#endif
/*--------------------------------------------------------------------------- */
