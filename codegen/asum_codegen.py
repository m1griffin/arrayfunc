#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for asum.
# Language: Python 3.6
# Date:     11-Jun-2014
#
###############################################################################
#
#   Copyright 2014 - 2019    Michael Griffin    <m12.griffin@gmail.com>
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


asum_head = """//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   %(funclabel)s.c
// Purpose:  Calculate the %(funclabel)s of values in an array.
// Language: C
// Date:     15-Nov-2017.
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

/*--------------------------------------------------------------------------- */
// This must be defined before "Python.h" in order for the pointers in the
// argument parsing functions to work properly. 
#define PY_SSIZE_T_CLEAN

#include "Python.h"

#include <limits.h>
#include <math.h>

#include "arrayerrs.h"

#include "arrayparams_base.h"

#include "arrayparams_asum.h"

#include "simddefs.h"

#ifdef AF_HASSIMD_X86
#include "asum_simd_x86.h"
#endif

/*--------------------------------------------------------------------------- */
"""

# ==============================================================================


# ==============================================================================


# Template for the asum functions with overflow for signed integer.
template_basic = """/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
long long asum_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, signed int *errflag, signed int ignoreerrors) { 

	// array index counter. 
	Py_ssize_t x; 
	long long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((partialsum > 0) && (data[x] > (LLONG_MAX - partialsum))) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			if ((partialsum < 0) && (data[x] < (LLONG_MIN - partialsum))) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			partialsum = partialsum + data[x];
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */

"""

# ==============================================================================


# Template for the asum functions with overflow for unsigned integer.
template_basic_u = """/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
unsigned long long asum_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, signed int *errflag, signed int ignoreerrors) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long long partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
			if (data[x] > (ULLONG_MAX - partialsum)) { 
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			partialsum = partialsum + data[x];
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */

"""

# ==============================================================================

# This is used for floating point versions only.
floattemplate = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   nosimd = If true, disable SIMD.
   Returns: The sum of the array.
*/
double asum_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, signed int *errflag, signed int ignoreerrors, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	%(arraytype)s partialsum = 0.0;


#ifdef AF_HASSIMD_X86
	// SIMD version. Only use this if overflow checking is disabled.
	if (ignoreerrors && !nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		return asum_%(funcmodifier)s_simd(arraylen, data);
	}
#endif

	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
			if (!isfinite(partialsum)) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
		}
	}

	return %(returnmodifier)spartialsum;
}
/*--------------------------------------------------------------------------- */
"""

# ==============================================================================

# This is used for floating point SIMD versions only.
simdsupport = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   nosimd = If true, disable SIMD.
   Returns: The sum of the array.
*/
#ifdef AF_HASSIMD_X86
double asum_%(funcmodifier)s_simd(Py_ssize_t arraylen, %(arraytype)s *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	%(arraytype)s partialsum = 0.0;

	%(arraytype)s sumvals[%(simdwidth)s];
	%(simdattr)s sumslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Initialise the sum values.
	sumslice = (%(simdattr)s) %(simdload)s(data);

	// Use SIMD.
	for(x = %(simdwidth)s; x < alignedlength; x += %(simdwidth)s) {
		dataslice = (%(simdattr)s) %(simdload)s(&data[x]);
		sumslice = sumslice + dataslice;
	}

	// Add up the values within the slice.
	%(simdstore)s(sumvals, (%(simdattr)s) sumslice);
	for (y = 0; y < %(simdwidth)s; y++) {
		partialsum = partialsum + sumvals[y];
	}

	// Add the values within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}


	return %(returnmodifier)spartialsum;
}
#endif
/*--------------------------------------------------------------------------- */
"""


# ==============================================================================

