#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for math functions which accept a single 
#			parameter.
# Language: Python 3.4
# Date:     08-Dec-2017
#
###############################################################################
#
#   Copyright 2014 - 2020    Michael Griffin    <m12.griffin@gmail.com>
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

mathfunc1_template = """//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   %(funclabel)s.c
// Purpose:  Calculate the %(funclabel)s of values in an array.
// Language: C
// Date:     15-Nov-2017.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2020    Michael Griffin    <m12.griffin@gmail.com>
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

#include "arrayparams_one.h"


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int %(funclabel)s_float(Py_ssize_t arraylen, float *data, float *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = %(floatfunc)s;
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = %(floatfunc)s;
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = %(floatfunc)s;
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = %(floatfunc)s;
				if (!isfinite(data[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
	}

	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int %(funclabel)s_double(Py_ssize_t arraylen, double *data, double *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {
			for (x = 0; x < arraylen; x++) {
				dataout[x] = %(doublefunc)s;
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = %(doublefunc)s;
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {
			for (x = 0; x < arraylen; x++) {
				dataout[x] = %(doublefunc)s;
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = %(doublefunc)s;
				if (!isfinite(data[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
	}
	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;

	// This is used to hold the parsed parameters.
	struct args_params_1 arraydata = ARGSINIT_ONE;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_one(self, args, keywds, 1, "%(funclabel)s");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}

	// Call the C function.
	switch(arraydata.arraytype) {
		// float
		case 'f' : {
			resultcode = %(funclabel)s_float(arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}
		// double
		case 'd' : {
			resultcode = %(funclabel)s_double(arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_one(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_one(arraydata);


	// Signal the errors.
	if (resultcode == ARR_ERR_ARITHMETIC) {
		ErrMsgArithCalc();
		return NULL;
	}


	// Everything was successful.
	Py_RETURN_NONE;

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(%(funclabel)s__doc__,
"%(funclabel)s \\n\\
_____________________________ \\n\\
\\n\\
Calculate %(funclabel)s over the values in an array.  \\n\\
\\n\\
======================  ============================================== \\n\\
Equivalent to:          [%(opcodedocs)s for x in array1] \\n\\
Array types supported:  %(supportedarrays)s \\n\\
Exceptions raised:      %(matherrors)s \\n\\
======================  ============================================== \\n\\
\\n\\
Call formats: \\n\\
\\n\\
    %(funclabel)s(array1) \\n\\
    %(funclabel)s(array1, outparray) \\n\\
    %(funclabel)s(array1, maxlen=y) \\n\\
    %(funclabel)s(array1, matherrors=False)) \\n\\
\\n\\
* array1 - The first input data array to be examined. If no output \\n\\
  array is provided the results will overwrite the input data. \\n\\
* outparray - The output array. This parameter is optional. \\n\\
* maxlen - Limit the length of the array used. This must be a valid  \\n\\
  positive integer. If a zero or negative length, or a value which is \\n\\
  greater than the actual length of the array is specified, this \\n\\
  parameter is ignored. \\n\\
* matherrors - If true, arithmetic error checking is disabled. The \\n\\
  default is false. \\n\\
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

# This provides tje correct template for the C library function or
# C operator equation for the appropriate style of function.
cfunctmpl = '%(c_operator)s(data[x])'


# ==============================================================================


# Read in the op codes.
opdata = codegen_common.ReadINI('affuncdata.ini')

# Filter out the desired math functions.
funclist = [(x,dict(y)) for x,y in opdata.items() if y.get('c_code_template') == 'template_mathfunc_1']

# ==============================================================================

for funcname, func in funclist:

	filename = funcname + '.c'


	c_code_template = func['c_code_template']


	# Get the correct C template for the calculation, filled out for the appropriate type. 
	floatfunc = cfunctmpl % {'c_operator' : func['c_operator_f']}
	doublefunc = cfunctmpl % {'c_operator' : func['c_operator_d']}


	supportedarrays = codegen_common.FormatDocsArrayTypes(func['arraytypes'])

	funcdata = {'funclabel' : funcname, 
			'funcfloatname' : func['c_operator_f'], 
			'funcdoublename' : func['c_operator_d'],
			'floatfunc' : floatfunc, 
			'doublefunc' : doublefunc,
			'opcodedocs' : func['opcodedocs'], 
			'supportedarrays' : supportedarrays,
			'matherrors' : ', '.join(func['matherrors'].split(',')),
			}	


	with open(filename, 'w') as f:
		f.write(mathfunc1_template % funcdata)


# ==============================================================================

