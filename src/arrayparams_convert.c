//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_convert.c
// Purpose:  Parameter parsing for convert.
// Language: C
// Date:     08-May-2014
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

#include "Python.h"

#include <string.h>
#include <limits.h>

#include "arrayerrs.h"
#include "arrayparams_base.h"
#include "arrayparams_convert.h"

/*--------------------------------------------------------------------------- */

// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist_convert[] = {"data", "dataout", "maxlen", NULL};

/*--------------------------------------------------------------------------- */

/* Release the buffers which represent the arrays. This function checks if the
 * 	array object was not intiailised.
 * arraydata = Structure which contains the array buffers to be released.
 * Returns: Nothing.
*/
void releasebuffers_convert(struct args_params_convert arraydata) {
	if (arraydata.hasbuffer1) {
		PyBuffer_Release(&arraydata.pybuffer1);
		arraydata.hasbuffer1 = 0;
	}

	if (arraydata.hasbuffer2) {
		PyBuffer_Release(&arraydata.pybuffer2);
		arraydata.hasbuffer2 = 0;
	}

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
struct args_params_convert getparams_convert(PyObject *self, PyObject *args, PyObject *keywds, char *funcname) {


	// This is used for constructing parameter format strings. The size must
	// be able to hold the largest string, which will be determined by the 
	// names of the functions which use this.
	char formatstr[FMTSTRLEN];
	

	// This is used to return the parsed parameters.
	struct args_params_convert arraydata = ARGSINIT_CONVERT;

	PyObject *dataobj1 = NULL;
	PyObject *dataobj2 = NULL;

	struct paramsdata paramobjdata1, paramobjdata2;


	// How long the array is.
	Py_ssize_t typedarraylength1, typedarraylength2;


	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;


	// These are used to track the types of each array.
	char paramoverflow = 0;


	// -----------------------------------------------------


	// This section determines the type of the arrays. We do this by parsing
	// the parameters as objects. We then examine the parameters.

	// Construct the format string. This is constructed dynamically because
	// we must be able to call this same function from different C extensions.
	makefmtstr("OO|n:", funcname, formatstr);

	// Import the raw objects. 
	if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_convert,
					&dataobj1, &dataobj2, &arraymaxlen)) {
		ErrMsgParameterError();
		arraydata.error = 1;
		return arraydata;
	}


	// Parse the first parameter. 
	if (get_paramdata(dataobj1, &paramobjdata1, &arraydata.hasbuffer1, &paramoverflow)) {
		if (paramoverflow) {
			ErrMsgArithOverflowParam();
		} else {
			ErrMsgParameterError();
		}
		arraydata.error = 2;
		releasebuffers_convert(arraydata);
		return arraydata;
	}


	// The first parameter must be an array.
	if (paramobjdata1.paramtype != paramobj_array) {
		ErrMsgParameterError();
		arraydata.error = 3;
		releasebuffers_convert(arraydata);
		return arraydata;
	}



	// Parse the second parameter. 
	if (get_paramdata(dataobj2, &paramobjdata2, &arraydata.hasbuffer2, &paramoverflow)) {
		if (paramoverflow) {
			ErrMsgArithOverflowParam();
		} else {
			ErrMsgParameterError();
		}
		arraydata.error = 4;
		releasebuffers_convert(arraydata);
		return arraydata;
	}


	// The second parameter must be an array.
	if (paramobjdata2.paramtype != paramobj_array) {
		ErrMsgParameterError();
		arraydata.error = 5;
		releasebuffers_convert(arraydata);
		return arraydata;
	}



	// Get the raw array length.
	// Adjust array length according to array type. This takes into account
	// the different sizes of different data types.
	typedarraylength1 = calcarraylength(paramobjdata1.arraycode, paramobjdata1.pybuffer.len);

	// The second array.
	typedarraylength2 = calcarraylength(paramobjdata2.arraycode, paramobjdata2.pybuffer.len);


	// Check to make sure the input and output arrays are of equal length.
	if (typedarraylength1 != typedarraylength2) {
		ErrMsgArrayLengthMismatch();
		releasebuffers_convert(arraydata);
		arraydata.error = 6;
		return arraydata;
	}


	arraydata.error = 0;
	arraydata.arraytype1 = paramobjdata1.arraycode;
	arraydata.arraytype2 = paramobjdata2.arraycode;
	arraydata.arraylength = adjustarraymaxlen(typedarraylength1, arraymaxlen);
	arraydata.array1.buf = paramobjdata1.array.buf;
	arraydata.pybuffer1 = paramobjdata1.pybuffer;
	arraydata.array2.buf = paramobjdata2.array.buf;
	arraydata.pybuffer2 = paramobjdata2.pybuffer;


	return arraydata;

}


/*--------------------------------------------------------------------------- */

