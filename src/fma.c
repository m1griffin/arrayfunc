//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   fma.c
// Purpose:  Calculate the fma of values in an array.
// Language: C
// Date:     15-Nov-2018.
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

#include "arrayparams_three.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   data4 = The fourth data array.
   param2 = The parameter which may be used in place of data2.
   param3 = The parameter which may be used in place of data3.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_num_none
signed int fma_float_1(Py_ssize_t arraylen, float *data1, float param2, float param3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * param2 + param3;
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * param2 + param3;
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_num_arr
signed int fma_float_2(Py_ssize_t arraylen, float *data1, float param2, float param3, float *data4, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data4[x] = data1[x] * param2 + param3;
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data4[x] = data1[x] * param2 + param3;
			if (!isfinite(data4[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_num_none
signed int fma_float_3(Py_ssize_t arraylen, float *data1, float *data2, float param3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * data2[x] + param3;
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * data2[x] + param3;
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_num_arr
signed int fma_float_4(Py_ssize_t arraylen, float *data1, float *data2, float param3, float *data4, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data4[x] = data1[x] * data2[x] + param3;
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data4[x] = data1[x] * data2[x] + param3;
			if (!isfinite(data4[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr_none
signed int fma_float_5(Py_ssize_t arraylen, float *data1, float param2, float *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * param2 + data3[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * param2 + data3[x];
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr_arr
signed int fma_float_6(Py_ssize_t arraylen, float *data1, float param2, float *data3, float *data4, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data4[x] = data1[x] * param2 + data3[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data4[x] = data1[x] * param2 + data3[x];
			if (!isfinite(data4[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr_none
signed int fma_float_7(Py_ssize_t arraylen, float *data1, float *data2, float *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * data2[x] + data3[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * data2[x] + data3[x];
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr_arr
signed int fma_float_8(Py_ssize_t arraylen, float *data1, float *data2, float *data3, float *data4, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data4[x] = data1[x] * data2[x] + data3[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data4[x] = data1[x] * data2[x] + data3[x];
			if (!isfinite(data4[x])) {return ARR_ERR_ARITHMETIC;}
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
   data4 = The fourth data array.
   param2 = The parameter which may be used in place of data2.
   param3 = The parameter which may be used in place of data3.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_num_none
signed int fma_double_1(Py_ssize_t arraylen, double *data1, double param2, double param3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * param2 + param3;
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * param2 + param3;
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_num_arr
signed int fma_double_2(Py_ssize_t arraylen, double *data1, double param2, double param3, double *data4, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data4[x] = data1[x] * param2 + param3;
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data4[x] = data1[x] * param2 + param3;
			if (!isfinite(data4[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_num_none
signed int fma_double_3(Py_ssize_t arraylen, double *data1, double *data2, double param3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * data2[x] + param3;
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * data2[x] + param3;
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_num_arr
signed int fma_double_4(Py_ssize_t arraylen, double *data1, double *data2, double param3, double *data4, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data4[x] = data1[x] * data2[x] + param3;
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data4[x] = data1[x] * data2[x] + param3;
			if (!isfinite(data4[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr_none
signed int fma_double_5(Py_ssize_t arraylen, double *data1, double param2, double *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * param2 + data3[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * param2 + data3[x];
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr_arr
signed int fma_double_6(Py_ssize_t arraylen, double *data1, double param2, double *data3, double *data4, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data4[x] = data1[x] * param2 + data3[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data4[x] = data1[x] * param2 + data3[x];
			if (!isfinite(data4[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr_none
signed int fma_double_7(Py_ssize_t arraylen, double *data1, double *data2, double *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * data2[x] + data3[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * data2[x] + data3[x];
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr_arr
signed int fma_double_8(Py_ssize_t arraylen, double *data1, double *data2, double *data3, double *data4, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data4[x] = data1[x] * data2[x] + data3[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data4[x] = data1[x] * data2[x] + data3[x];
			if (!isfinite(data4[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_fma(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;

	// This is used to hold the parsed parameters.
	struct args_params_3 arraydata = ARGSINIT_THREE;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_three(self, args, keywds, "fma");

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
				case param_arr_num_num_none : {
					resultcode = fma_float_1(arraydata.arraylength, arraydata.array1.f, arraydata.param2.f, arraydata.param3.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_num_arr : {
					resultcode = fma_float_2(arraydata.arraylength, arraydata.array1.f, arraydata.param2.f, arraydata.param3.f, arraydata.array4.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_num_none : {
					resultcode = fma_float_3(arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.param3.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_num_arr : {
					resultcode = fma_float_4(arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.param3.f, arraydata.array4.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr_none : {
					resultcode = fma_float_5(arraydata.arraylength, arraydata.array1.f, arraydata.param2.f, arraydata.array3.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr_arr : {
					resultcode = fma_float_6(arraydata.arraylength, arraydata.array1.f, arraydata.param2.f, arraydata.array3.f, arraydata.array4.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr_none : {
					resultcode = fma_float_7(arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.array3.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr_arr : {
					resultcode = fma_float_8(arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.array3.f, arraydata.array4.f, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}
		// double
		case 'd' : {
			switch (arraydata.paramcat) {
				case param_arr_num_num_none : {
					resultcode = fma_double_1(arraydata.arraylength, arraydata.array1.d, arraydata.param2.d, arraydata.param3.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_num_arr : {
					resultcode = fma_double_2(arraydata.arraylength, arraydata.array1.d, arraydata.param2.d, arraydata.param3.d, arraydata.array4.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_num_none : {
					resultcode = fma_double_3(arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.param3.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_num_arr : {
					resultcode = fma_double_4(arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.param3.d, arraydata.array4.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr_none : {
					resultcode = fma_double_5(arraydata.arraylength, arraydata.array1.d, arraydata.param2.d, arraydata.array3.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr_arr : {
					resultcode = fma_double_6(arraydata.arraylength, arraydata.array1.d, arraydata.param2.d, arraydata.array3.d, arraydata.array4.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr_none : {
					resultcode = fma_double_7(arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.array3.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr_arr : {
					resultcode = fma_double_8(arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.array3.d, arraydata.array4.d, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}
		// Wrong array type code.
		default: {
			releasebuffers_three(arraydata);
			ErrMsgTypeExpectFloat();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_three(arraydata);


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
PyDoc_STRVAR(fma__doc__,
"fma \n\
_____________________________ \n\
\n\
Calculate fma over the values in an array.  \n\
\n\
======================  ============================================== \n\
Equivalent to:          [(x * param2 + param3) for x in array1] \n\
or                      [(x * y + param3) for x,y in zip(array1, array2)] \n\
or                      [(x * param2 + z) for x,z in zip(array1, array3)] \n\
or                      [(x * y + z) for x,y,z in zip(array1, array2, array3)] \n\
======================  ============================================== \n\
\n\
======================  ============================================== \n\
Array types supported:  f, d \n\
Exceptions raised:      ArithmeticError \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
  fma(array1, array2, array3) \n\
  fma(array1, array2, array3, outparray) \n\
  fma(array1, array2, param3) \n\
  fma(array1, array2, param3, outparray) \n\
  fma(array1, param2, array3) \n\
  fma(array1, param2, array3, outparray) \n\
  fma(array1, param2, param3) \n\
  fma(array1, param2, param3, outparray) \n\
  fma(array1, array2, array3, maxlen=y) \n\
  fma(array1, array2, array3, matherrors=False) \n\
\n\
* array1 - The first input data array to be examined. If no output  \n\
  array is provided the results will overwrite the input data.  \n\
* array2 - A second input data array. Each element in this array is  \n\
    applied to the corresponding element in the first array.  \n\
* param2 - A non-array numeric parameter which may be used in place  \n\
    of array2.  \n\
* array3 - A third input data array. Each element in this array is  \n\
  applied to the corresponding element in the first array.  \n\
* param3 - A non-array numeric parameter which may be used in place  \n\
    of array3.  \n\
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
 "fma" is the name seen inside of Python. 
 "py_fma" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef fma_methods[] = {
	{"fma",  (PyCFunction)py_fma, METH_VARARGS | METH_KEYWORDS, fma__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef fmamodule = {
    PyModuleDef_HEAD_INIT,
    "fma",
    NULL,
    -1,
    fma_methods
};

PyMODINIT_FUNC PyInit_fma(void)
{
    return PyModule_Create(&fmamodule);
};

/*--------------------------------------------------------------------------- */

