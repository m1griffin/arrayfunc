//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   asum_simd_x86.c
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
#if defined(AF_HASSIMD_X86)
long long innerloop_asum_signed_char(Py_ssize_t arraylen, signed char *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	long long partialsum = 0;

	signed short sumvals[CHARSIMDSIZE / 2];
	v16qi loadslice1, loadslice2;
	v8hi sumslice1, sumslice2, sumslicetotal, dataslice1, dataslice2;
	v16qi shufflebytes;

	signed char initvals[16] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	signed char shufflemask[16] = {8, 9, 10, 11, 12, 13, 14, 15, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff};


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, CHARSIMDSIZE);

	// Initialise the sum values.
	sumslice1 = (v8hi) __builtin_ia32_lddqu((char *)  initvals);
	sumslice2 = (v8hi) __builtin_ia32_lddqu((char *)  initvals);

	// This is used with alternate means of moving high bytes to low bytes.
	shufflebytes = (v16qi) __builtin_ia32_lddqu((char *)  shufflemask);


	// Use SIMD.
	for (x = 0; x < alignedlength; x += CHARSIMDSIZE) {
		loadslice1 = (v16qi) __builtin_ia32_lddqu((char *)  &data[x]);

		// Shuffle the high bytes into the low bytes for the second vector.
		loadslice2 = (v16qi) __builtin_ia32_pshufb128( (v16qi) loadslice1, shufflebytes);


		// Split the vector into two smaller ones.
		dataslice1 = __builtin_ia32_pmovsxbw128(loadslice1);
		dataslice2 = __builtin_ia32_pmovsxbw128(loadslice2);


		// Add each half vector.
		sumslice1 = __builtin_ia32_paddw128(sumslice1, dataslice1);
		sumslice2 = __builtin_ia32_paddw128(sumslice2, dataslice2);

	}


	// Add the two half vectors together.
	sumslicetotal = (v8hi) __builtin_ia32_paddw128(sumslice1, sumslice2);


	// Add up the values within the slice.
	__builtin_ia32_storedqu((char *) sumvals, (v16qi) sumslicetotal);


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
#if defined(AF_HASSIMD_X86)
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
#if defined(AF_HASSIMD_X86)
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
/* For array code: h
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// This inner loop is used to sum small chunks of the array.
#if defined(AF_HASSIMD_X86)
long long innerloop_asum_signed_short(Py_ssize_t arraylen, signed short *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	long long partialsum = 0;

	signed int sumvals[SHORTSIMDSIZE / 2];
	v8hi loadslice1, loadslice2;
	v4si sumslice1, sumslice2, sumslicetotal, dataslice1, dataslice2;
	v16qi shufflebytes;

	signed char initvals[16] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	signed char shufflemask[16] = {8, 9, 10, 11, 12, 13, 14, 15, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff};


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, SHORTSIMDSIZE);

	// Initialise the sum values.
	sumslice1 = (v4si) __builtin_ia32_lddqu((char *)  initvals);
	sumslice2 = (v4si) __builtin_ia32_lddqu((char *)  initvals);

	// This is used with alternate means of moving high bytes to low bytes.
	shufflebytes = (v16qi) __builtin_ia32_lddqu((char *)  shufflemask);


	// Use SIMD.
	for (x = 0; x < alignedlength; x += SHORTSIMDSIZE) {
		loadslice1 = (v8hi) __builtin_ia32_lddqu((char *)  &data[x]);

		// Shuffle the high bytes into the low bytes for the second vector.
		loadslice2 = (v8hi) __builtin_ia32_pshufb128( (v16qi) loadslice1, shufflebytes);


		// Split the vector into two smaller ones.
		dataslice1 = __builtin_ia32_pmovsxwd128(loadslice1);
		dataslice2 = __builtin_ia32_pmovsxwd128(loadslice2);


		// Add each half vector.
		sumslice1 = __builtin_ia32_paddd128(sumslice1, dataslice1);
		sumslice2 = __builtin_ia32_paddd128(sumslice2, dataslice2);

	}


	// Add the two half vectors together.
	sumslicetotal = (v4si) __builtin_ia32_paddd128(sumslice1, sumslice2);


	// Add up the values within the slice.
	__builtin_ia32_storedqu((char *) sumvals, (v16qi) sumslicetotal);


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
#if defined(AF_HASSIMD_X86)
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
#if defined(AF_HASSIMD_X86)
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
/* For array code: i
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// This inner loop is used to sum small chunks of the array.
#if defined(AF_HASSIMD_X86)
long long innerloop_asum_signed_int(Py_ssize_t arraylen, signed int *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	long long partialsum = 0;

	signed long sumvals[INTSIMDSIZE / 2];
	v4si loadslice1, loadslice2;
	v2di sumslice1, sumslice2, sumslicetotal, dataslice1, dataslice2;
	v16qi shufflebytes;

	signed char initvals[16] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	signed char shufflemask[16] = {8, 9, 10, 11, 12, 13, 14, 15, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff};


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, INTSIMDSIZE);

	// Initialise the sum values.
	sumslice1 = (v2di) __builtin_ia32_lddqu((char *)  initvals);
	sumslice2 = (v2di) __builtin_ia32_lddqu((char *)  initvals);

	// This is used with alternate means of moving high bytes to low bytes.
	shufflebytes = (v16qi) __builtin_ia32_lddqu((char *)  shufflemask);


	// Use SIMD.
	for (x = 0; x < alignedlength; x += INTSIMDSIZE) {
		loadslice1 = (v4si) __builtin_ia32_lddqu((char *)  &data[x]);

		// Shuffle the high bytes into the low bytes for the second vector.
		loadslice2 = (v4si) __builtin_ia32_pshufb128( (v16qi) loadslice1, shufflebytes);


		// Split the vector into two smaller ones.
		dataslice1 = __builtin_ia32_pmovsxdq128(loadslice1);
		dataslice2 = __builtin_ia32_pmovsxdq128(loadslice2);


		// Add each half vector.
		sumslice1 = __builtin_ia32_paddq128(sumslice1, dataslice1);
		sumslice2 = __builtin_ia32_paddq128(sumslice2, dataslice2);

	}


	// Add the two half vectors together.
	sumslicetotal = (v2di) __builtin_ia32_paddq128(sumslice1, sumslice2);


	// Add up the values within the slice.
	__builtin_ia32_storedqu((char *) sumvals, (v16qi) sumslicetotal);


	for (y = 0; y < (INTSIMDSIZE / 2); y++) {
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
/* For array code: i
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// Version without error checking.
#if defined(AF_HASSIMD_X86)
long long asum_signed_int_simd(Py_ssize_t arraylen, signed int *data) { 

	Py_ssize_t x, loopremaining, loopchunk;
	long long partialsum = 0;

	for(x=0; x < arraylen; x += LOOPCHUNKSIZE) {
		// The array is summed in "chunks" using SIMD and then each
		// chunk added to the total.
		loopremaining = arraylen - x;
		loopchunk = (loopremaining >  LOOPCHUNKSIZE) ? LOOPCHUNKSIZE : loopremaining;

		// Add the chunk to the grand total.
		partialsum = partialsum + innerloop_asum_signed_int(loopchunk, &data[x]);
	}

	return partialsum;

}
#endif

/*--------------------------------------------------------------------------- */

