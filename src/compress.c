//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   compress.c
// Purpose:  Copy values from an array, using a selector array to filter values.
// Language: C
// Date:     10-May-2014.
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

#include <limits.h>
#include <math.h>

#include "arrayerrs.h"

#include "arrayparams_base.h"
#include "arrayops.h"

#include "arrayparams_compress.h"


/*--------------------------------------------------------------------------- */
/*--------------------------------------------------------------------------- */
/* For array code: b
   datalen = The length of the input array.
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

/*--------------------------------------------------------------------------- */
/* For array code: B
   datalen = The length of the input array.
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

/*--------------------------------------------------------------------------- */
/* For array code: h
   datalen = The length of the input array.
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

/*--------------------------------------------------------------------------- */
/* For array code: H
   datalen = The length of the input array.
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

/*--------------------------------------------------------------------------- */
/* For array code: i
   datalen = The length of the input array.
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

/*--------------------------------------------------------------------------- */
/* For array code: I
   datalen = The length of the input array.
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

/*--------------------------------------------------------------------------- */
/* For array code: l
   datalen = The length of the input array.
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

/*--------------------------------------------------------------------------- */
/* For array code: L
   datalen = The length of the input array.
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

/*--------------------------------------------------------------------------- */
/* For array code: q
   datalen = The length of the input array.
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

/*--------------------------------------------------------------------------- */
/* For array code: Q
   datalen = The length of the input array.
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

/*--------------------------------------------------------------------------- */
/* For array code: f
   datalen = The length of the input array.
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

/*--------------------------------------------------------------------------- */
/* For array code: d
   datalen = The length of the input array.
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


/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_compress(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	Py_ssize_t resultcode = 0;

	// This is used to hold the parsed parameters.
	struct args_params_compress arraydata = ARGSINIT_COMPRESS;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_compress(self, args, keywds, "compress");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}


	// The length of the data array.
	if (arraydata.arraylength1 < 1) {
		// Release the buffers. 
		releasebuffers_compress(arraydata);
		ErrMsgArrayLengthErr();
		return NULL;
	}



	/* Call the C function */
	switch(arraydata.arraytype) {
		// signed char
		case 'b' : {
			resultcode = compress_signed_char(arraydata.arraylength1, arraydata.array1.b, arraydata.arraylength2, arraydata.array2.b, arraydata.arraylength3, arraydata.array3.b);
			break;
		}
		// unsigned char
		case 'B' : {
			resultcode = compress_unsigned_char(arraydata.arraylength1, arraydata.array1.B, arraydata.arraylength2, arraydata.array2.B, arraydata.arraylength3, arraydata.array3.B);
			break;
		}
		// signed short
		case 'h' : {
			resultcode = compress_signed_short(arraydata.arraylength1, arraydata.array1.h, arraydata.arraylength2, arraydata.array2.h, arraydata.arraylength3, arraydata.array3.h);
			break;
		}
		// unsigned short
		case 'H' : {
			resultcode = compress_unsigned_short(arraydata.arraylength1, arraydata.array1.H, arraydata.arraylength2, arraydata.array2.H, arraydata.arraylength3, arraydata.array3.H);
			break;
		}
		// signed int
		case 'i' : {
			resultcode = compress_signed_int(arraydata.arraylength1, arraydata.array1.i, arraydata.arraylength2, arraydata.array2.i, arraydata.arraylength3, arraydata.array3.i);
			break;
		}
		// unsigned int
		case 'I' : {
			resultcode = compress_unsigned_int(arraydata.arraylength1, arraydata.array1.I, arraydata.arraylength2, arraydata.array2.I, arraydata.arraylength3, arraydata.array3.I);
			break;
		}
		// signed long
		case 'l' : {
			resultcode = compress_signed_long(arraydata.arraylength1, arraydata.array1.l, arraydata.arraylength2, arraydata.array2.l, arraydata.arraylength3, arraydata.array3.l);
			break;
		}
		// unsigned long
		case 'L' : {
			resultcode = compress_unsigned_long(arraydata.arraylength1, arraydata.array1.L, arraydata.arraylength2, arraydata.array2.L, arraydata.arraylength3, arraydata.array3.L);
			break;
		}
		// signed long long
		case 'q' : {
			resultcode = compress_signed_long_long(arraydata.arraylength1, arraydata.array1.q, arraydata.arraylength2, arraydata.array2.q, arraydata.arraylength3, arraydata.array3.q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultcode = compress_unsigned_long_long(arraydata.arraylength1, arraydata.array1.Q, arraydata.arraylength2, arraydata.array2.Q, arraydata.arraylength3, arraydata.array3.Q);
			break;
		}
		// float
		case 'f' : {
			resultcode = compress_float(arraydata.arraylength1, arraydata.array1.f, arraydata.arraylength2, arraydata.array2.f, arraydata.arraylength3, arraydata.array3.f);
			break;
		}
		// double
		case 'd' : {
			resultcode = compress_double(arraydata.arraylength1, arraydata.array1.d, arraydata.arraylength2, arraydata.array2.d, arraydata.arraylength3, arraydata.array3.d);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_compress(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_compress(arraydata);


	// Signal the errors.
	if (resultcode == ARR_ERR_INVALIDOP) {
		ErrMsgOperatorNotValidforthisFunction();
		return NULL;
	}


	// Adjust the result code if the data was not found, so that we don't leak
	// internal error codes to user space (and cause problems if they change).
	if (resultcode < 0) {
		resultcode = -1;
	}

	// Return the number of items filtered through.
	return PyLong_FromSsize_t(resultcode);

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(compress__doc__,
"compress \n\
_____________________________ \n\
\n\
Select values from an array based on another array of integers values. \n\
The selector array is interpreted as a set of boolean values, where any \n\
value other than *0* causes the value in the input array to be selected \n\
and copied to theoutput array, while a value of *0* causes the value to \n\
be ignored.\n\
\n\
======================  ============================================== \n\
Equivalent to:          itertools.compress(inparray, selectorarray) \n\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
  x = compress(inparray, outparray, selectorarray) \n\
  x = compress(inparray, outparray, selectorarray, maxlen=y) \n\
\n\
* inparray - The input data array to be filtered. \n\
* outparray - The output array. \n\
* selectorarray - The selector array. \n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored. \n\
* x - An integer count of the number of items filtered into outparray. \n\
");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "compress" is the name seen inside of Python. 
 "py_compress" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef compress_methods[] = {
	{"compress",  (PyCFunction)py_compress, METH_VARARGS | METH_KEYWORDS, compress__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef compressmodule = {
    PyModuleDef_HEAD_INIT,
    "compress",
    NULL,
    -1,
    compress_methods
};

PyMODINIT_FUNC PyInit_compress(void)
{
    return PyModule_Create(&compressmodule);
};

/*--------------------------------------------------------------------------- */

