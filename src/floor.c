//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   floor.c
// Purpose:  Calculate the floor of values in an array.
// Language: C
// Date:     15-Nov-2017.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2020    Michael Griffin    <m12.griffin@gmail.com>
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

#include "arrayparams_onesimd.h"

#include "simddefs.h"

#ifdef AF_HASSIMD_X86
#include "floor_simd_x86.h"
#endif




/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int floor_float(Py_ssize_t arraylen, int nosimd, float *data, float *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


#if defined(AF_HASSIMD_X86)
	signed int errorstate;

	// SIMD version. 
	if (!nosimd && enoughforsimd(arraylen, FLOATSIMDSIZE)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			if (hasoutputarray) {		
				floor_float_2_simd(arraylen, data, dataout);
			} else {
				floor_float_1_simd(arraylen, data);
			}
		} else {
		// Math error checking enabled.
			if (hasoutputarray) {		
				errorstate = floor_float_2_simd_ovfl(arraylen, data, dataout);
				if (errorstate) {return ARR_ERR_ARITHMETIC;}
			} else {
				errorstate = floor_float_1_simd_ovfl(arraylen, data);
				if (errorstate) {return ARR_ERR_ARITHMETIC;}
			}
		}

	} else {
#endif

		// Math error checking disabled.
		if (ignoreerrors) {
			if (hasoutputarray) {		
				for (x = 0; x < arraylen; x++) {
					dataout[x] = floorf(data[x]);
				}
			} else {
				for (x = 0; x < arraylen; x++) {
					data[x] = floorf(data[x]);
				}
			}
		} else {
		// Math error checking enabled.
			if (hasoutputarray) {		
				for (x = 0; x < arraylen; x++) {
					dataout[x] = floorf(data[x]);
					if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
				}
			} else {
				for (x = 0; x < arraylen; x++) {
					data[x] = floorf(data[x]);
					if (!isfinite(data[x])) {return ARR_ERR_ARITHMETIC;}
				}
			}
		}

#if defined(AF_HASSIMD_X86)
	}
#endif

	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int floor_double(Py_ssize_t arraylen, int nosimd, double *data, double *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


#if defined(AF_HASSIMD_X86)
	signed int errorstate;

	// SIMD version. 
	if (!nosimd && enoughforsimd(arraylen, DOUBLESIMDSIZE)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			if (hasoutputarray) {		
				floor_double_2_simd(arraylen, data, dataout);
			} else {
				floor_double_1_simd(arraylen, data);
			}
		} else {
		// Math error checking enabled.
			if (hasoutputarray) {		
				errorstate = floor_double_2_simd_ovfl(arraylen, data, dataout);
				if (errorstate) {return ARR_ERR_ARITHMETIC;}
			} else {
				errorstate = floor_double_1_simd_ovfl(arraylen, data);
				if (errorstate) {return ARR_ERR_ARITHMETIC;}
			}
		}

	} else {
#endif

		// Math error checking disabled.
		if (ignoreerrors) {
			if (hasoutputarray) {		
				for (x = 0; x < arraylen; x++) {
					dataout[x] = floor(data[x]);
				}
			} else {
				for (x = 0; x < arraylen; x++) {
					data[x] = floor(data[x]);
				}
			}
		} else {
		// Math error checking enabled.
			if (hasoutputarray) {		
				for (x = 0; x < arraylen; x++) {
					dataout[x] = floor(data[x]);
					if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
				}
			} else {
				for (x = 0; x < arraylen; x++) {
					data[x] = floor(data[x]);
					if (!isfinite(data[x])) {return ARR_ERR_ARITHMETIC;}
				}
			}
		}

#if defined(AF_HASSIMD_X86)
	}
#endif

	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_floor(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;

	// This is used to hold the parsed parameters.
	struct args_params_1 arraydata = ARGSINIT_ONE;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_one(self, args, keywds, 1, "floor");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}

	// Call the C function.
	switch(arraydata.arraytype) {
		// float
		case 'f' : {
			resultcode = floor_float(arraydata.arraylength, arraydata.nosimd, arraydata.array1.f, arraydata.array2.f, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}
		// double
		case 'd' : {
			resultcode = floor_double(arraydata.arraylength, arraydata.nosimd, arraydata.array1.d, arraydata.array2.d, arraydata.ignoreerrors, arraydata.hasoutputarray);
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


	// Everything was successful.
	Py_RETURN_NONE;

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(floor__doc__,
"floor \n\
_____________________________ \n\
\n\
Calculate floor over the values in an array.  \n\
\n\
======================  ============================================== \n\
Equivalent to:          [math.floor(x) for x in array1] \n\
Array types supported:  f, d \n\
Exceptions raised:      ArithmeticError \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
    floor(array1) \n\
    floor(array1, outparray) \n\
    floor(array1, maxlen=y) \n\
    floor(array1, matherrors=False)) \n\
    floor(array, nosimd=False) \n\
\n\
* array1 - The first input data array to be examined. If no output \n\
  array is provided the results will overwrite the input data. \n\
* outparray - The output array. This parameter is optional. \n\
* maxlen - Limit the length of the array used. This must be a valid  \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored. \n\
* matherrors - If true, arithmetic error checking is disabled. The \n\
  default is false. \n\
* nosimd - If True, SIMD acceleration is disabled. This parameter is \n\
  optional. The default is FALSE.  \n\
\
");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "floor" is the name seen inside of Python. 
 "py_floor" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef floor_methods[] = {
	{"floor",  (PyCFunction)py_floor, METH_VARARGS | METH_KEYWORDS, floor__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef floormodule = {
    PyModuleDef_HEAD_INIT,
    "floor",
    NULL,
    -1,
    floor_methods
};

PyMODINIT_FUNC PyInit_floor(void)
{
    return PyModule_Create(&floormodule);
};

/*--------------------------------------------------------------------------- */

