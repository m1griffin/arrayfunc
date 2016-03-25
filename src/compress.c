//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   compress.c
// Purpose:  Copy values from an array, using a selector array to filter values.
// Language: C
// Date:     10-May-2014
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2015    Michael Griffin    <m12.griffin@gmail.com>
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

#include "arrayfunc.h"
#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */


// Provide a struct for returning data from parsing Python arguments.
struct args_param {
	char array1type;
	char array2type;
	char array3type;
	char error;
};

// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist[] = {"data", "dataout", "selecdtor", "maxlen", NULL};

/*--------------------------------------------------------------------------- */

// Auto-generated code goes below.

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


/*--------------------------------------------------------------------------- */

/* Parse the Python arguments to objects, and then extract the object parameters
 * to determine their types. This lets us handle different data types as 
 * parameters.
 * This version expects the following parameters:
 * args (PyObject) = The positional arguments.
 * Returns a structure containing the results of each parameter.
*/
struct args_param parsepyargs_parm(PyObject *args, PyObject *keywds) {

	PyObject *dataobj, *dataoutobj, *selectorobj;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	struct args_param argtypes = {' ', ' ', ' ', 0};
	struct arrayparamstypes arr1type = {0, 0, ' '};
	struct arrayparamstypes arr2type = {0, 0, ' '};
	struct arrayparamstypes arr3type = {0, 0, ' '};


	/* Import the raw objects. */
	if (!PyArg_ParseTupleAndKeywords(args,keywds, "OOO|l:compress", kwlist, 
			&dataobj, &dataoutobj, &selectorobj, &arraymaxlen)) {
		argtypes.error = 1;
		return argtypes;
	}


	// Test if the first parameter is an array or bytes.
	arr1type = paramarraytype(dataobj);
	if (!arr1type.isarray) {
		argtypes.error = 2;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.array1type = arr1type.arraycode;
	}


	// Test if the second parameter is an array or bytes.
	arr2type = paramarraytype(dataoutobj);
	if (!arr2type.isarray) {
		argtypes.error = 3;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.array2type = arr2type.arraycode;
	}


	// Test if the third parameter is an array or bytes.
	arr3type = paramarraytype(selectorobj);
	if (!arr3type.isarray) {
		argtypes.error = 3;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.array3type = arr3type.arraycode;
	}


	return argtypes;

}


/*--------------------------------------------------------------------------- */


