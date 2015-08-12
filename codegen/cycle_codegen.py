#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for cycle.
# Language: Python 3.4
# Date:     11-Jun-2014
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

template = """
/*--------------------------------------------------------------------------- */
%(array64start)s
/* arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   Returns nothing (void).
*/
void cycle_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s startvalue, %(arraytype)s stopvalue, %(arraytype)s stepvalue) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	%(arraytype)s increment;

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}
%(array64end)s
"""


# ==============================================================================

with open('cycle_code.txt', 'w') as f:
	# Output the generated code.
	for funtypes in codegen_common.arraycodes:
		arraytype = codegen_common.arraytypes[funtypes]
		f.write(template % {'arraytype' : arraytype, 
			'funcmodifier' : arraytype.replace(' ', '_'),
			'array64start' : codegen_common.array64start[funtypes],
			'array64end' : codegen_common.array64end[funtypes]})

