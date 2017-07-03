#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for amin.
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
   Returns: The minimum value found.
*/
%(arraytype)s amin_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	%(arraytype)s minfound;

	minfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] < minfound) {
			minfound = data[x];
		}
	}

	return minfound;
}
/*--------------------------------------------------------------------------- */

"""


# ==============================================================================

simdtemplate = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The minimum value found.
*/
%(arraytype)s amin_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	%(arraytype)s minfound;


#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		return amin_%(funcmodifier)s_simd(arraylen, data);
	}
#endif

	minfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] < minfound) {
			minfound = data[x];
		}
	}

	return minfound;
}
/*--------------------------------------------------------------------------- */

"""

# ==============================================================================


template_simdsupport = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data arrays.
   data = The input data array.
   nosimd = If true, disable SIMD.
   Returns: The minimum value found.
*/
#ifdef AF_HASSIMD
%(arraytype)s amin_%(funcmodifier)s_simd(Py_ssize_t arraylen, %(arraytype)s *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	%(arraytype)s minfound;

	%(arraytype)s minvals[%(simdwidth)s];
	%(simdattr)s minslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Initialise the comparison values.
	minslice = (%(simdattr)s) %(simdload)s(%(simdcast)sdata);

	// Use SIMD.
	for(x = %(simdwidth)s; x < alignedlength; x += %(simdwidth)s) {
		dataslice = (%(simdattr)s) %(simdload)s(%(simdcast)s&data[x]);
		minslice = %(simdop)s (minslice, dataslice);
	}

	// Find the min within the slice.
	%(simdstore)s(%(simdcast)sminvals, (%(simdstoreattr)s) minslice);
	minfound = minvals[0];
	for (y = 1; y < %(simdwidth)s; y++) {
		if (minvals[y] < minfound) {
			minfound = minvals[y];
		}
	}

	// Get the min value within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		if (data[x] < minfound) {
			minfound = data[x];
		}
	}


	return minfound;
}
#endif
/*--------------------------------------------------------------------------- */

"""

# ==============================================================================

simdvalues = {
'b' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v16qi', 'simdstoreattr' : 'v16qi', 'simdwidth' : 'CHARSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu', 'simdop' : '__builtin_ia32_pminsb128', 'simdstore' : '__builtin_ia32_storedqu'},
'B' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v16qi', 'simdstoreattr' : 'v16qi', 'simdwidth' : 'CHARSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu', 'simdop' : '__builtin_ia32_pminub128', 'simdstore' : '__builtin_ia32_storedqu'},
'h' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v8hi', 'simdstoreattr' : 'v16qi', 'simdwidth' : 'SHORTSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu', 'simdop' : '__builtin_ia32_pminsw128', 'simdstore' : '__builtin_ia32_storedqu'},
'H' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v8hi', 'simdstoreattr' : 'v16qi', 'simdwidth' : 'SHORTSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu', 'simdop' : '__builtin_ia32_pminuw128', 'simdstore' : '__builtin_ia32_storedqu'},
'i' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v4si', 'simdstoreattr' : 'v16qi', 'simdwidth' : 'INTSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu', 'simdop' : '__builtin_ia32_pminsd128', 'simdstore' : '__builtin_ia32_storedqu'},
'I' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v4si', 'simdstoreattr' : 'v16qi', 'simdwidth' : 'INTSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu', 'simdop' : '__builtin_ia32_pminud128', 'simdstore' : '__builtin_ia32_storedqu'},
'l' : {'hassimd' : False},
'L' : {'hassimd' : False},
'q' : {'hassimd' : False},
'Q' : {'hassimd' : False},
'f' : {'hassimd' : True, 'simdcast' : '', 'simdattr' : 'v4sf', 'simdstoreattr' : 'v4sf', 'simdwidth' : 'FLOATSIMDSIZE', 'simdload' : '__builtin_ia32_loadups', 'simdop' : '__builtin_ia32_minps', 'simdstore' : '__builtin_ia32_storeups'},
'd' : {'hassimd' : True, 'simdcast' : '', 'simdattr' : 'v2df', 'simdstoreattr' : 'v2df', 'simdwidth' : 'DOUBLESIMDSIZE', 'simdload' : '__builtin_ia32_loadupd', 'simdop' : '__builtin_ia32_minpd', 'simdstore' : '__builtin_ia32_storeupd'},
}

# ==============================================================================

# This outputs the non-SIMD version.
with open('amin_code.txt', 'w') as f:
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

		f.write(template % datavals)


# This outputs the SIMD version.
with open('amin_simd_x86.txt', 'w') as f:
	# Output the generated code.
	for funtypes in codegen_common.arraycodes:
		if simdvalues[funtypes]['hassimd']:
			arraytype = codegen_common.arraytypes[funtypes]
			datavals = {'arraytype' : arraytype, 
				'funcmodifier' : arraytype.replace(' ', '_'),
				'arraycode' : funtypes}
			datavals.update(simdvalues[funtypes])

			f.write(template_simdsupport % datavals)
