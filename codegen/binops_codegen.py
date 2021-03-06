#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for math operations. 
# Language: Python 3.4
# Date:     30-Dec-2017
#
###############################################################################
#
#   Copyright 2014 - 2020    Michael Griffin    <m12.griffin@gmail.com>
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

mathops_head = """//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   %(funclabel)s.c
// Purpose:  Calculate the %(funclabel)s of values in an array.
// Language: C
// Date:     15-Nov-2017.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2020    Michael Griffin    <m12.griffin@gmail.com>
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

#include "arrayparams_two.h"

/*--------------------------------------------------------------------------- */
"""

# ==============================================================================

# This is to be included only for those functions which use SIMD.
simdinclude = """

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

# For all binary operators with two arguments.
ops_binop = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD acceleration.
*/
// param_arr_num_none
void %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data1, %(arraytype)s param) {

	// array index counter.
	Py_ssize_t x;
%(simd_call_1)s
	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] %(copname)s param;
	}


}

// param_arr_num_arr
void %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3) {

	// array index counter.
	Py_ssize_t x;
%(simd_call_2)s
	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] %(copname)s param;
	}

}

// param_num_arr_none
void %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, int nosimd, %(arraytype)s param, %(arraytype)s *data2) {

	// array index counter.
	Py_ssize_t x;
%(simd_call_3)s
	for (x = 0; x < arraylen; x++) {
		data2[x] = param %(copname)s data2[x];
	}

}

// param_num_arr_arr
void %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, int nosimd, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3) {

	// array index counter.
	Py_ssize_t x;
%(simd_call_4)s
	for (x = 0; x < arraylen; x++) {
		data3[x] = param %(copname)s data2[x];
	}

}



// param_arr_arr_none
void %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data1, %(arraytype)s *data2) {

	// array index counter.
	Py_ssize_t x;
%(simd_call_5)s
	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] %(copname)s data2[x];
	}

}

// param_arr_arr_arr
void %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3) {

	// array index counter.
	Py_ssize_t x;
%(simd_call_6)s
	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] %(copname)s data2[x];
	}

}
"""


# ==============================================================================


# ==============================================================================



# The actual compare operations using SIMD operations.
ops_simdsupport_x86 = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_X86)
void %(funclabel)s_%(funcmodifier)s_1_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param;
	}
	datasliceright = (%(simdattr)s) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = (%(simdattr)s) __builtin_ia32_lddqu((char *) &data1[index]);
		// The actual SIMD operation. 
		datasliceleft = %(vopinstr)s( %(simdattr_aox)s datasliceleft,  %(simdattr_aox)s datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[index], %(vstinstr2)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] %(copname)s param;
	}

}



// param_arr_num_arr
void %(funclabel)s_%(funcmodifier)s_2_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param;
	}
	datasliceright = (%(simdattr)s) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = (%(simdattr)s) __builtin_ia32_lddqu((char *) &data1[index]);
		// The actual SIMD operation. 
		datasliceleft = %(vopinstr)s( %(simdattr_aox)s datasliceleft,  %(simdattr_aox)s datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[index], %(vstinstr2)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] %(copname)s param;
	}

}



// param_num_arr_none
void %(funclabel)s_%(funcmodifier)s_3_simd(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param;
	}
	datasliceleft = (%(simdattr)s) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceright = (%(simdattr)s) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. 
		datasliceright = %(vopinstr)s( %(simdattr_aox)s datasliceleft,  %(simdattr_aox)s datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data2[index], %(vstinstr2)s datasliceright);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data2[index] = param %(copname)s data2[index];
	}

}



// param_num_arr_arr
void %(funclabel)s_%(funcmodifier)s_4_simd(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param;
	}
	datasliceleft = (%(simdattr)s) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceright = (%(simdattr)s) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. 
		datasliceright = %(vopinstr)s( %(simdattr_aox)s datasliceleft,  %(simdattr_aox)s datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[index], %(vstinstr2)s datasliceright);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = param %(copname)s data2[index];
	}

}



// param_arr_arr_none
void %(funclabel)s_%(funcmodifier)s_5_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = (%(simdattr)s) __builtin_ia32_lddqu((char *) &data1[index]);
		datasliceright = (%(simdattr)s) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. 
		datasliceleft = %(vopinstr)s( %(simdattr_aox)s datasliceleft,  %(simdattr_aox)s datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[index], %(vstinstr2)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] %(copname)s data2[index];
	}

}



