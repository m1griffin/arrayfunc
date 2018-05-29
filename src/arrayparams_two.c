//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayfunc.c
// Purpose:  Common functions for arrayfunc.
// Language: C
// Date:     28-Nov-2017
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2017    Michael Griffin    <m12.griffin@gmail.com>
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

#include "Python.h"

#include <string.h>
#include <limits.h>

#include "arrayerrs.h"
#include "arrayparams_base.h"
#include "arrayparams_two.h"


/*--------------------------------------------------------------------------- */


// Least significant digit is the first parameter.
// Most significant digit is the second parameter.
// 1 = Array, A = Integer, B = Float, C = Double.
#define IS_CAT_ARR_INT_ANY    0xA1
#define IS_CAT_ARR_FLOAT_ANY  0xB1
#define IS_CAT_ARR_DOUBLE_ANY 0xC1

#define IS_CAT_INT_ARR_ANY    0x1A
#define IS_CAT_FLOAT_ARR_ANY  0x1B
#define IS_CAT_DOUBLE_ARR_ANY 0x1C

#define IS_CAT_ARR_ARR_ANY 0x11

#define IS_CAT_INVALID 0


enum paramtypes
{ 
	param_is_int,
	param_is_float,
	param_is_double
};

// The valid combinations of the first two parameters.
// The INT, FLOAT, DOUBLE indicates the data type. Both must be the same.
// The ARR and NUM indicate the three parameters are an array or number.
// Since the third array is optional and always an array if present, we will
// check it later.
// There are two codes for invalid. One indicates an invalid combination of
// array and number (e.g. two numbers). The other indicates the data types of
// the two parameters (e.g. float, integer) are not the same.
enum paramclass {
 CAT_INT_ARR_NUM,
 CAT_FLOAT_ARR_NUM,
 CAT_DOUBLE_ARR_NUM,
 CAT_INT_NUM_ARR,
 CAT_FLOAT_NUM_ARR,
 CAT_DOUBLE_NUM_ARR,
 CAT_ANY_ARR_ARR,
 CAT_INVALID_COMB,
 CAT_INVALID_TYPE
};

/*--------------------------------------------------------------------------- */

// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist_2[] = {"data1", "data2", "dataout", "matherrors", "maxlen", NULL};

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

// Determine the category the parameters fall into, and whether they are. 
// compatible with each other. We are only checking two objects in this case.
//  dataobj1 = The first array or number object to be tested.
//  dataobj2 = The second array or number object to be tested.
// Return: A code indicating the parameter category, taking both parameters
//  into consideration. The code uses the CAT_* enums.
// 
unsigned int param2cat(PyObject *dataobj1, PyObject *dataobj2) {

	// An array and a number.
	if (isarrayobjtype(dataobj1) && isnumberobjcat(dataobj2)) {
		if (isintarrayobjtype(dataobj1) && isintobjtype(dataobj2)) { return CAT_INT_ARR_NUM; }
		if (isfloatarrayobjtype(dataobj1) && isfloatobjtype(dataobj2)) { return CAT_FLOAT_ARR_NUM; }
		if (isdoublearrayobjtype(dataobj1) && isfloatobjtype(dataobj2)) { return CAT_DOUBLE_ARR_NUM; }
		// The data types are incompatible.
		return CAT_INVALID_TYPE;
	}

	// A number and an array.
	if (isnumberobjcat(dataobj1) && isarrayobjtype(dataobj2)) {
		if (isintobjtype(dataobj1) && isintarrayobjtype(dataobj2)) { return CAT_INT_NUM_ARR; }
		if (isfloatobjtype(dataobj1) && isfloatarrayobjtype(dataobj2)) { return CAT_FLOAT_NUM_ARR; }
		if (isfloatobjtype(dataobj1) && isdoublearrayobjtype(dataobj2)) { return CAT_DOUBLE_NUM_ARR; }
		// The data types are incompatible.
		return CAT_INVALID_TYPE;
	}

	// An array and an array. We don't care at this point what the array type is,
	// so long as it is the same for both.
	if (isarrayobjtype(dataobj1) && isarrayobjtype(dataobj2)) {
		if (isintarrayobjtype(dataobj1) && isintarrayobjtype(dataobj2)) { return CAT_ANY_ARR_ARR; }
		if (isfloatarrayobjtype(dataobj1) && isfloatarrayobjtype(dataobj2)) { return CAT_ANY_ARR_ARR; }
		if (isdoublearrayobjtype(dataobj1) && isdoublearrayobjtype(dataobj2)) { return CAT_ANY_ARR_ARR; }
		// The data types are incompatible.
		return CAT_INVALID_TYPE;
	}

	// If none of the parameters matched, we have an invalid combination of parameters.
	return CAT_INVALID_COMB;
}
/*--------------------------------------------------------------------------- */

