//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   mul_simd_armv7.c
// Purpose:  Calculate the mul of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     8-Oct-2019
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
#ifdef AF_HASSIMD_ARMv7_32BIT
#include "arm_neon.h"
#endif

#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// Auto generated code goes below.

// Function specific macros and other definitions.
#include "mul_defs.h"

// Function specific macros and other definitions.
#include "mul_defs.h"

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
   This version is without overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARMv7_32BIT)
void mul_signed_char_1_simd(Py_ssize_t arraylen, signed char *data1, signed char param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x8_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_signed_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s8( &data1[x]);
		// The actual SIMD operation. 
		resultslice = vmul_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1_s8( &data1[x],  resultslice);
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

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x8_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_signed_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s8( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1_s8( &data3[x],  resultslice);
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

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x8_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_signed_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_s8( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1_s8( &data2[x],  resultslice);
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

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int8x8_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_signed_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_s8( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1_s8( &data3[x],  resultslice);
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

	int8x8_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s8( &data1[x]);
		datasliceright = vld1_s8( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1_s8( &data1[x],  resultslice);
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

	int8x8_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s8( &data1[x]);
		datasliceright = vld1_s8( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_s8(datasliceleft, datasliceright);
		// Store the result.
		vst1_s8( &data3[x],  resultslice);
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
   This version supports overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   Returns 1 if overflow occurred, else returns 0.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARMv7_32BIT)
char mul_signed_char_1_simd_ovfl(Py_ssize_t arraylen, signed char *data1, signed char param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed char ovlimit1, ovlimit2;
	int8x8_t datasliceleft, datasliceright, resultslice, ovflvec1, ovflvec2;
	uint8x8_t ovcheck1, ovcheck2;
	


	// If the parameter is zero, we can take a shortcut.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = 0; 
		}
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_signed_char(param);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);


	// Signed integers do not have a symetrical range (e.g. -128 to 127). 
	if (param == -1) {
		// This is used for detecting a potential overflow condition.
		ovflvec1 = initvec_signed_char(SCHAR_MIN);

		for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1_s8( &data1[x]);

			// Check for overflow. 
			// Do an equal compare operation.
			ovcheck1 = vceq_s8 (datasliceleft, ovflvec1); 
			// Check for overflow. 
			if (!(vreinterpret_u64_u8(ovcheck1) == 0x0000000000000000)){
				return 1;
			}
			// The actual SIMD operation. 
			resultslice = vmul_s8(datasliceleft, datasliceright);

			// Store the result.
			vst1_s8( &data1[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( minusone_loop_willoverflow_signed_char(data1[x]) ) {return 1;}
			data1[x] = data1[x] * param; 
		}

	} else {


		// Used to calculate overflow.
		ovlimit1 = max_ovlimit_signed_char(param);
		ovlimit2 = min_ovlimit_signed_char(param);

		// This is used for detecting a potential overflow condition.
		ovflvec1 = initvec_signed_char(ovlimit1);
		ovflvec2 = initvec_signed_char(ovlimit2);

		// param is positive.
		if (param > 0) {

			for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
				// Load the data into the vector register.
				datasliceleft = vld1_s8( &data1[x]);

				// Check for overflow. 
				// Check for overflow.
			ovcheck1 = vcgt_s8 (datasliceleft, ovflvec1);
			ovcheck2 = vclt_s8 (datasliceleft, ovflvec2); 
			// Check for overflow. 
			if ((!(vreinterpret_u64_u8(ovcheck1) == 0x0000000000000000)) ||
				(!(vreinterpret_u64_u8(ovcheck2) == 0x0000000000000000))){
					return 1;
				}

				// The actual SIMD operation. 
				resultslice = vmul_s8(datasliceleft, datasliceright);

				// Store the result.
				vst1_s8( &data1[x],  resultslice);
			}

			// Handle the values left over at the end of the array.
			for (x = alignedlength; x < arraylen; x++) {
				if ( pos_willoverflow(data1[x], ovlimit1, ovlimit2) ) {return 1;}
				data1[x] = data1[x] * param; 
			}

		}


		// param is negative.
		if (param < 0) {

			for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
				// Load the data into the vector register.
				datasliceleft = vld1_s8( &data1[x]);

				// Check for overflow. 
				// Check for overflow.
			ovcheck1 = vclt_s8 (datasliceleft, ovflvec1);
			ovcheck2 = vcgt_s8 (datasliceleft, ovflvec2); 
			// Check for overflow. 
			if ((!(vreinterpret_u64_u8(ovcheck1) == 0x0000000000000000)) ||
				(!(vreinterpret_u64_u8(ovcheck2) == 0x0000000000000000))){
					return 1;
				}

				// The actual SIMD operation. 
				resultslice = vmul_s8(datasliceleft, datasliceright);

				// Store the result.
				vst1_s8( &data1[x],  resultslice);

			}
		
			// Handle the values left over at the end of the array.
			for (x = alignedlength; x < arraylen; x++) {
				if ( neg_willoverflow(data1[x], ovlimit1, ovlimit2) ) {return 1;}
				data1[x] = data1[x] * param; 
			}
		}
	}

	return 0;

}



// param_arr_num_arr
char mul_signed_char_2_simd_ovfl(Py_ssize_t arraylen, signed char *data1, signed char param, signed char *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed char ovlimit1, ovlimit2;
	int8x8_t datasliceleft, datasliceright, resultslice, ovflvec1, ovflvec2;
	uint8x8_t ovcheck1, ovcheck2;
	


	// If the parameter is zero, we can take a shortcut.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = 0; 
		}
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_signed_char(param);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);


	// Signed integers do not have a symetrical range (e.g. -128 to 127). 
	if (param == -1) {
		// This is used for detecting a potential overflow condition.
		ovflvec1 = initvec_signed_char(SCHAR_MIN);

		for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1_s8( &data1[x]);

			// Check for overflow. 
			// Do an equal compare operation.
			ovcheck1 = vceq_s8 (datasliceleft, ovflvec1); 
			// Check for overflow. 
			if (!(vreinterpret_u64_u8(ovcheck1) == 0x0000000000000000)){
				return 1;
			}
			// The actual SIMD operation. 
			resultslice = vmul_s8(datasliceleft, datasliceright);

			// Store the result.
			vst1_s8( &data3[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( minusone_loop_willoverflow_signed_char(data1[x]) ) {return 1;}
			data3[x] = data1[x] * param; 
		}

	} else {


		// Used to calculate overflow.
		ovlimit1 = max_ovlimit_signed_char(param);
		ovlimit2 = min_ovlimit_signed_char(param);

		// This is used for detecting a potential overflow condition.
		ovflvec1 = initvec_signed_char(ovlimit1);
		ovflvec2 = initvec_signed_char(ovlimit2);

		// param is positive.
		if (param > 0) {

			for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
				// Load the data into the vector register.
				datasliceleft = vld1_s8( &data1[x]);

				// Check for overflow. 
				// Check for overflow.
			ovcheck1 = vcgt_s8 (datasliceleft, ovflvec1);
			ovcheck2 = vclt_s8 (datasliceleft, ovflvec2); 
			// Check for overflow. 
			if ((!(vreinterpret_u64_u8(ovcheck1) == 0x0000000000000000)) ||
				(!(vreinterpret_u64_u8(ovcheck2) == 0x0000000000000000))){
					return 1;
				}

				// The actual SIMD operation. 
				resultslice = vmul_s8(datasliceleft, datasliceright);

				// Store the result.
				vst1_s8( &data3[x],  resultslice);
			}

			// Handle the values left over at the end of the array.
			for (x = alignedlength; x < arraylen; x++) {
				if ( pos_willoverflow(data1[x], ovlimit1, ovlimit2) ) {return 1;}
				data3[x] = data1[x] * param; 
			}

		}


		// param is negative.
		if (param < 0) {

			for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
				// Load the data into the vector register.
				datasliceleft = vld1_s8( &data1[x]);

				// Check for overflow. 
				// Check for overflow.
			ovcheck1 = vclt_s8 (datasliceleft, ovflvec1);
			ovcheck2 = vcgt_s8 (datasliceleft, ovflvec2); 
			// Check for overflow. 
			if ((!(vreinterpret_u64_u8(ovcheck1) == 0x0000000000000000)) ||
				(!(vreinterpret_u64_u8(ovcheck2) == 0x0000000000000000))){
					return 1;
				}

				// The actual SIMD operation. 
				resultslice = vmul_s8(datasliceleft, datasliceright);

				// Store the result.
				vst1_s8( &data3[x],  resultslice);

			}
		
			// Handle the values left over at the end of the array.
			for (x = alignedlength; x < arraylen; x++) {
				if ( neg_willoverflow(data1[x], ovlimit1, ovlimit2) ) {return 1;}
				data3[x] = data1[x] * param; 
			}
		}
	}

	return 0;
	
}



