//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   add_simd_armv8.c
// Purpose:  Calculate the add of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     26-Mar-2020
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
#include "add_defs.h"

// Function specific macros and other definitions.
#include "add_defs.h"

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
   This version is without overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
void add_signed_char_1_simd(Py_ssize_t arraylen, signed char *data1, signed char param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_signed_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s8( &data1[x]);
		// The actual SIMD operation. 
		resultslice = vaddq_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s8( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] + param;
	}

}



// param_arr_num_arr
void add_signed_char_2_simd(Py_ssize_t arraylen, signed char *data1, signed char param, signed char *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_signed_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s8( &data1[x]);
		// The actual SIMD operation.
		resultslice = vaddq_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s8( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] + param;
	}

}



// param_num_arr_none
void add_signed_char_3_simd(Py_ssize_t arraylen, signed char param, signed char *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_signed_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_s8( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s8( &data2[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param + data2[x];
	}

}



// param_num_arr_arr
void add_signed_char_4_simd(Py_ssize_t arraylen, signed char param, signed char *data2, signed char *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_signed_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_s8( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s8( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param + data2[x];
	}

}



// param_arr_arr_none
void add_signed_char_5_simd(Py_ssize_t arraylen, signed char *data1, signed char *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s8( &data1[x]);
		datasliceright = vld1q_s8( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s8( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] + data2[x];
	}

}



// param_arr_arr_arr
void add_signed_char_6_simd(Py_ssize_t arraylen, signed char *data1, signed char *data2, signed char *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x16_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s8( &data1[x]);
		datasliceright = vld1q_s8( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s8( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] + data2[x];
	}

}
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   This version supports overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   Returns 1 if overflow occurred, else returns 0.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
char add_signed_char_1_simd_ovfl(Py_ssize_t arraylen, signed char *data1, signed char param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed char ovlimit;
	int8x16_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint8x16_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// We don't need to do anything if param is zero.
	if (param == 0) {
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_signed_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// param is positive.
	if (param > 0) {

		// Used to calculate overflow.
		ovlimit = pos_ovlimit_signed_char(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_char(ovlimit);


		for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s8( &data1[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = vcgtq_s8 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s8(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s8( &data1[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( pos_willoverflow(data1[x], ovlimit) ) {return 1;}
			data1[x] = data1[x] + param; 
		}

	}


	// param is negative.
	if (param < 0) {

		// Used to calculate overflow.
		ovlimit = neg_ovlimit_signed_char(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_char(ovlimit);


		for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s8( &data1[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = vcltq_s8 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s8(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s8( &data1[x],  resultslice);

		}
	
		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( neg_willoverflow(data1[x], ovlimit) ) {return 1;}
			data1[x] = data1[x] + param; 
		}
	}

	return 0;

}



// param_arr_num_arr
char add_signed_char_2_simd_ovfl(Py_ssize_t arraylen, signed char *data1, signed char param, signed char *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed char ovlimit;
	int8x16_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint8x16_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// We don't need to do anything if param is zero, just copy the data.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x];
		}
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_signed_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// param is positive.
	if (param > 0) {

		// Used to calculate overflow.
		ovlimit = pos_ovlimit_signed_char(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_char(ovlimit);


		for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s8( &data1[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = vcgtq_s8 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s8(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s8( &data3[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( pos_willoverflow(data1[x], ovlimit) ) {return 1;}
			data3[x] = data1[x] + param; 
		}
	}


	// param is negative.
	if (param < 0) {

		// Used to calculate overflow.
		ovlimit = neg_ovlimit_signed_char(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_char(ovlimit);


		for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s8( &data1[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = vcltq_s8 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s8(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s8( &data3[x],  resultslice);

		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( neg_willoverflow(data1[x], ovlimit) ) {return 1;}
			data3[x] = data1[x] + param; 
		}
	}

	return 0;

}



// param_num_arr_none
char add_signed_char_3_simd_ovfl(Py_ssize_t arraylen, signed char param, signed char *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed char ovlimit;
	int8x16_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint8x16_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// We don't need to do anything if param is zero.
	if (param == 0) {
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_signed_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// param is positive.
	if (param > 0) {

		ovlimit = pos_ovlimit_signed_char(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_char(ovlimit);


		for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s8( &data2[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = vcgtq_s8 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s8(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s8( &data2[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( pos_willoverflow(data2[x], ovlimit) ) {return 1;}
			data2[x] = data2[x] + param; 
		}
	}


	// param is negative.
	if (param < 0) {

		// Used to calculate overflow.
		ovlimit = neg_ovlimit_signed_char(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_char(ovlimit);


		for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s8( &data2[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = vcltq_s8 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s8(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s8( &data2[x],  resultslice);

		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( neg_willoverflow(data2[x], ovlimit) ) {return 1;}
			data2[x] = data2[x] + param;
		}
	}

	return 0;

}



// param_num_arr_arr
char add_signed_char_4_simd_ovfl(Py_ssize_t arraylen, signed char param, signed char *data2, signed char *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed char ovlimit;
	int8x16_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint8x16_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// We don't need to do anything if param is zero, just copy the data.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
		data3[x] = data2[x];
		}
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_signed_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// param is positive.
	if (param > 0) {

		// Used to calculate overflow.
		ovlimit = pos_ovlimit_signed_char(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_char(ovlimit);


		for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s8( &data2[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = vcgtq_s8 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s8(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s8( &data3[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( pos_willoverflow(data2[x], ovlimit) ) {return 1;}
			data3[x] = data2[x] + param;
		}
	}


	// param is negative.
	if (param < 0) {

		// Used to calculate overflow.
		ovlimit = neg_ovlimit_signed_char(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_char(ovlimit);


		for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s8( &data2[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = vcltq_s8 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s8(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s8( &data3[x],  resultslice);

		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( neg_willoverflow(data2[x], ovlimit) ) {return 1;}
			data3[x] = data2[x] + param; 
		}
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
uint8x16_t initvec_unsigned_char(unsigned char initval) {

	unsigned int y;
	unsigned char initvals[CHARSIMDSIZE];
	uint8x16_t simdvec;

	for (y = 0; y < CHARSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = vld1q_u8((initvals));

	return simdvec;
}
#endif



/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   This version is without overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
void add_unsigned_char_1_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x16_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u8( &data1[x]);
		// The actual SIMD operation. 
		resultslice = vaddq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] + param;
	}

}



// param_arr_num_arr
void add_unsigned_char_2_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param, unsigned char *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x16_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u8( &data1[x]);
		// The actual SIMD operation.
		resultslice = vaddq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] + param;
	}

}



// param_num_arr_none
void add_unsigned_char_3_simd(Py_ssize_t arraylen, unsigned char param, unsigned char *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x16_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_unsigned_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_u8( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8( &data2[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param + data2[x];
	}

}



// param_num_arr_arr
void add_unsigned_char_4_simd(Py_ssize_t arraylen, unsigned char param, unsigned char *data2, unsigned char *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x16_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_unsigned_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_u8( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param + data2[x];
	}

}



// param_arr_arr_none
void add_unsigned_char_5_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x16_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u8( &data1[x]);
		datasliceright = vld1q_u8( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] + data2[x];
	}

}



// param_arr_arr_arr
void add_unsigned_char_6_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2, unsigned char *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x16_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u8( &data1[x]);
		datasliceright = vld1q_u8( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] + data2[x];
	}

}
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   This version is with overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
char add_unsigned_char_1_simd_ovfl(Py_ssize_t arraylen, unsigned char *data1, unsigned char param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned char ovlimit;
	uint8x16_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint8x16_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_char(param);


	// Used to calculate overflow.
	ovlimit = ovlimit_unsigned_char(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_char(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u8( &data1[x]);

		// Check for overflow. 
		// Do a greater than compare operation.
			ovcheck = vcgtq_u8 (datasliceleft, ovflvec);

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
		resultslice = vaddq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8( &data1[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( pos_willoverflow(data1[x], ovlimit) ) {return 1;}
		data1[x] = data1[x] + param;
	}

	return 0;

}



// param_arr_num_arr
char add_unsigned_char_2_simd_ovfl(Py_ssize_t arraylen, unsigned char *data1, unsigned char param, unsigned char *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned char ovlimit;
	uint8x16_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint8x16_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_char(param);


	// Used to calculate overflow.
	ovlimit = ovlimit_unsigned_char(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_char(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u8( &data1[x]);

		// Check for overflow. 
		// Do a greater than compare operation.
			ovcheck = vcgtq_u8 (datasliceleft, ovflvec);

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
		resultslice = vaddq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8( &data3[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( pos_willoverflow(data1[x], ovlimit) ) {return 1;}
		data3[x] = data1[x] + param;
	}

	return 0;

}



// param_num_arr_none
char add_unsigned_char_3_simd_ovfl(Py_ssize_t arraylen, unsigned char param, unsigned char *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned char ovlimit;
	uint8x16_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint8x16_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_char(param);

	// Used to calculate overflow.
	ovlimit = ovlimit_unsigned_char(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_char(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u8( &data2[x]);

		// Check for overflow. 
		// Do a greater than compare operation.
			ovcheck = vcgtq_u8 (datasliceleft, ovflvec);

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
		resultslice = vaddq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8( &data2[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( pos_willoverflow(data2[x], ovlimit) ) {return 1;}
		data2[x] = param + data2[x];
	}

	return 0;

}



// param_num_arr_arr
char add_unsigned_char_4_simd_ovfl(Py_ssize_t arraylen, unsigned char param, unsigned char *data2, unsigned char *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned char ovlimit;
	uint8x16_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint8x16_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_char(param);


	// Used to calculate overflow.
	ovlimit = ovlimit_unsigned_char(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_char(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u8( &data2[x]);

		// Check for overflow. 
		// Do a greater than compare operation.
			ovcheck = vcgtq_u8 (datasliceleft, ovflvec);

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
		resultslice = vaddq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8( &data3[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( pos_willoverflow(data2[x], ovlimit) ) {return 1;}
		data3[x] = param + data2[x];
	}

	return 0;

}



// param_arr_arr_none
char add_unsigned_char_5_simd_ovfl(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	static unsigned char ovcompvals[CHARSIMDSIZE] = {UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX};
	uint8x16_t datasliceleft, datasliceright, resultslice, ovcompslice, ovflvec;
	uint8x16_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Used to check for overflows.
	ovcompslice = vld1q_u8( ovcompvals);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u8( &data1[x]);
		datasliceright = vld1q_u8( &data2[x]);

		// Subtract the right hand value.
		ovflvec = vsubq_u8(ovcompslice, datasliceright);

		// Check for overflow. 
		// Do a greater than compare operation.
			ovcheck = vcgtq_u8 (datasliceleft, ovflvec);

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
		resultslice = vaddq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8( &data1[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( loop_willoverflow_unsigned_char(data1[x], data2[x]) ) {return 1;}
		data1[x] = data1[x] + data2[x];
	}

	return 0;

}



// param_arr_arr_arr
char add_unsigned_char_6_simd_ovfl(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2, unsigned char *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	static unsigned char ovcompvals[CHARSIMDSIZE] = {UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX, UCHAR_MAX};
	uint8x16_t datasliceleft, datasliceright, resultslice, ovcompslice, ovflvec;
	uint8x16_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Used to check for overflows.
	ovcompslice = vld1q_u8( ovcompvals);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u8( &data1[x]);
		datasliceright = vld1q_u8( &data2[x]);

		// Subtract the right hand value.
		ovflvec = vsubq_u8(ovcompslice, datasliceright);

		// Check for overflow. 
		// Do a greater than compare operation.
			ovcheck = vcgtq_u8 (datasliceleft, ovflvec);

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
		resultslice = vaddq_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u8( &data3[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( loop_willoverflow_unsigned_char(data1[x], data2[x]) ) {return 1;}
		data3[x] = data1[x] + data2[x];
	}

	return 0;

}
#endif

/*--------------------------------------------------------------------------- */

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
   This version is without overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
void add_signed_short_1_simd(Py_ssize_t arraylen, signed short *data1, signed short param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_signed_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s16( &data1[x]);
		// The actual SIMD operation. 
		resultslice = vaddq_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s16( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] + param;
	}

}



// param_arr_num_arr
void add_signed_short_2_simd(Py_ssize_t arraylen, signed short *data1, signed short param, signed short *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_signed_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s16( &data1[x]);
		// The actual SIMD operation.
		resultslice = vaddq_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s16( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] + param;
	}

}



// param_num_arr_none
void add_signed_short_3_simd(Py_ssize_t arraylen, signed short param, signed short *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_signed_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_s16( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s16( &data2[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param + data2[x];
	}

}



// param_num_arr_arr
void add_signed_short_4_simd(Py_ssize_t arraylen, signed short param, signed short *data2, signed short *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_signed_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_s16( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s16( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param + data2[x];
	}

}



// param_arr_arr_none
void add_signed_short_5_simd(Py_ssize_t arraylen, signed short *data1, signed short *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s16( &data1[x]);
		datasliceright = vld1q_s16( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s16( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] + data2[x];
	}

}



// param_arr_arr_arr
void add_signed_short_6_simd(Py_ssize_t arraylen, signed short *data1, signed short *data2, signed short *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x8_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s16( &data1[x]);
		datasliceright = vld1q_s16( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s16( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] + data2[x];
	}

}
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   This version supports overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   Returns 1 if overflow occurred, else returns 0.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
char add_signed_short_1_simd_ovfl(Py_ssize_t arraylen, signed short *data1, signed short param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed short ovlimit;
	int16x8_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint16x8_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// We don't need to do anything if param is zero.
	if (param == 0) {
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_signed_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// param is positive.
	if (param > 0) {

		// Used to calculate overflow.
		ovlimit = pos_ovlimit_signed_short(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_short(ovlimit);


		for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s16( &data1[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = vcgtq_s16 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s16(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s16( &data1[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( pos_willoverflow(data1[x], ovlimit) ) {return 1;}
			data1[x] = data1[x] + param; 
		}

	}


	// param is negative.
	if (param < 0) {

		// Used to calculate overflow.
		ovlimit = neg_ovlimit_signed_short(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_short(ovlimit);


		for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s16( &data1[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = vcltq_s16 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s16(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s16( &data1[x],  resultslice);

		}
	
		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( neg_willoverflow(data1[x], ovlimit) ) {return 1;}
			data1[x] = data1[x] + param; 
		}
	}

	return 0;

}



// param_arr_num_arr
char add_signed_short_2_simd_ovfl(Py_ssize_t arraylen, signed short *data1, signed short param, signed short *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed short ovlimit;
	int16x8_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint16x8_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// We don't need to do anything if param is zero, just copy the data.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x];
		}
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_signed_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// param is positive.
	if (param > 0) {

		// Used to calculate overflow.
		ovlimit = pos_ovlimit_signed_short(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_short(ovlimit);


		for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s16( &data1[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = vcgtq_s16 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s16(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s16( &data3[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( pos_willoverflow(data1[x], ovlimit) ) {return 1;}
			data3[x] = data1[x] + param; 
		}
	}


	// param is negative.
	if (param < 0) {

		// Used to calculate overflow.
		ovlimit = neg_ovlimit_signed_short(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_short(ovlimit);


		for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s16( &data1[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = vcltq_s16 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s16(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s16( &data3[x],  resultslice);

		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( neg_willoverflow(data1[x], ovlimit) ) {return 1;}
			data3[x] = data1[x] + param; 
		}
	}

	return 0;

}



// param_num_arr_none
char add_signed_short_3_simd_ovfl(Py_ssize_t arraylen, signed short param, signed short *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed short ovlimit;
	int16x8_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint16x8_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// We don't need to do anything if param is zero.
	if (param == 0) {
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_signed_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// param is positive.
	if (param > 0) {

		ovlimit = pos_ovlimit_signed_short(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_short(ovlimit);


		for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s16( &data2[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = vcgtq_s16 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s16(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s16( &data2[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( pos_willoverflow(data2[x], ovlimit) ) {return 1;}
			data2[x] = data2[x] + param; 
		}
	}


	// param is negative.
	if (param < 0) {

		// Used to calculate overflow.
		ovlimit = neg_ovlimit_signed_short(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_short(ovlimit);


		for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s16( &data2[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = vcltq_s16 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s16(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s16( &data2[x],  resultslice);

		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( neg_willoverflow(data2[x], ovlimit) ) {return 1;}
			data2[x] = data2[x] + param;
		}
	}

	return 0;

}



// param_num_arr_arr
char add_signed_short_4_simd_ovfl(Py_ssize_t arraylen, signed short param, signed short *data2, signed short *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed short ovlimit;
	int16x8_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint16x8_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// We don't need to do anything if param is zero, just copy the data.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
		data3[x] = data2[x];
		}
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_signed_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// param is positive.
	if (param > 0) {

		// Used to calculate overflow.
		ovlimit = pos_ovlimit_signed_short(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_short(ovlimit);


		for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s16( &data2[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = vcgtq_s16 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s16(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s16( &data3[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( pos_willoverflow(data2[x], ovlimit) ) {return 1;}
			data3[x] = data2[x] + param;
		}
	}


	// param is negative.
	if (param < 0) {

		// Used to calculate overflow.
		ovlimit = neg_ovlimit_signed_short(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_short(ovlimit);


		for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s16( &data2[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = vcltq_s16 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s16(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s16( &data3[x],  resultslice);

		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( neg_willoverflow(data2[x], ovlimit) ) {return 1;}
			data3[x] = data2[x] + param; 
		}
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
uint16x8_t initvec_unsigned_short(unsigned short initval) {

	unsigned int y;
	unsigned short initvals[SHORTSIMDSIZE];
	uint16x8_t simdvec;

	for (y = 0; y < SHORTSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = vld1q_u16((initvals));

	return simdvec;
}
#endif



/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   This version is without overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
void add_unsigned_short_1_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x8_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u16( &data1[x]);
		// The actual SIMD operation. 
		resultslice = vaddq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] + param;
	}

}



// param_arr_num_arr
void add_unsigned_short_2_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param, unsigned short *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x8_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u16( &data1[x]);
		// The actual SIMD operation.
		resultslice = vaddq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] + param;
	}

}



// param_num_arr_none
void add_unsigned_short_3_simd(Py_ssize_t arraylen, unsigned short param, unsigned short *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x8_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_unsigned_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_u16( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16( &data2[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param + data2[x];
	}

}



// param_num_arr_arr
void add_unsigned_short_4_simd(Py_ssize_t arraylen, unsigned short param, unsigned short *data2, unsigned short *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x8_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_unsigned_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_u16( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param + data2[x];
	}

}



// param_arr_arr_none
void add_unsigned_short_5_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x8_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u16( &data1[x]);
		datasliceright = vld1q_u16( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] + data2[x];
	}

}



// param_arr_arr_arr
void add_unsigned_short_6_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2, unsigned short *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x8_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u16( &data1[x]);
		datasliceright = vld1q_u16( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] + data2[x];
	}

}
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   This version is with overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
char add_unsigned_short_1_simd_ovfl(Py_ssize_t arraylen, unsigned short *data1, unsigned short param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned short ovlimit;
	uint16x8_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint16x8_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_short(param);


	// Used to calculate overflow.
	ovlimit = ovlimit_unsigned_short(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_short(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u16( &data1[x]);

		// Check for overflow. 
		// Do a greater than compare operation.
			ovcheck = vcgtq_u16 (datasliceleft, ovflvec);

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
		resultslice = vaddq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16( &data1[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( pos_willoverflow(data1[x], ovlimit) ) {return 1;}
		data1[x] = data1[x] + param;
	}

	return 0;

}



// param_arr_num_arr
char add_unsigned_short_2_simd_ovfl(Py_ssize_t arraylen, unsigned short *data1, unsigned short param, unsigned short *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned short ovlimit;
	uint16x8_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint16x8_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_short(param);


	// Used to calculate overflow.
	ovlimit = ovlimit_unsigned_short(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_short(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u16( &data1[x]);

		// Check for overflow. 
		// Do a greater than compare operation.
			ovcheck = vcgtq_u16 (datasliceleft, ovflvec);

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
		resultslice = vaddq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16( &data3[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( pos_willoverflow(data1[x], ovlimit) ) {return 1;}
		data3[x] = data1[x] + param;
	}

	return 0;

}



// param_num_arr_none
char add_unsigned_short_3_simd_ovfl(Py_ssize_t arraylen, unsigned short param, unsigned short *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned short ovlimit;
	uint16x8_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint16x8_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_short(param);

	// Used to calculate overflow.
	ovlimit = ovlimit_unsigned_short(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_short(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u16( &data2[x]);

		// Check for overflow. 
		// Do a greater than compare operation.
			ovcheck = vcgtq_u16 (datasliceleft, ovflvec);

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
		resultslice = vaddq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16( &data2[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( pos_willoverflow(data2[x], ovlimit) ) {return 1;}
		data2[x] = param + data2[x];
	}

	return 0;

}



// param_num_arr_arr
char add_unsigned_short_4_simd_ovfl(Py_ssize_t arraylen, unsigned short param, unsigned short *data2, unsigned short *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned short ovlimit;
	uint16x8_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint16x8_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_short(param);


	// Used to calculate overflow.
	ovlimit = ovlimit_unsigned_short(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_short(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u16( &data2[x]);

		// Check for overflow. 
		// Do a greater than compare operation.
			ovcheck = vcgtq_u16 (datasliceleft, ovflvec);

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
		resultslice = vaddq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16( &data3[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( pos_willoverflow(data2[x], ovlimit) ) {return 1;}
		data3[x] = param + data2[x];
	}

	return 0;

}



// param_arr_arr_none
char add_unsigned_short_5_simd_ovfl(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	static unsigned short ovcompvals[SHORTSIMDSIZE] = {USHRT_MAX, USHRT_MAX, USHRT_MAX, USHRT_MAX, USHRT_MAX, USHRT_MAX, USHRT_MAX, USHRT_MAX};
	uint16x8_t datasliceleft, datasliceright, resultslice, ovcompslice, ovflvec;
	uint16x8_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Used to check for overflows.
	ovcompslice = vld1q_u16( ovcompvals);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u16( &data1[x]);
		datasliceright = vld1q_u16( &data2[x]);

		// Subtract the right hand value.
		ovflvec = vsubq_u16(ovcompslice, datasliceright);

		// Check for overflow. 
		// Do a greater than compare operation.
			ovcheck = vcgtq_u16 (datasliceleft, ovflvec);

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
		resultslice = vaddq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16( &data1[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( loop_willoverflow_unsigned_short(data1[x], data2[x]) ) {return 1;}
		data1[x] = data1[x] + data2[x];
	}

	return 0;

}



// param_arr_arr_arr
char add_unsigned_short_6_simd_ovfl(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2, unsigned short *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	static unsigned short ovcompvals[SHORTSIMDSIZE] = {USHRT_MAX, USHRT_MAX, USHRT_MAX, USHRT_MAX, USHRT_MAX, USHRT_MAX, USHRT_MAX, USHRT_MAX};
	uint16x8_t datasliceleft, datasliceright, resultslice, ovcompslice, ovflvec;
	uint16x8_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Used to check for overflows.
	ovcompslice = vld1q_u16( ovcompvals);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u16( &data1[x]);
		datasliceright = vld1q_u16( &data2[x]);

		// Subtract the right hand value.
		ovflvec = vsubq_u16(ovcompslice, datasliceright);

		// Check for overflow. 
		// Do a greater than compare operation.
			ovcheck = vcgtq_u16 (datasliceleft, ovflvec);

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
		resultslice = vaddq_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u16( &data3[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( loop_willoverflow_unsigned_short(data1[x], data2[x]) ) {return 1;}
		data3[x] = data1[x] + data2[x];
	}

	return 0;

}
#endif

/*--------------------------------------------------------------------------- */

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
   This version is without overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
void add_signed_int_1_simd(Py_ssize_t arraylen, signed int *data1, signed int param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_signed_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s32( &data1[x]);
		// The actual SIMD operation. 
		resultslice = vaddq_s32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s32( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] + param;
	}

}



// param_arr_num_arr
void add_signed_int_2_simd(Py_ssize_t arraylen, signed int *data1, signed int param, signed int *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_signed_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s32( &data1[x]);
		// The actual SIMD operation.
		resultslice = vaddq_s32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s32( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] + param;
	}

}



// param_num_arr_none
void add_signed_int_3_simd(Py_ssize_t arraylen, signed int param, signed int *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_signed_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_s32( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_s32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s32( &data2[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param + data2[x];
	}

}



// param_num_arr_arr
void add_signed_int_4_simd(Py_ssize_t arraylen, signed int param, signed int *data2, signed int *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_signed_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_s32( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_s32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s32( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param + data2[x];
	}

}



// param_arr_arr_none
void add_signed_int_5_simd(Py_ssize_t arraylen, signed int *data1, signed int *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s32( &data1[x]);
		datasliceright = vld1q_s32( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_s32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s32( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] + data2[x];
	}

}



// param_arr_arr_arr
void add_signed_int_6_simd(Py_ssize_t arraylen, signed int *data1, signed int *data2, signed int *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int32x4_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_s32( &data1[x]);
		datasliceright = vld1q_s32( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_s32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_s32( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] + data2[x];
	}

}
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   This version supports overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   Returns 1 if overflow occurred, else returns 0.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
char add_signed_int_1_simd_ovfl(Py_ssize_t arraylen, signed int *data1, signed int param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed int ovlimit;
	int32x4_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint32x4_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// We don't need to do anything if param is zero.
	if (param == 0) {
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_signed_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// param is positive.
	if (param > 0) {

		// Used to calculate overflow.
		ovlimit = pos_ovlimit_signed_int(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_int(ovlimit);


		for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s32( &data1[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = vcgtq_s32 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s32(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s32( &data1[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( pos_willoverflow(data1[x], ovlimit) ) {return 1;}
			data1[x] = data1[x] + param; 
		}

	}


	// param is negative.
	if (param < 0) {

		// Used to calculate overflow.
		ovlimit = neg_ovlimit_signed_int(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_int(ovlimit);


		for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s32( &data1[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = vcltq_s32 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s32(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s32( &data1[x],  resultslice);

		}
	
		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( neg_willoverflow(data1[x], ovlimit) ) {return 1;}
			data1[x] = data1[x] + param; 
		}
	}

	return 0;

}



// param_arr_num_arr
char add_signed_int_2_simd_ovfl(Py_ssize_t arraylen, signed int *data1, signed int param, signed int *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed int ovlimit;
	int32x4_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint32x4_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// We don't need to do anything if param is zero, just copy the data.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x];
		}
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_signed_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// param is positive.
	if (param > 0) {

		// Used to calculate overflow.
		ovlimit = pos_ovlimit_signed_int(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_int(ovlimit);


		for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s32( &data1[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = vcgtq_s32 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s32(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s32( &data3[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( pos_willoverflow(data1[x], ovlimit) ) {return 1;}
			data3[x] = data1[x] + param; 
		}
	}


	// param is negative.
	if (param < 0) {

		// Used to calculate overflow.
		ovlimit = neg_ovlimit_signed_int(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_int(ovlimit);


		for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s32( &data1[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = vcltq_s32 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s32(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s32( &data3[x],  resultslice);

		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( neg_willoverflow(data1[x], ovlimit) ) {return 1;}
			data3[x] = data1[x] + param; 
		}
	}

	return 0;

}



// param_num_arr_none
char add_signed_int_3_simd_ovfl(Py_ssize_t arraylen, signed int param, signed int *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed int ovlimit;
	int32x4_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint32x4_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// We don't need to do anything if param is zero.
	if (param == 0) {
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_signed_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// param is positive.
	if (param > 0) {

		ovlimit = pos_ovlimit_signed_int(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_int(ovlimit);


		for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s32( &data2[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = vcgtq_s32 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s32(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s32( &data2[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( pos_willoverflow(data2[x], ovlimit) ) {return 1;}
			data2[x] = data2[x] + param; 
		}
	}


	// param is negative.
	if (param < 0) {

		// Used to calculate overflow.
		ovlimit = neg_ovlimit_signed_int(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_int(ovlimit);


		for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s32( &data2[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = vcltq_s32 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s32(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s32( &data2[x],  resultslice);

		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( neg_willoverflow(data2[x], ovlimit) ) {return 1;}
			data2[x] = data2[x] + param;
		}
	}

	return 0;

}



// param_num_arr_arr
char add_signed_int_4_simd_ovfl(Py_ssize_t arraylen, signed int param, signed int *data2, signed int *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed int ovlimit;
	int32x4_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint32x4_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// We don't need to do anything if param is zero, just copy the data.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
		data3[x] = data2[x];
		}
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_signed_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// param is positive.
	if (param > 0) {

		// Used to calculate overflow.
		ovlimit = pos_ovlimit_signed_int(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_int(ovlimit);


		for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s32( &data2[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = vcgtq_s32 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s32(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s32( &data3[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( pos_willoverflow(data2[x], ovlimit) ) {return 1;}
			data3[x] = data2[x] + param;
		}
	}


	// param is negative.
	if (param < 0) {

		// Used to calculate overflow.
		ovlimit = neg_ovlimit_signed_int(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_signed_int(ovlimit);


		for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1q_s32( &data2[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = vcltq_s32 (datasliceleft, ovflvec);

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
			resultslice = vaddq_s32(datasliceleft, datasliceright);

			// Store the result.
			vst1q_s32( &data3[x],  resultslice);

		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( neg_willoverflow(data2[x], ovlimit) ) {return 1;}
			data3[x] = data2[x] + param; 
		}
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
uint32x4_t initvec_unsigned_int(unsigned int initval) {

	unsigned int y;
	unsigned int initvals[INTSIMDSIZE];
	uint32x4_t simdvec;

	for (y = 0; y < INTSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = vld1q_u32((initvals));

	return simdvec;
}
#endif



/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   This version is without overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
void add_unsigned_int_1_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u32( &data1[x]);
		// The actual SIMD operation. 
		resultslice = vaddq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] + param;
	}

}



// param_arr_num_arr
void add_unsigned_int_2_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param, unsigned int *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u32( &data1[x]);
		// The actual SIMD operation.
		resultslice = vaddq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] + param;
	}

}



// param_num_arr_none
void add_unsigned_int_3_simd(Py_ssize_t arraylen, unsigned int param, unsigned int *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_unsigned_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_u32( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32( &data2[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param + data2[x];
	}

}



// param_num_arr_arr
void add_unsigned_int_4_simd(Py_ssize_t arraylen, unsigned int param, unsigned int *data2, unsigned int *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_unsigned_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_u32( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param + data2[x];
	}

}



// param_arr_arr_none
void add_unsigned_int_5_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x4_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u32( &data1[x]);
		datasliceright = vld1q_u32( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] + data2[x];
	}

}



// param_arr_arr_arr
void add_unsigned_int_6_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2, unsigned int *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint32x4_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u32( &data1[x]);
		datasliceright = vld1q_u32( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] + data2[x];
	}

}
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   This version is with overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
char add_unsigned_int_1_simd_ovfl(Py_ssize_t arraylen, unsigned int *data1, unsigned int param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned int ovlimit;
	uint32x4_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint32x4_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_int(param);


	// Used to calculate overflow.
	ovlimit = ovlimit_unsigned_int(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_int(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u32( &data1[x]);

		// Check for overflow. 
		// Do a greater than compare operation.
			ovcheck = vcgtq_u32 (datasliceleft, ovflvec);

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
		resultslice = vaddq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32( &data1[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( pos_willoverflow(data1[x], ovlimit) ) {return 1;}
		data1[x] = data1[x] + param;
	}

	return 0;

}



// param_arr_num_arr
char add_unsigned_int_2_simd_ovfl(Py_ssize_t arraylen, unsigned int *data1, unsigned int param, unsigned int *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned int ovlimit;
	uint32x4_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint32x4_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_int(param);


	// Used to calculate overflow.
	ovlimit = ovlimit_unsigned_int(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_int(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u32( &data1[x]);

		// Check for overflow. 
		// Do a greater than compare operation.
			ovcheck = vcgtq_u32 (datasliceleft, ovflvec);

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
		resultslice = vaddq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32( &data3[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( pos_willoverflow(data1[x], ovlimit) ) {return 1;}
		data3[x] = data1[x] + param;
	}

	return 0;

}



// param_num_arr_none
char add_unsigned_int_3_simd_ovfl(Py_ssize_t arraylen, unsigned int param, unsigned int *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned int ovlimit;
	uint32x4_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint32x4_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_int(param);

	// Used to calculate overflow.
	ovlimit = ovlimit_unsigned_int(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_int(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u32( &data2[x]);

		// Check for overflow. 
		// Do a greater than compare operation.
			ovcheck = vcgtq_u32 (datasliceleft, ovflvec);

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
		resultslice = vaddq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32( &data2[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( pos_willoverflow(data2[x], ovlimit) ) {return 1;}
		data2[x] = param + data2[x];
	}

	return 0;

}



// param_num_arr_arr
char add_unsigned_int_4_simd_ovfl(Py_ssize_t arraylen, unsigned int param, unsigned int *data2, unsigned int *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned int ovlimit;
	uint32x4_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint32x4_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_int(param);


	// Used to calculate overflow.
	ovlimit = ovlimit_unsigned_int(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_int(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u32( &data2[x]);

		// Check for overflow. 
		// Do a greater than compare operation.
			ovcheck = vcgtq_u32 (datasliceleft, ovflvec);

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
		resultslice = vaddq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32( &data3[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( pos_willoverflow(data2[x], ovlimit) ) {return 1;}
		data3[x] = param + data2[x];
	}

	return 0;

}



// param_arr_arr_none
char add_unsigned_int_5_simd_ovfl(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	static unsigned int ovcompvals[INTSIMDSIZE] = {UINT_MAX, UINT_MAX, UINT_MAX, UINT_MAX};
	uint32x4_t datasliceleft, datasliceright, resultslice, ovcompslice, ovflvec;
	uint32x4_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Used to check for overflows.
	ovcompslice = vld1q_u32( ovcompvals);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u32( &data1[x]);
		datasliceright = vld1q_u32( &data2[x]);

		// Subtract the right hand value.
		ovflvec = vsubq_u32(ovcompslice, datasliceright);

		// Check for overflow. 
		// Do a greater than compare operation.
			ovcheck = vcgtq_u32 (datasliceleft, ovflvec);

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
		resultslice = vaddq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32( &data1[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( loop_willoverflow_unsigned_int(data1[x], data2[x]) ) {return 1;}
		data1[x] = data1[x] + data2[x];
	}

	return 0;

}



// param_arr_arr_arr
char add_unsigned_int_6_simd_ovfl(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2, unsigned int *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	static unsigned int ovcompvals[INTSIMDSIZE] = {UINT_MAX, UINT_MAX, UINT_MAX, UINT_MAX};
	uint32x4_t datasliceleft, datasliceright, resultslice, ovcompslice, ovflvec;
	uint32x4_t ovcheck;
	uint64x2_t veccombine;
	uint64_t highresult, lowresult;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Used to check for overflows.
	ovcompslice = vld1q_u32( ovcompvals);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_u32( &data1[x]);
		datasliceright = vld1q_u32( &data2[x]);

		// Subtract the right hand value.
		ovflvec = vsubq_u32(ovcompslice, datasliceright);

		// Check for overflow. 
		// Do a greater than compare operation.
			ovcheck = vcgtq_u32 (datasliceleft, ovflvec);

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
		resultslice = vaddq_u32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_u32( &data3[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( loop_willoverflow_unsigned_int(data1[x], data2[x]) ) {return 1;}
		data3[x] = data1[x] + data2[x];
	}

	return 0;

}
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specifired value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
*/
#if defined(AF_HASSIMD_ARM_AARCH64)
float32x4_t initvec_float(float initval) {

	unsigned int y;
	float initvals[FLOATSIMDSIZE];
	float32x4_t simdvec;

	for (y = 0; y < FLOATSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = vld1q_f32((initvals));

	return simdvec;
}
#endif



/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   This version is without overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARM_AARCH64)
void add_float_1_simd(Py_ssize_t arraylen, float *data1, float param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_float(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_f32( &data1[x]);
		// The actual SIMD operation. 
		resultslice = vaddq_f32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_f32( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] + param;
	}

}



// param_arr_num_arr
void add_float_2_simd(Py_ssize_t arraylen, float *data1, float param, float *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_float(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_f32( &data1[x]);
		// The actual SIMD operation.
		resultslice = vaddq_f32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_f32( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] + param;
	}

}



// param_num_arr_none
void add_float_3_simd(Py_ssize_t arraylen, float param, float *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_float(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_f32( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_f32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_f32( &data2[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param + data2[x];
	}

}



// param_num_arr_arr
void add_float_4_simd(Py_ssize_t arraylen, float param, float *data2, float *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_float(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1q_f32( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_f32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_f32( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param + data2[x];
	}

}



// param_arr_arr_none
void add_float_5_simd(Py_ssize_t arraylen, float *data1, float *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x4_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_f32( &data1[x]);
		datasliceright = vld1q_f32( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_f32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_f32( &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] + data2[x];
	}

}



// param_arr_arr_arr
void add_float_6_simd(Py_ssize_t arraylen, float *data1, float *data2, float *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	float32x4_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1q_f32( &data1[x]);
		datasliceright = vld1q_f32( &data2[x]);
		// The actual SIMD operation.
		resultslice = vaddq_f32(datasliceleft, datasliceright);
		// Store the result.
		vst1q_f32( &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] + data2[x];
	}

}
#endif

/*--------------------------------------------------------------------------- */
