//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   abs_.c
// Purpose:  Calculate the abs_ of values in an array.
// Language: C
// Date:     15-Nov-2017.
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
#include "arrayparams_onesimd.h"

#include "simddefs.h"

#ifdef AF_HASSIMD_X86
#include "abs__simd_x86.h"
#endif

#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
#include "arm_neon.h"
#endif

#if defined(AF_HASSIMD_ARMv7_32BIT)
#include "abs__simd_armv7.h"
#endif

#if defined(AF_HASSIMD_ARM_AARCH64)
#include "abs__simd_armv8.h"
#endif

/*--------------------------------------------------------------------------- */


// Function specific macros and other definitions.
#include "abs__defs.h"

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int abs__signed_char(Py_ssize_t arraylen, int nosimd, signed char *data, signed char *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	char ovflresult;

	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, CHARSIMDSIZE) ) {
		// Math error checking disabled.
		if (ignoreerrors) {
			if (hasoutputarray) {
				abs__signed_char_2_simd(arraylen, data, dataout);
			} else {
				abs__signed_char_1_simd(arraylen, data);
			}
			return ARR_NO_ERR;
		} else {
		// Math error checking enabled.
			if (hasoutputarray) {
				ovflresult = abs__signed_char_2_simd_ovfl(arraylen, data, dataout);
			} else {
				ovflresult = abs__signed_char_1_simd_ovfl(arraylen, data);
			}

			if (ovflresult) { 
				return ARR_ERR_OVFL; 
			} else {
				return ARR_NO_ERR;
			}
		}

	} else {
#endif

	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				if ( minval_loop_willoverflow_signed_char(data[x]) ) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ( minval_loop_willoverflow_signed_char(data[x]) ) {return ARR_ERR_OVFL;}
				data[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		}
	}


#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	}
#endif


	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int abs__signed_short(Py_ssize_t arraylen, int nosimd, signed short *data, signed short *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	char ovflresult;

	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, SHORTSIMDSIZE) ) {
		// Math error checking disabled.
		if (ignoreerrors) {
			if (hasoutputarray) {
				abs__signed_short_2_simd(arraylen, data, dataout);
			} else {
				abs__signed_short_1_simd(arraylen, data);
			}
			return ARR_NO_ERR;
		} else {
		// Math error checking enabled.
			if (hasoutputarray) {
				ovflresult = abs__signed_short_2_simd_ovfl(arraylen, data, dataout);
			} else {
				ovflresult = abs__signed_short_1_simd_ovfl(arraylen, data);
			}

			if (ovflresult) { 
				return ARR_ERR_OVFL; 
			} else {
				return ARR_NO_ERR;
			}
		}

	} else {
#endif

	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				if ( minval_loop_willoverflow_signed_short(data[x]) ) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ( minval_loop_willoverflow_signed_short(data[x]) ) {return ARR_ERR_OVFL;}
				data[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		}
	}


#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	}
#endif


	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int abs__signed_int(Py_ssize_t arraylen, int nosimd, signed int *data, signed int *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
	char ovflresult;

	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, INTSIMDSIZE) ) {
		// Math error checking disabled.
		if (ignoreerrors) {
			if (hasoutputarray) {
				abs__signed_int_2_simd(arraylen, data, dataout);
			} else {
				abs__signed_int_1_simd(arraylen, data);
			}
			return ARR_NO_ERR;
		} else {
		// Math error checking enabled.
			if (hasoutputarray) {
				ovflresult = abs__signed_int_2_simd_ovfl(arraylen, data, dataout);
			} else {
				ovflresult = abs__signed_int_1_simd_ovfl(arraylen, data);
			}

			if (ovflresult) { 
				return ARR_ERR_OVFL; 
			} else {
				return ARR_NO_ERR;
			}
		}

	} else {
#endif

	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				if ( minval_loop_willoverflow_signed_int(data[x]) ) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ( minval_loop_willoverflow_signed_int(data[x]) ) {return ARR_ERR_OVFL;}
				data[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		}
	}


#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
	}