// param_num_arr_none
char mul_signed_char_3_simd_ovfl(Py_ssize_t arraylen, signed char param, signed char *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed char ovlimit1, ovlimit2;
	int8x8_t datasliceleft, datasliceright, resultslice, ovflvec1, ovflvec2;
	uint8x8_t ovcheck1, ovcheck2;
	


	// If the parameter is zero, we can take a shortcut.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = 0; 
		}
		return 0;
	}


	// Initialise the param values.
	datasliceleft = initvec_signed_char(param);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);


	// Signed integers do not have a symetrical range (e.g. -128 to 127). 
	if (param == -1) {
		// This is used for detecting a potential overflow condition.
		ovflvec1 = initvec_signed_char(SCHAR_MIN);

		for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
			// Load the data into the vector register.
			datasliceright = vld1_s8( &data2[x]);

			// Check for overflow. 
			// Do an equal compare operation.
			ovcheck1 = vceq_s8 (datasliceright, ovflvec1); 
			// Check for overflow. 
			if (!(vreinterpret_u64_u8(ovcheck1) == 0x0000000000000000)){
				return 1;
			}
			// The actual SIMD operation. 
			resultslice = vmul_s8(datasliceleft, datasliceright);

			// Store the result.
			vst1_s8( &data2[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( minusone_loop_willoverflow_signed_char(data2[x]) ) {return 1;}
			data2[x] = param * data2[x]; 
		}

	} else {


		// Used to calculate overflow.
		ovlimit1 = max_ovlimit_signed_char(param);
		ovlimit2 = min_ovlimit_signed_char(param);

		// This is used for detecting a potential overflow condition.
		ovflvec1 = initvec_signed_char(ovlimit1);
		ovflvec2 = initvec_signed_char(ovlimit2);

		// param is positive.
		if (param > 0) {

			for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
				// Load the data into the vector register.
				datasliceright = vld1_s8( &data2[x]);

				// Check for overflow. 
				// Check for overflow.
			ovcheck1 = vcgt_s8 (datasliceright, ovflvec1);
			ovcheck2 = vclt_s8 (datasliceright, ovflvec2); 
			// Check for overflow. 
			if ((!(vreinterpret_u64_u8(ovcheck1) == 0x0000000000000000)) ||
				(!(vreinterpret_u64_u8(ovcheck2) == 0x0000000000000000))){
					return 1;
				}

				// The actual SIMD operation. 
				resultslice = vmul_s8(datasliceleft, datasliceright);

				// Store the result.
				vst1_s8( &data2[x],  resultslice);
			}

			// Handle the values left over at the end of the array.
			for (x = alignedlength; x < arraylen; x++) {
				if ( pos_willoverflow(data2[x], ovlimit1, ovlimit2) ) {return 1;}
				data2[x] = param * data2[x]; 
			}

		}


		// param is negative.
		if (param < 0) {

			for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
				// Load the data into the vector register.
				datasliceright = vld1_s8( &data2[x]);

				// Check for overflow. 
				// Check for overflow.
			ovcheck1 = vclt_s8 (datasliceright, ovflvec1);
			ovcheck2 = vcgt_s8 (datasliceright, ovflvec2); 
			// Check for overflow. 
			if ((!(vreinterpret_u64_u8(ovcheck1) == 0x0000000000000000)) ||
				(!(vreinterpret_u64_u8(ovcheck2) == 0x0000000000000000))){
					return 1;
				}

				// The actual SIMD operation. 
				resultslice = vmul_s8(datasliceleft, datasliceright);

				// Store the result.
				vst1_s8( &data2[x],  resultslice);

			}
		
			// Handle the values left over at the end of the array.
			for (x = alignedlength; x < arraylen; x++) {
				if ( neg_willoverflow(data2[x], ovlimit1, ovlimit2) ) {return 1;}
				data2[x] = param * data2[x]; 
			}
		}
	}

	return 0;

}