asum_params = """
/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// This is used to hold the parsed parameters.
	struct args_params_asum arraydata = ARGSINIT_ASUM;

	// The sum of the array, as a python object.
	PyObject *sumreturn;

	// Indicates an error.
	signed int errflag = 0;

	// Results are different types.
	long long resultll = 0;
	unsigned long long resultull = 0;
	double resultd = 0.0;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_asum(self, args, keywds, "%(funclabel)s");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}


	// The length of the data array.
	if (arraydata.arraylength < 1) {
		// Release the buffers. 
		releasebuffers_asum(arraydata);
		ErrMsgArrayLengthErr();
		return NULL;
	}



	/* Call the C function */
	switch(arraydata.arraytype) {
		// signed char
		case 'b' : {
			resultll = asum_signed_char(arraydata.arraylength, arraydata.array1.b, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromLongLong(resultll);
			break;
		}
		// unsigned char
		case 'B' : {
			resultull = asum_unsigned_char(arraydata.arraylength, arraydata.array1.B, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromUnsignedLongLong(resultull);
			break;
		}
		// signed short
		case 'h' : {
			resultll = asum_signed_short(arraydata.arraylength, arraydata.array1.h, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromLongLong(resultll);
			break;
		}
		// unsigned short
		case 'H' : {
			resultull = asum_unsigned_short(arraydata.arraylength, arraydata.array1.H, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromUnsignedLongLong(resultull);
			break;
		}
		// signed int
		case 'i' : {
			resultll = asum_signed_int(arraydata.arraylength, arraydata.array1.i, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromLongLong(resultll);
			break;
		}
		// unsigned int
		case 'I' : {
			resultull = asum_unsigned_int(arraydata.arraylength, arraydata.array1.I, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromUnsignedLongLong(resultull);
			break;
		}
		// signed long
		case 'l' : {
			resultll = asum_signed_long(arraydata.arraylength, arraydata.array1.l, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromLongLong(resultll);
			break;
		}
		// unsigned long
		case 'L' : {
			resultull = asum_unsigned_long(arraydata.arraylength, arraydata.array1.L, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromUnsignedLongLong(resultull);
			break;
		}
		// signed long long
		case 'q' : {
			resultll = asum_signed_long_long(arraydata.arraylength, arraydata.array1.q, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromLongLong(resultll);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultull = asum_unsigned_long_long(arraydata.arraylength, arraydata.array1.Q, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromUnsignedLongLong(resultull);
			break;
		}
		// float
		case 'f' : {
			resultd = asum_float(arraydata.arraylength, arraydata.array1.f, &errflag, arraydata.ignoreerrors, arraydata.nosimd);
			sumreturn = PyFloat_FromDouble(resultd);
			break;
		}
		// double
		case 'd' : {
			resultd = asum_double(arraydata.arraylength, arraydata.array1.d, &errflag, arraydata.ignoreerrors, arraydata.nosimd);
			sumreturn = PyFloat_FromDouble(resultd);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_asum(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_asum(arraydata);


	// Signal the errors.

	if (errflag == ARR_ERR_OVFL) {
		ErrMsgArithOverflowCalc();
		return NULL;
	}


	return sumreturn;

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(%(funclabel)s__doc__,
"asum \\n\\
_____________________________ \\n\\
\\n\\
Calculate the arithmetic sum of an array.  \\n\\
\\n\\
======================  ============================================== \\n\\
Equivalent to:          sum() \\n\\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \\n\\
Exceptions raised:      None \\n\\
======================  ============================================== \\n\\
\\n\\
Call formats: \\n\\
\\n\\
  result = %(funclabel)s(array) \\n\\
  result = %(funclabel)s(array, maxlen=y) \\n\\
  result = %(funclabel)s(array, nosimd=False) \\n\\
  result = %(funclabel)s(array, matherrors=False) \\n\\
\\n\\
* array - The input data array to be examined. \\n\\
* maxlen - Limit the length of the array used. This must be a valid \\n\\
  positive integer. If a zero or negative length, or a value which is \\n\\
  greater than the actual length of the array is specified, this \\n\\
  parameter is ignored. \\n\\
* nosimd - If True, SIMD acceleration is disabled if present. \\n\\
  The default is False (SIMD acceleration is enabled if present). \\n\\
* matherrors - If True, checks for numerical errors including integer \\n\\
  overflow are ignored. \\n\\
* result - The sum of the array. \\n\\
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

# This selects the correct template according to the C data type.
ops_calls = {'b' : template_basic, 'B' : template_basic_u, 
	'h' : template_basic, 'H' : template_basic_u, 
	'i' : template_basic, 'I' : template_basic_u, 
	'l' : template_basic, 'L' : template_basic_u, 
	'q' : template_basic, 'Q' : template_basic_u, 
	'f' : floattemplate, 'd' : floattemplate}


simdvalues = {
'f' : {'simdattr' : 'v4sf', 'simdstoreattr' : 'v4sf', 'simdwidth' : 'FLOATSIMDSIZE', 'simdload' : '__builtin_ia32_loadups', 'simdstore' : '__builtin_ia32_storeups'},
'd' : {'simdattr' : 'v2df', 'simdstoreattr' : 'v2df', 'simdwidth' : 'DOUBLESIMDSIZE', 'simdload' : '__builtin_ia32_loadupd', 'simdstore' : '__builtin_ia32_storeupd'},
}

# The cast to use for floating point array types.
returnmodifier = {'b' : '', 'B' : '', 
	'h' : '', 'H' : '', 
	'i' : '', 'I' : '', 
	'l' : '', 'L' : '', 
	'q' : '', 'Q' : '', 
	'f' : '(double) ', 'd' : ''}


# ==============================================================================

funcname = "asum"

# ==============================================================================
# This outputs the non-SIMD version.
# Output the generated code.

# Output the functions which implement the individual non-SIMD 
# implementation functions.
filename = funcname + '.c'

with open(filename, 'w') as f:
	f.write(asum_head % {'funclabel' : funcname})

	# Each type of array.
	for arraycode in codegen_common.arraycodes:
		arraytype = codegen_common.arraytypes[arraycode]
		funcmodifier = arraytype.replace(' ', '_')

		# This template parameter is only required for SIMD operations.
		if arraycode in codegen_common.floatarrays:
			simdwidth = simdvalues[arraycode]['simdwidth']
		else:
			simdwidth = ''

		# Select the implementation template for the current data type.
		optemplate = ops_calls[arraycode]

		# Write out the calculation source code. 
		f.write(optemplate % {'arraycode' : arraycode, 
					'arraytype' : arraytype, 
					'funcmodifier' : funcmodifier, 
					'returnmodifier' : returnmodifier[arraycode],
					'simdwidth' : simdwidth})

	# Write out the boilerplate at the end.
	f.write(asum_params % {'funclabel' : funcname})


# ==============================================================================
# This outputs the SIMD version.

# The original date of the SIMD C code.
simdcodedate = '05-May-2017'
simdfilename = '_simd_x86'

# This outputs the SIMD version.

outputlist = []


# This provides the description in the header of the file.
maindescription = 'Calculate the %s of values in an array.' % funcname

# Output the generated code.
for arraycode in codegen_common.floatarrays:

	arraytype = codegen_common.arraytypes[arraycode]

	outputlist.append(simdsupport % {'arraycode' : arraycode, 
				'arraytype' : arraytype, 
				'funcmodifier' : arraytype.replace(' ', '_'), 
				'returnmodifier' : returnmodifier[arraycode],
				'simdattr' : simdvalues[arraycode]['simdattr'],
				'simdwidth' : simdvalues[arraycode]['simdwidth'],
				'simdload' : simdvalues[arraycode]['simdload'],
				'simdstore' : simdvalues[arraycode]['simdstore'],
				})



# This outputs the SIMD version.
codegen_common.OutputSourceCode(funcname + simdfilename + '.c', outputlist, 
	maindescription, 
	codegen_common.SIMDDescription, 
	simdcodedate,
	'', ['simddefs'])


# Output the .h header file.
headedefs = codegen_common.GenSIMDCHeaderText(outputlist, funcname)

# Write out the file.
codegen_common.OutputCHeader(funcname + simdfilename + '.h', headedefs, 
	maindescription, 
	codegen_common.SIMDDescription, 
	simdcodedate)

# ==============================================================================

