//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   ldexp.c
// Purpose:  Calculate the ldexp of values in an array.
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

#include "arrayparams_special.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   exp = The exponent to be applied to each array element.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hassecondarray = If true, the output goes into the second array.
*/
signed int ldexp_float(Py_ssize_t arraylen, float *data, signed long long exp, float *dataout, unsigned int ignoreerrors, bool hassecondarray) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		if (hassecondarray) {		
			for(x = 0; x < arraylen; x++) {
				dataout[x] = ldexpf(data[x], exp);
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				data[x] = ldexpf(data[x], exp);
			}
		}
	} else {
	// Math error checking enabled.
		if (hassecondarray) {		
			for(x = 0; x < arraylen; x++) {
				dataout[x] = ldexpf(data[x], exp);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				data[x] = ldexpf(data[x], exp);
				if (!isfinite(data[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
	}

	return ARR_NO_ERR;

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   exp = The exponent to be applied to each array element.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hassecondarray = If true, the output goes into the second array.
*/
signed int ldexp_double(Py_ssize_t arraylen, double *data, signed long long exp, double *dataout, unsigned int ignoreerrors, bool hassecondarray) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		if (hassecondarray) {		
			for(x = 0; x < arraylen; x++) {
				dataout[x] = ldexp(data[x], exp);
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				data[x] = ldexp(data[x], exp);
			}
		}
	} else {
	// Math error checking enabled.
		if (hassecondarray) {		
			for(x = 0; x < arraylen; x++) {
				dataout[x] = ldexp(data[x], exp);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				data[x] = ldexp(data[x], exp);
				if (!isfinite(data[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
	}

	return ARR_NO_ERR;

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_ldexp(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;


	// This is used to return the parsed parameters.
	struct args_params_ldexp arraydata = ARGSINIT_SPECIAL;


	// -----------------------------------------------------

	// Get the parameters passed from Python.
	arraydata = getparams_ldexp(self, args, keywds);

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}


	// Call the C function.
	switch(arraydata.arraytype) {
		// float
		case 'f' : {
			resultcode = ldexp_float(arraydata.arraylength, arraydata.array1.f, arraydata.exp, arraydata.array2.f, arraydata.ignoreerrors, arraydata.hassecondarray);
			break;
		}
		// double
		case 'd' : {
			resultcode = ldexp_double(arraydata.arraylength, arraydata.array1.d, arraydata.exp, arraydata.array2.d, arraydata.ignoreerrors, arraydata.hassecondarray);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_twobuff(arraydata.pybuffer1, arraydata.pybuffer2, arraydata.hassecondarray);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_twobuff(arraydata.pybuffer1, arraydata.pybuffer2, arraydata.hassecondarray);


	// Signal the errors.
	if (resultcode == ARR_ERR_ARITHMETIC) {
		ErrMsgArithCalc();
		return NULL;
	}


	// Everything was successful.
	Py_RETURN_NONE;

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(ldexp__doc__,
"ldexp \n\
_____________________________ \n\
\n\
Calculate ldexp over the values in an array.  \n\
\n\
======================  ============================================== \n\
Equivalent to:          math.ldexp(x, y) \n\
Array types supported:  f, d \n\
Exceptions raised:      ArithmeticError \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
    ldexp(array1, exp) \n\
    ldexp(array1, exp, outparray) \n\
    ldexp(array1, exp, maxlen=y) \n\
    ldexp(array1, exp, matherrors=False)) \n\
\n\
* array1 - The first input data array to be examined. If no output  \n\
  array is provided the results will overwrite the input data.  \n\
* exp - The exponent to apply to the input array. This must be an \n\
  integer. \n\
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
 "ldexp" is the name seen inside of Python. 
 "py_ldexp" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef ldexp_methods[] = {
	{"ldexp",  (PyCFunction)py_ldexp, METH_VARARGS | METH_KEYWORDS, ldexp__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef ldexpmodule = {
    PyModuleDef_HEAD_INIT,
    "ldexp",
    NULL,
    -1,
    ldexp_methods
};

PyMODINIT_FUNC PyInit_ldexp(void)
{
    return PyModule_Create(&ldexpmodule);
};

/*--------------------------------------------------------------------------- */

