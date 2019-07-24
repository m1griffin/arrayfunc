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
#include "arrayparams_one.h"


/*--------------------------------------------------------------------------- */


// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 

// This version is for versions which support the "matherrors" parameter.
static char *kwlist_1wmath[] = {"data", "dataout", "matherrors", "maxlen", NULL};

// This version does not support "matherrors".
static char *kwlist_1womath[] = {"data", "dataout", "maxlen", NULL};


/*--------------------------------------------------------------------------- */

/* Release the buffers which represent the arrays. This function checks if the
 * 	array object was not intiailised.
 * array1 (Py_buffer) = The first array object.
 * array2 (Py_buffer) = The second array object.
 * Returns: Nothing.
*/
void releasebuffers_one(struct args_params_1 arraydata) {
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

/*--------------------------------------------------------------------------- */


/* Get the parameters passed from Python with a function which takes one or
 * 		optionally, two arrays.
 * self, args, keywds = The parameters of the same name passed from the PyObject
 * 		function which forms the original entry point.
 * matherrors = If zero, the "matherrors" keyword argument is not present. If
 * 		non-zero, the "matherrors" keyword argument is available.
 * funcname = A string which represents the C extension name. This is passed to
 * 		PyArg_ParseTupleAndKeywords for error reporting.
 * Returns: A structure which contains the parameter data.
*/
struct args_params_1 getparams_one(PyObject *self, PyObject *args, PyObject *keywds, char matherrors, char *funcname) {


	// This is used to return the parsed parameters.
	struct args_params_1 arraydata = ARGSINIT_ONE;

	PyObject *dataobj1 = NULL;
	PyObject *dataobj2 = NULL;

	struct paramsdata paramobjdata1, paramobjdata2;

	// How long the array is.
	Py_ssize_t arraylength, typedarraylength;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	// If true, *disabled* overflow checking.
	unsigned int ignoreerrors = 0;

	// This is used to track the types of each array.
	char arraytype = 0;

	char formatstr[FMTSTRLEN];

	// -----------------------------------------------------


	// This section determines the type of the arrays.

	// Construct the format string. This is constructed dynamically because
	// we must be able to call this same function from different C extensions.

	// This supports two styles of functions. One allows the "matherrors" 
	// keyword parameter, while the other does not.
	if (matherrors) {
		makefmtstr("O|Oin:", funcname, formatstr);

		// Import the raw objects. 
		if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_1wmath, &dataobj1, 
								&dataobj2, &ignoreerrors, &arraymaxlen)) {
			ErrMsgParameterError();
			arraydata.error = 1;
			return arraydata;
		}
	} else {
		// Construct the format string. This is constructed dynamically because
		// we must be able to call this same function from different C extensions.
		makefmtstr("O|On:", funcname, formatstr);

		// Import the raw objects. 
		if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_1womath, &dataobj1, 
								&dataobj2, &arraymaxlen)) {
			ErrMsgParameterError();
			arraydata.error = 1;
			return arraydata;
		}
	}



	// Parse the first object parameter. 
	if (get_paramdata_simple(dataobj1, &paramobjdata1, &arraydata.hasbuffer1)) {
		ErrMsgParameterError();
		arraydata.error = 2;
		releasebuffers_one(arraydata);
		return arraydata;
	}


	// The first parameter must be an array.
	if (paramobjdata1.paramtype != paramobj_array) {
		ErrMsgParameterError();
		arraydata.error = 3;
		releasebuffers_one(arraydata);
		return arraydata;
	}

	// The array type.
	arraytype = paramobjdata1.arraycode;

	// Get the raw array length.
	arraylength = paramobjdata1.pybuffer.len;

	// Parse the second object parameter. This one is optional.
	if (dataobj2 != NULL) {
		if (get_paramdata_simple(dataobj2, &paramobjdata2, &arraydata.hasbuffer2)) {
			ErrMsgParameterError();
			arraydata.error = 4;
			releasebuffers_one(arraydata);
			return arraydata;
		}
	
		// If the second parameter is present, it must be an array.
		if (paramobjdata2.paramtype != paramobj_array) {
			ErrMsgParameterError();
			arraydata.error = 5;
			releasebuffers_one(arraydata);
			return arraydata;
		}

		// The array codes must match the other parameters.
		if (paramobjdata1.arraycode != paramobjdata2.arraycode) {
			ErrMsgParameterError();
			arraydata.error = 6;
			releasebuffers_one(arraydata);
			return arraydata;
		}

		arraydata.hasoutputarray = 1;

		// The length must match the other arrays.
		if (paramobjdata2.pybuffer.len != arraylength) {
			ErrMsgParameterError();
			arraydata.error = 7;
			releasebuffers_one(arraydata);
			return arraydata;
		}

	}


	// Adjust arraylength according to array type. This takes into account
	// the different sizes of different data types.
	typedarraylength = calcarraylength(arraytype, arraylength);


	// Collect the parameter data for return to the calling function.
	arraydata.error = 0;
	arraydata.arraytype = arraytype;
	arraydata.ignoreerrors = ignoreerrors;
	arraydata.arraylength = adjustarraymaxlen(typedarraylength, arraymaxlen);
	arraydata.array1.buf = paramobjdata1.array.buf;
	arraydata.array2.buf = paramobjdata2.array.buf;
	arraydata.pybuffer1 = paramobjdata1.pybuffer;
	arraydata.pybuffer2 = paramobjdata2.pybuffer;


	return arraydata;


}


/*--------------------------------------------------------------------------- */

