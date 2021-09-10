#!/usr/bin/python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for math pow operations. 
#			parameter.
# Language: Python 3.8
# Date:     30-Dec-2017
#
###############################################################################
#
#   Copyright 2014 - 2021    Michael Griffin    <m12.griffin@gmail.com>
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

mathops_head = """//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   %(funclabel)s.c
// Purpose:  Calculate the %(funclabel)s of values in an array.
// Language: C
// Date:     15-Nov-2017.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2021    Michael Griffin    <m12.griffin@gmail.com>
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

#include "arrayparams_two.h"

%(includeoptions)s

/*--------------------------------------------------------------------------- */
"""

# ==============================================================================



# ==============================================================================

# For signed and unsigned integer.
ops_pow_int = """

%(powtemplate)s

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
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_%(funcmodifier)s(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_%(funcmodifier)s(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_%(funcmodifier)s(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_%(funcmodifier)s(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_%(funcmodifier)s(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_%(funcmodifier)s(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_%(funcmodifier)s(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_%(funcmodifier)s(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_%(funcmodifier)s(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_%(funcmodifier)s(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_%(funcmodifier)s(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_%(funcmodifier)s(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}
"""

# ==============================================================================


# ==============================================================================

# For floating point.
ops_pow_float = """
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
		for (x = 0; x < arraylen; x++) {
			data1[x] = %(copname)s(data1[x], param);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data1[x] = %(copname)s(data1[x], param);
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
		for (x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(data1[x], param);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(data1[x], param);
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
		for (x = 0; x < arraylen; x++) {
			data2[x] = %(copname)s(param, data2[x]);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data2[x] = %(copname)s(param, data2[x]);
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
		for (x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(param, data2[x]);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(param, data2[x]);
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
		for (x = 0; x < arraylen; x++) {
			data1[x] = %(copname)s(data1[x], data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = %(copname)s(data1[x], data2[x]);
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
		for (x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(data1[x], data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(data1[x], data2[x]);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}
"""

# ==============================================================================


# ==============================================================================

# These are used for the pow function only.

powtemplatesigned = """
/*--------------------------------------------------------------------------- */

// Note: The guard calculations for negative need to use abs(x) instead of -x
// because of problems with Microsoft MSVS 2010. MSVS was confused by negating
// a negative number with minimum integers (e.g. INT_MIN) and producing a
// positive result.

// Return x raised to the power of y.
%(arraytype)s arith_pow_%(funcmodifier)s(%(arraytype)s x, %(arraytype)s y, char *errflag) {
	%(arraytype)s i, z, ovtmp1, ovtmp2;
	z = 1;
	*errflag = 0;

	// We don't allow negative powers for integers.
	if (y < 0) {
		*errflag = ARR_ERR_VALUE_ERR;
		return z;
	}

	// Special case for raise to the power of zero.
	if (y == 0) { return 1; }

	// We need this special case to avoid dividing by zero.
	if (x == 0) {return 0;}

	if (x > 0) {
		ovtmp1 = %(intmaxvalue)s / x;
		for (i = 0; i < y; i++) {
			if (z > ovtmp1) {*errflag = ARR_ERR_OVFL; return z;}
			z = z * x;
		}
	} else {
		ovtmp1 = %(intmaxvalue)s / %(abs)s(x);
		ovtmp2 = %(intminvalue)s / %(abs)s(x);
		for (i = 0; i < y; i++) {
			if ((z > ovtmp1) || (z < ovtmp2)) {*errflag = ARR_ERR_OVFL; return z;}
			z = z * x;
		}
	}
	return z;
}

"""


powtemplateunsigned = """
// Return x raised to the power of y.
%(arraytype)s arith_pow_%(funcmodifier)s(%(arraytype)s x, %(arraytype)s y, char *errflag) {
	%(arraytype)s i, z, ovtmp1;
	z = 1;
	*errflag = 0;

	// Special case for raise to the power of zero.
	if (y == 0) { return 1; }

	// We need this special case to avoid dividing by zero.
	if (x == 0) {return 0;}

	ovtmp1 = %(intmaxvalue)s / x;
	for (i = 0; i < y; i++) {
		if (z > ovtmp1) {*errflag = ARR_ERR_OVFL; return z;}
		z = z * x;
	}
	return z;
}

/*--------------------------------------------------------------------------- */
"""


# ==============================================================================

# ==============================================================================

# This is the set of function calls used to call each operator function.
opscall = """
		// %(funcmodifier)s
		case '%(arraycode)s' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = %(funclabel)s_%(funcmodifier)s_1(arraydata.arraylength,%(nosimdparam)s arraydata.array1.%(arraycode)s, arraydata.param.%(arraycode)s, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = %(funclabel)s_%(funcmodifier)s_2(arraydata.arraylength,%(nosimdparam)s arraydata.array1.%(arraycode)s, arraydata.param.%(arraycode)s, arraydata.array3.%(arraycode)s, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = %(funclabel)s_%(funcmodifier)s_3(arraydata.arraylength,%(nosimdparam)s arraydata.param.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = %(funclabel)s_%(funcmodifier)s_4(arraydata.arraylength,%(nosimdparam)s arraydata.param.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.array3.%(arraycode)s, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = %(funclabel)s_%(funcmodifier)s_5(arraydata.arraylength,%(nosimdparam)s arraydata.array1.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = %(funclabel)s_%(funcmodifier)s_6(arraydata.arraylength,%(nosimdparam)s arraydata.array1.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.array3.%(arraycode)s, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}
"""


