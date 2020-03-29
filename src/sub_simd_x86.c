//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   sub_simd_x86.c
// Purpose:  Calculate the sub of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     1-Apr-2019
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
#if defined(AF_HASSIMD_X86)
void sub_signed_char_1_simd(Py_ssize_t arraylen, signed char *data1, signed char param) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft, datasliceright, resultslice;
	signed char opvals[CHARSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = (v16qi) __builtin_ia32_psubb128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] - param;
	}

}



// param_arr_num_arr
void sub_signed_char_2_simd(Py_ssize_t arraylen, signed char *data1, signed char param, signed char *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft, datasliceright, resultslice;
	signed char opvals[CHARSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = (v16qi) __builtin_ia32_psubb128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] - param;
	}

}



// param_num_arr_none
void sub_signed_char_3_simd(Py_ssize_t arraylen, signed char param, signed char *data2) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft, datasliceright, resultslice;
	signed char opvals[CHARSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = (v16qi) __builtin_ia32_psubb128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data2[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param - data2[x];
	}

}



// param_num_arr_arr
void sub_signed_char_4_simd(Py_ssize_t arraylen, signed char param, signed char *data2, signed char *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft, datasliceright, resultslice;
	signed char opvals[CHARSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = (v16qi) __builtin_ia32_psubb128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param - data2[x];
	}

}



// param_arr_arr_none
void sub_signed_char_5_simd(Py_ssize_t arraylen, signed char *data1, signed char *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data1[x]);
		datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = (v16qi) __builtin_ia32_psubb128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] - data2[x];
	}

}



// param_arr_arr_arr
void sub_signed_char_6_simd(Py_ssize_t arraylen, signed char *data1, signed char *data2, signed char *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data1[x]);
		datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = (v16qi) __builtin_ia32_psubb128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[x],  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] - data2[x];
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
#if defined(AF_HASSIMD_X86)
void sub_signed_short_1_simd(Py_ssize_t arraylen, signed short *data1, signed short param) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft, datasliceright, resultslice;
	signed short opvals[SHORTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = (v8hi) __builtin_ia32_psubw128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[x], (v16qi)  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] - param;
	}

}



// param_arr_num_arr
void sub_signed_short_2_simd(Py_ssize_t arraylen, signed short *data1, signed short param, signed short *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft, datasliceright, resultslice;
	signed short opvals[SHORTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = (v8hi) __builtin_ia32_psubw128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] - param;
	}

}



// param_num_arr_none
void sub_signed_short_3_simd(Py_ssize_t arraylen, signed short param, signed short *data2) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft, datasliceright, resultslice;
	signed short opvals[SHORTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = (v8hi) __builtin_ia32_psubw128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data2[x], (v16qi)  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param - data2[x];
	}

}



// param_num_arr_arr
void sub_signed_short_4_simd(Py_ssize_t arraylen, signed short param, signed short *data2, signed short *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft, datasliceright, resultslice;
	signed short opvals[SHORTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = (v8hi) __builtin_ia32_psubw128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param - data2[x];
	}

}



// param_arr_arr_none
void sub_signed_short_5_simd(Py_ssize_t arraylen, signed short *data1, signed short *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data1[x]);
		datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = (v8hi) __builtin_ia32_psubw128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[x], (v16qi)  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] - data2[x];
	}

}



// param_arr_arr_arr
void sub_signed_short_6_simd(Py_ssize_t arraylen, signed short *data1, signed short *data2, signed short *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data1[x]);
		datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = (v8hi) __builtin_ia32_psubw128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] - data2[x];
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
#if defined(AF_HASSIMD_X86)
void sub_signed_int_1_simd(Py_ssize_t arraylen, signed int *data1, signed int param) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft, datasliceright, resultslice;
	signed int opvals[INTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = (v4si) __builtin_ia32_lddqu((char *)  opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = (v4si) __builtin_ia32_psubd128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[x], (v16qi)  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] - param;
	}

}



// param_arr_num_arr
void sub_signed_int_2_simd(Py_ssize_t arraylen, signed int *data1, signed int param, signed int *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft, datasliceright, resultslice;
	signed int opvals[INTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = (v4si) __builtin_ia32_lddqu((char *)  opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = (v4si) __builtin_ia32_psubd128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] - param;
	}

}



// param_num_arr_none
void sub_signed_int_3_simd(Py_ssize_t arraylen, signed int param, signed int *data2) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft, datasliceright, resultslice;
	signed int opvals[INTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v4si) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = (v4si) __builtin_ia32_psubd128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data2[x], (v16qi)  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param - data2[x];
	}

}



// param_num_arr_arr
void sub_signed_int_4_simd(Py_ssize_t arraylen, signed int param, signed int *data2, signed int *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft, datasliceright, resultslice;
	signed int opvals[INTSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v4si) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = (v4si) __builtin_ia32_psubd128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param - data2[x];
	}

}



