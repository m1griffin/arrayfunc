//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   asum_simd_armv7.c
// Purpose:  Calculate the asum of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     05-May-2017
// Ver:      04-Jul-2022.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2022    Michael Griffin    <m12.griffin@gmail.com>
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

/*--------------------------------------------------------------------------- */

// Used to check for integer overflow. 
#include "asum_defs.h"

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

// This defines the "chunk" size used to process integer arrays in pieces small
// enough that overflow cannot occur within the "chunk".
#define LOOPCHUNKSIZE 256

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

/* For array code: b
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// This inner loop is used to sum small chunks of the array.
#if defined(AF_HASSIMD_ARMv7_32BIT)
long long innerloop_asum_signed_char(Py_ssize_t arraylen, signed char *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	long long partialsum = 0;

	signed short sumvals[CHARSIMDSIZE / 2];
	int8x8_t dataslice;
	int16x4_t resultslice;


	// Initialise the accumulator.
	resultslice = vdup_n_s16(0);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Use SIMD.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {

		// Load the data into the vector register.
		dataslice = vld1_s8( &data[x]);

		// The actual SIMD operation. 
		resultslice = vpadal_s8(resultslice, dataslice);

	}

	// Add up the values within the slice.
	vst1_s16(sumvals, resultslice);
	for (y = 0; y < (CHARSIMDSIZE / 2); y++) {
		partialsum = partialsum + sumvals[y];
	}

	// Add the values within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}

	return partialsum;

}
#endif



/*--------------------------------------------------------------------------- */
/* For array code: b
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// Version without error checking.
#if defined(AF_HASSIMD_ARMv7_32BIT)
long long asum_signed_char_simd(Py_ssize_t arraylen, signed char *data) { 

	Py_ssize_t x, loopremaining, loopchunk;
	long long partialsum = 0;

	for(x=0; x < arraylen; x += LOOPCHUNKSIZE) {
		// The array is summed in "chunks" using SIMD and then each
		// chunk added to the total.
		loopremaining = arraylen - x;
		loopchunk = (loopremaining >  LOOPCHUNKSIZE) ? LOOPCHUNKSIZE : loopremaining;

		// Add the chunk to the grand total.
		partialsum = partialsum + innerloop_asum_signed_char(loopchunk, &data[x]);
	}

	return partialsum;

}
#endif

/*--------------------------------------------------------------------------- */

/* For array code: b
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an error occured.
   Returns: The sum of the array.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
long long asum_signed_char_simd_ovfl(Py_ssize_t arraylen, signed char *data, signed int *errflag) { 

	long long partialsum = 0;
	long long chunksum;
	Py_ssize_t x, loopremaining, loopchunk;

	for(x=0; x < arraylen; x += LOOPCHUNKSIZE) {
		// The array is summed in "chunks" using SIMD and then each
		// chunk added to the total.
		loopremaining = arraylen - x;
		loopchunk = (loopremaining >  LOOPCHUNKSIZE) ? LOOPCHUNKSIZE : loopremaining;

		// Add up one "chunk" of the array.
		chunksum = innerloop_asum_signed_char(loopchunk, &data[x]);

		// Check for overflow.
		if (loop_willoverflow_signed(chunksum, partialsum)) {
			*errflag = ARR_ERR_OVFL;
			return partialsum; 
		}

		// Add the chunk to the grand total.
		partialsum = partialsum + chunksum;
	}

	return partialsum;

}
#endif

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

/* For array code: B
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// This inner loop is used to sum small chunks of the array.
#if defined(AF_HASSIMD_ARMv7_32BIT)
unsigned long long innerloop_asum_unsigned_char(Py_ssize_t arraylen, unsigned char *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	unsigned long long partialsum = 0;

	unsigned short sumvals[CHARSIMDSIZE / 2];
	uint8x8_t dataslice;
	uint16x4_t resultslice;


	// Initialise the accumulator.
	resultslice = vdup_n_u16(0);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Use SIMD.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {

		// Load the data into the vector register.
		dataslice = vld1_u8( &data[x]);

		// The actual SIMD operation. 
		resultslice = vpadal_u8(resultslice, dataslice);

	}

	// Add up the values within the slice.
	vst1_u16(sumvals, resultslice);
	for (y = 0; y < (CHARSIMDSIZE / 2); y++) {
		partialsum = partialsum + sumvals[y];
	}

	// Add the values within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}

	return partialsum;

}
#endif



/*--------------------------------------------------------------------------- */
/* For array code: B
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// Version without error checking.
#if defined(AF_HASSIMD_ARMv7_32BIT)
unsigned long long asum_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data) { 

	Py_ssize_t x, loopremaining, loopchunk;
	unsigned long long partialsum = 0;

	for(x=0; x < arraylen; x += LOOPCHUNKSIZE) {
		// The array is summed in "chunks" using SIMD and then each
		// chunk added to the total.
		loopremaining = arraylen - x;
		loopchunk = (loopremaining >  LOOPCHUNKSIZE) ? LOOPCHUNKSIZE : loopremaining;

		// Add the chunk to the grand total.
		partialsum = partialsum + innerloop_asum_unsigned_char(loopchunk, &data[x]);
	}

	return partialsum;

}
#endif

/*--------------------------------------------------------------------------- */

