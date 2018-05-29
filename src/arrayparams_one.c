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
static char *kwlist_1[] = {"data", "dataout", "matherrors", "maxlen", NULL};


/*--------------------------------------------------------------------------- */

/* Release the buffers which represent the arrays. This function checks if the
 * 	array object was not intiailised.
 * array1 (Py_buffer) = The first array object.
 * array2 (Py_buffer) = The second array object.
 * Returns: Nothing.
*/
void releasebuffers_one(struct args_params_1 arraydata) {
	if (!(&arraydata.pybuffer1 == NULL)) {
		PyBuffer_Release(&arraydata.pybuffer1);
	}

	if (!(&arraydata.pybuffer2 == NULL)) {
		PyBuffer_Release(&arraydata.pybuffer1);
	}
}

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */


/* Get the parameters passed from Python with a function which takes one or
 * 		optionally, two arrays.
 * self, args, keywds = The parameters of the same name passed from the PyObject
 * 		function which forms the original entry point.
 * funcname = A string which represents the C extension name. This is passed to
 * 		PyArg_ParseTupleAndKeywords for error reporting.
 * Returns: A structure which contains the parameter data.
*/
struct args_params_1 getparams_one(PyObject *self, PyObject *args, PyObject *keywds, char *funcname) {


	// This is used to return the parsed parameters.
	struct args_params_1 arraydata = ARGSINIT_ONE;

	PyObject *dataobj1 = NULL;
	PyObject *dataobj2 = NULL;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	// If true, *disabled* overflow checking.
	unsigned int ignoreerrors = 0;

	// The second array type code, this is optional.
	char array2code = 0;

	char formatstr[FMTSTRLEN];

	// -----------------------------------------------------


	// This section determines the type of the arrays.

	// Construct the format string. This is constructed dynamically because
	// we must be able to call this same function from different C extensions.
	makefmtstr("O|Oin:", funcname, formatstr);

	// Import the raw objects. 
	if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_1, &dataobj1, 
							&dataobj2, &ignoreerrors, &arraymaxlen)) {
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


	// The second array is optional. If present, it must match the first type code.
	if (dataobj2) {
		array2code = lookuparraycode(dataobj2);
		if (arraydata.arraytype != array2code) {
			ErrMsgArrayTypeMismatch();
			arraydata.error = 3;
			return arraydata;
		}
		// There is a second array present.
		arraydata.hassecondarray = 1;
	}


	// -----------------------------------------------------


	// This section extracts the actual arrays.

	// Construct the format string. This is constructed dynamically because
	// we must be able to call this same function from different C extensions.
	makefmtstr("y*|y*in:", funcname, formatstr);

	// Since all the parameters are either arrays or known data types, we
	// can parse all the different parameter types with one format string.
	if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_1, 
			&arraydata.pybuffer1, &arraydata.pybuffer2, &arraydata.ignoreerrors, &arraymaxlen)) {
		arraydata.error = 4;
		return arraydata;
	}


	// Assign the buffer to a union which lets us get at them as typed data.
	arraydata.array1.buf = arraydata.pybuffer1.buf;


	// The length of the data array.
	arraydata.arraylength = calcarraylength(arraydata.arraytype, arraydata.pybuffer1.len);
	if (arraydata.arraylength < 1) {
		// Release the buffers. 
		releasebuffers_one(arraydata);
		ErrMsgArrayLengthErr();
		arraydata.error = 5;
		return arraydata;
	}

	// Check to make sure the input and output arrays are of equal length.
	// However, the second array is optional.
	if (arraydata.hassecondarray) {
		arraydata.array2.buf = arraydata.pybuffer2.buf;
		if (arraydata.pybuffer2.len != arraydata.pybuffer1.len) {
			// Release the buffers. 
			releasebuffers_one(arraydata);
			ErrMsgArrayLengthMismatch();
			arraydata.error = 6;
			return arraydata;
		}
	} 

	// Adjust the length of array being operated on, if necessary.
	arraydata.arraylength = adjustarraymaxlen(arraydata.arraylength, arraymaxlen);


	return arraydata;

}


/*--------------------------------------------------------------------------- */