// param_arr_arr_none
void sub_signed_int_5_simd(Py_ssize_t arraylen, signed int *data1, signed int *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data1[x]);
		datasliceright = (v4si) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = (v4si) __builtin_ia32_psubd128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[x], (v16qi)  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] - data2[x];
	}

}



// param_arr_arr_arr
void sub_signed_int_6_simd(Py_ssize_t arraylen, signed int *data1, signed int *data2, signed int *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data1[x]);
		datasliceright = (v4si) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = (v4si) __builtin_ia32_psubd128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] - data2[x];
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
#if defined(AF_HASSIMD_X86)
void sub_float_1_simd(Py_ssize_t arraylen, float *data1, float param) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4sf datasliceleft, datasliceright, resultslice;
	float opvals[FLOATSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = (v4sf) __builtin_ia32_loadups( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4sf) __builtin_ia32_loadups( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_subps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data1[x], (v4sf) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] - param;
	}

}



// param_arr_num_arr
void sub_float_2_simd(Py_ssize_t arraylen, float *data1, float param, float *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4sf datasliceleft, datasliceright, resultslice;
	float opvals[FLOATSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = (v4sf) __builtin_ia32_loadups( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4sf) __builtin_ia32_loadups( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_subps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data3[x], (v4sf) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] - param;
	}

}



// param_num_arr_none
void sub_float_3_simd(Py_ssize_t arraylen, float param, float *data2) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4sf datasliceleft, datasliceright, resultslice;
	float opvals[FLOATSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = (v4sf) __builtin_ia32_loadups( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v4sf) __builtin_ia32_loadups( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_subps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data2[x], (v4sf) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param - data2[x];
	}

}



// param_num_arr_arr
void sub_float_4_simd(Py_ssize_t arraylen, float param, float *data2, float *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4sf datasliceleft, datasliceright, resultslice;
	float opvals[FLOATSIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = (v4sf) __builtin_ia32_loadups( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v4sf) __builtin_ia32_loadups( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_subps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data3[x], (v4sf) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param - data2[x];
	}

}



// param_arr_arr_none
void sub_float_5_simd(Py_ssize_t arraylen, float *data1, float *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4sf datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4sf) __builtin_ia32_loadups( &data1[x]);
		datasliceright = (v4sf) __builtin_ia32_loadups( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_subps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data1[x], (v4sf) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] - data2[x];
	}

}



// param_arr_arr_arr
void sub_float_6_simd(Py_ssize_t arraylen, float *data1, float *data2, float *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4sf datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4sf) __builtin_ia32_loadups( &data1[x]);
		datasliceright = (v4sf) __builtin_ia32_loadups( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_subps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data3[x], (v4sf) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] - data2[x];
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
#if defined(AF_HASSIMD_X86)
void sub_double_1_simd(Py_ssize_t arraylen, double *data1, double param) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice;
	double opvals[DOUBLESIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < DOUBLESIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = (v2df) __builtin_ia32_loadupd( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v2df) __builtin_ia32_loadupd( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_subpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data1[x], (v2df) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] - param;
	}

}



// param_arr_num_arr
void sub_double_2_simd(Py_ssize_t arraylen, double *data1, double param, double *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice;
	double opvals[DOUBLESIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < DOUBLESIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceright = (v2df) __builtin_ia32_loadupd( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v2df) __builtin_ia32_loadupd( &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_subpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data3[x], (v2df) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] - param;
	}

}



// param_num_arr_none
void sub_double_3_simd(Py_ssize_t arraylen, double param, double *data2) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice;
	double opvals[DOUBLESIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < DOUBLESIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = (v2df) __builtin_ia32_loadupd( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v2df) __builtin_ia32_loadupd( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_subpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data2[x], (v2df) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param - data2[x];
	}

}



// param_num_arr_arr
void sub_double_4_simd(Py_ssize_t arraylen, double param, double *data2, double *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice;
	double opvals[DOUBLESIMDSIZE];


	// Initialise the comparison values.
	for (y = 0; y < DOUBLESIMDSIZE; y++) {
		opvals[y] = param;
	}
	datasliceleft = (v2df) __builtin_ia32_loadupd( opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v2df) __builtin_ia32_loadupd( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_subpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data3[x], (v2df) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param - data2[x];
	}

}



// param_arr_arr_none
void sub_double_5_simd(Py_ssize_t arraylen, double *data1, double *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v2df) __builtin_ia32_loadupd( &data1[x]);
		datasliceright = (v2df) __builtin_ia32_loadupd( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_subpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data1[x], (v2df) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] - data2[x];
	}

}



// param_arr_arr_arr
void sub_double_6_simd(Py_ssize_t arraylen, double *data1, double *data2, double *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v2df) __builtin_ia32_loadupd( &data1[x]);
		datasliceright = (v2df) __builtin_ia32_loadupd( &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_subpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data3[x], (v2df) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] - data2[x];
	}

}
#endif

/*--------------------------------------------------------------------------- */
