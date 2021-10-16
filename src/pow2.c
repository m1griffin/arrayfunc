//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   pow2.c
// Purpose:  Calculate the pow2 of values in an array.
// Language: C
// Date:     09-Oct-2021.
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

#include <limits.h>
#include <math.h>

#include "arrayerrs.h"

#include "arrayparams_base.h"

#include "arrayparams_one.h"


/*--------------------------------------------------------------------------- */

#define SCHAR_POW2MAX 11
#define SCHAR_POW2MIN -11 
#define UCHAR_POW2MAX 15

#define SSHORT_POW2MAX 181
#define SSHORT_POW2MIN -181 
#define USHORT_POW2MAX 255

#define SINT_POW2MAX 46340
#define SINT_POW2MIN -46340
#define UINT_POW2MAX 65535

// Account for 64 bit versus 32 bit word sizes.
#if LONG_MAX == LLONG_MAX

#define SLINT_POW2MAX 3037000499L
#define SLINT_POW2MIN -3037000499L
#define ULINT_POW2MAX 4294967295UL

#else

#define SLINT_POW2MAX 46340
#define SLINT_POW2MIN -46340
#define ULINT_POW2MAX 65535

#endif

#define SLLINT_POW2MAX 3037000499LL
#define SLLINT_POW2MIN -3037000499LL
#define ULLINT_POW2MAX 4294967295ULL


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data array.
   data1 = The first data array.
   data2 = The second data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into a separate array.
*/
signed int pow2_signed_char(Py_ssize_t arraylen, signed char *data1, signed char *data2, unsigned int ignoreerrors, bool hasoutputarray) {


	// array index counter.
	Py_ssize_t x;

	if (hasoutputarray) {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data2[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ((data1[x] > SCHAR_POW2MAX) || (data1[x] < SCHAR_POW2MIN)) { return ARR_ERR_OVFL; }
				data2[x] = data1[x] * data1[x];
			}
		}

	} else {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ((data1[x] > SCHAR_POW2MAX) || (data1[x] < SCHAR_POW2MIN)) { return ARR_ERR_OVFL; }
				data1[x] = data1[x] * data1[x];
			}
		}
	}

	return ARR_NO_ERR;
}


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data array.
   data1 = The first data array.
   data2 = The second data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into a separate array.
*/
signed int pow2_unsigned_char(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2, unsigned int ignoreerrors, bool hasoutputarray) {


	// array index counter.
	Py_ssize_t x;

	if (hasoutputarray) {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data2[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if (data1[x] > UCHAR_POW2MAX) { return ARR_ERR_OVFL; }
				data2[x] = data1[x] * data1[x];
			}
		}

	} else {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if (data1[x] > UCHAR_POW2MAX) { return ARR_ERR_OVFL; }
				data1[x] = data1[x] * data1[x];
			}
		}

	}

	return ARR_NO_ERR;
}



/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data array.
   data1 = The first data array.
   data2 = The second data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into a separate array.
*/
signed int pow2_signed_short(Py_ssize_t arraylen, signed short *data1, signed short *data2, unsigned int ignoreerrors, bool hasoutputarray) {


	// array index counter.
	Py_ssize_t x;

	if (hasoutputarray) {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data2[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ((data1[x] > SSHORT_POW2MAX) || (data1[x] < SSHORT_POW2MIN)) { return ARR_ERR_OVFL; }
				data2[x] = data1[x] * data1[x];
			}
		}

	} else {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ((data1[x] > SSHORT_POW2MAX) || (data1[x] < SSHORT_POW2MIN)) { return ARR_ERR_OVFL; }
				data1[x] = data1[x] * data1[x];
			}
		}
	}

	return ARR_NO_ERR;
}


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data array.
   data1 = The first data array.
   data2 = The second data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into a separate array.
*/
signed int pow2_unsigned_short(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2, unsigned int ignoreerrors, bool hasoutputarray) {


	// array index counter.
	Py_ssize_t x;

	if (hasoutputarray) {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data2[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if (data1[x] > USHORT_POW2MAX) { return ARR_ERR_OVFL; }
				data2[x] = data1[x] * data1[x];
			}
		}

	} else {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if (data1[x] > USHORT_POW2MAX) { return ARR_ERR_OVFL; }
				data1[x] = data1[x] * data1[x];
			}
		}

	}

	return ARR_NO_ERR;
}



/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data array.
   data1 = The first data array.
   data2 = The second data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into a separate array.
