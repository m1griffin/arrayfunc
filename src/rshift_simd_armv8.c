//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   rshift_simd_armv8.c
// Purpose:  Calculate the rshift of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     24-Mar-2020
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
#include "rshift_defs.h"

/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specified value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
   Right shift is implemented by a negative shift amount. This is coded
   directly into the function. 
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
int8x16_t initvec_armshift_signed_char(signed char initval) {

	unsigned int y;
	signed char initvals[CHARSIMDSIZE];
	int8x16_t simdvec;

	for (y = 0; y < CHARSIMDSIZE; y++) {
		initvals[y] = -(signed char)initval;
	}
	simdvec = vld1q_s8(initvals);

	return simdvec;
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
#if defined(AF_HASSIMD_ARM_AARCH64)
void rshift_signed_char_1_simd(Py_ssize_t arraylen, signed char *data1, signed char param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft;
	int8x16_t datasliceright;

	// Initialise the comparison values.
	datasliceright = initvec_armshift_signed_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s8((&data1[index]));
		// The actual SIMD operation. 
		datasliceleft = vshlq_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s8(&data1[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] >> param;
	}

}



// param_arr_num_arr
void rshift_signed_char_2_simd(Py_ssize_t arraylen, signed char *data1, signed char param, signed char *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft;
	int8x16_t datasliceright;

	// Initialise the comparison values.
	datasliceright = initvec_armshift_signed_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s8((&data1[index]));
		// The actual SIMD operation. 
		datasliceleft = vshlq_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s8(&data3[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] >> param;
	}

}
#endif


/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specified value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
   Right shift is implemented by a negative shift amount. This is coded
   directly into the function. 
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
int8x16_t initvec_armshift_unsigned_char(unsigned char initval) {

	unsigned int y;
	signed char initvals[CHARSIMDSIZE];
	int8x16_t simdvec;

	for (y = 0; y < CHARSIMDSIZE; y++) {
		initvals[y] = -(signed char)initval;
	}
	simdvec = vld1q_s8(initvals);

	return simdvec;
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
#if defined(AF_HASSIMD_ARM_AARCH64)
void rshift_unsigned_char_1_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x16_t datasliceleft;
	int8x16_t datasliceright;

	// Initialise the comparison values.
	datasliceright = initvec_armshift_unsigned_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u8((&data1[index]));
		// The actual SIMD operation. 
		datasliceleft = vshlq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8(&data1[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] >> param;
	}

}



// param_arr_num_arr
void rshift_unsigned_char_2_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param, unsigned char *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x16_t datasliceleft;
	int8x16_t datasliceright;

	// Initialise the comparison values.
	datasliceright = initvec_armshift_unsigned_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u8((&data1[index]));
		// The actual SIMD operation. 
		datasliceleft = vshlq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8(&data3[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] >> param;
	}

}
#endif


