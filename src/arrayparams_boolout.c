//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_bool.c
// Purpose:  Common functions for arrayfunc.
// Language: C
// Date:     10-Apr-2018
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
#include "arrayparams_boolout.h"

/*--------------------------------------------------------------------------- */


// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist[] = {"data", "maxlen", NULL};


/*--------------------------------------------------------------------------- */

/* Release the buffers which represent the arrays. This function checks if the
 * 	array object was not intiailised.
 * array1 (Py_buffer) = The array object.
 * Returns: Nothing.
*/
void releasebuffers_boolout(struct args_params_boolout arraydata) {
	if (arraydata.hasbuffer1) {
		PyBuffer_Release(&arraydata.pybuffer1);
		arraydata.hasbuffer1 = 0;
	}
}

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */


/* Get the parameters passed from Python with a function which takes one array.
 * self, args, keywds = The parameters of the same name passed from the PyObject
 * 		function which forms the original entry point.
 * funcname = A string which represents the C extension name. This is passed to
 * 		PyArg_ParseTupleAndKeywords for error reporting.
 * Returns: A structure which contains the parameter data.
*/
struct args_params_boolout getparams_boolout(PyObject *self, PyObject *args, PyObject *keywds, char *funcname) {


	// This is used to return the parsed parameters.
	struct args_params_boolout arraydata = ARGSINIT_BOOLOUT;

	PyObject *dataobj1 = NULL;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;


	char formatstr[FMTSTRLEN];

	// -----------------------------------------------------


	// This section determines the type of the arrays.

	// Construct the format string. This is constructed dynamically because
	// we must be able to call this same function from different C extensions.
	makefmtstr("O|n:", funcname, formatstr);

	// Import the raw objects. 
	if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist, &dataobj1, 
							&arraymaxlen)) {
		ErrMsgParameterError();
		arraydata.error = 1;
		return arraydata;
	}


	// Find the array type code.
	arraydata.arraytype = lookuparraycode(dataobj1);
	if (!arraydata.arraytype) {
		ErrMsgParameterError();
		arraydata.error = 2;
		return arraydata;
	}



	// -----------------------------------------------------


	// This section extracts the actual arrays.

	// Construct the format string. This is constructed dynamically because
	// we must be able to call this same function from different C extensions.
	makefmtstr("y*|n:", funcname, formatstr);

	// Since all the parameters are either arrays or known data types, we
	// can parse all the different parameter types with one format string.
	if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist, 
			&arraydata.pybuffer1, &arraymaxlen)) {
		arraydata.error = 4;
		return arraydata;
	}


	// Assign the buffer to a union which lets us get at them as typed data.
	arraydata.array1.buf = arraydata.pybuffer1.buf;
	arraydata.hasbuffer1 = 1;


	// The length of the data array.
	arraydata.arraylength = calcarraylength(arraydata.arraytype, arraydata.pybuffer1.len);
	if (arraydata.arraylength < 1) {
		// Release the buffers. 
		releasebuffers_boolout(arraydata);
		ErrMsgArrayLengthErr();
		arraydata.error = 5;
		return arraydata;
	}


	// Adjust the length of array being operated on, if necessary.
	arraydata.arraylength = adjustarraymaxlen(arraydata.arraylength, arraymaxlen);


	return arraydata;

}


/*--------------------------------------------------------------------------- */

