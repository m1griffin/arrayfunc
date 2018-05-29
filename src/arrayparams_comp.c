//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_comp.c
// Purpose:  Common functions for arrayfunc.
// Language: C
// Date:     28-Nov-2017
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

#include "Python.h"

#include <string.h>
#include <limits.h>

#include "arrayerrs.h"
#include "arrayparams_base.h"
#include "arrayparams_comp.h"


/*--------------------------------------------------------------------------- */


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
static char *kwlist_comp[] = {"data1", "data2", "maxlen", NULL};

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
void releasebuffers_comp(struct args_params_comp arraydata) {
	if (!(&arraydata.pybuffer1 == NULL)) {
		PyBuffer_Release(&arraydata.pybuffer1);
	}

	if (!(&arraydata.pybuffer2 == NULL)) {
		PyBuffer_Release(&arraydata.pybuffer2);
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
struct args_params_comp getparams_comp(PyObject *self, PyObject *args, PyObject *keywds, char *funcname) {


	// This is used for constructing parameter format strings. The size must
	// be able to hold the largest string, which will be determined by the 
	// names of the functions which use this.
	char formatstr[FMTSTRLEN];
	

	// This is used to return the parsed parameters.
	struct args_params_comp arraydata = ARGSINIT_COMP;

	PyObject *dataobj1 = NULL;
	PyObject *dataobj2 = NULL;

	// The input buffers are arrays of bytes.
	Py_buffer datapy1 = {NULL};
	Py_buffer datapy2 = {NULL};


	// How long the array is.
	Py_ssize_t arraylength;

	// The numeric parameter version is available in all possible types.
	struct paramsvals parampy;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;


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
	makefmtstr("OO|n:", funcname, formatstr);

	// Import the raw objects. 
	if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_comp, &dataobj1, 
							&dataobj2, &arraymaxlen)) {
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
				makefmtstr("y*L|n:", funcname, formatstr);

				// Import the parsed parameters. 
				if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_comp, &datapy1, &paramtmp_q, &arraymaxlen)) {
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
						makefmtstr("y*k|n:", funcname, formatstr);

						// Import the parsed parameters. 
						if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_comp, &datapy1, &parampy.L, &arraymaxlen)) {
							ErrMsgParameterError();
							arraydata.error = 5;
							return arraydata;
						}
						break;

					}
					case 'Q':{
						makefmtstr("y*K|n:", funcname, formatstr);

						// Import the parsed parameters. 
						if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_comp, &datapy1, &parampy.Q, &arraymaxlen)) {
							ErrMsgParameterError();
							arraydata.error = 5;
							return arraydata;
						}
						break;
					}
					case 'q':{
						makefmtstr("y*L|n:", funcname, formatstr);

						// Import the parsed parameters. 
						if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_comp, &datapy1, &parampy.q, &arraymaxlen)) {
							ErrMsgParameterError();
							arraydata.error = 5;
							return arraydata;
						}
						break;
					}
				}
			}

			arraylength = calcarraylength(arraytype, datapy1.len);
			paramcat = param_arr_num;


			break;
		}
		case CAT_FLOAT_ARR_NUM : {
			makefmtstr("y*f|n:", funcname, formatstr);

			// Import the parsed parameters. 
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_comp, &datapy1, &parampy.f, &arraymaxlen)) {
				ErrMsgParameterError();
				arraydata.error = 5;
				return arraydata;
			}
			arraylength = calcarraylength(arraytype, datapy1.len);
			paramcat = param_arr_num;

			break;
		}
		case CAT_DOUBLE_ARR_NUM : {
			makefmtstr("y*d|n:", funcname, formatstr);

			// Import the parsed parameters. 
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_comp, &datapy1, &parampy.d, &arraymaxlen)) {
				ErrMsgParameterError();
				arraydata.error = 5;
				return arraydata;
			}
			arraylength = calcarraylength(arraytype, datapy1.len);
			paramcat = param_arr_num;

			break;
		}
		case CAT_INT_NUM_ARR : {
			if (ischeckedintcode(arraytype)) {
				// Unsigned integer number parameters types have to be checked
				// manually, so we check almost all integers this way. For 
				// parameter format strings, "L" is for a signed long long int.
				makefmtstr("Ly*|n:", funcname, formatstr);

				// Import the parsed parameters. 
				if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_comp, &paramtmp_q, &datapy2, &arraymaxlen)) {
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
						makefmtstr("ky*|n:", funcname, formatstr);

						// Import the parsed parameters. 
						if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_comp, &parampy.L, &datapy2, &arraymaxlen)) {
							ErrMsgParameterError();
							arraydata.error = 5;
							return arraydata;
						}
						break;

					}
					case 'Q':{
						makefmtstr("Ky*|n:", funcname, formatstr);

						// Import the parsed parameters. 
						if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_comp, &parampy.Q, &datapy2, &arraymaxlen)) {
							ErrMsgParameterError();
							arraydata.error = 5;
							return arraydata;
						}
						break;
					}
					case 'q':{
						makefmtstr("Ly*|n:", funcname, formatstr);

						// Import the parsed parameters. 
						if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_comp, &parampy.q, &datapy2, &arraymaxlen)) {
							ErrMsgParameterError();
							arraydata.error = 5;
							return arraydata;
						}
						break;
					}
				}
			}

			arraylength = calcarraylength(arraytype, datapy2.len);
			paramcat = param_num_arr;

			break;
		}
		case CAT_FLOAT_NUM_ARR : {
			makefmtstr("fy*|n:", funcname, formatstr);

			// Import the parsed parameters. 
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_comp, &parampy.f, &datapy2, &arraymaxlen)) {
				ErrMsgParameterError();
				arraydata.error = 5;
				return arraydata;
			}
			arraylength = calcarraylength(arraytype, datapy2.len);
			paramcat = param_num_arr;

			break;
		}
		case CAT_DOUBLE_NUM_ARR : {
			makefmtstr("dy*|n:", funcname, formatstr);

			// Import the parsed parameters. 
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_comp, &parampy.d, &datapy2, &arraymaxlen)) {
				ErrMsgParameterError();
				arraydata.error = 5;
				return arraydata;
			}
			arraylength = calcarraylength(arraytype, datapy2.len);
			paramcat = param_num_arr;

			break;
		}
		case CAT_ANY_ARR_ARR : {
			makefmtstr("y*y*|n:", funcname, formatstr);

			// Import the parsed parameters. 
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_comp, &datapy1, &datapy2, &arraymaxlen)) {
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
			paramcat = param_arr_arr;

			break;
		}
		default : {
			ErrMsgParameterError();
			arraydata.error = 5;
			return arraydata;
		}
	}



	arraydata.error = 0;
	arraydata.arraytype = arraytype;
	arraydata.arraylength = adjustarraymaxlen(arraylength, arraymaxlen);
	arraydata.array1.buf = datapy1.buf;
	arraydata.array2.buf = datapy2.buf;
	arraydata.pybuffer1 = datapy1;
	arraydata.pybuffer2 = datapy2;
	arraydata.param = parampy;
	arraydata.paramcat = paramcat;



	return arraydata;

}


/*--------------------------------------------------------------------------- */
