#!/usr/bin/python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for math pow2 and pow3 operations. 
#			parameter.
# Language: Python 3.8
# Date:     09-Oct-2021
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
// Date:     09-Oct-2021.
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

#include "arrayparams_one.h"


/*--------------------------------------------------------------------------- */
"""

# ==============================================================================


# ==============================================================================

# For signed integer.
ops_pow_int_signed = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data array.
   data1 = The first data array.
   data2 = The second data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into a separate array.
*/
signed int %(funclabel)s_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors, bool hasoutputarray) {


	// array index counter.
	Py_ssize_t x;

	if (hasoutputarray) {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data2[x] = data1[x] * data1[x]%(formulaexpansion)s;
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ((data1[x] > %(pow2max)s) || (data1[x] < %(pow2min)s)) { return ARR_ERR_OVFL; }
				data2[x] = data1[x] * data1[x]%(formulaexpansion)s;
			}
		}

	} else {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] * data1[x]%(formulaexpansion)s;
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ((data1[x] > %(pow2max)s) || (data1[x] < %(pow2min)s)) { return ARR_ERR_OVFL; }
				data1[x] = data1[x] * data1[x]%(formulaexpansion)s;
			}
		}
	}

	return ARR_NO_ERR;
}

"""



# For unsigned integer.
ops_pow_int_unsigned = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data array.
   data1 = The first data array.
   data2 = The second data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into a separate array.
*/
signed int %(funclabel)s_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors, bool hasoutputarray) {


	// array index counter.
	Py_ssize_t x;

	if (hasoutputarray) {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data2[x] = data1[x] * data1[x]%(formulaexpansion)s;
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if (data1[x] > %(pow2max)s) { return ARR_ERR_OVFL; }
				data2[x] = data1[x] * data1[x]%(formulaexpansion)s;
			}
		}

	} else {

		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] * data1[x]%(formulaexpansion)s;
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if (data1[x] > %(pow2max)s) { return ARR_ERR_OVFL; }
				data1[x] = data1[x] * data1[x]%(formulaexpansion)s;
			}
		}

	}

	return ARR_NO_ERR;
}


"""


# ==============================================================================

# For floating point.
ops_pow_float = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into a separate array.
*/
// param_arr_none
signed int %(funclabel)s_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;

	if (hasoutputarray) {

		// Math error checking disabled.
		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data2[x] = data1[x] * data1[x]%(formulaexpansion)s;
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data2[x] = data1[x] * data1[x]%(formulaexpansion)s;
				if (!isfinite(data2[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}

	} else {

		// Math error checking disabled.
		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] * data1[x]%(formulaexpansion)s;
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] * data1[x]%(formulaexpansion)s;
				if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}

	}

	return ARR_NO_ERR;

}


"""

# ==============================================================================


