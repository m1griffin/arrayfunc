//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   mul_simd_armv8.c
// Purpose:  Calculate the mul of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     26-Mar-2020
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
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
void mul_signed_char_1_simd(Py_ssize_t arraylen, signed char *data1, signed char param) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft, datasliceright, resultslice;
	signed char opvals[CHARSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = vld1q_s8( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s8( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s8( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * param;
	}

}



// param_arr_num_arr
void mul_signed_char_2_simd(Py_ssize_t arraylen, signed char *data1, signed char param, signed char *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft, datasliceright, resultslice;
	signed char opvals[CHARSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = vld1q_s8( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s8( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s8( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * param;
	}

}



// param_num_arr_none
void mul_signed_char_3_simd(Py_ssize_t arraylen, signed char param, signed char *data2) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft, datasliceright, resultslice;
	signed char opvals[CHARSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = vld1q_s8( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_s8( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s8( &data2[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param * data2[x];
	}

}



// param_num_arr_arr
void mul_signed_char_4_simd(Py_ssize_t arraylen, signed char param, signed char *data2, signed char *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft, datasliceright, resultslice;
	signed char opvals[CHARSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = vld1q_s8( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_s8( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s8( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param * data2[x];
	}

}



// param_arr_arr_none
void mul_signed_char_5_simd(Py_ssize_t arraylen, signed char *data1, signed char *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s8( &data1[x]);
		datasliceright = vld1q_s8( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s8( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * data2[x];
	}

}



// param_arr_arr_arr
void mul_signed_char_6_simd(Py_ssize_t arraylen, signed char *data1, signed char *data2, signed char *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s8( &data1[x]);
		datasliceright = vld1q_s8( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s8( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * data2[x];
	}

}
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
void mul_unsigned_char_1_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x16_t datasliceleft, datasliceright, resultslice;
	unsigned char opvals[CHARSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = vld1q_u8( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u8( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * param;
	}

}



// param_arr_num_arr
void mul_unsigned_char_2_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param, unsigned char *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x16_t datasliceleft, datasliceright, resultslice;
	unsigned char opvals[CHARSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = vld1q_u8( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u8( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * param;
	}

}



// param_num_arr_none
void mul_unsigned_char_3_simd(Py_ssize_t arraylen, unsigned char param, unsigned char *data2) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x16_t datasliceleft, datasliceright, resultslice;
	unsigned char opvals[CHARSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = vld1q_u8( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_u8( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8( &data2[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param * data2[x];
	}

}



// param_num_arr_arr
void mul_unsigned_char_4_simd(Py_ssize_t arraylen, unsigned char param, unsigned char *data2, unsigned char *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x16_t datasliceleft, datasliceright, resultslice;
	unsigned char opvals[CHARSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = vld1q_u8( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_u8( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param * data2[x];
	}

}



// param_arr_arr_none
void mul_unsigned_char_5_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x16_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u8( &data1[x]);
		datasliceright = vld1q_u8( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * data2[x];
	}

}



// param_arr_arr_arr
void mul_unsigned_char_6_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2, unsigned char *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x16_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u8( &data1[x]);
		datasliceright = vld1q_u8( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * data2[x];
	}

}
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
void mul_signed_short_1_simd(Py_ssize_t arraylen, signed short *data1, signed short param) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft, datasliceright, resultslice;
	signed short opvals[SHORTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = vld1q_s16( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s16( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s16( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * param;
	}

}



// param_arr_num_arr
void mul_signed_short_2_simd(Py_ssize_t arraylen, signed short *data1, signed short param, signed short *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft, datasliceright, resultslice;
	signed short opvals[SHORTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = vld1q_s16( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s16( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s16( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * param;
	}

}



// param_num_arr_none
void mul_signed_short_3_simd(Py_ssize_t arraylen, signed short param, signed short *data2) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft, datasliceright, resultslice;
	signed short opvals[SHORTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = vld1q_s16( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_s16( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s16( &data2[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param * data2[x];
	}

}



// param_num_arr_arr
void mul_signed_short_4_simd(Py_ssize_t arraylen, signed short param, signed short *data2, signed short *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft, datasliceright, resultslice;
	signed short opvals[SHORTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = vld1q_s16( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_s16( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s16( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param * data2[x];
	}

}



// param_arr_arr_none
void mul_signed_short_5_simd(Py_ssize_t arraylen, signed short *data1, signed short *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s16( &data1[x]);
		datasliceright = vld1q_s16( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s16( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * data2[x];
	}

}



// param_arr_arr_arr
void mul_signed_short_6_simd(Py_ssize_t arraylen, signed short *data1, signed short *data2, signed short *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s16( &data1[x]);
		datasliceright = vld1q_s16( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s16( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * data2[x];
	}

}
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
void mul_unsigned_short_1_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x8_t datasliceleft, datasliceright, resultslice;
	unsigned short opvals[SHORTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = vld1q_u16( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u16( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * param;
	}

}



// param_arr_num_arr
void mul_unsigned_short_2_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param, unsigned short *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x8_t datasliceleft, datasliceright, resultslice;
	unsigned short opvals[SHORTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = vld1q_u16( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u16( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * param;
	}

}



// param_num_arr_none
void mul_unsigned_short_3_simd(Py_ssize_t arraylen, unsigned short param, unsigned short *data2) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x8_t datasliceleft, datasliceright, resultslice;
	unsigned short opvals[SHORTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = vld1q_u16( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_u16( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16( &data2[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param * data2[x];
	}

}



// param_num_arr_arr
void mul_unsigned_short_4_simd(Py_ssize_t arraylen, unsigned short param, unsigned short *data2, unsigned short *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x8_t datasliceleft, datasliceright, resultslice;
	unsigned short opvals[SHORTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = vld1q_u16( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_u16( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param * data2[x];
	}

}



// param_arr_arr_none
void mul_unsigned_short_5_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x8_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u16( &data1[x]);
		datasliceright = vld1q_u16( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * data2[x];
	}

}



// param_arr_arr_arr
void mul_unsigned_short_6_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2, unsigned short *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x8_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u16( &data1[x]);
		datasliceright = vld1q_u16( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * data2[x];
	}

}
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
void mul_signed_int_1_simd(Py_ssize_t arraylen, signed int *data1, signed int param) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft, datasliceright, resultslice;
	signed int opvals[INTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = vld1q_s32( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s32( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_s32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s32( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * param;
	}

}



// param_arr_num_arr
void mul_signed_int_2_simd(Py_ssize_t arraylen, signed int *data1, signed int param, signed int *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft, datasliceright, resultslice;
	signed int opvals[INTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = vld1q_s32( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s32( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_s32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s32( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * param;
	}

}



// param_num_arr_none
void mul_signed_int_3_simd(Py_ssize_t arraylen, signed int param, signed int *data2) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft, datasliceright, resultslice;
	signed int opvals[INTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = vld1q_s32( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_s32( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_s32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s32( &data2[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param * data2[x];
	}

}



// param_num_arr_arr
void mul_signed_int_4_simd(Py_ssize_t arraylen, signed int param, signed int *data2, signed int *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft, datasliceright, resultslice;
	signed int opvals[INTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = vld1q_s32( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_s32( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_s32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s32( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param * data2[x];
	}

}



// param_arr_arr_none
void mul_signed_int_5_simd(Py_ssize_t arraylen, signed int *data1, signed int *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s32( &data1[x]);
		datasliceright = vld1q_s32( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_s32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s32( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * data2[x];
	}

}



// param_arr_arr_arr
void mul_signed_int_6_simd(Py_ssize_t arraylen, signed int *data1, signed int *data2, signed int *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s32( &data1[x]);
		datasliceright = vld1q_s32( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_s32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s32( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * data2[x];
	}

}
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
void mul_unsigned_int_1_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x4_t datasliceleft, datasliceright, resultslice;
	unsigned int opvals[INTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = vld1q_u32( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u32( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * param;
	}

}



// param_arr_num_arr
void mul_unsigned_int_2_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param, unsigned int *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x4_t datasliceleft, datasliceright, resultslice;
	unsigned int opvals[INTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = vld1q_u32( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u32( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * param;
	}

}



// param_num_arr_none
void mul_unsigned_int_3_simd(Py_ssize_t arraylen, unsigned int param, unsigned int *data2) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x4_t datasliceleft, datasliceright, resultslice;
	unsigned int opvals[INTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = vld1q_u32( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_u32( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32( &data2[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param * data2[x];
	}

}



// param_num_arr_arr
void mul_unsigned_int_4_simd(Py_ssize_t arraylen, unsigned int param, unsigned int *data2, unsigned int *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x4_t datasliceleft, datasliceright, resultslice;
	unsigned int opvals[INTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = vld1q_u32( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_u32( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param * data2[x];
	}

}



// param_arr_arr_none
void mul_unsigned_int_5_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x4_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u32( &data1[x]);
		datasliceright = vld1q_u32( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * data2[x];
	}

}



// param_arr_arr_arr
void mul_unsigned_int_6_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2, unsigned int *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x4_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u32( &data1[x]);
		datasliceright = vld1q_u32( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * data2[x];
	}

}
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
void mul_float_1_simd(Py_ssize_t arraylen, float *data1, float param) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x4_t datasliceleft, datasliceright, resultslice;
	float opvals[FLOATSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = vld1q_f32( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_f32( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_f32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_f32( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * param;
	}

}



// param_arr_num_arr
void mul_float_2_simd(Py_ssize_t arraylen, float *data1, float param, float *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x4_t datasliceleft, datasliceright, resultslice;
	float opvals[FLOATSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = vld1q_f32( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_f32( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_f32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_f32( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * param;
	}

}



// param_num_arr_none
void mul_float_3_simd(Py_ssize_t arraylen, float param, float *data2) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x4_t datasliceleft, datasliceright, resultslice;
	float opvals[FLOATSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = vld1q_f32( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_f32( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_f32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_f32( &data2[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param * data2[x];
	}

}



// param_num_arr_arr
void mul_float_4_simd(Py_ssize_t arraylen, float param, float *data2, float *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x4_t datasliceleft, datasliceright, resultslice;
	float opvals[FLOATSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = vld1q_f32( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_f32( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_f32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_f32( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param * data2[x];
	}

}



// param_arr_arr_none
void mul_float_5_simd(Py_ssize_t arraylen, float *data1, float *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x4_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_f32( &data1[x]);
		datasliceright = vld1q_f32( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_f32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_f32( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * data2[x];
	}

}



// param_arr_arr_arr
void mul_float_6_simd(Py_ssize_t arraylen, float *data1, float *data2, float *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x4_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_f32( &data1[x]);
		datasliceright = vld1q_f32( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmulq_f32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_f32( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * data2[x];
	}

}
#endif

/*--------------------------------------------------------------------------- */
