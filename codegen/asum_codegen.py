#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for asum.
# Language: Python 3.4
# Date:     13-May-2014
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


# This defines how python array codes translate to C data types for summation.
# Integer types are split into signed and unsigned longs.
sumtype = {'b' : 'signed long', 'B' : 'unsigned long', 
	'h' : 'signed long', 'H' : 'unsigned long', 
	'i' : 'signed long', 'I' : 'unsigned long', 
	'l' : 'signed long', 'L' : 'unsigned long', 
	'q' : 'signed long long', 'Q' : 'unsigned long long', 
	'f' : 'float', 'd' : 'double'}

# Zero, in integer or floating point format.
zerotype = {'b' : '0', 'B' : '0', 
	'h' : '0', 'H' : '0', 
	'i' : '0', 'I' : '0', 
	'l' : '0', 'L' : '0', 
	'q' : '0', 'Q' : '0', 
	'f' : '0.0', 'd' : '0.0'}

# ==============================================================================

# Template for the asum functions with overflow.
template_basic = """/*--------------------------------------------------------------------------- */
%(array64start)s
/* arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   disableovfl = If true, arithmetic overflow checking is disabled.
	Returns: The sum of the array.
*/
%(sumtype)s asum_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, signed int *errflag, signed int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	%(sumtype)s partialsum = %(zero)s;

	*errflag = 0;
	// Overflow checking disabled.
	if (disableovfl) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
"""

# Overflow checking for unsigned integers.
uint_overflow = """			if (data[x] > (ULONG_MAX - partialsum)) { 
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			partialsum = partialsum + data[x];
"""

# Overflow checking for signed integers.
int_overflow = """			if ((partialsum > 0) && (data[x] > (LONG_MAX - partialsum))) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			if ((partialsum < 0) && (data[x] < (LONG_MIN - partialsum))) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			partialsum = partialsum + data[x];
"""

# Overflow checking for unsigned long long integers.
ulonglongint_overflow = """			if (data[x] > (ULLONG_MAX - partialsum)) { 
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			partialsum = partialsum + data[x];
"""

# Overflow checking for signed long long integers.
longlongint_overflow = """			if ((partialsum > 0) && (data[x] > (LLONG_MAX - partialsum))) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			if ((partialsum < 0) && (data[x] < (LLONG_MIN - partialsum))) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			partialsum = partialsum + data[x];
"""


# Overflow checking for floating point numbers.
float_overflow = """			partialsum = partialsum + data[x];
			if (!isfinite(partialsum)) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
"""

# Close off the function.
func_close = """		}
	}

	return partialsum;
}
%(array64end)s
/*--------------------------------------------------------------------------- */
"""

# ==============================================================================
# Overflow template format.
overflowstyles = {'b' : int_overflow, 'B' : uint_overflow, 
	'h' : int_overflow, 'H' : uint_overflow, 
	'i' : int_overflow, 'I' : uint_overflow, 
	'l' : int_overflow, 'L' : uint_overflow, 
	'q' : longlongint_overflow, 'Q' : ulonglongint_overflow, 
	'f' : float_overflow, 'd' : float_overflow}

# ==============================================================================


with open('asum_code.txt', 'w') as f:
	# Output the generated code.
	for funtypes in codegen_common.arraycodes:
		arraytype = codegen_common.arraytypes[funtypes]

		datavalues = {'funcmodifier' : arraytype.replace(' ', '_'), 
			'arraytype' : arraytype,
			'sumtype' : sumtype[funtypes],
			'zero' : zerotype[funtypes],
			'array64start' : codegen_common.array64start[funtypes]}

		
		# Basic template start.
		f.write(template_basic % datavalues)

		# The type of overflow check we do depends on the array type.
		ovfl_template = overflowstyles[funtypes]

		# Overflow code.
		f.write(ovfl_template)

		# Close off function.
		f.write(func_close % {'array64end' : codegen_common.array64end[funtypes]})


