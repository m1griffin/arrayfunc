#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for math operators with one variable.
# Language: Python 3.4
# Date:     18-Mar-2018
#
###############################################################################
#
#   Copyright 2014 - 2021    Michael Griffin    <m12.griffin@gmail.com>
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

uniops_head = """//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   %(funclabel)s.c
// Purpose:  Calculate the %(funclabel)s of values in an array.
// Language: C
// Date:     15-Nov-2017.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2021    Michael Griffin    <m12.griffin@gmail.com>
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
#include "arrayparams_onesimd.h"

#include "simddefs.h"

#ifdef AF_HASSIMD_X86
#include "%(funclabel)s_simd_x86.h"
#endif

#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
#include "arm_neon.h"
#endif

#if defined(AF_HASSIMD_ARMv7_32BIT)
#include "%(funclabel)s_simd_armv7.h"
#endif

#if defined(AF_HASSIMD_ARM_AARCH64)
#include "%(funclabel)s_simd_armv8.h"
#endif

/*--------------------------------------------------------------------------- */

"""

# ==============================================================================

# For floating point.
uniops_op_float = """
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int %(funclabel)s_%(funcmodifier)s(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data, %(arraytype)s *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;

%(simd_call)s
	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = %(copname)s;
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = %(copname)s;
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = %(copname)s;
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = %(copname)s;
				if (!isfinite(data[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
	}

%(simd_call_close)s

	return ARR_NO_ERR;

}

"""
# ==============================================================================



# ==============================================================================

# For negating signed integer.
uniops_neg_int = """
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int %(funclabel)s_%(funcmodifier)s(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data, %(arraytype)s *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;

%(simd_call)s
	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = -data[x];
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				if ( minval_loop_willoverflow_%(funcmodifier)s(data[x]) ) {return ARR_ERR_OVFL;}
				dataout[x] = -data[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ( minval_loop_willoverflow_%(funcmodifier)s(data[x]) ) {return ARR_ERR_OVFL;}
				data[x] = -data[x];
			}
		}
	}

%(simd_call_close)s

	return ARR_NO_ERR;

}

"""
# ==============================================================================

# ==============================================================================

# For absolute value of a signed integer.
uniops_abs_int = """
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int %(funclabel)s_%(funcmodifier)s(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data, %(arraytype)s *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;

%(simd_call)s
	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				dataout[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				data[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for (x = 0; x < arraylen; x++) {
				if ( minval_loop_willoverflow_%(funcmodifier)s(data[x]) ) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		} else {
			for (x = 0; x < arraylen; x++) {
				if ( minval_loop_willoverflow_%(funcmodifier)s(data[x]) ) {return ARR_ERR_OVFL;}
				data[x] = data[x] >= 0 ? data[x] : -data[x];
			}
		}
	}

%(simd_call_close)s

	return ARR_NO_ERR;

}

"""
# ==============================================================================


# ==============================================================================

# The operations using SIMD.
ops_simdsupport = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
*/
// param_arr_none
%(simdplatform)s
void %(funclabel)s_%(funcmodifier)s_1_simd(Py_ssize_t arraylen, %(arraytype)s *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft;
	%(vsignparam)s


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data[x]);
		// The actual SIMD operation. 
		datasliceleft = %(simdop)s;
		// Store the result.
		%(vstinstr1)s &data[x], %(vstinstr2)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data[x] = %(simdcleanup)s;
	}

}
#endif


// param_arr_arr
%(simdplatform)s
void %(funclabel)s_%(funcmodifier)s_2_simd(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft;
	%(vsignparam)s


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data[x]);
		// The actual SIMD operation. 
		datasliceleft = %(simdop)s;
		// Store the result.
		%(vstinstr1)s &dataout[x], %(vstinstr2)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		dataout[x] = %(simdcleanup)s;
	}

}
#endif

"""


# ==============================================================================


# Helper functions for SIMD support. There needs to be one for each data type.
simd_helpers = """
/*--------------------------------------------------------------------------- */
/* Initialise an SIMD vector with a specifired value.
   initval = The value to initialise the vector to.
   Returns the initalised SIMD vector. 
*/
%(simdplatform)s
%(simdattr)s initvec_%(funcmodifier)s(%(arraytype)s initval) {

	unsigned int y;
	%(arraytype)s initvals[%(simdwidth)s];
	%(simdattr)s simdvec;

	for (y = 0; y < %(simdwidth)s; y++) {
		initvals[y] = initval;
	}
	simdvec = %(vldinstr)s(initvals));

	return simdvec;
}
#endif


