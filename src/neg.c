//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   neg.c
// Purpose:  Calculate the neg of values in an array.
// Language: C
// Date:     15-Nov-2017.
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

#include <limits.h>
#include <math.h>

#include "arrayerrs.h"
#include "arrayparams_base.h"
#include "arrayparams_one.h"

/*--------------------------------------------------------------------------- */



/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int neg_signed_char(Py_ssize_t arraylen, signed char *data, signed char *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				data[x] = -data[x];
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if (data[x] == SCHAR_MIN) {return ARR_ERR_OVFL;}
				dataout[x] = -data[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if (data[x] == SCHAR_MIN) {return ARR_ERR_OVFL;}
				data[x] = -data[x];
			}
		}
	}

	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int neg_signed_short(Py_ssize_t arraylen, signed short *data, signed short *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				data[x] = -data[x];
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if (data[x] == SHRT_MIN) {return ARR_ERR_OVFL;}
				dataout[x] = -data[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if (data[x] == SHRT_MIN) {return ARR_ERR_OVFL;}
				data[x] = -data[x];
			}
		}
	}

	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int neg_signed_int(Py_ssize_t arraylen, signed int *data, signed int *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				data[x] = -data[x];
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if (data[x] == INT_MIN) {return ARR_ERR_OVFL;}
				dataout[x] = -data[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if (data[x] == INT_MIN) {return ARR_ERR_OVFL;}
				data[x] = -data[x];
			}
		}
	}

	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int neg_signed_long(Py_ssize_t arraylen, signed long *data, signed long *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				data[x] = -data[x];
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if (data[x] == LONG_MIN) {return ARR_ERR_OVFL;}
				dataout[x] = -data[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if (data[x] == LONG_MIN) {return ARR_ERR_OVFL;}
				data[x] = -data[x];
			}
		}
	}

	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int neg_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				data[x] = -data[x];
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if (data[x] == LLONG_MIN) {return ARR_ERR_OVFL;}
				dataout[x] = -data[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if (data[x] == LLONG_MIN) {return ARR_ERR_OVFL;}
				data[x] = -data[x];
			}
		}
	}

	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int neg_float(Py_ssize_t arraylen, float *data, float *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				data[x] = -data[x];
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				data[x] = -data[x];
				if (!isfinite(data[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
	}

	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int neg_double(Py_ssize_t arraylen, double *data, double *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				data[x] = -data[x];
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				data[x] = -data[x];
				if (!isfinite(data[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
	}

	return ARR_NO_ERR;

}



/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_neg(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;

	// This is used to hold the parsed parameters.
	struct args_params_1 arraydata = ARGSINIT_ONE;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_one(self, args, keywds, 1, "neg");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}

	// Call the C function.
	switch(arraydata.arraytype) {

		// signed_char
		case 'b' : {
			resultcode = neg_signed_char(arraydata.arraylength, arraydata.array1.b, arraydata.array2.b, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// signed_short
		case 'h' : {
			resultcode = neg_signed_short(arraydata.arraylength, arraydata.array1.h, arraydata.array2.h, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// signed_int
		case 'i' : {
			resultcode = neg_signed_int(arraydata.arraylength, arraydata.array1.i, arraydata.array2.i, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// signed_long
		case 'l' : {
			resultcode = neg_signed_long(arraydata.arraylength, arraydata.array1.l, arraydata.array2.l, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// signed_long_long
		case 'q' : {
			resultcode = neg_signed_long_long(arraydata.arraylength, arraydata.array1.q, arraydata.array2.q, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// float
		case 'f' : {
			resultcode = neg_float(arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// double
		case 'd' : {
			resultcode = neg_double(arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// We don't know this code.
		default: {
			releasebuffers_one(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_one(arraydata);


	// Signal the errors.
	if (resultcode == ARR_ERR_ARITHMETIC) {
		ErrMsgArithCalc();
		return NULL;
	}

	if (resultcode == ARR_ERR_OVFL) {
		ErrMsgArithOverflowCalc();
		return NULL;
	}


	// Everything was successful.
	Py_RETURN_NONE;

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(neg__doc__,
"neg \n\
_____________________________ \n\
\n\
Calculate neg over the values in an array.  \n\
\n\
======================  ============================================== \n\
Equivalent to:          -x \n\
Array types supported:  b, h, i, l, q, f, d \n\
Exceptions raised:      OverflowError, ArithmeticError \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
    neg(array1) \n\
    neg(array1, outparray) \n\
    neg(array1, maxlen=y) \n\
    neg(array1, matherrors=False)) \n\
\n\
* array1 - The first input data array to be examined. If no output \n\
  array is provided the results will overwrite the input data. \n\
* outparray - The output array. This parameter is optional. \n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored. \n\
* matherrors - If true, arithmetic error checking is disabled. The \n\
  default is false. \n\
");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "neg" is the name seen inside of Python. 
 "py_neg" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef neg_methods[] = {
	{"neg",  (PyCFunction)py_neg, METH_VARARGS | METH_KEYWORDS, neg__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef negmodule = {
    PyModuleDef_HEAD_INIT,
    "neg",
    NULL,
    -1,
    neg_methods
};

PyMODINIT_FUNC PyInit_neg(void)
{
    return PyModule_Create(&negmodule);
};

/*--------------------------------------------------------------------------- */
