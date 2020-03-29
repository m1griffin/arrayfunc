//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   invert.c
// Purpose:  Calculate the invert of values in an array.
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
#include "invert_simd_x86.h"
#endif

#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
#include "arm_neon.h"
#endif

#if defined(AF_HASSIMD_ARMv7_32BIT)
#include "invert_simd_armv7.h"
#endif

#if defined(AF_HASSIMD_ARM_AARCH64)
#include "invert_simd_armv8.h"
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   hasoutputarray = If true, the output goes into the second array.
   nosimd = If true, disable SIMD acceleration.
*/
void invert_signed_char(Py_ssize_t arraylen, int nosimd, signed char *data, signed char *dataout, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
		if (hasoutputarray) {
			invert_signed_char_2_simd(arraylen, data, dataout);
		} else {
			invert_signed_char_1_simd(arraylen, data);
		}
		return;
	}
#endif

	if (hasoutputarray) {		
		for (x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data[x] = ~data[x];
		}
	}

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   hasoutputarray = If true, the output goes into the second array.
   nosimd = If true, disable SIMD acceleration.
*/
void invert_unsigned_char(Py_ssize_t arraylen, int nosimd, unsigned char *data, unsigned char *dataout, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
		if (hasoutputarray) {
			invert_unsigned_char_2_simd(arraylen, data, dataout);
		} else {
			invert_unsigned_char_1_simd(arraylen, data);
		}
		return;
	}
#endif

	if (hasoutputarray) {		
		for (x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data[x] = ~data[x];
		}
	}

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   hasoutputarray = If true, the output goes into the second array.
   nosimd = If true, disable SIMD acceleration.
*/
void invert_signed_short(Py_ssize_t arraylen, int nosimd, signed short *data, signed short *dataout, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
		if (hasoutputarray) {
			invert_signed_short_2_simd(arraylen, data, dataout);
		} else {
			invert_signed_short_1_simd(arraylen, data);
		}
		return;
	}
#endif

	if (hasoutputarray) {		
		for (x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data[x] = ~data[x];
		}
	}

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   hasoutputarray = If true, the output goes into the second array.
   nosimd = If true, disable SIMD acceleration.
*/
void invert_unsigned_short(Py_ssize_t arraylen, int nosimd, unsigned short *data, unsigned short *dataout, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
		if (hasoutputarray) {
			invert_unsigned_short_2_simd(arraylen, data, dataout);
		} else {
			invert_unsigned_short_1_simd(arraylen, data);
		}
		return;
	}
#endif

	if (hasoutputarray) {		
		for (x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data[x] = ~data[x];
		}
	}

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   hasoutputarray = If true, the output goes into the second array.
   nosimd = If true, disable SIMD acceleration.
*/
void invert_signed_int(Py_ssize_t arraylen, int nosimd, signed int *data, signed int *dataout, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
		if (hasoutputarray) {
			invert_signed_int_2_simd(arraylen, data, dataout);
		} else {
			invert_signed_int_1_simd(arraylen, data);
		}
		return;
	}
#endif

	if (hasoutputarray) {		
		for (x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data[x] = ~data[x];
		}
	}

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   hasoutputarray = If true, the output goes into the second array.
   nosimd = If true, disable SIMD acceleration.
*/
void invert_unsigned_int(Py_ssize_t arraylen, int nosimd, unsigned int *data, unsigned int *dataout, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
		if (hasoutputarray) {
			invert_unsigned_int_2_simd(arraylen, data, dataout);
		} else {
			invert_unsigned_int_1_simd(arraylen, data);
		}
		return;
	}
#endif

	if (hasoutputarray) {		
		for (x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data[x] = ~data[x];
		}
	}

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   hasoutputarray = If true, the output goes into the second array.
   nosimd = If true, disable SIMD acceleration.