#endif


	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int abs__signed_long(Py_ssize_t arraylen, int nosimd, signed long *data, signed long *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				if ( minval_loop_willoverflow_signed_long(data[x]) ) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ( minval_loop_willoverflow_signed_long(data[x]) ) {return ARR_ERR_OVFL;}
				data[x] = data[x] >= 0 ? data[x] : -data[x];
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
signed int abs__signed_long_long(Py_ssize_t arraylen, int nosimd, signed long long *data, signed long long *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				if ( minval_loop_willoverflow_signed_long_long(data[x]) ) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ( minval_loop_willoverflow_signed_long_long(data[x]) ) {return ARR_ERR_OVFL;}
				data[x] = data[x] >= 0 ? data[x] : -data[x];
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
signed int abs__float(Py_ssize_t arraylen, int nosimd, float *data, float *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = fabsf(data[x]);
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = fabsf(data[x]);
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = fabsf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = fabsf(data[x]);
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
signed int abs__double(Py_ssize_t arraylen, int nosimd, double *data, double *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = fabs(data[x]);
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = fabs(data[x]);
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = fabs(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = fabs(data[x]);
				if (!isfinite(data[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
	}

	return ARR_NO_ERR;

}



/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_abs_(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;

	// This is used to hold the parsed parameters.
	struct args_params_1 arraydata = ARGSINIT_ONE;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_one(self, args, keywds, 1, "abs_");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}

	// Call the C function.
	switch(arraydata.arraytype) {

		// signed_char
		case 'b' : {
			resultcode = abs__signed_char(arraydata.arraylength, arraydata.nosimd, arraydata.array1.b, arraydata.array2.b, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// signed_short
		case 'h' : {
			resultcode = abs__signed_short(arraydata.arraylength, arraydata.nosimd, arraydata.array1.h, arraydata.array2.h, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// signed_int
		case 'i' : {
			resultcode = abs__signed_int(arraydata.arraylength, arraydata.nosimd, arraydata.array1.i, arraydata.array2.i, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// signed_long
		case 'l' : {
			resultcode = abs__signed_long(arraydata.arraylength, arraydata.nosimd, arraydata.array1.l, arraydata.array2.l, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// signed_long_long
		case 'q' : {
			resultcode = abs__signed_long_long(arraydata.arraylength, arraydata.nosimd, arraydata.array1.q, arraydata.array2.q, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// float
		case 'f' : {
			resultcode = abs__float(arraydata.arraylength, arraydata.nosimd, arraydata.array1.f, arraydata.array2.f, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// double
		case 'd' : {
			resultcode = abs__double(arraydata.arraylength, arraydata.nosimd, arraydata.array1.d, arraydata.array2.d, arraydata.ignoreerrors, arraydata.hasoutputarray);
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
PyDoc_STRVAR(abs___doc__,
"abs_ \n\
_____________________________ \n\
\n\
Calculate abs_ over the values in an array.  \n\
\n\
======================  ============================================== \n\
Equivalent to:          [abs(x) for x in array1] \n\
======================  ============================================== \n\
\n\
======================  ============================================== \n\
Array types supported:  b, h, i, l, q, f, d \n\
Exceptions raised:      OverflowError \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
    abs_(array1) \n\
    abs_(array1, outparray) \n\
    abs_(array1, maxlen=y) \n\
    abs_(array1, matherrors=False)) \n\
    abs_(array1, nosimd=False) \n\
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
* nosimd - If True, SIMD acceleration is disabled. This parameter is \n\
  optional. The default is FALSE.  \n\
");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "abs_" is the name seen inside of Python. 
 "py_abs_" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef abs__methods[] = {
	{"abs_",  (PyCFunction)py_abs_, METH_VARARGS | METH_KEYWORDS, abs___doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef abs_module = {
    PyModuleDef_HEAD_INIT,
    "abs_",
    NULL,
    -1,
    abs__methods
};

PyMODINIT_FUNC PyInit_abs_(void)
{
    return PyModule_Create(&abs_module);
};

/*--------------------------------------------------------------------------- */

