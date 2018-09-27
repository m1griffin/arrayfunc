//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   compress_common.c
// Purpose:  Copy values from an array, using a selector array to filter values.
//           Common platform independent code.
// Language: C
// Date:     10-May-2014
// Ver:      19-Jun-2018.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2018    Michael Griffin    <m12.griffin@gmail.com>
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

#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// Auto generated code goes below.
/*--------------------------------------------------------------------------- */
/* datalen = The length of the input array.
   data = The input data array.
   outlen = The length of the output array.
   dataout = The output data array.
   selectorlen = The length of the selector array.
   selector = The array of filter values.
   Returns a positive integer indicating the number of input elements 
         copied to the output array.
*/
Py_ssize_t compress_signed_char(Py_ssize_t datalen, signed char *data, 
			Py_ssize_t outlen, signed char *dataout, 
			Py_ssize_t selectorlen, signed char *selector) { 

	// Array index counter. 
	Py_ssize_t index, outindex, selectorindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;
	selectorindex = 0;

	for(index = 0; index < datalen; index++) {
		// Check if the output index is within bounds.
		if (outindex >= outlen) {
			break;
		}
		// If we reach the end of the selector array, start again from the start.
		if (selectorindex >= selectorlen) {
			selectorindex = 0;
		}
		// Copy the data.
		if (selector[selectorindex]) {
			dataout[outindex] = data[index];
			outindex++;
		}
		// We need to advance the selector index for each input index.
		selectorindex++;
	}
	return outindex;
}
/*--------------------------------------------------------------------------- */
/* datalen = The length of the input array.
   data = The input data array.
   outlen = The length of the output array.
   dataout = The output data array.
   selectorlen = The length of the selector array.
   selector = The array of filter values.
   Returns a positive integer indicating the number of input elements 
         copied to the output array.
*/
Py_ssize_t compress_unsigned_char(Py_ssize_t datalen, unsigned char *data, 
			Py_ssize_t outlen, unsigned char *dataout, 
			Py_ssize_t selectorlen, unsigned char *selector) { 

	// Array index counter. 
	Py_ssize_t index, outindex, selectorindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;
	selectorindex = 0;

	for(index = 0; index < datalen; index++) {
		// Check if the output index is within bounds.
		if (outindex >= outlen) {
			break;
		}
		// If we reach the end of the selector array, start again from the start.
		if (selectorindex >= selectorlen) {
			selectorindex = 0;
		}
		// Copy the data.
		if (selector[selectorindex]) {
			dataout[outindex] = data[index];
			outindex++;
		}
		// We need to advance the selector index for each input index.
		selectorindex++;
	}
	return outindex;
}
/*--------------------------------------------------------------------------- */
/* datalen = The length of the input array.
   data = The input data array.
   outlen = The length of the output array.
   dataout = The output data array.
   selectorlen = The length of the selector array.
   selector = The array of filter values.
   Returns a positive integer indicating the number of input elements 
         copied to the output array.
*/
Py_ssize_t compress_signed_short(Py_ssize_t datalen, signed short *data, 
			Py_ssize_t outlen, signed short *dataout, 
			Py_ssize_t selectorlen, signed short *selector) { 

	// Array index counter. 
	Py_ssize_t index, outindex, selectorindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;
	selectorindex = 0;

	for(index = 0; index < datalen; index++) {
		// Check if the output index is within bounds.
		if (outindex >= outlen) {
			break;
		}
		// If we reach the end of the selector array, start again from the start.
		if (selectorindex >= selectorlen) {
			selectorindex = 0;
		}
		// Copy the data.
		if (selector[selectorindex]) {
			dataout[outindex] = data[index];
			outindex++;
		}
		// We need to advance the selector index for each input index.
		selectorindex++;
	}
	return outindex;
}
/*--------------------------------------------------------------------------- */
/* datalen = The length of the input array.
   data = The input data array.
   outlen = The length of the output array.
   dataout = The output data array.
   selectorlen = The length of the selector array.
   selector = The array of filter values.
   Returns a positive integer indicating the number of input elements 
         copied to the output array.
*/
Py_ssize_t compress_unsigned_short(Py_ssize_t datalen, unsigned short *data, 
			Py_ssize_t outlen, unsigned short *dataout, 
			Py_ssize_t selectorlen, unsigned short *selector) { 

	// Array index counter. 
	Py_ssize_t index, outindex, selectorindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;
	selectorindex = 0;

	for(index = 0; index < datalen; index++) {
		// Check if the output index is within bounds.
		if (outindex >= outlen) {
			break;
		}
		// If we reach the end of the selector array, start again from the start.
		if (selectorindex >= selectorlen) {
			selectorindex = 0;
		}
		// Copy the data.
		if (selector[selectorindex]) {
			dataout[outindex] = data[index];
			outindex++;
		}
		// We need to advance the selector index for each input index.
		selectorindex++;
	}
	return outindex;
}
/*--------------------------------------------------------------------------- */
/* datalen = The length of the input array.
   data = The input data array.
   outlen = The length of the output array.
   dataout = The output data array.
   selectorlen = The length of the selector array.
   selector = The array of filter values.
   Returns a positive integer indicating the number of input elements 
         copied to the output array.
*/
Py_ssize_t compress_signed_int(Py_ssize_t datalen, signed int *data, 
			Py_ssize_t outlen, signed int *dataout, 
			Py_ssize_t selectorlen, signed int *selector) { 

	// Array index counter. 
	Py_ssize_t index, outindex, selectorindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;
	selectorindex = 0;

	for(index = 0; index < datalen; index++) {
		// Check if the output index is within bounds.
		if (outindex >= outlen) {
			break;
		}
		// If we reach the end of the selector array, start again from the start.
		if (selectorindex >= selectorlen) {
			selectorindex = 0;
		}
		// Copy the data.
		if (selector[selectorindex]) {
			dataout[outindex] = data[index];
			outindex++;
		}
		// We need to advance the selector index for each input index.
		selectorindex++;
	}
	return outindex;
}
/*--------------------------------------------------------------------------- */
/* datalen = The length of the input array.
   data = The input data array.
   outlen = The length of the output array.
   dataout = The output data array.
   selectorlen = The length of the selector array.
   selector = The array of filter values.
   Returns a positive integer indicating the number of input elements 
         copied to the output array.
*/
Py_ssize_t compress_unsigned_int(Py_ssize_t datalen, unsigned int *data, 
			Py_ssize_t outlen, unsigned int *dataout, 
			Py_ssize_t selectorlen, unsigned int *selector) { 

	// Array index counter. 
	Py_ssize_t index, outindex, selectorindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;
	selectorindex = 0;

	for(index = 0; index < datalen; index++) {
		// Check if the output index is within bounds.
		if (outindex >= outlen) {
			break;
		}
		// If we reach the end of the selector array, start again from the start.
		if (selectorindex >= selectorlen) {
			selectorindex = 0;
		}
		// Copy the data.
		if (selector[selectorindex]) {
			dataout[outindex] = data[index];
			outindex++;
		}
		// We need to advance the selector index for each input index.
		selectorindex++;
	}
	return outindex;
}
/*--------------------------------------------------------------------------- */
/* datalen = The length of the input array.
   data = The input data array.
   outlen = The length of the output array.
   dataout = The output data array.
   selectorlen = The length of the selector array.
   selector = The array of filter values.
   Returns a positive integer indicating the number of input elements 
         copied to the output array.
*/
Py_ssize_t compress_signed_long(Py_ssize_t datalen, signed long *data, 
			Py_ssize_t outlen, signed long *dataout, 
			Py_ssize_t selectorlen, signed long *selector) { 

	// Array index counter. 
	Py_ssize_t index, outindex, selectorindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;
	selectorindex = 0;

	for(index = 0; index < datalen; index++) {
		// Check if the output index is within bounds.
		if (outindex >= outlen) {
			break;
		}
		// If we reach the end of the selector array, start again from the start.
		if (selectorindex >= selectorlen) {
			selectorindex = 0;
		}
		// Copy the data.
		if (selector[selectorindex]) {
			dataout[outindex] = data[index];
			outindex++;
		}
		// We need to advance the selector index for each input index.
		selectorindex++;
	}
	return outindex;
}
/*--------------------------------------------------------------------------- */
/* datalen = The length of the input array.
   data = The input data array.
   outlen = The length of the output array.
   dataout = The output data array.
   selectorlen = The length of the selector array.
   selector = The array of filter values.
   Returns a positive integer indicating the number of input elements 
         copied to the output array.
*/
Py_ssize_t compress_unsigned_long(Py_ssize_t datalen, unsigned long *data, 
			Py_ssize_t outlen, unsigned long *dataout, 
			Py_ssize_t selectorlen, unsigned long *selector) { 

	// Array index counter. 
	Py_ssize_t index, outindex, selectorindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;
	selectorindex = 0;

	for(index = 0; index < datalen; index++) {
		// Check if the output index is within bounds.
		if (outindex >= outlen) {
			break;
		}
		// If we reach the end of the selector array, start again from the start.
		if (selectorindex >= selectorlen) {
			selectorindex = 0;
		}
		// Copy the data.
		if (selector[selectorindex]) {
			dataout[outindex] = data[index];
			outindex++;
		}
		// We need to advance the selector index for each input index.
		selectorindex++;
	}
	return outindex;
}
/*--------------------------------------------------------------------------- */
/* datalen = The length of the input array.
   data = The input data array.
   outlen = The length of the output array.
   dataout = The output data array.
   selectorlen = The length of the selector array.
   selector = The array of filter values.
   Returns a positive integer indicating the number of input elements 
         copied to the output array.
*/
Py_ssize_t compress_signed_long_long(Py_ssize_t datalen, signed long long *data, 
			Py_ssize_t outlen, signed long long *dataout, 
			Py_ssize_t selectorlen, signed long long *selector) { 

	// Array index counter. 
	Py_ssize_t index, outindex, selectorindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;
	selectorindex = 0;

	for(index = 0; index < datalen; index++) {
		// Check if the output index is within bounds.
		if (outindex >= outlen) {
			break;
		}
		// If we reach the end of the selector array, start again from the start.
		if (selectorindex >= selectorlen) {
			selectorindex = 0;
		}
		// Copy the data.
		if (selector[selectorindex]) {
			dataout[outindex] = data[index];
			outindex++;
		}
		// We need to advance the selector index for each input index.
		selectorindex++;
	}
	return outindex;
}
/*--------------------------------------------------------------------------- */
/* datalen = The length of the input array.
   data = The input data array.
   outlen = The length of the output array.
   dataout = The output data array.
   selectorlen = The length of the selector array.
   selector = The array of filter values.
   Returns a positive integer indicating the number of input elements 
         copied to the output array.
*/
Py_ssize_t compress_unsigned_long_long(Py_ssize_t datalen, unsigned long long *data, 
			Py_ssize_t outlen, unsigned long long *dataout, 
			Py_ssize_t selectorlen, unsigned long long *selector) { 

	// Array index counter. 
	Py_ssize_t index, outindex, selectorindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;
	selectorindex = 0;

	for(index = 0; index < datalen; index++) {
		// Check if the output index is within bounds.
		if (outindex >= outlen) {
			break;
		}
		// If we reach the end of the selector array, start again from the start.
		if (selectorindex >= selectorlen) {
			selectorindex = 0;
		}
		// Copy the data.
		if (selector[selectorindex]) {
			dataout[outindex] = data[index];
			outindex++;
		}
		// We need to advance the selector index for each input index.
		selectorindex++;
	}
	return outindex;
}
/*--------------------------------------------------------------------------- */
/* datalen = The length of the input array.
   data = The input data array.
   outlen = The length of the output array.
   dataout = The output data array.
   selectorlen = The length of the selector array.
   selector = The array of filter values.
   Returns a positive integer indicating the number of input elements 
         copied to the output array.
*/
Py_ssize_t compress_float(Py_ssize_t datalen, float *data, 
			Py_ssize_t outlen, float *dataout, 
			Py_ssize_t selectorlen, float *selector) { 

	// Array index counter. 
	Py_ssize_t index, outindex, selectorindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;
	selectorindex = 0;

	for(index = 0; index < datalen; index++) {
		// Check if the output index is within bounds.
		if (outindex >= outlen) {
			break;
		}
		// If we reach the end of the selector array, start again from the start.
		if (selectorindex >= selectorlen) {
			selectorindex = 0;
		}
		// Copy the data.
		if (selector[selectorindex]) {
			dataout[outindex] = data[index];
			outindex++;
		}
		// We need to advance the selector index for each input index.
		selectorindex++;
	}
	return outindex;
}
/*--------------------------------------------------------------------------- */
/* datalen = The length of the input array.
   data = The input data array.
   outlen = The length of the output array.
   dataout = The output data array.
   selectorlen = The length of the selector array.
   selector = The array of filter values.
   Returns a positive integer indicating the number of input elements 
         copied to the output array.
*/
Py_ssize_t compress_double(Py_ssize_t datalen, double *data, 
			Py_ssize_t outlen, double *dataout, 
			Py_ssize_t selectorlen, double *selector) { 

	// Array index counter. 
	Py_ssize_t index, outindex, selectorindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;
	selectorindex = 0;

	for(index = 0; index < datalen; index++) {
		// Check if the output index is within bounds.
		if (outindex >= outlen) {
			break;
		}
		// If we reach the end of the selector array, start again from the start.
		if (selectorindex >= selectorlen) {
			selectorindex = 0;
		}
		// Copy the data.
		if (selector[selectorindex]) {
			dataout[outindex] = data[index];
			outindex++;
		}
		// We need to advance the selector index for each input index.
		selectorindex++;
	}
	return outindex;
}
/*--------------------------------------------------------------------------- */
