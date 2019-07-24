//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_compress.c
// Purpose:  Parameter parsing for dropwhile, takewhile, afilter.
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
#include "arrayparams_compress.h"

/*--------------------------------------------------------------------------- */

// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist_compress[] = {"data", "dataout", "selector", "maxlen", NULL};

/*--------------------------------------------------------------------------- */

/* Release the buffers which represent the arrays. This function checks if the
 * 	array object was not intiailised.
 * arraydata = Structure which contains the three array buffers to be released.
 * Returns: Nothing.
*/
void releasebuffers_compress(struct args_params_compress arraydata) {
	if (arraydata.hasbuffer1) {
		PyBuffer_Release(&arraydata.pybuffer1);
		arraydata.hasbuffer1 = 0;
	}

	if (arraydata.hasbuffer2) {
		PyBuffer_Release(&arraydata.pybuffer2);
		arraydata.hasbuffer2 = 0;
	}

	if (arraydata.hasbuffer3) {
		PyBuffer_Release(&arraydata.pybuffer3);
		arraydata.hasbuffer3 = 0;
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
struct args_params_compress getparams_compress(PyObject *self, PyObject *args, PyObject *keywds, char *funcname) {


	// This is used for constructing parameter format strings. The size must
	// be able to hold the largest string, which will be determined by the 
	// names of the functions which use this.
	char formatstr[FMTSTRLEN];
	

	// This is used to return the parsed parameters.
	struct args_params_compress arraydata = ARGSINIT_COMPRESS;

	PyObject *dataobj1 = NULL;
	PyObject *dataobj2 = NULL;
	PyObject *dataobj3 = NULL;

	struct paramsdata paramobjdata1, paramobjdata2, paramobjdata3;


	// How long the array is.
	Py_ssize_t typedarraylength1, typedarraylength2, typedarraylength3;


	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;


	// These are used to track the types of each array.
	char arraytype = 0;
	char paramoverflow = 0;


	// -----------------------------------------------------


	// This section determines the type of the arrays. We do this by parsing
	// the parameters as objects. We then examine the parameters.

	// Construct the format string. This is constructed dynamically because
	// we must be able to call this same function from different C extensions.
	makefmtstr("OOO|n:", funcname, formatstr);

	// Import the raw objects. 
	if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_compress,
					&dataobj1, &dataobj2, &dataobj3, &arraymaxlen)) {
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
		releasebuffers_compress(arraydata);
		return arraydata;
	}


	// The first parameter must be an array.
	if (paramobjdata1.paramtype != paramobj_array) {
		ErrMsgParameterError();
		arraydata.error = 3;
		releasebuffers_compress(arraydata);
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
		releasebuffers_compress(arraydata);
		return arraydata;
	}


	// The second parameter must be an array.
	if (paramobjdata2.paramtype != paramobj_array) {
		ErrMsgParameterError();
		arraydata.error = 5;
		releasebuffers_compress(arraydata);
		return arraydata;
	}


	// Parse the third parameter. 
	if (get_paramdata(dataobj3, &paramobjdata3, &arraydata.hasbuffer3, &paramoverflow)) {
		if (paramoverflow) {
			ErrMsgArithOverflowParam();
		} else {
			ErrMsgParameterError();
		}
		arraydata.error = 6;
		releasebuffers_compress(arraydata);
		return arraydata;
	}


	// The second third must be an array.
	if (paramobjdata3.paramtype != paramobj_array) {
		ErrMsgParameterError();
		arraydata.error = 7;
		releasebuffers_compress(arraydata);
		return arraydata;
	}


	// All arrays must be the same type.
	if ((paramobjdata1.arraycode != paramobjdata2.arraycode) || 
			(paramobjdata1.arraycode != paramobjdata2.arraycode)) {
		ErrMsgArrayTypeMismatch();
		arraydata.error = 8;
		releasebuffers_compress(arraydata);
		return arraydata;
	}

	// Get the array code.
	arraytype = paramobjdata1.arraycode;


	// Get the raw array length.
	// Adjust array length according to array type. This takes into account
	// the different sizes of different data types.
	typedarraylength1 = calcarraylength(arraytype, paramobjdata1.pybuffer.len);

	// Arrays are permitted to be of different lengths.
	typedarraylength2 = calcarraylength(arraytype, paramobjdata2.pybuffer.len);
	typedarraylength3 = calcarraylength(arraytype, paramobjdata3.pybuffer.len);


	arraydata.error = 0;
	arraydata.arraytype = arraytype;
	arraydata.arraylength1 = adjustarraymaxlen(typedarraylength1, arraymaxlen);
	arraydata.arraylength2 = typedarraylength2;
	arraydata.arraylength3 = typedarraylength3;
	arraydata.array1.buf = paramobjdata1.array.buf;
	arraydata.pybuffer1 = paramobjdata1.pybuffer;
	arraydata.array2.buf = paramobjdata2.array.buf;
	arraydata.pybuffer2 = paramobjdata2.pybuffer;
	arraydata.array3.buf = paramobjdata3.array.buf;
	arraydata.pybuffer3 = paramobjdata3.pybuffer;


	return arraydata;

}


/*--------------------------------------------------------------------------- */

