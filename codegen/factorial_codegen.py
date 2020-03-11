#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for factorial.
# Language: Python 3.4
# Date:     18-Mar-2018
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

# ==============================================================================

uniops_head = """//------------------------------------------------------------------------------
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
#include "arrayparams_one.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// Calculate factorials.
// We are making some assumptions here about the sizes of integers.
// Instead of calculating factorials using a loop, we create a series of 
// look-up tables. This seems to be about 5 to 20 times faster than using
// a loop and test method.


// Factorial data.

// The default value to return when a factorial calculation was in error.
#define DEFAULT_FACT 0

// Signed and unsigned chars.
#define MAX_SC_FACT 5
signed char fact_sc_data[] = {1, 1, 2, 6, 24, 120};
#define MAX_USC_FACT 5
unsigned char fact_usc_data[] = {1, 1, 2, 6, 24, 120};

// Signed and unsigned shorts.
#define MAX_SS_FACT 7
signed short fact_ss_data[] = {1, 1, 2, 6, 24, 120, 720, 5040};
#define MAX_USS_FACT 8
unsigned short fact_uss_data[] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320};


// Signed and unsigned ints.
#define MAX_SI_FACT 12
signed int fact_si_data[] = {1, 1, 2, 6, 24, 120, 720, 5040, 5040, 40320, 362880, 3628800, 39916800, 479001600};
#define MAX_USI_FACT 12
unsigned int fact_usi_data[] = {1, 1, 2, 6, 24, 120, 720, 5040, 5040, 40320, 362880, 3628800, 39916800, 479001600};


// Signed and unsigned long.
// Check if long integer is 8 bytes.
#if LONG_MAX == 9223372036854775807

#define MAX_SL_FACT 20
signed long fact_sl_data[] = {1, 1, 2, 6, 24, 120, 720, 5040, 5040, 40320, 362880, 
				3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 
				20922789888000, 355687428096000, 6402373705728000, 121645100408832000,
				2432902008176640000};
#define MAX_USL_FACT 20
unsigned long fact_usl_data[] = {1, 1, 2, 6, 24, 120, 720, 5040, 5040, 40320, 362880, 
				3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 
				20922789888000, 355687428096000, 6402373705728000, 121645100408832000,
				2432902008176640000};

// Long integers are assumed to be 4 bytes.
#else

#define MAX_SL_FACT 12
signed long fact_sl_data[] = {1, 1, 2, 6, 24, 120, 720, 5040};
#define MAX_USL_FACT 12
unsigned long fact_usl_data[] = {1, 1, 2, 6, 24, 120, 720, 5040, 5040, 40320, 362880, 3628800, 39916800, 479001600};

#endif // End for long integer.

#define MAX_SLL_FACT 20
signed long long fact_sll_data[] = {1, 1, 2, 6, 24, 120, 720, 5040, 5040, 40320, 362880, 
				3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 
				20922789888000, 355687428096000, 6402373705728000, 121645100408832000,
				2432902008176640000};
#define MAX_USLL_FACT 20
unsigned long long fact_usll_data[] = {1, 1, 2, 6, 24, 120, 720, 5040, 5040, 40320, 362880, 
				3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 
				20922789888000, 355687428096000, 6402373705728000, 121645100408832000,
				2432902008176640000};

/*--------------------------------------------------------------------------- */

"""

# ==============================================================================

# ==============================================================================


# Calculate factorial of a signed integer.
uniops_fac_intsigned = """
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int %(funclabel)s_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Factorial is not defined for negative values, and there is
	// a limit to the size of factorial that can be calculated.

	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > %(maxfact)s)) {
					dataout[x] = DEFAULT_FACT;
				} else {
					dataout[x] = %(factdata)s[data[x]];
				}
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > %(maxfact)s)) {
					data[x] = DEFAULT_FACT;
				} else {
					data[x] = %(factdata)s[data[x]];
				}
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > %(maxfact)s)) {
					return ARR_ERR_OVFL;
				}
				dataout[x] = %(factdata)s[data[x]];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > %(maxfact)s)) {
					return ARR_ERR_OVFL;
				}
				data[x] = %(factdata)s[data[x]];
			}
		}
	}

	return ARR_NO_ERR;

}

"""

