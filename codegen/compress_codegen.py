#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for compress.
# Language: Python 3.4
# Date:     11-Jun-2014
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

# This is the template for each compress function.
template = """/*--------------------------------------------------------------------------- */
/* datalen = The length of the input array.
   data = The input data array.
   outlen = The length of the output array.
   dataout = The output data array.
   selectorlen = The length of the selector array.
   selector = The array of filter values.
   Returns a positive integer indicating the number of input elements 
         copied to the output array.
*/
Py_ssize_t compress_%(funcmodifier)s(Py_ssize_t datalen, %(arraytype)s *data, 
			Py_ssize_t outlen, %(arraytype)s *dataout, 
			Py_ssize_t selectorlen, %(arraytype)s *selector) { 

	// Array index counter. 
	Py_ssize_t index, outindex, selectorindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;
	selectorindex = 0;

	for(index = 0; index < datalen; index++) {
		// Check if the output index is within bounds.
		if (outindex >= outlen) {
			break;
		}
		// If we reach the end of the selector array, start again from the start.
		if (selectorindex >= selectorlen) {
			selectorindex = 0;
		}
		// Copy the data.
		if (selector[selectorindex]) {
			dataout[outindex] = data[index];
			outindex++;
		}
		// We need to advance the selector index for each input index.
		selectorindex++;
	}
	return outindex;
}
"""

endcomment = """/*--------------------------------------------------------------------------- */
"""

# ==============================================================================

outputlist = []

funcname = 'compress'
filename = funcname + '_common'

maindescription = 'Copy values from an array, using a selector array to filter values.'

# The original date of the platform independent C code.
ccodedate = '10-May-2014'


# ==============================================================================


# Output the generated code.
for funtypes in codegen_common.arraycodes:
	arraytype = codegen_common.arraytypes[funtypes]
	outputlist.append(template % {'arraytype' : arraytype, 
		'funcmodifier' : arraytype.replace(' ', '_')})

outputlist.append(endcomment)


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

