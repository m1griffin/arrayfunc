//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   mul_simd_x86.c
// Purpose:  Calculate the mul of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     1-Apr-2019
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
#include "mul_defs.h"

// Function specific macros and other definitions.
#include "mul_defs.h"

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
void mul_float_1_simd(Py_ssize_t arraylen, float *data1, float param) {

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
		resultslice = __builtin_ia32_mulps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data1[x], (v4sf) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * param;
	}

}



// param_arr_num_arr
void mul_float_2_simd(Py_ssize_t arraylen, float *data1, float param, float *data3) {

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
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_mulps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data3[x], (v4sf) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * param;
	}

}



// param_num_arr_none
void mul_float_3_simd(Py_ssize_t arraylen, float param, float *data2) {

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
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_mulps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data2[x], (v4sf) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param * data2[x];
	}

}



// param_num_arr_arr
void mul_float_4_simd(Py_ssize_t arraylen, float param, float *data2, float *data3) {

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
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_mulps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data3[x], (v4sf) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param * data2[x];
	}

}



// param_arr_arr_none
void mul_float_5_simd(Py_ssize_t arraylen, float *data1, float *data2) {

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
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_mulps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data1[x], (v4sf) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * data2[x];
	}

}



// param_arr_arr_arr
void mul_float_6_simd(Py_ssize_t arraylen, float *data1, float *data2, float *data3) {

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
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_mulps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data3[x], (v4sf) resultslice);
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
   This version is without overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   Returns 1 if overflow occurred, else returns 0.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_X86)
char mul_float_1_simd_ovfl(Py_ssize_t arraylen, float *data1, float param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4sf datasliceleft, datasliceright, resultslice, checkslice;

	float checkvecresults[FLOATSIMDSIZE];
	float checksliceinit[FLOATSIMDSIZE] = {0.0};


	// Initialise the comparison values.
	datasliceright = initvec_float(param);

	// This is used to check for errors by accumulating non-finite values.
	checkslice = (v4sf) __builtin_ia32_loadups( checksliceinit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4sf) __builtin_ia32_loadups( &data1[x]);
		// The actual SIMD operation. 
		resultslice = __builtin_ia32_mulps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data1[x], (v4sf) resultslice);

		// Check the result. None-finite errors should accumulate.
		checkslice = __builtin_ia32_mulps(checkslice, resultslice);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	__builtin_ia32_storeups( checkvecresults, checkslice);
	for (x = 0; x < FLOATSIMDSIZE; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * param;
		if (!isfinite(data1[x])) {return 1;}
	}

	return 0;

}



