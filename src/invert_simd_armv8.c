//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   invert_simd_armv8.c
// Purpose:  Calculate the invert of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     25-Mar-2020
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
   data = The input data array.
   dataout = The output data array.
*/
// param_arr_none
#if defined(AF_HASSIMD_ARM_AARCH64)
void invert_signed_char_1_simd(Py_ssize_t arraylen, signed char *data) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	 int8x16_t datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s8(&data[index]);
		// The actual SIMD operation. 
		datasliceleft = vmvnq_s8(datasliceleft);
		// Store the result.
		vst1q_s8(&data[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data[index] = ~data[index];
	}

}


// param_arr_arr
void invert_signed_char_2_simd(Py_ssize_t arraylen, signed char *data, signed char *dataout) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	 int8x16_t datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s8(&data[index]);
		// The actual SIMD operation. 
		datasliceleft = vmvnq_s8(datasliceleft);
		// Store the result.
		vst1q_s8(&dataout[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		dataout[index] = ~data[index];
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
void invert_unsigned_char_1_simd(Py_ssize_t arraylen, unsigned char *data) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x16_t datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u8(&data[index]);
		// The actual SIMD operation. 
		datasliceleft = vmvnq_u8(datasliceleft);
		// Store the result.
		vst1q_u8(&data[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data[index] = ~data[index];
	}

}


// param_arr_arr
void invert_unsigned_char_2_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char *dataout) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x16_t datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u8(&data[index]);
		// The actual SIMD operation. 
		datasliceleft = vmvnq_u8(datasliceleft);
		// Store the result.
		vst1q_u8(&dataout[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		dataout[index] = ~data[index];
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
void invert_signed_short_1_simd(Py_ssize_t arraylen, signed short *data) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s16(&data[index]);
		// The actual SIMD operation. 
		datasliceleft = vmvnq_s16(datasliceleft);
		// Store the result.
		vst1q_s16(&data[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data[index] = ~data[index];
	}

}


// param_arr_arr
void invert_signed_short_2_simd(Py_ssize_t arraylen, signed short *data, signed short *dataout) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s16(&data[index]);
		// The actual SIMD operation. 
		datasliceleft = vmvnq_s16(datasliceleft);
		// Store the result.
		vst1q_s16(&dataout[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		dataout[index] = ~data[index];
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
void invert_unsigned_short_1_simd(Py_ssize_t arraylen, unsigned short *data) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x8_t datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u16(&data[index]);
		// The actual SIMD operation. 
		datasliceleft = vmvnq_u16(datasliceleft);
		// Store the result.
		vst1q_u16(&data[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data[index] = ~data[index];
	}

}


// param_arr_arr
void invert_unsigned_short_2_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short *dataout) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x8_t datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u16(&data[index]);
		// The actual SIMD operation. 
		datasliceleft = vmvnq_u16(datasliceleft);
		// Store the result.
		vst1q_u16(&dataout[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		dataout[index] = ~data[index];
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
void invert_signed_int_1_simd(Py_ssize_t arraylen, signed int *data) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t  datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s32(&data[index]);
		// The actual SIMD operation. 
		datasliceleft = vmvnq_s32(datasliceleft);
		// Store the result.
		vst1q_s32(&data[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data[index] = ~data[index];
	}

}


// param_arr_arr
void invert_signed_int_2_simd(Py_ssize_t arraylen, signed int *data, signed int *dataout) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t  datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s32(&data[index]);
		// The actual SIMD operation. 
		datasliceleft = vmvnq_s32(datasliceleft);
		// Store the result.
		vst1q_s32(&dataout[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		dataout[index] = ~data[index];
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
void invert_unsigned_int_1_simd(Py_ssize_t arraylen, unsigned int *data) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x4_t datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u32(&data[index]);
		// The actual SIMD operation. 
		datasliceleft = vmvnq_u32(datasliceleft);
		// Store the result.
		vst1q_u32(&data[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data[index] = ~data[index];
	}

}


// param_arr_arr
void invert_unsigned_int_2_simd(Py_ssize_t arraylen, unsigned int *data, unsigned int *dataout) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x4_t datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u32(&data[index]);
		// The actual SIMD operation. 
		datasliceleft = vmvnq_u32(datasliceleft);
		// Store the result.
		vst1q_u32(&dataout[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		dataout[index] = ~data[index];
	}

}
#endif

