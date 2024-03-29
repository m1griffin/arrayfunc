//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   degrees_simd_armv8.c
// Purpose:  Calculate the degrees of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     26-Mar-2020
// Ver:      31-Oct-2021.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2021    Michael Griffin    <m12.griffin@gmail.com>
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
#ifdef AF_HASSIMD_ARM_AARCH64
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

// Used to calculate radians to degrees.
#define RADTODEG_D 180.0 / M_PI
#define RADTODEG_F (float) (180.0 / M_PI)

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

#ifdef AF_HASSIMD_ARM_AARCH64
// Used to calculate radians to degrees in vector format ARM NEON for 64 bit ARMv8.
const float32x4_t RADTODEG_F_VEC = {RADTODEG_F, RADTODEG_F, RADTODEG_F, RADTODEG_F};
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
*/
// param_arr_none
#if defined(AF_HASSIMD_ARM_AARCH64)
void degrees_float_1_simd(Py_ssize_t arraylen, float *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x4_t datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_f32(&data[x]);
		// The actual SIMD operation. 
		datasliceleft = vmulq_f32 (datasliceleft, RADTODEG_F_VEC);
		// Store the result.
		vst1q_f32(&data[x], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data[x] = RADTODEG_F * data[x];
	}

}



// param_arr_arr
void degrees_float_2_simd(Py_ssize_t arraylen, float *data, float *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x4_t datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_f32(&data[x]);
		// The actual SIMD operation. 
		datasliceleft = vmulq_f32 (datasliceleft, RADTODEG_F_VEC);
		// Store the result.
		vst1q_f32(&dataout[x], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		dataout[x] = RADTODEG_F * data[x];
	}

}
#endif


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   Returns 1 if overflow occurred, else returns 0.
*/
// param_arr_none
#if defined(AF_HASSIMD_ARM_AARCH64)
char degrees_float_1_simd_ovfl(Py_ssize_t arraylen, float *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x4_t datasliceleft, checkslice;

	float checkvecresults[FLOATSIMDSIZE];
	float checksliceinit[FLOATSIMDSIZE] = {0.0};


	// This is used to check for errors by accumulating non-finite values.
	checkslice = vld1q_f32 (checksliceinit);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_f32(&data[x]);
		// The actual SIMD operation. 
		datasliceleft = vmulq_f32 (datasliceleft, RADTODEG_F_VEC);
		// Store the result.
		vst1q_f32(&data[x], datasliceleft);

		// Check the result. None-finite errors should accumulate.
		checkslice = vmulq_f32(checkslice, datasliceleft);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	vst1q_f32 (checkvecresults, checkslice);
	for (x = 0; x < FLOATSIMDSIZE; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data[x] = RADTODEG_F * data[x];
		if (!isfinite(data[x])) {return 1;}
	}

	// Everything was OK.
	return 0;

}



// param_arr_arr
char degrees_float_2_simd_ovfl(Py_ssize_t arraylen, float *data, float *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x4_t datasliceleft, checkslice;

	float checkvecresults[FLOATSIMDSIZE];
	float checksliceinit[FLOATSIMDSIZE] = {0.0};


	// This is used to check for errors by accumulating non-finite values.
	checkslice = vld1q_f32 (checksliceinit);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_f32(&data[x]);
		// The actual SIMD operation. 
		datasliceleft = vmulq_f32 (datasliceleft, RADTODEG_F_VEC);
		// Store the result.
		vst1q_f32(&dataout[x], datasliceleft);

		// Check the result. None-finite errors should accumulate.
		checkslice = vmulq_f32(checkslice, datasliceleft);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	vst1q_f32 (checkvecresults, checkslice);
	for (x = 0; x < FLOATSIMDSIZE; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		dataout[x] = RADTODEG_F * data[x];
		if (!isfinite(dataout[x])) {return 1;}
	}

	// Everything was OK.
	return 0;

}
#endif

