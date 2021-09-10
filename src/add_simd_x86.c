//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   add_simd_x86.c
// Purpose:  Calculate the add of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     1-Apr-2019
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
#if defined(AF_HASSIMD_X86)
v16qi initvec_signed_char(signed char initval) {

	unsigned int y;
	signed char initvals[CHARSIMDSIZE];
	v16qi simdvec;

	for (y = 0; y < CHARSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = (v16qi) __builtin_ia32_lddqu((char *) (initvals));

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
#if defined(AF_HASSIMD_X86)
void add_signed_char_1_simd(Py_ssize_t arraylen, signed char *data1, signed char param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_signed_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data1[x]);
		// The actual SIMD operation. 
		resultslice = (v16qi) __builtin_ia32_paddb128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[x],  resultslice);
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

	v16qi datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_signed_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data1[x]);
		// The actual SIMD operation.
		resultslice = (v16qi) __builtin_ia32_paddb128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[x],  resultslice);
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

	v16qi datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_signed_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation.
		resultslice = (v16qi) __builtin_ia32_paddb128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data2[x],  resultslice);
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

	v16qi datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_signed_char(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation.
		resultslice = (v16qi) __builtin_ia32_paddb128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[x],  resultslice);
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

	v16qi datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data1[x]);
		datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation.
		resultslice = (v16qi) __builtin_ia32_paddb128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[x],  resultslice);
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

	v16qi datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data1[x]);
		datasliceright = (v16qi) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation.
		resultslice = (v16qi) __builtin_ia32_paddb128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[x],  resultslice);
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
#if defined(AF_HASSIMD_X86)
char add_signed_char_1_simd_ovfl(Py_ssize_t arraylen, signed char *data1, signed char param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed char ovlimit;
	v16qi datasliceleft, datasliceright, resultslice, ovflvec;
	v16qi ovcheck;
	


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
			datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data1[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = __builtin_ia32_pcmpgtb128 (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v16qi) __builtin_ia32_paddb128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data1[x],  resultslice);
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
			datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data1[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = __builtin_ia32_pcmpgtb128 (ovflvec, datasliceleft);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v16qi) __builtin_ia32_paddb128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data1[x],  resultslice);

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
	v16qi datasliceleft, datasliceright, resultslice, ovflvec;
	v16qi ovcheck;
	


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
			datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data1[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = __builtin_ia32_pcmpgtb128 (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v16qi) __builtin_ia32_paddb128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data3[x],  resultslice);
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
			datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data1[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = __builtin_ia32_pcmpgtb128 (ovflvec, datasliceleft);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v16qi) __builtin_ia32_paddb128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data3[x],  resultslice);

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
	v16qi datasliceleft, datasliceright, resultslice, ovflvec;
	v16qi ovcheck;
	


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
			datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data2[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = __builtin_ia32_pcmpgtb128 (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v16qi) __builtin_ia32_paddb128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data2[x],  resultslice);
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
			datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data2[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = __builtin_ia32_pcmpgtb128 (ovflvec, datasliceleft);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v16qi) __builtin_ia32_paddb128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data2[x],  resultslice);

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
	v16qi datasliceleft, datasliceright, resultslice, ovflvec;
	v16qi ovcheck;
	


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
			datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data2[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = __builtin_ia32_pcmpgtb128 (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v16qi) __builtin_ia32_paddb128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data3[x],  resultslice);
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
			datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data2[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = __builtin_ia32_pcmpgtb128 (ovflvec, datasliceleft);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v16qi) __builtin_ia32_paddb128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data3[x],  resultslice);

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
#if defined(AF_HASSIMD_X86)
v8hi initvec_signed_short(signed short initval) {

	unsigned int y;
	signed short initvals[SHORTSIMDSIZE];
	v8hi simdvec;

	for (y = 0; y < SHORTSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = (v8hi) __builtin_ia32_lddqu((char *) (initvals));

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
#if defined(AF_HASSIMD_X86)
void add_signed_short_1_simd(Py_ssize_t arraylen, signed short *data1, signed short param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_signed_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data1[x]);
		// The actual SIMD operation. 
		resultslice = (v8hi) __builtin_ia32_paddw128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[x], (v16qi)  resultslice);
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

	v8hi datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_signed_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data1[x]);
		// The actual SIMD operation.
		resultslice = (v8hi) __builtin_ia32_paddw128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);
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

	v8hi datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_signed_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation.
		resultslice = (v8hi) __builtin_ia32_paddw128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data2[x], (v16qi)  resultslice);
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

	v8hi datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_signed_short(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation.
		resultslice = (v8hi) __builtin_ia32_paddw128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);
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

	v8hi datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data1[x]);
		datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation.
		resultslice = (v8hi) __builtin_ia32_paddw128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[x], (v16qi)  resultslice);
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

	v8hi datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data1[x]);
		datasliceright = (v8hi) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation.
		resultslice = (v8hi) __builtin_ia32_paddw128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);
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
#if defined(AF_HASSIMD_X86)
char add_signed_short_1_simd_ovfl(Py_ssize_t arraylen, signed short *data1, signed short param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed short ovlimit;
	v8hi datasliceleft, datasliceright, resultslice, ovflvec;
	v8hi ovcheck;
	


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
			datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data1[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = __builtin_ia32_pcmpgtw128 (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v8hi) __builtin_ia32_paddw128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data1[x], (v16qi)  resultslice);
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
			datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data1[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = __builtin_ia32_pcmpgtw128 (ovflvec, datasliceleft);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v8hi) __builtin_ia32_paddw128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data1[x], (v16qi)  resultslice);

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
	v8hi datasliceleft, datasliceright, resultslice, ovflvec;
	v8hi ovcheck;
	


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
			datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data1[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = __builtin_ia32_pcmpgtw128 (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v8hi) __builtin_ia32_paddw128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);
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
			datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data1[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = __builtin_ia32_pcmpgtw128 (ovflvec, datasliceleft);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v8hi) __builtin_ia32_paddw128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);

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
	v8hi datasliceleft, datasliceright, resultslice, ovflvec;
	v8hi ovcheck;
	


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
			datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data2[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = __builtin_ia32_pcmpgtw128 (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v8hi) __builtin_ia32_paddw128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data2[x], (v16qi)  resultslice);
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
			datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data2[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = __builtin_ia32_pcmpgtw128 (ovflvec, datasliceleft);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v8hi) __builtin_ia32_paddw128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data2[x], (v16qi)  resultslice);

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
	v8hi datasliceleft, datasliceright, resultslice, ovflvec;
	v8hi ovcheck;
	


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
			datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data2[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = __builtin_ia32_pcmpgtw128 (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v8hi) __builtin_ia32_paddw128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);
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
			datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data2[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = __builtin_ia32_pcmpgtw128 (ovflvec, datasliceleft);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v8hi) __builtin_ia32_paddw128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);

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
#if defined(AF_HASSIMD_X86)
v4si initvec_signed_int(signed int initval) {

	unsigned int y;
	signed int initvals[INTSIMDSIZE];
	v4si simdvec;

	for (y = 0; y < INTSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = (v4si) __builtin_ia32_lddqu((char *) (initvals));

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
#if defined(AF_HASSIMD_X86)
void add_signed_int_1_simd(Py_ssize_t arraylen, signed int *data1, signed int param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_signed_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data1[x]);
		// The actual SIMD operation. 
		resultslice = (v4si) __builtin_ia32_paddd128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[x], (v16qi)  resultslice);
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

	v4si datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_signed_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data1[x]);
		// The actual SIMD operation.
		resultslice = (v4si) __builtin_ia32_paddd128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);
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

	v4si datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_signed_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v4si) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation.
		resultslice = (v4si) __builtin_ia32_paddd128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data2[x], (v16qi)  resultslice);
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

	v4si datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_signed_int(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v4si) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation.
		resultslice = (v4si) __builtin_ia32_paddd128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);
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

	v4si datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data1[x]);
		datasliceright = (v4si) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation.
		resultslice = (v4si) __builtin_ia32_paddd128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[x], (v16qi)  resultslice);
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

	v4si datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data1[x]);
		datasliceright = (v4si) __builtin_ia32_lddqu((char *)  &data2[x]);
		// The actual SIMD operation.
		resultslice = (v4si) __builtin_ia32_paddd128(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);
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
#if defined(AF_HASSIMD_X86)
char add_signed_int_1_simd_ovfl(Py_ssize_t arraylen, signed int *data1, signed int param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	signed int ovlimit;
	v4si datasliceleft, datasliceright, resultslice, ovflvec;
	v4si ovcheck;
	


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
			datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data1[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = __builtin_ia32_pcmpgtd128  (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v4si) __builtin_ia32_paddd128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data1[x], (v16qi)  resultslice);
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
			datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data1[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = __builtin_ia32_pcmpgtd128  (ovflvec, datasliceleft);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v4si) __builtin_ia32_paddd128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data1[x], (v16qi)  resultslice);

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
	v4si datasliceleft, datasliceright, resultslice, ovflvec;
	v4si ovcheck;
	


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
			datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data1[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = __builtin_ia32_pcmpgtd128  (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v4si) __builtin_ia32_paddd128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);
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
			datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data1[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = __builtin_ia32_pcmpgtd128  (ovflvec, datasliceleft);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v4si) __builtin_ia32_paddd128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);

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
	v4si datasliceleft, datasliceright, resultslice, ovflvec;
	v4si ovcheck;
	


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
			datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data2[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = __builtin_ia32_pcmpgtd128  (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v4si) __builtin_ia32_paddd128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data2[x], (v16qi)  resultslice);
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
			datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data2[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = __builtin_ia32_pcmpgtd128  (ovflvec, datasliceleft);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v4si) __builtin_ia32_paddd128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data2[x], (v16qi)  resultslice);

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
	v4si datasliceleft, datasliceright, resultslice, ovflvec;
	v4si ovcheck;
	


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
			datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data2[x]);

			// Check for overflow. 
			// Do a greater than compare operation.
			ovcheck = __builtin_ia32_pcmpgtd128  (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v4si) __builtin_ia32_paddd128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);
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
			datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data2[x]);

			// Check for overflow. 
			// Do a less than compare operation.
			ovcheck = __builtin_ia32_pcmpgtd128  (ovflvec, datasliceleft);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = (v4si) __builtin_ia32_paddd128(datasliceleft, datasliceright);

			// Store the result.
			__builtin_ia32_storedqu((char *) &data3[x], (v16qi)  resultslice);

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
#if defined(AF_HASSIMD_X86)
v4sf initvec_float(float initval) {

	unsigned int y;
	float initvals[FLOATSIMDSIZE];
	v4sf simdvec;

	for (y = 0; y < FLOATSIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = (v4sf) __builtin_ia32_loadups((initvals));

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
#if defined(AF_HASSIMD_X86)
void add_float_1_simd(Py_ssize_t arraylen, float *data1, float param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4sf datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_float(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4sf) __builtin_ia32_loadups( &data1[x]);
		// The actual SIMD operation. 
		resultslice = __builtin_ia32_addps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data1[x], (v4sf) resultslice);
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

	v4sf datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_float(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4sf) __builtin_ia32_loadups( &data1[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_addps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data3[x], (v4sf) resultslice);
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

	v4sf datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_float(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v4sf) __builtin_ia32_loadups( &data2[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_addps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data2[x], (v4sf) resultslice);
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

	v4sf datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_float(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v4sf) __builtin_ia32_loadups( &data2[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_addps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data3[x], (v4sf) resultslice);
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

	v4sf datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4sf) __builtin_ia32_loadups( &data1[x]);
		datasliceright = (v4sf) __builtin_ia32_loadups( &data2[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_addps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data1[x], (v4sf) resultslice);
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

	v4sf datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4sf) __builtin_ia32_loadups( &data1[x]);
		datasliceright = (v4sf) __builtin_ia32_loadups( &data2[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_addps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data3[x], (v4sf) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] + data2[x];
	}

}
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specifired value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
*/
#if defined(AF_HASSIMD_X86)
v2df initvec_double(double initval) {

	unsigned int y;
	double initvals[DOUBLESIMDSIZE];
	v2df simdvec;

	for (y = 0; y < DOUBLESIMDSIZE; y++) {
		initvals[y] = initval;
	}
	simdvec = (v2df) __builtin_ia32_loadupd((initvals));

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
#if defined(AF_HASSIMD_X86)
void add_double_1_simd(Py_ssize_t arraylen, double *data1, double param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_double(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v2df) __builtin_ia32_loadupd( &data1[x]);
		// The actual SIMD operation. 
		resultslice = __builtin_ia32_addpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data1[x], (v2df) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] + param;
	}

}



// param_arr_num_arr
void add_double_2_simd(Py_ssize_t arraylen, double *data1, double param, double *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_double(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v2df) __builtin_ia32_loadupd( &data1[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_addpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data3[x], (v2df) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] + param;
	}

}



// param_num_arr_none
void add_double_3_simd(Py_ssize_t arraylen, double param, double *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_double(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v2df) __builtin_ia32_loadupd( &data2[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_addpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data2[x], (v2df) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param + data2[x];
	}

}



// param_num_arr_arr
void add_double_4_simd(Py_ssize_t arraylen, double param, double *data2, double *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_double(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v2df) __builtin_ia32_loadupd( &data2[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_addpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data3[x], (v2df) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param + data2[x];
	}

}



// param_arr_arr_none
void add_double_5_simd(Py_ssize_t arraylen, double *data1, double *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v2df) __builtin_ia32_loadupd( &data1[x]);
		datasliceright = (v2df) __builtin_ia32_loadupd( &data2[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_addpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data1[x], (v2df) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] + data2[x];
	}

}



// param_arr_arr_arr
void add_double_6_simd(Py_ssize_t arraylen, double *data1, double *data2, double *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v2df) __builtin_ia32_loadupd( &data1[x]);
		datasliceright = (v2df) __builtin_ia32_loadupd( &data2[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_addpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data3[x], (v2df) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] + data2[x];
	}

}
#endif

/*--------------------------------------------------------------------------- */
