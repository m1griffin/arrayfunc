//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_asum.c
// Purpose:  Common functions for arrayfunc.
// Language: C
// Date:     10-Apr-2018
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
#include "arrayparams_asum.h"

/*--------------------------------------------------------------------------- */


// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist[] = {"data", "matherrors", "maxlen", "nosimd", NULL};


/*--------------------------------------------------------------------------- */

/* Release the buffers which represent the arrays. This function checks if the
 * 	array object was not intiailised.
 * array1 (Py_buffer) = The array object.
 * Returns: Nothing.
*/
void releasebuffers_asum(struct args_params_asum arraydata) {
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
struct args_params_asum getparams_asum(PyObject *self, PyObject *args, PyObject *keywds, char *funcname) {


	// This is used to return the parsed parameters.
	struct args_params_asum arraydata = ARGSINIT_ASUM;

	PyObject *dataobj1 = NULL;

	struct paramsdata paramobjdata1;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;
	Py_ssize_t arraylength, typedarraylength;

	// If true, *disabled* overflow checking.
	unsigned int ignoreerrors = 0;

	// If True, SIMD processing is disabled.
	int nosimd = 0;

	// This is used to track the types of each array.
	char arraytype = 0;

	char formatstr[FMTSTRLEN];

	// -----------------------------------------------------


	// This section determines the type of the arrays.

	// Construct the format string. This is constructed dynamically because
	// we must be able to call this same function from different C extensions.
	makefmtstr("O|ini:", funcname, formatstr);

	// Import the raw objects. 
	if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist, &dataobj1, 
							&ignoreerrors, &arraymaxlen, &nosimd)) {
		ErrMsgParameterError();
		arraydata.error = 1;
		return arraydata;
	}

	// Parse the first object parameter. 
	if (get_paramdata_simple(dataobj1, &paramobjdata1, &arraydata.hasbuffer1)) {
		ErrMsgParameterError();
		arraydata.error = 2;
		releasebuffers_asum(arraydata);
		return arraydata;
	}


	// The first parameter must be an array.
	if (paramobjdata1.paramtype != paramobj_array) {
		ErrMsgParameterError();
		arraydata.error = 3;
		releasebuffers_asum(arraydata);
		return arraydata;
	}

	// The array type.
	arraytype = paramobjdata1.arraycode;

	// Get the raw array length.
	arraylength = paramobjdata1.pybuffer.len;


	// Adjust arraylength according to array type. This takes into account
	// the different sizes of different data types.
	typedarraylength = calcarraylength(arraytype, arraylength);


	arraydata.nosimd = nosimd;

	// Collect the parameter data for return to the calling function.
	arraydata.error = 0;
	arraydata.arraytype = arraytype;
	arraydata.ignoreerrors = ignoreerrors;
	arraydata.nosimd = nosimd;
	arraydata.arraylength = adjustarraymaxlen(typedarraylength, arraymaxlen);
	arraydata.array1.buf = paramobjdata1.array.buf;
	arraydata.pybuffer1 = paramobjdata1.pybuffer;


	return arraydata;

}


/*--------------------------------------------------------------------------- */

