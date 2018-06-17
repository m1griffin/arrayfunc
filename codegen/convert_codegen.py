#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for convert.
# Language: Python 3.4
# Date:     22-Jun-2014
#
###############################################################################
#
#   Copyright 2014 - 2015    Michael Griffin    <m12.griffin@gmail.com>
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

template_start = """
/*--------------------------------------------------------------------------- */
/* arraycode = The type code used by the destination array.
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

outputlist = []

funcname = 'convert'
filename = funcname + '_common'

maindescription = 'Convert arrays between data types.'

# The original date of the platform independent C code.
ccodedate = '08-May-2014'


# ==============================================================================



# Output the generated code.
for funtypes in codegen_common.arraycodes:
	arraytype = codegen_common.arraytypes[funtypes]


	outputlist.append(template_start % {'arraytype' : arraytype, 
		'funcmodifier' : arraytype.replace(' ', '_')})

	# Create the individual cases.
	for arraycode in codegen_common.arraycodes:

		# Get the appropriate limit value depending on the source and destination
		# array types. This has to be done differently from most array
		# functions because of the need to avoid integer overflow when
		# converting from floating point.
		if (funtypes in codegen_common.floatarrays) and (arraycode in codegen_common.maxguardvalue[funtypes]):
			maxvalue = codegen_common.maxguardvalue[funtypes][arraycode]
			minvalue = codegen_common.minguardvalue[funtypes][arraycode]
			if arraycode == 'Q':
				codetype = copyloop_float
			else:
				codetype = copyloop_floatint
		# All other conversion cases, where loss of resolution is not a problem.
		else: 
			maxvalue = codegen_common.maxvalue[arraycode]
			minvalue = codegen_common.minvalue[arraycode]

			# Select the type of template to use.
			# Both array types are the same.
			if arraycode == funtypes:
				codetype = copyloopsame
			# Convert double to float. This requires passing NaN and inf through.
			elif (funtypes == 'd') and (arraycode == 'f'):
				codetype = copyloop_doubletofloat
			# Float to integer. We have to do special checks for this because of NaN and inf.
			elif (funtypes in codegen_common.floatarrays) and (arraycode in codegen_common.intarrays):
				codetype = copyloop_floatint
			# No checking required because we know we cannot overflow.
			elif arraycode in convertsafe[funtypes]:
				codetype = copyloopnocheck

			# Source is signed and output is unsigned integer.
			elif (funtypes in codegen_common.signedint) and (arraycode in codegen_common.unsignedint):
				codetype = copyloop_signedint_to_unsigned

			# Unsigned integers.
			elif funtypes in codegen_common.unsignedint:
				codetype = copyloop_unsigned
			# Signed integers.
			else:
				codetype = copyloop_signed


		testop = {'arraytype' : codegen_common.arraytypes[arraycode],
			'arraycode' : arraycode,
			'maxvalue' : maxvalue,
			'minvalue' : minvalue}

		outputlist.append(codetype % testop)

	outputlist.append(template_end)


# ==============================================================================

# Write out the actual code.
codegen_common.OutputSourceCode(filename + '.c', outputlist, 
	maindescription, 
	codegen_common.PlatformIndependentDescr, 
	ccodedate, 
	funcname, ['float', 'guardbands', 'arrayparams_base'])

# ==============================================================================

# Output the .h header file. 
headedefs = codegen_common.GenCHeaderText(outputlist, funcname)

# Write out the file.
codegen_common.OutputCHeader(filename + '.h', headedefs, 
	maindescription, 
	codegen_common.PlatformIndependentDescr, 
	ccodedate)

# ==============================================================================



