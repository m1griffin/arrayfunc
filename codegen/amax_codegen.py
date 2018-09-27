#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for amax.
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

nosimdtemplate = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
%(arraytype)s amax_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	%(arraytype)s maxfound;

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return maxfound;
}
/*--------------------------------------------------------------------------- */

"""

# ==============================================================================

simdtemplate = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
%(arraytype)s amax_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	%(arraytype)s maxfound;


#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		return amax_%(funcmodifier)s_simd(arraylen, data);
	}
#endif

	maxfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return maxfound;
}
/*--------------------------------------------------------------------------- */

"""


# ==============================================================================

template_simdsupport = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The maximum value found.
*/
#ifdef AF_HASSIMD
%(arraytype)s amax_%(funcmodifier)s_simd(Py_ssize_t arraylen, %(arraytype)s *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	%(arraytype)s maxfound;

	%(arraytype)s maxvals[%(simdwidth)s];
	%(simdattr)s maxslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Initialise the comparison values.
	maxslice = (%(simdattr)s) %(simdload)s(%(simdcast)sdata);

	// Use SIMD.
	for(x = %(simdwidth)s; x < alignedlength; x += %(simdwidth)s) {
		dataslice = (%(simdattr)s) %(simdload)s(%(simdcast)s&data[x]);
		maxslice = %(simdop)s (maxslice, dataslice);
	}

	// Find the max within the slice.
	%(simdstore)s(%(simdcast)smaxvals, (%(simdstoreattr)s) maxslice);
	maxfound = maxvals[0];
	for (y = 1; y < %(simdwidth)s; y++) {
		if (maxvals[y] > maxfound) {
			maxfound = maxvals[y];
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		if (data[x] > maxfound) {
			maxfound = data[x];
		}
	}

	return maxfound;
}
#endif
/*--------------------------------------------------------------------------- */

"""


# ==============================================================================

simdvalues = {
'b' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v16qi', 'simdstoreattr' : 'v16qi', 'simdwidth' : 'CHARSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu', 'simdop' : '__builtin_ia32_pmaxsb128', 'simdstore' : '__builtin_ia32_storedqu'},
'B' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v16qi', 'simdstoreattr' : 'v16qi', 'simdwidth' : 'CHARSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu', 'simdop' : '__builtin_ia32_pmaxub128', 'simdstore' : '__builtin_ia32_storedqu'},
'h' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v8hi', 'simdstoreattr' : 'v16qi', 'simdwidth' : 'SHORTSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu', 'simdop' : '__builtin_ia32_pmaxsw128', 'simdstore' : '__builtin_ia32_storedqu'},
'H' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v8hi', 'simdstoreattr' : 'v16qi', 'simdwidth' : 'SHORTSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu', 'simdop' : '__builtin_ia32_pmaxuw128', 'simdstore' : '__builtin_ia32_storedqu'},
'i' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v4si', 'simdstoreattr' : 'v16qi', 'simdwidth' : 'INTSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu', 'simdop' : '__builtin_ia32_pmaxsd128', 'simdstore' : '__builtin_ia32_storedqu'},
'I' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v4si', 'simdstoreattr' : 'v16qi', 'simdwidth' : 'INTSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu', 'simdop' : '__builtin_ia32_pmaxud128', 'simdstore' : '__builtin_ia32_storedqu'},
'l' : {'hassimd' : False},
'L' : {'hassimd' : False},
'q' : {'hassimd' : False},
'Q' : {'hassimd' : False},
'f' : {'hassimd' : True, 'simdcast' : '', 'simdattr' : 'v4sf', 'simdstoreattr' : 'v4sf', 'simdwidth' : 'FLOATSIMDSIZE', 'simdload' : '__builtin_ia32_loadups', 'simdop' : '__builtin_ia32_maxps', 'simdstore' : '__builtin_ia32_storeups'},
'd' : {'hassimd' : True, 'simdcast' : '', 'simdattr' : 'v2df', 'simdstoreattr' : 'v2df', 'simdwidth' : 'DOUBLESIMDSIZE', 'simdload' : '__builtin_ia32_loadupd', 'simdop' : '__builtin_ia32_maxpd', 'simdstore' : '__builtin_ia32_storeupd'},
}

# ==============================================================================

outputlist = []

funcname = 'amax'
filename = funcname + '_common'

simdfilename = 'amax_simd_x86'

maindescription = 'Find the maximum value in an array.'

# The original date of the platform independent C code.
ccodedate = '04-May-2014'

# The original date of the SIMD C code.
simdcodedate = '01-May-2017'


# ==============================================================================

# This outputs the non-SIMD version.
# Output the generated code.
for funtypes in codegen_common.arraycodes:
	arraytype = codegen_common.arraytypes[funtypes]
	datavals = {'arraytype' : arraytype, 
		'funcmodifier' : arraytype.replace(' ', '_'),
		'arraycode' : funtypes}

	if simdvalues[funtypes]['hassimd']:
		template = simdtemplate
		datavals.update(simdvalues[funtypes])
	else:
		template = nosimdtemplate

	outputlist.append(template % datavals)


# Write out the actual code.
codegen_common.OutputSourceCode(filename + '.c', outputlist, 
	maindescription, 
	codegen_common.PlatformIndependentDescr, 
	ccodedate, 
	funcname, ['simddefs', 'simdmacromsg'])


# ==============================================================================

# Output the .h header file. 
headedefs = codegen_common.GenCHeaderText(outputlist, funcname)

# Write out the file.
codegen_common.OutputCHeader(filename + '.h', headedefs, 
	maindescription, 
	codegen_common.PlatformIndependentDescr, 
	ccodedate)

# ==============================================================================


outputlist = []

# This outputs the SIMD version.
# Output the generated code.
for funtypes in codegen_common.arraycodes:
	if simdvalues[funtypes]['hassimd']:
		arraytype = codegen_common.arraytypes[funtypes]
		datavals = {'arraytype' : arraytype, 
			'funcmodifier' : arraytype.replace(' ', '_'),
			'arraycode' : funtypes}
		datavals.update(simdvalues[funtypes])

		outputlist.append(template_simdsupport % datavals)


# This outputs the SIMD version.
codegen_common.OutputSourceCode(simdfilename + '.c', outputlist, 
	maindescription, 
	codegen_common.SIMDDescription, 
	simdcodedate,
	'', ['simddefs', 'arrayops'])


# ==============================================================================

# Output the .h header file.
headedefs = codegen_common.GenSIMDCHeaderText(outputlist, funcname)

# Write out the file.
codegen_common.OutputCHeader(simdfilename + '.h', headedefs, 
	maindescription, 
	codegen_common.SIMDDescription, 
	simdcodedate)

# ==============================================================================