"""



# Create this for each signed integers type.
intov_macros_signed = """
/*--------------------------------------------------------------------------- */
// For %(arraytype)s.
// Use to detect if an overflow condition will occur due to negating a minimum integer. 
#define minval_loop_willoverflow_%(funcmodifier)s(val) (val == %(intminvalue)s)
"""

# ==============================================================================

# The template for overflow checks for x86_64. This requires the correct SIMD attribute
# to be insertered before itself being inserted into the next template.
simd_ovflchk1_x86 = '''// Do an equal compare operation.
			ovcheck = %(veqinstr)s (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {'''

simd_equ_willoverflow_armv7 = '''// Do an equal compare operation.
			ovcheck = %(veqinstr)s (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(%(vreinterpinstr)s(ovcheck) == 0x0000000000000000)){'''


simd_equ_willoverflow_armv8 = '''// Do an equal compare operation.
			ovcheck = %(veqinstr)s (datasliceleft, ovflvec);

			// Check for overflow. 
			// Combine the result to two 64 bit vectors.
			veccombine = %(vreinterpinstr)s(ovcheck);
			// Get the high and low lanes of the combined vector.
			lowresult = vgetq_lane_u64(veccombine, 0);
			highresult = vgetq_lane_u64(veccombine, 1);
			// Check if overflow will happen.
			if ((lowresult != 0x0000000000000000) || (highresult != 0x0000000000000000)) {'''


# Extra variables needed for ARMv8.
simd_ovflchk_extravars_armv8 = '''uint64x2_t veccombine;
	uint64_t highresult, lowresult;'''

# ==============================================================================

# The abs_ operations using SIMD. This version checks for overflow.
ops_simdsupport_ovfl_abs = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
*/
// param_arr_none
%(simdplatform)s
char %(funclabel)s_%(funcmodifier)s_1_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, ovflvec;
	%(ovflsimdattr)s ovcheck;
	%(vsignparam)s
	%(simd_ovflchk_extravars)s


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_%(funcmodifier)s(%(intminvalue)s);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data[x]);

		// Check for overflow. 
		%(simd_equ_willoverflow)s
			return 1;
		}

		// The actual SIMD operation. 
		datasliceright = %(simdop)s;

		// Take the max value to get the abs.
		datasliceleft = %(simdmaxop)s(datasliceleft, datasliceright);

		// Store the result.
		%(vstinstr1)s &data[x], %(vstinstr2)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( minval_loop_willoverflow_%(funcmodifier)s(data[x]) ) {return ARR_ERR_OVFL;}
		data[x] = data[x] >= 0 ? data[x] : -data[x];
	}

	return 0;

}


// param_arr_arr
char %(funclabel)s_%(funcmodifier)s_2_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, ovflvec;
	%(ovflsimdattr)s ovcheck;
	%(vsignparam)s
	%(simd_ovflchk_extravars)s


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_%(funcmodifier)s(%(intminvalue)s);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data[x]);

		// Check for overflow. 
		%(simd_equ_willoverflow)s
			return 1;
		}

		// The actual SIMD operation. 
		datasliceright = %(simdop)s;

		// Take the max value to get the abs.
		datasliceleft = %(simdmaxop)s(datasliceleft, datasliceright);

		// Store the result.
		%(vstinstr1)s &dataout[x], %(vstinstr2)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( minval_loop_willoverflow_%(funcmodifier)s(data[x]) ) {return ARR_ERR_OVFL;}
		dataout[x] = data[x] >= 0 ? data[x] : -data[x];
	}

	return 0;

}
#endif

"""


# ==============================================================================


# The neg operations using SIMD. This version checks for overflow.
ops_simdsupport_ovfl_neg = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
*/
// param_arr_none
%(simdplatform)s
char %(funclabel)s_%(funcmodifier)s_1_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, ovflvec;
	%(ovflsimdattr)s ovcheck;
	%(vsignparam)s
	%(simd_ovflchk_extravars)s


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_%(funcmodifier)s(%(intminvalue)s);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data[x]);

		// Check for overflow. 
		%(simd_equ_willoverflow)s
			return 1;
		}

		// The actual SIMD operation. 
		datasliceleft = %(simdop)s;

		// Store the result.
		%(vstinstr1)s &data[x], %(vstinstr2)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( minval_loop_willoverflow_%(funcmodifier)s(data[x]) ) {return ARR_ERR_OVFL;}
		data[x] = -data[x];
	}

	return 0;

}


// param_arr_arr
char %(funclabel)s_%(funcmodifier)s_2_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, ovflvec;
	%(ovflsimdattr)s ovcheck;
	%(vsignparam)s
	%(simd_ovflchk_extravars)s


	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_%(funcmodifier)s(%(intminvalue)s);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data[x]);

		// Check for overflow. 
		%(simd_equ_willoverflow)s
			return 1;
		}

		// The actual SIMD operation. 
		datasliceleft = %(simdop)s;

		// Store the result.
		%(vstinstr1)s &dataout[x], %(vstinstr2)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( minval_loop_willoverflow_%(funcmodifier)s(data[x]) ) {return ARR_ERR_OVFL;}
		dataout[x] = -data[x];
	}

	return 0;

}
#endif

"""


# ==============================================================================


# ==============================================================================


# The operations using SIMD.
ops_simdsupport_float = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
*/
// param_arr_none
%(simdplatform)s
void %(funclabel)s_%(funcmodifier)s_1_simd(Py_ssize_t arraylen, %(arraytype)s *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data[x]);
		// The actual SIMD operation. 
		datasliceleft = %(simdop)s;
		// Store the result.
		%(vstinstr1)s &data[x], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data[x] = %(simdcleanup)s;
	}

}



// param_arr_arr
void %(funclabel)s_%(funcmodifier)s_2_simd(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data[x]);
		// The actual SIMD operation. 
		datasliceleft = %(simdop)s;
		// Store the result.
		%(vstinstr1)s &dataout[x], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		dataout[x] = %(simdcleanup)s;
	}

}
#endif

"""

# ==============================================================================

