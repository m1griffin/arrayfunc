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

// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist_comp[] = {"data1", "data2", "maxlen", "nosimd", NULL};

/*--------------------------------------------------------------------------- */

/* Release the buffers which represent the arrays. This function checks if the
 * 	array object was not intiailised.
 * arraydata = Structure which contains the three array buffers to be released.
 * Returns: Nothing.
*/
void releasebuffers_comp(struct args_params_comp arraydata) {
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
struct args_params_comp getparams_comp(PyObject *self, PyObject *args, PyObject *keywds, char *funcname) {


	// This is used for constructing parameter format strings. The size must
	// be able to hold the largest string, which will be determined by the 
	// names of the functions which use this.
	char formatstr[FMTSTRLEN];
	

	// This is used to return the parsed parameters.
	struct args_params_comp arraydata = ARGSINIT_COMP;

	PyObject *dataobj1 = NULL;
	PyObject *dataobj2 = NULL;

	struct paramsdata paramobjdata1, paramobjdata2;


	// How long the array is.
	Py_ssize_t arraylength, typedarraylength;

	// The numeric parameter version is available in all possible types.
	struct paramsvals parampy;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;
	// If True, SIMD processing is disabled.
	int nosimd = 0;


	// These are used to track the types of each array.
	char arraytype = 0;


	// The category of the parameters. That is, what type (array, number, none)
	// of each parameter. 
	enum paramcats paramcat;


	// -----------------------------------------------------


	// This section determines the type of the arrays. We do this by parsing
	// the parameters as objects. We then examine the parameters 

	// Construct the format string. This is constructed dynamically because
	// we must be able to call this same function from different C extensions.
	makefmtstr("OO|ni:", funcname, formatstr);

	// Import the raw objects. 
	if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_comp, &dataobj1, 
							&dataobj2, &arraymaxlen, &nosimd)) {
		ErrMsgParameterError();
		arraydata.error = 2;
		return arraydata;
	}


	// Parse the first object parameter. 
	if (get_paramdata_simple(dataobj1, &paramobjdata1, &arraydata.hasbuffer1)) {
		ErrMsgParameterError();
		arraydata.error = 3;
		releasebuffers_comp(arraydata);
		return arraydata;
	}

	// Parse the second object parameter. 
	if (get_paramdata_simple(dataobj2, &paramobjdata2, &arraydata.hasbuffer2)) {
		ErrMsgParameterError();
		arraydata.error = 4;
		releasebuffers_comp(arraydata);
		return arraydata;
	}


	// Either the first or second parameter (or both) must be an array.
	if ((paramobjdata1.paramtype != paramobj_array) && (paramobjdata2.paramtype != paramobj_array)) {
		ErrMsgParameterError();
		arraydata.error = 5;
		releasebuffers_comp(arraydata);
		return arraydata;
	}


	// If both the first and second parameters are arrays, they must be of the same type.
	if ((paramobjdata1.paramtype == paramobj_array) && (paramobjdata2.paramtype == paramobj_array)) {
		if (paramobjdata1.arraycode != paramobjdata2.arraycode) {
			ErrMsgParameterError();
			arraydata.error = 6;
			releasebuffers_comp(arraydata);
			return arraydata;
		}
	
		// And also the same length.
		if (paramobjdata1.pybuffer.len != paramobjdata2.pybuffer.len) {
			ErrMsgParameterError();
			arraydata.error = 7;
			releasebuffers_comp(arraydata);
			return arraydata;
		}

		// This keeps track of the pattern of parameters.
		paramcat = param_arr_arr;
		arraytype = paramobjdata1.arraycode;

	}


	// Get the raw array length.
	if (paramobjdata1.paramtype == paramobj_array) {
		arraylength = paramobjdata1.pybuffer.len;
	} else {
		if (paramobjdata2.paramtype == paramobj_array) {
		arraylength = paramobjdata2.pybuffer.len;
		}
	}




	// At this point we have checked if the parameters are present, and if all
	// arrays match with respect to their array codes.
	// After this we need to check the numeric parameters and whether they are
	// compatible with the arrays.


	// The first parameter is an array and the second is not.
	if ((paramobjdata1.paramtype == paramobj_array) && (paramobjdata2.paramtype != paramobj_array)) {

		if (get_numericparams_simple(paramobjdata1.arraycode, &paramobjdata2, &parampy)) {
			ErrMsgParameterError();
			arraydata.error = 13;
			releasebuffers_comp(arraydata);
			return arraydata;
		}

		arraytype = paramobjdata1.arraycode;
		// This keeps track of the pattern of parameters.
		paramcat = param_arr_num;
	}


	// The second parameter is an array and the first is not.
	if ((paramobjdata1.paramtype != paramobj_array) && (paramobjdata2.paramtype == paramobj_array)) {

		if (get_numericparams_simple(paramobjdata2.arraycode, &paramobjdata1, &parampy)) {
			ErrMsgParameterError();
			arraydata.error = 14;
			releasebuffers_comp(arraydata);
			return arraydata;
		}

		arraytype = paramobjdata2.arraycode;
		// This keeps track of the pattern of parameters.
		paramcat = param_num_arr;
	}


	// Adjust arraylength according to array type. This takes into account
	// the different sizes of different data types.
	typedarraylength = calcarraylength(arraytype, arraylength);


	arraydata.error = 0;
	arraydata.arraytype = arraytype;
	arraydata.arraylength = adjustarraymaxlen(typedarraylength, arraymaxlen);
	arraydata.nosimd = nosimd;
	arraydata.array1.buf = paramobjdata1.array.buf;
	arraydata.array2.buf = paramobjdata2.array.buf;
	arraydata.pybuffer1 = paramobjdata1.pybuffer;
	arraydata.pybuffer2 = paramobjdata2.pybuffer;
	arraydata.param = parampy;
	arraydata.paramcat = paramcat;


	return arraydata;

}


/*--------------------------------------------------------------------------- */