/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specified value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
   Right shift is implemented by a negative shift amount. This is coded
   directly into the function. 
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
int16x8_t initvec_armshift_signed_short(signed short initval) {

	unsigned int y;
	signed short initvals[SHORTSIMDSIZE];
	int16x8_t simdvec;

	for (y = 0; y < SHORTSIMDSIZE; y++) {
		initvals[y] = -(signed short)initval;
	}
	simdvec = vld1q_s16(initvals);

	return simdvec;
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
#if defined(AF_HASSIMD_ARM_AARCH64)
void rshift_signed_short_1_simd(Py_ssize_t arraylen, signed short *data1, signed short param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft;
	int16x8_t datasliceright;

	// Initialise the comparison values.
	datasliceright = initvec_armshift_signed_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s16((&data1[index]));
		// The actual SIMD operation. 
		datasliceleft = vshlq_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s16(&data1[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] >> param;
	}

}



// param_arr_num_arr
void rshift_signed_short_2_simd(Py_ssize_t arraylen, signed short *data1, signed short param, signed short *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft;
	int16x8_t datasliceright;

	// Initialise the comparison values.
	datasliceright = initvec_armshift_signed_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s16((&data1[index]));
		// The actual SIMD operation. 
		datasliceleft = vshlq_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s16(&data3[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] >> param;
	}

}
#endif


/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specified value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
   Right shift is implemented by a negative shift amount. This is coded
   directly into the function. 
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
int16x8_t initvec_armshift_unsigned_short(unsigned short initval) {

	unsigned int y;
	signed short initvals[SHORTSIMDSIZE];
	int16x8_t simdvec;

	for (y = 0; y < SHORTSIMDSIZE; y++) {
		initvals[y] = -(signed short)initval;
	}
	simdvec = vld1q_s16(initvals);

	return simdvec;
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
#if defined(AF_HASSIMD_ARM_AARCH64)
void rshift_unsigned_short_1_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x8_t datasliceleft;
	int16x8_t datasliceright;

	// Initialise the comparison values.
	datasliceright = initvec_armshift_unsigned_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u16((&data1[index]));
		// The actual SIMD operation. 
		datasliceleft = vshlq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16(&data1[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] >> param;
	}

}



// param_arr_num_arr
void rshift_unsigned_short_2_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param, unsigned short *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x8_t datasliceleft;
	int16x8_t datasliceright;

	// Initialise the comparison values.
	datasliceright = initvec_armshift_unsigned_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u16((&data1[index]));
		// The actual SIMD operation. 
		datasliceleft = vshlq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16(&data3[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] >> param;
	}

}
#endif


/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specified value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
   Right shift is implemented by a negative shift amount. This is coded
   directly into the function. 
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
int32x4_t initvec_armshift_signed_int(signed int initval) {

	unsigned int y;
	signed int initvals[INTSIMDSIZE];
	int32x4_t simdvec;

	for (y = 0; y < INTSIMDSIZE; y++) {
		initvals[y] = -(signed int)initval;
	}
	simdvec = vld1q_s32(initvals);

	return simdvec;
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
#if defined(AF_HASSIMD_ARM_AARCH64)
void rshift_signed_int_1_simd(Py_ssize_t arraylen, signed int *data1, signed int param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft;
	int32x4_t datasliceright;

	// Initialise the comparison values.
	datasliceright = initvec_armshift_signed_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s32((&data1[index]));
		// The actual SIMD operation. 
		datasliceleft = vshlq_s32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s32(&data1[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] >> param;
	}

}



// param_arr_num_arr
void rshift_signed_int_2_simd(Py_ssize_t arraylen, signed int *data1, signed int param, signed int *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft;
	int32x4_t datasliceright;

	// Initialise the comparison values.
	datasliceright = initvec_armshift_signed_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s32((&data1[index]));
		// The actual SIMD operation. 
		datasliceleft = vshlq_s32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s32(&data3[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] >> param;
	}

}
#endif


/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specified value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
   Right shift is implemented by a negative shift amount. This is coded
   directly into the function. 
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
int32x4_t initvec_armshift_unsigned_int(unsigned int initval) {

	unsigned int y;
	signed int initvals[INTSIMDSIZE];
	int32x4_t simdvec;

	for (y = 0; y < INTSIMDSIZE; y++) {
		initvals[y] = -(signed int)initval;
	}
	simdvec = vld1q_s32(initvals);

	return simdvec;
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
#if defined(AF_HASSIMD_ARM_AARCH64)
void rshift_unsigned_int_1_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x4_t datasliceleft;
	int32x4_t datasliceright;

	// Initialise the comparison values.
	datasliceright = initvec_armshift_unsigned_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u32((&data1[index]));
		// The actual SIMD operation. 
		datasliceleft = vshlq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32(&data1[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] >> param;
	}

}



// param_arr_num_arr
void rshift_unsigned_int_2_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param, unsigned int *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x4_t datasliceleft;
	int32x4_t datasliceright;

	// Initialise the comparison values.
	datasliceright = initvec_armshift_unsigned_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u32((&data1[index]));
		// The actual SIMD operation. 
		datasliceleft = vshlq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32(&data3[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] >> param;
	}

}
#endif

