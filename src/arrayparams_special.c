//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_special.c
// Purpose:  Common functions for arrayfunc.
// Language: C
// Date:     25-Jan-2018
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
#include "arrayparams_special.h"



/*--------------------------------------------------------------------------- */

// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist[] = {"data", "exp", "dataout", "matherrors", "maxlen", NULL};


/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

/* Release the buffers which represent the arrays. This function checks if the
 * 	array object was not intiailised.
 * pybuffer1 (Py_buffer) = The first array object.
 * pybuffer2 (Py_buffer) = The second array object.
 * Returns: Nothing.
*/

void releasebuffers_twobuff(Py_buffer pybuffer1, Py_buffer pybuffer2, char hasoutputarray) {
	PyBuffer_Release(&pybuffer1);

	if (hasoutputarray) {
		PyBuffer_Release(&pybuffer2);
	}
}

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
struct args_params_ldexp getparams_ldexp(PyObject *self, PyObject *args, PyObject *keywds) {

	// This is used to return the parsed parameters.
	struct args_params_ldexp arraydata = ARGSINIT_SPECIAL;

	PyObject *dataobj1 = NULL;
	PyObject *dataobj2 = NULL;


	// The length of the data array.
	Py_ssize_t databufflength;
	

	// How long the array is.
	Py_ssize_t arraylength;
	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;



	// -----------------------------------------------------
	// Import the raw objects. 
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "OL|Oin:ldexp", kwlist, &dataobj1, 
							&arraydata.exp, &dataobj2, &arraydata.ignoreerrors, &arraymaxlen)) {
		arraydata.error = 1;
		return arraydata;
	}


	// The first parameter must be an array.
	if (!isarrayobjtype(dataobj1)) {
		ErrMsgParameterError();
		arraydata.error = 1;
		return arraydata;
	}


	// Find the array code.
	arraydata.arraytype = lookuparraycode(dataobj1);
	// This must be float or double.
	if (!(isfloatarraycode(arraydata.arraytype) || isdoublearraycode(arraydata.arraytype))) {
		ErrMsgParameterError();
		arraydata.error = 2;
		return arraydata;
	}


	// Now check if there is an output array.
	if (dataobj2) {
		// This must also be an array.
		if (!isarrayobjtype(dataobj2)) {
			ErrMsgParameterError();
			arraydata.error = 3;
			return arraydata;
		}
		// This must be of the same type as the input array.
		if (lookuparraycode(dataobj2) != arraydata.arraytype) {
			ErrMsgArrayTypeMismatch();
			arraydata.error = 3;
			return arraydata;
		}
		// There is a second array present.
		arraydata.hassecondarray = 1;
	} else {
		arraydata.hassecondarray = 0;
	}


	// -----------------------------------------------------


	// Now parse fully to get the array data.
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "y*L|y*in:ldexp", kwlist, &arraydata.pybuffer1, 
							&arraydata.exp, &arraydata.pybuffer2, &arraydata.ignoreerrors, &arraymaxlen)) {
		arraydata.error = 4;
		return arraydata;
	}


	// The length of the data array.
	databufflength = arraydata.pybuffer1.len;
	arraylength = calcarraylength(arraydata.arraytype, databufflength);
	if (arraylength < 1) {
		// Release the buffers. 
		releasebuffers_twobuff(arraydata.pybuffer1, arraydata.pybuffer2, arraydata.hassecondarray);
		ErrMsgArrayLengthErr();
		arraydata.error = 5;
		return arraydata;
	}


	// If we have an output array, then we need to make sure its size matches
	// that of the input array.
	if (arraydata.hassecondarray) {
		// Check to make sure the input and output arrays are of equal length.
		if (databufflength != arraydata.pybuffer2.len) {
			// Release the buffers. 
			releasebuffers_twobuff(arraydata.pybuffer1, arraydata.pybuffer2, arraydata.hassecondarray);
			ErrMsgArrayLengthMismatch();
			arraydata.error = 6;
			return arraydata;
		}
	}


	// Adjust the length of array being operated on, if necessary.
	arraydata.arraylength = adjustarraymaxlen(arraylength, arraymaxlen);

	// Assign the buffer to a union which lets us get at them as typed data.
	arraydata.array1.buf = arraydata.pybuffer1.buf;
	arraydata.array2.buf = arraydata.pybuffer2.buf;


	return arraydata;

}
/*--------------------------------------------------------------------------- */
