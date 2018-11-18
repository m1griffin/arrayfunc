#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for math functions which accept a single 
#			parameter and returns a true or false.
# Language: Python 3.4
# Date:     10-Apr-2018
#
###############################################################################
#
#   Copyright 2014 - 2018    Michael Griffin    <m12.griffin@gmail.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
##############################################################################

# ==============================================================================

import itertools

import codegen_common

# ==============================================================================

mathfunc1 = """//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   %(funclabel)s.c
// Purpose:  Calculate the %(funclabel)s of values in an array.
// Language: C
// Date:     15-Nov-2017.
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

/*--------------------------------------------------------------------------- */
// This must be defined before "Python.h" in order for the pointers in the
// argument parsing functions to work properly. 
#define PY_SSIZE_T_CLEAN

#include "Python.h"

#include <limits.h>
#include <math.h>

#include "arrayerrs.h"
#include "arrayparams_base.h"
#include "arrayparams_boolout.h"


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   Returns True if the search condition is met.
*/
signed int %(funclabel)s_float(Py_ssize_t arraylen, float *data) {

	// array index counter.
	Py_ssize_t x;

	for(x = 0; x < arraylen; x++) {
		if (%(floatfunc)s) { return %(foundsearch)s; }
	}

	return %(notfoundsearch)s;

}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   Returns True if the search condition is met.
*/
signed int %(funclabel)s_double(Py_ssize_t arraylen, double *data) {

	// array index counter.
	Py_ssize_t x;

	for(x = 0; x < arraylen; x++) {
		if (%(doublefunc)s) { return %(foundsearch)s; }
	}

	return %(notfoundsearch)s;

}

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;

	// This is used to hold the parsed parameters.
	struct args_params_boolout arraydata = ARGSINIT_BOOLOUT;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_boolout(self, args, keywds, "%(funclabel)s");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}

	// Call the C function.
	switch(arraydata.arraytype) {
		// float
		case 'f' : {
			resultcode = %(funclabel)s_float(arraydata.arraylength, arraydata.array1.f);
			break;
		}
		// double
		case 'd' : {
			resultcode = %(funclabel)s_double(arraydata.arraylength, arraydata.array1.d);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_boolout(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_boolout(arraydata);


	// Return whether compare was OK.
	if (resultcode) {
		Py_RETURN_TRUE;
	} else {
		Py_RETURN_FALSE;
	}

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(%(funclabel)s__doc__,
"%(funclabel)s \\n\\
_____________________________ \\n\\
\\n\\
Calculate %(funclabel)s over the values in an array. \\n\\
\\n\\
======================  ============================================== \\n\\
Equivalent to:          %(opcodedocs)s \\n\\
Array types supported:  %(supportedarrays)s \\n\\
Exceptions raised:      %(matherrors)s \\n\\
======================  ============================================== \\n\\
\\n\\
Call formats: \\n\\
\\n\\
    result = %(funclabel)s(array1) \\n\\
    result = %(funclabel)s(array1, maxlen=y) \\n\\
\\n\\
* array1 - The first input data array to be examined. If no output \\n\\
  array is provided the results will overwrite the input data. \\n\\
* maxlen - Limit the length of the array used. This must be a valid \\n\\
  positive integer. If a zero or negative length, or a value which is \\n\\
  greater than the actual length of the array is specified, this \\n\\
  parameter is ignored. \\n\\
* %(helpresult)s\\n\\
");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "%(funclabel)s" is the name seen inside of Python. 
 "py_%(funclabel)s" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef %(funclabel)s_methods[] = {
	{"%(funclabel)s",  (PyCFunction)py_%(funclabel)s, METH_VARARGS | METH_KEYWORDS, %(funclabel)s__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef %(funclabel)smodule = {
    PyModuleDef_HEAD_INIT,
    "%(funclabel)s",
    NULL,
    -1,
    %(funclabel)s_methods
};

PyMODINIT_FUNC PyInit_%(funclabel)s(void)
{
    return PyModule_Create(&%(funclabel)smodule);
};

/*--------------------------------------------------------------------------- */

"""


# ==============================================================================

# These are used for most normal functions.
floatfunctmpl = '%(c_operator_f)s(data[x])'
doublefunctmpl = '%(c_operator_d)s(data[x])'

# These are used for functions which do not follow the normal pattern.
# The correct format is read from the spreadsheet.
specialfloatfunctmpl = '%(c_operator_f)s'
specialdoublefunctmpl = '%(c_operator_d)s'


# ==============================================================================

# Select what return value is used when condition is found.
foundsearch = {'isinf' : 1,
			'isnan' : 1,
			'isfinite' : 0
}


# Select what return value is used when condition is not found.
notfoundsearch = {'isinf' : 0,
			'isnan' : 0,
			'isfinite' : 1
}

# ==============================================================================

anyhelp = """result - A boolean value corresponding to the result of all the \\n\\
  comparison operations. If at least one comparison operation results in \\n\\
  true, the return value will be true. If none of them result in true, \\n\\
  the return value will be false."""

allhelp = """result - A boolean value corresponding to the result of all the \\n\\
  comparison operations. If all of the comparison operations result in \\n\\
  true, the return value will be true. If any of them result in false, \\n\\
  the return value will be false."""

# Select the help description for the type of function.
helpresult = {'isinf' : anyhelp,
			'isnan' : anyhelp,
			'isfinite' : allhelp
}

# ==============================================================================

# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.

funclist = [x for x in oplist if x['c_code_template'] == 'template_mathfuncnan']

# ==============================================================================

for func in funclist:
	funcname = func['funcname']

	filename = funcname + '.c'

	floatfunc = specialfloatfunctmpl % {'c_operator_f' : func['c_operator_f']}
	doublefunc = specialdoublefunctmpl % {'c_operator_d' : func['c_operator_d']}

	supportedarrays = codegen_common.FormatDocsArrayTypes(func['arraytypes'])

	funcdata = {'funclabel' : funcname, 
			'funcfloatname' : func['c_operator_f'], 
			'funcdoublename' : func['c_operator_d'],
			'floatfunc' : floatfunc, 
			'doublefunc' : doublefunc, 
			'opcodedocs' : func['opcodedocs'], 
			'supportedarrays' : supportedarrays,
			'matherrors' : ', '.join(func['matherrors'].split(',')),
			'foundsearch' : foundsearch[funcname],
			'notfoundsearch' : notfoundsearch[funcname],
			'helpresult' : helpresult[funcname]
			}	

	with open(filename, 'w') as f:
		f.write(mathfunc1 % funcdata)



# ==============================================================================
