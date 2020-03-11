//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   cycle.c
// Purpose:  Fill an array with a series of values, repeating as necessary.
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
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   hasstep = If true, use the provided step value, otherwise use a default step.
   Returns nothing (void).
*/
void cycle_signed_char(Py_ssize_t arraylen, signed char *data, signed char startvalue, signed char stopvalue, signed char stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	signed char increment, step;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1;
	}

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: B
   arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   hasstep = If true, use the provided step value, otherwise use a default step.
   Returns nothing (void).
*/
void cycle_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char startvalue, unsigned char stopvalue, unsigned char stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	unsigned char increment, step;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1;
	}

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: h
   arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   hasstep = If true, use the provided step value, otherwise use a default step.
   Returns nothing (void).
*/
void cycle_signed_short(Py_ssize_t arraylen, signed short *data, signed short startvalue, signed short stopvalue, signed short stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	signed short increment, step;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1;
	}

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: H
   arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   hasstep = If true, use the provided step value, otherwise use a default step.
   Returns nothing (void).
*/
void cycle_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short startvalue, unsigned short stopvalue, unsigned short stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	unsigned short increment, step;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1;
	}

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: i
   arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   hasstep = If true, use the provided step value, otherwise use a default step.
   Returns nothing (void).
*/
void cycle_signed_int(Py_ssize_t arraylen, signed int *data, signed int startvalue, signed int stopvalue, signed int stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	signed int increment, step;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1;
	}

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: I
   arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   hasstep = If true, use the provided step value, otherwise use a default step.
   Returns nothing (void).
*/
void cycle_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int startvalue, unsigned int stopvalue, unsigned int stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	unsigned int increment, step;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1;
	}

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: l
   arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   hasstep = If true, use the provided step value, otherwise use a default step.
   Returns nothing (void).
*/
void cycle_signed_long(Py_ssize_t arraylen, signed long *data, signed long startvalue, signed long stopvalue, signed long stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	signed long increment, step;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1;
	}

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: L
   arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   hasstep = If true, use the provided step value, otherwise use a default step.
   Returns nothing (void).
*/
void cycle_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long startvalue, unsigned long stopvalue, unsigned long stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	unsigned long increment, step;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1;
	}

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: q
   arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   hasstep = If true, use the provided step value, otherwise use a default step.
   Returns nothing (void).
*/
void cycle_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long startvalue, signed long long stopvalue, signed long long stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	signed long long increment, step;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1;
	}

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: Q
   arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   hasstep = If true, use the provided step value, otherwise use a default step.
   Returns nothing (void).
*/
void cycle_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long startvalue, unsigned long long stopvalue, unsigned long long stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	unsigned long long increment, step;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1;
	}

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: f
   arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   hasstep = If true, use the provided step value, otherwise use a default step.
   Returns nothing (void).
*/
void cycle_float(Py_ssize_t arraylen, float *data, float startvalue, float stopvalue, float stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	float increment, step;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1.0;
	}

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */
/* For arraycode: d
   arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   hasstep = If true, use the provided step value, otherwise use a default step.
   Returns nothing (void).
*/
void cycle_double(Py_ssize_t arraylen, double *data, double startvalue, double stopvalue, double stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	double increment, step;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1.0;
	}

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_cycle(PyObject *self, PyObject *args, PyObject *keywds) {


	// This is used to hold the parsed parameters.
	struct args_params_cntcycrep arraydata = ARGSINIT_CNTCYCREP;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_cycle(self, args, keywds, "cycle");

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
			cycle_signed_char(arraydata.arraylength, arraydata.array1.b, arraydata.param1.b, arraydata.param2.b, arraydata.param3.b, arraydata.hasparam3);
			break;
		}
		// unsigned char
		case 'B' : {
			cycle_unsigned_char(arraydata.arraylength, arraydata.array1.B, arraydata.param1.B, arraydata.param2.B, arraydata.param3.B, arraydata.hasparam3);
			break;
		}
		// signed short
		case 'h' : {
			cycle_signed_short(arraydata.arraylength, arraydata.array1.h, arraydata.param1.h, arraydata.param2.h, arraydata.param3.h, arraydata.hasparam3);
			break;
		}
		// unsigned short
		case 'H' : {
			cycle_unsigned_short(arraydata.arraylength, arraydata.array1.H, arraydata.param1.H, arraydata.param2.H, arraydata.param3.H, arraydata.hasparam3);
			break;
		}
		// signed int
		case 'i' : {
			cycle_signed_int(arraydata.arraylength, arraydata.array1.i, arraydata.param1.i, arraydata.param2.i, arraydata.param3.i, arraydata.hasparam3);
			break;
		}
		// unsigned int
		case 'I' : {
			cycle_unsigned_int(arraydata.arraylength, arraydata.array1.I, arraydata.param1.I, arraydata.param2.I, arraydata.param3.I, arraydata.hasparam3);
			break;
		}
		// signed long
		case 'l' : {
			cycle_signed_long(arraydata.arraylength, arraydata.array1.l, arraydata.param1.l, arraydata.param2.l, arraydata.param3.l, arraydata.hasparam3);
			break;
		}
		// unsigned long
		case 'L' : {
			cycle_unsigned_long(arraydata.arraylength, arraydata.array1.L, arraydata.param1.L, arraydata.param2.L, arraydata.param3.L, arraydata.hasparam3);
			break;
		}
		// signed long long
		case 'q' : {
			cycle_signed_long_long(arraydata.arraylength, arraydata.array1.q, arraydata.param1.q, arraydata.param2.q, arraydata.param3.q, arraydata.hasparam3);
			break;
		}
		// unsigned long long
		case 'Q' : {
			cycle_unsigned_long_long(arraydata.arraylength, arraydata.array1.Q, arraydata.param1.Q, arraydata.param2.Q, arraydata.param3.Q, arraydata.hasparam3);
			break;
		}
		// float
		case 'f' : {
			cycle_float(arraydata.arraylength, arraydata.array1.f, arraydata.param1.f, arraydata.param2.f, arraydata.param3.f, arraydata.hasparam3);
			break;
		}
		// double
		case 'd' : {
			cycle_double(arraydata.arraylength, arraydata.array1.d, arraydata.param1.d, arraydata.param2.d, arraydata.param3.d, arraydata.hasparam3);
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
PyDoc_STRVAR(cycle__doc__,
"cycle \n\
_____________________________ \n\
\n\
Fill an array with a series of values, repeating as necessary. \n\
\n\
======================  ============================================== \n\
Equivalent to:          itertools.cycle(itertools.count(start, len(array)))\n\
or                      itertools.cycle(itertools.count(start, len(array), step))\n\
======================  ============================================== \n\
\n\
======================  ============================================== \n\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
  cycle(array, start, stop, step) \n\
\n\
* array - The output array. \n\
* start - The numeric value to start from. \n\
* stop - The value at which to stop incrementing. If stop is less than \n\
  start, cycle will count down. \n\
* step - The value to increment by when creating each element. This \n\
  parameter is optional. If it is omitted, a value of 1 is assumed. The\n\
  sign is ignored and the absolute value used when incrementing.");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "cycle" is the name seen inside of Python. 
 "py_cycle" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef cycle_methods[] = {
	{"cycle",  (PyCFunction)py_cycle, METH_VARARGS | METH_KEYWORDS, cycle__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef cyclemodule = {
    PyModuleDef_HEAD_INIT,
    "cycle",
    NULL,
    -1,
    cycle_methods
};

PyMODINIT_FUNC PyInit_cycle(void)
{
    return PyModule_Create(&cyclemodule);
};

/*--------------------------------------------------------------------------- */