/* For array code: B
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an error occured.
   Returns: The sum of the array.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
unsigned long long asum_unsigned_char_simd_ovfl(Py_ssize_t arraylen, unsigned char *data, signed int *errflag) { 

	unsigned long long partialsum = 0;
	unsigned long long chunksum;
	Py_ssize_t x, loopremaining, loopchunk;

	for(x=0; x < arraylen; x += LOOPCHUNKSIZE) {
		// The array is summed in "chunks" using SIMD and then each
		// chunk added to the total.
		loopremaining = arraylen - x;
		loopchunk = (loopremaining >  LOOPCHUNKSIZE) ? LOOPCHUNKSIZE : loopremaining;

		// Add up one "chunk" of the array.
		chunksum = innerloop_asum_unsigned_char(loopchunk, &data[x]);

		// Check for overflow.
		if (loop_willoverflow_signed(chunksum, partialsum)) {
			*errflag = ARR_ERR_OVFL;
			return partialsum; 
		}

		// Add the chunk to the grand total.
		partialsum = partialsum + chunksum;
	}

	return partialsum;

}
#endif

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

/* For array code: h
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// This inner loop is used to sum small chunks of the array.
#if defined(AF_HASSIMD_ARMv7_32BIT)
long long innerloop_asum_signed_short(Py_ssize_t arraylen, signed short *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	long long partialsum = 0;

	signed int sumvals[SHORTSIMDSIZE / 2];
	int16x4_t dataslice;
	int32x2_t resultslice;


	// Initialise the accumulator.
	resultslice = vdup_n_s32(0);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Use SIMD.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {

		// Load the data into the vector register.
		dataslice = vld1_s16( &data[x]);

		// The actual SIMD operation. 
		resultslice = vpadal_s16(resultslice, dataslice);

	}

	// Add up the values within the slice.
	vst1_s32(sumvals, resultslice);
	for (y = 0; y < (SHORTSIMDSIZE / 2); y++) {
		partialsum = partialsum + sumvals[y];
	}

	// Add the values within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}

	return partialsum;

}
#endif



/*--------------------------------------------------------------------------- */
/* For array code: h
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// Version without error checking.
#if defined(AF_HASSIMD_ARMv7_32BIT)
long long asum_signed_short_simd(Py_ssize_t arraylen, signed short *data) { 

	Py_ssize_t x, loopremaining, loopchunk;
	long long partialsum = 0;

	for(x=0; x < arraylen; x += LOOPCHUNKSIZE) {
		// The array is summed in "chunks" using SIMD and then each
		// chunk added to the total.
		loopremaining = arraylen - x;
		loopchunk = (loopremaining >  LOOPCHUNKSIZE) ? LOOPCHUNKSIZE : loopremaining;

		// Add the chunk to the grand total.
		partialsum = partialsum + innerloop_asum_signed_short(loopchunk, &data[x]);
	}

	return partialsum;

}
#endif

/*--------------------------------------------------------------------------- */

