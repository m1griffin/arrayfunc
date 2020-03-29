//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   neg_simd_x86.c
// Purpose:  Calculate the neg of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     22-Mar-2019
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
   data = The input data array.
   dataout = The output data array.
*/
// param_arr_none
#if defined(AF_HASSIMD_X86)
void neg_signed_char_1_simd(Py_ssize_t arraylen, signed char *data) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft;
	v16qi vsignparam = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = __builtin_ia32_psignb128(datasliceleft, vsignparam);
		// Store the result.
		__builtin_ia32_storedqu((char *)  &data[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data[index] = -data[index];
	}

}
#endif


// param_arr_arr
#if defined(AF_HASSIMD_X86)
void neg_signed_char_2_simd(Py_ssize_t arraylen, signed char *data, signed char *dataout) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft;
	v16qi vsignparam = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = __builtin_ia32_psignb128(datasliceleft, vsignparam);
		// Store the result.
		__builtin_ia32_storedqu((char *)  &dataout[index],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		dataout[index] = -data[index];
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
#if defined(AF_HASSIMD_X86)
void neg_signed_short_1_simd(Py_ssize_t arraylen, signed short *data) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft;
	v8hi vsignparam = {-1, -1, -1, -1, -1, -1, -1, -1};


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = __builtin_ia32_psignw128(datasliceleft, vsignparam);
		// Store the result.
		__builtin_ia32_storedqu((char *)  &data[index], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data[index] = -data[index];
	}

}
#endif


// param_arr_arr
#if defined(AF_HASSIMD_X86)
void neg_signed_short_2_simd(Py_ssize_t arraylen, signed short *data, signed short *dataout) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft;
	v8hi vsignparam = {-1, -1, -1, -1, -1, -1, -1, -1};


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = __builtin_ia32_psignw128(datasliceleft, vsignparam);
		// Store the result.
		__builtin_ia32_storedqu((char *)  &dataout[index], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		dataout[index] = -data[index];
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
#if defined(AF_HASSIMD_X86)
void neg_signed_int_1_simd(Py_ssize_t arraylen, signed int *data) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft;
	v4si vsignparam = {-1, -1, -1, -1};


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = __builtin_ia32_psignd128(datasliceleft, vsignparam);
		// Store the result.
		__builtin_ia32_storedqu((char *)  &data[index], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data[index] = -data[index];
	}

}
#endif


// param_arr_arr
#if defined(AF_HASSIMD_X86)
void neg_signed_int_2_simd(Py_ssize_t arraylen, signed int *data, signed int *dataout) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft;
	v4si vsignparam = {-1, -1, -1, -1};


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = __builtin_ia32_psignd128(datasliceleft, vsignparam);
		// Store the result.
		__builtin_ia32_storedqu((char *)  &dataout[index], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		dataout[index] = -data[index];
	}

}
#endif

