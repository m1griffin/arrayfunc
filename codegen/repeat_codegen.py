#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for repeat.
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
   fillvalue = The value to fill the data array.
*/
void repeat_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}
%(array64end)s
"""


# ==============================================================================

with open('repeat_code.txt', 'w') as f:
	# Output the generated code.
	for funtypes in codegen_common.arraycodes:
		arraytype = codegen_common.arraytypes[funtypes]
		f.write(template % {'arraytype' : arraytype, 
		'funcmodifier' : arraytype.replace(' ', '_'),
			'array64start' : codegen_common.array64start[funtypes],
			'array64end' : codegen_common.array64end[funtypes]})

