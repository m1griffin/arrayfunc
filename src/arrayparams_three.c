//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_three.c
// Purpose:  Functions for parsing parameters for functions which take three params.
// Language: C
// Date:     29-Nov-2018
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
#include "arrayparams_three.h"


/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist_3wmath[] = {"data1", "data2", "data3", "dataout", "matherrors", "maxlen", NULL};


/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

/* Release the buffers which represent the arrays. This function checks if the
 * 	array object was initialised before releasing it.
 * arraydata = Structure which contains the three array buffers to be released.
 * Returns: Nothing.
*/
void releasebuffers_three(struct args_params_3 arraydata) {

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

	if (arraydata.hasbuffer4) {
		PyBuffer_Release(&arraydata.pybuffer4);
		arraydata.hasbuffer4 = 0;
	}

}

/*--------------------------------------------------------------------------- */



/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

/* Get the parameters passed from Python with a function which takes three 
 * 		input arrays or numeric parameters, plus an optional output array.
 * self, args, keywds = The parameters of the same name passed from the PyObject
 * 		function which forms the original entry point.
 * funcname = A string which represents the C extension name. This is passed to
 * 		PyArg_ParseTupleAndKeywords for error reporting.
 * Returns: A structure which contains the parameter data.
*/
struct args_params_3 getparams_three(PyObject *self, PyObject *args, PyObject *keywds, char *funcname) {


	// This is used for constructing parameter format strings. The size must
	// be able to hold the largest string, which will be determined by the 
	// names of the functions which use this.
	char formatstr[FMTSTRLEN];
	

	// This is used to return the parsed parameters.
	struct args_params_3 arraydata = ARGSINIT_THREE;

	PyObject *dataobj1 = NULL;
	PyObject *dataobj2 = NULL;
	PyObject *dataobj3 = NULL;
	PyObject *dataobj4 = NULL;


	struct paramsdata paramobjdata1, paramobjdata2, paramobjdata3, paramobjdata4;


	// How long the array is.
	Py_ssize_t arraylength, typedarraylength;

	// The numeric parameter version is available in all possible types.
	struct paramsvals parampy2, parampy3;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	// If true, *disabled* overflow checking.
	unsigned int ignoreerrors = 0;


	// This is used to track the types of each array.
	char arraytype = 0;


	// The category of the parameters. That is, what type (array, number, none)
	// of each parameter. 
	enum paramcats paramcat;


	// -----------------------------------------------------


	// This section determines the type of the arrays. We do this by parsing
	// the parameters as objects. 

	// Construct the format string. This is constructed dynamically because
	// we must be able to call this same function from different C extensions.
	makefmtstr("OOO|Oin:", funcname, formatstr);

