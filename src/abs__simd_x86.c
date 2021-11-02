//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   abs__simd_x86.c
// Purpose:  Calculate the abs_ of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     22-Mar-2019
// Ver:      31-Oct-2021.
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
#include "abs__defs.h"

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
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
*/
// param_arr_none
#if defined(AF_HASSIMD_X86)
void abs__signed_char_1_simd(Py_ssize_t arraylen, signed char *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft;
	


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data[x]);
		// The actual SIMD operation. 
		datasliceleft = __builtin_ia32_pabsb128(datasliceleft);
		// Store the result.
		__builtin_ia32_storedqu((char *)  &data[x],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data[x] = data[x] >= 0 ? data[x] : -data[x];
	}

}
#endif


// param_arr_arr
#if defined(AF_HASSIMD_X86)
void abs__signed_char_2_simd(Py_ssize_t arraylen, signed char *data, signed char *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft;
	


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data[x]);
		// The actual SIMD operation. 
		datasliceleft = __builtin_ia32_pabsb128(datasliceleft);
		// Store the result.
		__builtin_ia32_storedqu((char *)  &dataout[x],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		dataout[x] = data[x] >= 0 ? data[x] : -data[x];
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
char abs__signed_char_1_simd_ovfl(Py_ssize_t arraylen, signed char *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft, datasliceright, ovflvec;
	v16qi ovcheck;
	
	


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_signed_char(SCHAR_MIN);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data[x]);

		// Check for overflow. 
		// Do an equal compare operation.
			ovcheck = __builtin_ia32_pcmpeqb128 (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
			return 1;
		}

		// The actual SIMD operation. 
		datasliceright = __builtin_ia32_pabsb128(datasliceleft);

		// Take the max value to get the abs.
		datasliceleft = __builtin_ia32_pmaxsb128(datasliceleft, datasliceright);

		// Store the result.
		__builtin_ia32_storedqu((char *)  &data[x],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( minval_loop_willoverflow_signed_char(data[x]) ) {return ARR_ERR_OVFL;}
		data[x] = data[x] >= 0 ? data[x] : -data[x];
	}

	return 0;

}


// param_arr_arr
char abs__signed_char_2_simd_ovfl(Py_ssize_t arraylen, signed char *data, signed char *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v16qi datasliceleft, datasliceright, ovflvec;
	v16qi ovcheck;
	
	


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_signed_char(SCHAR_MIN);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v16qi) __builtin_ia32_lddqu((char *)  &data[x]);

		// Check for overflow. 
		// Do an equal compare operation.
			ovcheck = __builtin_ia32_pcmpeqb128 (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
			return 1;
		}

		// The actual SIMD operation. 
		datasliceright = __builtin_ia32_pabsb128(datasliceleft);

		// Take the max value to get the abs.
		datasliceleft = __builtin_ia32_pmaxsb128(datasliceleft, datasliceright);

		// Store the result.
		__builtin_ia32_storedqu((char *)  &dataout[x],  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( minval_loop_willoverflow_signed_char(data[x]) ) {return ARR_ERR_OVFL;}
		dataout[x] = data[x] >= 0 ? data[x] : -data[x];
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
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
*/
// param_arr_none
#if defined(AF_HASSIMD_X86)
void abs__signed_short_1_simd(Py_ssize_t arraylen, signed short *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft;
	


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data[x]);
		// The actual SIMD operation. 
		datasliceleft = __builtin_ia32_pabsw128(datasliceleft);
		// Store the result.
		__builtin_ia32_storedqu((char *)  &data[x], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data[x] = data[x] >= 0 ? data[x] : -data[x];
	}

}
#endif


// param_arr_arr
#if defined(AF_HASSIMD_X86)
void abs__signed_short_2_simd(Py_ssize_t arraylen, signed short *data, signed short *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft;
	


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data[x]);
		// The actual SIMD operation. 
		datasliceleft = __builtin_ia32_pabsw128(datasliceleft);
		// Store the result.
		__builtin_ia32_storedqu((char *)  &dataout[x], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		dataout[x] = data[x] >= 0 ? data[x] : -data[x];
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
char abs__signed_short_1_simd_ovfl(Py_ssize_t arraylen, signed short *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft, datasliceright, ovflvec;
	v8hi ovcheck;
	
	


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_signed_short(SHRT_MIN);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data[x]);

		// Check for overflow. 
		// Do an equal compare operation.
			ovcheck = __builtin_ia32_pcmpeqw128 (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
			return 1;
		}

		// The actual SIMD operation. 
		datasliceright = __builtin_ia32_pabsw128(datasliceleft);

		// Take the max value to get the abs.
		datasliceleft = __builtin_ia32_pmaxsw128(datasliceleft, datasliceright);

		// Store the result.
		__builtin_ia32_storedqu((char *)  &data[x], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( minval_loop_willoverflow_signed_short(data[x]) ) {return ARR_ERR_OVFL;}
		data[x] = data[x] >= 0 ? data[x] : -data[x];
	}

	return 0;

}


