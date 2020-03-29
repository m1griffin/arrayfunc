//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   ne_simd_armv7.c
// Purpose:  Calculate the ne of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     06-Oct-2019
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


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#if defined(AF_HASSIMD_ARMv7_32BIT)
char ne_signed_char_1_simd(Py_ssize_t arraylen, signed char *data1, signed char param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int8x8_t datasliceleft, datasliceright;
	uint8x8_t resultslice;
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
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1_s8( &data1[index]);
		// The actual SIMD operation. 
		resultslice = vceq_s8(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(vreinterpret_u64_u8(resultslice) == 0x0000000000000000)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] != param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char ne_signed_char_3_simd(Py_ssize_t arraylen, signed char param, signed char *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int8x8_t datasliceleft, datasliceright;
	uint8x8_t resultslice;
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
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceright = vld1_s8( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vceq_s8(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(vreinterpret_u64_u8(resultslice) == 0x0000000000000000)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(param != data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char ne_signed_char_5_simd(Py_ssize_t arraylen, signed char *data1, signed char *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x8_t datasliceleft, datasliceright;
	uint8x8_t resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1_s8( &data1[index]);
		datasliceright = vld1_s8( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vceq_s8(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(vreinterpret_u64_u8(resultslice) == 0x0000000000000000)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] != data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */



/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#if defined(AF_HASSIMD_ARMv7_32BIT)
char ne_unsigned_char_1_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint8x8_t datasliceleft, datasliceright;
	uint8x8_t resultslice;
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
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1_u8( &data1[index]);
		// The actual SIMD operation. 
		resultslice = vceq_u8(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(vreinterpret_u64_u8(resultslice) == 0x0000000000000000)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] != param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char ne_unsigned_char_3_simd(Py_ssize_t arraylen, unsigned char param, unsigned char *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint8x8_t datasliceleft, datasliceright;
	uint8x8_t resultslice;
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
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceright = vld1_u8( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vceq_u8(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(vreinterpret_u64_u8(resultslice) == 0x0000000000000000)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(param != data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char ne_unsigned_char_5_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x8_t datasliceleft, datasliceright;
	uint8x8_t resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1_u8( &data1[index]);
		datasliceright = vld1_u8( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vceq_u8(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(vreinterpret_u64_u8(resultslice) == 0x0000000000000000)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] != data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */



/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#if defined(AF_HASSIMD_ARMv7_32BIT)
char ne_signed_short_1_simd(Py_ssize_t arraylen, signed short *data1, signed short param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int16x4_t datasliceleft, datasliceright;
	uint16x4_t resultslice;
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
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1_s16( &data1[index]);
		// The actual SIMD operation. 
		resultslice = vceq_s16(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(vreinterpret_u64_u16(resultslice) == 0x0000000000000000)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] != param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char ne_signed_short_3_simd(Py_ssize_t arraylen, signed short param, signed short *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int16x4_t datasliceleft, datasliceright;
	uint16x4_t resultslice;
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
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceright = vld1_s16( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vceq_s16(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(vreinterpret_u64_u16(resultslice) == 0x0000000000000000)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(param != data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char ne_signed_short_5_simd(Py_ssize_t arraylen, signed short *data1, signed short *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x4_t datasliceleft, datasliceright;
	uint16x4_t resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1_s16( &data1[index]);
		datasliceright = vld1_s16( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vceq_s16(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(vreinterpret_u64_u16(resultslice) == 0x0000000000000000)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] != data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */



/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#if defined(AF_HASSIMD_ARMv7_32BIT)
char ne_unsigned_short_1_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint16x4_t datasliceleft, datasliceright;
	uint16x4_t resultslice;
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
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1_u16( &data1[index]);
		// The actual SIMD operation. 
		resultslice = vceq_u16(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(vreinterpret_u64_u16(resultslice) == 0x0000000000000000)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] != param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char ne_unsigned_short_3_simd(Py_ssize_t arraylen, unsigned short param, unsigned short *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint16x4_t datasliceleft, datasliceright;
	uint16x4_t resultslice;
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
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceright = vld1_u16( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vceq_u16(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(vreinterpret_u64_u16(resultslice) == 0x0000000000000000)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(param != data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char ne_unsigned_short_5_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x4_t datasliceleft, datasliceright;
	uint16x4_t resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1_u16( &data1[index]);
		datasliceright = vld1_u16( &data2[index]);
		// The actual SIMD operation. 
		resultslice = vceq_u16(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (!(vreinterpret_u64_u16(resultslice) == 0x0000000000000000)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] != data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */

