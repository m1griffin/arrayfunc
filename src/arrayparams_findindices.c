//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_findindices.c
// Purpose:  Common functions for arrayfunc.
// Language: C
// Date:     28-Nov-2017
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
#include "arrayops.h"
#include "arrayparams_findindices.h"

/*--------------------------------------------------------------------------- */

// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist_findindices[] = {"op", "data", "dataout", "param", "maxlen", NULL};

/*--------------------------------------------------------------------------- */

/* Release the buffers which represent the arrays. This function checks if the
 * 	array object was not intiailised.
 * arraydata = Structure which contains the three array buffers to be released.
 * Returns: Nothing.
*/
void releasebuffers_findindices(struct args_params_findindices arraydata) {
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
struct args_params_findindices getparams_findindices(PyObject *self, PyObject *args, PyObject *keywds, char *funcname) {


	// This is used for constructing parameter format strings. The size must
	// be able to hold the largest string, which will be determined by the 
	// names of the functions which use this.
	char formatstr[FMTSTRLEN];
	

	// This is used to return the parsed parameters.
	struct args_params_findindices arraydata = ARGSINIT_FINDINDICES;

	PyObject *dataobj1 = NULL;
	PyObject *dataobj2 = NULL;
	PyObject *param1obj = NULL;
	
	PyObject *opstr = NULL;

	struct paramsdata paramobjdata1, paramobjdata2, paramobjdata3;


	// How long the array is.
	Py_ssize_t arraylength, typedarraylength;

	// The numeric parameter version is available in all possible types.
	struct paramsvals parampy;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;



	// These are used to track the types of each array.
	char arraytype = 0;
	char paramoverflow = 0;
	signed int opcode = 0;

	// Need this to parse the object of the numeric parameter, but
	// otherwise don't need it.
	char param1hasbuffer = 0;



	// -----------------------------------------------------


	// This section determines the type of the arrays. We do this by parsing
	// the parameters as objects. We then examine the parameters 

	// Construct the format string. This is constructed dynamically because
	// we must be able to call this same function from different C extensions.
	makefmtstr("UOOO|n:", funcname, formatstr);

	// Import the raw objects. 
	if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_findindices, &opstr, 
					&dataobj1, &dataobj2, &param1obj, &arraymaxlen)) {
		ErrMsgParameterError();
		arraydata.error = 1;
		return arraydata;
	}

	// Convert the command string to an integer.
	opcode = opstrdecode(opstr);

	// Check if the command string is valid.
	if (opcode < 0) {
		ErrMsgOperatorNotValidforthisFunction();
		arraydata.error = 2;
		// Release the buffers. 
		releasebuffers_findindices(arraydata);
		return arraydata;
	}


	// Parse the second parameter. 
	if (get_paramdata(dataobj1, &paramobjdata1, &arraydata.hasbuffer1, &paramoverflow)) {
		if (paramoverflow) {
			ErrMsgArithOverflowParam();
		} else {
			ErrMsgParameterError();
		}
		arraydata.error = 3;
		releasebuffers_findindices(arraydata);
		return arraydata;
	}


	// The second parameter must be an array.
	if (paramobjdata1.paramtype != paramobj_array) {
		ErrMsgParameterError();
		arraydata.error = 4;
		releasebuffers_findindices(arraydata);
		return arraydata;
	}


	// Get the raw array length.
	arraylength = paramobjdata1.pybuffer.len;
	// Get the array code.
	arraytype = paramobjdata1.arraycode;
	// Adjust arraylength according to array type. This takes into account
	// the different sizes of different data types.
	typedarraylength = calcarraylength(arraytype, arraylength);


	// Parse the third parameter. 
	if (get_paramdata(dataobj2, &paramobjdata2, &arraydata.hasbuffer2, &paramoverflow)) {
		if (paramoverflow) {
			ErrMsgArithOverflowParam();
		} else {
			ErrMsgParameterError();
		}
		arraydata.error = 5;
		releasebuffers_findindices(arraydata);
		return arraydata;
	}


	// The third parameter must be an array.
	if (paramobjdata2.paramtype != paramobj_array) {
		ErrMsgParameterError();
		arraydata.error = 6;
		releasebuffers_findindices(arraydata);
		return arraydata;
	}

	// The array must be of type 'q'.
	if (paramobjdata2.arraycode != 'q') {
		ErrMsgParameterError();
		arraydata.error = 7;
		releasebuffers_findindices(arraydata);
		return arraydata;
	}

	// It must also be of the same typed length as the input array.
	if (calcarraylength('q', paramobjdata2.pybuffer.len) != typedarraylength) {
		ErrMsgArrayLengthMismatch();
		arraydata.error = 8;
		releasebuffers_findindices(arraydata);
		return arraydata;
	}


	// Parse the fourth parameter. 
	if (get_paramdata(param1obj, &paramobjdata3, &param1hasbuffer, &paramoverflow)) {
		if (paramoverflow) {
			ErrMsgArithOverflowParam();
		} else {
			ErrMsgParameterError();
		}
		arraydata.error = 9;
		releasebuffers_findindices(arraydata);
		return arraydata;
	}


	// The numeric parameter must match the array type.
	if (get_numericparams(paramobjdata1.arraycode, &paramobjdata3, &parampy, &paramoverflow)) {
		if (paramoverflow) {
			ErrMsgArithOverflowParam();
		} else {
			ErrMsgParameterError();
		}
		arraydata.error = 10;
		releasebuffers_findindices(arraydata);
		return arraydata;
	}



	arraydata.error = 0;
	arraydata.arraytype = arraytype;
	arraydata.opcode = opcode;
	arraydata.arraylength = adjustarraymaxlen(typedarraylength, arraymaxlen);
	arraydata.array1.buf = paramobjdata1.array.buf;
	arraydata.pybuffer1 = paramobjdata1.pybuffer;
	arraydata.array2.buf = paramobjdata2.array.buf;
	arraydata.pybuffer2 = paramobjdata2.pybuffer;
	arraydata.param = parampy;


	return arraydata;

}


/*--------------------------------------------------------------------------- */