/* For array code: h
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an error occured.
   Returns: The sum of the array.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
long long asum_signed_short_simd_ovfl(Py_ssize_t arraylen, signed short *data, signed int *errflag) { 

	long long partialsum = 0;
	long long chunksum;
	Py_ssize_t x, loopremaining, loopchunk;

	for(x=0; x < arraylen; x += LOOPCHUNKSIZE) {
		// The array is summed in "chunks" using SIMD and then each
		// chunk added to the total.
		loopremaining = arraylen - x;
		loopchunk = (loopremaining >  LOOPCHUNKSIZE) ? LOOPCHUNKSIZE : loopremaining;

		// Add up one "chunk" of the array.
		chunksum = innerloop_asum_signed_short(loopchunk, &data[x]);

		// Check for overflow.
		if (loop_willoverflow_signed(chunksum, partialsum)) {
			*errflag = ARR_ERR_OVFL;
			return partialsum; 
		}

		// Add the chunk to the grand total.
		partialsum = partialsum + chunksum;
	}

	return partialsum;

}
#endif

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

/* For array code: H
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// This inner loop is used to sum small chunks of the array.
#if defined(AF_HASSIMD_ARMv7_32BIT)
unsigned long long innerloop_asum_unsigned_short(Py_ssize_t arraylen, unsigned short *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	unsigned long long partialsum = 0;

	unsigned int sumvals[SHORTSIMDSIZE / 2];
	uint16x4_t dataslice;
	uint32x2_t resultslice;


	// Initialise the accumulator.
	resultslice = vdup_n_u32(0);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Use SIMD.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {

		// Load the data into the vector register.
		dataslice = vld1_u16( &data[x]);

		// The actual SIMD operation. 
		resultslice = vpadal_u16(resultslice, dataslice);

	}

	// Add up the values within the slice.
	vst1_u32(sumvals, resultslice);
	for (y = 0; y < (SHORTSIMDSIZE / 2); y++) {
		partialsum = partialsum + sumvals[y];
	}

	// Add the values within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}

	return partialsum;

}
#endif



/*--------------------------------------------------------------------------- */
/* For array code: H
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// Version without error checking.
#if defined(AF_HASSIMD_ARMv7_32BIT)
unsigned long long asum_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data) { 

	Py_ssize_t x, loopremaining, loopchunk;
	unsigned long long partialsum = 0;

	for(x=0; x < arraylen; x += LOOPCHUNKSIZE) {
		// The array is summed in "chunks" using SIMD and then each
		// chunk added to the total.
		loopremaining = arraylen - x;
		loopchunk = (loopremaining >  LOOPCHUNKSIZE) ? LOOPCHUNKSIZE : loopremaining;

		// Add the chunk to the grand total.
		partialsum = partialsum + innerloop_asum_unsigned_short(loopchunk, &data[x]);
	}

	return partialsum;

}
#endif

/*--------------------------------------------------------------------------- */

/* For array code: H
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an error occured.
   Returns: The sum of the array.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
unsigned long long asum_unsigned_short_simd_ovfl(Py_ssize_t arraylen, unsigned short *data, signed int *errflag) { 

	unsigned long long partialsum = 0;
	unsigned long long chunksum;
	Py_ssize_t x, loopremaining, loopchunk;

	for(x=0; x < arraylen; x += LOOPCHUNKSIZE) {
		// The array is summed in "chunks" using SIMD and then each
		// chunk added to the total.
		loopremaining = arraylen - x;
		loopchunk = (loopremaining >  LOOPCHUNKSIZE) ? LOOPCHUNKSIZE : loopremaining;

		// Add up one "chunk" of the array.
		chunksum = innerloop_asum_unsigned_short(loopchunk, &data[x]);

		// Check for overflow.
		if (loop_willoverflow_signed(chunksum, partialsum)) {
			*errflag = ARR_ERR_OVFL;
			return partialsum; 
		}

		// Add the chunk to the grand total.
		partialsum = partialsum + chunksum;
	}

	return partialsum;

}
#endif

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For array code: f
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// This inner loop is used to sum small chunks of the array.
#if defined(AF_HASSIMD_ARMv7_32BIT)
float asum_float_simd(Py_ssize_t arraylen, float *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	float partialsum = 0.0;

	float sumvals[FLOATSIMDSIZE];
	float32x2_t dataslice, resultslice;


	// Initialise the accumulator.
	resultslice = vdup_n_f32(0.0);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Use SIMD.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {

		// Load the data into the vector register.
		dataslice = vld1_f32( &data[x]);

		// The actual SIMD operation. 
		resultslice = vadd_f32(resultslice, dataslice);

	}

	// Add up the values within the slice.
	vst1_f32(sumvals, resultslice);
	for (y = 0; y < (FLOATSIMDSIZE); y++) {
		partialsum = partialsum + sumvals[y];
	}

	// Add the values within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}

	return partialsum;

}
#endif

/*--------------------------------------------------------------------------- */
/* For array code: f
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// This inner loop is used to sum small chunks of the array.
#if defined(AF_HASSIMD_ARMv7_32BIT)
float asum_float_simd_ovfl(Py_ssize_t arraylen, float *data, signed int *errflag) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	float partialsum = 0.0;

	float sumvals[FLOATSIMDSIZE];
	float32x2_t dataslice, resultslice;


	*errflag = 0;

	// Initialise the accumulator.
	resultslice = vdup_n_f32(0.0);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Use SIMD.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {

		// Load the data into the vector register.
		dataslice = vld1_f32( &data[x]);

		// The actual SIMD operation. 
		resultslice = vadd_f32(resultslice, dataslice);

	}

	// Add up the values within the slice.
	vst1_f32(sumvals, resultslice);
	for (y = 0; y < (FLOATSIMDSIZE); y++) {
		partialsum = partialsum + sumvals[y];
	}

	// Add the values within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}


	// If an error occured resulting in NaN or INF anywhere in the course of
	// the calculation it should have propagated through to the end and we will
	// find it here at the end.
	if (!isfinite(partialsum)) {
		*errflag = ARR_ERR_OVFL;
	}


	return partialsum;

}
#endif