# The operations using SIMD.
ops_simdsupport_float_ovfl = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   Returns 1 if overflow occurred, else returns 0.
*/
// param_arr_none
%(simdplatform)s
char %(funclabel)s_%(funcmodifier)s_1_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, checkslice;

	%(arraytype)s checkvecresults[%(simdwidth)s];
	%(arraytype)s checksliceinit[%(simdwidth)s] = {0.0};


	// This is used to check for errors by accumulating non-finite values.
	checkslice = %(vldinstr)s checksliceinit);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data[x]);
		// The actual SIMD operation. 
		datasliceleft = %(simdop)s;
		// Store the result.
		%(vstinstr1)s &data[x], datasliceleft);

		// Check the result. None-finite errors should accumulate.
		checkslice = %(simdmul)s(checkslice, datasliceleft);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	%(vstinstr1)s checkvecresults, checkslice);
	for (x = 0; x < %(simdwidth)s; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data[x] = %(simdcleanup)s;
		if (!isfinite(data[x])) {return 1;}
	}

	// Everything was OK.
	return 0;

}



// param_arr_arr
char %(funclabel)s_%(funcmodifier)s_2_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s *dataout) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, checkslice;

	%(arraytype)s checkvecresults[%(simdwidth)s];
	%(arraytype)s checksliceinit[%(simdwidth)s] = {0.0};


	// This is used to check for errors by accumulating non-finite values.
	checkslice = %(vldinstr)s checksliceinit);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data[x]);
		// The actual SIMD operation. 
		datasliceleft = %(simdop)s;
		// Store the result.
		%(vstinstr1)s &dataout[x], datasliceleft);

		// Check the result. None-finite errors should accumulate.
		checkslice = %(simdmul)s(checkslice, datasliceleft);
	}

	// Check the results of the SIMD operations. If all is OK then the
	// results should be all zeros. Any none-finite numbers however will
	// propagate through and accumulate. 
	%(vstinstr1)s checkvecresults, checkslice);
	for (x = 0; x < %(simdwidth)s; x++) {
		if (!isfinite(checkvecresults[x])) {return 1;}
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		dataout[x] = %(simdcleanup)s;
		if (!isfinite(dataout[x])) {return 1;}
	}

	// Everything was OK.
	return 0;

}
#endif

