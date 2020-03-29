//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   aall_simd_armv8.c
// Purpose:  Calculate the aall of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     17-Mar-2020
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
   For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_eq_signed_char_simd(Py_ssize_t arraylen, signed char *data, signed char param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_s8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1q_s8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceqq_s8(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u8(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_gt_signed_char_simd(Py_ssize_t arraylen, signed char *data, signed char param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_s8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1q_s8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_s8(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u8(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_ge_signed_char_simd(Py_ssize_t arraylen, signed char *data, signed char param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_s8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1q_s8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcgeq_s8(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u8(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_lt_signed_char_simd(Py_ssize_t arraylen, signed char *data, signed char param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_s8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1q_s8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcltq_s8(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u8(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_le_signed_char_simd(Py_ssize_t arraylen, signed char *data, signed char param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_s8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1q_s8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcleq_s8(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u8(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_ne_signed_char_simd(Py_ssize_t arraylen, signed char *data, signed char param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_s8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1q_s8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceqq_s8(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u8(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0x0000000000000000) || (highresult != 0x0000000000000000)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_eq_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_u8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1q_u8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceqq_u8(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u8(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_gt_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_u8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1q_u8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_u8(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u8(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_ge_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_u8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1q_u8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcgeq_u8(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u8(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_lt_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_u8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1q_u8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcltq_u8(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u8(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_le_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_u8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1q_u8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcleq_u8(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u8(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_ne_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_u8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1q_u8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceqq_u8(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u8(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0x0000000000000000) || (highresult != 0x0000000000000000)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_eq_signed_short_simd(Py_ssize_t arraylen, signed short *data, signed short param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_s16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1q_s16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceqq_s16(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u16(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_gt_signed_short_simd(Py_ssize_t arraylen, signed short *data, signed short param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_s16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1q_s16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_s16(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u16(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_ge_signed_short_simd(Py_ssize_t arraylen, signed short *data, signed short param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_s16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1q_s16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcgeq_s16(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u16(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_lt_signed_short_simd(Py_ssize_t arraylen, signed short *data, signed short param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_s16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1q_s16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcltq_s16(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u16(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_le_signed_short_simd(Py_ssize_t arraylen, signed short *data, signed short param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_s16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1q_s16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcleq_s16(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u16(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_ne_signed_short_simd(Py_ssize_t arraylen, signed short *data, signed short param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_s16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1q_s16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceqq_s16(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u16(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0x0000000000000000) || (highresult != 0x0000000000000000)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_eq_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_u16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1q_u16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceqq_u16(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u16(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_gt_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_u16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1q_u16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_u16(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u16(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_ge_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_u16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1q_u16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcgeq_u16(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u16(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_lt_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_u16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1q_u16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcltq_u16(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u16(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_le_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_u16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1q_u16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcleq_u16(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u16(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_ne_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_u16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1q_u16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceqq_u16(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u16(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0x0000000000000000) || (highresult != 0x0000000000000000)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_eq_signed_int_simd(Py_ssize_t arraylen, signed int *data, signed int param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_s32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = vld1q_s32( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceqq_s32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_gt_signed_int_simd(Py_ssize_t arraylen, signed int *data, signed int param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_s32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = vld1q_s32( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_s32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_ge_signed_int_simd(Py_ssize_t arraylen, signed int *data, signed int param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_s32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = vld1q_s32( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcgeq_s32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_lt_signed_int_simd(Py_ssize_t arraylen, signed int *data, signed int param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_s32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = vld1q_s32( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcltq_s32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_le_signed_int_simd(Py_ssize_t arraylen, signed int *data, signed int param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_s32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = vld1q_s32( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcleq_s32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_ne_signed_int_simd(Py_ssize_t arraylen, signed int *data, signed int param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_s32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = vld1q_s32( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceqq_s32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0x0000000000000000) || (highresult != 0x0000000000000000)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_eq_unsigned_int_simd(Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_u32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = vld1q_u32( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceqq_u32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_gt_unsigned_int_simd(Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_u32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = vld1q_u32( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_u32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_ge_unsigned_int_simd(Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_u32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = vld1q_u32( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcgeq_u32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_lt_unsigned_int_simd(Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_u32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = vld1q_u32( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcltq_u32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_le_unsigned_int_simd(Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_u32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = vld1q_u32( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcleq_u32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_ne_unsigned_int_simd(Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_u32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = vld1q_u32( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceqq_u32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0x0000000000000000) || (highresult != 0x0000000000000000)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_eq_float_simd(Py_ssize_t arraylen, float *data, float param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_f32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
		datasliceleft = vld1q_f32( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceqq_f32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_gt_float_simd(Py_ssize_t arraylen, float *data, float param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_f32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
		datasliceleft = vld1q_f32( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcgtq_f32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_ge_float_simd(Py_ssize_t arraylen, float *data, float param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_f32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
		datasliceleft = vld1q_f32( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcgeq_f32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_lt_float_simd(Py_ssize_t arraylen, float *data, float param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_f32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
		datasliceleft = vld1q_f32( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcltq_f32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_le_float_simd(Py_ssize_t arraylen, float *data, float param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_f32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
		datasliceleft = vld1q_f32( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcleq_f32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0xffffffffffffffff) || (highresult != 0xffffffffffffffff)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv8 AARCH64 64 bit SIMD.
   For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, or ARR_ERR_NOTFOUND
		 if it was false at least once.
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
signed int aall_ne_float_simd(Py_ssize_t arraylen, float *data, float param1) { 

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
		compvals[y] = param1;
	}
	datasliceright = vld1q_f32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
		datasliceleft = vld1q_f32( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceqq_f32(datasliceleft, datasliceright);
		// Combine the result to two 64 bit vectors.
		veccombine = vreinterpretq_u64_u32(resultslice);
		// Get the high and low lanes of the combined vector.
		lowresult = vgetq_lane_u64(veccombine, 0);
		highresult = vgetq_lane_u64(veccombine, 1);
		// Compare the results of the SIMD operation.
		if ((lowresult != 0x0000000000000000) || (highresult != 0x0000000000000000)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return ARR_ERR_NOTFOUND;
		}
	}

	return 1;

}

#endif

