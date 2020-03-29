//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   radians_simd_armv7.c
// Purpose:  Calculate the radians of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     02-Oct-2019
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

#ifdef AF_HASSIMD_ARMv7_32BIT
// Used to calculate degrees to radians for ARM NEON for 32 bit ARMv7.
const float32x2_t DEGTORAD_F_VEC = {DEGTORAD_F, DEGTORAD_F};
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
*/
// param_arr_none
#if defined(AF_HASSIMD_ARMv7_32BIT)
void radians_float_1_simd(Py_ssize_t arraylen, float *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x2_t datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_f32(&data[x]);
		// The actual SIMD operation. 
		datasliceleft = vmul_f32 (datasliceleft, DEGTORAD_F_VEC);
		// Store the result.
		vst1_f32(&data[x], datasliceleft);
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

	float32x2_t datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_f32(&data[x]);
		// The actual SIMD operation. 
		datasliceleft = vmul_f32 (datasliceleft, DEGTORAD_F_VEC);
		// Store the result.
		vst1_f32(&dataout[x], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		dataout[x] = DEGTORAD_F * data[x];
	}

}
#endif

