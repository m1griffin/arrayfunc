#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for asum.
# Language: Python 3.6
# Date:     11-Jun-2014
#
###############################################################################
#
#   Copyright 2014 - 2022    Michael Griffin    <m12.griffin@gmail.com>
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

import itertools

import codegen_common

# ==============================================================================


asum_head = """//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   %(funclabel)s.c
// Purpose:  Calculate the %(funclabel)s of values in an array.
// Language: C
// Date:     15-Nov-2017.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2022    Michael Griffin    <m12.griffin@gmail.com>
//
//   Licensed under the Apache License, Version 2.0 (the "License");
//   you may not use this file except in compliance with the License.
//   You may obtain a copy of the License at
//
//       http://www.apache.org/licenses/LICENSE-2.0
//
//   Unless required by applicable law or agreed to in writing, software
//   distributed under the License is distributed on an "AS IS" BASIS,
//   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//   See the License for the specific language governing permissions and
//   limitations under the License.
//
//------------------------------------------------------------------------------

/*--------------------------------------------------------------------------- */
// This must be defined before "Python.h" in order for the pointers in the
// argument parsing functions to work properly. 
#define PY_SSIZE_T_CLEAN

#include "Python.h"

#include <limits.h>
#include <math.h>

#include "arrayerrs.h"

#include "arrayparams_base.h"

#include "arrayparams_asum.h"

#include "simddefs.h"

#include "asum_defs.h"

#ifdef AF_HASSIMD_X86
#include "asum_simd_x86.h"
#endif


#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
#include "arm_neon.h"
#endif

#ifdef AF_HASSIMD_ARMv7_32BIT
#include "asum_simd_armv7.h"
#endif

#ifdef AF_HASSIMD_ARM_AARCH64
#include "asum_simd_armv8.h"
#endif


/*--------------------------------------------------------------------------- */

/* These are for use with the integer versions of asum to optimize overflow
   checking performance by determining if an array is short enough that there
   is no risk that the accumulated sum may overflow when summing that data type. 
   Each value represents the maximum number of array elements for which it is 
   safe to skip overflow checks without risk of integer overflow even if the 
   array is full of the largest values for that type. 
   These are defined for known architectures as there seems to be no platform
   independent means of determining whether it is being compiled for 32 or 64
   bits. Array indexes are limited to a value related to Py_ssize_t. However
   Py_ssize_t will vary depending on whether Python is compiled for 32 or 64 
   bits. There is currently no means of determining the size of Py_ssize_t
   at compile time due to the way it is defined.
*/

#if defined( __x86_64__ ) ||  defined( __i386__ ) ||  defined( __ARM_64BIT_STATE ) ||  defined( __ARM_32BIT_STATE )

// 64 bit architectures.
#if defined( __x86_64__ ) ||  defined( __ARM_64BIT_STATE )

// Array codes B, b
#define CHARSKIPOVFLCHECK 72057594037927936LL
// Array codes H, h
#define SHORTSKIPOVFLCHECK 281474976710656LL
// Array codes I, i
#define INTSKIPOVFLCHECK 4294967296

#endif


// 32 bit architectures.
#if defined( __i386__ ) ||  defined( __ARM_32BIT_STATE )

// Array codes B, b
#define CHARSKIPOVFLCHECK 2147483648
// Array codes H, h
#define SHORTSKIPOVFLCHECK 2147483648
// Array codes I, i
#define INTSKIPOVFLCHECK 2147483648

#endif


#else
// Default values for unknown architectures which don't trigger the optimization. 

// Array codes B, b
#define CHARSKIPOVFLCHECK 0
// Array codes H, h
#define SHORTSKIPOVFLCHECK 0
// Array codes I, i
#define INTSKIPOVFLCHECK 0

#endif

// Skip overflow checks for b and B arrays.
#define charskipovflcheck(arraylen) (arraylen <= CHARSKIPOVFLCHECK)
// Skip overflow checks for h and H arrays.
#define shortskipovflcheck(arraylen) (arraylen <= SHORTSKIPOVFLCHECK)
// Skip overflow checks for i and I arrays.
#define intskipovflcheck(arraylen) (arraylen <= INTSKIPOVFLCHECK)


/*--------------------------------------------------------------------------- */
"""

# ==============================================================================

# ==============================================================================

# Integer overflow checks. These go in a common file to be included where necessary.
int_ovcheck = """

/*--------------------------------------------------------------------------- */

// Integer overflow checks.

// Unsigned integer - new value will cause an integer overflow.
#define loop_willoverflow_unsigned(val, partialsum) (val > (ULLONG_MAX - partialsum))

// Signed integer - new value will cause an integer overflow.
#define loop_willoverflow_signed(val, partialsum) (((partialsum > 0) && (val > (LLONG_MAX - partialsum))) || \
                                                   ((partialsum < 0) && (val < (LLONG_MIN - partialsum))))

/*--------------------------------------------------------------------------- */

"""

# ==============================================================================


# Template for the asum functions with overflow for signed integer without SIMD support.
template_basic = """/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
%(return_type)s asum_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, signed int *errflag, signed int ignoreerrors) { 

	// array index counter. 
	Py_ssize_t x; 
	%(return_type)s partialsum = 0;

	*errflag = 0;
	// Overflow checking disabled.
	if (ignoreerrors%(skipcheckovflcheck)s) {
		for (x = 0; x < arraylen; x++) {
			partialsum = partialsum + data[x];
		}
	} else {
		// Overflow checking enabled.
		for (x = 0; x < arraylen; x++) {
			if (%(loop_overflow)s(data[x], partialsum)) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			} else {
				partialsum = partialsum + data[x];
			}
		}
	}

	return partialsum;
}
/*--------------------------------------------------------------------------- */

"""

# ==============================================================================
# Template for the asum functions with overflow for signed integer with SIMD support.
template_basic_int_simd = """/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   Returns: The sum of the array.
*/
%(return_type)s asum_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, signed int *errflag, signed int ignoreerrors, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	%(return_type)s partialsum = 0;

	*errflag = 0;

%(simdplatform)s

	// SIMD version. 
	if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			partialsum = asum_%(funcmodifier)s_simd(arraylen, data);
		} else {
			partialsum = asum_%(funcmodifier)s_simd_ovfl(arraylen, data, errflag);
		}
	} else {
#endif

		// Overflow checking disabled.
		if (ignoreerrors%(skipcheckovflcheck)s) {
			for (x = 0; x < arraylen; x++) {
				partialsum = partialsum + data[x];
			}
		} else {
			// Overflow checking enabled.
			for (x = 0; x < arraylen; x++) {
				if (%(loop_overflow)s(data[x], partialsum)) {
					*errflag = ARR_ERR_OVFL;
					return partialsum; 
				} else {
					partialsum = partialsum + data[x];
				}
			}
		}

%(simdplatform)s
	}
#endif

	return partialsum;
}
/*--------------------------------------------------------------------------- */

"""

