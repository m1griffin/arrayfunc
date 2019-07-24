//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayfunc.c
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
#include "arrayparams_two.h"


/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 

// This version is for versions which support the "matherrors" parameter.
static char *kwlist_2wmath[] = {"data1", "data2", "dataout", "matherrors", "maxlen", NULL};

// This version does not support "matherrors".
static char *kwlist_2womath[] = {"data1", "data2", "dataout", "maxlen", NULL};

// This version is for versions which support the "nosimd" but not "matherrors" parameter.
static char *kwlist_2wsimdwomath[] = {"data1", "data2", "dataout", "maxlen", "nosimd", NULL};

// This version is for versions which support both the "nosimd" and "matherrors" parameter.
static char *kwlist_2wsimdwmath[] = {"data1", "data2", "dataout", "matherrors", "maxlen", "nosimd", NULL};

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

/* Release the buffers which represent the arrays. This function checks if the
 * 	array object was initialised before releasing it.
 * arraydata = Structure which contains the three array buffers to be released.
 * Returns: Nothing.
*/
void releasebuffers_two(struct args_params_2 arraydata) {

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



/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

/* Get the parameters passed from Python with a function which takes one input 
 * 		array and one input value, or two input arrays, plus an optional
 * 		output array.
 * self, args, keywds = The parameters of the same name passed from the PyObject
 * 		function which forms the original entry point.
 * matherrors = If zero, the "matherrors" keyword argument is not present. If
 * 		non-zero, the "matherrors" keyword argument is available.
 * hasnosimd = If zero, the "hasnosimd" keyword argument is not present. If
 * 		non-zero, the "hasnosimd" keyword argument is available.
 * funcname = A string which represents the C extension name. This is passed to
 * 		PyArg_ParseTupleAndKeywords for error reporting.
 * Returns: A structure which contains the parameter data.
*/
struct args_params_2 getparams_two(PyObject *self, PyObject *args, PyObject *keywds, char matherrors, char hasnosimd, char *funcname) {


	// This is used for constructing parameter format strings. The size must
	// be able to hold the largest string, which will be determined by the 
	// names of the functions which use this.
	char formatstr[FMTSTRLEN];
	

	// This is used to return the parsed parameters.
	struct args_params_2 arraydata = ARGSINIT_TWO;

	PyObject *dataobj1 = NULL;
	PyObject *dataobj2 = NULL;
	PyObject *dataobj3 = NULL;


	struct paramsdata paramobjdata1, paramobjdata2, paramobjdata3;


	// How long the array is.
	Py_ssize_t arraylength, typedarraylength;

	// The numeric parameter version is available in all possible types.
	struct paramsvals parampy;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	// If true, *disabled* overflow checking.
	unsigned int ignoreerrors = 0;
	// If True, SIMD processing is disabled.
	int nosimd = 0;


	// This is used to track the types of each array.
	char arraytype = 0;


	// The category of the parameters. That is, what type (array, number, none)
	// of each parameter. 
	enum paramcats paramcat;


	// -----------------------------------------------------


	// This section determines the type of the arrays. We do this by parsing
	// the parameters as objects. 

	// This supports two styles of functions. One allows the "matherrors" 
	// keyword parameter, while the other does not.
	if (matherrors) {
		if (hasnosimd) {
			// Construct the format string. This is constructed dynamically because
			// we must be able to call this same function from different C extensions.
			makefmtstr("OO|Oini:", funcname, formatstr);

			// Import the raw objects. 
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_2wsimdwmath, &dataobj1, 
									&dataobj2, &dataobj3, &ignoreerrors, &arraymaxlen, &nosimd)) {
				ErrMsgParameterError();
				arraydata.error = 2;
				return arraydata;
			}
		} else {
			// Construct the format string. This is constructed dynamically because
			// we must be able to call this same function from different C extensions.
			makefmtstr("OO|Oin:", funcname, formatstr);

			// Import the raw objects. 
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_2wmath, &dataobj1, 
									&dataobj2, &dataobj3, &ignoreerrors, &arraymaxlen)) {
				ErrMsgParameterError();
				arraydata.error = 2;
				return arraydata;
			}
		}
	} else {
		if (hasnosimd) {
			// Construct the format string. This is constructed dynamically because
			// we must be able to call this same function from different C extensions.
			makefmtstr("OO|Oni:", funcname, formatstr);

			// Import the raw objects. 
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_2wsimdwomath, &dataobj1, 
									&dataobj2, &dataobj3, &arraymaxlen, &nosimd)) {
				ErrMsgParameterError();
				arraydata.error = 2;
				return arraydata;
			}
		} else {
			// Construct the format string. This is constructed dynamically because
			// we must be able to call this same function from different C extensions.
			makefmtstr("OO|On:", funcname, formatstr);

			// Import the raw objects. 
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_2womath, &dataobj1, 
									&dataobj2, &dataobj3, &arraymaxlen)) {
				ErrMsgParameterError();
				arraydata.error = 2;
				return arraydata;
			}
		}
	}


	// Parse the first object parameter. 
	if (get_paramdata_simple(dataobj1, &paramobjdata1, &arraydata.hasbuffer1)) {
		ErrMsgParameterError();
		arraydata.error = 3;
		releasebuffers_two(arraydata);
		return arraydata;
	}

	// Parse the second object parameter. 
	if (get_paramdata_simple(dataobj2, &paramobjdata2, &arraydata.hasbuffer2)) {
		ErrMsgParameterError();
		arraydata.error = 4;
		releasebuffers_two(arraydata);
		return arraydata;
	}



	// Either the first or second parameter (or both) must be an array.
	if ((paramobjdata1.paramtype != paramobj_array) && (paramobjdata2.paramtype != paramobj_array)) {
		ErrMsgParameterError();
		arraydata.error = 5;
		releasebuffers_two(arraydata);
		return arraydata;
	}

	// If both the first and second parameters are arrays, they must be of the same type.
	if ((paramobjdata1.paramtype == paramobj_array) && (paramobjdata2.paramtype == paramobj_array)) {
		if (paramobjdata1.arraycode != paramobjdata2.arraycode) {
			ErrMsgParameterError();
			arraydata.error = 6;
			releasebuffers_two(arraydata);
			return arraydata;
		}
	
		// And also the same length.
		if (paramobjdata1.pybuffer.len != paramobjdata2.pybuffer.len) {
			ErrMsgParameterError();
			arraydata.error = 7;
			releasebuffers_two(arraydata);
			return arraydata;
		}

		// This keeps track of the pattern of parameters.
		paramcat = param_arr_arr_none;
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


	// Parse the third object parameter. This one is optional.
	if (dataobj3 != NULL) {
		if (get_paramdata_simple(dataobj3, &paramobjdata3, &arraydata.hasbuffer3)) {
			ErrMsgParameterError();
			arraydata.error = 8;
			releasebuffers_two(arraydata);
			return arraydata;
		}
	
		// If the third parameter is present, it must be an array.
		if (paramobjdata3.paramtype != paramobj_array) {
			ErrMsgParameterError();
			arraydata.error = 9;
			releasebuffers_two(arraydata);
			return arraydata;
		}

		// The array codes must match the other parameters.
		if ((paramobjdata1.paramtype == paramobj_array) && 
				(paramobjdata1.arraycode != paramobjdata3.arraycode)) {
			ErrMsgParameterError();
			arraydata.error = 10;
			releasebuffers_two(arraydata);
			return arraydata;
		}

		if ((paramobjdata2.paramtype == paramobj_array) && 
				(paramobjdata2.arraycode != paramobjdata3.arraycode)) {
			ErrMsgParameterError();
			arraydata.error = 11;
			releasebuffers_two(arraydata);
			return arraydata;
		}

		arraydata.hasoutputarray = 1;

		
		// The length must match the other arrays.
		if (paramobjdata3.pybuffer.len != arraylength) {
			ErrMsgParameterError();
			arraydata.error = 12;
			releasebuffers_two(arraydata);
			return arraydata;
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
			releasebuffers_two(arraydata);
			return arraydata;
		}

		arraytype = paramobjdata1.arraycode;
		// This keeps track of the pattern of parameters.
		paramcat = param_arr_num_none;
	}


	// The second parameter is an array and the first is not.
	if ((paramobjdata1.paramtype != paramobj_array) && (paramobjdata2.paramtype == paramobj_array)) {

		if (get_numericparams_simple(paramobjdata2.arraycode, &paramobjdata1, &parampy)) {
			ErrMsgParameterError();
			arraydata.error = 14;
			releasebuffers_two(arraydata);
			return arraydata;
		}

		arraytype = paramobjdata2.arraycode;
		// This keeps track of the pattern of parameters.
		paramcat = param_num_arr_none;
	}


	// If there was a third array, adjust the parameter category to suit.
	if (arraydata.hasoutputarray) {
		if (paramcat == param_arr_num_none) { paramcat = param_arr_num_arr; }
		if (paramcat == param_num_arr_none) { paramcat = param_num_arr_arr; }
		if (paramcat == param_arr_arr_none) { paramcat = param_arr_arr_arr; }
	}

	// Adjust arraylength according to array type. This takes into account
	// the different sizes of different data types.
	typedarraylength = calcarraylength(arraytype, arraylength);

	// Collect the parameter data for return to the calling function.
	arraydata.error = 0;
	arraydata.arraytype = arraytype;
	arraydata.ignoreerrors = ignoreerrors;
	arraydata.nosimd = nosimd;
	arraydata.arraylength = adjustarraymaxlen(typedarraylength, arraymaxlen);
	arraydata.array1.buf = paramobjdata1.array.buf;
	arraydata.array2.buf = paramobjdata2.array.buf;
	arraydata.array3.buf = paramobjdata3.array.buf;
	arraydata.pybuffer1 = paramobjdata1.pybuffer;
	arraydata.pybuffer2 = paramobjdata2.pybuffer;
	arraydata.pybuffer3 = paramobjdata3.pybuffer;
	arraydata.param = parampy;
	arraydata.paramcat = paramcat;


	return arraydata;

}