/* Release the buffers which represent the arrays. This function checks if the
 * 	array object was not intiailised.
 * arraydata = Structure which contains the three array buffers to be released.
 * Returns: Nothing.
*/
void releasebuffers_two(struct args_params_2 arraydata) {
	if (!(&arraydata.pybuffer1 == NULL)) {
		PyBuffer_Release(&arraydata.pybuffer1);
	}

	if (!(&arraydata.pybuffer2 == NULL)) {
		PyBuffer_Release(&arraydata.pybuffer2);
	}

	if (!(&arraydata.pybuffer3 == NULL)) {
		PyBuffer_Release(&arraydata.pybuffer3);
	}

}

/*--------------------------------------------------------------------------- */


// Check that the array object matches the expected type derived from another.
// array. This simply checks for an exact match between the two array codes.
// Returns true if OK.
char arraycompatok(PyObject *dataobj3, char arraytype) {
	char arraycode;

	arraycode = lookuparraycode(dataobj3);

	return (arraytype == arraycode);

}


/*--------------------------------------------------------------------------- */

/* Get the parameters passed from Python with a function which takes one input 
 * 		array and one input value, or two input arrays, plus an optional
 * 		output array.
 * self, args, keywds = The parameters of the same name passed from the PyObject
 * 		function which forms the original entry point.
 * funcname = A string which represents the C extension name. This is passed to
 * 		PyArg_ParseTupleAndKeywords for error reporting.
 * Returns: A structure which contains the parameter data.
*/
struct args_params_2 getparams_two(PyObject *self, PyObject *args, PyObject *keywds, char *funcname) {


	// This is used for constructing parameter format strings. The size must
	// be able to hold the largest string, which will be determined by the 
	// names of the functions which use this.
	char formatstr[FMTSTRLEN];
	

	// This is used to return the parsed parameters.
	struct args_params_2 arraydata = ARGSINIT_TWO;

	PyObject *dataobj1 = NULL;
	PyObject *dataobj2 = NULL;
	PyObject *dataobj3 = NULL;

	// The input buffers are arrays of bytes.
	Py_buffer datapy1 = {NULL};
	Py_buffer datapy2 = {NULL};
	Py_buffer datapy3 = {NULL};


	// How long the array is.
	Py_ssize_t arraylength;

	// The numeric parameter version is available in all possible types.
	struct paramsvals parampy;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	// If true, *disabled* overflow checking.
	unsigned int ignoreerrors = 0;


	// These are used to track the types of each array.
	char arraytype;


	// The category of the parameters. That is, what type (array, number, none)
	// of each parameter. 
	enum paramcats paramcat;
	enum paramclass prmclass;

	// PyArg_ParseTuple does not match directly to the array codes. We need to
	// use some temporary variables of alternate types to parse the parameter 
	// data.
	// PyArg_ParseTuple does not check for overflow of unsigned parameters.
	signed long long paramtmp_q = 0;


	// -----------------------------------------------------


	// This section determines the type of the arrays. We do this by parsing
	// the parameters as objects. We then examine the parameters 

	// Construct the format string. This is constructed dynamically because
	// we must be able to call this same function from different C extensions.
	makefmtstr("OO|Oin:", funcname, formatstr);