# ==============================================================================

# Template for integer SIMD support for x86 only.
ops_simdsupport_int_x86 = """

/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// This inner loop is used to sum small chunks of the array.
%(simdplatform)s
long long innerloop_asum_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	long long partialsum = 0;

	%(arraytype2)s sumvals[%(simdwidth)s / 2];
	%(simdattr)s loadslice1, loadslice2;
	%(simdattr2)s sumslice1, sumslice2, sumslicetotal, dataslice1, dataslice2;
	v16qi shufflebytes;

	signed char initvals[16] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	signed char shufflemask[16] = {8, 9, 10, 11, 12, 13, 14, 15, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff};


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Initialise the sum values.
	sumslice1 = (%(simdattr2)s) __builtin_ia32_lddqu((char *)  initvals);
	sumslice2 = (%(simdattr2)s) __builtin_ia32_lddqu((char *)  initvals);

	// This is used with alternate means of moving high bytes to low bytes.
	shufflebytes = (v16qi) __builtin_ia32_lddqu((char *)  shufflemask);


	// Use SIMD.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		loadslice1 = (%(simdattr)s) __builtin_ia32_lddqu((char *)  &data[x]);

		// Shuffle the high bytes into the low bytes for the second vector.
		loadslice2 = (%(simdattr)s) __builtin_ia32_pshufb128( (v16qi) loadslice1, shufflebytes);


		// Split the vector into two smaller ones.
		dataslice1 = %(simdvecsplit)s(loadslice1);
		dataslice2 = %(simdvecsplit)s(loadslice2);


		// Add each half vector.
		sumslice1 = %(simdop)s(sumslice1, dataslice1);
		sumslice2 = %(simdop)s(sumslice2, dataslice2);

	}


	// Add the two half vectors together.
	sumslicetotal = (%(simdattr2)s) %(simdop)s(sumslice1, sumslice2);


	// Add up the values within the slice.
	__builtin_ia32_storedqu((char *) sumvals, (v16qi) sumslicetotal);


	for (y = 0; y < (%(simdwidth)s / 2); y++) {
		partialsum = partialsum + sumvals[y];
	}

	// Add the values within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}


	return partialsum;
}
#endif
"""

# ==============================================================================

# Template for integer SIMD support for ARMv7 and ARMv8 only.
ops_simdsupport_int_arm = """
/*--------------------------------------------------------------------------- */

/* For array code: %(arraycode)s
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// This inner loop is used to sum small chunks of the array.
%(simdplatform)s
%(return_type)s innerloop_asum_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	%(return_type)s partialsum = 0;

	%(arraytype2)s sumvals[%(simdwidth)s / 2];
	%(simdattr)s dataslice;
	%(simdattr2)s resultslice;


	// Initialise the accumulator.
	resultslice = %(simdinitaccu)s(0);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Use SIMD.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {

		// Load the data into the vector register.
		dataslice = %(simdload)s( &data[x]);

		// The actual SIMD operation. 
		resultslice = %(simdop)s(resultslice, dataslice);

	}

	// Add up the values within the slice.
	%(simdop2)s(sumvals, resultslice);
	for (y = 0; y < (%(simdwidth)s / 2); y++) {
		partialsum = partialsum + sumvals[y];
	}

	// Add the values within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}

	return partialsum;

}
#endif
"""


# ==============================================================================

# Template for integer SIMD support for ARMv7 with array types 'i' or 'I' only.
# This is a special case because we want a 64 bit result from a 64 bit SIMD register.
ops_simdsupport_int_armv7i = """
/*--------------------------------------------------------------------------- */

/* For array code: %(arraycode)s
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// This inner loop is used to sum small chunks of the array.
%(simdplatform)s
%(return_type)s innerloop_asum_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	%(return_type)s partialsum = 0;

	%(simdattr)s dataslice;
	%(simdattr2)s resultslice;


	// Initialise the accumulator.
	resultslice = %(simdinitaccu)s(0);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Use SIMD.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {

		// Load the data into the vector register.
		dataslice = %(simdload)s( &data[x]);

		// The actual SIMD operation. 
		resultslice = %(simdop)s(resultslice, dataslice);

	}

	// Extract the result from the vector. As the SIMD register is only
	// 64 bits and we want a 64 bit result, we don't need to iterate through
	// an array in this special case. 
	%(simdop2)s (&partialsum, resultslice);

	// Add the values within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}

	return partialsum;

}
#endif
"""

# ==============================================================================

# ==============================================================================

# Template for integer SIMD support for all SIMD architectures.
ops_simdsupport_int = """


/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// Version without error checking.
%(simdplatform)s
%(return_type)s asum_%(funcmodifier)s_simd(Py_ssize_t arraylen, %(arraytype)s *data) { 

	Py_ssize_t x, loopremaining, loopchunk;
	%(return_type)s partialsum = 0;

	for(x=0; x < arraylen; x += LOOPCHUNKSIZE) {
		// The array is summed in "chunks" using SIMD and then each
		// chunk added to the total.
		loopremaining = arraylen - x;
		loopchunk = (loopremaining >  LOOPCHUNKSIZE) ? LOOPCHUNKSIZE : loopremaining;

		// Add the chunk to the grand total.
		partialsum = partialsum + innerloop_asum_%(funcmodifier)s(loopchunk, &data[x]);
	}

	return partialsum;

}
#endif

/*--------------------------------------------------------------------------- */

/* For array code: %(arraycode)s
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an error occured.
   Returns: The sum of the array.
*/
%(simdplatform)s
%(return_type)s asum_%(funcmodifier)s_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data, signed int *errflag) { 

	%(return_type)s partialsum = 0;
	%(return_type)s chunksum;
	Py_ssize_t x, loopremaining, loopchunk;

	for(x=0; x < arraylen; x += LOOPCHUNKSIZE) {
		// The array is summed in "chunks" using SIMD and then each
		// chunk added to the total.
		loopremaining = arraylen - x;
		loopchunk = (loopremaining >  LOOPCHUNKSIZE) ? LOOPCHUNKSIZE : loopremaining;

		// Add up one "chunk" of the array.
		chunksum = innerloop_asum_%(funcmodifier)s(loopchunk, &data[x]);

		// Check for overflow.
		if (loop_willoverflow_signed(chunksum, partialsum)) {
			*errflag = ARR_ERR_OVFL;
			return partialsum; 
		}

		// Add the chunk to the grand total.
		partialsum = partialsum + chunksum;
	}

	return partialsum;

}
#endif

/*--------------------------------------------------------------------------- */

"""


