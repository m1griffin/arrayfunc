#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for asum.
# Language: Python 3.4
# Date:     13-May-2014
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


# Template for the asum functions with overflow for signed integer.
template_basic = """/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   disableovfl = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
%(sumtype)s asum_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, signed int *errflag, signed int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	%(sumtype)s partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (disableovfl) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((partialsum > 0) && (data[x] > (LONG_MAX - partialsum))) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			if ((partialsum < 0) && (data[x] < (LONG_MIN - partialsum))) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			partialsum = partialsum + data[x];
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */

"""

# ==============================================================================


# Template for the asum functions with overflow for unsigned integer.
template_basic_u = """/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   disableovfl = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
%(sumtype)s asum_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, signed int *errflag, signed int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	%(sumtype)s partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (disableovfl) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
			if (data[x] > (ULONG_MAX - partialsum)) { 
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
			partialsum = partialsum + data[x];
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */

"""

# ==============================================================================

# This is used for floating point SIMD versions only.
simdtemplate = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   disableovfl = If true, arithmetic overflow checking is disabled.
   nosimd = If true, disable SIMD.
   Returns: The sum of the array.
*/
%(sumtype)s asum_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, signed int *errflag, signed int disableovfl, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	%(sumtype)s partialsum = 0.0;


#ifdef AF_HASSIMD
	// SIMD version. Only use this if overflow checking is disabled.
	if (disableovfl && !nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		return asum_%(funcmodifier)s_simd(arraylen, data);
	}
#endif


	*errflag = 0;
	// Overflow checking disabled.
	if (disableovfl) {
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for(x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
			if (!isfinite(partialsum)) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */
"""

# ==============================================================================

# This is used for floating point SIMD versions only.
simdsupport = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   disableovfl = If true, arithmetic overflow checking is disabled.
   nosimd = If true, disable SIMD.
   Returns: The sum of the array.
*/
#ifdef AF_HASSIMD
%(sumtype)s asum_%(funcmodifier)s_simd(Py_ssize_t arraylen, %(arraytype)s *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	%(sumtype)s partialsum = 0.0;

	%(sumtype)s sumvals[%(simdwidth)s];
	%(simdattr)s sumslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Initialise the sum values.
	sumslice = (%(simdattr)s) %(simdload)s(data);

	// Use SIMD.
	for(x = %(simdwidth)s; x < alignedlength; x += %(simdwidth)s) {
		dataslice = (%(simdattr)s) %(simdload)s(&data[x]);
		sumslice = %(simdop)s (sumslice, dataslice);
	}

	// Add up the values within the slice.
	%(simdstore)s(sumvals, (%(simdattr)s) sumslice);
	for (y = 0; y < %(simdwidth)s; y++) {
		partialsum = partialsum + sumvals[y];
	}

	// Add the values within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}


	return partialsum;
}
#endif
/*--------------------------------------------------------------------------- */
"""


# ==============================================================================

simdvalues = {
'f' : {'simdattr' : 'v4sf', 'simdstoreattr' : 'v4sf', 'simdwidth' : 'FLOATSIMDSIZE', 'simdload' : '__builtin_ia32_loadups', 'simdop' : '__builtin_ia32_addps', 'simdstore' : '__builtin_ia32_storeups'},
'd' : {'simdattr' : 'v2df', 'simdstoreattr' : 'v2df', 'simdwidth' : 'DOUBLESIMDSIZE', 'simdload' : '__builtin_ia32_loadupd', 'simdop' : '__builtin_ia32_addpd', 'simdstore' : '__builtin_ia32_storeupd'},
}


# This defines how python array codes translate to C data types for summation.
# Integer types are split into signed and unsigned longs.
sumtype = {'b' : 'signed long', 'B' : 'unsigned long', 
	'h' : 'signed long', 'H' : 'unsigned long', 
	'i' : 'signed long', 'I' : 'unsigned long', 
	'l' : 'signed long', 'L' : 'unsigned long', 
	'q' : 'signed long long', 'Q' : 'unsigned long long', 
	'f' : 'float', 'd' : 'double'}


# ==============================================================================

outputlist = []

funcname = 'asum'
filename = funcname + '_common'

simdfilename = 'asum_simd_x86'

maindescription = 'Sum all the values in an array.'

# The original date of the platform independent C code.
ccodedate = '15-May-2014'

# The original date of the SIMD C code.
simdcodedate = '05-May-2017'


# ==============================================================================


# Output the generated code for integer types.
for funtypes in codegen_common.arraycodes:
	arraytype = codegen_common.arraytypes[funtypes]

	datavals = {'funcmodifier' : arraytype.replace(' ', '_'), 
		'arraytype' : arraytype,
		'sumtype' : sumtype[funtypes],
		'arraycode' : funtypes}


	# The type of overflow check we do depends on the array type.
	if funtypes in codegen_common.signedint:
		codetemplate = template_basic
	elif funtypes in codegen_common.unsignedint:
		codetemplate = template_basic_u
	elif funtypes in codegen_common.floatarrays:
		codetemplate = simdtemplate
		datavals.update(simdvalues[funtypes])


	# Basic template start.
	outputlist.append(codetemplate % datavals)

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


outputlist = []

# Output the generated code for floating point types.
for funtypes in codegen_common.floatarrays:
	arraytype = codegen_common.arraytypes[funtypes]

	datavals = {'funcmodifier' : arraytype.replace(' ', '_'), 
		'arraytype' : arraytype,
		'sumtype' : sumtype[funtypes],
		'arraycode' : funtypes}

	# Use the SIMD values.
	datavals.update(simdvalues[funtypes])

	# Use the SIMD template.
	outputlist.append(simdsupport % datavals)


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