"""


# ==============================================================================



# ==============================================================================


# SIMD call template without integer overflow detection.
SIMD_call = '''\n%(simdplatform)s
	// SIMD version.
	if (ignoreerrors && !nosimd && enoughforsimd(arraylen, %(simdwidth)s) ) {
		if (hasoutputarray) {
			%(funclabel)s_%(funcmodifier)s_2_simd(arraylen, data, dataout);
		} else {
			%(funclabel)s_%(funcmodifier)s_1_simd(arraylen, data);
		}
		return ARR_NO_ERR;
	}
#endif\n'''

# For SIMD operations that have integer overflow detection.
SIMD_call_ovfl = '''\n%(simdplatform)s
	char ovflresult;

	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s) ) {
		// Math error checking disabled.
		if (ignoreerrors) {
			if (hasoutputarray) {
				%(funclabel)s_%(funcmodifier)s_2_simd(arraylen, data, dataout);
			} else {
				%(funclabel)s_%(funcmodifier)s_1_simd(arraylen, data);
			}
			return ARR_NO_ERR;
		} else {
		// Math error checking enabled.
			if (hasoutputarray) {
				ovflresult = %(funclabel)s_%(funcmodifier)s_2_simd_ovfl(arraylen, data, dataout);
			} else {
				ovflresult = %(funclabel)s_%(funcmodifier)s_1_simd_ovfl(arraylen, data);
			}

			if (ovflresult) { 
				return ARR_ERR_OVFL; 
			} else {
				return ARR_NO_ERR;
			}
		}

	} else {
#endif\n'''

# For use with integer overflow detection.
SIMD_call_close = '''\n%(simdplatform)s
	}
#endif\n'''



# ==============================================================================


# ==============================================================================

# This is the set of function calls used to call each operator function.
opscall = """
		// %(funcmodifier)s
		case '%(arraycode)s' : {
			resultcode = %(funclabel)s_%(funcmodifier)s(arraydata.arraylength, arraydata.nosimd, arraydata.array1.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}
"""



uniops_params = """

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;

	// This is used to hold the parsed parameters.
	struct args_params_1 arraydata = ARGSINIT_ONE;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_one(self, args, keywds, 1, "%(funclabel)s");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}

	// Call the C function.
	switch(arraydata.arraytype) {
%(opscall)s
		// We don't know this code.
		default: {
			releasebuffers_one(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_one(arraydata);


	// Signal the errors.
	if (resultcode == ARR_ERR_ARITHMETIC) {
		ErrMsgArithCalc();
		return NULL;
	}

	if (resultcode == ARR_ERR_OVFL) {
		ErrMsgArithOverflowCalc();
		return NULL;
	}


	// Everything was successful.
	Py_RETURN_NONE;

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(%(funclabel)s__doc__,
"%(funclabel)s \\n\\
_____________________________ \\n\\
\\n\\
Calculate %(funclabel)s over the values in an array.  \\n\\
\\n\\
======================  ============================================== \\n\\
Equivalent to:          [%(opcodedocs)s for x in array1] \\n\\
======================  ============================================== \\n\\
\\n\\
======================  ============================================== \\n\\
Array types supported:  %(supportedarrays)s \\n\\
Exceptions raised:      %(matherrors)s \\n\\
======================  ============================================== \\n\\
\\n\\
Call formats: \\n\\
\\n\\
    %(funclabel)s(array1) \\n\\
    %(funclabel)s(array1, outparray) \\n\\
    %(funclabel)s(array1, maxlen=y) \\n\\
    %(funclabel)s(array1, matherrors=False)) \\n\\
    %(funclabel)s(array1, nosimd=False) \\n\\
\\n\\
* array1 - The first input data array to be examined. If no output \\n\\
  array is provided the results will overwrite the input data. \\n\\
* outparray - The output array. This parameter is optional. \\n\\
* maxlen - Limit the length of the array used. This must be a valid \\n\\
  positive integer. If a zero or negative length, or a value which is \\n\\
  greater than the actual length of the array is specified, this \\n\\
  parameter is ignored. \\n\\
* matherrors - If true, arithmetic error checking is disabled. The \\n\\
  default is false. \\n\\
* nosimd - If True, SIMD acceleration is disabled. This parameter is \\n\\
  optional. The default is FALSE.  \\n\\
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


# ==============================================================================


# The SIMD operations used for each function.
# For x86-64.
vsimdop_x86 = {
'b' : {'abs_' : '__builtin_ia32_pabsb128(datasliceleft)', 'neg' : '__builtin_ia32_psignb128(datasliceleft, vsignparam)'},
'h' : {'abs_' : '__builtin_ia32_pabsw128(datasliceleft)', 'neg' : '__builtin_ia32_psignw128(datasliceleft, vsignparam)'},
'i' : {'abs_' : '__builtin_ia32_pabsd128(datasliceleft)', 'neg' : '__builtin_ia32_psignd128(datasliceleft, vsignparam)'},
}


# These are needed for neg for x86 only, as otherwise the vector literal just gets too long.
vsignparam_x86 = {
'b' : {'abs_' : '', 'neg' : 'v16qi vsignparam = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1};'},
'h' : {'abs_' : '', 'neg' : 'v8hi vsignparam = {-1, -1, -1, -1, -1, -1, -1, -1};'},
'i' : {'abs_' : '', 'neg' : 'v4si vsignparam = {-1, -1, -1, -1};'},
}


# Various SIMD instruction information which varies according to array type.
# For x86-64.

simdattr_x86 = {
	'b' : 'v16qi', 
	'h' : 'v8hi', 
	'i' : 'v4si', 
}

ovflsimdattr_x86 = {
	'b' : 'v16qi', 
	'B' : 'v16qi', 
	'h' : 'v8hi', 
	'H' : 'v8hi', 
	'i' : 'v4si', 
	'I' : 'v4si', 
	'f' : 'v4sf',
	'd' : 'v2df',
}

vldinstr_x86 = {
	'b' : '(v16qi) __builtin_ia32_lddqu((char *) ', 
	'h' : '(v8hi) __builtin_ia32_lddqu((char *) ', 
	'i' : '(v4si) __builtin_ia32_lddqu((char *) ', 
}

vstinstr1_x86 = {
	'b' : '__builtin_ia32_storedqu((char *) ',
	'h' : '__builtin_ia32_storedqu((char *) ',
	'i' : '__builtin_ia32_storedqu((char *) ',
}

vstinstr2_x86 = {
	'b' : '',
	'h' : '(v16qi) ',
	'i' : '(v16qi) ',
}

# Equal to instruction for overflow checking.
veqinstr_x86 = {
	'b' : '__builtin_ia32_pcmpeqb128', 
	'h' : '__builtin_ia32_pcmpeqw128', 
	'i' : '__builtin_ia32_pcmpeqd128 ', 
	'f' : '', 
	'd' : '',  
}

# Max instruction.
vmaxops_x86 = {
		'b' : '__builtin_ia32_pmaxsb128',
		'B' : '__builtin_ia32_pmaxub128',
		'h' : '__builtin_ia32_pmaxsw128',
		'H' : '__builtin_ia32_pmaxuw128',
		'i' : '__builtin_ia32_pmaxsd128',
		'I' : '__builtin_ia32_pmaxud128',
		'f' : '__builtin_ia32_maxps',
		'd' : '__builtin_ia32_maxpd',
}


# Total list of which array types are supported by x86 SIMD instructions.
SIMD_x86_support = ('b', 'h', 'i')



# ==============================================================================


# For ARM NEON ARMv7 32 bit.
vsimdop_armv7 = {
'b' : {'abs_' : 'vabs_s8(datasliceleft)', 'neg' : 'vneg_s8(datasliceleft)'},
'h' : {'abs_' : 'vabs_s16(datasliceleft)', 'neg' : 'vneg_s16(datasliceleft)'},
'i' : {'abs_' : 'vabs_s32(datasliceleft)', 'neg' : 'vneg_s32(datasliceleft)'},
'f' : {'abs_' : 'vabs_f32(datasliceleft)', 'neg' : 'vneg_f32(datasliceleft)'},
}

vsignparam_armv7 = {
'b' : {'abs_' : '', 'neg' : ''},
'h' : {'abs_' : '', 'neg' : ''},
'i' : {'abs_' : '', 'neg' : ''},
'f' : {'abs_' : '', 'neg' : ''},
}



# For ARM NEON ARMv7 32 bit.
simdattr_armv7 = {
	'b' : 'int8x8_t', 
	'h' : 'int16x4_t', 
	'i' : 'int32x2_t', 
	'f' : 'float32x2_t', 
}


ovflsimdattr_armv7 = {
	'b' : 'uint8x8_t',
	'B' : 'uint8x8_t',
	'h' : 'uint16x4_t',
	'H' : 'uint16x4_t',
	'f' : '',
}


vldinstr_armv7 = {
	'b' : 'vld1_s8(', 
	'h' : 'vld1_s16(', 
	'i' : 'vld1_s32(', 
	'f' : 'vld1_f32(', 
}

vstinstr1_armv7 = {
	'b' : 'vst1_s8(',
	'h' : 'vst1_s16(',
	'i' : 'vst1_s32(',
	'f' : 'vst1_f32(',
}

vstinstr2_armv7 = {
	'b' : '',
	'h' : '',
	'i' : '',
	'f' : '',
}


# For ARM NEON ARMv7 32 bit.
vmaxops_armv7 = {
		'b' : 'vmax_s8',
		'B' : 'vmax_u8',
		'h' : 'vmax_s16',
		'H' : 'vmax_u16',
		'i' : 'vmax_s32',
		'I' : 'vmax_u32',
		'f' : 'vmax_f32',
}


# Equal to.
veqinstr_armv7 = {
	'b' : 'vceq_s8',
	'B' : 'vceq_u8',
	'h' : 'vceq_s16',
	'H' : 'vceq_u16',
}


# Used to turn vector results into integers so we can examine them.
vreinterpinstr_armv7 = {
	'b' : 'vreinterpret_u64_u8', 
	'B' : 'vreinterpret_u64_u8', 
	'h' : 'vreinterpret_u64_u16', 
	'H' : 'vreinterpret_u64_u16', 
}


# Multiplication, used for checking for math errors.
simdmulop_armv7 = 'vmul_f32'


# Total list of which array types are supported by ARM SIMD instructions.
SIMD_armv7_support = ('b', 'h', 'f')



# ==============================================================================


# For ARM NEON armv8 64 bit.
vsimdop_armv8 = {
'b' : {'abs_' : 'vabsq_s8(datasliceleft)', 'neg' : 'vnegq_s8(datasliceleft)'},
'h' : {'abs_' : 'vabsq_s16(datasliceleft)', 'neg' : 'vnegq_s16(datasliceleft)'},
'i' : {'abs_' : 'vabsq_s32(datasliceleft)', 'neg' : 'vnegq_s32(datasliceleft)'},
'f' : {'abs_' : 'vabsq_f32(datasliceleft)', 'neg' : 'vnegq_f32(datasliceleft)'},
}

vsignparam_armv8 = {
'b' : {'abs_' : '', 'neg' : ''},
'h' : {'abs_' : '', 'neg' : ''},
'i' : {'abs_' : '', 'neg' : ''},
'f' : {'abs_' : '', 'neg' : ''},
}



# For ARM NEON armv8 64 bit.
simdattr_armv8 = {
	'b' : 'int8x16_t', 
	'h' : 'int16x8_t', 
	'i' : 'int32x4_t', 
	'f' : 'float32x4_t', 
}


ovflsimdattr_armv8 = {
	'b' : 'uint8x16_t',
	'B' : 'uint8x16_t',
	'h' : 'uint16x8_t',
	'H' : 'uint16x8_t',
	'i' : 'uint32x4_t',
	'I' : 'uint32x4_t',
	'f' : 'float32x4_t',
}


vldinstr_armv8 = {
	'b' : 'vld1q_s8(', 
	'h' : 'vld1q_s16(', 
	'i' : 'vld1q_s32(', 
	'f' : 'vld1q_f32(', 
}

vstinstr1_armv8 = {
	'b' : 'vst1q_s8(',
	'h' : 'vst1q_s16(',
	'i' : 'vst1q_s32(',
	'f' : 'vst1q_f32(',
}

vstinstr2_armv8 = {
	'b' : '',
	'h' : '',
	'i' : '',
	'f' : '',
}


# For ARM NEON armv8 64 bit.
vmaxops_armv8 = {
		'b' : 'vmaxq_s8',
		'B' : 'vmaxq_u8',
		'h' : 'vmaxq_s16',
		'H' : 'vmaxq_u16',
		'i' : 'vmaxq_s32',
		'I' : 'vmaxq_u32',
		'f' : 'vmaxq_f32',
}

# Equal to.
veqinstr_armv8 = {
	'b' : 'vceqq_s8',
	'B' : 'vceqq_u8',
	'h' : 'vceqq_s16',
	'H' : 'vceqq_u16',
	'i' : 'vceqq_s32',
	'I' : 'vceqq_u32',
	'f' : 'vceqq_f32',
}

# Used to turn vector results into integers so we can examine them.
vreinterpinstr_armv8 = {
	'b' : 'vreinterpretq_u64_u8', 
	'B' : 'vreinterpretq_u64_u8', 
	'h' : 'vreinterpretq_u64_u16', 
	'H' : 'vreinterpretq_u64_u16', 
	'i' : 'vreinterpretq_u64_u32', 
	'I' : 'vreinterpretq_u64_u32', 
	'f' : '', 
}

# Multiplication, used for checking for math errors.
simdmulop_armv8 = 'vmulq_f32'


# Total list of which array types are supported by ARM SIMD instructions.
SIMD_armv8_support = ('b', 'h', 'i','f')


# ==============================================================================

# This is used to finish up array elements which were left over at the
# end of the SIMD operation.
simdcleanup = {'abs_' : 'data[x] >= 0 ? data[x] : -data[x]', 'neg' : '-data[x]'}

# This is the floating point version. This is for float only, and not double.
simdcleanup_float = {'abs_' : 'fabsf(data[x])', 'neg' : '-data[x]'}


# Width of array elements.
simdwidth = {'b' : 'CHARSIMDSIZE',
		'B' : 'CHARSIMDSIZE',
		'h' : 'SHORTSIMDSIZE',
		'H' : 'SHORTSIMDSIZE',
		'i' : 'INTSIMDSIZE',
		'I' : 'INTSIMDSIZE',
		'f' : 'FLOATSIMDSIZE',
		}

# ==============================================================================

# These get substituted into function call templates.
SIMD_platform_x86 = '#if defined(AF_HASSIMD_X86)'
SIMD_platform_x86_ARM = '#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)'
SIMD_platform_x86_ARMv8 = '#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)'
SIMD_platform_ARMv7 = '#if defined(AF_HASSIMD_ARMv7_32BIT)'
SIMD_platform_ARM64v8 = '#if defined(AF_HASSIMD_ARM_AARCH64)'
SIMD_platform_ARM = '#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)'


# ==============================================================================

# Return the platform SIMD enable C macro. 
# This is for the platform independent file, and not the plaform specific
# SIMD files.
def findsimdplatform(arraycode):

	hasx86 = arraycode in SIMD_x86_support
	hasarmv7 = arraycode in SIMD_armv7_support
	hasarmv8 = arraycode in SIMD_armv8_support

	# Only the platforms combinations which are used currently are defined here.
	if hasx86 and hasarmv7 and hasarmv8:
		return SIMD_platform_x86_ARM
	elif hasx86 and (not hasarmv7) and (not hasarmv8):
		return SIMD_platform_x86
	elif hasx86 and (not hasarmv7) and hasarmv8:
		return SIMD_platform_x86_ARMv8
	elif (not hasx86) and (not hasarmv7) and hasarmv8:
		return SIMD_platform_ARM64v8
	elif (not hasx86) and hasarmv7 and hasarmv8:
		return SIMD_platform_ARM
	else:
		return 'Error: Template error, this should not be here.'

# ==============================================================================

# Which opstemplate is valid for which operation. Each math operation requires
# different templates for signed int, unsigned int, and float.
opstemplates = {'neg' : uniops_neg_int,
			'abs_' : uniops_abs_int}

supportedtypes = (codegen_common.signedint + codegen_common.floatarrays)

# ==============================================================================


# The text to include the function specific macros.
funcdefsblock = '''
// Function specific macros and other definitions.
#include "%s"
''' 

# ==============================================================================


# Configuration data.
funclist = [
	{'funcname': 'neg', 
	'c_operator_f': '-data[x]', 'c_operator_d': '-data[x]', 'c_operator_i': '-data[x]', 
	'arraytypes': 'si,f', 
	'opcodedocs': '-x', 
	'matherrors': 'OverflowError,ArithmeticError',
	},

	{'funcname': 'abs_', 
	'c_operator_f': 'fabsf(data[x])', 'c_operator_d': 'fabs(data[x])', 'c_operator_i': 'abs int', 
	'arraytypes': 'si,f', 
	'opcodedocs': 'abs(x)', 
	'matherrors': 'OverflowError',
	},
]

# Function specific templates.
ops_simdsupport_ovfl = {
	'abs_' : ops_simdsupport_ovfl_abs,
	'neg'  : ops_simdsupport_ovfl_neg,
}


# ==============================================================================

def CreateHeader(funcname):
	''' The header and related code. This is returned as two blocks of text.
	'''
	headtext = uniops_head % {'funclabel' : funcname}

	# Function specific includes.
	includextext = funcdefsblock % (funcname + '_defs' + '.h')

	return headtext, includextext


def CreateArrayDataCCode(arraycode, funcname):
	''' Conventional C code for a single data type.
	This returns the data to be written later.
	It returns two blocks of text, the C code and the call code.
	'''

	funcdata = {'funcmodifier' : codegen_common.arraytypes[arraycode].replace(' ', '_'),
			'funclabel' : funcname,
			'arraytype' : codegen_common.arraytypes[arraycode],
			'intminvalue' : codegen_common.minvalue[arraycode],
			'arraycode' : arraycode,
		}


	# Some array types have SIMD support.
	if arraycode in (set(SIMD_x86_support) | set(SIMD_armv7_support) | set(SIMD_armv8_support)):
		simd_call_vals = {'simdwidth' : simdwidth[arraycode], 
			'funclabel' : funcdata['funclabel'], 
			'funcmodifier' : funcdata['funcmodifier'],
			'simdplatform' : findsimdplatform(arraycode),
			}
		funcdata['simd_call'] = SIMD_call_ovfl % simd_call_vals
		funcdata['simd_call_close'] = SIMD_call_close % simd_call_vals
	else:
		funcdata['simd_call'] = ''
		funcdata['simd_call_close'] = ''


	if arraycode == 'f':
		funcdata['copname'] = func['c_operator_f']
		ops_calc = uniops_op_float
	elif arraycode == 'd':
		funcdata['copname'] = func['c_operator_d']
		ops_calc = uniops_op_float
	elif arraycode in codegen_common.signedint:
		funcdata['copname'] = func['c_operator_i']
		ops_calc = opstemplates[funcname]
	else:
		print('Error - Unsupported array code.', arraycode)


	opscalctext = ops_calc % funcdata

	# This is the call to the functions for this array type. This
	# is inserted into another template below.
	opscalltext = opscall % funcdata

	return opscalctext, opscalltext


# Output conventional C code.
# Go through the list of functions being created. 
for func in funclist:

	# Function name.
	funcname = func['funcname']

	# Create the source code based on templates.
	filename = funcname + '.c'
	with open(filename, 'w') as f:
		headtext, includextext = CreateHeader(funcname)
		f.write(headtext)
		f.write(includextext)

		opscalcdatatext = []
		opscalldatatext = []

		# Check each array type. The types of arrays supported must be looked up.
		for arraycode in supportedtypes:
			opscalctext, opscalltext = CreateArrayDataCCode(arraycode, funcname)

			opscalcdatatext.append(opscalctext)
			opscalldatatext.append(opscalltext)

		f.write(''.join(opscalcdatatext))

		supportedarrays = codegen_common.FormatDocsArrayTypes(func['arraytypes'])

		# Write the remaining boilerplate C code. 
		f.write(uniops_params % {'funclabel' : funcname, 
				'opcodedocs' : func['opcodedocs'], 
				'supportedarrays' : supportedarrays,
				'matherrors' : ', '.join(func['matherrors'].split(',')),
				'opscall' : ''.join(opscalldatatext)})



# ==============================================================================


# This outputs helper macros.
macrocodedate = '26-Aug-2021'

# Go through the list of functions being created. 
for func in funclist:

	# Function name.
	funcname = func['funcname']


	outputlist = []

	# Macro definitions.

	# Array type specific macros.
	for arraycode in codegen_common.signedint:

		arraytype = codegen_common.arraytypes[arraycode]
		funcdata = {'arraytype' : arraytype,
			'funcmodifier' : arraytype.replace(' ', '_'),
			'intminvalue' : codegen_common.minvalue[arraycode],
			}
		outputlist.append(intov_macros_signed % funcdata)


	macrofilename = funcname + '_defs' + '.h'

	# Write out the file.
	codegen_common.OutputCHeader(macrofilename, 
		outputlist, 
		'Additional macros for %s' % funcname, 
		'', 
		macrocodedate)



# ==============================================================================

# Write the SIMD code.

# x86
def SetSIMDData_x86(funcname, simdtempplate):
	'''Set the SIMD template data for x86. This is for SIMD without
	overflow checking.
	'''
	outputlist = []

	# Generate code for each array type.
	for arraycode in SIMD_x86_support:

		arraytype = codegen_common.arraytypes[arraycode]

		simd_equ_willoverflow = simd_ovflchk1_x86 % {'veqinstr' : veqinstr_x86[arraycode]}

		# The compare_ops symbols is the same for integer and floating point.
		datavals = {'funclabel' : funcname,
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'intminvalue' : codegen_common.minvalue[arraycode],
					'simdwidth' : simdwidth[arraycode],
					'simdplatform' : SIMD_platform_x86,
					'simdop' : vsimdop_x86[arraycode][funcname],
					'vsignparam' : vsignparam_x86[arraycode][funcname],
					'simdcleanup' : simdcleanup[funcname],
					'simdattr' : simdattr_x86[arraycode],
					'vldinstr' : vldinstr_x86[arraycode],
					'vstinstr1' : vstinstr1_x86[arraycode],
					'vstinstr2' : vstinstr2_x86[arraycode],
					'vstinstr2' : vstinstr2_x86[arraycode],
					'simdmaxop' : vmaxops_x86[arraycode],
					'simd_equ_willoverflow' : simd_equ_willoverflow,
					'ovflsimdattr' : ovflsimdattr_x86[arraycode],
					'simd_ovflchk_extravars' : '',
					}

		# Helper functions.
		outputlist.append(simd_helpers % datavals)

		# Start of function definition.
		outputlist.append(ops_simdsupport % datavals)

		# SIMD with integer overflow detection.
		outputlist.append(simdtempplate % datavals)

	return outputlist


# ARMv7
def SetSIMDData_ARMv7(funcname, simdtempplate):
	'''Set the SIMD template data for ARMv7. This is for SIMD without
	overflow checking.
	'''
	outputlist = []

	# Generate code for each array type.
	for arraycode in SIMD_armv7_support:

		arraytype = codegen_common.arraytypes[arraycode]

		if arraycode in codegen_common.intarrays:
			simd_equ_willoverflow = simd_equ_willoverflow_armv7 % {'veqinstr' : veqinstr_armv7[arraycode],
																'vreinterpinstr' : vreinterpinstr_armv7[arraycode]}
			simdcleanup_op = simdcleanup[funcname]
		else:
			simd_equ_willoverflow = ''
			simdcleanup_op = simdcleanup_float[funcname]

		# The compare_ops symbols is the same for integer and floating point.
		datavals = {'funclabel' : funcname,
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'intminvalue' : codegen_common.minvalue[arraycode],
					'simdwidth' : simdwidth[arraycode],
					'simdplatform' : SIMD_platform_ARMv7,
					'simdop' : vsimdop_armv7[arraycode][funcname],
					'vsignparam' : vsignparam_armv7[arraycode][funcname],
					'simdcleanup' : simdcleanup_op,
					'simdattr' : simdattr_armv7[arraycode],
					'vldinstr' : vldinstr_armv7[arraycode],
					'vstinstr1' : vstinstr1_armv7[arraycode],
					'vstinstr2' : vstinstr2_armv7[arraycode],
					'simdmaxop' : vmaxops_armv7[arraycode],
					'simd_equ_willoverflow' : simd_equ_willoverflow,
					'ovflsimdattr' : ovflsimdattr_armv7[arraycode],
					'simd_ovflchk_extravars' : '',
					'simdmul' : simdmulop_armv7,
					}


		if arraycode in codegen_common.intarrays:
			# Helper functions.
			outputlist.append(simd_helpers % datavals)

			# Start of function definition.
			outputlist.append(ops_simdsupport % datavals)

			# SIMD with integer overflow detection.
			outputlist.append(simdtempplate % datavals)
		else:
			outputlist.append(ops_simdsupport_float % datavals)
			outputlist.append(ops_simdsupport_float_ovfl % datavals)


	return outputlist



# ARMv8
def SetSIMDData_ARMv8(funcname, simdtempplate):
	'''Set the SIMD template data for ARMv8. This is for SIMD without
	overflow checking.
	'''
	outputlist = []

	# Generate code for each array type.
	for arraycode in SIMD_armv8_support:

		arraytype = codegen_common.arraytypes[arraycode]

		if arraycode in codegen_common.intarrays:
			simd_equ_willoverflow = simd_equ_willoverflow_armv8 % {'veqinstr' : veqinstr_armv8[arraycode],
																	'vreinterpinstr' : vreinterpinstr_armv8[arraycode]}
			simdcleanup_op = simdcleanup[funcname]
		else:
			simd_equ_willoverflow = ''
			simdcleanup_op = simdcleanup_float[funcname]

		# The compare_ops symbols is the same for integer and floating point.
		datavals = {'funclabel' : funcname,
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'intminvalue' : codegen_common.minvalue[arraycode],
					'simdwidth' : simdwidth[arraycode],
					'simdplatform' : SIMD_platform_ARM64v8,
					'simdop' : vsimdop_armv8[arraycode][funcname],
					'vsignparam' : vsignparam_armv8[arraycode][funcname],
					'simdcleanup' : simdcleanup_op,
					'simdattr' : simdattr_armv8[arraycode],
					'vldinstr' : vldinstr_armv8[arraycode],
					'vstinstr1' : vstinstr1_armv8[arraycode],
					'vstinstr2' : vstinstr2_armv8[arraycode],
					'simdmaxop' : vmaxops_armv8[arraycode],
					'simd_equ_willoverflow' : simd_equ_willoverflow,
					'ovflsimdattr' : ovflsimdattr_armv8[arraycode],
					'simd_ovflchk_extravars' : simd_ovflchk_extravars_armv8,
					'simdmul' : simdmulop_armv8,
					}

		if arraycode in codegen_common.intarrays:
			# Helper functions.
			outputlist.append(simd_helpers % datavals)

			# Start of function definition.
			outputlist.append(ops_simdsupport % datavals)

			# SIMD with integer overflow detection.
			outputlist.append(simdtempplate % datavals)
		else:
			outputlist.append(ops_simdsupport_float % datavals)
			outputlist.append(ops_simdsupport_float_ovfl % datavals)



	return outputlist



def WriteSIMDCode(funcname, simdplatform, simdfilename, simdcodedate, includextext, outputlist):
	'''This writes out the SIMD code to the .c and .h files.
	'''
	# The SIMD options to select the additional file header info.
	simdoptions = {
	'x86' : ['simddefs'],
	'armv7' : ['simddefs', 'simdmacromsg_armv7'],
	'armv8' : ['simddefs', 'simdmacromsg_armv8'],
	}

	outputfull = [includextext] + outputlist

	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname

	# This outputs the SIMD version.
	codegen_common.OutputSourceCode(funcname + simdfilename + '.c', outputfull, 
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


# Output SIMD code.
for func in funclist:

	funcname = func['funcname']

	# Function specific includes.
	includextext = funcdefsblock % (funcname + '_defs' + '.h')

	# Function specific templates.
	simdtempplate = ops_simdsupport_ovfl[funcname]

	# x86.
	simdcodedate = '22-Mar-2019'
	simdfilename = '_simd_x86'
	outputlist = SetSIMDData_x86(funcname, simdtempplate)
	WriteSIMDCode(funcname, 'x86', simdfilename, simdcodedate, includextext, outputlist)

	simdcodedate = '08-Oct-2019'
	simdfilename = '_simd_armv7'
	outputlist = SetSIMDData_ARMv7(funcname, simdtempplate)
	WriteSIMDCode(funcname, 'armv7', simdfilename, simdcodedate, includextext, outputlist)

	simdcodedate = '25-Mar-2020'
	simdfilename = '_simd_armv8'
	outputlist = SetSIMDData_ARMv8(funcname, simdtempplate)
	WriteSIMDCode(funcname, 'armv8', simdfilename, simdcodedate, includextext, outputlist)


# ==============================================================================