# ==============================================================================

# ==============================================================================

fixfloatfinite = """
/* This function is used to overcome what appears to be a compiler bug in 
   x86 32 bit platforms. When two maximum float (32 bit floating point numbers) 
   values were added together they would result in a value which should have 
   been infinity, but instead were twice the maximum value (6.805646932770577e+38).
   Passing the result into and out of this function seems to force the correct 
   result of "inf" to be produced. A variety of different fixes and tweaks were 
   tried, but this was the simpliest that worked.
*/
#ifdef AF_FIXFLOAT_i386
float fixfloatfinite(float inval) {
	return inval;
}
#endif
"""
# This is the function call for the above, to be inserted where required.
fixfloatfinitecall = """#ifdef AF_FIXFLOAT_i386
			partialsum = fixfloatfinite(partialsum);
#endif
"""


# ==============================================================================

# This is used for floating point versions only.
floattemplate = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an overflow error occured in integer operations.
   ignoreerrors = If true, arithmetic overflow checking is disabled.
   nosimd = If true, disable SIMD.
   Returns: The sum of the array.
*/
%(arraytype)s asum_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, signed int *errflag, signed int ignoreerrors, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t x; 
	%(arraytype)s partialsum = 0.0;

	*errflag = 0;

%(simdplatform)s
	// SIMD version. 
	if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			partialsum = asum_%(funcmodifier)s_simd(arraylen, data);
		} else {
			partialsum = asum_%(funcmodifier)s_simd_ovfl(arraylen, data, errflag);
		}
	} else {
#endif

		// Non-SIMD version.
		// Overflow checking disabled.
		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				partialsum = partialsum + data[x];
			}
%(fixfloatfinitecall)s
		} else {
			// Overflow checking enabled.
			for (x = 0; x < arraylen; x++) {
				partialsum = partialsum + data[x];
			}
			// Non-finite data will propagate through the sum, so we
			// only have to check it when we are all done.
			if (!isfinite(partialsum)) {
				*errflag = ARR_ERR_OVFL;
				return partialsum; 
			}
		}
%(simdplatform)s
	}
#endif

	return partialsum;
}
/*--------------------------------------------------------------------------- */
"""

# ==============================================================================

# This is used for x86 floating point SIMD versions only.
ops_simdsupport_float_x86 = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data array.
   data = The input data array.
   errflag = Set to true if an error occured.
   Returns: The sum of the array.
*/
// Version without error checking.
%(simdplatform)s
%(arraytype)s asum_%(funcmodifier)s_simd(Py_ssize_t arraylen, %(arraytype)s *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	%(arraytype)s partialsum = 0.0;

	%(arraytype)s sumvals[%(simdwidth)s];
	%(simdattr)s sumslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Initialise the sum values.
	sumslice = (%(simdattr)s) %(simdload)s(data);

	// Use SIMD.
	for (x = %(simdwidth)s; x < alignedlength; x += %(simdwidth)s) {
		dataslice = (%(simdattr)s) %(simdload)s(&data[x]);
		sumslice = %(simdop)s(sumslice, dataslice);
	}

	// Add up the values within the slice.
	%(simdstore)s(sumvals, (%(simdattr)s) sumslice);
	for (y = 0; y < %(simdwidth)s; y++) {
		partialsum = partialsum + sumvals[y];
	}

	// Add the values within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}


	return partialsum;
}

/*--------------------------------------------------------------------------- */

// Version with error checking.
%(arraytype)s asum_%(funcmodifier)s_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data, signed int *errflag) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	%(arraytype)s partialsum = 0.0;

	%(arraytype)s sumvals[%(simdwidth)s];
	%(simdattr)s sumslice, dataslice;


	*errflag = 0;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Initialise the sum values.
	sumslice = (%(simdattr)s) %(simdload)s(data);

	// Use SIMD.
	for (x = %(simdwidth)s; x < alignedlength; x += %(simdwidth)s) {
		dataslice = (%(simdattr)s) %(simdload)s(&data[x]);
		sumslice = %(simdop)s(sumslice, dataslice);
	}

	// Add up the values within the slice.
	%(simdstore)s(sumvals, (%(simdattr)s) sumslice);
	for (y = 0; y < %(simdwidth)s; y++) {
		partialsum = partialsum + sumvals[y];
	}


	// Add the values within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}

	// If an error occured resulting in NaN or INF anywhere in the course of
	// the calculation it should have propagated through to the end and we will
	// find it here at the end.
	if (!isfinite(partialsum)) {
		*errflag = ARR_ERR_OVFL;
	}


	return partialsum;
}
#endif
/*--------------------------------------------------------------------------- */
"""


# ==============================================================================


