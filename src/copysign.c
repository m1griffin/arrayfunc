//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   copysign.c
// Purpose:  Calculate the copysign of values in an array.
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

#include "arrayparams_two.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int copysign_float_1(Py_ssize_t arraylen, float *data1, float param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = copysignf(data1[x], param);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = copysignf(data1[x], param);
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int copysign_float_2(Py_ssize_t arraylen, float *data1, float param, float *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = copysignf(data1[x], param);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = copysignf(data1[x], param);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int copysign_float_3(Py_ssize_t arraylen, float param, float *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = copysignf(param, data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data2[x] = copysignf(param, data2[x]);
			if (!isfinite(data2[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int copysign_float_4(Py_ssize_t arraylen, float param, float *data2, float *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = copysignf(param, data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = copysignf(param, data2[x]);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int copysign_float_5(Py_ssize_t arraylen, float *data1, float *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = copysignf(data1[x], data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = copysignf(data1[x], data2[x]);
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int copysign_float_6(Py_ssize_t arraylen, float *data1, float *data2, float *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = copysignf(data1[x], data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = copysignf(data1[x], data2[x]);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int copysign_double_1(Py_ssize_t arraylen, double *data1, double param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = copysign(data1[x], param);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = copysign(data1[x], param);
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int copysign_double_2(Py_ssize_t arraylen, double *data1, double param, double *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = copysign(data1[x], param);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = copysign(data1[x], param);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int copysign_double_3(Py_ssize_t arraylen, double param, double *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = copysign(param, data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data2[x] = copysign(param, data2[x]);
			if (!isfinite(data2[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int copysign_double_4(Py_ssize_t arraylen, double param, double *data2, double *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = copysign(param, data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = copysign(param, data2[x]);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int copysign_double_5(Py_ssize_t arraylen, double *data1, double *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = copysign(data1[x], data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = copysign(data1[x], data2[x]);
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int copysign_double_6(Py_ssize_t arraylen, double *data1, double *data2, double *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = copysign(data1[x], data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = copysign(data1[x], data2[x]);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_copysign(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;

	// This is used to hold the parsed parameters.
	struct args_params_2 arraydata = ARGSINIT_TWO;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_two(self, args, keywds, 1, 0, "copysign");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}

	// Call the C function.
	switch(arraydata.arraytype) {
		// float
		case 'f' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = copysign_float_1(arraydata.arraylength, arraydata.array1.f, arraydata.param.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = copysign_float_2(arraydata.arraylength, arraydata.array1.f, arraydata.param.f, arraydata.array3.f, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = copysign_float_3(arraydata.arraylength, arraydata.param.f, arraydata.array2.f, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = copysign_float_4(arraydata.arraylength, arraydata.param.f, arraydata.array2.f, arraydata.array3.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = copysign_float_5(arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = copysign_float_6(arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.array3.f, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}
		// double
		case 'd' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = copysign_double_1(arraydata.arraylength, arraydata.array1.d, arraydata.param.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = copysign_double_2(arraydata.arraylength, arraydata.array1.d, arraydata.param.d, arraydata.array3.d, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = copysign_double_3(arraydata.arraylength, arraydata.param.d, arraydata.array2.d, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = copysign_double_4(arraydata.arraylength, arraydata.param.d, arraydata.array2.d, arraydata.array3.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = copysign_double_5(arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = copysign_double_6(arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.array3.d, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}
		// Wrong array type code.
		default: {
			releasebuffers_two(arraydata);
			ErrMsgTypeExpectFloat();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_two(arraydata);


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
PyDoc_STRVAR(copysign__doc__,
"copysign \n\
_____________________________ \n\
\n\
Calculate copysign over the values in an array.  \n\
\n\
======================  ============================================== \n\
Equivalent to:          [copysign(x, param) for x in array1] \n\
or                      [copysign(param, x) for x in array1] \n\
or                      [copysign(x, y) for x, y in zip(array1, array2)] \n\
======================  ============================================== \n\
\n\
======================  ============================================== \n\
Array types supported:  f, d \n\
Exceptions raised:      ArithmeticError \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
  copysign(array1, param) \n\
  copysign(array1, param, outparray) \n\
  copysign(param, array1) \n\
  copysign(param, array1, outparray) \n\
  copysign(array1, array2) \n\
  copysign(array1, array2, outparray) \n\
  copysign(array1, param, maxlen=y) \n\
  copysign(array1, param, matherrors=False) \n\
\n\
* array1 - The first input data array to be examined. If no output  \n\
  array is provided the results will overwrite the input data.  \n\
* param - A non-array numeric parameter.  \n\
* array2 - A second input data array. Each element in this array is  \n\
  applied to the corresponding element in the first array.  \n\
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
 "copysign" is the name seen inside of Python. 
 "py_copysign" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef copysign_methods[] = {
	{"copysign",  (PyCFunction)py_copysign, METH_VARARGS | METH_KEYWORDS, copysign__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef copysignmodule = {
    PyModuleDef_HEAD_INIT,
    "copysign",
    NULL,
    -1,
    copysign_methods
};

PyMODINIT_FUNC PyInit_copysign(void)
{
    return PyModule_Create(&copysignmodule);
};

/*--------------------------------------------------------------------------- */

