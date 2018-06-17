//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   asum.c
// Purpose:  Sum all the values in an array.
// Language: C
// Date:     15-May-2014
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

#include "asum_common.h"


/*--------------------------------------------------------------------------- */

// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist[] = {"data", "matherrors", "maxlen", "nosimd", NULL};

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */


/* The wrapper to the underlying C function */
static PyObject *py_asum(PyObject *self, PyObject *args, PyObject *keywds)
{


	// The array of data we work on. 
	union dataarrays data;

	// The input buffers are arrays of bytes.
	Py_buffer datapy;

	// The length of the data array.
	Py_ssize_t databufflength;

	// The raw object so we can examine what it is, plus the final result. 
	PyObject *dataobj, *sumreturn;


	// Codes indicating the type of array and the operation desired.
	char itemcode;

	// Indicates an error.
	signed int errflag = 0;
	// If true, disable integer overflow checking.
	signed int ignoreerrors = 0;

	// How long the array is.
	Py_ssize_t arraylength;
	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	// The parameter version is available in all possible types.
	struct paramsvals resultfound;

	// If true, disable using SIMD.
	unsigned int nosimd = 0;

	// -------------------------------------------------------------------------


	/* Import the raw objects. */
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "O|ini:asum", kwlist, &dataobj, &ignoreerrors, &arraymaxlen, &nosimd)) {
		ErrMsgParameterError();
		return NULL;
	}


	// Test if the parameter is an array.
	itemcode = lookuparraycode(dataobj);
	if (!itemcode) {
		ErrMsgArrayExpected();
		return NULL;
	}


	// Now we will fetch the actual data.
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "y*|ini:asum", kwlist, 
			&datapy, &ignoreerrors, &arraymaxlen, &nosimd)) {
		return NULL;
	}


	// Assign the buffer to a union which lets us get at them as typed data.
	data.buf = datapy.buf;


	// The length of the data array.
	databufflength = datapy.len;
	arraylength = calcarraylength(itemcode, databufflength);
	if (arraylength < 1) {
		// Release the buffers.
		PyBuffer_Release(&datapy);
		ErrMsgArrayLengthErr();
		return NULL;
	}

	// Adjust the length of array being operated on, if necessary.
	arraylength = adjustarraymaxlen(arraylength, arraymaxlen);



	/* Call the C function */
	switch(itemcode) {
		// signed char
		case 'b' : {
			resultfound.l = asum_signed_char(arraylength, data.b, &errflag, ignoreerrors);
			sumreturn = PyLong_FromLong(resultfound.l);
			break;
		}
		// unsigned char
		case 'B' : {
			resultfound.L = asum_unsigned_char(arraylength, data.B, &errflag, ignoreerrors);
			sumreturn = PyLong_FromUnsignedLong(resultfound.L);
			break;
		}
		// signed short
		case 'h' : {
			resultfound.l = asum_signed_short(arraylength, data.h, &errflag, ignoreerrors);
			sumreturn = PyLong_FromLong(resultfound.l);
			break;
		}
		// unsigned short
		case 'H' : {
			resultfound.L = asum_unsigned_short(arraylength, data.H, &errflag, ignoreerrors);
			sumreturn = PyLong_FromUnsignedLong(resultfound.L);
			break;
		}
		// signed int
		case 'i' : {
			resultfound.l = asum_signed_int(arraylength, data.i, &errflag, ignoreerrors);
			sumreturn = PyLong_FromLong(resultfound.l);
			break;
		}
		// unsigned int
		case 'I' : {
			resultfound.L = asum_unsigned_int(arraylength, data.I, &errflag, ignoreerrors);
			sumreturn = PyLong_FromUnsignedLong(resultfound.L);
			break;
		}
		// signed long
		case 'l' : {
			resultfound.l = asum_signed_long(arraylength, data.l, &errflag, ignoreerrors);
			sumreturn = PyLong_FromLong(resultfound.l);
			break;
		}
		// unsigned long
		case 'L' : {
			resultfound.L = asum_unsigned_long(arraylength, data.L, &errflag, ignoreerrors);
			sumreturn = PyLong_FromUnsignedLong(resultfound.L);
			break;
		}
		// signed long long
		case 'q' : {
			resultfound.q = asum_signed_long_long(arraylength, data.q, &errflag, ignoreerrors);
			sumreturn = PyLong_FromLongLong(resultfound.q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultfound.Q = asum_unsigned_long_long(arraylength, data.Q, &errflag, ignoreerrors);
			sumreturn = PyLong_FromUnsignedLongLong(resultfound.Q);
			break;
		}
		// float
		case 'f' : {
			resultfound.f = asum_float(arraylength, data.f, &errflag, ignoreerrors, nosimd);
			sumreturn = PyFloat_FromDouble((double) resultfound.f);
			break;
		}
		// double
		case 'd' : {
			resultfound.d = asum_double(arraylength, data.d, &errflag, ignoreerrors, nosimd);
			sumreturn = PyFloat_FromDouble(resultfound.d);
			break;
		}
		// We don't know this code.
		default: {
			// Release the buffers.
			PyBuffer_Release(&datapy);
			ErrMsgUnknownArrayType();
			return NULL;
		}
	}


	// Release the buffers.
	PyBuffer_Release(&datapy);

	if (errflag == ARR_ERR_OVFL) {
		ErrMsgArithOverflowCalc();
		return NULL;
	}

	return sumreturn;

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(asum__doc__,
"Calculate the arithmetic sum of an array. \n\
\n\
For integer arrays, the intermediate sum is accumulated in the largest \n\
corresponding integer size. Signed integers are accumulated in the  \n\
equivalent to an 'l' array type, and unsigned integers are accumulated \n\
in the equivalent to an 'L' array type. This means that integer arrays \n\
using smaller integer word sizes cannot overflow unless extremenly \n\
large arrays are used (and may be impossible due to limits on array \n\
indices in the array module). \n\
\n\
x = asum(inparray)\n\
x = asum(inparray, matherrors=True, maxlen=y)\n\
x = asum(inparray, nosimd=True)\n\
\n\
* inparray - The array to be summed.\n\
* matherrors - If this keyword parameter is True, integer overflow \n\
  checking will be disabled. This is an optional parameter.\n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored. \n\
* nosimd - If true, disable SIMD. SIMD will only be enabled if overflow \n\
  checking is also disabled.");



/* A list of all the methods defined by this module. 
 "asum" is the name seen inside of Python. 
 "py_asum" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef asum_methods[] = {
	{"asum",  (PyCFunction)py_asum, METH_VARARGS | METH_KEYWORDS, asum__doc__}, 
	{NULL, NULL, 0, NULL}
};

static struct PyModuleDef asummodule = {
    PyModuleDef_HEAD_INIT,
    "asum",
    NULL,
    -1,
    asum_methods
};

PyMODINIT_FUNC PyInit_asum(void)
{
    return PyModule_Create(&asummodule);
};

/*--------------------------------------------------------------------------- */