// param_arr_arr_arr
void %(funclabel)s_%(funcmodifier)s_6_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = (%(simdattr)s) __builtin_ia32_lddqu((char *) &data1[index]);
		datasliceright = (%(simdattr)s) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. 
		datasliceleft = %(vopinstr)s( %(simdattr_aox)s datasliceleft,  %(simdattr_aox)s datasliceright);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[index], %(vstinstr2)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] %(copname)s data2[index];
	}

}
#endif

"""
# ==============================================================================



# ==============================================================================

# The actual compare operations using SIMD operations.
# This is a special version for x86-64 lshift and rshift only. This 
# implements array shifted by a constant only, as shift by a vector
# (array shifted by elements in another array) do not appear to work
# when handled by GCC built-in functions. 
ops_simdsupport_shift_x86 = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
#if defined(AF_HASSIMD_X86)
void %(funclabel)s_%(funcmodifier)s_1_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = (%(simdattr)s) __builtin_ia32_lddqu((char *) &data1[index]);
		// The actual SIMD operation. 
		datasliceleft = %(vopinstr)s(datasliceleft, (int) param);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[index], %(vstinstr2)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] %(copname)s param;
	}

}



// param_arr_num_arr
void %(funclabel)s_%(funcmodifier)s_2_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = (%(simdattr)s) __builtin_ia32_lddqu((char *) &data1[index]);
		// The actual SIMD operation. 
		datasliceleft = %(vopinstr)s(datasliceleft, (int) param);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[index], %(vstinstr2)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] %(copname)s param;
	}

}
#endif


"""

# ==============================================================================

# ==============================================================================

# The actual compare operations using SIMD operations.
ops_simdsupport_arm = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
%(simdplatform)s
void %(funclabel)s_%(funcmodifier)s_1_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param;
	}
	datasliceright = %(vldinstr)s(compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s(&data1[index]);
		// The actual SIMD operation. 
		datasliceleft = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr)s(&data1[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] %(copname)s param;
	}

}



// param_arr_num_arr
void %(funclabel)s_%(funcmodifier)s_2_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param;
	}
	datasliceright = %(vldinstr)s(compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s(&data1[index]);
		// The actual SIMD operation. 
		datasliceleft = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr)s(&data3[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] %(copname)s param;
	}

}



// param_num_arr_none
void %(funclabel)s_%(funcmodifier)s_3_simd(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param;
	}
	datasliceleft = %(vldinstr)s(compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceright = %(vldinstr)s(&data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceright = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr)s(&data2[index], datasliceright);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data2[index] = param %(copname)s data2[index];
	}

}



// param_num_arr_arr
void %(funclabel)s_%(funcmodifier)s_4_simd(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param;
	}
	datasliceleft = %(vldinstr)s(compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceright = %(vldinstr)s(&data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceright = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr)s(&data3[index], datasliceright);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = param %(copname)s data2[index];
	}

}



// param_arr_arr_none
void %(funclabel)s_%(funcmodifier)s_5_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s(&data1[index]);
		datasliceright = %(vldinstr)s(&data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr)s(&data1[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] %(copname)s data2[index];
	}

}



// param_arr_arr_arr
void %(funclabel)s_%(funcmodifier)s_6_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright;

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s(&data1[index]);
		datasliceright = %(vldinstr)s(&data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr)s(&data3[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] %(copname)s data2[index];
	}

}
#endif

"""

# ==============================================================================

# The actual compare operations using SIMD operations. Shift operations have
# more limited support in terms of the forms of the equations.
ops_simdsupport_shift_arm = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
%(simdplatform)s
void %(funclabel)s_%(funcmodifier)s_1_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft;
	%(simdattr_shft)s datasliceright;
	%(arraytype_shft)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = %(vshift_sign)s(%(arraytype_shft)s)param;
	}
	datasliceright = %(vldinstr_shft)s(compvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s(&data1[index]);
		// The actual SIMD operation. 
		datasliceleft = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr)s(&data1[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] %(copname)s param;
	}

}



// param_arr_num_arr
void %(funclabel)s_%(funcmodifier)s_2_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft;
	%(simdattr_shft)s datasliceright;
	%(arraytype_shft)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = %(vshift_sign)s(%(arraytype_shft)s)param;
	}
	datasliceright = %(vldinstr_shft)s(compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s(&data1[index]);
		// The actual SIMD operation. 
		datasliceleft = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr)s(&data3[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] %(copname)s param;
	}

}
#endif

"""

