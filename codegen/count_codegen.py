#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for count.
# Language: Python 3.4
# Date:     10-Jun-2014
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
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s startvalue, %(arraytype)s stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	%(arraytype)s increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}
"""


# ==============================================================================

outputlist = []

funcname = 'count'
filename = funcname + '_common'

maindescription = 'Fill an array with a series of values.'

# The original date of the platform independent C code.
ccodedate = '04-May-2014'


# ==============================================================================

# Output the generated code.
for funtypes in codegen_common.arraycodes:
	arraytype = codegen_common.arraytypes[funtypes]
	outputlist.append(template % {'arraytype' : arraytype, 
		'funcmodifier' : arraytype.replace(' ', '_')})


# ==============================================================================

# Write out the actual code.
codegen_common.OutputSourceCode(filename + '.c', outputlist, 
	maindescription, 
	codegen_common.PlatformIndependentDescr, 
	ccodedate, 
	funcname, [])

# ==============================================================================

# Output the .h header file. 
headedefs = codegen_common.GenCHeaderText(outputlist, funcname)

# Write out the file.
codegen_common.OutputCHeader(filename + '.h', headedefs, 
	maindescription, 
	codegen_common.PlatformIndependentDescr, 
	ccodedate)

# ==============================================================================