# This is the set of function calls used to call each operator function.
opscall = """
		// %(funcmodifier)s
		case '%(arraycode)s' : {
			resultcode = %(funclabel)s_%(funcmodifier)s(arraydata.arraylength, arraydata.array1.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.ignoreerrors, arraydata.hasoutputarray);
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
%(opscall)s
		// Wrong array type code.
		default: {
			releasebuffers_one(arraydata);
			ErrMsgTypeExpectFloat();
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

	if (resultcode == ARR_ERR_OVFL) {
		ErrMsgArithOverflowCalc();
		return NULL;
	}

	if (resultcode == ARR_ERR_VALUE_ERR) {
		ErrMsgParameterNotValidforthisOperation();
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
Equivalent to:          [x * x%(docexpansion)s for x in array1] \\n\\
======================  ============================================== \\n\\
\\n\\
======================  ============================================== \\n\\
Array types supported:  %(supportedarrays)s \\n\\
Exceptions raised:      %(matherrors)s \\n\\
======================  ============================================== \\n\\
\\n\\
Call formats: \\n\\
\\n\\
  %(funclabel)s(array1) \\n\\
  %(funclabel)s(array1, outparray) \\n\\
  %(funclabel)s(array1, maxlen=y) \\n\\
  %(funclabel)s(array1, matherrors=False) \\n\\
\\n\\
* array1 - The first input data array to be examined. If no output  \\n\\
  array is provided the results will overwrite the input data.  \\n\\
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

# Limits to squares and cubes for overflow detection for each integer types.
# POW2MAX and POW2MIN refer to the maximum and mininum value which can be
# raised to the power of 2 without overflowing for that array type.
# POW3MAX and POW3MIN are the corresponding versions for raising to
# the power of 3.

pow2_limits_definitions = '''
#define SCHAR_POW2MAX 11
#define SCHAR_POW2MIN -11 
#define UCHAR_POW2MAX 15

#define SSHORT_POW2MAX 181
#define SSHORT_POW2MIN -181 
#define USHORT_POW2MAX 255

#define SINT_POW2MAX 46340
#define SINT_POW2MIN -46340
#define UINT_POW2MAX 65535

// Account for 64 bit versus 32 bit word sizes.
#if LONG_MAX == LLONG_MAX

#define SLINT_POW2MAX 3037000499L
#define SLINT_POW2MIN -3037000499L
#define ULINT_POW2MAX 4294967295UL

#else

#define SLINT_POW2MAX 46340
#define SLINT_POW2MIN -46340
#define ULINT_POW2MAX 65535

#endif

#define SLLINT_POW2MAX 3037000499LL
#define SLLINT_POW2MIN -3037000499LL
#define ULLINT_POW2MAX 4294967295ULL

'''


pow3_limits_definitions = '''
#define SCHAR_POW3MAX 5
#define SCHAR_POW3MIN -5 
#define UCHAR_POW3MAX 6

#define SSHORT_POW3MAX 31
#define SSHORT_POW3MIN -32 
#define USHORT_POW3MAX 40

#define SINT_POW3MAX 1290
#define SINT_POW3MIN -1290
#define UINT_POW3MAX 1625

// Account for 64 bit versus 32 bit word sizes.
#if LONG_MAX == LLONG_MAX

#define SLINT_POW3MAX 2097151
#define SLINT_POW3MIN -2097152
#define ULINT_POW3MAX 2642245

#else

#define SLINT_POW3MAX 1290
#define SLINT_POW3MIN -1290
#define ULINT_POW3MAX 1625

#endif

#define SLLINT_POW3MAX 2097151
#define SLLINT_POW3MIN -2097152
#define ULLINT_POW3MAX 2642245

'''

# Maximum and minimum limits for raising integers to powers of 2 or 3.
pow2_limits_max = {
	'b' : 'SCHAR_POW2MAX',
	'B' : 'UCHAR_POW2MAX',
	'h' : 'SSHORT_POW2MAX',
	'H' : 'USHORT_POW2MAX',
	'i' : 'SINT_POW2MAX',
	'I' : 'UINT_POW2MAX',
	'l' : 'SLINT_POW2MAX',
	'L' : 'ULINT_POW2MAX',
	'q' : 'SLLINT_POW2MAX',
	'Q' : 'ULLINT_POW2MAX',
	'f' : '',
	'd' : '',
}

pow2_limits_min = {
	'b' : 'SCHAR_POW2MIN',
	'B' : '0',
	'h' : 'SSHORT_POW2MIN',
	'H' : '0',
	'i' : 'SINT_POW2MIN',
	'I' : '0',
	'l' : 'SLINT_POW2MIN',
	'L' : '0',
	'q' : 'SLLINT_POW2MIN',
	'Q' : '0',
	'f' : '',
	'd' : '',
}

pow3_limits_max = {
	'b' : 'SCHAR_POW3MAX',
	'B' : 'UCHAR_POW3MAX',
	'h' : 'SSHORT_POW3MAX',
	'H' : 'USHORT_POW3MAX',
	'i' : 'SINT_POW3MAX',
	'I' : 'UINT_POW3MAX',
	'l' : 'SLINT_POW3MAX',
	'L' : 'ULINT_POW3MAX',
	'q' : 'SLLINT_POW3MAX',
	'Q' : 'ULLINT_POW3MAX',
	'f' : '',
	'd' : '',
}

pow3_limits_min = {
	'b' : 'SCHAR_POW3MIN',
	'B' : '0',
	'h' : 'SSHORT_POW3MIN',
	'H' : '0',
	'i' : 'SINT_POW3MIN',
	'I' : '0',
	'l' : 'SLINT_POW3MIN',
	'L' : '0',
	'q' : 'SLLINT_POW3MIN',
	'Q' : '0',
	'f' : '',
	'd' : '',
}

# ==============================================================================


# Output conventional C code.
# Go through the list of functions being created. 
def MakeOutputFile(funcname, pow_limits_definitions, pow_limits_max, pow_limits_min, 
					formulaexpansion, docexpansion):

	matherrorsdocs = 'OverflowError, ArithmeticError, ValueError'
	arraytypesdocs = 'si,ui,f'
	supportedarrays = codegen_common.FormatDocsArrayTypes(arraytypesdocs)

	# Create the source code based on templates.
	filename = funcname + '.c'
	with open(filename, 'w') as f:

		f.write(mathops_head % {'funclabel' : funcname})

		f.write(pow_limits_definitions)

		opscalldatatext = []

		# Check each array type. The types of arrays supported must be looked up.
		for arraycode in codegen_common.arraycodes:
			arraytype = codegen_common.arraytypes[arraycode]
			funcmodifier = arraytype.replace(' ', '_')

			funcdata = {'arraycode' : arraycode,
						'arraytype' : arraytype,
						'funclabel' : funcname,
						'funcmodifier' : funcmodifier,
						'pow2max' : pow_limits_max[arraycode],
						'pow2min' : pow_limits_min[arraycode],
						'formulaexpansion' : formulaexpansion,
						}

			# The code for each array type.
			if arraycode in codegen_common.signedint:
				template = ops_pow_int_signed
			elif arraycode in codegen_common.unsignedint:
				template = ops_pow_int_unsigned
			elif arraycode in codegen_common.floatarrays:
				template = ops_pow_float
			else:
				print('Error: Unknown array type: ', arraycode)

			f.write(template % funcdata)

			# Accumulate the switch data for calling the code for each arraytype.
			opscalldatatext.append(opscall % funcdata)


		# Write the remaining boilerplate C code. 
		f.write(mathops_params % {'funclabel' : funcname, 
				'supportedarrays' : supportedarrays,
				'matherrors' : matherrorsdocs,
				'docexpansion' : docexpansion,
				'opscall' : ''.join(opscalldatatext)})


# ==============================================================================

# pow2
MakeOutputFile('pow2', pow2_limits_definitions, pow2_limits_max, pow2_limits_min,
				'', '')

# pow3
MakeOutputFile('pow3', pow3_limits_definitions, pow3_limits_max, pow3_limits_min,
				' * data1[x]', ' * x')