*/
void invert_signed_long(Py_ssize_t arraylen, int nosimd, signed long *data, signed long *dataout, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	if (hasoutputarray) {		
		for (x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data[x] = ~data[x];
		}
	}

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   hasoutputarray = If true, the output goes into the second array.
   nosimd = If true, disable SIMD acceleration.
*/
void invert_unsigned_long(Py_ssize_t arraylen, int nosimd, unsigned long *data, unsigned long *dataout, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	if (hasoutputarray) {		
		for (x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data[x] = ~data[x];
		}
	}

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   hasoutputarray = If true, the output goes into the second array.
   nosimd = If true, disable SIMD acceleration.
*/
void invert_signed_long_long(Py_ssize_t arraylen, int nosimd, signed long long *data, signed long long *dataout, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	if (hasoutputarray) {		
		for (x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data[x] = ~data[x];
		}
	}

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   hasoutputarray = If true, the output goes into the second array.
   nosimd = If true, disable SIMD acceleration.
*/
void invert_unsigned_long_long(Py_ssize_t arraylen, int nosimd, unsigned long long *data, unsigned long long *dataout, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	if (hasoutputarray) {		
		for (x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data[x] = ~data[x];
		}
	}

}



/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_invert(PyObject *self, PyObject *args, PyObject *keywds) {


	// This is used to hold the parsed parameters.
	struct args_params_1 arraydata = ARGSINIT_ONE;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_one(self, args, keywds, 0, "invert");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}

	// Call the C function.
	switch(arraydata.arraytype) {

		// signed_char
		case 'b' : {
			invert_signed_char(arraydata.arraylength, arraydata.nosimd, arraydata.array1.b, arraydata.array2.b, arraydata.hasoutputarray);
			break;
		}

		// unsigned_char
		case 'B' : {
			invert_unsigned_char(arraydata.arraylength, arraydata.nosimd, arraydata.array1.B, arraydata.array2.B, arraydata.hasoutputarray);
			break;
		}

		// signed_short
		case 'h' : {
			invert_signed_short(arraydata.arraylength, arraydata.nosimd, arraydata.array1.h, arraydata.array2.h, arraydata.hasoutputarray);
			break;
		}

		// unsigned_short
		case 'H' : {
			invert_unsigned_short(arraydata.arraylength, arraydata.nosimd, arraydata.array1.H, arraydata.array2.H, arraydata.hasoutputarray);
			break;
		}

		// signed_int
		case 'i' : {
			invert_signed_int(arraydata.arraylength, arraydata.nosimd, arraydata.array1.i, arraydata.array2.i, arraydata.hasoutputarray);
			break;
		}

		// unsigned_int
		case 'I' : {
			invert_unsigned_int(arraydata.arraylength, arraydata.nosimd, arraydata.array1.I, arraydata.array2.I, arraydata.hasoutputarray);
			break;
		}

		// signed_long
		case 'l' : {
			invert_signed_long(arraydata.arraylength, arraydata.nosimd, arraydata.array1.l, arraydata.array2.l, arraydata.hasoutputarray);
			break;
		}

		// unsigned_long
		case 'L' : {
			invert_unsigned_long(arraydata.arraylength, arraydata.nosimd, arraydata.array1.L, arraydata.array2.L, arraydata.hasoutputarray);
			break;
		}

		// signed_long_long
		case 'q' : {
			invert_signed_long_long(arraydata.arraylength, arraydata.nosimd, arraydata.array1.q, arraydata.array2.q, arraydata.hasoutputarray);
			break;
		}

		// unsigned_long_long
		case 'Q' : {
			invert_unsigned_long_long(arraydata.arraylength, arraydata.nosimd, arraydata.array1.Q, arraydata.array2.Q, arraydata.hasoutputarray);
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


	// Everything was successful.
	Py_RETURN_NONE;

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(invert__doc__,
"invert \n\
_____________________________ \n\
\n\
Calculate invert over the values in an array.  \n\
\n\
======================  ============================================== \n\
Equivalent to:          [~x for x in array1] \n\
======================  ============================================== \n\
\n\
======================  ============================================== \n\
Array types supported:  b, B, h, H, i, I, l, L, q, Q \n\
Exceptions raised:       \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
    invert(array1) \n\
    invert(array1, outparray) \n\
    invert(array1, maxlen=y) \n\
    invert(array1, nosimd=False) \n\
 \n\
* array1 - The first input data array to be examined. If no output  \n\
  array is provided the results will overwrite the input data.  \n\
* outparray - The output array. This parameter is optional.  \n\
* maxlen - Limit the length of the array used. This must be a valid  \n\
  positive integer. If a zero or negative length, or a value which is  \n\
  greater than the actual length of the array is specified, this  \n\
  parameter is ignored.  \n\
* nosimd - If True, SIMD acceleration is disabled. This parameter is \n\
  optional. The default is FALSE.  \n\
");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "invert" is the name seen inside of Python. 
 "py_invert" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef invert_methods[] = {
	{"invert",  (PyCFunction)py_invert, METH_VARARGS | METH_KEYWORDS, invert__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef invertmodule = {
    PyModuleDef_HEAD_INIT,
    "invert",
    NULL,
    -1,
    invert_methods
};

PyMODINIT_FUNC PyInit_invert(void)
{
    return PyModule_Create(&invertmodule);
};

/*--------------------------------------------------------------------------- */

