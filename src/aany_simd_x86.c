//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   aany_simd_x86.c
// Purpose:  Calculate the aany of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     16-Apr-2019
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
/* For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_eq_signed_char_simd(Py_ssize_t arraylen, signed char *data, signed char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v16qi datasliceleft, datasliceright;
	v16qi resultslice;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_pcmpeqb128(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] == param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_gt_signed_char_simd(Py_ssize_t arraylen, signed char *data, signed char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v16qi datasliceleft, datasliceright;
	v16qi resultslice;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_pcmpgtb128(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] > param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_ge_signed_char_simd(Py_ssize_t arraylen, signed char *data, signed char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v16qi datasliceleft, datasliceright;
	v16qi resultslice, compslice;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Find the minimum values. 
		compslice = __builtin_ia32_pminsb128(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is greater than or equal to.
		resultslice = __builtin_ia32_pcmpeqb128(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] >= param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_lt_signed_char_simd(Py_ssize_t arraylen, signed char *data, signed char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v16qi datasliceleft, datasliceright;
	v16qi resultslice, compslice;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Find the minimum values. 
		compslice = __builtin_ia32_pminsb128(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is less than.
		resultslice = __builtin_ia32_pcmpeqb128(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] < param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_le_signed_char_simd(Py_ssize_t arraylen, signed char *data, signed char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v16qi datasliceleft, datasliceright;
	v16qi resultslice;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_pcmpgtb128(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] <= param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_ne_signed_char_simd(Py_ssize_t arraylen, signed char *data, signed char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v16qi datasliceleft, datasliceright;
	v16qi resultslice;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Compare for equality.
		resultslice = __builtin_ia32_pcmpeqb128(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] != param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_eq_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v16qi datasliceleft, datasliceright;
	v16qi resultslice;
	unsigned char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_pcmpeqb128(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] == param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_gt_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v16qi datasliceleft, datasliceright;
	v16qi resultslice, compslice;
	unsigned char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Find the maximum values. 
		compslice = __builtin_ia32_pmaxub128(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is greater than. 
		resultslice = __builtin_ia32_pcmpeqb128(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] > param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_ge_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v16qi datasliceleft, datasliceright;
	v16qi resultslice, compslice;
	unsigned char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Find the minimum values. 
		compslice = __builtin_ia32_pminub128(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then a least.
		// one value is less than.
		resultslice = __builtin_ia32_pcmpeqb128(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] >= param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_lt_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v16qi datasliceleft, datasliceright;
	v16qi resultslice, compslice;
	unsigned char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Find the minimum values. 
		compslice = __builtin_ia32_pminub128(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is less than.
		resultslice = __builtin_ia32_pcmpeqb128(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] < param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_le_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v16qi datasliceleft, datasliceright;
	v16qi resultslice, compslice;
	unsigned char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Find the maximum values. 
		compslice = __builtin_ia32_pmaxub128(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is less than or equal to.
		resultslice = __builtin_ia32_pcmpeqb128(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] <= param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_ne_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v16qi datasliceleft, datasliceright;
	v16qi resultslice;
	unsigned char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Compare for equality.
		resultslice = __builtin_ia32_pcmpeqb128(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] != param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_eq_signed_short_simd(Py_ssize_t arraylen, signed short *data, signed short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v8hi datasliceleft, datasliceright;
	v8hi resultslice;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_pcmpeqw128(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] == param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_gt_signed_short_simd(Py_ssize_t arraylen, signed short *data, signed short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v8hi datasliceleft, datasliceright;
	v8hi resultslice;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_pcmpgtw128(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] > param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_ge_signed_short_simd(Py_ssize_t arraylen, signed short *data, signed short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v8hi datasliceleft, datasliceright;
	v8hi resultslice, compslice;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Find the minimum values. 
		compslice = __builtin_ia32_pminsw128(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is greater than or equal to.
		resultslice = __builtin_ia32_pcmpeqw128(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] >= param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_lt_signed_short_simd(Py_ssize_t arraylen, signed short *data, signed short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v8hi datasliceleft, datasliceright;
	v8hi resultslice, compslice;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Find the minimum values. 
		compslice = __builtin_ia32_pminsw128(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is less than.
		resultslice = __builtin_ia32_pcmpeqw128(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] < param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_le_signed_short_simd(Py_ssize_t arraylen, signed short *data, signed short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v8hi datasliceleft, datasliceright;
	v8hi resultslice;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_pcmpgtw128(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] <= param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_ne_signed_short_simd(Py_ssize_t arraylen, signed short *data, signed short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v8hi datasliceleft, datasliceright;
	v8hi resultslice;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Compare for equality.
		resultslice = __builtin_ia32_pcmpeqw128(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] != param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_eq_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v8hi datasliceleft, datasliceright;
	v8hi resultslice;
	unsigned short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_pcmpeqw128(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] == param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_gt_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v8hi datasliceleft, datasliceright;
	v8hi resultslice, compslice;
	unsigned short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Find the maximum values. 
		compslice = __builtin_ia32_pmaxuw128(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is greater than. 
		resultslice = __builtin_ia32_pcmpeqw128(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] > param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_ge_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v8hi datasliceleft, datasliceright;
	v8hi resultslice, compslice;
	unsigned short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Find the minimum values. 
		compslice = __builtin_ia32_pminuw128(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then a least.
		// one value is less than.
		resultslice = __builtin_ia32_pcmpeqw128(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] >= param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_lt_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v8hi datasliceleft, datasliceright;
	v8hi resultslice, compslice;
	unsigned short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Find the minimum values. 
		compslice = __builtin_ia32_pminuw128(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is less than.
		resultslice = __builtin_ia32_pcmpeqw128(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] < param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_le_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v8hi datasliceleft, datasliceright;
	v8hi resultslice, compslice;
	unsigned short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Find the maximum values. 
		compslice = __builtin_ia32_pmaxuw128(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is less than or equal to.
		resultslice = __builtin_ia32_pcmpeqw128(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] <= param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_ne_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v8hi datasliceleft, datasliceright;
	v8hi resultslice;
	unsigned short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data[index]);
		// Compare for equality.
		resultslice = __builtin_ia32_pcmpeqw128(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] != param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_eq_signed_int_simd(Py_ssize_t arraylen, signed int *data, signed int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4si datasliceleft, datasliceright;
	v4si resultslice;
	signed int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v4si) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_pcmpeqd128(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] == param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_gt_signed_int_simd(Py_ssize_t arraylen, signed int *data, signed int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4si datasliceleft, datasliceright;
	v4si resultslice;
	signed int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v4si) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_pcmpgtd128(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] > param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_ge_signed_int_simd(Py_ssize_t arraylen, signed int *data, signed int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4si datasliceleft, datasliceright;
	v4si resultslice, compslice;
	signed int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v4si) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data[index]);
		// Find the minimum values. 
		compslice = __builtin_ia32_pminsd128(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is greater than or equal to.
		resultslice = __builtin_ia32_pcmpeqd128(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] >= param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_lt_signed_int_simd(Py_ssize_t arraylen, signed int *data, signed int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4si datasliceleft, datasliceright;
	v4si resultslice, compslice;
	signed int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v4si) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data[index]);
		// Find the minimum values. 
		compslice = __builtin_ia32_pminsd128(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is less than.
		resultslice = __builtin_ia32_pcmpeqd128(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] < param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_le_signed_int_simd(Py_ssize_t arraylen, signed int *data, signed int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4si datasliceleft, datasliceright;
	v4si resultslice;
	signed int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v4si) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_pcmpgtd128(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] <= param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_ne_signed_int_simd(Py_ssize_t arraylen, signed int *data, signed int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4si datasliceleft, datasliceright;
	v4si resultslice;
	signed int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v4si) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data[index]);
		// Compare for equality.
		resultslice = __builtin_ia32_pcmpeqd128(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] != param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_eq_unsigned_int_simd(Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4si datasliceleft, datasliceright;
	v4si resultslice;
	unsigned int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v4si) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_pcmpeqd128(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] == param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_gt_unsigned_int_simd(Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4si datasliceleft, datasliceright;
	v4si resultslice, compslice;
	unsigned int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v4si) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data[index]);
		// Find the maximum values. 
		compslice = __builtin_ia32_pmaxud128(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is greater than. 
		resultslice = __builtin_ia32_pcmpeqd128(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] > param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_ge_unsigned_int_simd(Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4si datasliceleft, datasliceright;
	v4si resultslice, compslice;
	unsigned int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v4si) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data[index]);
		// Find the minimum values. 
		compslice = __builtin_ia32_pminud128(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then a least.
		// one value is less than.
		resultslice = __builtin_ia32_pcmpeqd128(compslice, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] >= param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_lt_unsigned_int_simd(Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4si datasliceleft, datasliceright;
	v4si resultslice, compslice;
	unsigned int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v4si) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data[index]);
		// Find the minimum values. 
		compslice = __builtin_ia32_pminud128(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is less than.
		resultslice = __builtin_ia32_pcmpeqd128(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] < param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_le_unsigned_int_simd(Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4si datasliceleft, datasliceright;
	v4si resultslice, compslice;
	unsigned int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v4si) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data[index]);
		// Find the maximum values. 
		compslice = __builtin_ia32_pmaxud128(datasliceleft, datasliceright);
		// If this is different from our compare parameter, then at
		// least one value is less than or equal to.
		resultslice = __builtin_ia32_pcmpeqd128(compslice, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] <= param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_ne_unsigned_int_simd(Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4si datasliceleft, datasliceright;
	v4si resultslice;
	unsigned int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v4si) __builtin_ia32_lddqu((char *)  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data[index]);
		// Compare for equality.
		resultslice = __builtin_ia32_pcmpeqd128(datasliceleft, datasliceright);
		// Compare the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0xffff) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] != param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_eq_float_simd(Py_ssize_t arraylen, float *data, float param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4sf datasliceleft, datasliceright;
	v4sf resultslice;
	float compvals[FLOATSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v4sf) __builtin_ia32_loadups(  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
		datasliceleft = (v4sf) __builtin_ia32_loadups(  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_cmpeqps(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] == param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_gt_float_simd(Py_ssize_t arraylen, float *data, float param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4sf datasliceleft, datasliceright;
	v4sf resultslice;
	float compvals[FLOATSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v4sf) __builtin_ia32_loadups(  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
		datasliceleft = (v4sf) __builtin_ia32_loadups(  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_cmpgtps(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] > param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_ge_float_simd(Py_ssize_t arraylen, float *data, float param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4sf datasliceleft, datasliceright;
	v4sf resultslice;
	float compvals[FLOATSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v4sf) __builtin_ia32_loadups(  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
		datasliceleft = (v4sf) __builtin_ia32_loadups(  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_cmpgeps(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] >= param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_lt_float_simd(Py_ssize_t arraylen, float *data, float param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4sf datasliceleft, datasliceright;
	v4sf resultslice;
	float compvals[FLOATSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v4sf) __builtin_ia32_loadups(  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
		datasliceleft = (v4sf) __builtin_ia32_loadups(  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_cmpltps(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] < param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_le_float_simd(Py_ssize_t arraylen, float *data, float param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4sf datasliceleft, datasliceright;
	v4sf resultslice;
	float compvals[FLOATSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v4sf) __builtin_ia32_loadups(  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
		datasliceleft = (v4sf) __builtin_ia32_loadups(  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_cmpleps(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] <= param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_ne_float_simd(Py_ssize_t arraylen, float *data, float param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4sf datasliceleft, datasliceright;
	v4sf resultslice;
	float compvals[FLOATSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v4sf) __builtin_ia32_loadups(  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
		datasliceleft = (v4sf) __builtin_ia32_loadups(  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_cmpneqps(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] != param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: d
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_eq_double_simd(Py_ssize_t arraylen, double *data, double param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v2df datasliceleft, datasliceright;
	v2df resultslice;
	double compvals[DOUBLESIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < DOUBLESIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v2df) __builtin_ia32_loadupd(  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += DOUBLESIMDSIZE) {
		datasliceleft = (v2df) __builtin_ia32_loadupd(  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_cmpeqpd(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] == param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: d
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_gt_double_simd(Py_ssize_t arraylen, double *data, double param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v2df datasliceleft, datasliceright;
	v2df resultslice;
	double compvals[DOUBLESIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < DOUBLESIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v2df) __builtin_ia32_loadupd(  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += DOUBLESIMDSIZE) {
		datasliceleft = (v2df) __builtin_ia32_loadupd(  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_cmpgtpd(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] > param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: d
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_ge_double_simd(Py_ssize_t arraylen, double *data, double param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v2df datasliceleft, datasliceright;
	v2df resultslice;
	double compvals[DOUBLESIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < DOUBLESIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v2df) __builtin_ia32_loadupd(  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += DOUBLESIMDSIZE) {
		datasliceleft = (v2df) __builtin_ia32_loadupd(  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_cmpgepd(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] >= param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: d
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_lt_double_simd(Py_ssize_t arraylen, double *data, double param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v2df datasliceleft, datasliceright;
	v2df resultslice;
	double compvals[DOUBLESIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < DOUBLESIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v2df) __builtin_ia32_loadupd(  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += DOUBLESIMDSIZE) {
		datasliceleft = (v2df) __builtin_ia32_loadupd(  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_cmpltpd(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] < param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: d
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_le_double_simd(Py_ssize_t arraylen, double *data, double param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v2df datasliceleft, datasliceright;
	v2df resultslice;
	double compvals[DOUBLESIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < DOUBLESIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v2df) __builtin_ia32_loadupd(  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += DOUBLESIMDSIZE) {
		datasliceleft = (v2df) __builtin_ia32_loadupd(  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_cmplepd(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] <= param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* For array code: d
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_X86)
signed int aany_ne_double_simd(Py_ssize_t arraylen, double *data, double param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v2df datasliceleft, datasliceright;
	v2df resultslice;
	double compvals[DOUBLESIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < DOUBLESIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = (v2df) __builtin_ia32_loadupd(  compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	// On x86 we have to do this in a round-about fashion for some
	// types of comparison operations due to how SIMD works on that
	// platform.
	for (index = 0; index < alignedlength; index += DOUBLESIMDSIZE) {
		datasliceleft = (v2df) __builtin_ia32_loadupd(  &data[index]);
		// Compare the slices.
		resultslice = __builtin_ia32_cmpneqpd(datasliceleft, datasliceright);
		// Check the results of the SIMD operation.
		if (__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000) {
			return 1;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] != param1) {
			return 1;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif

