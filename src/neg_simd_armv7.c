//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   neg_simd_armv7.c
// Purpose:  Calculate the neg of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     08-Oct-2019
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
#ifdef AF_HASSIMD_ARMv7_32BIT
#include "arm_neon.h"
#endif

#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// Auto generated code goes below.

// Function specific macros and other definitions.
#include "neg_defs.h"

/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specifired value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
int8x8_t initvec_signed_char(signed char initval) {

	unsigned int y;
	signed char initvals[CHARSIMDSIZE];
	int8x8_t simdvec;

	for (y = 0; y < CHARSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = vld1_s8((initvals));

	return simdvec;
}
#endif



/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
*/
// param_arr_none
#if defined(AF_HASSIMD_ARMv7_32BIT)
void neg_signed_char_1_simd(Py_ssize_t arraylen, signed char *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x8_t datasliceleft;
	


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s8( &data[x]);
		// The actual SIMD operation. 
		datasliceleft = vneg_s8(datasliceleft);
		// Store the result.
		vst1_s8( &data[x],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data[x] = -data[x];
	}

}
#endif


// param_arr_arr
#if defined(AF_HASSIMD_ARMv7_32BIT)
void neg_signed_char_2_simd(Py_ssize_t arraylen, signed char *data, signed char *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x8_t datasliceleft;
	


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s8( &data[x]);
		// The actual SIMD operation. 
		datasliceleft = vneg_s8(datasliceleft);
		// Store the result.
		vst1_s8( &dataout[x],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		dataout[x] = -data[x];
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
#if defined(AF_HASSIMD_ARMv7_32BIT)
char neg_signed_char_1_simd_ovfl(Py_ssize_t arraylen, signed char *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x8_t datasliceleft, ovflvec;
	uint8x8_t ovcheck;
	
	


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_signed_char(SCHAR_MIN);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s8( &data[x]);

		// Check for overflow. 
		// Do an equal compare operation.
			ovcheck = vceq_s8 (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(vreinterpret_u64_u8(ovcheck) == 0x0000000000000000)){
			return 1;
		}

		// The actual SIMD operation. 
		datasliceleft = vneg_s8(datasliceleft);

		// Store the result.
		vst1_s8( &data[x],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( minval_loop_willoverflow_signed_char(data[x]) ) {return ARR_ERR_OVFL;}
		data[x] = -data[x];
	}

	return 0;

}


// param_arr_arr
char neg_signed_char_2_simd_ovfl(Py_ssize_t arraylen, signed char *data, signed char *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x8_t datasliceleft, ovflvec;
	uint8x8_t ovcheck;
	
	


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_signed_char(SCHAR_MIN);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s8( &data[x]);

		// Check for overflow. 
		// Do an equal compare operation.
			ovcheck = vceq_s8 (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(vreinterpret_u64_u8(ovcheck) == 0x0000000000000000)){
			return 1;
		}

		// The actual SIMD operation. 
		datasliceleft = vneg_s8(datasliceleft);

		// Store the result.
		vst1_s8( &dataout[x],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( minval_loop_willoverflow_signed_char(data[x]) ) {return ARR_ERR_OVFL;}
		dataout[x] = -data[x];
	}

	return 0;

}
#endif


/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specifired value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
int16x4_t initvec_signed_short(signed short initval) {

	unsigned int y;
	signed short initvals[SHORTSIMDSIZE];
	int16x4_t simdvec;

	for (y = 0; y < SHORTSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = vld1_s16((initvals));

	return simdvec;
}
#endif



/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
*/
// param_arr_none
#if defined(AF_HASSIMD_ARMv7_32BIT)
void neg_signed_short_1_simd(Py_ssize_t arraylen, signed short *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x4_t datasliceleft;
	


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s16( &data[x]);
		// The actual SIMD operation. 
		datasliceleft = vneg_s16(datasliceleft);
		// Store the result.
		vst1_s16( &data[x],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data[x] = -data[x];
	}

}
#endif


// param_arr_arr
#if defined(AF_HASSIMD_ARMv7_32BIT)
void neg_signed_short_2_simd(Py_ssize_t arraylen, signed short *data, signed short *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x4_t datasliceleft;
	


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s16( &data[x]);
		// The actual SIMD operation. 
		datasliceleft = vneg_s16(datasliceleft);
		// Store the result.
		vst1_s16( &dataout[x],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		dataout[x] = -data[x];
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
#if defined(AF_HASSIMD_ARMv7_32BIT)
char neg_signed_short_1_simd_ovfl(Py_ssize_t arraylen, signed short *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x4_t datasliceleft, ovflvec;
	uint16x4_t ovcheck;
	
	


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_signed_short(SHRT_MIN);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s16( &data[x]);

		// Check for overflow. 
		// Do an equal compare operation.
			ovcheck = vceq_s16 (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(vreinterpret_u64_u16(ovcheck) == 0x0000000000000000)){
			return 1;
		}

		// The actual SIMD operation. 
		datasliceleft = vneg_s16(datasliceleft);

		// Store the result.
		vst1_s16( &data[x],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( minval_loop_willoverflow_signed_short(data[x]) ) {return ARR_ERR_OVFL;}
		data[x] = -data[x];
	}

	return 0;

}


// param_arr_arr
char neg_signed_short_2_simd_ovfl(Py_ssize_t arraylen, signed short *data, signed short *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x4_t datasliceleft, ovflvec;
	uint16x4_t ovcheck;
	
	


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_signed_short(SHRT_MIN);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s16( &data[x]);

		// Check for overflow. 
		// Do an equal compare operation.
			ovcheck = vceq_s16 (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(vreinterpret_u64_u16(ovcheck) == 0x0000000000000000)){
			return 1;
		}

		// The actual SIMD operation. 
		datasliceleft = vneg_s16(datasliceleft);

		// Store the result.
		vst1_s16( &dataout[x],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( minval_loop_willoverflow_signed_short(data[x]) ) {return ARR_ERR_OVFL;}
		dataout[x] = -data[x];
	}

	return 0;

}
#endif


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
*/
// param_arr_none
#if defined(AF_HASSIMD_ARMv7_32BIT)
void neg_float_1_simd(Py_ssize_t arraylen, float *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x2_t datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_f32( &data[x]);
		// The actual SIMD operation. 
		datasliceleft = vneg_f32(datasliceleft);
		// Store the result.
		vst1_f32( &data[x], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data[x] = -data[x];
	}

}



// param_arr_arr
void neg_float_2_simd(Py_ssize_t arraylen, float *data, float *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x2_t datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_f32( &data[x]);
		// The actual SIMD operation. 
		datasliceleft = vneg_f32(datasliceleft);
		// Store the result.
		vst1_f32( &dataout[x], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		dataout[x] = -data[x];
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
#if defined(AF_HASSIMD_ARMv7_32BIT)
char neg_float_1_simd_ovfl(Py_ssize_t arraylen, float *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x2_t datasliceleft, checkslice;

	float checkvecresults[FLOATSIMDSIZE];
	float checksliceinit[FLOATSIMDSIZE] = {0.0};


	// This is used to check for errors by accumulating non-finite values.
	checkslice = vld1_f32( checksliceinit);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_f32( &data[x]);
		// The actual SIMD operation. 
		datasliceleft = vneg_f32(datasliceleft);
		// Store the result.
		vst1_f32( &data[x], datasliceleft);

		// Check the result. None-finite errors should accumulate.
		checkslice = vmul_f32(checkslice, datasliceleft);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	vst1_f32( checkvecresults, checkslice);
	for (x = 0; x < FLOATSIMDSIZE; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data[x] = -data[x];
		if (!isfinite(data[x])) {return 1;}
	}

	// Everything was OK.
	return 0;

}



// param_arr_arr
char neg_float_2_simd_ovfl(Py_ssize_t arraylen, float *data, float *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x2_t datasliceleft, checkslice;

	float checkvecresults[FLOATSIMDSIZE];
	float checksliceinit[FLOATSIMDSIZE] = {0.0};


	// This is used to check for errors by accumulating non-finite values.
	checkslice = vld1_f32( checksliceinit);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_f32( &data[x]);
		// The actual SIMD operation. 
		datasliceleft = vneg_f32(datasliceleft);
		// Store the result.
		vst1_f32( &dataout[x], datasliceleft);

		// Check the result. None-finite errors should accumulate.
		checkslice = vmul_f32(checkslice, datasliceleft);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	vst1_f32( checkvecresults, checkslice);
	for (x = 0; x < FLOATSIMDSIZE; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		dataout[x] = -data[x];
		if (!isfinite(dataout[x])) {return 1;}
	}

	// Everything was OK.
	return 0;

}
#endif