# ==============================================================================



# ==============================================================================

# This is the set of function calls used to call each operator function.
binopscall = """
		// %(funcmodifier)s
		case '%(arraycode)s' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					%(funclabel)s_%(funcmodifier)s_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.%(arraycode)s, arraydata.param.%(arraycode)s);
					break;
				}
				case param_arr_num_arr : {
					%(funclabel)s_%(funcmodifier)s_2(arraydata.arraylength, arraydata.nosimd, arraydata.array1.%(arraycode)s, arraydata.param.%(arraycode)s, arraydata.array3.%(arraycode)s);
					break;
				}
				case param_num_arr_none : {
					%(funclabel)s_%(funcmodifier)s_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.%(arraycode)s, arraydata.array2.%(arraycode)s);
					break;
				}
				case param_num_arr_arr : {
					%(funclabel)s_%(funcmodifier)s_4(arraydata.arraylength, arraydata.nosimd, arraydata.param.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.array3.%(arraycode)s);
					break;
				}
				case param_arr_arr_none : {
					%(funclabel)s_%(funcmodifier)s_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.%(arraycode)s, arraydata.array2.%(arraycode)s);
					break;
				}
				case param_arr_arr_arr : {
					%(funclabel)s_%(funcmodifier)s_6(arraydata.arraylength, arraydata.nosimd, arraydata.array1.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.array3.%(arraycode)s);
					break;
				}
			}
			break;
		}
"""


# ==============================================================================

