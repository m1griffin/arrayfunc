//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   lshift_simd_x86.c
// Purpose:  Calculate the lshift of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     12-Mar-2019
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
void lshift_signed_char_1_simd(Py_ssize_t arraylen, signed char *data1, signed char param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft << param;
		// Store the result.
		__builtin_ia32_storedqu((char *)  &data1[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] << param;
	}

}
#endif


// param_arr_num_arr
#if defined(AF_HASSIMD_X86)
void lshift_signed_char_2_simd(Py_ssize_t arraylen, signed char *data1, signed char param, signed char *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft << param;
		// Store the result.
		__builtin_ia32_storedqu((char *)  &data3[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] << param;
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
#if defined(AF_HASSIMD_X86)
void lshift_unsigned_char_1_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft << param;
		// Store the result.
		__builtin_ia32_storedqu((char *)  &data1[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] << param;
	}

}
#endif


// param_arr_num_arr
#if defined(AF_HASSIMD_X86)
void lshift_unsigned_char_2_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param, unsigned char *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft << param;
		// Store the result.
		__builtin_ia32_storedqu((char *)  &data3[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] << param;
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
#if defined(AF_HASSIMD_X86)
void lshift_signed_short_1_simd(Py_ssize_t arraylen, signed short *data1, signed short param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft << param;
		// Store the result.
		__builtin_ia32_storedqu((char *)  &data1[index], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] << param;
	}

}
#endif


// param_arr_num_arr
#if defined(AF_HASSIMD_X86)
void lshift_signed_short_2_simd(Py_ssize_t arraylen, signed short *data1, signed short param, signed short *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft << param;
		// Store the result.
		__builtin_ia32_storedqu((char *)  &data3[index], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] << param;
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
#if defined(AF_HASSIMD_X86)
void lshift_unsigned_short_1_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft << param;
		// Store the result.
		__builtin_ia32_storedqu((char *)  &data1[index], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] << param;
	}

}
#endif


// param_arr_num_arr
#if defined(AF_HASSIMD_X86)
void lshift_unsigned_short_2_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param, unsigned short *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft << param;
		// Store the result.
		__builtin_ia32_storedqu((char *)  &data3[index], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] << param;
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
#if defined(AF_HASSIMD_X86)
void lshift_signed_int_1_simd(Py_ssize_t arraylen, signed int *data1, signed int param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft << param;
		// Store the result.
		__builtin_ia32_storedqu((char *)  &data1[index], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] << param;
	}

}
#endif


// param_arr_num_arr
#if defined(AF_HASSIMD_X86)
void lshift_signed_int_2_simd(Py_ssize_t arraylen, signed int *data1, signed int param, signed int *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft << param;
		// Store the result.
		__builtin_ia32_storedqu((char *)  &data3[index], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] << param;
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
#if defined(AF_HASSIMD_X86)
void lshift_unsigned_int_1_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft << param;
		// Store the result.
		__builtin_ia32_storedqu((char *)  &data1[index], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] << param;
	}

}
#endif


// param_arr_num_arr
#if defined(AF_HASSIMD_X86)
void lshift_unsigned_int_2_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param, unsigned int *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft << param;
		// Store the result.
		__builtin_ia32_storedqu((char *)  &data3[index], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] << param;
	}

}
#endif


