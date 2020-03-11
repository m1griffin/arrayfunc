//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   repeat.c
// Purpose:  Fill an array with a specified value.
// Language: C
// Date:     04-Jun-2019.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2019    Michael Griffin    <m12.griffin@gmail.com>
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

#include "arrayerrs.h"

#include "arrayparams_base.h"

#include "arrayparams_cntcycrep.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For arraycode: b
   arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_signed_char(Py_ssize_t arraylen, signed char *data, signed char fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* For arraycode: B
   arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* For arraycode: h
   arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_signed_short(Py_ssize_t arraylen, signed short *data, signed short fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* For arraycode: H
   arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* For arraycode: i
   arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_signed_int(Py_ssize_t arraylen, signed int *data, signed int fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* For arraycode: I
   arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* For arraycode: l
   arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_signed_long(Py_ssize_t arraylen, signed long *data, signed long fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* For arraycode: L
   arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* For arraycode: q
   arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* For arraycode: Q
   arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* For arraycode: f
   arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_float(Py_ssize_t arraylen, float *data, float fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* For arraycode: d
   arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_double(Py_ssize_t arraylen, double *data, double fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_repeat(PyObject *self, PyObject *args, PyObject *keywds) {


	// This is used to hold the parsed parameters.
	struct args_params_cntcycrep arraydata = ARGSINIT_CNTCYCREP;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_repeat(self, args, keywds, "repeat");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}


	// The length of the data array.
	if (arraydata.arraylength < 1) {
		// Release the buffers. 
		releasebuffers_cntcycrep(arraydata);
		ErrMsgArrayLengthErr();
		return NULL;
	}



	/* Call the C function */
	switch(arraydata.arraytype) {
		// signed char
		case 'b' : {
			repeat_signed_char(arraydata.arraylength, arraydata.array1.b, arraydata.param1.b);
			break;
		}
		// unsigned char
		case 'B' : {
			repeat_unsigned_char(arraydata.arraylength, arraydata.array1.B, arraydata.param1.B);
			break;
		}
		// signed short
		case 'h' : {
			repeat_signed_short(arraydata.arraylength, arraydata.array1.h, arraydata.param1.h);
			break;
		}
		// unsigned short
		case 'H' : {
			repeat_unsigned_short(arraydata.arraylength, arraydata.array1.H, arraydata.param1.H);
			break;
		}
		// signed int
		case 'i' : {
			repeat_signed_int(arraydata.arraylength, arraydata.array1.i, arraydata.param1.i);
			break;
		}
		// unsigned int
		case 'I' : {
			repeat_unsigned_int(arraydata.arraylength, arraydata.array1.I, arraydata.param1.I);
			break;
		}
		// signed long
		case 'l' : {
			repeat_signed_long(arraydata.arraylength, arraydata.array1.l, arraydata.param1.l);
			break;
		}
		// unsigned long
		case 'L' : {
			repeat_unsigned_long(arraydata.arraylength, arraydata.array1.L, arraydata.param1.L);
			break;
		}
		// signed long long
		case 'q' : {
			repeat_signed_long_long(arraydata.arraylength, arraydata.array1.q, arraydata.param1.q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			repeat_unsigned_long_long(arraydata.arraylength, arraydata.array1.Q, arraydata.param1.Q);
			break;
		}
		// float
		case 'f' : {
			repeat_float(arraydata.arraylength, arraydata.array1.f, arraydata.param1.f);
			break;
		}
		// double
		case 'd' : {
			repeat_double(arraydata.arraylength, arraydata.array1.d, arraydata.param1.d);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_cntcycrep(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_cntcycrep(arraydata);

	// Everything was successful.
	Py_RETURN_NONE;


}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(repeat__doc__,
"repeat \n\
_____________________________ \n\
\n\
Fill an array with a specified value. \n\
\n\
======================  ============================================== \n\
Equivalent to:          itertools.repeat(value)\n\
======================  ============================================== \n\
\n\
======================  ============================================== \n\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
  repeat(array, value) \n\
\n\
* array - The output array. \n\
* value - The value to use to fill the array.");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "repeat" is the name seen inside of Python. 
 "py_repeat" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef repeat_methods[] = {
	{"repeat",  (PyCFunction)py_repeat, METH_VARARGS | METH_KEYWORDS, repeat__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef repeatmodule = {
    PyModuleDef_HEAD_INIT,
    "repeat",
    NULL,
    -1,
    repeat_methods
};

PyMODINIT_FUNC PyInit_repeat(void)
{
    return PyModule_Create(&repeatmodule);
};

/*--------------------------------------------------------------------------- */