/* For array code: i
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an error occured.
   Returns: The sum of the array.
*/
#if defined(AF_HASSIMD_X86)
long long asum_signed_int_simd_ovfl(Py_ssize_t arraylen, signed int *data, signed int *errflag) { 

	long long partialsum = 0;
	long long chunksum;
	Py_ssize_t x, loopremaining, loopchunk;

	for(x=0; x < arraylen; x += LOOPCHUNKSIZE) {
		// The array is summed in "chunks" using SIMD and then each
		// chunk added to the total.
		loopremaining = arraylen - x;
		loopchunk = (loopremaining >  LOOPCHUNKSIZE) ? LOOPCHUNKSIZE : loopremaining;

		// Add up one "chunk" of the array.
		chunksum = innerloop_asum_signed_int(loopchunk, &data[x]);

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
   errflag = Set to true if an error occured.
   Returns: The sum of the array.
*/
// Version without error checking.
#if defined(AF_HASSIMD_X86)
float asum_float_simd(Py_ssize_t arraylen, float *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	float partialsum = 0.0;

	float sumvals[FLOATSIMDSIZE];
	v4sf sumslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Initialise the sum values.
	sumslice = (v4sf) __builtin_ia32_loadups(data);

	// Use SIMD.
	for (x = FLOATSIMDSIZE; x < alignedlength; x += FLOATSIMDSIZE) {
		dataslice = (v4sf) __builtin_ia32_loadups(&data[x]);
		sumslice = __builtin_ia32_addps(sumslice, dataslice);
	}

	// Add up the values within the slice.
	__builtin_ia32_storeups(sumvals, (v4sf) sumslice);
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		partialsum = partialsum + sumvals[y];
	}

	// Add the values within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}


	return partialsum;
}

/*--------------------------------------------------------------------------- */

// Version with error checking.
float asum_float_simd_ovfl(Py_ssize_t arraylen, float *data, signed int *errflag) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	float partialsum = 0.0;

	float sumvals[FLOATSIMDSIZE];
	v4sf sumslice, dataslice;


	*errflag = 0;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);

	// Initialise the sum values.
	sumslice = (v4sf) __builtin_ia32_loadups(data);

	// Use SIMD.
	for (x = FLOATSIMDSIZE; x < alignedlength; x += FLOATSIMDSIZE) {
		dataslice = (v4sf) __builtin_ia32_loadups(&data[x]);
		sumslice = __builtin_ia32_addps(sumslice, dataslice);
	}

	// Add up the values within the slice.
	__builtin_ia32_storeups(sumvals, (v4sf) sumslice);
	for (y = 0; y < FLOATSIMDSIZE; y++) {
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
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: d
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an error occured.
   Returns: The sum of the array.
*/
// Version without error checking.
#if defined(AF_HASSIMD_X86)
double asum_double_simd(Py_ssize_t arraylen, double *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	double partialsum = 0.0;

	double sumvals[DOUBLESIMDSIZE];
	v2df sumslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Initialise the sum values.
	sumslice = (v2df) __builtin_ia32_loadupd(data);

	// Use SIMD.
	for (x = DOUBLESIMDSIZE; x < alignedlength; x += DOUBLESIMDSIZE) {
		dataslice = (v2df) __builtin_ia32_loadupd(&data[x]);
		sumslice = __builtin_ia32_addpd(sumslice, dataslice);
	}

	// Add up the values within the slice.
	__builtin_ia32_storeupd(sumvals, (v2df) sumslice);
	for (y = 0; y < DOUBLESIMDSIZE; y++) {
		partialsum = partialsum + sumvals[y];
	}

	// Add the values within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}


	return partialsum;
}

/*--------------------------------------------------------------------------- */

// Version with error checking.
double asum_double_simd_ovfl(Py_ssize_t arraylen, double *data, signed int *errflag) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	double partialsum = 0.0;

	double sumvals[DOUBLESIMDSIZE];
	v2df sumslice, dataslice;


	*errflag = 0;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);

	// Initialise the sum values.
	sumslice = (v2df) __builtin_ia32_loadupd(data);

	// Use SIMD.
	for (x = DOUBLESIMDSIZE; x < alignedlength; x += DOUBLESIMDSIZE) {
		dataslice = (v2df) __builtin_ia32_loadupd(&data[x]);
		sumslice = __builtin_ia32_addpd(sumslice, dataslice);
	}

	// Add up the values within the slice.
	__builtin_ia32_storeupd(sumvals, (v2df) sumslice);
	for (y = 0; y < DOUBLESIMDSIZE; y++) {
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
/*--------------------------------------------------------------------------- */