	// Import the raw objects. 
	if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_2, &dataobj1, 
							&dataobj2, &dataobj3, &ignoreerrors, &arraymaxlen)) {
		ErrMsgParameterError();
		arraydata.error = 2;
		return arraydata;
	}



	// This categorises the first two parameters into classes that we can parse
	// more conveniently. This takes only the first two parameters into account.
	// It also does some basic checking to make sure the data types are compatible.
	prmclass = param2cat(dataobj1, dataobj2);
	if ((prmclass == CAT_INVALID_COMB) || (prmclass == CAT_INVALID_TYPE)) {
		ErrMsgParameterError();
		arraydata.error = 3;
		return arraydata;
	}


	// At this point we know the first two parameters are either a number and
	// an array, or an array and a number, or an array and an array.
	// We also know that the basic data types are compatible with each other.

	// The array type code is a character corresponding to the array.array codes.
	if (isarrayobjtype(dataobj1)) {
		arraytype = lookuparraycode(dataobj1);
	} else {
		arraytype = lookuparraycode(dataobj2);
	}


	// Now parse the objects into actual data we can access directly in C.
	// How we do this depends on the combination of parameters, including 
	// arrays, integers, floats, and doubles that we expect based on our 
	// previous examination of the objects.
	switch(prmclass){
		case CAT_INT_ARR_NUM : {
			if (ischeckedintcode(arraytype)) {
				// Unsigned integer number parameters types have to be checked
				// manually, so we check almost all integers this way. For 
				// parameter format strings, "L" is for a signed long long int.
				makefmtstr("y*L|y*in:", funcname, formatstr);

				// Import the parsed parameters. 
				if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_2, &datapy1, &paramtmp_q, &datapy3, &ignoreerrors, &arraymaxlen)) {
					ErrMsgParameterError();
					arraydata.error = 5;
					return arraydata;
				}

				// Check if the integer falls within the expected range for that array type.
				if (!intparamrangeok(arraytype, paramtmp_q, &parampy)) {
					ErrMsgParameterError();
					arraydata.error = 5;
					return arraydata;
				} 

			} else {
				// This is for the integer types which can't be handled by the above.
				switch (arraytype) {
					case 'L': {
						makefmtstr("y*k|y*in:", funcname, formatstr);

						// Import the parsed parameters. 
						if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_2, &datapy1, &parampy.L, &datapy3, &ignoreerrors, &arraymaxlen)) {
							ErrMsgParameterError();
							arraydata.error = 5;
							return arraydata;
						}
						break;

					}
					case 'Q':{
						makefmtstr("y*K|y*in:", funcname, formatstr);

						// Import the parsed parameters. 
						if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_2, &datapy1, &parampy.Q, &datapy3, &ignoreerrors, &arraymaxlen)) {
							ErrMsgParameterError();
							arraydata.error = 5;
							return arraydata;
						}
						break;
					}
					case 'q':{
						makefmtstr("y*L|y*in:", funcname, formatstr);

						// Import the parsed parameters. 
						if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_2, &datapy1, &parampy.q, &datapy3, &ignoreerrors, &arraymaxlen)) {
							ErrMsgParameterError();
							arraydata.error = 5;
							return arraydata;
						}
						break;
					}
				}
			}

			arraylength = calcarraylength(arraytype, datapy1.len);
			paramcat = param_arr_num_none;


			break;
		}
		case CAT_FLOAT_ARR_NUM : {
			makefmtstr("y*f|y*in:", funcname, formatstr);

			// Import the parsed parameters. 
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_2, &datapy1, &parampy.f, &datapy3, &ignoreerrors, &arraymaxlen)) {
				ErrMsgParameterError();
				arraydata.error = 5;
				return arraydata;
			}
			arraylength = calcarraylength(arraytype, datapy1.len);
			paramcat = param_arr_num_none;

			break;
		}
		case CAT_DOUBLE_ARR_NUM : {
			makefmtstr("y*d|y*in:", funcname, formatstr);

			// Import the parsed parameters. 
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_2, &datapy1, &parampy.d, &datapy3, &ignoreerrors, &arraymaxlen)) {
				ErrMsgParameterError();
				arraydata.error = 5;
				return arraydata;
			}
			arraylength = calcarraylength(arraytype, datapy1.len);
			paramcat = param_arr_num_none;

			break;
		}
		case CAT_INT_NUM_ARR : {
			if (ischeckedintcode(arraytype)) {
				// Unsigned integer number parameters types have to be checked
				// manually, so we check almost all integers this way. For 
				// parameter format strings, "L" is for a signed long long int.
				makefmtstr("Ly*|y*in:", funcname, formatstr);

				// Import the parsed parameters. 
				if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_2, &paramtmp_q, &datapy2, &datapy3, &ignoreerrors, &arraymaxlen)) {
					ErrMsgParameterError();
					arraydata.error = 5;
					return arraydata;
				}

				// Check if the integer falls within the expected range for that array type.
				if (!intparamrangeok(arraytype, paramtmp_q, &parampy)) {
					ErrMsgParameterError();
					arraydata.error = 5;
					return arraydata;
				} 
			} else {
				// This is for the integer types which can't be handled by the above.
				switch (arraytype) {
					case 'L': {
						makefmtstr("ky*|y*in:", funcname, formatstr);

						// Import the parsed parameters. 
						if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_2, &parampy.L, &datapy2, &datapy3, &ignoreerrors, &arraymaxlen)) {
							ErrMsgParameterError();
							arraydata.error = 5;
							return arraydata;
						}
						break;

					}
					case 'Q':{
						makefmtstr("Ky*|y*in:", funcname, formatstr);

						// Import the parsed parameters. 
						if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_2, &parampy.Q, &datapy2, &datapy3, &ignoreerrors, &arraymaxlen)) {
							ErrMsgParameterError();
							arraydata.error = 5;
							return arraydata;
						}
						break;
					}
					case 'q':{
						makefmtstr("Ly*|y*in:", funcname, formatstr);

						// Import the parsed parameters. 
						if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_2, &parampy.q, &datapy2, &datapy3, &ignoreerrors, &arraymaxlen)) {
							ErrMsgParameterError();
							arraydata.error = 5;
							return arraydata;
						}
						break;
					}
				}
			}

			arraylength = calcarraylength(arraytype, datapy2.len);
			paramcat = param_num_arr_none;

			break;
		}
		case CAT_FLOAT_NUM_ARR : {
			makefmtstr("fy*|y*in:", funcname, formatstr);

			// Import the parsed parameters. 
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_2, &parampy.f, &datapy2, &datapy3, &ignoreerrors, &arraymaxlen)) {
				ErrMsgParameterError();
				arraydata.error = 5;
				return arraydata;
			}
			arraylength = calcarraylength(arraytype, datapy2.len);
			paramcat = param_num_arr_none;

			break;
		}
		case CAT_DOUBLE_NUM_ARR : {
			makefmtstr("dy*|y*in:", funcname, formatstr);

			// Import the parsed parameters. 
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_2, &parampy.d, &datapy2, &datapy3, &ignoreerrors, &arraymaxlen)) {
				ErrMsgParameterError();
				arraydata.error = 5;
				return arraydata;
			}
			arraylength = calcarraylength(arraytype, datapy2.len);
			paramcat = param_num_arr_none;

			break;
		}
		case CAT_ANY_ARR_ARR : {
			makefmtstr("y*y*|y*in:", funcname, formatstr);

			// Import the parsed parameters. 
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_2, &datapy1, &datapy2, &datapy3, &ignoreerrors, &arraymaxlen)) {
				ErrMsgParameterError();
				arraydata.error = 5;
				return arraydata;
			}

			// Both arrays must be the exact same type. We are of course assuming
			// that the first array determines the required array type.
			if (!arraycompatok(dataobj2, arraytype)) {
				ErrMsgParameterError();
				arraydata.error = 6;
				return arraydata;
			}

			// Both arrays must be the same length. Since they are of the
			// same array type, we can just compare the raw length.
			if (datapy1.len != datapy2.len) {
				ErrMsgArrayLengthErr();
				arraydata.error = 6;
				return arraydata;
			}


			arraylength = calcarraylength(arraytype, datapy1.len);
			paramcat = param_arr_arr_none;

			break;
		}
		default : {
			ErrMsgParameterError();
			arraydata.error = 5;
			return arraydata;
		}
	}


	// Optional checks to be done only if the third array is present.
	if (dataobj3 != NULL) {
		// Check the optional array parameter for compatibilty with the array type
		// of the mandatory parameters.
		if (!arraycompatok(dataobj3, arraytype)) {
			ErrMsgParameterError();
			arraydata.error = 6;
			return arraydata;
		}
		// Array length must match that of other arrays.
		if (arraylength != calcarraylength(arraytype, datapy3.len)) {
			ErrMsgArrayLengthErr();
			arraydata.error = 6;
			return arraydata;
		}
		arraydata.hasoutputarray = 1;

		// Fix up the parameter category to account for the presence of an output array.
		switch (paramcat) {
			case param_arr_num_none : { paramcat = param_arr_num_arr; break; }
			case param_num_arr_none : { paramcat = param_num_arr_arr; break; }
			case param_arr_arr_none : { paramcat = param_arr_arr_arr; break; }
			default : { ErrMsgParameterError(); arraydata.error = 6; return arraydata; break; }
		}
	} else {
		arraydata.hasoutputarray = 0;
	}
	


	arraydata.error = 0;
	arraydata.arraytype = arraytype;
	arraydata.ignoreerrors = ignoreerrors;
	arraydata.arraylength = adjustarraymaxlen(arraylength, arraymaxlen);
	arraydata.array1.buf = datapy1.buf;
	arraydata.array2.buf = datapy2.buf;
	arraydata.array3.buf = datapy3.buf;
	arraydata.pybuffer1 = datapy1;
	arraydata.pybuffer2 = datapy2;
	arraydata.pybuffer3 = datapy3;
	arraydata.param = parampy;
	arraydata.paramcat = paramcat;



	return arraydata;

}


/*--------------------------------------------------------------------------- */