# Template for float SIMD support for ARMv7 and ARMv8.
ops_simdsupport_float_arm = """
/*--------------------------------------------------------------------------- */
/* For array code: f
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// This inner loop is used to sum small chunks of the array.
%(simdplatform)s
float asum_float_simd(Py_ssize_t arraylen, float *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	float partialsum = 0.0;

	float sumvals[FLOATSIMDSIZE];
	%(simdattr)s dataslice, resultslice;


	// Initialise the accumulator.
	resultslice = %(simdinitaccu)s(0.0);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Use SIMD.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {

		// Load the data into the vector register.
		dataslice = %(simdload)s( &data[x]);

		// The actual SIMD operation. 
		resultslice = %(simdop)s(resultslice, dataslice);

	}

	// Add up the values within the slice.
	%(simdstore)s(sumvals, resultslice);
	for (y = 0; y < (FLOATSIMDSIZE); y++) {
		partialsum = partialsum + sumvals[y];
	}

	// Add the values within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}

	return partialsum;

}
#endif

/*--------------------------------------------------------------------------- */
/* For array code: f
   arraylen = The length of the data array.
   data = The input data array.
   Returns: The sum of the array.
*/
// This inner loop is used to sum small chunks of the array.
%(simdplatform)s
float asum_float_simd_ovfl(Py_ssize_t arraylen, float *data, signed int *errflag) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	float partialsum = 0.0;

	float sumvals[FLOATSIMDSIZE];
	%(simdattr)s dataslice, resultslice;


	*errflag = 0;

	// Initialise the accumulator.
	resultslice = %(simdinitaccu)s(0.0);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, FLOATSIMDSIZE);

	// Use SIMD.
	for (x = 0; x < alignedlength; x += FLOATSIMDSIZE) {

		// Load the data into the vector register.
		dataslice = %(simdload)s( &data[x]);

		// The actual SIMD operation. 
		resultslice = %(simdop)s(resultslice, dataslice);

	}

	// Add up the values within the slice.
	%(simdstore)s(sumvals, resultslice);
	for (y = 0; y < (FLOATSIMDSIZE); y++) {
		partialsum = partialsum + sumvals[y];
	}

	// Add the values within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		partialsum = partialsum + data[x];
	}


	// If an error occured resulting in NaN or INF anywhere in the course of
	// the calculation it should have propagated through to the end and we will
	// find it here at the end.
	if (!isfinite(partialsum)) {
		*errflag = ARR_ERR_OVFL;
	}


	return partialsum;

}
#endif

"""

# ==============================================================================

asum_params = """
/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// This is used to hold the parsed parameters.
	struct args_params_asum arraydata = ARGSINIT_ASUM;

	// The sum of the array, as a python object.
	PyObject *sumreturn;

	// Indicates an error.
	signed int errflag = 0;

	// Results are different types.
	long long resultll = 0;
	unsigned long long resultull = 0;
	double resultd = 0.0;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_asum(self, args, keywds, "%(funclabel)s");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}


	// The length of the data array.
	if (arraydata.arraylength < 1) {
		// Release the buffers. 
		releasebuffers_asum(arraydata);
		ErrMsgArrayLengthErr();
		return NULL;
	}



	/* Call the C function */
	switch(arraydata.arraytype) {
		// signed char
		case 'b' : {
			resultll = asum_signed_char(arraydata.arraylength, arraydata.array1.b, &errflag, arraydata.ignoreerrors, arraydata.nosimd);
			sumreturn = PyLong_FromLongLong(resultll);
			break;
		}
		// unsigned char
		case 'B' : {
			resultull = asum_unsigned_char(arraydata.arraylength, arraydata.array1.B, &errflag, arraydata.ignoreerrors, arraydata.nosimd);
			sumreturn = PyLong_FromUnsignedLongLong(resultull);
			break;
		}
		// signed short
		case 'h' : {
			resultll = asum_signed_short(arraydata.arraylength, arraydata.array1.h, &errflag, arraydata.ignoreerrors, arraydata.nosimd);
			sumreturn = PyLong_FromLongLong(resultll);
			break;
		}
		// unsigned short
		case 'H' : {
			resultull = asum_unsigned_short(arraydata.arraylength, arraydata.array1.H, &errflag, arraydata.ignoreerrors, arraydata.nosimd);
			sumreturn = PyLong_FromUnsignedLongLong(resultull);
			break;
		}
		// signed int
		case 'i' : {
			resultll = asum_signed_int(arraydata.arraylength, arraydata.array1.i, &errflag, arraydata.ignoreerrors, arraydata.nosimd);
			sumreturn = PyLong_FromLongLong(resultll);
			break;
		}
		// unsigned int
		case 'I' : {
			resultull = asum_unsigned_int(arraydata.arraylength, arraydata.array1.I, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromUnsignedLongLong(resultull);
			break;
		}
		// signed long
		case 'l' : {
			resultll = asum_signed_long(arraydata.arraylength, arraydata.array1.l, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromLongLong(resultll);
			break;
		}
		// unsigned long
		case 'L' : {
			resultull = asum_unsigned_long(arraydata.arraylength, arraydata.array1.L, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromUnsignedLongLong(resultull);
			break;
		}
		// signed long long
		case 'q' : {
			resultll = asum_signed_long_long(arraydata.arraylength, arraydata.array1.q, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromLongLong(resultll);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultull = asum_unsigned_long_long(arraydata.arraylength, arraydata.array1.Q, &errflag, arraydata.ignoreerrors);
			sumreturn = PyLong_FromUnsignedLongLong(resultull);
			break;
		}
		// float
		case 'f' : {
			resultd = (double) asum_float(arraydata.arraylength, arraydata.array1.f, &errflag, arraydata.ignoreerrors, arraydata.nosimd);
			sumreturn = PyFloat_FromDouble(resultd);
			break;
		}
		// double
		case 'd' : {
			resultd = asum_double(arraydata.arraylength, arraydata.array1.d, &errflag, arraydata.ignoreerrors, arraydata.nosimd);
			sumreturn = PyFloat_FromDouble(resultd);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_asum(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_asum(arraydata);


	// Signal the errors.

	if (errflag == ARR_ERR_OVFL) {
		ErrMsgArithOverflowCalc();
		return NULL;
	}


	return sumreturn;

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(%(funclabel)s__doc__,
"asum \\n\\
_____________________________ \\n\\
\\n\\
Calculate the arithmetic sum of an array.  \\n\\
\\n\\
======================  ============================================== \\n\\
Equivalent to:          sum() \\n\\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \\n\\
======================  ============================================== \\n\\
\\n\\
Call formats: \\n\\
\\n\\
  result = %(funclabel)s(array) \\n\\
  result = %(funclabel)s(array, maxlen=y) \\n\\
  result = %(funclabel)s(array, nosimd=False) \\n\\
  result = %(funclabel)s(array, matherrors=False) \\n\\
\\n\\
* array - The input data array to be examined. \\n\\
* maxlen - Limit the length of the array used. This must be a valid \\n\\
  positive integer. If a zero or negative length, or a value which is \\n\\
  greater than the actual length of the array is specified, this \\n\\
  parameter is ignored. \\n\\
* nosimd - If True, SIMD acceleration is disabled if present. \\n\\
  The default is False (SIMD acceleration is enabled if present). \\n\\
* matherrors - If True, checks for numerical errors including integer \\n\\
  overflow are ignored. \\n\\
* result - The sum of the array. \\n\\
");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "%(funclabel)s" is the name seen inside of Python. 
 "py_%(funclabel)s" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef %(funclabel)s_methods[] = {
	{"%(funclabel)s",  (PyCFunction)py_%(funclabel)s, METH_VARARGS | METH_KEYWORDS, %(funclabel)s__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef %(funclabel)smodule = {
    PyModuleDef_HEAD_INIT,
    "%(funclabel)s",
    NULL,
    -1,
    %(funclabel)s_methods
};

PyMODINIT_FUNC PyInit_%(funclabel)s(void)
{
    return PyModule_Create(&%(funclabel)smodule);
};

/*--------------------------------------------------------------------------- */

"""


