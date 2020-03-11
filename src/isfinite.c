//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   isfinite.c
// Purpose:  Calculate the isfinite of values in an array.
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
#include "arrayparams_boolout.h"


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   Returns True if the search condition is met.
*/
signed int isfinite_float(Py_ssize_t arraylen, float *data) {

	// array index counter.
	Py_ssize_t x;

	for(x = 0; x < arraylen; x++) {
		if (!isfinite(data[x])) { return 0; }
	}

	return 1;

}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   Returns True if the search condition is met.
*/
signed int isfinite_double(Py_ssize_t arraylen, double *data) {

	// array index counter.
	Py_ssize_t x;

	for(x = 0; x < arraylen; x++) {
		if (!isfinite(data[x])) { return 0; }
	}

	return 1;

}

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_isfinite(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;

	// This is used to hold the parsed parameters.
	struct args_params_boolout arraydata = ARGSINIT_BOOLOUT;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_boolout(self, args, keywds, "isfinite");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}

	// Call the C function.
	switch(arraydata.arraytype) {
		// float
		case 'f' : {
			resultcode = isfinite_float(arraydata.arraylength, arraydata.array1.f);
			break;
		}
		// double
		case 'd' : {
			resultcode = isfinite_double(arraydata.arraylength, arraydata.array1.d);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_boolout(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_boolout(arraydata);


	// Return whether compare was OK.
	if (resultcode) {
		Py_RETURN_TRUE;
	} else {
		Py_RETURN_FALSE;
	}

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(isfinite__doc__,
"isfinite \n\
_____________________________ \n\
\n\
Calculate isfinite over the values in an array. \n\
\n\
======================  ============================================== \n\
Equivalent to:          all([isfinite(x) for x in array1]) \n\
======================  ============================================== \n\
\n\
======================  ============================================== \
Array types supported:  f, d \n\
Exceptions raised:       \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
    result = isfinite(array1) \n\
    result = isfinite(array1, maxlen=y) \n\
\n\
* array1 - The first input data array to be examined. If no output \n\
  array is provided the results will overwrite the input data. \n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored. \n\
* result - A boolean value corresponding to the result of all the \n\
  comparison operations. If all of the comparison operations result in \n\
  true, the return value will be true. If any of them result in false, \n\
  the return value will be false.\n\
");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "isfinite" is the name seen inside of Python. 
 "py_isfinite" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef isfinite_methods[] = {
	{"isfinite",  (PyCFunction)py_isfinite, METH_VARARGS | METH_KEYWORDS, isfinite__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef isfinitemodule = {
    PyModuleDef_HEAD_INIT,
    "isfinite",
    NULL,
    -1,
    isfinite_methods
};

PyMODINIT_FUNC PyInit_isfinite(void)
{
    return PyModule_Create(&isfinitemodule);
};

/*--------------------------------------------------------------------------- */