binops_params = """
/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// This is used to hold the parsed parameters.
	struct args_params_2 arraydata = ARGSINIT_TWO;


	// -----------------------------------------------------


	// Get the parameters passed from Python. Does not have "matherrors". 
	// Some functions using this template do have "nosimd".
	arraydata = getparams_two(self, args, keywds, 0%(hasnosimd)s, "%(funclabel)s");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}

	// Call the C function.
	switch(arraydata.arraytype) {
%(opscall)s
		// Wrong array type code.
		default: {
			releasebuffers_two(arraydata);
			ErrMsgTypeExpectFloat();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_two(arraydata);


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
Equivalent to:          [x %(opcodedocs)s param for x in array1] \\n\\
or                      [param %(opcodedocs)s x for x in array1] \\n\\
or                      [x %(opcodedocs)s y for x,y in zip(array1, array2)] \\n\\
======================  ============================================== \\n\\
\\n\\
======================  ============================================== \\n\\
Array types supported:  %(supportedarrays)s \\n\\
Exceptions raised:      %(matherrors)s \\n\\
======================  ============================================== \\n\\
\\n\\
Call formats: \\n\\
\\n\\
  %(funclabel)s(array1, param) \\n\\
  %(funclabel)s(array1, param, outparray) \\n\\
  %(funclabel)s(param, array1) \\n\\
  %(funclabel)s(param, array1, outparray) \\n\\
  %(funclabel)s(array1, array2) \\n\\
  %(funclabel)s(array1, array2, outparray) \\n\\
  %(funclabel)s(array1, param, maxlen=y) \\n\\
%(helpsimd1)s\\n\\
\\n\\
* array1 - The first input data array to be examined. If no output \\n\\
  array is provided the results will overwrite the input data.  \\n\\
* param - A non-array numeric parameter.  \\n\\
* array2 - A second input data array. Each element in this array is  \\n\\
  applied to the corresponding element in the first array.  \\n\\
* outparray - The output array. This parameter is optional.  \\n\\
* maxlen - Limit the length of the array used. This must be a valid  \\n\\
  positive integer. If a zero or negative length, or a value which is  \\n\\
  greater than the actual length of the array is specified, this  \\n\\
  parameter is ignored.  \\n\\
%(helpsimd2)s");


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


# SIMD call, version 1.
SIMD_call_1 = '''\n%(simdplatform)s
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		%(funclabel)s_%(funcmodifier)s_1_simd(arraylen, data1, param);
		return;
	}
#endif\n'''


# SIMD call, version 2.
SIMD_call_2 = '''\n%(simdplatform)s
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		%(funclabel)s_%(funcmodifier)s_2_simd(arraylen, data1, param, data3);
		return;
	}
#endif\n'''


# SIMD call, version 3.
SIMD_call_3 = '''\n%(simdplatform)s
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		%(funclabel)s_%(funcmodifier)s_3_simd(arraylen, param, data2);
		return;
	}
#endif\n'''


# SIMD call, version 4.
SIMD_call_4 = '''\n%(simdplatform)s
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		%(funclabel)s_%(funcmodifier)s_4_simd(arraylen, param, data2, data3);
		return;
	}
#endif\n'''


# SIMD call, version 5.
SIMD_call_5 = '''\n%(simdplatform)s
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		%(funclabel)s_%(funcmodifier)s_5_simd(arraylen, data1, data2);
		return;
	}
#endif\n'''


# SIMD call, version 6.
SIMD_call_6 = '''\n%(simdplatform)s
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		%(funclabel)s_%(funcmodifier)s_6_simd(arraylen, data1, data2, data3);
		return;
	}
#endif\n'''


SIMD_call_hassimd = {
	'simd_call_1' : SIMD_call_1,
	'simd_call_2' : SIMD_call_2,
	'simd_call_3' : SIMD_call_3,
	'simd_call_4' : SIMD_call_4,
	'simd_call_5' : SIMD_call_5,
	'simd_call_6' : SIMD_call_6
}

SIMD_call_nosimd = {
	'simd_call_1' : '',
	'simd_call_2' : '',
	'simd_call_3' : '',
	'simd_call_4' : '',
	'simd_call_5' : '',
	'simd_call_6' : ''
}


SIMD_call_hassimd_shift = {
	'simd_call_1' : SIMD_call_1,
	'simd_call_2' : SIMD_call_2,
	'simd_call_3' : '',
	'simd_call_4' : '',
	'simd_call_5' : '',
	'simd_call_6' : ''
}


# ==============================================================================


# The following are used to fill in template data which handles whether
# a function requires SIMD related template data or not. 
funcwithsimd = {'hasnosimd' : ', 1',
		'helpsimd1' : '  %(funclabel)s(array1, param, nosimd=False) \\n\\', 
		'helpsimd2' : '''* nosimd - If True, SIMD acceleration is disabled. This parameter is \\n\\
  optional. The default is FALSE.  \\n\\\n'''
		}

# ==============================================================================

# x86 SIMD instructions.

simdattr_x86 = {
	'b' : 'v16qi', 
	'B' : 'v16qi', 
	'h' : 'v8hi', 
	'H' : 'v8hi', 
	'i' : 'v4si', 
	'I' : 'v4si', 
}

simdattr_aox_x86 = {
	'lshift' : '', 
	'rshift' : '',
	'and_' : '(v2di)', 
	'or_' : '(v2di)', 
	'xor' : '(v2di)',
}


vldinstr_x86 = {
	'b' : '(v16qi) __builtin_ia32_lddqu((char *) ', 
	'B' : '(v16qi) __builtin_ia32_lddqu((char *) ', 
	'h' : '(v8hi) __builtin_ia32_lddqu((char *) ', 
	'H' : '(v8hi) __builtin_ia32_lddqu((char *) ', 
	'i' : '(v4si) __builtin_ia32_lddqu((char *) ', 
	'I' : '(v4si) __builtin_ia32_lddqu((char *) ', 
}


vstinstr2_x86 = {
	'b' : '', 
	'B' : '', 
	'h' : '(v16qi) ', 
	'H' : '(v16qi) ', 
	'i' : '(v16qi) ', 
	'I' : '(v16qi) ', 
}

# SIMD operations.

vsimdop_x86 = {
	'b' : {'and_' : '(v16qi) __builtin_ia32_pand128', 
			'or_' : '(v16qi) __builtin_ia32_por128', 
			'xor' : '(v16qi) __builtin_ia32_pxor128',
			},
	'B' : {'and_' : '(v16qi) __builtin_ia32_pand128', 
			'or_' : '(v16qi) __builtin_ia32_por128', 
			'xor' : '(v16qi) __builtin_ia32_pxor128',
			},
	'h' : {'lshift' : '__builtin_ia32_psllwi128', 
			'and_' : '(v8hi) __builtin_ia32_pand128', 
			'or_' : '(v8hi) __builtin_ia32_por128', 
			'xor' : '(v8hi) __builtin_ia32_pxor128',
			},
	'H' : {'lshift' : '__builtin_ia32_psllwi128', 
			'rshift' : '__builtin_ia32_psrlwi128',
			'and_' : '(v8hi) __builtin_ia32_pand128', 
			'or_' : '(v8hi) __builtin_ia32_por128', 
			'xor' : '(v8hi) __builtin_ia32_pxor128',
			},
	'i' : {'lshift' : '__builtin_ia32_pslldi128', 
			'and_' : '(v4si) __builtin_ia32_pand128', 
			'or_' : '(v4si) __builtin_ia32_por128', 
			'xor' : '(v4si) __builtin_ia32_pxor128',
			},
	'I' : {'lshift' : '__builtin_ia32_pslldi128', 
			'rshift' : '__builtin_ia32_psrldi128',
			'and_' : '(v4si) __builtin_ia32_pand128', 
			'or_' : '(v4si) __builtin_ia32_por128', 
			'xor' : '(v4si) __builtin_ia32_pxor128',
			},
}


# A list of which array types are supported by x86 SIMD instructions.
def x86_simdtypes(funcname):
	return [x for x in vsimdop_x86.keys() if funcname in vsimdop_x86[x]]

# ==============================================================================

# For ARM NEON ARMv7 32 bit.

simdattr_armv7 = {
	'b' : 'int8x8_t', 
	'B' : 'uint8x8_t', 
	'h' : 'int16x4_t', 
	'H' : 'uint16x4_t', 
	'i' : 'int32x2_t', 
	'I' : 'uint32x2_t', 
}

vldinstr_armv7 = {
	'b' : 'vld1_s8', 
	'B' : 'vld1_u8', 
	'h' : 'vld1_s16', 
	'H' : 'vld1_u16', 
	'i' : 'vld1_s32', 
	'I' : 'vld1_u32', 
}

vstinstr_armv7 = {
	'b' : 'vst1_s8', 
	'B' : 'vst1_u8', 
	'h' : 'vst1_s16', 
	'H' : 'vst1_u16', 
	'i' : 'vst1_s32', 
	'I' : 'vst1_u32', 
}

# Left and right shift use the same instruction, with the sign of the
# second parameter controlling the shift direction.
vopinstr_armv7 = {
	'b' : {'lshift' : 'vshl_s8', 
			'rshift' : 'vshl_s8',
			'and_' : 'vand_s8', 
			'or_' : 'vorr_s8', 
			'xor' : 'veor_s8',
			},
	'B' : {'lshift' : 'vshl_u8', 
			'rshift' : 'vshl_u8',
			'and_' : 'vand_u8', 
			'or_' : 'vorr_u8', 
			'xor' : 'veor_u8',
			},
	'h' : {'lshift' : 'vshl_s16', 
			'rshift' : 'vshl_s16',
			'and_' : 'vand_s16', 
			'or_' : 'vorr_s16', 
			'xor' : 'veor_s16',
			},
	'H' : {'lshift' : 'vshl_u16', 
			'rshift' : 'vshl_u16',
			'and_' : 'vand_u16', 
			'or_' : 'vorr_u16', 
			'xor' : 'veor_u16',
			},
	'i' : {'lshift' : 'vshl_s32', 
			'rshift' : 'vshl_s32',
			'and_' : 'vand_s32', 
			'or_' : 'vorr_s32', 
			'xor' : 'veor_s32',
			},
	'I' : {'lshift' : 'vshl_u32', 
			'rshift' : 'vshl_u32',
			'and_' : 'vand_u32', 
			'or_' : 'vorr_u32', 
			'xor' : 'veor_u32',
			},
}


# Shift instructions need additional parameters. The second parameter
# is always a signed value, with a negative producing a right shift.
simdattr_shft_armv7 = {
	'b' : 'int8x8_t', 
	'B' : 'int8x8_t', 
	'h' : 'int16x4_t', 
	'H' : 'int16x4_t', 
	'i' : 'int32x2_t', 
	'I' : 'int32x2_t', 
}


vldinstr_shft_armv7 = {
	'b' : 'vld1_s8', 
	'B' : 'vld1_s8', 
	'h' : 'vld1_s16', 
	'H' : 'vld1_s16', 
	'i' : 'vld1_s32', 
	'I' : 'vld1_s32', 
}


# Total list of which array types are supported by ARM SIMD instructions.
SIMD_armv7_support = simdattr_armv7.keys()

# ==============================================================================

# For ARM NEON armv8 64 bit.

simdattr_armv8 = {
	'b' : 'int8x16_t', 
	'B' : 'uint8x16_t', 
	'h' : 'int16x8_t', 
	'H' : 'uint16x8_t', 
	'i' : 'int32x4_t', 
	'I' : 'uint32x4_t', 
}

vldinstr_armv8 = {
	'b' : 'vld1q_s8', 
	'B' : 'vld1q_u8', 
	'h' : 'vld1q_s16', 
	'H' : 'vld1q_u16', 
	'i' : 'vld1q_s32', 
	'I' : 'vld1q_u32', 
}

vstinstr_armv8 = {
	'b' : 'vst1q_s8', 
	'B' : 'vst1q_u8', 
	'h' : 'vst1q_s16', 
	'H' : 'vst1q_u16', 
	'i' : 'vst1q_s32', 
	'I' : 'vst1q_u32', 
}

# Left and right shift use the same instruction, with the sign of the
# second parameter controlling the shift direction.
vopinstr_armv8 = {
	'b' : {'lshift' : 'vshlq_s8', 
			'rshift' : 'vshlq_s8',
			'and_' : 'vandq_s8', 
			'or_' : 'vorrq_s8', 
			'xor' : 'veorq_s8',
			},
	'B' : {'lshift' : 'vshlq_u8', 
			'rshift' : 'vshlq_u8',
			'and_' : 'vandq_u8', 
			'or_' : 'vorrq_u8', 
			'xor' : 'veorq_u8',
			},
	'h' : {'lshift' : 'vshlq_s16', 
			'rshift' : 'vshlq_s16',
			'and_' : 'vandq_s16', 
			'or_' : 'vorrq_s16', 
			'xor' : 'veorq_s16',
			},
	'H' : {'lshift' : 'vshlq_u16', 
			'rshift' : 'vshlq_u16',
			'and_' : 'vandq_u16', 
			'or_' : 'vorrq_u16', 
			'xor' : 'veorq_u16',
			},
	'i' : {'lshift' : 'vshlq_s32', 
			'rshift' : 'vshlq_s32',
			'and_' : 'vandq_s32', 
			'or_' : 'vorrq_s32', 
			'xor' : 'veorq_s32',
			},
	'I' : {'lshift' : 'vshlq_u32', 
			'rshift' : 'vshlq_u32',
			'and_' : 'vandq_u32', 
			'or_' : 'vorrq_u32', 
			'xor' : 'veorq_u32',
			},
}


# Shift instructions need additional parameters. The second parameter
# is always a signed value, with a negative producing a right shift.
simdattr_shft_armv8 = {
	'b' : 'int8x16_t', 
	'B' : 'int8x16_t', 
	'h' : 'int16x8_t', 
	'H' : 'int16x8_t', 
	'i' : 'int32x4_t', 
	'I' : 'int32x4_t', 
}


vldinstr_shft_armv8 = {
	'b' : 'vld1q_s8', 
	'B' : 'vld1q_s8', 
	'h' : 'vld1q_s16', 
	'H' : 'vld1q_s16', 
	'i' : 'vld1q_s32', 
	'I' : 'vld1q_s32', 
}

# Total list of which array types are supported by ARM SIMD instructions.
SIMD_armv8_support = simdattr_armv8.keys()

# ==============================================================================

# ==============================================================================

# For all versions of ARM NEON SIMD.

arraytype_shft_arm = {
	'b' : 'signed char', 
	'B' : 'signed char', 
	'h' : 'signed short', 
	'H' : 'signed short', 
	'i' : 'signed int', 
	'I' : 'signed int', 
}


vshift_sign_arm = {
	'lshift' : '',
	'rshift' : '-',
	'and_' : '',
	'or_' : '',
	'xor' : '',
}


# ==============================================================================

# Width of array elements.
simdwidth = {'b' : 'CHARSIMDSIZE',
		'B' : 'CHARSIMDSIZE',
		'h' : 'SHORTSIMDSIZE',
		'H' : 'SHORTSIMDSIZE',
		'i' : 'INTSIMDSIZE',
		'I' : 'INTSIMDSIZE',
		}

# ==============================================================================


# These get substituted into function call templates.
SIMD_platform_x86 = '#if defined(AF_HASSIMD_X86)'
SIMD_platform_x86_ARM = '#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)'
SIMD_platform_x86_ARMv8 = '#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)'
SIMD_platform_ARMv7 = '#if defined(AF_HASSIMD_ARMv7_32BIT)'
SIMD_platform_ARM64v8 = '#if defined(AF_HASSIMD_ARM_AARCH64)'
SIMD_platform_ARM64v7v8 = '#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)'


# ==============================================================================

# Return the platform SIMD enable C macro. 
# This is for the platform independent file, and not the plaform specific
# SIMD files.
def findsimdplatform(arraycode, funcname):

	hasx86 = arraycode in x86_simdtypes(funcname)
	hasarmv7 = arraycode in SIMD_armv7_support
	hasarmv8 = arraycode in SIMD_armv8_support

	# Only the platforms combinations which are used currently are defined here.
	if hasx86 and hasarmv7 and hasarmv8:
		return SIMD_platform_x86_ARM
	elif hasx86 and (not hasarmv7) and (not hasarmv8):
		return SIMD_platform_x86
	elif hasx86 and (not hasarmv7) and hasarmv8:
		return SIMD_platform_x86_ARMv8
	elif (not hasx86) and (hasarmv7 and hasarmv8):
		return SIMD_platform_ARM64v7v8
	else:
		return 'Error: Template error, this should not be here.'

# ==============================================================================

# ==============================================================================


# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.

funclist = [x for x in oplist if x['c_code_template'] in ('template_binop', 'template_binop2')]


# ==============================================================================

for func in funclist:

	# The name of the arrayfunc function.
	funcname = func['funcname']

	# Create the source code based on templates.
	filename = funcname + '.c'
	with open(filename, 'w') as f:
		funcdata = {'funclabel' : funcname}
		f.write(mathops_head % {'funclabel' : funcname})

		# This includes the SIMD support data.
		f.write(simdinclude % {'funclabel' : funcname})

		opscalltext = []


		# Check each array type.
		for arraycode in codegen_common.intarrays:
			funcdata['funcmodifier'] = codegen_common.arraytypes[arraycode].replace(' ', '_')
			funcdata['arraytype'] = codegen_common.arraytypes[arraycode]
			funcdata['copname'] = func['c_operator_i']

			# Insert the correct SIMD call template in functions which have SIMD versions.
			# For x86, there is a special case due to compiler problems on this platform.
			if arraycode in (set(x86_simdtypes(funcname)) | set(SIMD_armv7_support) | set(SIMD_armv8_support)):

				simd_call_vals = {'simdwidth' : simdwidth[arraycode], 
							'funclabel' : funcdata['funclabel'], 
							'funcmodifier' : funcdata['funcmodifier'],
							'simdplatform' : findsimdplatform(arraycode, funcname)}

					# This updates the SIMD call templates with the values for this array type.
				if funcname in ('lshift', 'rshift'):
					# lshift and rshift do not have SIMD for all call formats.
					funcdata.update(dict([(x,y % simd_call_vals) for x,y in SIMD_call_hassimd_shift.items()]))
				else:
					# Other functions have SIMD for all call formats.
					funcdata.update(dict([(x,y % simd_call_vals) for x,y in SIMD_call_hassimd.items()]))
			else:
				# For array types without SIMD support.
				funcdata.update(SIMD_call_nosimd)

			f.write(ops_binop % funcdata)

			# This is the call to the functions for this array type. This
			# is inserted into another template below.
			funcdata['arraycode'] = arraycode
			opscalltext.append(binopscall % funcdata)

		supportedarrays = codegen_common.FormatDocsArrayTypes(func['arraytypes'])


		paramsdata = {'funclabel' : funcname, 
				'opcodedocs' : func['opcodedocs'], 
				'supportedarrays' : supportedarrays,
				'matherrors' : ', '.join(func['matherrors'].split(',')),
				'opscall' : ''.join(opscalltext),
				'hasnosimd' : funcwithsimd['hasnosimd'],
				'helpsimd1' : funcwithsimd['helpsimd1'] % {'funclabel' : funcname},
				'helpsimd2' : funcwithsimd['helpsimd2'],
				}
		f.write(binops_params % paramsdata)


# ==============================================================================


# ==============================================================================

# The original date of the x86-64 SIMD C code.
simdcodedate = '12-Mar-2019'
simdfilename = '_simd_x86'

# This outputs the SIMD version.

for func in funclist:

	outputlist = []

	funcname = func['funcname']

	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname


	# Output the generated code.
	for arraycode in x86_simdtypes(funcname):

		arraytype = codegen_common.arraytypes[arraycode]

		# The compare_ops symbols is the same for integer and floating point.
		datavals = {'funclabel' : funcname,
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'simdwidth' : simdwidth[arraycode],
					'simdattr' : simdattr_x86[arraycode],
					'vldinstr' : vldinstr_x86[arraycode],
					'vstinstr2' : vstinstr2_x86[arraycode],
					'vopinstr' : vsimdop_x86[arraycode][funcname],
					'simdattr_aox' : simdattr_aox_x86[funcname],
					'copname' :  func['c_operator_i'],
					}


		# Start of function definition.
		if funcname in ('lshift', 'rshift'):
			outputlist.append(ops_simdsupport_shift_x86 % datavals)
		else:
			outputlist.append(ops_simdsupport_x86 % datavals)



	# This outputs the SIMD version.
	codegen_common.OutputSourceCode(funcname + simdfilename + '.c', outputlist, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate,
		'', ['simddefs'])


	# Output the .h header file.
	headedefs = codegen_common.GenSIMDCHeaderText(outputlist, funcname)

	# Write out the file.
	codegen_common.OutputCHeader(funcname + simdfilename + '.h', headedefs, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate)

# ==============================================================================



# ==============================================================================

# The original date of the SIMD C code.
simdcodedate = '05-Oct-2019'
simdfilename = '_simd_armv7'

# This outputs the SIMD version for ARM NEON ARMv7 32 bit.

for func in funclist:

	outputlist = []

	funcname = func['funcname']

	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname


	# Output the generated code.
	for arraycode in SIMD_armv7_support:

		arraytype = codegen_common.arraytypes[arraycode]

		# The compare_ops symbols is the same for integer and floating point.
		datavals = {'funclabel' : funcname,
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'simdwidth' : simdwidth[arraycode],
					'simdattr' : simdattr_armv7[arraycode],
					'vldinstr' : vldinstr_armv7[arraycode],
					'vstinstr' : vstinstr_armv7[arraycode],
					'vopinstr' : vopinstr_armv7[arraycode][funcname],
					'simdattr_shft' : simdattr_shft_armv7[arraycode],
					'arraytype_shft' : arraytype_shft_arm[arraycode],
					'vldinstr_shft' : vldinstr_shft_armv7[arraycode],
					'vshift_sign' : vshift_sign_arm[funcname],
					'copname' :  func['c_operator_i'],
					'simdplatform' : SIMD_platform_ARMv7,
					}

		
		# Start of function definition.
		if funcname in ('lshift', 'rshift'):
			outputlist.append(ops_simdsupport_shift_arm % datavals)
		else:
			outputlist.append(ops_simdsupport_arm % datavals)



	# This outputs the SIMD version.
	codegen_common.OutputSourceCode(funcname + simdfilename + '.c', outputlist, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate,
		'', ['simddefs', 'simdmacromsg_armv7'])


	# Output the .h header file.
	headedefs = codegen_common.GenSIMDCHeaderText(outputlist, funcname)

	# Write out the file.
	codegen_common.OutputCHeader(funcname + simdfilename + '.h', headedefs, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate)

# ==============================================================================



# ==============================================================================

# The original date of the SIMD C code.
simdcodedate = '24-Mar-2020'
simdfilename = '_simd_armv8'

# This outputs the SIMD version for ARM NEON ARMv8 64 bit.

for func in funclist:

	outputlist = []

	funcname = func['funcname']

	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname


	# Output the generated code.
	for arraycode in SIMD_armv8_support:

		arraytype = codegen_common.arraytypes[arraycode]

		# The compare_ops symbols is the same for integer and floating point.
		datavals = {'funclabel' : funcname,
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'simdwidth' : simdwidth[arraycode],
					'simdattr' : simdattr_armv8[arraycode],
					'vldinstr' : vldinstr_armv8[arraycode],
					'vstinstr' : vstinstr_armv8[arraycode],
					'vopinstr' : vopinstr_armv8[arraycode][funcname],
					'simdattr_shft' : simdattr_shft_armv8[arraycode],
					'arraytype_shft' : arraytype_shft_arm[arraycode],
					'vldinstr_shft' : vldinstr_shft_armv8[arraycode],
					'vshift_sign' : vshift_sign_arm[funcname],
					'copname' :  func['c_operator_i'],
					'simdplatform' : SIMD_platform_ARM64v8,
					}

		
		# Start of function definition.
		if funcname in ('lshift', 'rshift'):
			outputlist.append(ops_simdsupport_shift_arm % datavals)
		else:
			outputlist.append(ops_simdsupport_arm % datavals)



	# This outputs the SIMD version.
	codegen_common.OutputSourceCode(funcname + simdfilename + '.c', outputlist, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate,
		'', ['simddefs', 'simdmacromsg_armv8'])


	# Output the .h header file.
	headedefs = codegen_common.GenSIMDCHeaderText(outputlist, funcname)

	# Write out the file.
	codegen_common.OutputCHeader(funcname + simdfilename + '.h', headedefs, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate)

# ==============================================================================


