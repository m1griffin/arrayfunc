//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   lt_simd_x86.c
// Purpose:  Calculate the lt of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     16-Jan-2018
// Ver:      23-Mar-2019.
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
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#ifdef AF_HASSIMD
char lt_signed_char_1_simd(Py_ssize_t arraylen, signed char *data1, signed char param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v16qi datasliceleft, datasliceright, resultslice;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = (v16qi) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *) &data1[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] < param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char lt_signed_char_3_simd(Py_ssize_t arraylen, signed char param, signed char *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v16qi datasliceleft, datasliceright, resultslice;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = (v16qi) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceright = (v16qi) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(param < data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char lt_signed_char_5_simd(Py_ssize_t arraylen, signed char *data1, signed char *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *) &data1[index]);
		datasliceright = (v16qi) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] < data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#ifdef AF_HASSIMD
char lt_unsigned_char_1_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v16qi datasliceleft, datasliceright, resultslice;
	unsigned char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = (v16qi) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *) &data1[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] < param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char lt_unsigned_char_3_simd(Py_ssize_t arraylen, unsigned char param, unsigned char *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v16qi datasliceleft, datasliceright, resultslice;
	unsigned char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = (v16qi) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceright = (v16qi) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(param < data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char lt_unsigned_char_5_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *) &data1[index]);
		datasliceright = (v16qi) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] < data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#ifdef AF_HASSIMD
char lt_signed_short_1_simd(Py_ssize_t arraylen, signed short *data1, signed short param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v8hi datasliceleft, datasliceright, resultslice;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = (v8hi) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *) &data1[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] < param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char lt_signed_short_3_simd(Py_ssize_t arraylen, signed short param, signed short *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v8hi datasliceleft, datasliceright, resultslice;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = (v8hi) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceright = (v8hi) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(param < data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char lt_signed_short_5_simd(Py_ssize_t arraylen, signed short *data1, signed short *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *) &data1[index]);
		datasliceright = (v8hi) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] < data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#ifdef AF_HASSIMD
char lt_unsigned_short_1_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v8hi datasliceleft, datasliceright, resultslice;
	unsigned short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = (v8hi) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *) &data1[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] < param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char lt_unsigned_short_3_simd(Py_ssize_t arraylen, unsigned short param, unsigned short *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v8hi datasliceleft, datasliceright, resultslice;
	unsigned short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = (v8hi) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceright = (v8hi) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(param < data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char lt_unsigned_short_5_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *) &data1[index]);
		datasliceright = (v8hi) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] < data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#ifdef AF_HASSIMD
char lt_signed_int_1_simd(Py_ssize_t arraylen, signed int *data1, signed int param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4si datasliceleft, datasliceright, resultslice;
	signed int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = (v4si) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *) &data1[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] < param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char lt_signed_int_3_simd(Py_ssize_t arraylen, signed int param, signed int *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4si datasliceleft, datasliceright, resultslice;
	signed int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = (v4si) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceright = (v4si) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(param < data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char lt_signed_int_5_simd(Py_ssize_t arraylen, signed int *data1, signed int *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *) &data1[index]);
		datasliceright = (v4si) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] < data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#ifdef AF_HASSIMD
char lt_unsigned_int_1_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4si datasliceleft, datasliceright, resultslice;
	unsigned int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = (v4si) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *) &data1[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] < param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char lt_unsigned_int_3_simd(Py_ssize_t arraylen, unsigned int param, unsigned int *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4si datasliceleft, datasliceright, resultslice;
	unsigned int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = (v4si) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceright = (v4si) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(param < data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char lt_unsigned_int_5_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *) &data1[index]);
		datasliceright = (v4si) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] < data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#ifdef AF_HASSIMD
char lt_float_1_simd(Py_ssize_t arraylen, float *data1, float param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4sf datasliceleft, datasliceright, resultslice;
	float compvals[FLOATSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = (v4sf) __builtin_ia32_loadups(compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
		datasliceleft = (v4sf) __builtin_ia32_loadups(&data1[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] < param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char lt_float_3_simd(Py_ssize_t arraylen, float param, float *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4sf datasliceleft, datasliceright, resultslice;
	float compvals[FLOATSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = (v4sf) __builtin_ia32_loadups(compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
		datasliceright = (v4sf) __builtin_ia32_loadups(&data2[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(param < data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char lt_float_5_simd(Py_ssize_t arraylen, float *data1, float *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4sf datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
		datasliceleft = (v4sf) __builtin_ia32_loadups(&data1[index]);
		datasliceright = (v4sf) __builtin_ia32_loadups(&data2[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] < data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#ifdef AF_HASSIMD
char lt_double_1_simd(Py_ssize_t arraylen, double *data1, double param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v2df datasliceleft, datasliceright, resultslice;
	double compvals[DOUBLESIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < DOUBLESIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceright = (v2df) __builtin_ia32_loadupd(compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += DOUBLESIMDSIZE) {
		datasliceleft = (v2df) __builtin_ia32_loadupd(&data1[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] < param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char lt_double_3_simd(Py_ssize_t arraylen, double param, double *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v2df datasliceleft, datasliceright, resultslice;
	double compvals[DOUBLESIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < DOUBLESIMDSIZE; y++) {
		compvals[y] = param;
	}
	datasliceleft = (v2df) __builtin_ia32_loadupd(compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += DOUBLESIMDSIZE) {
		datasliceright = (v2df) __builtin_ia32_loadupd(&data2[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(param < data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char lt_double_5_simd(Py_ssize_t arraylen, double *data1, double *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += DOUBLESIMDSIZE) {
		datasliceleft = (v2df) __builtin_ia32_loadupd(&data1[index]);
		datasliceright = (v2df) __builtin_ia32_loadupd(&data2[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft < datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] < data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif

