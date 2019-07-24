#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for convert.
# Language: Python 3.4
# Date:     22-Jun-2014
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

import codegen_common

# ==============================================================================

convert_head = """//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   %(funclabel)s.c
// Purpose:  Copy values from an array, using a selector array to filter values.
// Language: C
// Date:     08-May-2014.
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

#include <float.h>

#include "arrayerrs.h"

#include "arrayparams_base.h"

#include "convguardbands.h"
#include "arrayparams_convert.h"


/*--------------------------------------------------------------------------- */
"""

# ==============================================================================


# ==============================================================================

template_start = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraycode = The type code used by the destination array.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The converted output array.
   Return = 0 if converted OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int convert_%(funcmodifier)s(char arraycode, Py_ssize_t arraylen, %(arraytype)s *data, union dataarrays dataout) {

	// array index counter.
	Py_ssize_t x;

	switch(arraycode) {
"""

template_end = """	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;

}
/*--------------------------------------------------------------------------- */
"""

# ==============================================================================
# This copies data for cases where the input and output loops are different types and the input is signed data.
copyloop_signed = """
		// %(arraytype)s
		case '%(arraycode)s': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > %(maxvalue)s) || (data[x] < %(minvalue)s)) {
					return ARR_ERR_OVFL;
				}
				dataout.%(arraycode)s[x] = (%(arraytype)s) data[x];
			}
			return 0;
		}
"""


# This copies data for cases where the input is float or double and the output is int.
copyloop_floatint = """
		// %(arraytype)s
		case '%(arraycode)s': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > %(maxvalue)s) || (data[x] < %(minvalue)s) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.%(arraycode)s[x] = (%(arraytype)s) data[x];
			}
			return 0;
		}
"""


# This copies data for double to float. We have to check if the data is in range,
# but we need to let nan, inf, and -inf pass through.
copyloop_doubletofloat = """
		// %(arraytype)s
		case '%(arraycode)s': {
			for(x = 0; x < arraylen; x++) {
				// NaN, inf, and -inf must be passed through.
				if (isfinite(data[x]) && ((data[x] > %(maxvalue)s) || (data[x] < %(minvalue)s))) {
					return ARR_ERR_OVFL;
				}
				dataout.%(arraycode)s[x] = (%(arraytype)s) data[x];
			}
			return 0;
		}
"""


# This copies data for cases where float or double must be converted to integer
# arrays where the integer precision is greater than the floating point precision.
copyloop_float = """
		// %(arraytype)s
		case '%(arraycode)s': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > %(maxvalue)s) || (data[x] < %(minvalue)s) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.%(arraycode)s[x] = (%(arraytype)s) data[x];
			}
			return 0;
		}
"""


# This copies data for cases where the input and output loops are different types and the input is unsigned data.
copyloop_unsigned = """
		// %(arraytype)s
		case '%(arraycode)s': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > %(maxvalue)s) {
					return ARR_ERR_OVFL;
				}
				dataout.%(arraycode)s[x] = (%(arraytype)s) data[x];
			}
			return 0;
		}
"""


# This copies data for cases where the output is an unsigned integer and the input is signed data.
copyloop_signedint_to_unsigned = """
		// %(arraytype)s
		case '%(arraycode)s': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < %(minvalue)s) {
					return ARR_ERR_OVFL;
				}
				dataout.%(arraycode)s[x] = (%(arraytype)s) data[x];
			}
			return 0;
		}
"""


# This copies data for cases where the input and output loops are the same type.
copyloopsame = """
		// %(arraytype)s
		case '%(arraycode)s': {
			for(x = 0; x < arraylen; x++) {
				dataout.%(arraycode)s[x] = data[x];
			}
			return 0;
		}
"""

# This copies data for cases where the input range is smaller than the output size.
copyloopnocheck = """
		// %(arraytype)s
		case '%(arraycode)s': {
			for(x = 0; x < arraylen; x++) {
				dataout.%(arraycode)s[x] = (%(arraytype)s) data[x];
			}
			return 0;
		}
