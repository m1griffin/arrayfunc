//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_allany.c
// Purpose:  Common functions for arrayfunc.
// Language: C
// Date:     28-May-2018
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
#include "arrayops.h"

#include "arrayparams_allany.h"


/*--------------------------------------------------------------------------- */

// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist[] = {"op", "data", "param", "maxlen", "nosimd", NULL};

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

/* Release the buffers which represent the arrays. This function checks if the
 * 	array object was not intiailised.
 * array1 (Py_buffer) = The array object.
 * Returns: Nothing.
*/
void releasebuffers_allany(struct args_params_allany arraydata) {
	if (!(&arraydata.pybuffer1 == NULL)) {
		PyBuffer_Release(&arraydata.pybuffer1);
	}
}

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */


/* Get the parameters passed from Python for functions aall or aany.
 * self, args, keywds = The parameters of the same name passed from the PyObject
 * 		function which forms the original entry point.
 * funcname = A string which represents the C extension name. This is passed to
 * 		PyArg_ParseTupleAndKeywords for error reporting.
 * Returns: A structure which contains the parameter data.
*/
struct args_params_allany getparams_allany(PyObject *self, PyObject *args, PyObject *keywds, char *funcname) {


	// This is used to return the parsed parameters.
	struct args_params_allany arraydata = ARGSINIT_ALLANY;

	char formatstr[FMTSTRLEN];

	// -----------------------------------------------------


	PyObject *dataobj1, *param1obj, *opstr;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	char param1type, itemcode;

	unsigned int nosimd = 0;

	// -----------------------------------------------------

	// Construct the format string. This is constructed dynamically because
	// we must be able to call this same function from different C extensions.
	makefmtstr("UOO|ni:", funcname, formatstr);


	/* Import the raw objects. */
	if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist, 
			&opstr, &dataobj1, &param1obj, &arraymaxlen, &nosimd)) {
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


	// Get the parameter type codes.
	param1type = paramtypecode(param1obj);


	// -----------------------------------------------------


	// Check if the array and parameter types are compatible.
	if (!paramcompatok(argtypes.array1type, param1type)) {
		ErrMsgArrayAndParamMismatch();
		arraydata.error = 3;
		return arraydata;
	}


	itemcode = argtypes.array1type;



	// Now we will fetch the actual data depending on the array type.
	switch (itemcode) {
		// signed char
		case 'b' : {
			makefmtstr("Uy*l|ni:", funcname, formatstr);
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist, 
					&opstr, &arraydata.pybuffer1, &param1tmp_l, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(issignedcharrange(param1tmp_l))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			} else {
				param1py.b = (signed char) param1tmp_l;
			}
			break;
		}
		// unsigned char
		case 'B' : {
			makefmtstr("Uy*l|ni:", funcname, formatstr);
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist, 
					&opstr, &arraydata.pybuffer1, &param1tmp_l, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isunsignedcharrange(param1tmp_l))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			} else {
				param1py.B = (unsigned char) param1tmp_l;
			}
			break;
		}
		// signed short
		case 'h' : {
			makefmtstr("Uy*h|ni:", funcname, formatstr);
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist, 
					&opstr, &arraydata.pybuffer1, &param1py.h, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			break;
		}
		// unsigned short
		case 'H' : {
			makefmtstr("Uy*l|ni:", funcname, formatstr);
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist, 
					&opstr, &arraydata.pybuffer1, &param1tmp_l, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isunsignedshortrange(param1tmp_l))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			} else {
				param1py.H = (unsigned short) param1tmp_l;
			}
			break;
		}
		// signed int
		case 'i' : {
			makefmtstr("Uy*i|ni:", funcname, formatstr);
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist, 
					&opstr, &arraydata.pybuffer1, &param1py.i, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			break;
		}
		// unsigned int
		case 'I' : {
			// With architectures where signed long is larger than unsigned int, we
			// can use the larger signed value to test for overflow. If they are the
			// same size, then we cannot check for overflow.
			if (sizeof(signed long) > sizeof(unsigned int)) {
				makefmtstr("Uy*l|ni:", funcname, formatstr);
				// The format string and parameter names depend on the expected data types.
				if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist, 
						&opstr, &arraydata.pybuffer1, &param1tmp_l, &arraymaxlen, &nosimd)) {
					return NULL;
				}
				// Check the data range manually.
				if (!(isunsignedintrange(param1tmp_l))) {
					PyBuffer_Release(&datapy);
					ErrMsgArithOverflowParam();
					return NULL;
				} else {
					param1py.I = (unsigned int) param1tmp_l;
				}
			} else {
				makefmtstr("Uy*I|ni:", funcname, formatstr);
				// The format string and parameter names depend on the expected data types.
				if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist,
						&opstr, &arraydata.pybuffer1, &param1py.I, &arraymaxlen, &nosimd)) {
					return NULL;
				}
			}
			break;
		}
		// signed long
		case 'l' : {
			makefmtstr("Uy*l|ni:", funcname, formatstr);
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist, 
					&opstr, &arraydata.pybuffer1, &param1py.l, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			break;
		}
		// unsigned long
		case 'L' : {
			// The format string and parameter names depend on the expected data types.
			// We don't have a guaranteed data size larger than unsigned long, so
			// we can't manually range check it.
			makefmtstr("Uy*k|ni:", funcname, formatstr);
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist,
					&opstr, &arraydata.pybuffer1, &param1py.L, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			// We can't check this data range manually.
			break;
		}
		// signed long long
		case 'q' : {
			makefmtstr("Uy*L|ni:", funcname, formatstr);
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist, 
					&opstr, &arraydata.pybuffer1, &param1py.q, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			break;
		}
		// unsigned long long
		case 'Q' : {
			makefmtstr("Uy*K|ni:", funcname, formatstr);
			// The format string and parameter names depend on the expected data types.
			// We don't have a guaranteed data size larger than unsigned long long, so
			// we can't manually range check it.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist,
					&opstr, &arraydata.pybuffer1, &param1py.Q, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			// We can't check this data range manually.
			break;
		}
		// float
		case 'f' : {
			makefmtstr("Uy*f|ni:", funcname, formatstr);
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist, 
					&opstr, &arraydata.pybuffer1, &param1py.f, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isfinite(param1py.f))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			}
			break;
		}
		// double
		case 'd' : {
			makefmtstr("Uy*d|ni:", funcname, formatstr);
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, formatstr, kwlist, 
					&opstr, &arraydata.pybuffer1, &param1py.d, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isfinite(param1py.d))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			}
			break;
		}
		// We don't know this code.
		default: {
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}