# ==============================================================================

# This selects the correct template according to the C data type.
ops_calls = {'b' : template_basic_int_simd, 'B' : template_basic_int_simd, 
	'h' : template_basic_int_simd, 'H' : template_basic_int_simd, 
	'i' : template_basic_int_simd, 'I' : template_basic, 
	'l' : template_basic, 'L' : template_basic, 
	'q' : template_basic, 'Q' : template_basic, 
	'f' : floattemplate, 'd' : floattemplate}


# Used to determine the return type for integer templates.
return_type = {
	'b' : 'long long', 'B' : 'unsigned long long', 
	'h' : 'long long', 'H' : 'unsigned long long', 
	'i' : 'long long', 'I' : 'unsigned long long', 
	'l' : 'long long', 'L' : 'unsigned long long', 
	'q' : 'long long', 'Q' : 'unsigned long long', 
	'f' : '', 'd' : '',
	}

# Used to determine the type of overflow macro to use
loop_overflow = {
	'b' : 'loop_willoverflow_signed', 'B' : 'loop_willoverflow_unsigned', 
	'h' : 'loop_willoverflow_signed', 'H' : 'loop_willoverflow_unsigned', 
	'i' : 'loop_willoverflow_signed', 'I' : 'loop_willoverflow_unsigned', 
	'l' : 'loop_willoverflow_signed', 'L' : 'loop_willoverflow_unsigned', 
	'q' : 'loop_willoverflow_signed', 'Q' : 'loop_willoverflow_unsigned', 
	'f' : '', 'd' : '',
	}

# This is a 'fix" for what appears to be a compiler bug.
fixfloatfinite_ops = {'f' : fixfloatfinitecall}


simdloopchunksize = """
/*--------------------------------------------------------------------------- */

// This defines the "chunk" size used to process integer arrays in pieces small
// enough that overflow cannot occur within the "chunk".
#define LOOPCHUNKSIZE %i

/*--------------------------------------------------------------------------- */

"""

# ==============================================================================

# For all architectures.
simdwidth_allarch = {
	'b' : 'CHARSIMDSIZE',
	'B' : 'CHARSIMDSIZE',
	'h' : 'SHORTSIMDSIZE',
	'H' : 'SHORTSIMDSIZE',
	'i' : 'INTSIMDSIZE',
	'I' : 'INTSIMDSIZE',
	'l' : '',
	'L' : '',
	'q' : '',
	'Q' : '',
	'f' : 'FLOATSIMDSIZE',
	'd' : 'DOUBLESIMDSIZE',
}

# ==============================================================================

# x86 SIMD data.

simdattr_x86 = {
	'b' : 'v16qi',
	'h' : 'v8hi',
	'i' : 'v4si',
	'f' : 'v4sf',
	'd' : 'v2df',
}

simdattr2_x86 = {
	'b' : 'v8hi',
	'h' : 'v4si',
	'i' : 'v2di',
	'f' : '',
	'd' : '',
}

# This defines an array type with larger word sizes than the actual array type 
# so that the integer type can be promoted to a larger size to avoid overflow. 
arraytype2_x86 = {
	'b' : 'signed short',
	'h' : 'signed int',
	'i' : 'signed long',
	'f' : '',
	'd' : '',
}


simdstoreattr_x86 = {
	'f' : 'v4sf',
	'd' : 'v2df',
}


simdload_x86 = {
	'f' : '__builtin_ia32_loadups',
	'd' : '__builtin_ia32_loadupd',
}

simdstore_x86 = {
	'f' : '__builtin_ia32_storeups',
	'd' : '__builtin_ia32_storeupd',
}

simdop_x86 = {
	'b' : '__builtin_ia32_paddw128', 
	'h' : '__builtin_ia32_paddd128', 
	'i' : '__builtin_ia32_paddq128', 
	'f' : '__builtin_ia32_addps',
	'd' : '__builtin_ia32_addpd',
}

simdvecsplit_x86 = {
	'b' : '__builtin_ia32_pmovsxbw128', 
	'h' : '__builtin_ia32_pmovsxwd128', 
	'i' : '__builtin_ia32_pmovsxdq128', 
	'f' : '',
	'd' : '',
}

# A list of which array types are supported by x86 SIMD instructions.
x86_simdtypes = tuple(simdop_x86.keys())

# Set the size of the "chunks" used when processing x86 SIMD.
simdloopchunksize_x86 = simdloopchunksize % 256


# ==============================================================================
# ARMv7 SIMD data.


# This defines an array type with larger word sizes than the actual array type 
# so that the integer type can be promoted to a larger size to avoid overflow. 
arraytype2_armv7 = {
	'b' : 'signed short',
	'B' : 'unsigned short',
	'h' : 'signed int',
	'H' : 'unsigned int',
	'i' : 'signed long',
	'I' : 'unsigned long',
	'f' : '',
}

simdattr_armv7 = {
	'b' : 'int8x8_t',
	'B' : 'uint8x8_t',
	'h' : 'int16x4_t',
	'H' : 'uint16x4_t',
	'i' : 'int32x2_t',
	'I' : 'uint32x2_t',
	'f' : 'float32x2_t',
}

simdattr2_armv7 = {
	'b' : 'int16x4_t',
	'B' : 'uint16x4_t',
	'h' : 'int32x2_t',
	'H' : 'uint32x2_t',
	'i' : 'int64x1_t',
	'I' : 'uint64x1_t',
	'f' : '',
}