"""

# ==============================================================================




convert_params = """
/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = 0;

	// This is used to hold the parsed parameters.
	struct args_params_convert arraydata = ARGSINIT_CONVERT;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_convert(self, args, keywds, "%(funclabel)s");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}


	// The length of the data array.
	if (arraydata.arraylength < 1) {
		// Release the buffers. 
		releasebuffers_convert(arraydata);
		ErrMsgArrayLengthErr();
		return NULL;
	}



	/* Call the C function */
	switch(arraydata.arraytype1) {
		// signed char
		case 'b' : {
			resultcode = convert_signed_char(arraydata.arraytype2, arraydata.arraylength, arraydata.array1.b, arraydata.array2);
			break;
		}
		// unsigned char
		case 'B' : {
			resultcode = convert_unsigned_char(arraydata.arraytype2, arraydata.arraylength, arraydata.array1.B, arraydata.array2);
			break;
		}
		// signed short
		case 'h' : {
			resultcode = convert_signed_short(arraydata.arraytype2, arraydata.arraylength, arraydata.array1.h, arraydata.array2);
			break;
		}
		// unsigned short
		case 'H' : {
			resultcode = convert_unsigned_short(arraydata.arraytype2, arraydata.arraylength, arraydata.array1.H, arraydata.array2);
			break;
		}
		// signed int
		case 'i' : {
			resultcode = convert_signed_int(arraydata.arraytype2, arraydata.arraylength, arraydata.array1.i, arraydata.array2);
			break;
		}
		// unsigned int
		case 'I' : {
			resultcode = convert_unsigned_int(arraydata.arraytype2, arraydata.arraylength, arraydata.array1.I, arraydata.array2);
			break;
		}
		// signed long
		case 'l' : {
			resultcode = convert_signed_long(arraydata.arraytype2, arraydata.arraylength, arraydata.array1.l, arraydata.array2);
			break;
		}
		// unsigned long
		case 'L' : {
			resultcode = convert_unsigned_long(arraydata.arraytype2, arraydata.arraylength, arraydata.array1.L, arraydata.array2);
			break;
		}
		// signed long long
		case 'q' : {
			resultcode = convert_signed_long_long(arraydata.arraytype2, arraydata.arraylength, arraydata.array1.q, arraydata.array2);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultcode = convert_unsigned_long_long(arraydata.arraytype2, arraydata.arraylength, arraydata.array1.Q, arraydata.array2);
			break;
		}
		// float
		case 'f' : {
			resultcode = convert_float(arraydata.arraytype2, arraydata.arraylength, arraydata.array1.f, arraydata.array2);
			break;
		}
		// double
		case 'd' : {
			resultcode = convert_double(arraydata.arraytype2, arraydata.arraylength, arraydata.array1.d, arraydata.array2);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_convert(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_convert(arraydata);


	// Signal the errors.
	switch (resultcode) {
		case ARR_ERR_INVALIDOP : {
			ErrMsgConversionNotValidforthisType();
			return NULL;
		}
		case ARR_ERR_OVFL : {
			ErrMsgArithOverflowCalc();
			return NULL;
		}
		case ARR_ERR_VALUE_ERR : {
			ErrMsgNaNError();
			return NULL;
		}
		case ARR_ERR_PLATFORM : {
			ErrMsgOperatorNotValidforthisPlatform();
			return NULL;
		}
	}


	// Return NONE.
	Py_RETURN_NONE;


}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(%(funclabel)s__doc__,
"%(funclabel)s \\n\\
_____________________________ \\n\\
\\n\\
Convert arrays between data types. The data will be converted into the \\n\\
form required by the output array. If any values in the input array are \\n\\
outside the range of the output array type, an exception will be \\n\\
raised. When floating point values are converted to integers, the value \\n\\
will be truncated. \\n\\
\\n\\
======================  ============================================== \\n\\
Equivalent to:          [x for x in inputarray] \\n\\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \\n\\
======================  ============================================== \\n\\
\\n\\
Call formats: \\n\\
\\n\\
  convert(inparray, outparray) \\n\\
  convert(inparray, outparray, maxlen=y) \\n\\
\\n\\
* inparray - The input data array to be filtered. \\n\\
* outparray - The output array. \\n\\
* maxlen - Limit the length of the array used. This must be a valid \\n\\
  positive integer. If a zero or negative length, or a value which is \\n\\
  greater than the actual length of the array is specified, this \\n\\
  parameter is ignored. \\n\\
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


# List the types which can be converted to without needing to check for overflow.
# The key is the source, and the list of values is the destination.
convertsafe = {
	'b' : ('b', 'h', 'i', 'l', 'q', 'f', 'd'),
	'B' : ('B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd'),
	'h' : ('h', 'i', 'l', 'q', 'f', 'd'),
	'H' : ('H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd'),
	'i' : ('i', 'l', 'q', 'f', 'd'),
	'I' : ('I', 'l', 'L', 'q', 'Q', 'f', 'd'),
	'l' : ('l', 'q', 'f', 'd'),
	'L' : ('I', 'l', 'L', 'q', 'Q', 'f', 'd'),
	'q' : ('q', 'f', 'd'),
	'Q' : ('Q', 'f', 'd'),
	'f' : ('f', 'd'),
	'd' : ('d')
}

# ==============================================================================


funcname = 'convert'

filename = funcname + '.c'


with open(filename, 'w') as f:
	f.write(convert_head % {'funclabel' : funcname})

	# Each type of array.
	for arraycode in codegen_common.arraycodes:
		arraytype = codegen_common.arraytypes[arraycode]
		funcmodifier = arraytype.replace(' ', '_')

		f.write(template_start % {'arraytype' : arraytype, 
					'funcmodifier' : funcmodifier,
					'arraycode' : arraycode})


		# Create the individual cases for output targets.
		for arraycodetarget in codegen_common.arraycodes:

			# Get the appropriate limit value depending on the source and destination
			# array types. This has to be done differently from most array
			# functions because of the need to avoid integer overflow when
			# converting from floating point.
			if (arraycode in codegen_common.floatarrays) and (arraycodetarget in codegen_common.maxguardvalue[arraycode]):
				maxvalue = codegen_common.maxguardvalue[arraycode][arraycodetarget]
				minvalue = codegen_common.minguardvalue[arraycode][arraycodetarget]
				if arraycodetarget == 'Q':
					codetype = copyloop_float
				else:
					codetype = copyloop_floatint
			# All other conversion cases, where loss of resolution is not a problem.
			else: 
				maxvalue = codegen_common.maxvalue[arraycodetarget]
				minvalue = codegen_common.minvalue[arraycodetarget]

				# Select the type of template to use.
				# Both array types are the same.
				if arraycodetarget == arraycode:
					codetype = copyloopsame
				# Convert double to float. This requires passing NaN and inf through.
				elif (arraycode == 'd') and (arraycodetarget == 'f'):
					codetype = copyloop_doubletofloat
				# Float to integer. We have to do special checks for this because of NaN and inf.
				elif (arraycode in codegen_common.floatarrays) and (arraycodetarget in codegen_common.intarrays):
					codetype = copyloop_floatint
				# No checking required because we know we cannot overflow.
				elif arraycodetarget in convertsafe[arraycode]:
					codetype = copyloopnocheck

				# Source is signed and output is unsigned integer.
				elif (arraycode in codegen_common.signedint) and (arraycodetarget in codegen_common.unsignedint):
					codetype = copyloop_signedint_to_unsigned

				# Unsigned integers.
				elif arraycode in codegen_common.unsignedint:
					codetype = copyloop_unsigned
				# Signed integers.
				else:
					codetype = copyloop_signed

			datavals = {'arraytype' : codegen_common.arraytypes[arraycodetarget],
				'arraycode' : arraycodetarget,
				'maxvalue' : maxvalue,
				'minvalue' : minvalue}

			f.write(codetype % datavals)


		# Close off the end of the function.
		f.write(template_end)


	#####

	# The program entry point and parameter parsing and code.
	f.write(convert_params % {'funclabel' : funcname})

# ==============================================================================
