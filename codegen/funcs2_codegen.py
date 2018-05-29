#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for math functions which accept a single 
#			parameter.
# Language: Python 3.4
# Date:     30-Dec-2017
#
###############################################################################
#
#   Copyright 2014 - 2017    Michael Griffin    <m12.griffin@gmail.com>
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

mathfunc2_head = """//------------------------------------------------------------------------------
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

#include "%(arrayparamsheader)s.h"

/*--------------------------------------------------------------------------- */
"""

# ==============================================================================

mathfunc2_calc = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = %(cfuncname)s(data1[x], param);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = %(cfuncname)s(data1[x], param);
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = %(cfuncname)s(data1[x], param);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = %(cfuncname)s(data1[x], param);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = %(cfuncname)s(param, data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data2[x] = %(cfuncname)s(param, data2[x]);
			if (!isfinite(data2[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = %(cfuncname)s(param, data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = %(cfuncname)s(param, data2[x]);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = %(cfuncname)s(data1[x], data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = %(cfuncname)s(data1[x], data2[x]);
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = %(cfuncname)s(data1[x], data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = %(cfuncname)s(data1[x], data2[x]);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}
"""


mathfunc2_params = """
/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;

	// This is used to hold the parsed parameters.
	struct args_params_2 arraydata = ARGSINIT_TWO;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_two(self, args, keywds, "%(funclabel)s");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}

	// Call the C function.
	switch(arraydata.arraytype) {
		// float
		case 'f' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = %(funclabel)s_float_1(arraydata.arraylength, arraydata.array1.f, arraydata.param.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = %(funclabel)s_float_2(arraydata.arraylength, arraydata.array1.f, arraydata.param.f, arraydata.array3.f, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = %(funclabel)s_float_3(arraydata.arraylength, arraydata.param.f, arraydata.array2.f, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = %(funclabel)s_float_4(arraydata.arraylength, arraydata.param.f, arraydata.array2.f, arraydata.array3.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = %(funclabel)s_float_5(arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = %(funclabel)s_float_6(arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.array3.f, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}
		// double
		case 'd' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = %(funclabel)s_double_1(arraydata.arraylength, arraydata.array1.d, arraydata.param.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = %(funclabel)s_double_2(arraydata.arraylength, arraydata.array1.d, arraydata.param.d, arraydata.array3.d, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = %(funclabel)s_double_3(arraydata.arraylength, arraydata.param.d, arraydata.array2.d, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = %(funclabel)s_double_4(arraydata.arraylength, arraydata.param.d, arraydata.array2.d, arraydata.array3.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = %(funclabel)s_double_5(arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = %(funclabel)s_double_6(arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.array3.d, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}
		// Wrong array type code.
		default: {
			releasebuffers_two(arraydata);
			ErrMsgTypeExpectFloat();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_two(arraydata);


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
Equivalent to:          %(opcodedocs)s \\n\\
Array types supported:  %(supportedarrays)s \\n\\
Exceptions raised:      %(matherrors)s \\n\\
======================  ============================================== \\n\\
\\n\\
Call formats: \\n\\
\\n\\
  %(funclabel)s(array1, param) \\n\\
  %(funclabel)s(array1, param, outparray) \\n\\
  %(funclabel)s(param, array1) \\n\\
  %(funclabel)s(param, array1, outparray) \\n\\
  %(funclabel)s(array1, array2) \\n\\
  %(funclabel)s(array1, array2, outparray) \\n\\
  %(funclabel)s(array1, param, maxlen=y) \\n\\
  %(funclabel)s(array1, param, matherrors=False) \\n\\
\\n\\
* array1 - The first input data array to be examined. If no output  \\n\\
  array is provided the results will overwrite the input data.  \\n\\
* param - A non-array numeric parameter.  \\n\\
* array2 - A second input data array. Each element in this array is  \\n\\
  applied to the corresponding element in the first array.  \\n\\
* outparray - The output array. This parameter is optional.  \\n\\
* maxlen - Limit the length of the array used. This must be a valid  \\n\\
  positive integer. If a zero or negative length, or a value which is  \\n\\
  greater than the actual length of the array is specified, this  \\n\\
  parameter is ignored.  \\n\\
* matherrors - If true, arithmetic error checking is disabled. The  \\n\\
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

# ==============================================================================


# For ldexp only. 
mathfunc_ldexp_calc = """
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   exp = The exponent to be applied to each array element.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hassecondarray = If true, the output goes into the second array.
*/
signed int ldexp_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, signed long long exp, %(arraytype)s *dataout, unsigned int ignoreerrors, bool hassecondarray) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		if (hassecondarray) {		
			for(x = 0; x < arraylen; x++) {
				dataout[x] = %(cfuncname)s(data[x], exp);
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				data[x] = %(cfuncname)s(data[x], exp);
			}
		}
	} else {
	// Math error checking enabled.
		if (hassecondarray) {		
			for(x = 0; x < arraylen; x++) {
				dataout[x] = %(cfuncname)s(data[x], exp);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				data[x] = %(cfuncname)s(data[x], exp);
				if (!isfinite(data[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
	}

	return ARR_NO_ERR;

}
/*--------------------------------------------------------------------------- */

"""

mathfunc2_ldexp_params = """
/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_ldexp(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;


	// This is used to return the parsed parameters.
	struct args_params_ldexp arraydata = ARGSINIT_SPECIAL;


	// -----------------------------------------------------

	// Get the parameters passed from Python.
	arraydata = getparams_ldexp(self, args, keywds);

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}


	// Call the C function.
	switch(arraydata.arraytype) {
		// float
		case 'f' : {
			resultcode = ldexp_float(arraydata.arraylength, arraydata.array1.f, arraydata.exp, arraydata.array2.f, arraydata.ignoreerrors, arraydata.hassecondarray);
			break;
		}
		// double
		case 'd' : {
			resultcode = ldexp_double(arraydata.arraylength, arraydata.array1.d, arraydata.exp, arraydata.array2.d, arraydata.ignoreerrors, arraydata.hassecondarray);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_twobuff(arraydata.pybuffer1, arraydata.pybuffer2, arraydata.hassecondarray);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_twobuff(arraydata.pybuffer1, arraydata.pybuffer2, arraydata.hassecondarray);


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
PyDoc_STRVAR(ldexp__doc__,
"%(funclabel)s \\n\\
_____________________________ \\n\\
\\n\\
Calculate %(funclabel)s over the values in an array.  \\n\\
\\n\\
======================  ============================================== \\n\\
Equivalent to:          %(opcodedocs)s \\n\\
Array types supported:  %(supportedarrays)s \\n\\
Exceptions raised:      %(matherrors)s \\n\\
======================  ============================================== \\n\\
\\n\\
Call formats: \\n\\
\\n\\
    %(funclabel)s(array1, exp) \\n\\
    %(funclabel)s(array1, exp, outparray) \\n\\
    %(funclabel)s(array1, exp, maxlen=y) \\n\\
    %(funclabel)s(array1, exp, matherrors=False)) \\n\\
\\n\\
* array1 - The first input data array to be examined. If no output  \\n\\
  array is provided the results will overwrite the input data.  \\n\\
* exp - The exponent to apply to the input array. This must be an \\n\\
  integer. \\n\\
* outparray - The output array. This parameter is optional.  \\n\\
* maxlen - Limit the length of the array used. This must be a valid  \\n\\
  positive integer. If a zero or negative length, or a value which is  \\n\\
  greater than the actual length of the array is specified, this  \\n\\
  parameter is ignored.  \\n\\
* matherrors - If true, arithmetic error checking is disabled. The  \\n\\
  default is false. \\n\\
");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "ldexp" is the name seen inside of Python. 
 "py_ldexp" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef ldexp_methods[] = {
	{"ldexp",  (PyCFunction)py_ldexp, METH_VARARGS | METH_KEYWORDS, ldexp__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef ldexpmodule = {
    PyModuleDef_HEAD_INIT,
    "ldexp",
    NULL,
    -1,
    ldexp_methods
};

PyMODINIT_FUNC PyInit_ldexp(void)
{
    return PyModule_Create(&ldexpmodule);
};

/*--------------------------------------------------------------------------- */

"""


# ==============================================================================

# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.

funclist = [x for x in oplist if x['c_code_template'] in ['template_mathfunc_2', 'template_ldexpfunc_2']]


# ==============================================================================

for func in funclist:

	# Some functions use a different template than the rest.
	# This one is for most normal functions.
	if func['c_code_template'] == 'template_mathfunc_2':
		arrayparamsheader = 'arrayparams_two'
		func_calc = mathfunc2_calc
		func_params = mathfunc2_params

	# This one is for ldexp.
	elif func['c_code_template'] == 'template_ldexpfunc_2':
		arrayparamsheader = 'arrayparams_special'
		func_calc = mathfunc_ldexp_calc
		func_params = mathfunc2_ldexp_params

	else:
		print('Error - unknown C code template.', func['c_code_template'])



	# Create the source code based on templates.
	filename = func['funcname'] + '.c'
	with open(filename, 'w') as f:
		funcdata = {'funclabel' : func['funcname']}
		f.write(mathfunc2_head % {'funclabel' : func['funcname'], 'arrayparamsheader' : arrayparamsheader})
		for arraycode in codegen_common.floatarrays:
			funcdata['funcmodifier'] = codegen_common.arraytypes[arraycode]
			funcdata['arraytype'] = codegen_common.arraytypes[arraycode]
			if arraycode == 'f':
				funcdata['cfuncname'] = func['c_operator_f']
			else:
				 funcdata['cfuncname'] = func['c_operator_d']
			f.write(func_calc % funcdata)


		supportedarrays = codegen_common.FormatDocsArrayTypes(func['arraytypes'])

		f.write(func_params % {'funclabel' : func['funcname'], 
				'opcodedocs' : func['opcodedocs'], 
				'supportedarrays' : supportedarrays,
				'matherrors' : ', '.join(func['matherrors'].split(','))})



# ==============================================================================