// param_arr_arr
char abs__signed_short_2_simd_ovfl(Py_ssize_t arraylen, signed short *data, signed short *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v8hi datasliceleft, datasliceright, ovflvec;
	v8hi ovcheck;
	
	


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_signed_short(SHRT_MIN);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v8hi) __builtin_ia32_lddqu((char *)  &data[x]);

		// Check for overflow. 
		// Do an equal compare operation.
			ovcheck = __builtin_ia32_pcmpeqw128 (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
			return 1;
		}

		// The actual SIMD operation. 
		datasliceright = __builtin_ia32_pabsw128(datasliceleft);

		// Take the max value to get the abs.
		datasliceleft = __builtin_ia32_pmaxsw128(datasliceleft, datasliceright);

		// Store the result.
		__builtin_ia32_storedqu((char *)  &dataout[x], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( minval_loop_willoverflow_signed_short(data[x]) ) {return ARR_ERR_OVFL;}
		dataout[x] = data[x] >= 0 ? data[x] : -data[x];
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
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
*/
// param_arr_none
#if defined(AF_HASSIMD_X86)
void abs__signed_int_1_simd(Py_ssize_t arraylen, signed int *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft;
	


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data[x]);
		// The actual SIMD operation. 
		datasliceleft = __builtin_ia32_pabsd128(datasliceleft);
		// Store the result.
		__builtin_ia32_storedqu((char *)  &data[x], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data[x] = data[x] >= 0 ? data[x] : -data[x];
	}

}
#endif


// param_arr_arr
#if defined(AF_HASSIMD_X86)
void abs__signed_int_2_simd(Py_ssize_t arraylen, signed int *data, signed int *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft;
	


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data[x]);
		// The actual SIMD operation. 
		datasliceleft = __builtin_ia32_pabsd128(datasliceleft);
		// Store the result.
		__builtin_ia32_storedqu((char *)  &dataout[x], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		dataout[x] = data[x] >= 0 ? data[x] : -data[x];
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
char abs__signed_int_1_simd_ovfl(Py_ssize_t arraylen, signed int *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft, datasliceright, ovflvec;
	v4si ovcheck;
	
	


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_signed_int(INT_MIN);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data[x]);

		// Check for overflow. 
		// Do an equal compare operation.
			ovcheck = __builtin_ia32_pcmpeqd128  (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
			return 1;
		}

		// The actual SIMD operation. 
		datasliceright = __builtin_ia32_pabsd128(datasliceleft);

		// Take the max value to get the abs.
		datasliceleft = __builtin_ia32_pmaxsd128(datasliceleft, datasliceright);

		// Store the result.
		__builtin_ia32_storedqu((char *)  &data[x], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( minval_loop_willoverflow_signed_int(data[x]) ) {return ARR_ERR_OVFL;}
		data[x] = data[x] >= 0 ? data[x] : -data[x];
	}

	return 0;

}


// param_arr_arr
char abs__signed_int_2_simd_ovfl(Py_ssize_t arraylen, signed int *data, signed int *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4si datasliceleft, datasliceright, ovflvec;
	v4si ovcheck;
	
	


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_signed_int(INT_MIN);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4si) __builtin_ia32_lddqu((char *)  &data[x]);

		// Check for overflow. 
		// Do an equal compare operation.
			ovcheck = __builtin_ia32_pcmpeqd128  (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {
			return 1;
		}

		// The actual SIMD operation. 
		datasliceright = __builtin_ia32_pabsd128(datasliceleft);

		// Take the max value to get the abs.
		datasliceleft = __builtin_ia32_pmaxsd128(datasliceleft, datasliceright);

		// Store the result.
		__builtin_ia32_storedqu((char *)  &dataout[x], (v16qi)  datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( minval_loop_willoverflow_signed_int(data[x]) ) {return ARR_ERR_OVFL;}
		dataout[x] = data[x] >= 0 ? data[x] : -data[x];
	}

	return 0;

}
#endif