# ==============================================================================


mathops_params = """
/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;

	// This is used to hold the parsed parameters.
	struct args_params_2 arraydata = ARGSINIT_TWO;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_two(self, args, keywds, 1, %(getsimdparam)s, "%(funclabel)s");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}

	// Call the C function.
	switch(arraydata.arraytype) {
%(opscall)s
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
	if (resultcode == ARR_ERR_ZERODIV) {
		ErrMsgZeroDiv();
		return NULL;
	}

	if (resultcode == ARR_ERR_ARITHMETIC) {
		ErrMsgArithCalc();
		return NULL;
	}

	if (resultcode == ARR_ERR_OVFL) {
		ErrMsgArithOverflowCalc();
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
Equivalent to:          [x %(pyoperator)s param for x in array1] \\n\\
or                      [param %(pyoperator)s y for y in array2] \\n\\
or                      [x %(pyoperator)s y for x, y in zip(array1, array2)] \\n\\
======================  ============================================== \\n\\
\\n\\
======================  ============================================== \\n\\
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
%(helpsimd1)s\\n\\
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
%(helpsimd2)s");

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

# These are the C functions used to calculate absolute value (abs).
absfunc = {
	'b' : 'abs',
	'B' : '',
	'h' : 'abs',
	'H' : '',
	'i' : 'abs',
	'I' : '',
	'l' : 'labs',
	'L' : '',
	'q' : 'llabs',
	'Q' : '',
	'f' : '',
	'd' : ''
}

# ==============================================================================


# Create the source code based on templates.
funcname = 'pow'
filename = funcname + '.c'
pyoperator = '**'
copname = '/'

c_operator_i = 'arith_pow_int-type'
c_operator_f = 'powf'
c_operator_d = 'pow'


# This code generator script does not use data read from the spreadsheet.
arraytypesdocs = 'si,ui,f'
opcodedocs = 'x**y or math.pow(x, y)'
matherrorsdocs = 'OverflowError,ArithmeticError'

# These are the templates for each type specific operation. 
float_template = ops_pow_float
uint_template = ops_pow_int
int_template = ops_pow_int

# ==============================================================================

with open(filename, 'w') as f:

	funcdata = {'funclabel' : funcname, 
				'includeoptions' : '',
				'copname' : copname,
				'nosimddecl' : '',
				'nosimdparam' : '',
				}
		
	f.write(mathops_head % funcdata)
	opscalltext = []

		

	# Check each array type.
	for arraycode in codegen_common.arraycodes:
		arraytype = codegen_common.arraytypes[arraycode]
		funcmodifier = arraytype.replace(' ', '_')

		funcdata['funcmodifier'] = funcmodifier
		funcdata['arraytype'] = arraytype
		funcdata['intmaxvalue'] = codegen_common.maxvalue[arraycode]
		funcdata['intminvalue'] = codegen_common.minvalue[arraycode]


		if arraycode == 'd':
			ops_calc = float_template
			funcdata['copname'] = c_operator_d
		elif arraycode == 'f':
			ops_calc = float_template
			funcdata['copname'] = c_operator_f
		elif arraycode in codegen_common.unsignedint:
			ops_calc = uint_template
			funcdata['copname'] = c_operator_i
		elif arraycode in codegen_common.signedint:
			ops_calc = int_template
			funcdata['copname'] = c_operator_i
		else:
			print('Error - Unsupported array code.', arraycode)

		# This is used for pow only.
		funcdata['abs'] = absfunc[arraycode]

		# This is for pow and inserts some of the data so far back into the 
		# dictionary to be added in again.
		if arraycode in codegen_common.unsignedint:
			 funcdata['powtemplate'] = powtemplateunsigned % funcdata
		elif arraycode in codegen_common.signedint:
			 funcdata['powtemplate'] = powtemplatesigned % funcdata


		f.write(ops_calc % funcdata)

		# This is the call to the functions for this array type. This
		# is inserted into another template below.
		funcdata['arraycode'] = arraycode
		opscalltext.append(opscall % funcdata)


	helpsimd1 = ''
	helpsimd2 = ''
	getsimdparam = '0'


	supportedarrays = codegen_common.FormatDocsArrayTypes(arraytypesdocs)

	f.write(mathops_params % {'funclabel' : funcname, 
			'opcodedocs' : opcodedocs, 
			'supportedarrays' : supportedarrays,
			'pyoperator' : pyoperator,
			'matherrors' : ', '.join(matherrorsdocs.split(',')),
			'opscall' : ''.join(opscalltext),
			'getsimdparam' : getsimdparam,
			'helpsimd1' : helpsimd1,
			'helpsimd2' : helpsimd2})


# ==============================================================================
