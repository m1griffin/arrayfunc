//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   gt_simd_armv8.c
// Purpose:  Calculate the gt of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     22-Mar-2020
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
#ifdef AF_HASSIMD_ARM_AARCH64
#include "arm_neon.h"
#endif

#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// Auto generated code goes below.


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#if defined(AF_HASSIMD_ARM_AARCH64)
char gt_signed_char_1_simd(Py_ssize_t arraylen, signed char *data1, signed char param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int8x16_t datasliceleft, datasliceright;
	uint8x16_t resultslice;
	signed char compvals[CHARSIMDSIZE];
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1q_s8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1q_s8( &data1[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_s8(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u8(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] > param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char gt_signed_char_3_simd(Py_ssize_t arraylen, signed char param, signed char *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int8x16_t datasliceleft, datasliceright;
	uint8x16_t resultslice;
	signed char compvals[CHARSIMDSIZE];
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1q_s8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceright = vld1q_s8( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_s8(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u8(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(param > data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char gt_signed_char_5_simd(Py_ssize_t arraylen, signed char *data1, signed char *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft, datasliceright;
	uint8x16_t resultslice;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1q_s8( &data1[index]);
		datasliceright = vld1q_s8( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_s8(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u8(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] > data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */



/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#if defined(AF_HASSIMD_ARM_AARCH64)
char gt_unsigned_char_1_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint8x16_t datasliceleft, datasliceright;
	uint8x16_t resultslice;
	unsigned char compvals[CHARSIMDSIZE];
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1q_u8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1q_u8( &data1[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_u8(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u8(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] > param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char gt_unsigned_char_3_simd(Py_ssize_t arraylen, unsigned char param, unsigned char *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint8x16_t datasliceleft, datasliceright;
	uint8x16_t resultslice;
	unsigned char compvals[CHARSIMDSIZE];
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1q_u8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceright = vld1q_u8( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_u8(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u8(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(param > data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char gt_unsigned_char_5_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x16_t datasliceleft, datasliceright;
	uint8x16_t resultslice;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1q_u8( &data1[index]);
		datasliceright = vld1q_u8( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_u8(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u8(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] > data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */



/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#if defined(AF_HASSIMD_ARM_AARCH64)
char gt_signed_short_1_simd(Py_ssize_t arraylen, signed short *data1, signed short param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int16x8_t datasliceleft, datasliceright;
	uint16x8_t resultslice;
	signed short compvals[SHORTSIMDSIZE];
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1q_s16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1q_s16( &data1[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_s16(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u16(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] > param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char gt_signed_short_3_simd(Py_ssize_t arraylen, signed short param, signed short *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int16x8_t datasliceleft, datasliceright;
	uint16x8_t resultslice;
	signed short compvals[SHORTSIMDSIZE];
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1q_s16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceright = vld1q_s16( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_s16(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u16(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(param > data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char gt_signed_short_5_simd(Py_ssize_t arraylen, signed short *data1, signed short *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft, datasliceright;
	uint16x8_t resultslice;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1q_s16( &data1[index]);
		datasliceright = vld1q_s16( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_s16(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u16(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] > data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */



/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#if defined(AF_HASSIMD_ARM_AARCH64)
char gt_unsigned_short_1_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint16x8_t datasliceleft, datasliceright;
	uint16x8_t resultslice;
	unsigned short compvals[SHORTSIMDSIZE];
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1q_u16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1q_u16( &data1[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_u16(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u16(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] > param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char gt_unsigned_short_3_simd(Py_ssize_t arraylen, unsigned short param, unsigned short *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint16x8_t datasliceleft, datasliceright;
	uint16x8_t resultslice;
	unsigned short compvals[SHORTSIMDSIZE];
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1q_u16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceright = vld1q_u16( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_u16(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u16(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(param > data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char gt_unsigned_short_5_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x8_t datasliceleft, datasliceright;
	uint16x8_t resultslice;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1q_u16( &data1[index]);
		datasliceright = vld1q_u16( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_u16(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u16(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] > data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */



/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#if defined(AF_HASSIMD_ARM_AARCH64)
char gt_signed_int_1_simd(Py_ssize_t arraylen, signed int *data1, signed int param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int32x4_t datasliceleft, datasliceright;
	uint32x4_t resultslice;
	signed int compvals[INTSIMDSIZE];
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1q_s32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = vld1q_s32( &data1[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_s32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] > param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char gt_signed_int_3_simd(Py_ssize_t arraylen, signed int param, signed int *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int32x4_t datasliceleft, datasliceright;
	uint32x4_t resultslice;
	signed int compvals[INTSIMDSIZE];
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1q_s32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceright = vld1q_s32( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_s32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(param > data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char gt_signed_int_5_simd(Py_ssize_t arraylen, signed int *data1, signed int *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft, datasliceright;
	uint32x4_t resultslice;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = vld1q_s32( &data1[index]);
		datasliceright = vld1q_s32( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_s32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] > data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */



/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#if defined(AF_HASSIMD_ARM_AARCH64)
char gt_unsigned_int_1_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint32x4_t datasliceleft, datasliceright;
	uint32x4_t resultslice;
	unsigned int compvals[INTSIMDSIZE];
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1q_u32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = vld1q_u32( &data1[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_u32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] > param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char gt_unsigned_int_3_simd(Py_ssize_t arraylen, unsigned int param, unsigned int *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint32x4_t datasliceleft, datasliceright;
	uint32x4_t resultslice;
	unsigned int compvals[INTSIMDSIZE];
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1q_u32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceright = vld1q_u32( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_u32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(param > data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char gt_unsigned_int_5_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x4_t datasliceleft, datasliceright;
	uint32x4_t resultslice;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = vld1q_u32( &data1[index]);
		datasliceright = vld1q_u32( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_u32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] > data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */



/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#if defined(AF_HASSIMD_ARM_AARCH64)
char gt_float_1_simd(Py_ssize_t arraylen, float *data1, float param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	float32x4_t datasliceleft, datasliceright;
	uint32x4_t resultslice;
	float compvals[FLOATSIMDSIZE];
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;

	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1q_f32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
		datasliceleft = vld1q_f32( &data1[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_f32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] > param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char gt_float_3_simd(Py_ssize_t arraylen, float param, float *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	float32x4_t datasliceleft, datasliceright;
	uint32x4_t resultslice;
	float compvals[FLOATSIMDSIZE];
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;

	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1q_f32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
		datasliceright = vld1q_f32( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_f32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(param > data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char gt_float_5_simd(Py_ssize_t arraylen, float *data1, float *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x4_t datasliceleft, datasliceright;
	uint32x4_t resultslice;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
		datasliceleft = vld1q_f32( &data1[index]);
		datasliceright = vld1q_f32( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_f32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] > data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */

