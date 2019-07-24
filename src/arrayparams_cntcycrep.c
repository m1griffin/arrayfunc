//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_cntcycrep.c
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
#include "arrayparams_cntcycrep.h"


/*--------------------------------------------------------------------------- */


// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 

// This version is for "repeat".
static char *kwlist_repeat[] = {"data", "value", NULL};

// This version is for "count".
static char *kwlist_count[] = {"data", "start", "step", NULL};

// This version is for "cycle".
static char *kwlist_cycle[] = {"data", "start", "stop", "step", NULL};

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* Release the buffers which represent the arrays. This function checks if the
 * 	array object was not intiailised.
 * array1 (Py_buffer) = The first array object.
 * array2 (Py_buffer) = The second array object.
 * Returns: Nothing.
*/
void releasebuffers_cntcycrep(struct args_params_cntcycrep arraydata) {
	if (arraydata.hasbuffer1) {
		PyBuffer_Release(&arraydata.pybuffer1);
		arraydata.hasbuffer1 = 0;
	}
}

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* For the "step" parameter for count, look up the correct array type
 * code to use with the actual array type. Step must be a signed value even
 * with unsigned integer arrays because a negative step indicates counting 
 * down.
 * step = The actual array type.
 * Returns: The array code to use when extracting the parameter and checking
 *          for overflow.
*/
char stepcodelookup(char step) {
	switch(step) {
		case 'b' : { return 'b'; break; }
		case 'B' : { return 'b'; break; }
		case 'h' : { return 'h'; break; }
		case 'H' : { return 'h'; break; }
		case 'i' : { return 'i'; break; }
		case 'I' : { return 'i'; break; }
		case 'l' : { return 'l'; break; }
		case 'L' : { return 'l'; break; }
		case 'q' : { return 'q'; break; }
		case 'Q' : { return 'q'; break; }
		case 'f' : { return 'f'; break; }
		case 'd' : { return 'd'; break; }
		// We don't know this code.
		default: { return 0; break; }
	}

}

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* Get the parameters passed from Python with a function which takes one array
 * 		 and one numeric parameter.
 * self, args, keywds = The parameters of the same name passed from the PyObject
 * 		function which forms the original entry point.
 * funcname = A string which represents the C extension name. This is passed to
 * 		PyArg_ParseTupleAndKeywords for error reporting.
 * Returns: A structure which contains the parameter data.
*/
struct args_params_cntcycrep getparams_repeat(PyObject *self, PyObject *args, PyObject *keywds, char *funcname) {


	// This is used to return the parsed parameters.
	struct args_params_cntcycrep arraydata = ARGSINIT_CNTCYCREP;

	PyObject *dataobj1 = NULL;
	PyObject *dataobj2 = NULL;

	struct paramsdata paramobjdata1, paramobjdata2;

	// The numeric parameter version is available in all possible types.
	struct paramsvals parampy;

	// How long the array is.
	Py_ssize_t arraylength, typedarraylength;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	// Check if the parameter overflowed.
	char paramoverflow = 0;
	char param1hasbuffer = 0;

	// This is used to track the types of each array.
	char arraytype = 0;

	char formatstr[FMTSTRLEN];

	// -----------------------------------------------------


	// This section determines the type of the arrays.

	// Construct the format string. This is constructed dynamically because
	// we must be able to call this same function from different C extensions.

	makefmtstr("OO:", funcname, formatstr);

	// Import the raw objects. 
	if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_repeat, &dataobj1, 
							&dataobj2)) {
		ErrMsgParameterError();
		arraydata.error = 1;
		return arraydata;
	}


	// Parse the first object parameter. 
	if (get_paramdata_simple(dataobj1, &paramobjdata1, &arraydata.hasbuffer1)) {
		ErrMsgParameterError();
		arraydata.error = 2;
		releasebuffers_cntcycrep(arraydata);
		return arraydata;
	}


	// The first parameter must be an array.
	if (paramobjdata1.paramtype != paramobj_array) {
		ErrMsgParameterError();
		arraydata.error = 3;
		releasebuffers_cntcycrep(arraydata);
		return arraydata;
	}

	// The array type.
	arraytype = paramobjdata1.arraycode;

	// Get the raw array length.
	arraylength = paramobjdata1.pybuffer.len;


	// Parse the second parameter. 
	if (get_paramdata(dataobj2, &paramobjdata2, &param1hasbuffer, &paramoverflow)) {
		if (paramoverflow) {
			ErrMsgArithOverflowParam();
		} else {
			ErrMsgParameterError();
		}
		arraydata.error = 4;
		releasebuffers_cntcycrep(arraydata);
		return arraydata;
	}

	// The numeric parameter must match the array type.
	if (get_numericparams(paramobjdata1.arraycode, &paramobjdata2, &parampy, &paramoverflow)) {
		if (paramoverflow) {
			ErrMsgArithOverflowParam();
		} else {
			ErrMsgParameterError();
		}
		arraydata.error = 5;
		releasebuffers_cntcycrep(arraydata);
		return arraydata;
	}



	// Adjust arraylength according to array type. This takes into account
	// the different sizes of different data types.
	typedarraylength = calcarraylength(arraytype, arraylength);


	// Collect the parameter data for return to the calling function.
	arraydata.error = 0;
	arraydata.arraytype = arraytype;
	arraydata.arraylength = adjustarraymaxlen(typedarraylength, arraymaxlen);
	arraydata.array1.buf = paramobjdata1.array.buf;
	arraydata.pybuffer1 = paramobjdata1.pybuffer;
	arraydata.param1 = parampy;


	return arraydata;


}


/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* Get the parameters passed from Python with a function which takes one array
 * 		 and two numeric parameters.
 * self, args, keywds = The parameters of the same name passed from the PyObject
 * 		function which forms the original entry point.
 * funcname = A string which represents the C extension name. This is passed to
 * 		PyArg_ParseTupleAndKeywords for error reporting.
 * Returns: A structure which contains the parameter data.
*/
struct args_params_cntcycrep getparams_count(PyObject *self, PyObject *args, PyObject *keywds, char *funcname) {


	// This is used to return the parsed parameters.
	struct args_params_cntcycrep arraydata = ARGSINIT_CNTCYCREP;

	PyObject *dataobj1 = NULL;
	PyObject *dataobj2 = NULL;
	PyObject *dataobj3 = NULL;

	struct paramsdata paramobjdata1, paramobjdata2, paramobjdata3;

	// The numeric parameter version is available in all possible types.
	struct paramsvals parampy1;
	struct paramsvals parampy2;

	// How long the array is.
	Py_ssize_t arraylength, typedarraylength;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	// Check if the parameter overflowed.
	char paramoverflow = 0;
	char param1hasbuffer = 0;
	char param2hasbuffer = 0;

	// This is used to track the types of each array.
	char arraytype = 0;
	// The step parameter must be a signed value.
	char steptype = 0;

	char formatstr[FMTSTRLEN];

	// -----------------------------------------------------


	// This section determines the type of the arrays.

	// Construct the format string. This is constructed dynamically because
	// we must be able to call this same function from different C extensions.

	makefmtstr("OO|O:", funcname, formatstr);

	// Import the raw objects. 
	if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_count, &dataobj1, 
							&dataobj2, &dataobj3)) {
		ErrMsgParameterError();
		arraydata.error = 1;
		return arraydata;
	}


	// Parse the first object parameter. 
	if (get_paramdata_simple(dataobj1, &paramobjdata1, &arraydata.hasbuffer1)) {
		ErrMsgParameterError();
		arraydata.error = 2;
		releasebuffers_cntcycrep(arraydata);
		return arraydata;
	}


	// The first parameter must be an array.
	if (paramobjdata1.paramtype != paramobj_array) {
		ErrMsgParameterError();
		arraydata.error = 3;
		releasebuffers_cntcycrep(arraydata);
		return arraydata;
	}

	// The array type.
	arraytype = paramobjdata1.arraycode;

	// Get the raw array length.
	arraylength = paramobjdata1.pybuffer.len;


	// Parse the second parameter. 
	if (get_paramdata(dataobj2, &paramobjdata2, &param1hasbuffer, &paramoverflow)) {
		if (paramoverflow) {
			ErrMsgArithOverflowParam();
		} else {
			ErrMsgParameterError();
		}
		arraydata.error = 4;
		releasebuffers_cntcycrep(arraydata);
		return arraydata;
	}

	// The numeric parameter must match the array type.
	if (get_numericparams(paramobjdata1.arraycode, &paramobjdata2, &parampy1, &paramoverflow)) {
		if (paramoverflow) {
			ErrMsgArithOverflowParam();
		} else {
			ErrMsgParameterError();
		}
		arraydata.error = 5;
		releasebuffers_cntcycrep(arraydata);
		return arraydata;
	}


	// Parse the third object parameter. This one is optional.
	if (dataobj3 != NULL) {
		if (get_paramdata(dataobj3, &paramobjdata3, &param2hasbuffer, &paramoverflow)) {
			if (paramoverflow) {
				ErrMsgArithOverflowParam();
			} else {
				ErrMsgParameterError();
			}
			arraydata.error = 6;
			releasebuffers_cntcycrep(arraydata);
			return arraydata;
		}

		// The "step" parameter may be slightly different from the array type.
		steptype = stepcodelookup(paramobjdata1.arraycode);

		// The numeric parameter depends on the (modified) array type.
		if (get_numericparams(steptype, &paramobjdata3, &parampy2, &paramoverflow)) {
			if (paramoverflow) {
				ErrMsgArithOverflowParam();
			} else {
				ErrMsgParameterError();
			}
			arraydata.error = 7;
			releasebuffers_cntcycrep(arraydata);
			return arraydata;
		}
	
		arraydata.hasparam2 = 1;
	} else {
		// The optional parameter has not been used.
		arraydata.hasparam2 = 0;
	}

	// Adjust arraylength according to array type. This takes into account
	// the different sizes of different data types.
	typedarraylength = calcarraylength(arraytype, arraylength);


	// Collect the parameter data for return to the calling function.
	arraydata.error = 0;
	arraydata.arraytype = arraytype;
	arraydata.arraylength = adjustarraymaxlen(typedarraylength, arraymaxlen);
	arraydata.array1.buf = paramobjdata1.array.buf;
	arraydata.pybuffer1 = paramobjdata1.pybuffer;
	arraydata.param1 = parampy1;
	arraydata.param2 = parampy2;


	return arraydata;


}


/*--------------------------------------------------------------------------- */



/*--------------------------------------------------------------------------- */
/* Get the parameters passed from Python with a function which takes one array
 * 		 and three numeric parameters.
 * self, args, keywds = The parameters of the same name passed from the PyObject
 * 		function which forms the original entry point.
 * funcname = A string which represents the C extension name. This is passed to
 * 		PyArg_ParseTupleAndKeywords for error reporting.
 * Returns: A structure which contains the parameter data.
*/
struct args_params_cntcycrep getparams_cycle(PyObject *self, PyObject *args, PyObject *keywds, char *funcname) {


	// This is used to return the parsed parameters.
	struct args_params_cntcycrep arraydata = ARGSINIT_CNTCYCREP;

	PyObject *dataobj1 = NULL;
	PyObject *dataobj2 = NULL;
	PyObject *dataobj3 = NULL;
	PyObject *dataobj4 = NULL;

	struct paramsdata paramobjdata1, paramobjdata2, paramobjdata3, paramobjdata4;

	// The numeric parameter version is available in all possible types.
	struct paramsvals parampy1;
	struct paramsvals parampy2;
	struct paramsvals parampy3;

	// How long the array is.
	Py_ssize_t arraylength, typedarraylength;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	// Check if the parameter overflowed.
	char paramoverflow = 0;
	char param1hasbuffer = 0;
	char param2hasbuffer = 0;
	char param3hasbuffer = 0;

	// This is used to track the types of each array.
	char arraytype = 0;

	char formatstr[FMTSTRLEN];

	// -----------------------------------------------------


	// This section determines the type of the arrays.

	// Construct the format string. This is constructed dynamically because
	// we must be able to call this same function from different C extensions.

	makefmtstr("OOO|O:", funcname, formatstr);

	// Import the raw objects. 
	if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist_cycle, &dataobj1, 
							&dataobj2, &dataobj3, &dataobj4)) {
		ErrMsgParameterError();
		arraydata.error = 1;
		return arraydata;
	}


	// Parse the first object parameter. 
	if (get_paramdata_simple(dataobj1, &paramobjdata1, &arraydata.hasbuffer1)) {
		ErrMsgParameterError();
		arraydata.error = 2;
		releasebuffers_cntcycrep(arraydata);
		return arraydata;
	}


	// The first parameter must be an array.
	if (paramobjdata1.paramtype != paramobj_array) {
		ErrMsgParameterError();
		arraydata.error = 3;
		releasebuffers_cntcycrep(arraydata);
		return arraydata;
	}

	// The array type.
	arraytype = paramobjdata1.arraycode;

	// Get the raw array length.
	arraylength = paramobjdata1.pybuffer.len;


	// Parse the second parameter. 
	if (get_paramdata(dataobj2, &paramobjdata2, &param1hasbuffer, &paramoverflow)) {
		if (paramoverflow) {
			ErrMsgArithOverflowParam();
		} else {
			ErrMsgParameterError();
		}
		arraydata.error = 4;
		releasebuffers_cntcycrep(arraydata);
		return arraydata;
	}

	// The numeric parameter must match the array type.
	if (get_numericparams(paramobjdata1.arraycode, &paramobjdata2, &parampy1, &paramoverflow)) {
		if (paramoverflow) {
			ErrMsgArithOverflowParam();
		} else {
			ErrMsgParameterError();
		}
		arraydata.error = 5;
		releasebuffers_cntcycrep(arraydata);
		return arraydata;
	}


	// Parse the third parameter. 
	if (get_paramdata(dataobj3, &paramobjdata3, &param2hasbuffer, &paramoverflow)) {
		if (paramoverflow) {
			ErrMsgArithOverflowParam();
		} else {
			ErrMsgParameterError();
		}
		arraydata.error = 6;
		releasebuffers_cntcycrep(arraydata);
		return arraydata;
	}

	// The numeric parameter must match the array type.
	if (get_numericparams(paramobjdata1.arraycode, &paramobjdata3, &parampy2, &paramoverflow)) {
		if (paramoverflow) {
			ErrMsgArithOverflowParam();
		} else {
			ErrMsgParameterError();
		}
		arraydata.error = 7;
		releasebuffers_cntcycrep(arraydata);
		return arraydata;
	}

	// Parse the fourth object parameter. This one is optional.
	if (dataobj4 != NULL) {
		if (get_paramdata(dataobj4, &paramobjdata4, &param3hasbuffer, &paramoverflow)) {
			if (paramoverflow) {
				ErrMsgArithOverflowParam();
			} else {
				ErrMsgParameterError();
			}
			arraydata.error = 8;
			releasebuffers_cntcycrep(arraydata);
			return arraydata;
		}


		// The numeric parameter must match the array type.
		if (get_numericparams(paramobjdata1.arraycode, &paramobjdata4, &parampy3, &paramoverflow)) {
			if (paramoverflow) {
				ErrMsgArithOverflowParam();
			} else {
				ErrMsgParameterError();
			}
			arraydata.error = 9;
			releasebuffers_cntcycrep(arraydata);
			return arraydata;
		}

		arraydata.hasparam3 = 1;
	} else {
		// The optional parameter has not been used.
		arraydata.hasparam3 = 0;
	}


	// Adjust arraylength according to array type. This takes into account
	// the different sizes of different data types.
	typedarraylength = calcarraylength(arraytype, arraylength);


	// Collect the parameter data for return to the calling function.
	arraydata.error = 0;
	arraydata.arraytype = arraytype;
	arraydata.arraylength = adjustarraymaxlen(typedarraylength, arraymaxlen);
	arraydata.array1.buf = paramobjdata1.array.buf;
	arraydata.pybuffer1 = paramobjdata1.pybuffer;
	arraydata.param1 = parampy1;
	arraydata.param2 = parampy2;
	arraydata.param3 = parampy3;


	return arraydata;


}


/*--------------------------------------------------------------------------- */