# Calculate factorial of an unsigned integer.
uniops_fac_intunsigned = """
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int %(funclabel)s_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Factorial is not defined for negative values, and there is
	// a limit to the size of factorial that can be calculated.

	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if (data[x] > %(maxfact)s) {
					dataout[x] = DEFAULT_FACT;
				} else {
					dataout[x] = %(factdata)s[data[x]];
				}
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > %(maxfact)s) {
					data[x] = DEFAULT_FACT;
				} else {
					data[x] = %(factdata)s[data[x]];
				}
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if (data[x] > %(maxfact)s) {
					return ARR_ERR_OVFL;
				}
				dataout[x] = %(factdata)s[data[x]];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > %(maxfact)s) {
					return ARR_ERR_OVFL;
				}
				data[x] = %(factdata)s[data[x]];
			}
		}
	}

	return ARR_NO_ERR;

}

"""


# ==============================================================================


# ==============================================================================

# This is the set of function calls used to call each operator function.
opscall = """
		// %(funcmodifier)s
		case '%(arraycode)s' : {
			resultcode = %(funclabel)s_%(funcmodifier)s(arraydata.arraylength, arraydata.array1.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}
"""



uniops_params = """

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
* maxlen - Limit the length of the array used. This must be a valid \\n\\
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


# ==============================================================================

# What C code definitions to use with factorial.
maxfact = {
	'b' : 'MAX_SC_FACT',
	'B' : 'MAX_USC_FACT',
	'h' : 'MAX_SS_FACT',
	'H' : 'MAX_USS_FACT',
	'i' : 'MAX_SI_FACT',
	'I' : 'MAX_USI_FACT',
	'l' : 'MAX_SL_FACT',
	'L' : 'MAX_USL_FACT',
	'q' : 'MAX_SLL_FACT',
	'Q' : 'MAX_USLL_FACT',
	'f' : '',
	'd' : ''
}

factdata = {
	'b' : 'fact_sc_data',
	'B' : 'fact_usc_data',
	'h' : 'fact_ss_data',
	'H' : 'fact_uss_data',
	'i' : 'fact_si_data',
	'I' : 'fact_usi_data',
	'l' : 'fact_sl_data',
	'L' : 'fact_usl_data',
	'q' : 'fact_sll_data',
	'Q' : 'fact_usll_data',
	'f' : '',
	'd' : ''
}

# ==============================================================================

# ==============================================================================

# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.

funclist = [x for x in oplist if x['c_code_template'] in ['template_factorial']]

# ==============================================================================


for func in funclist:

	# Create the source code based on templates.
	filename = func['funcname'] + '.c'
	with open(filename, 'w') as f:
		funcdata = {'funclabel' : func['funcname'], 'factdefs' : ''}


		f.write(uniops_head % funcdata)
		opscalltext = []


		# Check each array type. 
		for arraycode in codegen_common.intarrays:
			funcdata['funcmodifier'] = codegen_common.arraytypes[arraycode].replace(' ', '_')
			funcdata['arraytype'] = codegen_common.arraytypes[arraycode]
			funcdata['intmaxvalue'] = codegen_common.maxvalue[arraycode]
			funcdata['intminvalue'] = codegen_common.minvalue[arraycode]
			funcdata['maxfact'] = maxfact[arraycode]
			funcdata['factdata'] = factdata[arraycode]
			funcdata['copname'] = func['c_operator_i']


			if arraycode in codegen_common.unsignedint:
				 ops_calc = uniops_fac_intunsigned
			elif arraycode in codegen_common.signedint:
				 ops_calc = uniops_fac_intsigned
			else:
				print('Error - Unsupported array code.', arraycode)


			f.write(ops_calc % funcdata)

			# This is the call to the functions for this array type. This
			# is inserted into another template below.
			funcdata['arraycode'] = arraycode
			opscalltext.append(opscall % funcdata)


		supportedarrays = codegen_common.FormatDocsArrayTypes(func['arraytypes'])

		f.write(uniops_params % {'funclabel' : func['funcname'], 
				'opcodedocs' : func['opcodedocs'], 
				'supportedarrays' : supportedarrays,
				'matherrors' : ', '.join(func['matherrors'].split(',')),
				'opscall' : ''.join(opscalltext)})

# ==============================================================================






