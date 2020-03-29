//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   radians_simd_x86.c
// Purpose:  Calculate the radians of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     24-Mar-2019
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

// This _USE_MATH_DEFINES is required for MSVC 2010 compatibility to enable
// the M_PI constant. This must be immediately above <math.h>.
#define _USE_MATH_DEFINES
#include <math.h>


/*--------------------------------------------------------------------------- */

// Used to calculate degrees to radians.
#define DEGTORAD_D M_PI / 180.0
#define DEGTORAD_F (float) (M_PI / 180.0)

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

#ifdef AF_HASSIMD_X86
// Used to calculate degrees to radians for x86-64.
const v2df DEGTORAD_D_VEC = {DEGTORAD_D, DEGTORAD_D};
const v4sf DEGTORAD_F_VEC = {DEGTORAD_F, DEGTORAD_F, DEGTORAD_F, DEGTORAD_F};
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
*/
// param_arr_none
#if defined(AF_HASSIMD_X86)
void radians_float_1_simd(Py_ssize_t arraylen, float *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4sf datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = __builtin_ia32_loadups(&data[x]);
		// The actual SIMD operation. 
		datasliceleft = __builtin_ia32_mulps (datasliceleft, DEGTORAD_F_VEC);
		// Store the result.
		__builtin_ia32_storeups(&data[x], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data[x] = DEGTORAD_F * data[x];
	}

}



// param_arr_arr
void radians_float_2_simd(Py_ssize_t arraylen, float *data, float *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4sf datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = __builtin_ia32_loadups(&data[x]);
		// The actual SIMD operation. 
		datasliceleft = __builtin_ia32_mulps (datasliceleft, DEGTORAD_F_VEC);
		// Store the result.
		__builtin_ia32_storeups(&dataout[x], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		dataout[x] = DEGTORAD_F * data[x];
	}

}
#endif


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
*/
// param_arr_none
#if defined(AF_HASSIMD_X86)
void radians_double_1_simd(Py_ssize_t arraylen, double *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = __builtin_ia32_loadupd(&data[x]);
		// The actual SIMD operation. 
		datasliceleft = __builtin_ia32_mulpd (datasliceleft, DEGTORAD_D_VEC);
		// Store the result.
		__builtin_ia32_storeupd(&data[x], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data[x] = DEGTORAD_D * data[x];
	}

}



// param_arr_arr
void radians_double_2_simd(Py_ssize_t arraylen, double *data, double *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = __builtin_ia32_loadupd(&data[x]);
		// The actual SIMD operation. 
		datasliceleft = __builtin_ia32_mulpd (datasliceleft, DEGTORAD_D_VEC);
		// Store the result.
		__builtin_ia32_storeupd(&dataout[x], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		dataout[x] = DEGTORAD_D * data[x];
	}

}
#endif