*/
signed int pow2_signed_int(Py_ssize_t arraylen, signed int *data1, signed int *data2, unsigned int ignoreerrors, bool hasoutputarray) {


	// array index counter.
	Py_ssize_t x;

	if (hasoutputarray) {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data2[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ((data1[x] > SINT_POW2MAX) || (data1[x] < SINT_POW2MIN)) { return ARR_ERR_OVFL; }
				data2[x] = data1[x] * data1[x];
			}
		}

	} else {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ((data1[x] > SINT_POW2MAX) || (data1[x] < SINT_POW2MIN)) { return ARR_ERR_OVFL; }
				data1[x] = data1[x] * data1[x];
			}
		}
	}

	return ARR_NO_ERR;
}


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data array.
   data1 = The first data array.
   data2 = The second data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into a separate array.
*/
signed int pow2_unsigned_int(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2, unsigned int ignoreerrors, bool hasoutputarray) {


	// array index counter.
	Py_ssize_t x;

	if (hasoutputarray) {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data2[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if (data1[x] > UINT_POW2MAX) { return ARR_ERR_OVFL; }
				data2[x] = data1[x] * data1[x];
			}
		}

	} else {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if (data1[x] > UINT_POW2MAX) { return ARR_ERR_OVFL; }
				data1[x] = data1[x] * data1[x];
			}
		}

	}

	return ARR_NO_ERR;
}



/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data array.
   data1 = The first data array.
   data2 = The second data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into a separate array.
*/
signed int pow2_signed_long(Py_ssize_t arraylen, signed long *data1, signed long *data2, unsigned int ignoreerrors, bool hasoutputarray) {


	// array index counter.
	Py_ssize_t x;

	if (hasoutputarray) {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data2[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ((data1[x] > SLINT_POW2MAX) || (data1[x] < SLINT_POW2MIN)) { return ARR_ERR_OVFL; }
				data2[x] = data1[x] * data1[x];
			}
		}

	} else {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ((data1[x] > SLINT_POW2MAX) || (data1[x] < SLINT_POW2MIN)) { return ARR_ERR_OVFL; }
				data1[x] = data1[x] * data1[x];
			}
		}
	}

	return ARR_NO_ERR;
}


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data array.
   data1 = The first data array.
   data2 = The second data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into a separate array.
*/
signed int pow2_unsigned_long(Py_ssize_t arraylen, unsigned long *data1, unsigned long *data2, unsigned int ignoreerrors, bool hasoutputarray) {


	// array index counter.
	Py_ssize_t x;

	if (hasoutputarray) {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data2[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if (data1[x] > ULINT_POW2MAX) { return ARR_ERR_OVFL; }
				data2[x] = data1[x] * data1[x];
			}
		}

	} else {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if (data1[x] > ULINT_POW2MAX) { return ARR_ERR_OVFL; }
				data1[x] = data1[x] * data1[x];
			}
		}

	}

	return ARR_NO_ERR;
}



/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data array.
   data1 = The first data array.
   data2 = The second data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into a separate array.
*/
signed int pow2_signed_long_long(Py_ssize_t arraylen, signed long long *data1, signed long long *data2, unsigned int ignoreerrors, bool hasoutputarray) {


	// array index counter.
	Py_ssize_t x;

	if (hasoutputarray) {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data2[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ((data1[x] > SLLINT_POW2MAX) || (data1[x] < SLLINT_POW2MIN)) { return ARR_ERR_OVFL; }
				data2[x] = data1[x] * data1[x];
			}
		}

	} else {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ((data1[x] > SLLINT_POW2MAX) || (data1[x] < SLLINT_POW2MIN)) { return ARR_ERR_OVFL; }
				data1[x] = data1[x] * data1[x];
			}
		}
	}

	return ARR_NO_ERR;
}


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data array.
   data1 = The first data array.
   data2 = The second data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into a separate array.
*/
signed int pow2_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data1, unsigned long long *data2, unsigned int ignoreerrors, bool hasoutputarray) {


	// array index counter.
	Py_ssize_t x;

	if (hasoutputarray) {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data2[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if (data1[x] > ULLINT_POW2MAX) { return ARR_ERR_OVFL; }
				data2[x] = data1[x] * data1[x];
			}
		}

	} else {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if (data1[x] > ULLINT_POW2MAX) { return ARR_ERR_OVFL; }
				data1[x] = data1[x] * data1[x];
			}
		}

	}

	return ARR_NO_ERR;
}



