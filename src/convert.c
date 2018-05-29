//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   convert.c
// Purpose:  Convert arrays between data types.
// Language: C
// Date:     08-May-2014
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

#include "arrayparams_base.h"
#include "arrayerrs.h"

#include "convert_common.h"

/*--------------------------------------------------------------------------- */


// Provide a struct for returning data from parsing Python arguments.
struct args_param {
	char array1type;
	char param1type;
	char error;
};


// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist[] = {"data", "dataout", "maxlen", NULL};

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */


/* The wrapper to the underlying C function */
static PyObject *py_convert(PyObject *self, PyObject *args, PyObject *keywds) {

	// The arrays of data we work on. 
	union dataarrays data, dataout;

	// The buffers are arrays of bytes.
	Py_buffer datapy, dataoutpy;

	// The length of the data array.
	Py_ssize_t databufflength, dataoutbufflength;

	// The arrays as objects, so we can examine their types.
	PyObject *dataobj, *dataoutobj;

	// Codes indicating the types of arrays.
	char itemcode, arraycode;

	// How long the array is.
	Py_ssize_t arraylength, arrayoutlength;
	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;


	// The error code returned by the function.
	signed int resultcode;

	// -------------------------------------------------------------------------



	/* Import the raw objects. */
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "OO|l:convert", kwlist, 
			&dataobj, &dataoutobj, &arraymaxlen)) {
		ErrMsgParameterError();
		return NULL;
	}


	// Test if the first parameter is an array.
	itemcode = lookuparraycode(dataobj);
	if (!itemcode) {
		ErrMsgArrayExpected();
		return NULL;
	}


	// Test if the second parameter is an array.
	arraycode = lookuparraycode(dataoutobj);
	if (!arraycode) {
		ErrMsgArrayExpected();
		return NULL;
	}


	// Now we will fetch the actual data.
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "y*y*|l:convert", kwlist, 
			&datapy, &dataoutpy, &arraymaxlen)) {
		return NULL;
	}


	// Assign the buffer to a union which lets us get at them as typed data.
	data.buf = datapy.buf;
	dataout.buf = dataoutpy.buf;


	// The length of the data array.
	databufflength = datapy.len;
	dataoutbufflength = dataoutpy.len;
	arraylength = calcarraylength(itemcode, databufflength);
	if (arraylength < 1) {
		PyBuffer_Release(&datapy);
		PyBuffer_Release(&dataoutpy);
		ErrMsgArrayLengthErr();
		return NULL;
	}

	// Get the length of the output array. We need to compare the number of
	// elements rather than just the number of bytes, because the two
	// array types may not be the same. 
	arrayoutlength = calcarraylength(arraycode, dataoutbufflength);

	// Check to make sure the input and output arrays are of equal length.
	if (arraylength != arrayoutlength) {
		PyBuffer_Release(&datapy);
		PyBuffer_Release(&dataoutpy);
		ErrMsgArrayLengthMismatch();
		return NULL;
	}


	// Adjust the length of array being operated on, if necessary.
	arraylength = adjustarraymaxlen(arraylength, arraymaxlen);



	/* Call the C function */
	switch(itemcode) {
		// signed char
		case 'b' : {
			resultcode = convert_signed_char(arraycode, arraylength, data.b, dataout);
			break;
		}
		// unsigned char
		case 'B' : {
			resultcode = convert_unsigned_char(arraycode, arraylength, data.B, dataout);
			break;
		}
		// signed short
		case 'h' : {
			resultcode = convert_signed_short(arraycode, arraylength, data.h, dataout);
			break;
		}
		// unsigned short
		case 'H' : {
			resultcode = convert_unsigned_short(arraycode, arraylength, data.H, dataout);
			break;
		}
		// signed int
		case 'i' : {
			resultcode = convert_signed_int(arraycode, arraylength, data.i, dataout);
			break;
		}
		// unsigned int
		case 'I' : {
			resultcode = convert_unsigned_int(arraycode, arraylength, data.I, dataout);
			break;
		}
		// signed long
		case 'l' : {
			resultcode = convert_signed_long(arraycode, arraylength, data.l, dataout);
			break;
		}
		// unsigned long
		case 'L' : {
			resultcode = convert_unsigned_long(arraycode, arraylength, data.L, dataout);
			break;
		}
		// signed long long
		case 'q' : {
			resultcode = convert_signed_long_long(arraycode, arraylength, data.q, dataout);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultcode = convert_unsigned_long_long(arraycode, arraylength, data.Q, dataout);
			break;
		}
		// float
		case 'f' : {
			resultcode = convert_float(arraycode, arraylength, data.f, dataout);
			break;
		}
		// double
		case 'd' : {
			resultcode = convert_double(arraycode, arraylength, data.d, dataout);
			break;
		}
		// We don't know this code.
		default: {
			// Release the buffers. 
			PyBuffer_Release(&datapy);
			PyBuffer_Release(&dataoutpy);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}


	// Release the buffers. 
	PyBuffer_Release(&datapy);
	PyBuffer_Release(&dataoutpy);


	// Signal the errors.
	switch (resultcode) {
		case ARR_ERR_INVALIDOP : {
			ErrMsgConversionNotValidforthisType();
			return NULL;
		}
		case ARR_ERR_OVFL : {
			ErrMsgArithOverflowCalc();
			return NULL;
		}
		case ARR_ERR_VALUE_ERR : {
			ErrMsgNaNError();
			return NULL;
		}
		case ARR_ERR_PLATFORM : {
			ErrMsgOperatorNotValidforthisPlatform();
			return NULL;
		}
	}


	// Return NONE.
	Py_RETURN_NONE;


}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(convert__doc__,
"Convert arrays between data types. The data will be converted into the \n\
form required by the output array. If any values in the input array are \n\
outside the range of the output array type, an exception will be \n\
raised. When floating point values are converted to integers, the value \n\
will be truncated. \n\
\n\
convert(inparray, outparray)\n\
convert(inparray, outparray, maxlen=y)\n\
\n\
* inparray - The input data array to be examined.\n\
* outparray - The output array.\n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored.");


/* A list of all the methods defined by this module. 
 "convert" is the name seen inside of Python. 
 "py_convert" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef convert_methods[] = {
	{"convert",  (PyCFunction) py_convert, METH_VARARGS | METH_KEYWORDS, convert__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef convertmodule = {
    PyModuleDef_HEAD_INIT,
    "convert",
    NULL,
    -1,
    convert_methods
};

PyMODINIT_FUNC PyInit_convert(void)
{
    return PyModule_Create(&convertmodule);
};

/*--------------------------------------------------------------------------- */
