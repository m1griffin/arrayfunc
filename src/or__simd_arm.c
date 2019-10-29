//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   or__simd_arm.c
// Purpose:  Calculate the or_ of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     05-Oct-2019
// Ver:      20-Oct-2019.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2019    Michael Griffin    <m12.griffin@gmail.com>
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
#ifdef AF_HASSIMD_ARM
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
#if defined(AF_HASSIMD_ARM)
void or__signed_char_1_simd(Py_ssize_t arraylen, signed char *data1, signed char param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	 int8x8_t datasliceleft, datasliceright;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1_s8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s8( &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_s8( &data1[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] | param;
	}

}
#endif


// param_arr_num_arr
#if defined(AF_HASSIMD_ARM)
void or__signed_char_2_simd(Py_ssize_t arraylen, signed char *data1, signed char param, signed char *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	 int8x8_t datasliceleft, datasliceright;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1_s8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s8( &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_s8( &data3[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] | param;
	}

}
#endif


// param_num_arr_none
#if defined(AF_HASSIMD_ARM)
void or__signed_char_3_simd(Py_ssize_t arraylen, signed char param, signed char *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	 int8x8_t datasliceleft, datasliceright;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1_s8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_s8( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceright = datasliceleft | datasliceright;
		// Store the result.
		vst1_s8( &data2[index],  datasliceright);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data2[index] = param | data2[index];
	}

}
#endif


// param_num_arr_arr
#if defined(AF_HASSIMD_ARM)
void or__signed_char_4_simd(Py_ssize_t arraylen, signed char param, signed char *data2, signed char *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	 int8x8_t datasliceleft, datasliceright;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1_s8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_s8( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceright = datasliceleft | datasliceright;
		// Store the result.
		vst1_s8( &data3[index],  datasliceright);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = param | data2[index];
	}

}
#endif


// param_arr_arr_none
#if defined(AF_HASSIMD_ARM)
void or__signed_char_5_simd(Py_ssize_t arraylen, signed char *data1, signed char *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	 int8x8_t datasliceleft, datasliceright;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s8( &data1[index]);
		datasliceright = vld1_s8( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_s8( &data1[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] | data2[index];
	}

}
#endif


// param_arr_arr_arr
#if defined(AF_HASSIMD_ARM)
void or__signed_char_6_simd(Py_ssize_t arraylen, signed char *data1, signed char *data2, signed char *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	 int8x8_t datasliceleft, datasliceright;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s8( &data1[index]);
		datasliceright = vld1_s8( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_s8( &data3[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] | data2[index];
	}

}
#endif


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM)
void or__unsigned_char_1_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint8x8_t datasliceleft, datasliceright;
	unsigned char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1_u8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u8( &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_u8( &data1[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] | param;
	}

}
#endif


// param_arr_num_arr
#if defined(AF_HASSIMD_ARM)
void or__unsigned_char_2_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param, unsigned char *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint8x8_t datasliceleft, datasliceright;
	unsigned char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1_u8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u8( &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_u8( &data3[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] | param;
	}

}
#endif


// param_num_arr_none
#if defined(AF_HASSIMD_ARM)
void or__unsigned_char_3_simd(Py_ssize_t arraylen, unsigned char param, unsigned char *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint8x8_t datasliceleft, datasliceright;
	unsigned char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1_u8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_u8( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceright = datasliceleft | datasliceright;
		// Store the result.
		vst1_u8( &data2[index],  datasliceright);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data2[index] = param | data2[index];
	}

}
#endif


// param_num_arr_arr
#if defined(AF_HASSIMD_ARM)
void or__unsigned_char_4_simd(Py_ssize_t arraylen, unsigned char param, unsigned char *data2, unsigned char *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint8x8_t datasliceleft, datasliceright;
	unsigned char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1_u8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_u8( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceright = datasliceleft | datasliceright;
		// Store the result.
		vst1_u8( &data3[index],  datasliceright);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = param | data2[index];
	}

}
#endif


// param_arr_arr_none
#if defined(AF_HASSIMD_ARM)
void or__unsigned_char_5_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x8_t datasliceleft, datasliceright;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u8( &data1[index]);
		datasliceright = vld1_u8( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_u8( &data1[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] | data2[index];
	}

}
#endif


// param_arr_arr_arr
#if defined(AF_HASSIMD_ARM)
void or__unsigned_char_6_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2, unsigned char *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x8_t datasliceleft, datasliceright;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u8( &data1[index]);
		datasliceright = vld1_u8( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_u8( &data3[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] | data2[index];
	}

}
#endif


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM)
void or__signed_short_1_simd(Py_ssize_t arraylen, signed short *data1, signed short param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int16x4_t datasliceleft, datasliceright;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1_s16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s16( &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_s16( &data1[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] | param;
	}

}
#endif


// param_arr_num_arr
#if defined(AF_HASSIMD_ARM)
void or__signed_short_2_simd(Py_ssize_t arraylen, signed short *data1, signed short param, signed short *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int16x4_t datasliceleft, datasliceright;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1_s16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s16( &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_s16( &data3[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] | param;
	}

}
#endif


// param_num_arr_none
#if defined(AF_HASSIMD_ARM)
void or__signed_short_3_simd(Py_ssize_t arraylen, signed short param, signed short *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int16x4_t datasliceleft, datasliceright;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1_s16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_s16( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceright = datasliceleft | datasliceright;
		// Store the result.
		vst1_s16( &data2[index],  datasliceright);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data2[index] = param | data2[index];
	}

}
#endif


// param_num_arr_arr
#if defined(AF_HASSIMD_ARM)
void or__signed_short_4_simd(Py_ssize_t arraylen, signed short param, signed short *data2, signed short *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int16x4_t datasliceleft, datasliceright;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1_s16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_s16( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceright = datasliceleft | datasliceright;
		// Store the result.
		vst1_s16( &data3[index],  datasliceright);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = param | data2[index];
	}

}
#endif


// param_arr_arr_none
#if defined(AF_HASSIMD_ARM)
void or__signed_short_5_simd(Py_ssize_t arraylen, signed short *data1, signed short *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x4_t datasliceleft, datasliceright;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s16( &data1[index]);
		datasliceright = vld1_s16( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_s16( &data1[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] | data2[index];
	}

}
#endif


// param_arr_arr_arr
#if defined(AF_HASSIMD_ARM)
void or__signed_short_6_simd(Py_ssize_t arraylen, signed short *data1, signed short *data2, signed short *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x4_t datasliceleft, datasliceright;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s16( &data1[index]);
		datasliceright = vld1_s16( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_s16( &data3[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] | data2[index];
	}

}
#endif


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM)
void or__unsigned_short_1_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint16x4_t datasliceleft, datasliceright;
	unsigned short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1_u16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u16( &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		 vst1_u16( &data1[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] | param;
	}

}
#endif


// param_arr_num_arr
#if defined(AF_HASSIMD_ARM)
void or__unsigned_short_2_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param, unsigned short *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint16x4_t datasliceleft, datasliceright;
	unsigned short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1_u16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u16( &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		 vst1_u16( &data3[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] | param;
	}

}
#endif


// param_num_arr_none
#if defined(AF_HASSIMD_ARM)
void or__unsigned_short_3_simd(Py_ssize_t arraylen, unsigned short param, unsigned short *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint16x4_t datasliceleft, datasliceright;
	unsigned short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1_u16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_u16( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceright = datasliceleft | datasliceright;
		// Store the result.
		 vst1_u16( &data2[index],  datasliceright);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data2[index] = param | data2[index];
	}

}
#endif


// param_num_arr_arr
#if defined(AF_HASSIMD_ARM)
void or__unsigned_short_4_simd(Py_ssize_t arraylen, unsigned short param, unsigned short *data2, unsigned short *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint16x4_t datasliceleft, datasliceright;
	unsigned short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1_u16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_u16( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceright = datasliceleft | datasliceright;
		// Store the result.
		 vst1_u16( &data3[index],  datasliceright);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = param | data2[index];
	}

}
#endif


// param_arr_arr_none
#if defined(AF_HASSIMD_ARM)
void or__unsigned_short_5_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x4_t datasliceleft, datasliceright;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u16( &data1[index]);
		datasliceright = vld1_u16( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		 vst1_u16( &data1[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] | data2[index];
	}

}
#endif


// param_arr_arr_arr
#if defined(AF_HASSIMD_ARM)
void or__unsigned_short_6_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2, unsigned short *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x4_t datasliceleft, datasliceright;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u16( &data1[index]);
		datasliceright = vld1_u16( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		 vst1_u16( &data3[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] | data2[index];
	}

}
#endif


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM)
void or__signed_int_1_simd(Py_ssize_t arraylen, signed int *data1, signed int param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int32x2_t  datasliceleft, datasliceright;
	signed int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1_s32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s32( &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_s32( &data1[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] | param;
	}

}
#endif


// param_arr_num_arr
#if defined(AF_HASSIMD_ARM)
void or__signed_int_2_simd(Py_ssize_t arraylen, signed int *data1, signed int param, signed int *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int32x2_t  datasliceleft, datasliceright;
	signed int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1_s32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s32( &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_s32( &data3[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] | param;
	}

}
#endif


// param_num_arr_none
#if defined(AF_HASSIMD_ARM)
void or__signed_int_3_simd(Py_ssize_t arraylen, signed int param, signed int *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int32x2_t  datasliceleft, datasliceright;
	signed int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1_s32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_s32( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceright = datasliceleft | datasliceright;
		// Store the result.
		vst1_s32( &data2[index],  datasliceright);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data2[index] = param | data2[index];
	}

}
#endif


// param_num_arr_arr
#if defined(AF_HASSIMD_ARM)
void or__signed_int_4_simd(Py_ssize_t arraylen, signed int param, signed int *data2, signed int *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int32x2_t  datasliceleft, datasliceright;
	signed int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1_s32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_s32( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceright = datasliceleft | datasliceright;
		// Store the result.
		vst1_s32( &data3[index],  datasliceright);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = param | data2[index];
	}

}
#endif


// param_arr_arr_none
#if defined(AF_HASSIMD_ARM)
void or__signed_int_5_simd(Py_ssize_t arraylen, signed int *data1, signed int *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x2_t  datasliceleft, datasliceright;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s32( &data1[index]);
		datasliceright = vld1_s32( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_s32( &data1[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] | data2[index];
	}

}
#endif


// param_arr_arr_arr
#if defined(AF_HASSIMD_ARM)
void or__signed_int_6_simd(Py_ssize_t arraylen, signed int *data1, signed int *data2, signed int *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x2_t  datasliceleft, datasliceright;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s32( &data1[index]);
		datasliceright = vld1_s32( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_s32( &data3[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] | data2[index];
	}

}
#endif


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM)
void or__unsigned_int_1_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint32x2_t datasliceleft, datasliceright;
	unsigned int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1_u32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u32( &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_u32( &data1[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] | param;
	}

}
#endif


// param_arr_num_arr
#if defined(AF_HASSIMD_ARM)
void or__unsigned_int_2_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param, unsigned int *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint32x2_t datasliceleft, datasliceright;
	unsigned int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = vld1_u32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u32( &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_u32( &data3[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] | param;
	}

}
#endif


// param_num_arr_none
#if defined(AF_HASSIMD_ARM)
void or__unsigned_int_3_simd(Py_ssize_t arraylen, unsigned int param, unsigned int *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint32x2_t datasliceleft, datasliceright;
	unsigned int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1_u32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_u32( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceright = datasliceleft | datasliceright;
		// Store the result.
		vst1_u32( &data2[index],  datasliceright);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data2[index] = param | data2[index];
	}

}
#endif


// param_num_arr_arr
#if defined(AF_HASSIMD_ARM)
void or__unsigned_int_4_simd(Py_ssize_t arraylen, unsigned int param, unsigned int *data2, unsigned int *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint32x2_t datasliceleft, datasliceright;
	unsigned int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = vld1_u32( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_u32( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceright = datasliceleft | datasliceright;
		// Store the result.
		vst1_u32( &data3[index],  datasliceright);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = param | data2[index];
	}

}
#endif


// param_arr_arr_none
#if defined(AF_HASSIMD_ARM)
void or__unsigned_int_5_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x2_t datasliceleft, datasliceright;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u32( &data1[index]);
		datasliceright = vld1_u32( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_u32( &data1[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] | data2[index];
	}

}
#endif


// param_arr_arr_arr
#if defined(AF_HASSIMD_ARM)
void or__unsigned_int_6_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2, unsigned int *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x2_t datasliceleft, datasliceright;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u32( &data1[index]);
		datasliceright = vld1_u32( &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft | datasliceright;
		// Store the result.
		vst1_u32( &data3[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] | data2[index];
	}

}
#endif