simdinitaccu_armv7 = {
	'b' : 'vdup_n_s16',
	'B' : 'vdup_n_u16',
	'h' : 'vdup_n_s32',
	'H' : 'vdup_n_u32',
	'i' : 'vdup_n_s64',
	'I' : 'vdup_n_u64',
	'f' : 'vdup_n_f32',
}


simdload_armv7 = {
	'b' : 'vld1_s8',
	'B' : 'vld1_u8',
	'h' : 'vld1_s16',
	'H' : 'vld1_u16',
	'i' : 'vld1_s32',
	'I' : 'vld1_u32',
	'f' : 'vld1_f32',
}


simdop_armv7 = {
	'b' : 'vpadal_s8',
	'B' : 'vpadal_u8',
	'h' : 'vpadal_s16',
	'H' : 'vpadal_u16',
	'i' : 'vpadal_s32',
	'I' : 'vpadal_u32',
	'f' : 'vadd_f32',
}

simdop2_armv7 = {
	'b' : 'vst1_s16',
	'B' : 'vst1_u16',
	'h' : 'vst1_s32',
	'H' : 'vst1_u32',
	'i' : 'vst1_s64',
	'I' : 'vst1_u64',
	'f' : '',
}

simdstore_armv7 = {
	'b' : '',
	'B' : '',
	'h' : '',
	'H' : '',
	'i' : '',
	'I' : '',
	'f' : 'vst1_f32',
}


# A list of which array types are supported by ARMv7 SIMD instructions.
armv7_simdtypes = ('b', 'B', 'h', 'H', 'f')

# Just the integer SIMD arrays.
armv7_int_simdtypes = ('b', 'B', 'h', 'H')

# Set the size of the "chunks" used when processing ARMv7 SIMD.
simdloopchunksize_armv7 = simdloopchunksize % 256


# ==============================================================================
# ARMv8 SIMD data.


# This defines an array type with larger word sizes than the actual array type 
# so that the integer type can be promoted to a larger size to avoid overflow. 
arraytype2_armv8 = {
	'b' : 'signed short',
	'B' : 'unsigned short',
	'h' : 'signed int',
	'H' : 'unsigned int',
	'i' : 'signed long',
	'I' : 'unsigned long',
	'f' : '',
	'd' : '',
}

simdattr_armv8 = {
	'b' : 'int8x16_t',
	'B' : 'uint8x16_t',
	'h' : 'int16x8_t',
	'H' : 'uint16x8_t',
	'i' : 'int32x4_t',
	'I' : 'uint32x4_t',
	'f' : 'float32x4_t',
}

simdattr2_armv8 = {
	'b' : 'int16x8_t',
	'B' : 'uint16x8_t',
	'h' : 'int32x4_t',
	'H' : 'uint32x4_t',
	'i' : 'int64x2_t',
	'I' : 'uint64x2_t',
	'f' : '',
}


simdinitaccu_armv8 = {
	'b' : 'vdupq_n_s16',
	'B' : 'vdupq_n_u16',
	'h' : 'vdupq_n_s32',
	'H' : 'vdupq_n_u32',
	'i' : 'vdupq_n_s64',
	'I' : 'vdupq_n_u64',
	'f' : 'vdupq_n_f32',
}


simdload_armv8 = {
	'b' : 'vld1q_s8',
	'B' : 'vld1q_u8',
	'h' : 'vld1q_s16',
	'H' : 'vld1q_u16',
	'i' : 'vld1q_s32',
	'I' : 'vld1q_u32',
	'f' : 'vld1q_f32',
}


simdop_armv8 = {
	'b' : 'vpadalq_s8',
	'B' : 'vpadalq_u8',
	'h' : 'vpadalq_s16',
	'H' : 'vpadalq_u16',
	'i' : 'vpadalq_s32',
	'I' : 'vpadalq_u32',
	'f' : 'vaddq_f32',
}

simdop2_armv8 = {
	'b' : 'vst1q_s16',
	'B' : 'vst1q_u16',
	'h' : 'vst1q_s32',
	'H' : 'vst1q_u32',
	'i' : 'vst1q_s64',
	'I' : 'vst1q_u64',
	'f' : '',
}

simdstore_armv8 = {
	'b' : '',
	'B' : '',
	'h' : '',
	'H' : '',
	'i' : '',
	'I' : '',
	'f' : 'vst1q_f32',
}


# A list of which array types are supported by ARMv8 SIMD instructions.
# Benchmark tests of 'i' arrays showed them to be slower as SIMD than
# for non-SIMD, so they are excluded.
armv8_simdtypes = ('b', 'B', 'h', 'H', 'f')

# Just the integer SIMD arrays.
armv8_int_simdtypes = ('b', 'B', 'h', 'H')

# Set the size of the "chunks" used when processing ARMv8 SIMD.
simdloopchunksize_armv8 = simdloopchunksize % 256

# ==============================================================================
# ==============================================================================

# Includes added to code files.
ovfl_includes = """
/*--------------------------------------------------------------------------- */

// Used to check for integer overflow. 
#include "asum_defs.h"

/*--------------------------------------------------------------------------- */

"""



# Select skipping overflow checks.
skipcheckovflcheck = {
	'b' : ' || charskipovflcheck(arraylen)', 
	'B' : ' || charskipovflcheck(arraylen)', 
	'h' : ' || shortskipovflcheck(arraylen)', 
	'H' : ' || shortskipovflcheck(arraylen)', 
	'i' : ' || intskipovflcheck(arraylen)', 
	'I' : ' || intskipovflcheck(arraylen)', 
	'l' : '', 'L' : '', 
	'q' : '', 'Q' : '', 
	'f' : '', 'd' : ''}

# ==============================================================================

# These get substituted into function call templates.
SIMD_platform_x86 = '#if defined(AF_HASSIMD_X86)'
SIMD_platform_x86_ARM = '#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)'
SIMD_platform_x86_ARMv8 = '#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)'
SIMD_platform_x86_ARMv7 = '#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT)'
SIMD_platform_ARMv7 = '#if defined(AF_HASSIMD_ARMv7_32BIT)'
SIMD_platform_ARM64v8 = '#if defined(AF_HASSIMD_ARM_AARCH64)'
SIMD_platform_ARM = '#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)'


# ==============================================================================

