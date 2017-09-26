#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for takewhile.
# Language: Python 3.4
# Date:     18-Jun-2014
#
###############################################################################
#
#   Copyright 2014 - 2017    Michael Griffin    <m12.griffin@gmail.com>
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

template_start = """
/*--------------------------------------------------------------------------- */
/* opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_%(funcmodifier)s(signed int opcode, Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s *dataout, %(arraytype)s param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
"""


template_end = """	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */
"""

# The basic template for each operator.
op_template = """		// %(opcodename)s
		case OP_%(oplabel)s: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] %(compare_ops)s param1)) {
					return index;
				}
				dataout[index] = data[index];
			}
			return index;
		}
"""


# ==============================================================================

outputlist = []

funcname = 'takewhile'
filename = funcname + '_common'

maindescription = 'Copy values from an array, stopping when a condition fails.'

# The original date of the platform independent C code.
ccodedate = '10-May-2014'


# ==============================================================================

# Read in the op codes.
oplist = codegen_common.ReadCSVData('arrayfunc.csv')

# Filter out
compops = [x for x in oplist if x['compare_ops'] != '']

# ==============================================================================

# Output the generated code.
for funtypes in codegen_common.arraycodes:
	arraytype = codegen_common.arraytypes[funtypes]
	outputlist.append(template_start % {'arraytype' : arraytype, 
		'funcmodifier' : arraytype.replace(' ', '_')})

	for ops in compops:
		testop = {'oplabel' : ops['opcodename'].replace(' ', '_').upper()}
		testop.update(ops)
		outputlist.append(op_template % testop)

	outputlist.append(template_end)

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
