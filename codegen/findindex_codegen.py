#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for findindex.
# Language: Python 3.4
# Date:     21-Jun-2014
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

# ==============================================================================

template_start = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the array index of the found item, 
	or a negative integer as an error code.
*/
Py_ssize_t findindex_%(funcmodifier)s(signed int opcode, Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
"""

# ==============================================================================


template_start_simd = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the array index of the found item, 
	or a negative integer as an error code.
*/
Py_ssize_t findindex_%(funcmodifier)s(signed int opcode, Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s param1, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t index; 


#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		return findindex_%(funcmodifier)s_simd(opcode, arraylen, data, param1);
	}
#endif

	switch(opcode) {
"""


# ==============================================================================

# The basic template for each operator.
op_template = """	// %(opcodename)s
	case OP_%(oplabel)s: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] %(compare_ops)s param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
"""

# ==============================================================================

template_start_simd_support = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 0 or a positive integer indicating the array index of the found item, 
	or a negative integer as an error code.
*/
#ifdef AF_HASSIMD
Py_ssize_t findindex_%(funcmodifier)s_simd(signed int opcode, Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex, alignedlength; 

	unsigned int y;

	%(simdattr)s compslice, dataslice, %(tmpslice)s;
	%(arraytype)s compvals[%(simdwidth)s];


	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param1;
	}
	compslice = (%(simdattr)s) %(simdload)s(%(simdcast)scompvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);


	switch(opcode) {
"""

# ==============================================================================


# The SIMD version.
op_simd_template = """		// %(opcodename)s
		case OP_%(oplabel)s: {
			// Use SIMD.
			for(index = 0; index < alignedlength; index += %(simdwidth)s) {
				dataslice = (%(simdattr)s) %(simdload)s(%(simdcast)s&data[index]);
				%(simd_op)s
				// Find the rough location.
				if (%(simd_comp)s) {
					// Home in on the exact location.
					for(fineindex = index; fineindex < alignedlength; fineindex++) {
						if (data[fineindex] %(compare_ops)s param1) {
							return fineindex;
						}
					}
				}
			}

			// Find the value within the left over elements at the end of the array.
			for(index = alignedlength; index < arraylen; index++) {
				if (data[index] %(compare_ops)s param1) {
					return index;
				}
			}

		return ARR_ERR_NOTFOUND;
		}
"""

# ==============================================================================


template_end = """	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

"""

template_end_simd = """	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
#endif
/*--------------------------------------------------------------------------- */

"""

# ==============================================================================


slicepad = '\t\t\t\t\t'

# These conduct the SIMD operations.
b_eqslice = 'eqslice = __builtin_ia32_pcmpeqb128(dataslice, compslice);'
b_gtslice = 'gtslice = __builtin_ia32_pcmpgtb128(dataslice, compslice);'


b_simdops = {
	'==' : b_eqslice,
	'>' : b_gtslice,
	'>=' : b_eqslice + '\n' + slicepad + b_gtslice,
	'<' : b_eqslice + '\n' + slicepad + b_gtslice,
	'<=' : b_gtslice,
	'!=' : b_eqslice
}

h_eqslice = 'eqslice = __builtin_ia32_pcmpeqw128(dataslice, compslice);'
h_gtslice = 'gtslice = __builtin_ia32_pcmpgtw128(dataslice, compslice);'

h_simdops = {
	'==' : h_eqslice,
	'>' : h_gtslice,
	'>=' : h_eqslice + '\n' + slicepad + h_gtslice,
	'<' : h_eqslice + '\n' + slicepad + h_gtslice,
	'<=' : h_gtslice,
	'!=' : h_eqslice
}

i_eqslice = 'eqslice = __builtin_ia32_pcmpeqd128(dataslice, compslice);'
i_gtslice = 'gtslice = __builtin_ia32_pcmpgtd128(dataslice, compslice);'

i_simdops = {
	'==' : i_eqslice,
	'>' : i_gtslice,
	'>=' : i_eqslice + '\n' + slicepad + i_gtslice,
	'<' : i_eqslice + '\n' + slicepad + i_gtslice,
	'<=' : i_gtslice,
	'!=' : i_eqslice
}


f_simdops = {
	'==' : 'resultslice = __builtin_ia32_cmpeqps(dataslice, compslice);',
	'>' : 'resultslice = __builtin_ia32_cmpgtps(dataslice, compslice);',
	'>=' : 'resultslice = __builtin_ia32_cmpgeps(dataslice, compslice);',
	'<' : 'resultslice = __builtin_ia32_cmpltps(dataslice, compslice);',
	'<=' : 'resultslice = __builtin_ia32_cmpleps(dataslice, compslice);',
	'!=' : 'resultslice = __builtin_ia32_cmpneqps(dataslice, compslice);'
}


d_simdops = {
	'==' : 'resultslice = __builtin_ia32_cmpeqpd(dataslice, compslice);',
	'>' : 'resultslice = __builtin_ia32_cmpgtpd(dataslice, compslice);',
	'>=' : 'resultslice = __builtin_ia32_cmpgepd(dataslice, compslice);',
	'<' : 'resultslice = __builtin_ia32_cmpltpd(dataslice, compslice);',
	'<=' : 'resultslice = __builtin_ia32_cmplepd(dataslice, compslice);',
	'!=' : 'resultslice = __builtin_ia32_cmpneqpd(dataslice, compslice);'
}



simdops = { 'b' : b_simdops, 'h' : h_simdops, 'i' : i_simdops, 'f' : f_simdops, 'd' : d_simdops}



# This provide the 'if' test conditions for SIMD.
simdcomp_i = {
	'==' : '__builtin_ia32_pmovmskb128((v16qi) eqslice) != 0x0000',
	'>' : '__builtin_ia32_pmovmskb128((v16qi) gtslice) != 0x0000',
	'>=' : '(__builtin_ia32_pmovmskb128((v16qi) gtslice) | __builtin_ia32_pmovmskb128((v16qi) eqslice)) != 0x0000',
	'<' : '(__builtin_ia32_pmovmskb128((v16qi) gtslice) | __builtin_ia32_pmovmskb128((v16qi) eqslice)) != 0xffff',
	'<=' : '__builtin_ia32_pmovmskb128((v16qi) gtslice) != 0xffff',
	'!=' : '__builtin_ia32_pmovmskb128((v16qi) eqslice) != 0xffff'
}

# For floating point.
simdcomp_f_val = '__builtin_ia32_pmovmskb128((v16qi) resultslice) != 0x0000'
simdcomp_f = {
	'==' : simdcomp_f_val,
	'>' : simdcomp_f_val,
	'>=' : simdcomp_f_val,
	'<' : simdcomp_f_val,
	'<=' : simdcomp_f_val,
	'!=' : simdcomp_f_val
}

simdcomp = {
	'b' : simdcomp_i,
	'h' : simdcomp_i,
	'i' : simdcomp_i,
	'f' : simdcomp_f,
	'd' : simdcomp_f
}


tmpintslice = 'eqslice, gtslice'
tmpfloatslice = 'resultslice'


simdvalues = {
'b' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v16qi', 'simdwidth' : 'CHARSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu', 'tmpslice' : tmpintslice},
'B' : {'hassimd' : False},
'h' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v8hi', 'simdwidth' : 'SHORTSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu', 'tmpslice' : tmpintslice},
'H' : {'hassimd' : False},
'i' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v4si', 'simdwidth' : 'INTSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu', 'tmpslice' : tmpintslice},
'I' : {'hassimd' : False},
'l' : {'hassimd' : False},
'L' : {'hassimd' : False},
'q' : {'hassimd' : False},
'Q' : {'hassimd' : False},
'f' : {'hassimd' : True, 'simdcast' : '', 'simdattr' : 'v4sf', 'simdwidth' : 'FLOATSIMDSIZE', 'simdload' : '__builtin_ia32_loadups', 'tmpslice' : tmpfloatslice},
'd' : {'hassimd' : True, 'simdcast' : '', 'simdattr' : 'v2df', 'simdwidth' : 'DOUBLESIMDSIZE', 'simdload' : '__builtin_ia32_loadupd', 'tmpslice' : tmpfloatslice},
}



# ==============================================================================

outputlist = []

funcname = 'findindex'
filename = funcname + '_common'

simdfilename = 'findindex_simd_x86'

maindescription = 'Returns the index of the first value in an array to meet the specified criteria.'

# The original date of the platform independent C code.
ccodedate = '10-May-2014'

# The original date of the SIMD C code.
simdcodedate = '10-May-2017'


# ==============================================================================

# Read in the op codes.
oplist = codegen_common.ReadCSVData('arrayfunc.csv')

# Filter out the compare operations.
compops = [x for x in oplist if x['compare_ops'] != '']

# ==============================================================================

# Output the generated code.
for funtypes in codegen_common.arraycodes:
	arraytype = codegen_common.arraytypes[funtypes]

	datavals = {'arraytype' : arraytype, 
				'funcmodifier' : arraytype.replace(' ', '_'),
				'arraycode' : funtypes}


	if simdvalues[funtypes]['hassimd']:
		start_temp = template_start_simd
		datavals.update(simdvalues[funtypes])
	else:
		start_temp = template_start


	# Start of function definition.
	outputlist.append(start_temp % datavals)


	# Write the non-SIMD code.
	# Each comparison operation.
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
	funcname, ['simdmacromsg'])


# ==============================================================================

# Output the .h header file. 
headedefs = codegen_common.GenCHeaderText(outputlist, funcname)

# Write out the file.
codegen_common.OutputCHeader(filename + '.h', headedefs, 
	maindescription, 
	codegen_common.PlatformIndependentDescr, 
	ccodedate)

# ==============================================================================

# This outputs the SIMD version.
outputlist = []

# SIMD version.

# Output the generated code.
for funtypes in codegen_common.arraycodes:
	if simdvalues[funtypes]['hassimd']:
		arraytype = codegen_common.arraytypes[funtypes]

		datavals = {'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'arraycode' : funtypes}

		datavals.update(simdvalues[funtypes])

		# Start of function definition.
		outputlist.append(template_start_simd_support % datavals)


		# Each comparison operation.
		for ops in compops:
			testop = {'oplabel' : ops['opcodename'].replace(' ', '_').upper()}
			testop.update(ops)
			testop.update(simdvalues[funtypes])
			opsymb = ops['compare_ops']
			testop.update({'simd_op' : simdops[funtypes][opsymb], 'simd_comp' : simdcomp[funtypes][opsymb]})
			outputlist.append(op_simd_template % testop)


		outputlist.append(template_end_simd)

# ==============================================================================

# This outputs the SIMD version.
codegen_common.OutputSourceCode(simdfilename + '.c', outputlist, 
	maindescription, 
	codegen_common.SIMDDescription, 
	simdcodedate,
	'', [])

# ==============================================================================

# Output the .h header file.
headedefs = codegen_common.GenSIMDCHeaderText(outputlist, funcname)

# Write out the file.
codegen_common.OutputCHeader(simdfilename + '.h', headedefs, 
	maindescription, 
	codegen_common.SIMDDescription, 
	simdcodedate)

# ==============================================================================