# Return the platform SIMD enable C macro. 
# This is for the platform independent file, and not the plaform specific
# SIMD files.
def findsimdplatform(arraycode, funcname):

	hasx86 = arraycode in x86_simdtypes
	hasarmv7 = arraycode in armv7_simdtypes
	hasarmv8 = arraycode in armv8_simdtypes

	# Only the platforms combinations which are used currently are defined here.
	if hasx86 and hasarmv7 and hasarmv8:
		return SIMD_platform_x86_ARM
	elif hasx86 and (not hasarmv7) and (not hasarmv8):
		return SIMD_platform_x86
	elif hasx86 and (not hasarmv7) and hasarmv8:
		return SIMD_platform_x86_ARMv8
	elif hasx86 and hasarmv7 and (not hasarmv8):
		return SIMD_platform_x86_ARMv7
	elif (not hasx86) and hasarmv7 and hasarmv8:
		return SIMD_platform_ARM
	elif (not hasx86) and (not hasarmv7) and hasarmv8:
		return SIMD_platform_ARM64v8
	else:
		print('Error: Template error in findsimdplatform: %s %s' % (arraycode, funcname))
		return 'Error: Template error, this should not be here.'

# ==============================================================================


# ==============================================================================

funcname = "asum"

# ==============================================================================
# This outputs the non-SIMD version.
# Output the generated code.

# Output the functions which implement the individual non-SIMD 
# implementation functions.
def CreateNonSIMDCode(funcname):

	filename = funcname + '.c'

	with open(filename, 'w') as f:
		f.write(asum_head % {'funclabel' : funcname})

		# Each type of array.
		for arraycode in codegen_common.arraycodes:
			arraytype = codegen_common.arraytypes[arraycode]
			funcmodifier = arraytype.replace(' ', '_')


			# Select the implementation template for the current data type.
			optemplate = ops_calls[arraycode]

			# This is to address what appears to be a compiler bug.
			if arraycode == 'f':
				f.write(fixfloatfinite)

			if arraycode in (set(x86_simdtypes) | set(armv7_simdtypes) | set(armv8_simdtypes)):
				simdplatform = findsimdplatform(arraycode, funcname)
			else:
				simdplatform = ''

			# Write out the calculation source code. 
			f.write(optemplate % {'arraycode' : arraycode, 
						'arraytype' : arraytype, 
						'funcmodifier' : funcmodifier, 
						'return_type' : return_type[arraycode],
						'simdplatform' : simdplatform,
						'simdwidth' : simdwidth_allarch[arraycode],
						'fixfloatfinitecall' : fixfloatfinite_ops.get(arraycode, ''),
						'skipcheckovflcheck' : skipcheckovflcheck[arraycode],
						'loop_overflow' : loop_overflow[arraycode],
						})

		# Write out the boilerplate at the end.
		f.write(asum_params % {'funclabel' : funcname})


CreateNonSIMDCode(funcname)

# ==============================================================================

# This outputs helper macros.
def CreateMacroHelpers(funcname):

	macrofilename = funcname + '_defs' + '.h'

	macrocodedate = '21-Jun-2022'

	outputlist = []

	# Macro definitions.
	# Not array type specific. 
	outputlist.append(int_ovcheck)


	# Write out the file.
	codegen_common.OutputCHeader(macrofilename, 
		outputlist, 
		'Additional macros for %s' % funcname, 
		'', 
		macrocodedate)


CreateMacroHelpers(funcname)

# ==============================================================================

# ==============================================================================
# This outputs the SIMD code for x86

# x86
def SetSIMDData_x86(funcname):
	'''Set the SIMD template data for x86. 
	'''
	outputlist = []


	# This adds an include for common macro definitions.
	outputlist.append(ovfl_includes)

	# This adds a define block at the top.
	outputlist.append(simdloopchunksize_x86)

	# Output the generated code for integer arrays.
	for arraycode in ['b', 'h', 'i']:

		arraytype = codegen_common.arraytypes[arraycode]

		# x86 specific code.
		outputlist.append(ops_simdsupport_int_x86 % {'arraycode' : arraycode, 
					'arraytype' : arraytype, 
					'arraytype2' : arraytype2_x86[arraycode], 
					'funcmodifier' : arraytype.replace(' ', '_'), 
					'simdplatform' : SIMD_platform_x86,
					'simdattr' : simdattr_x86[arraycode],
					'simdattr2' : simdattr2_x86[arraycode],
					'simdwidth' : simdwidth_allarch[arraycode],
					'simdop' : simdop_x86[arraycode],
					'simdvecsplit' : simdvecsplit_x86[arraycode],
					})

		# Architecture independent code.
		outputlist.append(ops_simdsupport_int % {'arraycode' : arraycode, 
					'arraytype' : arraytype, 
					'arraytype2' : arraytype2_x86[arraycode], 
					'funcmodifier' : arraytype.replace(' ', '_'), 
					'return_type' : return_type[arraycode],
					'simdwidth' : simdwidth_allarch[arraycode],
					'simdplatform' : SIMD_platform_x86,
					})



	# Output the generated code for floating point arrays.
	for arraycode in codegen_common.floatarrays:

		arraytype = codegen_common.arraytypes[arraycode]

		outputlist.append(ops_simdsupport_float_x86 % {'arraycode' : arraycode, 
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'), 
					'simdplatform' : SIMD_platform_x86,
					'simdattr' : simdattr_x86[arraycode],
					'simdwidth' : simdwidth_allarch[arraycode],
					'simdload' : simdload_x86[arraycode],
					'simdstore' : simdstore_x86[arraycode],
					'simdop' : simdop_x86[arraycode],
					})


	return outputlist


# ==============================================================================
# This outputs the SIMD code for ARMv7