/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into a separate array.
*/
// param_arr_none
signed int pow2_float(Py_ssize_t arraylen, float *data1, float *data2, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;

	if (hasoutputarray) {

		// Math error checking disabled.
		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data2[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data2[x] = data1[x] * data1[x];
				if (!isfinite(data2[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}

	} else {

		// Math error checking disabled.
		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] * data1[x];
				if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}

	}

	return ARR_NO_ERR;

}



/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into a separate array.
*/
// param_arr_none
signed int pow2_double(Py_ssize_t arraylen, double *data1, double *data2, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;

	if (hasoutputarray) {

		// Math error checking disabled.
		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data2[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data2[x] = data1[x] * data1[x];
				if (!isfinite(data2[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}

	} else {

		// Math error checking disabled.
		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] * data1[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] * data1[x];
				if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}

	}

	return ARR_NO_ERR;

}



/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_pow2(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;

	// This is used to hold the parsed parameters.
	struct args_params_1 arraydata = ARGSINIT_ONE;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_one(self, args, keywds, 1, "pow2");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}

	// Call the C function.
	switch(arraydata.arraytype) {

		// signed_char
		case 'b' : {
			resultcode = pow2_signed_char(arraydata.arraylength, arraydata.array1.b, arraydata.array2.b, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// unsigned_char
		case 'B' : {
			resultcode = pow2_unsigned_char(arraydata.arraylength, arraydata.array1.B, arraydata.array2.B, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// signed_short
		case 'h' : {
			resultcode = pow2_signed_short(arraydata.arraylength, arraydata.array1.h, arraydata.array2.h, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// unsigned_short
		case 'H' : {
			resultcode = pow2_unsigned_short(arraydata.arraylength, arraydata.array1.H, arraydata.array2.H, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// signed_int
		case 'i' : {
			resultcode = pow2_signed_int(arraydata.arraylength, arraydata.array1.i, arraydata.array2.i, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// unsigned_int
		case 'I' : {
			resultcode = pow2_unsigned_int(arraydata.arraylength, arraydata.array1.I, arraydata.array2.I, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// signed_long
		case 'l' : {
			resultcode = pow2_signed_long(arraydata.arraylength, arraydata.array1.l, arraydata.array2.l, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// unsigned_long
		case 'L' : {
			resultcode = pow2_unsigned_long(arraydata.arraylength, arraydata.array1.L, arraydata.array2.L, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// signed_long_long
		case 'q' : {
			resultcode = pow2_signed_long_long(arraydata.arraylength, arraydata.array1.q, arraydata.array2.q, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// unsigned_long_long
		case 'Q' : {
			resultcode = pow2_unsigned_long_long(arraydata.arraylength, arraydata.array1.Q, arraydata.array2.Q, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// float
		case 'f' : {
			resultcode = pow2_float(arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// double
		case 'd' : {
			resultcode = pow2_double(arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// Wrong array type code.
		default: {
			releasebuffers_one(arraydata);
			ErrMsgTypeExpectFloat();
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

	if (resultcode == ARR_ERR_VALUE_ERR) {
		ErrMsgParameterNotValidforthisOperation();
		return NULL;
	}


	// Everything was successful.
	Py_RETURN_NONE;

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(pow2__doc__,
"pow2 \n\
_____________________________ \n\
\n\
Calculate pow2 over the values in an array.  \n\
\n\
======================  ============================================== \n\
Equivalent to:          [x * x for x in array1] \n\
======================  ============================================== \n\
\n\
======================  ============================================== \n\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \n\
Exceptions raised:      OverflowError, ArithmeticError, ValueError \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
  pow2(array1) \n\
  pow2(array1, outparray) \n\
  pow2(array1, maxlen=y) \n\
  pow2(array1, matherrors=False) \n\
\n\
* array1 - The first input data array to be examined. If no output  \n\
  array is provided the results will overwrite the input data.  \n\
* outparray - The output array. This parameter is optional.  \n\
* maxlen - Limit the length of the array used. This must be a valid  \n\
  positive integer. If a zero or negative length, or a value which is  \n\
  greater than the actual length of the array is specified, this  \n\
  parameter is ignored.  \n\
* matherrors - If true, arithmetic error checking is disabled. The  \n\
  default is false. \n\
");

/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "pow2" is the name seen inside of Python. 
 "py_pow2" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef pow2_methods[] = {
	{"pow2",  (PyCFunction)py_pow2, METH_VARARGS | METH_KEYWORDS, pow2__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef pow2module = {
    PyModuleDef_HEAD_INIT,
    "pow2",
    NULL,
    -1,
    pow2_methods
};

PyMODINIT_FUNC PyInit_pow2(void)
{
    return PyModule_Create(&pow2module);
};

/*--------------------------------------------------------------------------- */

