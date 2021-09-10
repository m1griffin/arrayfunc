//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   neg_simd_armv8.c
// Purpose:  Calculate the neg of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     25-Mar-2020
// Ver:      06-Sep-2021.
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

// Function specific macros and other definitions.
#include "neg_defs.h"

/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specifired value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
int8x16_t initvec_signed_char(signed char initval) {

	unsigned int y;
	signed char initvals[CHARSIMDSIZE];
	int8x16_t simdvec;

	for (y = 0; y < CHARSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = vld1q_s8((initvals));

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
#if defined(AF_HASSIMD_ARM_AARCH64)
void neg_signed_char_1_simd(Py_ssize_t arraylen, signed char *data) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft;
	


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s8( &data[index]);
		// The actual SIMD operation. 
		datasliceleft = vnegq_s8(datasliceleft);
		// Store the result.
		vst1q_s8( &data[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data[index] = -data[index];
	}

}
#endif


// param_arr_arr
#if defined(AF_HASSIMD_ARM_AARCH64)
void neg_signed_char_2_simd(Py_ssize_t arraylen, signed char *data, signed char *dataout) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft;
	


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s8( &data[index]);
		// The actual SIMD operation. 
		datasliceleft = vnegq_s8(datasliceleft);
		// Store the result.
		vst1q_s8( &dataout[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		dataout[index] = -data[index];
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
#if defined(AF_HASSIMD_ARM_AARCH64)
char neg_signed_char_1_simd_ovfl(Py_ssize_t arraylen, signed char *data) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft, ovflvec;
	uint8x16_t ovcheck;
	
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_signed_char(SCHAR_MIN);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s8( &data[index]);

		// Check for overflow. 
		// Do an equal compare operation.
			ovcheck = vceqq_s8 (datasliceleft, ovflvec);

			// Check for overflow. 
			// Combine the result to two 64 bit vectors.
			veccombine = vreinterpretq_u64_u8(ovcheck);
			// Get the high and low lanes of the combined vector.
			lowresult = vgetq_lane_u64(veccombine, 0);
			highresult = vgetq_lane_u64(veccombine, 1);
			// Check if overflow will happen.
			if ((lowresult != 0x0000000000000000) || (highresult != 0x0000000000000000)) {
			return 1;
		}

		// The actual SIMD operation. 
		datasliceleft = vnegq_s8(datasliceleft);

		// Store the result.
		vst1q_s8( &data[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if ( minval_loop_willoverflow_signed_char(data[index]) ) {return ARR_ERR_OVFL;}
		data[index] = -data[index];
	}

	return 0;

}


// param_arr_arr
char neg_signed_char_2_simd_ovfl(Py_ssize_t arraylen, signed char *data, signed char *dataout) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft, ovflvec;
	uint8x16_t ovcheck;
	
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_signed_char(SCHAR_MIN);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s8( &data[index]);

		// Check for overflow. 
		// Do an equal compare operation.
			ovcheck = vceqq_s8 (datasliceleft, ovflvec);

			// Check for overflow. 
			// Combine the result to two 64 bit vectors.
			veccombine = vreinterpretq_u64_u8(ovcheck);
			// Get the high and low lanes of the combined vector.
			lowresult = vgetq_lane_u64(veccombine, 0);
			highresult = vgetq_lane_u64(veccombine, 1);
			// Check if overflow will happen.
			if ((lowresult != 0x0000000000000000) || (highresult != 0x0000000000000000)) {
			return 1;
		}

		// The actual SIMD operation. 
		datasliceleft = vnegq_s8(datasliceleft);

		// Store the result.
		vst1q_s8( &dataout[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if ( minval_loop_willoverflow_signed_char(data[index]) ) {return ARR_ERR_OVFL;}
		dataout[index] = -data[index];
	}

	return 0;

}
#endif


/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specifired value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
int16x8_t initvec_signed_short(signed short initval) {

	unsigned int y;
	signed short initvals[SHORTSIMDSIZE];
	int16x8_t simdvec;

	for (y = 0; y < SHORTSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = vld1q_s16((initvals));

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
#if defined(AF_HASSIMD_ARM_AARCH64)
void neg_signed_short_1_simd(Py_ssize_t arraylen, signed short *data) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft;
	


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s16( &data[index]);
		// The actual SIMD operation. 
		datasliceleft = vnegq_s16(datasliceleft);
		// Store the result.
		vst1q_s16( &data[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data[index] = -data[index];
	}

}
#endif


// param_arr_arr
#if defined(AF_HASSIMD_ARM_AARCH64)
void neg_signed_short_2_simd(Py_ssize_t arraylen, signed short *data, signed short *dataout) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft;
	


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s16( &data[index]);
		// The actual SIMD operation. 
		datasliceleft = vnegq_s16(datasliceleft);
		// Store the result.
		vst1q_s16( &dataout[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		dataout[index] = -data[index];
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
#if defined(AF_HASSIMD_ARM_AARCH64)
char neg_signed_short_1_simd_ovfl(Py_ssize_t arraylen, signed short *data) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft, ovflvec;
	uint16x8_t ovcheck;
	
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_signed_short(SHRT_MIN);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s16( &data[index]);

		// Check for overflow. 
		// Do an equal compare operation.
			ovcheck = vceqq_s16 (datasliceleft, ovflvec);

			// Check for overflow. 
			// Combine the result to two 64 bit vectors.
			veccombine = vreinterpretq_u64_u16(ovcheck);
			// Get the high and low lanes of the combined vector.
			lowresult = vgetq_lane_u64(veccombine, 0);
			highresult = vgetq_lane_u64(veccombine, 1);
			// Check if overflow will happen.
			if ((lowresult != 0x0000000000000000) || (highresult != 0x0000000000000000)) {
			return 1;
		}

		// The actual SIMD operation. 
		datasliceleft = vnegq_s16(datasliceleft);

		// Store the result.
		vst1q_s16( &data[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if ( minval_loop_willoverflow_signed_short(data[index]) ) {return ARR_ERR_OVFL;}
		data[index] = -data[index];
	}

	return 0;

}


// param_arr_arr
char neg_signed_short_2_simd_ovfl(Py_ssize_t arraylen, signed short *data, signed short *dataout) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft, ovflvec;
	uint16x8_t ovcheck;
	
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_signed_short(SHRT_MIN);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s16( &data[index]);

		// Check for overflow. 
		// Do an equal compare operation.
			ovcheck = vceqq_s16 (datasliceleft, ovflvec);

			// Check for overflow. 
			// Combine the result to two 64 bit vectors.
			veccombine = vreinterpretq_u64_u16(ovcheck);
			// Get the high and low lanes of the combined vector.
			lowresult = vgetq_lane_u64(veccombine, 0);
			highresult = vgetq_lane_u64(veccombine, 1);
			// Check if overflow will happen.
			if ((lowresult != 0x0000000000000000) || (highresult != 0x0000000000000000)) {
			return 1;
		}

		// The actual SIMD operation. 
		datasliceleft = vnegq_s16(datasliceleft);

		// Store the result.
		vst1q_s16( &dataout[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if ( minval_loop_willoverflow_signed_short(data[index]) ) {return ARR_ERR_OVFL;}
		dataout[index] = -data[index];
	}

	return 0;

}
#endif


/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specifired value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
int32x4_t initvec_signed_int(signed int initval) {

	unsigned int y;
	signed int initvals[INTSIMDSIZE];
	int32x4_t simdvec;

	for (y = 0; y < INTSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = vld1q_s32((initvals));

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
#if defined(AF_HASSIMD_ARM_AARCH64)
void neg_signed_int_1_simd(Py_ssize_t arraylen, signed int *data) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft;
	


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s32( &data[index]);
		// The actual SIMD operation. 
		datasliceleft = vnegq_s32(datasliceleft);
		// Store the result.
		vst1q_s32( &data[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data[index] = -data[index];
	}

}
#endif


// param_arr_arr
#if defined(AF_HASSIMD_ARM_AARCH64)
void neg_signed_int_2_simd(Py_ssize_t arraylen, signed int *data, signed int *dataout) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft;
	


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s32( &data[index]);
		// The actual SIMD operation. 
		datasliceleft = vnegq_s32(datasliceleft);
		// Store the result.
		vst1q_s32( &dataout[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		dataout[index] = -data[index];
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
#if defined(AF_HASSIMD_ARM_AARCH64)
char neg_signed_int_1_simd_ovfl(Py_ssize_t arraylen, signed int *data) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft, ovflvec;
	uint32x4_t ovcheck;
	
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_signed_int(INT_MIN);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s32( &data[index]);

		// Check for overflow. 
		// Do an equal compare operation.
			ovcheck = vceqq_s32 (datasliceleft, ovflvec);

			// Check for overflow. 
			// Combine the result to two 64 bit vectors.
			veccombine = vreinterpretq_u64_u32(ovcheck);
			// Get the high and low lanes of the combined vector.
			lowresult = vgetq_lane_u64(veccombine, 0);
			highresult = vgetq_lane_u64(veccombine, 1);
			// Check if overflow will happen.
			if ((lowresult != 0x0000000000000000) || (highresult != 0x0000000000000000)) {
			return 1;
		}

		// The actual SIMD operation. 
		datasliceleft = vnegq_s32(datasliceleft);

		// Store the result.
		vst1q_s32( &data[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if ( minval_loop_willoverflow_signed_int(data[index]) ) {return ARR_ERR_OVFL;}
		data[index] = -data[index];
	}

	return 0;

}


// param_arr_arr
char neg_signed_int_2_simd_ovfl(Py_ssize_t arraylen, signed int *data, signed int *dataout) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft, ovflvec;
	uint32x4_t ovcheck;
	
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_signed_int(INT_MIN);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s32( &data[index]);

		// Check for overflow. 
		// Do an equal compare operation.
			ovcheck = vceqq_s32 (datasliceleft, ovflvec);

			// Check for overflow. 
			// Combine the result to two 64 bit vectors.
			veccombine = vreinterpretq_u64_u32(ovcheck);
			// Get the high and low lanes of the combined vector.
			lowresult = vgetq_lane_u64(veccombine, 0);
			highresult = vgetq_lane_u64(veccombine, 1);
			// Check if overflow will happen.
			if ((lowresult != 0x0000000000000000) || (highresult != 0x0000000000000000)) {
			return 1;
		}

		// The actual SIMD operation. 
		datasliceleft = vnegq_s32(datasliceleft);

		// Store the result.
		vst1q_s32( &dataout[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if ( minval_loop_willoverflow_signed_int(data[index]) ) {return ARR_ERR_OVFL;}
		dataout[index] = -data[index];
	}

	return 0;

}
#endif