# ARMv7
def SetSIMDData_ARMv7(funcname):
	'''Set the SIMD template data for ARMv7. 
	'''
	outputlist = []


	# This adds an include for common macro definitions.
	outputlist.append(ovfl_includes)

	# This adds a define block at the top.
	outputlist.append(simdloopchunksize_armv7)

	# Output the generated code for integer arrays.
	for arraycode in armv7_int_simdtypes:

		arraytype = codegen_common.arraytypes[arraycode]

		# Array type 'i' needs a special template because it needs a 64 bit
		# result from a 64 bit SIMD register.
		if arraycode in ('i', 'I'):
			simdsupporttemplate = ops_simdsupport_int_armv7i
		else:
			simdsupporttemplate = ops_simdsupport_int_arm

		# ARMv7 specific code.
		outputlist.append(simdsupporttemplate % {'arraycode' : arraycode, 
					'arraytype' : arraytype, 
					'arraytype2' : arraytype2_armv7[arraycode], 
					'funcmodifier' : arraytype.replace(' ', '_'), 
					'return_type' : return_type[arraycode],
					'simdplatform' : SIMD_platform_ARMv7,
					'simdattr' : simdattr_armv7[arraycode],
					'simdattr2' : simdattr2_armv7[arraycode],
					'simdwidth' : simdwidth_allarch[arraycode],
					'simdop' : simdop_armv7[arraycode],
					'simdop2' : simdop2_armv7[arraycode],
					'simdinitaccu' : simdinitaccu_armv7[arraycode],
					'simdload' : simdload_armv7[arraycode],
					})

		# Architecture independent code.
		outputlist.append(ops_simdsupport_int % {'arraycode' : arraycode, 
					'arraytype' : arraytype, 
					'arraytype2' : arraytype2_armv7[arraycode], 
					'funcmodifier' : arraytype.replace(' ', '_'), 
					'return_type' : return_type[arraycode],
					'simdwidth' : simdwidth_allarch[arraycode],
					'simdplatform' : SIMD_platform_ARMv7,
					})

	# Output the generated code for floating point arrays.
	arraycode = 'f'
	arraytype = codegen_common.arraytypes[arraycode]

	outputlist.append(ops_simdsupport_float_arm % {'arraycode' : arraycode, 
				'arraytype' : arraytype, 
				'funcmodifier' : arraytype.replace(' ', '_'), 
				'simdwidth' : simdwidth_allarch[arraycode],
				'simdplatform' : SIMD_platform_ARMv7,
				'simdattr' : simdattr_armv7[arraycode],
				'simdinitaccu' : simdinitaccu_armv7[arraycode],
				'simdload' : simdload_armv7[arraycode],
				'simdop' : simdop_armv7[arraycode],
				'simdstore' : simdstore_armv7[arraycode],
				})


	return outputlist


# ==============================================================================

# ==============================================================================
# This outputs the SIMD code for ARMv8

# ARMv8
def SetSIMDData_ARMv8(funcname):
	'''Set the SIMD template data for ARMv8. 
	'''
	outputlist = []


	# This adds an include for common macro definitions.
	outputlist.append(ovfl_includes)

	# This adds a define block at the top.
	outputlist.append(simdloopchunksize_armv8)

	# Output the generated code for integer arrays.
	for arraycode in armv8_int_simdtypes:

		arraytype = codegen_common.arraytypes[arraycode]

		# ARMv8 specific code.
		outputlist.append(ops_simdsupport_int_arm % {'arraycode' : arraycode, 
					'arraytype' : arraytype, 
					'arraytype2' : arraytype2_armv8[arraycode], 
					'funcmodifier' : arraytype.replace(' ', '_'), 
					'return_type' : return_type[arraycode],
					'simdplatform' : SIMD_platform_ARM64v8,
					'simdattr' : simdattr_armv8[arraycode],
					'simdattr2' : simdattr2_armv8[arraycode],
					'simdwidth' : simdwidth_allarch[arraycode],
					'simdop' : simdop_armv8[arraycode],
					'simdop2' : simdop2_armv8[arraycode],
					'simdinitaccu' : simdinitaccu_armv8[arraycode],
					'simdload' : simdload_armv8[arraycode],
					})

		# Architecture independent code.
		outputlist.append(ops_simdsupport_int % {'arraycode' : arraycode, 
					'arraytype' : arraytype, 
					'arraytype2' : arraytype2_armv8[arraycode], 
					'funcmodifier' : arraytype.replace(' ', '_'), 
					'return_type' : return_type[arraycode],
					'simdwidth' : simdwidth_allarch[arraycode],
					'simdplatform' : SIMD_platform_ARM64v8,
					})

	# Output the generated code for floating point arrays.
	arraycode = 'f'
	arraytype = codegen_common.arraytypes[arraycode]

	outputlist.append(ops_simdsupport_float_arm % {'arraycode' : arraycode, 
				'arraytype' : arraytype, 
				'funcmodifier' : arraytype.replace(' ', '_'), 
				'simdwidth' : simdwidth_allarch[arraycode],
				'simdplatform' : SIMD_platform_ARM64v8,
				'simdattr' : simdattr_armv8[arraycode],
				'simdinitaccu' : simdinitaccu_armv8[arraycode],
				'simdload' : simdload_armv8[arraycode],
				'simdop' : simdop_armv8[arraycode],
				'simdstore' : simdstore_armv8[arraycode],
				})


	return outputlist


# ==============================================================================

def WriteSIMDCode(funcname, simdplatform, simdfilename, simdcodedate, outputlist):
	'''This writes out the SIMD code to the .c and .h files.
	'''
	# The SIMD options to select the additional file header info.
	simdoptions = {
	'x86' : ['simddefs'],
	'armv7' : ['simddefs', 'simdmacromsg_armv7'],
	'armv8' : ['simddefs', 'simdmacromsg_armv8'],
	}

	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname

	# This outputs the SIMD version.
	codegen_common.OutputSourceCode(funcname + simdfilename + '.c', outputlist, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate,
		'', simdoptions[simdplatform])


	# Output the .h header file.
	headedefs = codegen_common.GenSIMDCHeaderText(outputlist, funcname)

	# Write out the file.
	codegen_common.OutputCHeader(funcname + simdfilename + '.h', headedefs, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate)

# ==============================================================================

# The original date of the SIMD C code.
simdcodedate = '05-May-2017'
simdfilename = '_simd_x86'
outputlist = SetSIMDData_x86(funcname)
WriteSIMDCode(funcname, 'x86', simdfilename, simdcodedate, outputlist)


# The original date of the SIMD C code.
simdcodedate = '05-May-2017'
simdfilename = '_simd_armv7'
outputlist = SetSIMDData_ARMv7(funcname)
WriteSIMDCode(funcname, 'armv7', simdfilename, simdcodedate, outputlist)


# The original date of the SIMD C code.
simdcodedate = '05-May-2017'
simdfilename = '_simd_armv8'
outputlist = SetSIMDData_ARMv8(funcname)
WriteSIMDCode(funcname, 'armv8', simdfilename, simdcodedate, outputlist)


# ==============================================================================