	// Import the raw objects. 
	if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_3wmath, &dataobj1, 
							&dataobj2, &dataobj3, &dataobj4, &ignoreerrors, &arraymaxlen)) {
		ErrMsgParameterError();
		arraydata.error = 2;
		return arraydata;
	}


	// Parse the first object parameter. 
	if (get_paramdata_simple(dataobj1, &paramobjdata1, &arraydata.hasbuffer1)) {
		ErrMsgParameterError();
		arraydata.error = 3;
		releasebuffers_three(arraydata);
		return arraydata;
	}

	// Parse the second object parameter. 
	if (get_paramdata_simple(dataobj2, &paramobjdata2, &arraydata.hasbuffer2)) {
		ErrMsgParameterError();
		arraydata.error = 4;
		releasebuffers_three(arraydata);
		return arraydata;
	}

	// Parse the third object parameter. 
	if (get_paramdata_simple(dataobj3, &paramobjdata3, &arraydata.hasbuffer3)) {
		ErrMsgParameterError();
		arraydata.error = 5;
		releasebuffers_three(arraydata);
		return arraydata;
	}


	// The first parameter must always be an array.
	if (paramobjdata1.paramtype != paramobj_array) {
		ErrMsgParameterError();
		arraydata.error = 6;
		releasebuffers_three(arraydata);
		return arraydata;
	} else {
		arraytype = paramobjdata1.arraycode;
		// Get the raw array length.
		arraylength = paramobjdata1.pybuffer.len;
	}


	// If the second parameter is an array, it must be of the same type.
	if (paramobjdata2.paramtype == paramobj_array) {
		if (paramobjdata1.arraycode != paramobjdata2.arraycode) {
			ErrMsgParameterError();
			arraydata.error = 7;
			releasebuffers_three(arraydata);
			return arraydata;
		}
	
		// And also the same length.
		if (paramobjdata1.pybuffer.len != paramobjdata2.pybuffer.len) {
			ErrMsgParameterError();
			arraydata.error = 8;
			releasebuffers_three(arraydata);
			return arraydata;
		}

		// This keeps track of the pattern of parameters.
		// This is a preliminary assignment, as we don't know the 
		// next parameter yet.
		paramcat = param_arr_arr_arr_none;

	} else {

		// As this is not an array, it should be a number.
		if (get_numericparams_simple(paramobjdata1.arraycode, &paramobjdata2, &parampy2)) {
			ErrMsgParameterError();
			arraydata.error = 9;
			releasebuffers_three(arraydata);
			return arraydata;
		}
		paramcat = param_arr_num_arr_none;
	}


	// If the third parameter is an array, it must be of the same type.
	if (paramobjdata3.paramtype == paramobj_array) {
		if (paramobjdata1.arraycode != paramobjdata3.arraycode) {
			ErrMsgParameterError();
			arraydata.error = 10;
			releasebuffers_three(arraydata);
			return arraydata;
		}
	
		// And also the same length.
		if (paramobjdata1.pybuffer.len != paramobjdata3.pybuffer.len) {
			ErrMsgParameterError();
			arraydata.error = 11;
			releasebuffers_three(arraydata);
			return arraydata;
		}

	} else {
		// As this is not an array, it should be a number.
		if (get_numericparams_simple(paramobjdata1.arraycode, &paramobjdata3, &parampy3)) {
			ErrMsgParameterError();
			arraydata.error = 12;
			releasebuffers_three(arraydata);
			return arraydata;
		}

		// This keeps track of the pattern of parameters.
		if (paramcat == param_arr_num_arr_none) {
			paramcat = param_arr_num_num_none;
		} else {
			paramcat = param_arr_arr_num_none;
		}
	}



	// Parse the fourth object parameter. This one is optional.
	if (dataobj4 != NULL) {
		if (get_paramdata_simple(dataobj4, &paramobjdata4, &arraydata.hasbuffer4)) {
			ErrMsgParameterError();
			arraydata.error = 13;
			releasebuffers_three(arraydata);
			return arraydata;
		}
	
		// If the fourth parameter is present, it must be an array.
		if (paramobjdata4.paramtype != paramobj_array) {
			ErrMsgParameterError();
			arraydata.error = 14;
			releasebuffers_three(arraydata);
			return arraydata;
		}

		// The array codes must match the other parameters.
		if (paramobjdata1.arraycode != paramobjdata4.arraycode) {
			ErrMsgParameterError();
			arraydata.error = 15;
			releasebuffers_three(arraydata);
			return arraydata;
		}

		arraydata.hasoutputarray = 1;

		
		// The length must match the other arrays.
		if (paramobjdata4.pybuffer.len != arraylength) {
			ErrMsgParameterError();
			arraydata.error = 16;
			releasebuffers_three(arraydata);
			return arraydata;
		}

		// If there was an optional output array, adjust the parameter category to suit.
		if (paramcat == param_arr_num_num_none) { paramcat = param_arr_num_num_arr; }
		if (paramcat == param_arr_arr_num_none) { paramcat = param_arr_arr_num_arr; }
		if (paramcat == param_arr_num_arr_none) { paramcat = param_arr_num_arr_arr; }
		if (paramcat == param_arr_arr_arr_none) { paramcat = param_arr_arr_arr_arr; }

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
	arraydata.array3.buf = paramobjdata3.array.buf;
	arraydata.array4.buf = paramobjdata4.array.buf;
	arraydata.pybuffer1 = paramobjdata1.pybuffer;
	arraydata.pybuffer2 = paramobjdata2.pybuffer;
	arraydata.pybuffer3 = paramobjdata3.pybuffer;
	arraydata.pybuffer4 = paramobjdata4.pybuffer;
	arraydata.param2 = parampy2;
	arraydata.param3 = parampy3;
	arraydata.paramcat = paramcat;


	return arraydata;

}