// param_num_arr_arr
char mul_signed_char_4_simd_ovfl(Py_ssize_t arraylen, signed char param, signed char *data2, signed char *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed char ovlimit1, ovlimit2;
	int8x8_t datasliceleft, datasliceright, resultslice, ovflvec1, ovflvec2;
	uint8x8_t ovcheck1, ovcheck2;
	


	// If the parameter is zero, we can take a shortcut.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = 0; 
		}
		return 0;
	}


	// Initialise the param values.
	datasliceleft = initvec_signed_char(param);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);


	// Signed integers do not have a symetrical range (e.g. -128 to 127). 
	if (param == -1) {
		// This is used for detecting a potential overflow condition.
		ovflvec1 = initvec_signed_char(SCHAR_MIN);

		for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
			// Load the data into the vector register.
			datasliceright = vld1_s8( &data2[x]);

			// Check for overflow. 
			// Do an equal compare operation.
			ovcheck1 = vceq_s8 (datasliceright, ovflvec1); 
			// Check for overflow. 
			if (!(vreinterpret_u64_u8(ovcheck1) == 0x0000000000000000)){
				return 1;
			}
			// The actual SIMD operation. 
			resultslice = vmul_s8(datasliceleft, datasliceright);

			// Store the result.
			vst1_s8( &data3[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( minusone_loop_willoverflow_signed_char(data2[x]) ) {return 1;}
			data3[x] = param * data2[x]; 
		}

	} else {


		// Used to calculate overflow.
		ovlimit1 = max_ovlimit_signed_char(param);
		ovlimit2 = min_ovlimit_signed_char(param);

		// This is used for detecting a potential overflow condition.
		ovflvec1 = initvec_signed_char(ovlimit1);
		ovflvec2 = initvec_signed_char(ovlimit2);

		// param is positive.
		if (param > 0) {

			for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
				// Load the data into the vector register.
				datasliceright = vld1_s8( &data2[x]);

				// Check for overflow. 
				// Check for overflow.
			ovcheck1 = vcgt_s8 (datasliceright, ovflvec1);
			ovcheck2 = vclt_s8 (datasliceright, ovflvec2); 
			// Check for overflow. 
			if ((!(vreinterpret_u64_u8(ovcheck1) == 0x0000000000000000)) ||
				(!(vreinterpret_u64_u8(ovcheck2) == 0x0000000000000000))){
					return 1;
				}

				// The actual SIMD operation. 
				resultslice = vmul_s8(datasliceleft, datasliceright);

				// Store the result.
				vst1_s8( &data3[x],  resultslice);
			}

			// Handle the values left over at the end of the array.
			for (x = alignedlength; x < arraylen; x++) {
				if ( pos_willoverflow(data2[x], ovlimit1, ovlimit2) ) {return 1;}
				data3[x] = param * data2[x]; 
			}

		}


		// param is negative.
		if (param < 0) {

			for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
				// Load the data into the vector register.
				datasliceright = vld1_s8( &data2[x]);

				// Check for overflow. 
				// Check for overflow.
			ovcheck1 = vclt_s8 (datasliceright, ovflvec1);
			ovcheck2 = vcgt_s8 (datasliceright, ovflvec2); 
			// Check for overflow. 
			if ((!(vreinterpret_u64_u8(ovcheck1) == 0x0000000000000000)) ||
				(!(vreinterpret_u64_u8(ovcheck2) == 0x0000000000000000))){
					return 1;
				}

				// The actual SIMD operation. 
				resultslice = vmul_s8(datasliceleft, datasliceright);

				// Store the result.
				vst1_s8( &data3[x],  resultslice);

			}
		
			// Handle the values left over at the end of the array.
			for (x = alignedlength; x < arraylen; x++) {
				if ( neg_willoverflow(data2[x], ovlimit1, ovlimit2) ) {return 1;}
				data3[x] = param * data2[x]; 
			}
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
#if defined(AF_HASSIMD_ARMv7_32BIT)
uint8x8_t initvec_unsigned_char(unsigned char initval) {

	unsigned int y;
	unsigned char initvals[CHARSIMDSIZE];
	uint8x8_t simdvec;

	for (y = 0; y < CHARSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = vld1_u8((initvals));

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
#if defined(AF_HASSIMD_ARMv7_32BIT)
void mul_unsigned_char_1_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x8_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u8( &data1[x]);
		// The actual SIMD operation. 
		resultslice = vmul_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1_u8( &data1[x],  resultslice);
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

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x8_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u8( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1_u8( &data3[x],  resultslice);
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

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x8_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_unsigned_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_u8( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1_u8( &data2[x],  resultslice);
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

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint8x8_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_unsigned_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_u8( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1_u8( &data3[x],  resultslice);
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

	uint8x8_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u8( &data1[x]);
		datasliceright = vld1_u8( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1_u8( &data1[x],  resultslice);
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

	uint8x8_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u8( &data1[x]);
		datasliceright = vld1_u8( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1_u8( &data3[x],  resultslice);
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
   This version is with overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARMv7_32BIT)
char mul_unsigned_char_1_simd_ovfl(Py_ssize_t arraylen, unsigned char *data1, unsigned char param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned char ovlimit;
	uint8x8_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint8x8_t ovcheck1;
	


	// If the parameter is zero, we can take a shortcut.
	// This also avoids division by zero during the overflow check.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = 0; 
		}
		return 0;
	}


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_char(param);


	// Used to calculate overflow.
	ovlimit = uint_ovlimit_unsigned_char(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_char(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u8( &data1[x]);

		// Check for overflow. 
		// Check for overflow.
		ovcheck1 = vcgt_u8 (datasliceleft, ovflvec); 
			// Check for overflow. 
			if (!(vreinterpret_u64_u8(ovcheck1) == 0x0000000000000000)){
			return 1;
		}

		// The actual SIMD operation. 
		resultslice = vmul_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1_u8( &data1[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( uint_willoverflow(data1[x], ovlimit) ) {return 1;}
		data1[x] = data1[x] * param;
	}

	return 0;

}


// param_arr_num_arr
char mul_unsigned_char_2_simd_ovfl(Py_ssize_t arraylen, unsigned char *data1, unsigned char param, unsigned char *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned char ovlimit;
	uint8x8_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint8x8_t ovcheck1;
	


	// If the parameter is zero, we can take a shortcut.
	// This also avoids division by zero during the overflow check.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = 0; 
		}
		return 0;
	}


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_char(param);

	// Used to calculate overflow.
	ovlimit = uint_ovlimit_unsigned_char(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_char(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u8( &data1[x]);

		// Check for overflow. 
		// Check for overflow.
		ovcheck1 = vcgt_u8 (datasliceleft, ovflvec); 
			// Check for overflow. 
			if (!(vreinterpret_u64_u8(ovcheck1) == 0x0000000000000000)){
			return 1;
		}

		// The actual SIMD operation.
		resultslice = vmul_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1_u8( &data3[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( uint_willoverflow(data1[x], ovlimit) ) {return 1;}
		data3[x] = data1[x] * param;
	}

	return 0;

}


// param_num_arr_none
char mul_unsigned_char_3_simd_ovfl(Py_ssize_t arraylen, unsigned char param, unsigned char *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned char ovlimit;
	uint8x8_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint8x8_t ovcheck1;
	


	// If the parameter is zero, we can take a shortcut.
	// This also avoids division by zero during the overflow check.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = 0; 
		}
		return 0;
	}


	// Initialise the comparison values.
	datasliceleft = initvec_unsigned_char(param);

	// Used to calculate overflow.
	ovlimit = uint_ovlimit_unsigned_char(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_char(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_u8( &data2[x]);

		// Check for overflow. 
		// Check for overflow.
		ovcheck1 = vcgt_u8 (datasliceright, ovflvec); 
			// Check for overflow. 
			if (!(vreinterpret_u64_u8(ovcheck1) == 0x0000000000000000)){
			return 1;
		}

		// The actual SIMD operation.
		resultslice = vmul_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1_u8( &data2[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( uint_willoverflow(data2[x], ovlimit) ) {return 1;}
		data2[x] = param * data2[x];
	}

	return 0;

}


// param_num_arr_arr
char mul_unsigned_char_4_simd_ovfl(Py_ssize_t arraylen, unsigned char param, unsigned char *data2, unsigned char *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned char ovlimit;
	uint8x8_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint8x8_t ovcheck1;
	


	// If the parameter is zero, we can take a shortcut.
	// This also avoids division by zero during the overflow check.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = 0; 
		}
		return 0;
	}


	// Initialise the comparison values.
	datasliceleft = initvec_unsigned_char(param);

	// Used to calculate overflow.
	ovlimit = uint_ovlimit_unsigned_char(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_char(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_u8( &data2[x]);

		// Check for overflow. 
		// Check for overflow.
		ovcheck1 = vcgt_u8 (datasliceright, ovflvec); 
			// Check for overflow. 
			if (!(vreinterpret_u64_u8(ovcheck1) == 0x0000000000000000)){
			return 1;
		}

		// The actual SIMD operation.
		resultslice = vmul_u8(datasliceleft, datasliceright);
		// Store the result.
		vst1_u8( &data3[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( uint_willoverflow(data2[x], ovlimit) ) {return 1;}
		data3[x] = param * data2[x];
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
   This version is without overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARMv7_32BIT)
void mul_signed_short_1_simd(Py_ssize_t arraylen, signed short *data1, signed short param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_signed_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s16( &data1[x]);
		// The actual SIMD operation. 
		resultslice = vmul_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1_s16( &data1[x],  resultslice);
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

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_signed_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s16( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1_s16( &data3[x],  resultslice);
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

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_signed_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_s16( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1_s16( &data2[x],  resultslice);
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

	// SIMD related variables.
	Py_ssize_t alignedlength;

	int16x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_signed_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_s16( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1_s16( &data3[x],  resultslice);
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

	int16x4_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s16( &data1[x]);
		datasliceright = vld1_s16( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1_s16( &data1[x],  resultslice);
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

	int16x4_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_s16( &data1[x]);
		datasliceright = vld1_s16( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_s16(datasliceleft, datasliceright);
		// Store the result.
		vst1_s16( &data3[x],  resultslice);
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
   This version supports overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   Returns 1 if overflow occurred, else returns 0.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARMv7_32BIT)
char mul_signed_short_1_simd_ovfl(Py_ssize_t arraylen, signed short *data1, signed short param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed short ovlimit1, ovlimit2;
	int16x4_t datasliceleft, datasliceright, resultslice, ovflvec1, ovflvec2;
	uint16x4_t ovcheck1, ovcheck2;
	


	// If the parameter is zero, we can take a shortcut.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = 0; 
		}
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_signed_short(param);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);


	// Signed integers do not have a symetrical range (e.g. -128 to 127). 
	if (param == -1) {
		// This is used for detecting a potential overflow condition.
		ovflvec1 = initvec_signed_short(SHRT_MIN);

		for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1_s16( &data1[x]);

			// Check for overflow. 
			// Do an equal compare operation.
			ovcheck1 = vceq_s16 (datasliceleft, ovflvec1); 
			// Check for overflow. 
			if (!(vreinterpret_u64_u16(ovcheck1) == 0x0000000000000000)){
				return 1;
			}
			// The actual SIMD operation. 
			resultslice = vmul_s16(datasliceleft, datasliceright);

			// Store the result.
			vst1_s16( &data1[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( minusone_loop_willoverflow_signed_short(data1[x]) ) {return 1;}
			data1[x] = data1[x] * param; 
		}

	} else {


		// Used to calculate overflow.
		ovlimit1 = max_ovlimit_signed_short(param);
		ovlimit2 = min_ovlimit_signed_short(param);

		// This is used for detecting a potential overflow condition.
		ovflvec1 = initvec_signed_short(ovlimit1);
		ovflvec2 = initvec_signed_short(ovlimit2);

		// param is positive.
		if (param > 0) {

			for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
				// Load the data into the vector register.
				datasliceleft = vld1_s16( &data1[x]);

				// Check for overflow. 
				// Check for overflow.
			ovcheck1 = vcgt_s16 (datasliceleft, ovflvec1);
			ovcheck2 = vclt_s16 (datasliceleft, ovflvec2); 
			// Check for overflow. 
			if ((!(vreinterpret_u64_u16(ovcheck1) == 0x0000000000000000)) ||
				(!(vreinterpret_u64_u16(ovcheck2) == 0x0000000000000000))){
					return 1;
				}

				// The actual SIMD operation. 
				resultslice = vmul_s16(datasliceleft, datasliceright);

				// Store the result.
				vst1_s16( &data1[x],  resultslice);
			}

			// Handle the values left over at the end of the array.
			for (x = alignedlength; x < arraylen; x++) {
				if ( pos_willoverflow(data1[x], ovlimit1, ovlimit2) ) {return 1;}
				data1[x] = data1[x] * param; 
			}

		}


		// param is negative.
		if (param < 0) {

			for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
				// Load the data into the vector register.
				datasliceleft = vld1_s16( &data1[x]);

				// Check for overflow. 
				// Check for overflow.
			ovcheck1 = vclt_s16 (datasliceleft, ovflvec1);
			ovcheck2 = vcgt_s16 (datasliceleft, ovflvec2); 
			// Check for overflow. 
			if ((!(vreinterpret_u64_u16(ovcheck1) == 0x0000000000000000)) ||
				(!(vreinterpret_u64_u16(ovcheck2) == 0x0000000000000000))){
					return 1;
				}

				// The actual SIMD operation. 
				resultslice = vmul_s16(datasliceleft, datasliceright);

				// Store the result.
				vst1_s16( &data1[x],  resultslice);

			}
		
			// Handle the values left over at the end of the array.
			for (x = alignedlength; x < arraylen; x++) {
				if ( neg_willoverflow(data1[x], ovlimit1, ovlimit2) ) {return 1;}
				data1[x] = data1[x] * param; 
			}
		}
	}

	return 0;

}



// param_arr_num_arr
char mul_signed_short_2_simd_ovfl(Py_ssize_t arraylen, signed short *data1, signed short param, signed short *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed short ovlimit1, ovlimit2;
	int16x4_t datasliceleft, datasliceright, resultslice, ovflvec1, ovflvec2;
	uint16x4_t ovcheck1, ovcheck2;
	


	// If the parameter is zero, we can take a shortcut.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = 0; 
		}
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_signed_short(param);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);


	// Signed integers do not have a symetrical range (e.g. -128 to 127). 
	if (param == -1) {
		// This is used for detecting a potential overflow condition.
		ovflvec1 = initvec_signed_short(SHRT_MIN);

		for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceleft = vld1_s16( &data1[x]);

			// Check for overflow. 
			// Do an equal compare operation.
			ovcheck1 = vceq_s16 (datasliceleft, ovflvec1); 
			// Check for overflow. 
			if (!(vreinterpret_u64_u16(ovcheck1) == 0x0000000000000000)){
				return 1;
			}
			// The actual SIMD operation. 
			resultslice = vmul_s16(datasliceleft, datasliceright);

			// Store the result.
			vst1_s16( &data3[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( minusone_loop_willoverflow_signed_short(data1[x]) ) {return 1;}
			data3[x] = data1[x] * param; 
		}

	} else {


		// Used to calculate overflow.
		ovlimit1 = max_ovlimit_signed_short(param);
		ovlimit2 = min_ovlimit_signed_short(param);

		// This is used for detecting a potential overflow condition.
		ovflvec1 = initvec_signed_short(ovlimit1);
		ovflvec2 = initvec_signed_short(ovlimit2);

		// param is positive.
		if (param > 0) {

			for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
				// Load the data into the vector register.
				datasliceleft = vld1_s16( &data1[x]);

				// Check for overflow. 
				// Check for overflow.
			ovcheck1 = vcgt_s16 (datasliceleft, ovflvec1);
			ovcheck2 = vclt_s16 (datasliceleft, ovflvec2); 
			// Check for overflow. 
			if ((!(vreinterpret_u64_u16(ovcheck1) == 0x0000000000000000)) ||
				(!(vreinterpret_u64_u16(ovcheck2) == 0x0000000000000000))){
					return 1;
				}

				// The actual SIMD operation. 
				resultslice = vmul_s16(datasliceleft, datasliceright);

				// Store the result.
				vst1_s16( &data3[x],  resultslice);
			}

			// Handle the values left over at the end of the array.
			for (x = alignedlength; x < arraylen; x++) {
				if ( pos_willoverflow(data1[x], ovlimit1, ovlimit2) ) {return 1;}
				data3[x] = data1[x] * param; 
			}

		}


		// param is negative.
		if (param < 0) {

			for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
				// Load the data into the vector register.
				datasliceleft = vld1_s16( &data1[x]);

				// Check for overflow. 
				// Check for overflow.
			ovcheck1 = vclt_s16 (datasliceleft, ovflvec1);
			ovcheck2 = vcgt_s16 (datasliceleft, ovflvec2); 
			// Check for overflow. 
			if ((!(vreinterpret_u64_u16(ovcheck1) == 0x0000000000000000)) ||
				(!(vreinterpret_u64_u16(ovcheck2) == 0x0000000000000000))){
					return 1;
				}

				// The actual SIMD operation. 
				resultslice = vmul_s16(datasliceleft, datasliceright);

				// Store the result.
				vst1_s16( &data3[x],  resultslice);

			}
		
			// Handle the values left over at the end of the array.
			for (x = alignedlength; x < arraylen; x++) {
				if ( neg_willoverflow(data1[x], ovlimit1, ovlimit2) ) {return 1;}
				data3[x] = data1[x] * param; 
			}
		}
	}

	return 0;
	
}



// param_num_arr_none
char mul_signed_short_3_simd_ovfl(Py_ssize_t arraylen, signed short param, signed short *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed short ovlimit1, ovlimit2;
	int16x4_t datasliceleft, datasliceright, resultslice, ovflvec1, ovflvec2;
	uint16x4_t ovcheck1, ovcheck2;
	


	// If the parameter is zero, we can take a shortcut.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = 0; 
		}
		return 0;
	}


	// Initialise the param values.
	datasliceleft = initvec_signed_short(param);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);


	// Signed integers do not have a symetrical range (e.g. -128 to 127). 
	if (param == -1) {
		// This is used for detecting a potential overflow condition.
		ovflvec1 = initvec_signed_short(SHRT_MIN);

		for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceright = vld1_s16( &data2[x]);

			// Check for overflow. 
			// Do an equal compare operation.
			ovcheck1 = vceq_s16 (datasliceright, ovflvec1); 
			// Check for overflow. 
			if (!(vreinterpret_u64_u16(ovcheck1) == 0x0000000000000000)){
				return 1;
			}
			// The actual SIMD operation. 
			resultslice = vmul_s16(datasliceleft, datasliceright);

			// Store the result.
			vst1_s16( &data2[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( minusone_loop_willoverflow_signed_short(data2[x]) ) {return 1;}
			data2[x] = param * data2[x]; 
		}

	} else {


		// Used to calculate overflow.
		ovlimit1 = max_ovlimit_signed_short(param);
		ovlimit2 = min_ovlimit_signed_short(param);

		// This is used for detecting a potential overflow condition.
		ovflvec1 = initvec_signed_short(ovlimit1);
		ovflvec2 = initvec_signed_short(ovlimit2);

		// param is positive.
		if (param > 0) {

			for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
				// Load the data into the vector register.
				datasliceright = vld1_s16( &data2[x]);

				// Check for overflow. 
				// Check for overflow.
			ovcheck1 = vcgt_s16 (datasliceright, ovflvec1);
			ovcheck2 = vclt_s16 (datasliceright, ovflvec2); 
			// Check for overflow. 
			if ((!(vreinterpret_u64_u16(ovcheck1) == 0x0000000000000000)) ||
				(!(vreinterpret_u64_u16(ovcheck2) == 0x0000000000000000))){
					return 1;
				}

				// The actual SIMD operation. 
				resultslice = vmul_s16(datasliceleft, datasliceright);

				// Store the result.
				vst1_s16( &data2[x],  resultslice);
			}

			// Handle the values left over at the end of the array.
			for (x = alignedlength; x < arraylen; x++) {
				if ( pos_willoverflow(data2[x], ovlimit1, ovlimit2) ) {return 1;}
				data2[x] = param * data2[x]; 
			}

		}


		// param is negative.
		if (param < 0) {

			for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
				// Load the data into the vector register.
				datasliceright = vld1_s16( &data2[x]);

				// Check for overflow. 
				// Check for overflow.
			ovcheck1 = vclt_s16 (datasliceright, ovflvec1);
			ovcheck2 = vcgt_s16 (datasliceright, ovflvec2); 
			// Check for overflow. 
			if ((!(vreinterpret_u64_u16(ovcheck1) == 0x0000000000000000)) ||
				(!(vreinterpret_u64_u16(ovcheck2) == 0x0000000000000000))){
					return 1;
				}

				// The actual SIMD operation. 
				resultslice = vmul_s16(datasliceleft, datasliceright);

				// Store the result.
				vst1_s16( &data2[x],  resultslice);

			}
		
			// Handle the values left over at the end of the array.
			for (x = alignedlength; x < arraylen; x++) {
				if ( neg_willoverflow(data2[x], ovlimit1, ovlimit2) ) {return 1;}
				data2[x] = param * data2[x]; 
			}
		}
	}

	return 0;

}



// param_num_arr_arr
char mul_signed_short_4_simd_ovfl(Py_ssize_t arraylen, signed short param, signed short *data2, signed short *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed short ovlimit1, ovlimit2;
	int16x4_t datasliceleft, datasliceright, resultslice, ovflvec1, ovflvec2;
	uint16x4_t ovcheck1, ovcheck2;
	


	// If the parameter is zero, we can take a shortcut.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = 0; 
		}
		return 0;
	}


	// Initialise the param values.
	datasliceleft = initvec_signed_short(param);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);


	// Signed integers do not have a symetrical range (e.g. -128 to 127). 
	if (param == -1) {
		// This is used for detecting a potential overflow condition.
		ovflvec1 = initvec_signed_short(SHRT_MIN);

		for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
			// Load the data into the vector register.
			datasliceright = vld1_s16( &data2[x]);

			// Check for overflow. 
			// Do an equal compare operation.
			ovcheck1 = vceq_s16 (datasliceright, ovflvec1); 
			// Check for overflow. 
			if (!(vreinterpret_u64_u16(ovcheck1) == 0x0000000000000000)){
				return 1;
			}
			// The actual SIMD operation. 
			resultslice = vmul_s16(datasliceleft, datasliceright);

			// Store the result.
			vst1_s16( &data3[x],  resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( minusone_loop_willoverflow_signed_short(data2[x]) ) {return 1;}
			data3[x] = param * data2[x]; 
		}

	} else {


		// Used to calculate overflow.
		ovlimit1 = max_ovlimit_signed_short(param);
		ovlimit2 = min_ovlimit_signed_short(param);

		// This is used for detecting a potential overflow condition.
		ovflvec1 = initvec_signed_short(ovlimit1);
		ovflvec2 = initvec_signed_short(ovlimit2);

		// param is positive.
		if (param > 0) {

			for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
				// Load the data into the vector register.
				datasliceright = vld1_s16( &data2[x]);

				// Check for overflow. 
				// Check for overflow.
			ovcheck1 = vcgt_s16 (datasliceright, ovflvec1);
			ovcheck2 = vclt_s16 (datasliceright, ovflvec2); 
			// Check for overflow. 
			if ((!(vreinterpret_u64_u16(ovcheck1) == 0x0000000000000000)) ||
				(!(vreinterpret_u64_u16(ovcheck2) == 0x0000000000000000))){
					return 1;
				}

				// The actual SIMD operation. 
				resultslice = vmul_s16(datasliceleft, datasliceright);

				// Store the result.
				vst1_s16( &data3[x],  resultslice);
			}

			// Handle the values left over at the end of the array.
			for (x = alignedlength; x < arraylen; x++) {
				if ( pos_willoverflow(data2[x], ovlimit1, ovlimit2) ) {return 1;}
				data3[x] = param * data2[x]; 
			}

		}


		// param is negative.
		if (param < 0) {

			for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
				// Load the data into the vector register.
				datasliceright = vld1_s16( &data2[x]);

				// Check for overflow. 
				// Check for overflow.
			ovcheck1 = vclt_s16 (datasliceright, ovflvec1);
			ovcheck2 = vcgt_s16 (datasliceright, ovflvec2); 
			// Check for overflow. 
			if ((!(vreinterpret_u64_u16(ovcheck1) == 0x0000000000000000)) ||
				(!(vreinterpret_u64_u16(ovcheck2) == 0x0000000000000000))){
					return 1;
				}

				// The actual SIMD operation. 
				resultslice = vmul_s16(datasliceleft, datasliceright);

				// Store the result.
				vst1_s16( &data3[x],  resultslice);

			}
		
			// Handle the values left over at the end of the array.
			for (x = alignedlength; x < arraylen; x++) {
				if ( neg_willoverflow(data2[x], ovlimit1, ovlimit2) ) {return 1;}
				data3[x] = param * data2[x]; 
			}
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
#if defined(AF_HASSIMD_ARMv7_32BIT)
uint16x4_t initvec_unsigned_short(unsigned short initval) {

	unsigned int y;
	unsigned short initvals[SHORTSIMDSIZE];
	uint16x4_t simdvec;

	for (y = 0; y < SHORTSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = vld1_u16((initvals));

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
#if defined(AF_HASSIMD_ARMv7_32BIT)
void mul_unsigned_short_1_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u16( &data1[x]);
		// The actual SIMD operation. 
		resultslice = vmul_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1_u16( &data1[x],  resultslice);
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

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u16( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1_u16( &data3[x],  resultslice);
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

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_unsigned_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_u16( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1_u16( &data2[x],  resultslice);
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

	// SIMD related variables.
	Py_ssize_t alignedlength;

	uint16x4_t datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_unsigned_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_u16( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1_u16( &data3[x],  resultslice);
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

	uint16x4_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u16( &data1[x]);
		datasliceright = vld1_u16( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1_u16( &data1[x],  resultslice);
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

	uint16x4_t datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u16( &data1[x]);
		datasliceright = vld1_u16( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = vmul_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1_u16( &data3[x],  resultslice);
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
   This version is with overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_ARMv7_32BIT)
char mul_unsigned_short_1_simd_ovfl(Py_ssize_t arraylen, unsigned short *data1, unsigned short param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned short ovlimit;
	uint16x4_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint16x4_t ovcheck1;
	


	// If the parameter is zero, we can take a shortcut.
	// This also avoids division by zero during the overflow check.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = 0; 
		}
		return 0;
	}


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_short(param);


	// Used to calculate overflow.
	ovlimit = uint_ovlimit_unsigned_short(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_short(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u16( &data1[x]);

		// Check for overflow. 
		// Check for overflow.
		ovcheck1 = vcgt_u16 (datasliceleft, ovflvec); 
			// Check for overflow. 
			if (!(vreinterpret_u64_u16(ovcheck1) == 0x0000000000000000)){
			return 1;
		}

		// The actual SIMD operation. 
		resultslice = vmul_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1_u16( &data1[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( uint_willoverflow(data1[x], ovlimit) ) {return 1;}
		data1[x] = data1[x] * param;
	}

	return 0;

}


// param_arr_num_arr
char mul_unsigned_short_2_simd_ovfl(Py_ssize_t arraylen, unsigned short *data1, unsigned short param, unsigned short *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned short ovlimit;
	uint16x4_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint16x4_t ovcheck1;
	


	// If the parameter is zero, we can take a shortcut.
	// This also avoids division by zero during the overflow check.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = 0; 
		}
		return 0;
	}


	// Initialise the comparison values.
	datasliceright = initvec_unsigned_short(param);

	// Used to calculate overflow.
	ovlimit = uint_ovlimit_unsigned_short(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_short(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = vld1_u16( &data1[x]);

		// Check for overflow. 
		// Check for overflow.
		ovcheck1 = vcgt_u16 (datasliceleft, ovflvec); 
			// Check for overflow. 
			if (!(vreinterpret_u64_u16(ovcheck1) == 0x0000000000000000)){
			return 1;
		}

		// The actual SIMD operation.
		resultslice = vmul_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1_u16( &data3[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( uint_willoverflow(data1[x], ovlimit) ) {return 1;}
		data3[x] = data1[x] * param;
	}

	return 0;

}


// param_num_arr_none
char mul_unsigned_short_3_simd_ovfl(Py_ssize_t arraylen, unsigned short param, unsigned short *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned short ovlimit;
	uint16x4_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint16x4_t ovcheck1;
	


	// If the parameter is zero, we can take a shortcut.
	// This also avoids division by zero during the overflow check.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = 0; 
		}
		return 0;
	}


	// Initialise the comparison values.
	datasliceleft = initvec_unsigned_short(param);

	// Used to calculate overflow.
	ovlimit = uint_ovlimit_unsigned_short(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_short(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_u16( &data2[x]);

		// Check for overflow. 
		// Check for overflow.
		ovcheck1 = vcgt_u16 (datasliceright, ovflvec); 
			// Check for overflow. 
			if (!(vreinterpret_u64_u16(ovcheck1) == 0x0000000000000000)){
			return 1;
		}

		// The actual SIMD operation.
		resultslice = vmul_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1_u16( &data2[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( uint_willoverflow(data2[x], ovlimit) ) {return 1;}
		data2[x] = param * data2[x];
	}

	return 0;

}


// param_num_arr_arr
char mul_unsigned_short_4_simd_ovfl(Py_ssize_t arraylen, unsigned short param, unsigned short *data2, unsigned short *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	unsigned short ovlimit;
	uint16x4_t datasliceleft, datasliceright, resultslice, ovflvec;
	uint16x4_t ovcheck1;
	


	// If the parameter is zero, we can take a shortcut.
	// This also avoids division by zero during the overflow check.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = 0; 
		}
		return 0;
	}


	// Initialise the comparison values.
	datasliceleft = initvec_unsigned_short(param);

	// Used to calculate overflow.
	ovlimit = uint_ovlimit_unsigned_short(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_unsigned_short(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = vld1_u16( &data2[x]);

		// Check for overflow. 
		// Check for overflow.
		ovcheck1 = vcgt_u16 (datasliceright, ovflvec); 
			// Check for overflow. 
			if (!(vreinterpret_u64_u16(ovcheck1) == 0x0000000000000000)){
			return 1;
		}

		// The actual SIMD operation.
		resultslice = vmul_u16(datasliceleft, datasliceright);
		// Store the result.
		vst1_u16( &data3[x],  resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( uint_willoverflow(data2[x], ovlimit) ) {return 1;}
		data3[x] = param * data2[x];
	}

	return 0;

}
#endif

/*--------------------------------------------------------------------------- */