/* The wrapper to the underlying C function */
static PyObject *py_compress(PyObject *self, PyObject *args, PyObject *keywds) {


	// The array of data we work on. 
	union dataarrays data, dataout, selector;

	// The input buffers are arrays of bytes.
	Py_buffer datapy, dataoutpy, selectorpy;

	// The length of the data array.
	Py_ssize_t databufflength, dataoutbufflength, selectorbufflength;

	// This is used to hold the results from inspecting the Python args.
	struct args_param argtypes;

	// Codes indicating the type of array.
	char itemcode;

	// How long the array is, and the error code returned by the function.
	Py_ssize_t datalen, outlen, selectorlen, resultcode;
	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;


	// -------------------------------------------------------------------------


	// Check the parameters to see what they are.
	argtypes = parsepyargs_parm(args, keywds);


	// There was an error reading the parameter types.
	if (argtypes.error) {
		ErrMsgParameterError();
		return NULL;
	}

	// All array types must be the same.
	if ((argtypes.array1type != argtypes.array2type) || (argtypes.array1type != argtypes.array3type)) {
		ErrMsgArrayTypeMismatch();
		return NULL;
	}


	itemcode = argtypes.array1type;

	// Now we will fetch the actual array data. Since all of these parameters
	// are arrays, we don't have to worry about the data type at this point.
	// The format string and parameter names depend on the expected data types.
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "y*y*y*|l:compress", kwlist, 
		&datapy, &dataoutpy, &selectorpy, &arraymaxlen)) {
		return NULL;
	}

	// Assign the buffer to a union which lets us get at them as typed data.
	data.buf = datapy.buf;
	dataout.buf = dataoutpy.buf;
	selector.buf = selectorpy.buf;


	// The length of the input data array.
	databufflength = datapy.len;
	dataoutbufflength = dataoutpy.len;
	selectorbufflength = selectorpy.len;

	datalen = calcarraylength(itemcode, databufflength);
	if (datalen < 1) {
		PyBuffer_Release(&datapy);
		PyBuffer_Release(&dataoutpy);
		PyBuffer_Release(&selectorpy);
		ErrMsgArrayLengthInput();
		return NULL;
	}

	// The length of the output data array.
	outlen = calcarraylength(itemcode, dataoutbufflength);
	if (outlen < 1) {
		PyBuffer_Release(&datapy);
		PyBuffer_Release(&dataoutpy);
		PyBuffer_Release(&selectorpy);
		ErrMsgArrayLengthOutput();
		return NULL;
	}

	// The length of the selector data array.
	selectorlen = calcarraylength(itemcode, selectorbufflength);
	if (selectorlen < 1) {
		PyBuffer_Release(&datapy);
		PyBuffer_Release(&dataoutpy);
		PyBuffer_Release(&selectorpy);
		ErrMsgArrayLengthSelector();
		return NULL;
	}


	// Adjust the length of array being operated on, if necessary.
	// We don't check the lengths of the output or selector arrays here, because
	// we check for them as we go along during the conversion.
	datalen = adjustarraymaxlen(datalen, arraymaxlen);


	/* Call the C function */
	switch(itemcode) {
		// signed char
		case 'b' : {
			resultcode = compress_signed_char(datalen, data.b, outlen, dataout.b, selectorlen, selector.b);
			break;
		}
		// unsigned char
		case 'B' : {
			resultcode = compress_unsigned_char(datalen, data.B, outlen, dataout.B, selectorlen, selector.B);
			break;
		}
		// signed short
		case 'h' : {
			resultcode = compress_signed_short(datalen, data.h, outlen, dataout.h, selectorlen, selector.h);
			break;
		}
		// unsigned short
		case 'H' : {
			resultcode = compress_unsigned_short(datalen, data.H, outlen, dataout.H, selectorlen, selector.H);
			break;
		}
		// signed int
		case 'i' : {
			resultcode = compress_signed_int(datalen, data.i, outlen, dataout.i, selectorlen, selector.i);
			break;
		}
		// unsigned int
		case 'I' : {
			resultcode = compress_unsigned_int(datalen, data.I, outlen, dataout.I, selectorlen, selector.I);
			break;
		}
		// signed long
		case 'l' : {
			resultcode = compress_signed_long(datalen, data.l, outlen, dataout.l, selectorlen, selector.l);
			break;
		}
		// unsigned long
		case 'L' : {
			resultcode = compress_unsigned_long(datalen, data.L, outlen, dataout.L, selectorlen, selector.L);
			break;
		}
		// signed long long
		case 'q' : {
			resultcode = compress_signed_long_long(datalen, data.q, outlen, dataout.q, selectorlen, selector.q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultcode = compress_unsigned_long_long(datalen, data.Q, outlen, dataout.Q, selectorlen, selector.Q);
			break;
		}
		// float
		case 'f' : {
			resultcode = compress_float(datalen, data.f, outlen, dataout.f, selectorlen, selector.f);
			break;
		}
		// double
		case 'd' : {
			resultcode = compress_double(datalen, data.d, outlen, dataout.d, selectorlen, selector.d);
			break;
		}
		// We don't know this code.
		default: {
			PyBuffer_Release(&datapy);
			PyBuffer_Release(&dataoutpy);
			PyBuffer_Release(&selectorpy);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	PyBuffer_Release(&datapy);
	PyBuffer_Release(&dataoutpy);
	PyBuffer_Release(&selectorpy);


	// Return the number of items filtered through.
	return PyLong_FromLong(resultcode);


}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(compress__doc__,
"Select values from an array based on another array of integers values. \n\
The selector array is interpreted as a set of boolean values, where any \n\
value other than *0* causes the value in the input array to be selected \n\
and copied to theoutput array, while a value of *0* causes the value to \n\
be ignored.\n\
\n\
The input, selector, and output arrays need not be of the same length. \n\
The copy operation will be terminated when the end of the input or \n\
output array is reached. The selector array will be cycled through \n\
repeatedly as many times as necessary until the end of the input or \n\
output array is reached. \n\
\n\
x = compress(inparray, outparray, selectorarray)\n\
x = compress(inparray, outparray, selectorarray, maxlen=y)\n\
\n\
* inparray - The input data array to be filtered.\n\
* outparray - The output array.\n\
* selectorarray - The selector array.\n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored.\n\
* x - An integer count of the number of items filtered into outparray.");


/*--------------------------------------------------------------------------- */


/* A list of all the methods defined by this module. 
 "compress" is the name seen inside of Python. 
 "py_compress" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef compress_methods[] = {
	{"compress",  (PyCFunction) py_compress, METH_VARARGS | METH_KEYWORDS, compress__doc__}, 
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