// param_arr_num_arr
char mul_float_2_simd_ovfl(Py_ssize_t arraylen, float *data1, float param, float *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4sf datasliceleft, datasliceright, resultslice, checkslice;

	float checkvecresults[FLOATSIMDSIZE];
	float checksliceinit[FLOATSIMDSIZE] = {0.0};


	// Initialise the comparison values.
	datasliceright = initvec_float(param);

	// This is used to check for errors by accumulating non-finite values.
	checkslice = (v4sf) __builtin_ia32_loadups( checksliceinit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4sf) __builtin_ia32_loadups( &data1[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_mulps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data3[x], (v4sf) resultslice);

		// Check the result. None-finite errors should accumulate.
		checkslice = __builtin_ia32_mulps(checkslice, resultslice);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	__builtin_ia32_storeups( checkvecresults, checkslice);
	for (x = 0; x < FLOATSIMDSIZE; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * param;
		if (!isfinite(data3[x])) {return 1;}
	}

	return 0;

}



// param_num_arr_none
char mul_float_3_simd_ovfl(Py_ssize_t arraylen, float param, float *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4sf datasliceleft, datasliceright, resultslice, checkslice;

	float checkvecresults[FLOATSIMDSIZE];
	float checksliceinit[FLOATSIMDSIZE] = {0.0};


	// Initialise the comparison values.
	datasliceleft = initvec_float(param);

	// This is used to check for errors by accumulating non-finite values.
	checkslice = (v4sf) __builtin_ia32_loadups( checksliceinit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v4sf) __builtin_ia32_loadups( &data2[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_mulps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data2[x], (v4sf) resultslice);

		// Check the result. None-finite errors should accumulate.
		checkslice = __builtin_ia32_mulps(checkslice, resultslice);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	__builtin_ia32_storeups( checkvecresults, checkslice);
	for (x = 0; x < FLOATSIMDSIZE; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param * data2[x];
		if (!isfinite(data2[x])) {return 1;}
	}

	return 0;

}



// param_num_arr_arr
char mul_float_4_simd_ovfl(Py_ssize_t arraylen, float param, float *data2, float *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4sf datasliceleft, datasliceright, resultslice, checkslice;

	float checkvecresults[FLOATSIMDSIZE];
	float checksliceinit[FLOATSIMDSIZE] = {0.0};


	// Initialise the comparison values.
	datasliceleft = initvec_float(param);

	// This is used to check for errors by accumulating non-finite values.
	checkslice = (v4sf) __builtin_ia32_loadups( checksliceinit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v4sf) __builtin_ia32_loadups( &data2[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_mulps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data3[x], (v4sf) resultslice);

		// Check the result. None-finite errors should accumulate.
		checkslice = __builtin_ia32_mulps(checkslice, resultslice);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	__builtin_ia32_storeups( checkvecresults, checkslice);
	for (x = 0; x < FLOATSIMDSIZE; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param * data2[x];
		if (!isfinite(data3[x])) {return 1;}
	}

	return 0;

}



// param_arr_arr_none
char mul_float_5_simd_ovfl(Py_ssize_t arraylen, float *data1, float *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4sf datasliceleft, datasliceright, resultslice, checkslice;

	float checkvecresults[FLOATSIMDSIZE];
	float checksliceinit[FLOATSIMDSIZE] = {0.0};

	// This is used to check for errors by accumulating non-finite values.
	checkslice = (v4sf) __builtin_ia32_loadups( checksliceinit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4sf) __builtin_ia32_loadups( &data1[x]);
		datasliceright = (v4sf) __builtin_ia32_loadups( &data2[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_mulps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data1[x], (v4sf) resultslice);

		// Check the result. None-finite errors should accumulate.
		checkslice = __builtin_ia32_mulps(checkslice, resultslice);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	__builtin_ia32_storeups( checkvecresults, checkslice);
	for (x = 0; x < FLOATSIMDSIZE; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * data2[x];
		if (!isfinite(data1[x])) {return 1;}
	}

	return 0;

}



// param_arr_arr_arr
char mul_float_6_simd_ovfl(Py_ssize_t arraylen, float *data1, float *data2, float *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v4sf datasliceleft, datasliceright, resultslice, checkslice;

	float checkvecresults[FLOATSIMDSIZE];
	float checksliceinit[FLOATSIMDSIZE] = {0.0};

	// This is used to check for errors by accumulating non-finite values.
	checkslice = (v4sf) __builtin_ia32_loadups( checksliceinit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v4sf) __builtin_ia32_loadups( &data1[x]);
		datasliceright = (v4sf) __builtin_ia32_loadups( &data2[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_mulps(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeups( &data3[x], (v4sf) resultslice);

		// Check the result. None-finite errors should accumulate.
		checkslice = __builtin_ia32_mulps(checkslice, resultslice);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	__builtin_ia32_storeups( checkvecresults, checkslice);
	for (x = 0; x < FLOATSIMDSIZE; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * data2[x];
		if (!isfinite(data3[x])) {return 1;}
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
void mul_double_1_simd(Py_ssize_t arraylen, double *data1, double param) {

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
		resultslice = __builtin_ia32_mulpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data1[x], (v2df) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * param;
	}

}



// param_arr_num_arr
void mul_double_2_simd(Py_ssize_t arraylen, double *data1, double param, double *data3) {

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
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_mulpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data3[x], (v2df) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * param;
	}

}



// param_num_arr_none
void mul_double_3_simd(Py_ssize_t arraylen, double param, double *data2) {

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
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_mulpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data2[x], (v2df) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param * data2[x];
	}

}



// param_num_arr_arr
void mul_double_4_simd(Py_ssize_t arraylen, double param, double *data2, double *data3) {

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
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_mulpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data3[x], (v2df) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param * data2[x];
	}

}



// param_arr_arr_none
void mul_double_5_simd(Py_ssize_t arraylen, double *data1, double *data2) {

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
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_mulpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data1[x], (v2df) resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * data2[x];
	}

}



// param_arr_arr_arr
void mul_double_6_simd(Py_ssize_t arraylen, double *data1, double *data2, double *data3) {

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
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = __builtin_ia32_mulpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data3[x], (v2df) resultslice);
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
   This version is without overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   Returns 1 if overflow occurred, else returns 0.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_X86)
char mul_double_1_simd_ovfl(Py_ssize_t arraylen, double *data1, double param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice, checkslice;

	double checkvecresults[DOUBLESIMDSIZE];
	double checksliceinit[DOUBLESIMDSIZE] = {0.0};


	// Initialise the comparison values.
	datasliceright = initvec_double(param);

	// This is used to check for errors by accumulating non-finite values.
	checkslice = (v2df) __builtin_ia32_loadupd( checksliceinit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v2df) __builtin_ia32_loadupd( &data1[x]);
		// The actual SIMD operation. 
		resultslice = __builtin_ia32_mulpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data1[x], (v2df) resultslice);

		// Check the result. None-finite errors should accumulate.
		checkslice = __builtin_ia32_mulpd(checkslice, resultslice);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	__builtin_ia32_storeupd( checkvecresults, checkslice);
	for (x = 0; x < DOUBLESIMDSIZE; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * param;
		if (!isfinite(data1[x])) {return 1;}
	}

	return 0;

}



// param_arr_num_arr
char mul_double_2_simd_ovfl(Py_ssize_t arraylen, double *data1, double param, double *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice, checkslice;

	double checkvecresults[DOUBLESIMDSIZE];
	double checksliceinit[DOUBLESIMDSIZE] = {0.0};


	// Initialise the comparison values.
	datasliceright = initvec_double(param);

	// This is used to check for errors by accumulating non-finite values.
	checkslice = (v2df) __builtin_ia32_loadupd( checksliceinit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v2df) __builtin_ia32_loadupd( &data1[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_mulpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data3[x], (v2df) resultslice);

		// Check the result. None-finite errors should accumulate.
		checkslice = __builtin_ia32_mulpd(checkslice, resultslice);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	__builtin_ia32_storeupd( checkvecresults, checkslice);
	for (x = 0; x < DOUBLESIMDSIZE; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * param;
		if (!isfinite(data3[x])) {return 1;}
	}

	return 0;

}



// param_num_arr_none
char mul_double_3_simd_ovfl(Py_ssize_t arraylen, double param, double *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice, checkslice;

	double checkvecresults[DOUBLESIMDSIZE];
	double checksliceinit[DOUBLESIMDSIZE] = {0.0};


	// Initialise the comparison values.
	datasliceleft = initvec_double(param);

	// This is used to check for errors by accumulating non-finite values.
	checkslice = (v2df) __builtin_ia32_loadupd( checksliceinit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v2df) __builtin_ia32_loadupd( &data2[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_mulpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data2[x], (v2df) resultslice);

		// Check the result. None-finite errors should accumulate.
		checkslice = __builtin_ia32_mulpd(checkslice, resultslice);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	__builtin_ia32_storeupd( checkvecresults, checkslice);
	for (x = 0; x < DOUBLESIMDSIZE; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param * data2[x];
		if (!isfinite(data2[x])) {return 1;}
	}

	return 0;

}



// param_num_arr_arr
char mul_double_4_simd_ovfl(Py_ssize_t arraylen, double param, double *data2, double *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice, checkslice;

	double checkvecresults[DOUBLESIMDSIZE];
	double checksliceinit[DOUBLESIMDSIZE] = {0.0};


	// Initialise the comparison values.
	datasliceleft = initvec_double(param);

	// This is used to check for errors by accumulating non-finite values.
	checkslice = (v2df) __builtin_ia32_loadupd( checksliceinit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceright = (v2df) __builtin_ia32_loadupd( &data2[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_mulpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data3[x], (v2df) resultslice);

		// Check the result. None-finite errors should accumulate.
		checkslice = __builtin_ia32_mulpd(checkslice, resultslice);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	__builtin_ia32_storeupd( checkvecresults, checkslice);
	for (x = 0; x < DOUBLESIMDSIZE; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param * data2[x];
		if (!isfinite(data3[x])) {return 1;}
	}

	return 0;

}



// param_arr_arr_none
char mul_double_5_simd_ovfl(Py_ssize_t arraylen, double *data1, double *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice, checkslice;

	double checkvecresults[DOUBLESIMDSIZE];
	double checksliceinit[DOUBLESIMDSIZE] = {0.0};

	// This is used to check for errors by accumulating non-finite values.
	checkslice = (v2df) __builtin_ia32_loadupd( checksliceinit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v2df) __builtin_ia32_loadupd( &data1[x]);
		datasliceright = (v2df) __builtin_ia32_loadupd( &data2[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_mulpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data1[x], (v2df) resultslice);

		// Check the result. None-finite errors should accumulate.
		checkslice = __builtin_ia32_mulpd(checkslice, resultslice);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	__builtin_ia32_storeupd( checkvecresults, checkslice);
	for (x = 0; x < DOUBLESIMDSIZE; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] * data2[x];
		if (!isfinite(data1[x])) {return 1;}
	}

	return 0;

}



// param_arr_arr_arr
char mul_double_6_simd_ovfl(Py_ssize_t arraylen, double *data1, double *data2, double *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2df datasliceleft, datasliceright, resultslice, checkslice;

	double checkvecresults[DOUBLESIMDSIZE];
	double checksliceinit[DOUBLESIMDSIZE] = {0.0};

	// This is used to check for errors by accumulating non-finite values.
	checkslice = (v2df) __builtin_ia32_loadupd( checksliceinit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, DOUBLESIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += DOUBLESIMDSIZE) {
		// Load the data into the vector register.
		datasliceleft = (v2df) __builtin_ia32_loadupd( &data1[x]);
		datasliceright = (v2df) __builtin_ia32_loadupd( &data2[x]);
		// The actual SIMD operation.
		resultslice = __builtin_ia32_mulpd(datasliceleft, datasliceright);
		// Store the result.
		__builtin_ia32_storeupd( &data3[x], (v2df) resultslice);

		// Check the result. None-finite errors should accumulate.
		checkslice = __builtin_ia32_mulpd(checkslice, resultslice);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	__builtin_ia32_storeupd( checkvecresults, checkslice);
	for (x = 0; x < DOUBLESIMDSIZE; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] * data2[x];
		if (!isfinite(data3[x])) {return 1;}
	}

	return 0;

}
#endif

/*--------------------------------------------------------------------------- */
