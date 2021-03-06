#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for math operations. 
#			parameter.
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

%(includeoptions)s

/*--------------------------------------------------------------------------- */
"""

# ==============================================================================

# For floating point.
ops_op_float = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_1)s
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s param;
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_2)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s param;
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_3)s
		for (x = 0; x < arraylen; x++) {
			data2[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data2[x] = param %(copname)s data2[x];
			if (!isfinite(data2[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_4)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = param %(copname)s data2[x];
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_5)s
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s data2[x];
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_6)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s data2[x];
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}
"""


# ==============================================================================

# For unsigned integer.
ops_add_uint = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_1)s
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		ovtmp = %(intmaxvalue)s - param;
		for (x = 0; x < arraylen; x++) {
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] %(copname)s param;
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_2)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		ovtmp = %(intmaxvalue)s - param;
		for (x = 0; x < arraylen; x++) {
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] %(copname)s param;
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_3)s
		for (x = 0; x < arraylen; x++) {
			data2[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			ovtmp = %(intmaxvalue)s - data2[x];
			if (param > ovtmp) {return ARR_ERR_OVFL;}
			data2[x] = param %(copname)s data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_4)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			ovtmp = %(intmaxvalue)s - data2[x];
			if (param > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = param %(copname)s data2[x];
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_5)s
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			ovtmp = %(intmaxvalue)s - data2[x];
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] %(copname)s data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_6)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			ovtmp = %(intmaxvalue)s - data2[x];
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] %(copname)s data2[x];
		}
	}
	return ARR_NO_ERR;

}
"""


# ==============================================================================

# For signed integer.
ops_add_int = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_1)s
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			return ARR_NO_ERR;
		}
		if (param > 0) {
			ovtmp = %(intmaxvalue)s - param;
			for (x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] %(copname)s param; 
			}
		}
		if (param < 0) {
			ovtmp = %(intminvalue)s - param;
			for (x = 0; x < arraylen; x++) {
				if (data1[x] < ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] %(copname)s param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_2)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for (x = 0; x < arraylen; x++) {
				data3[x] = data1[x]; 
			}
		}
		if (param > 0) {
			ovtmp = %(intmaxvalue)s - param;
			for (x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] %(copname)s param; 
			}
		}
		if (param < 0) {
			ovtmp = %(intminvalue)s - param;
			for (x = 0; x < arraylen; x++) {
				if (data1[x] < ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] %(copname)s param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_3)s
		for (x = 0; x < arraylen; x++) {
			data2[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			return ARR_NO_ERR;
		}
		if (param > 0) {
			ovtmp = %(intmaxvalue)s - param;
			for (x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = data2[x] %(copname)s param; 
			}
		}
		if (param < 0) {
			ovtmp = %(intminvalue)s - param;
			for (x = 0; x < arraylen; x++) {
				if (data2[x] < ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = data2[x] %(copname)s param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_4)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for (x = 0; x < arraylen; x++) {
				data3[x] = data2[x]; 
			}
		}
		if (param > 0) {
			ovtmp = %(intmaxvalue)s - param;
			for (x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data2[x] %(copname)s param; 
			}
		}
		if (param < 0) {
			ovtmp = %(intminvalue)s - param;
			for (x = 0; x < arraylen; x++) {
				if (data2[x] < ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data2[x] %(copname)s param; 
			}
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_5)s
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && (data1[x] > (%(intmaxvalue)s - data2[x]))) {return ARR_ERR_OVFL;}
			if ((data2[x] < 0) && (data1[x] < (%(intminvalue)s - data2[x]))) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] %(copname)s data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_6)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && (data1[x] > (%(intmaxvalue)s - data2[x]))) {return ARR_ERR_OVFL;}
			if ((data2[x] < 0) && (data1[x] < (%(intminvalue)s - data2[x]))) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] %(copname)s data2[x];
		}
	}
	return ARR_NO_ERR;

}
"""

# ==============================================================================

# For unsigned integer.
ops_sub_uint = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_1)s
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			if (data1[x] < param) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] %(copname)s param;
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_2)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			if (data1[x] < param) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] %(copname)s param;
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_3)s
		for (x = 0; x < arraylen; x++) {
			data2[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			if (param < data2[x]) {return ARR_ERR_OVFL;}
			data2[x] = param %(copname)s data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_4)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			if (param < data2[x]) {return ARR_ERR_OVFL;}
			data3[x] = param %(copname)s data2[x];
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_5)s
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			if (data1[x] < data2[x]) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] %(copname)s data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_6)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			if (data1[x] < data2[x]) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] %(copname)s data2[x];
		}
	}
	return ARR_NO_ERR;

}
"""


# ==============================================================================

# ==============================================================================

# For signed integer.
ops_sub_int = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_1)s
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			return ARR_NO_ERR;
		}
		if (param > 0) {
			ovtmp = %(intminvalue)s + param;
			for (x = 0; x < arraylen; x++) {
				if (data1[x] < ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] %(copname)s param; 
			}
		}
		if (param < 0) {
			ovtmp = %(intmaxvalue)s + param;
			for (x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] %(copname)s param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_2)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for (x = 0; x < arraylen; x++) {
				data3[x] = data1[x]; 
			}
		}
		if (param > 0) {
			ovtmp = %(intminvalue)s + param;
			for (x = 0; x < arraylen; x++) {
				if (data1[x] < ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] %(copname)s param; 
			}
		}
		if (param < 0) {
			ovtmp = %(intmaxvalue)s + param;
			for (x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] %(copname)s param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_3)s
		for (x = 0; x < arraylen; x++) {
			data2[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			for (x = 0; x < arraylen; x++) {
				if (data2[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
				data2[x] = -data2[x]; 
			}
		}
		if (param > 0) {
			ovtmp = param - %(intmaxvalue)s;
			for (x = 0; x < arraylen; x++) {
				if (data2[x] < ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = param %(copname)s data2[x]; 
			}
		}
		if (param < 0) {
			ovtmp = param - %(intminvalue)s;
			for (x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = param %(copname)s data2[x]; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_4)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			for (x = 0; x < arraylen; x++) {
				if (data2[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
				data3[x] = -data2[x]; 
			}
		}
		if (param > 0) {
			ovtmp = param - %(intmaxvalue)s;
			for (x = 0; x < arraylen; x++) {
				if (data2[x] < ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = param %(copname)s data2[x]; 
			}
		}
		if (param < 0) {
			ovtmp = param - %(intminvalue)s;
			for (x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = param %(copname)s data2[x]; 
			}
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_5)s
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && (data1[x] < (%(intminvalue)s + data2[x]))) {return ARR_ERR_OVFL;}
			if ((data2[x] < 0) && (data1[x] > (%(intmaxvalue)s + data2[x]))) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] %(copname)s data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_6)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && (data1[x] < (%(intminvalue)s + data2[x]))) {return ARR_ERR_OVFL;}
			if ((data2[x] < 0) && (data1[x] > (%(intmaxvalue)s + data2[x]))) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] %(copname)s data2[x];
		}
	}
	return ARR_NO_ERR;

}
"""

# ==============================================================================
# ==============================================================================

# For signed integer.
ops_mul_int = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp1, ovtmp2;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_1)s
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * param; 
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = 0;
			}
		} else {
			// Signed integers do not have a symetrical range (e.g. -128 to 127). 
			if (param == -1) {
				for (x = 0; x < arraylen; x++) {
					if (data1[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
					data1[x] = data1[x] * param; 
				}
			} else {
				ovtmp1 = %(intmaxvalue)s / param;
				ovtmp2 = %(intminvalue)s / param;
				if (param > 0) {
					for (x = 0; x < arraylen; x++) {
						if ((data1[x] > ovtmp1) || (data1[x] < ovtmp2)) {return ARR_ERR_OVFL;}
						data1[x] = data1[x] * param; 
					}
				}
				if (param < 0) {
					for (x = 0; x < arraylen; x++) {
						if ((data1[x] < ovtmp1) || (data1[x] > ovtmp2)) {return ARR_ERR_OVFL;}
						data1[x] = data1[x] * param; 
					}
				}
			}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp1, ovtmp2;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_2)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] * param; 
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			for (x = 0; x < arraylen; x++) {
				data3[x] = 0;
			}
		} else {
			// Signed integers do not have a symetrical range (e.g. -128 to 127). 
			if (param == -1) {
				for (x = 0; x < arraylen; x++) {
					if (data1[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
					data3[x] = data1[x] * param; 
				}
			} else {
				ovtmp1 = %(intmaxvalue)s / param;
				ovtmp2 = %(intminvalue)s / param;
				if (param > 0) {
					for (x = 0; x < arraylen; x++) {
						if ((data1[x] > ovtmp1) || (data1[x] < ovtmp2)) {return ARR_ERR_OVFL;}
						data3[x] = data1[x] * param; 
					}
				}
				if (param < 0) {
					for (x = 0; x < arraylen; x++) {
						if ((data1[x] < ovtmp1) || (data1[x] > ovtmp2)) {return ARR_ERR_OVFL;}
						data3[x] = data1[x] * param; 
					}
				}
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp1, ovtmp2;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_3)s
		for (x = 0; x < arraylen; x++) {
			data2[x] = data2[x] * param; 
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			for (x = 0; x < arraylen; x++) {
				data2[x] = 0;
			}
		} else {
			// Signed integers do not have a symetrical range (e.g. -128 to 127). 
			if (param == -1) {
				for (x = 0; x < arraylen; x++) {
					if (data2[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
					data2[x] = data2[x] * param; 
				}
			} else {
				ovtmp1 = %(intmaxvalue)s / param;
				ovtmp2 = %(intminvalue)s / param;
				if (param > 0) {
					for (x = 0; x < arraylen; x++) {
						if ((data2[x] > ovtmp1) || (data2[x] < ovtmp2)) {return ARR_ERR_OVFL;}
						data2[x] = data2[x] * param; 
					}
				}
				if (param < 0) {
					for (x = 0; x < arraylen; x++) {
						if ((data2[x] < ovtmp1) || (data2[x] > ovtmp2)) {return ARR_ERR_OVFL;}
						data2[x] = data2[x] * param; 
					}
				}
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp1, ovtmp2;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_4)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = data2[x] * param; 
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			for (x = 0; x < arraylen; x++) {
				data3[x] = 0;
			}
		} else {
			// Signed integers do not have a symetrical range (e.g. -128 to 127). 
			if (param == -1) {
				for (x = 0; x < arraylen; x++) {
					if (data2[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
					data3[x] = data2[x] * param; 
				}
			} else {
				ovtmp1 = %(intmaxvalue)s / param;
				ovtmp2 = %(intminvalue)s / param;
				if (param > 0) {
					for (x = 0; x < arraylen; x++) {
						if ((data2[x] > ovtmp1) || (data2[x] < ovtmp2)) {return ARR_ERR_OVFL;}
						data3[x] = data2[x] * param; 
					}
				}
				if (param < 0) {
					for (x = 0; x < arraylen; x++) {
						if ((data2[x] < ovtmp1) || (data2[x] > ovtmp2)) {return ARR_ERR_OVFL;}
						data3[x] = data2[x] * param; 
					}
				}
			}
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_5)s
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && ((data1[x] > (%(intmaxvalue)s / data2[x])) || (data1[x] < (%(intminvalue)s / data2[x])))) {return ARR_ERR_OVFL;}
			if ((data2[x] < -1) && ((data1[x] < (%(intmaxvalue)s / data2[x])) || (data1[x] > (%(intminvalue)s / data2[x])))) {return ARR_ERR_OVFL;}
			if ((data2[x] == -1) && (data1[x] == %(intminvalue)s)) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] * data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_6)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] * data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && ((data1[x] > (%(intmaxvalue)s / data2[x])) || (data1[x] < (%(intminvalue)s / data2[x])))) {return ARR_ERR_OVFL;}
			if ((data2[x] < -1) && ((data1[x] < (%(intmaxvalue)s / data2[x])) || (data1[x] > (%(intminvalue)s / data2[x])))) {return ARR_ERR_OVFL;}
			if ((data2[x] == -1) && (data1[x] == %(intminvalue)s)) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] * data2[x];
		}
	}
	return ARR_NO_ERR;

}
"""

# ==============================================================================

# ==============================================================================

# For unsigned integer.
ops_mul_uint = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_1)s
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * param; 
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = 0; 
			}
		} else {
			ovtmp = %(intmaxvalue)s / param;
			for (x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] * param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_2)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] * param; 
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for (x = 0; x < arraylen; x++) {
				data3[x] = 0; 
			}
		} else {
			ovtmp = %(intmaxvalue)s / param;
			for (x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] * param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_3)s
		for (x = 0; x < arraylen; x++) {
			data2[x] = data2[x] * param; 
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for (x = 0; x < arraylen; x++) {
				data2[x] = 0; 
			}
		} else {
			ovtmp = %(intmaxvalue)s / param;
			for (x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = data2[x] * param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_4)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = data2[x] * param; 
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for (x = 0; x < arraylen; x++) {
				data3[x] = 0; 
			}
		} else {
			ovtmp = %(intmaxvalue)s / param;
			for (x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data2[x] * param; 
			}
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_5)s
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			if ((data2[x] != 0) && (data1[x] > (%(intmaxvalue)s / data2[x]))) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] * data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
%(simd_call_6)s
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] * data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			if ((data2[x] != 0) && (data1[x] > (%(intmaxvalue)s / data2[x]))) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] * data2[x];
		}
	}
	return ARR_NO_ERR;

}
"""


# ==============================================================================


# ==============================================================================

# For signed integer.
ops_truediv_int = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	if (param == 0) {return ARR_ERR_ZERODIV;}

	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == -1) {
		for (x = 0; x < arraylen; x++) {
			if (data1[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] / param; 
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] / param; 
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	if (param == 0) {return ARR_ERR_ZERODIV;}

	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == -1) {
		for (x = 0; x < arraylen; x++) {
			if (data1[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] / param; 
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] / param; 
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == %(intminvalue)s) {
		for (x = 0; x < arraylen; x++) {
			// Math error check.
			if (data2[x] == 0)  {return ARR_ERR_ZERODIV;}
			if (data2[x] == -1) {return ARR_ERR_OVFL;}
			data2[x] = param / data2[x];
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			// Math error check.
			if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
			data2[x] = param / data2[x];
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == %(intminvalue)s) {
		for (x = 0; x < arraylen; x++) {
			// Math error check.
			if (data2[x] == 0)  {return ARR_ERR_ZERODIV;}
			if (data2[x] == -1) {return ARR_ERR_OVFL;}
			data3[x] = param / data2[x];
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			// Math error check.
			if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
			data3[x] = param / data2[x];
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Division of min-int by -1 produces a similar error as division by 0.
	for (x = 0; x < arraylen; x++) {
		// Math error check.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		if ((data2[x] == -1) && (data1[x] == %(intminvalue)s)) {return ARR_ERR_OVFL;}
		data1[x] = data1[x] / data2[x];
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Division of min-int by -1 produces a similar error as division by 0.
	for (x = 0; x < arraylen; x++) {
		// Math error check.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		if ((data2[x] == -1) && (data1[x] == %(intminvalue)s)) {return ARR_ERR_OVFL;}
		data3[x] = data1[x] / data2[x];
	}
	return ARR_NO_ERR;

}
"""

# ==============================================================================

# For unsigned integer.
ops_truediv_uint = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	if (param == 0) {return ARR_ERR_ZERODIV;}		// Math error check.

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] / param;
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	if (param == 0) {return ARR_ERR_ZERODIV;}		// Math error check.

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] / param;
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data2[x] = param / data2[x];
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data3[x] = param / data2[x];
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data1[x] = data1[x] / data2[x];
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data3[x] = data1[x] / data2[x];
	}
	return ARR_NO_ERR;

}
"""


# ==============================================================================

# For floating point.
ops_truediv_float = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s param;
			if (!isfinite(data1[x])) {
				if (param == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s param;
			if (!isfinite(data3[x])) {
				if (param == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s datatmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			data2[x] = param %(copname)s data2[x];
			if (!isfinite(data2[x])) {
				if (datatmp == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = param %(copname)s data2[x];
			if (!isfinite(data3[x])) {
				if (data2[x] == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s data2[x];
			if (!isfinite(data1[x])) {
				if (data2[x] == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s data2[x];
			if (!isfinite(data3[x])) {
				if (data2[x] == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}
"""

# ==============================================================================

# ==============================================================================

# For signed integer.
ops_floordiv_int = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Math error check.
	if (param == 0) {return ARR_ERR_ZERODIV;}

	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == -1) {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			// Math error check.
			if (datatmp == %(intminvalue)s) {return ARR_ERR_OVFL;}
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data1[x] = dataouttmp - 1; 
			} else {
				data1[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data1[x] = dataouttmp - 1; 
			} else {
				data1[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Math error check.
	if (param == 0) {return ARR_ERR_ZERODIV;}

	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == -1) {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			// Math error check.
			if (datatmp == %(intminvalue)s) {return ARR_ERR_OVFL;}
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == %(intminvalue)s) {
		for (x = 0; x < arraylen; x++) {
			// Math error check.
			datatmp = data2[x];
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			if (datatmp == -1) {return ARR_ERR_OVFL;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data2[x] = dataouttmp - 1; 
			} else {
				data2[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			// Math error check.
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data2[x] = dataouttmp - 1; 
			} else {
				data2[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == %(intminvalue)s) {
		for (x = 0; x < arraylen; x++) {
			// Math error check.
			datatmp = data2[x];
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			if (datatmp == -1) {return ARR_ERR_OVFL;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			// Math error check.
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s datatmp, data2tmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	for (x = 0; x < arraylen; x++) {
		datatmp = data1[x];
		data2tmp = data2[x];
		// Math error check.
		if (data2tmp == 0) {return ARR_ERR_ZERODIV;}
		// Math error check.
		if ((data2tmp == -1) && (datatmp == %(intminvalue)s)) {return ARR_ERR_OVFL;}
		dataouttmp = datatmp / data2tmp;
		// This check is required for floor division.
		if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
			data1[x] = dataouttmp - 1; 
		} else {
			data1[x] = dataouttmp;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s datatmp, data2tmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	for (x = 0; x < arraylen; x++) {
		datatmp = data1[x];
		data2tmp = data2[x];
		// Math error check.
		if (data2tmp == 0) {return ARR_ERR_ZERODIV;}
		// Math error check.
		if ((data2tmp == -1) && (datatmp == %(intminvalue)s)) {return ARR_ERR_OVFL;}
		dataouttmp = datatmp / data2tmp;
		// This check is required for floor division.
		if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
			data3[x] = dataouttmp - 1; 
		} else {
			data3[x] = dataouttmp;
		}
	}
	return ARR_NO_ERR;

}
"""


# ==============================================================================

# ==============================================================================

# For unsigned integer.
ops_floordiv_uint = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	if (param == 0) {return ARR_ERR_ZERODIV;}		// Math error check.

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] / param;
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	if (param == 0) {return ARR_ERR_ZERODIV;}		// Math error check.

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] / param;
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data2[x] = param / data2[x];
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data3[x] = param / data2[x];
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data1[x] = data1[x] / data2[x];
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data3[x] = data1[x] / data2[x];
	}
	return ARR_NO_ERR;

}
"""


# ==============================================================================

# ==============================================================================

# For floating point floor division.
ops_floordiv_float = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {

		for (x = 0; x < arraylen; x++) {
			data1[x] = %(copname)s(data1[x] / param);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = %(copname)s(data1[x] / param);
			if (!isfinite(data1[x])) {
				if (param == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {

		for (x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(data1[x] / param);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(data1[x] / param);
			if (!isfinite(data3[x])) {
				if (param == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s datatmp;

	// Math error checking disabled.
	if (ignoreerrors) {

		for (x = 0; x < arraylen; x++) {
			data2[x] = %(copname)s(param / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			data2[x] = %(copname)s(param / data2[x]);
			if (!isfinite(data2[x])) {
				if (datatmp == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {

		for (x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(param / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(param / data2[x]);
			if (!isfinite(data3[x])) {
				if (data2[x] == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {

		for (x = 0; x < arraylen; x++) {
			data1[x] = %(copname)s(data1[x] / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = %(copname)s(data1[x] / data2[x]);
			if (!isfinite(data1[x])) {
				if (data2[x] == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {

		for (x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(data1[x] / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(data1[x] / data2[x]);
			if (!isfinite(data3[x])) {
				if (data2[x] == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}
"""


# ==============================================================================


# ==============================================================================

# For signed integer.
ops_mod_int = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Math error check.
	if (param == 0) {return ARR_ERR_ZERODIV;}

	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == -1) {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			if (datatmp == %(intminvalue)s) {return ARR_ERR_OVFL;}		// Math error check.
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			data1[x] = datatmp - param * dataouttmp;
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			data1[x] = datatmp - param * dataouttmp;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Math error check.
	if (param == 0) {return ARR_ERR_ZERODIV;}

	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == -1) {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			if (datatmp == %(intminvalue)s) {return ARR_ERR_OVFL;}		// Math error check.
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			data3[x] = datatmp - param * dataouttmp;
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			data3[x] = datatmp - param * dataouttmp;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == %(intminvalue)s) {
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			// Math error check.
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			if (datatmp == -1) {return ARR_ERR_OVFL;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				dataouttmp = dataouttmp - 1;
			}
			data2[x] = param - datatmp * dataouttmp;
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			// Math error check.
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				dataouttmp = dataouttmp - 1;
			}
			data2[x] = param - datatmp * dataouttmp;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == %(intminvalue)s) {
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			// Math error check.
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			if (datatmp == -1) {return ARR_ERR_OVFL;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				dataouttmp = dataouttmp - 1;
			}
			data3[x] = param - datatmp * dataouttmp;
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			// Math error check.
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				dataouttmp = dataouttmp - 1;
			}
			data3[x] = param - datatmp * dataouttmp;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s datatmp, data2tmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	for (x = 0; x < arraylen; x++) {
		datatmp = data1[x];
		data2tmp = data2[x];
		// Math error check.
		if (data2tmp == 0) {return ARR_ERR_ZERODIV;}
		if ((data2tmp == -1) && (datatmp == %(intminvalue)s)) {return ARR_ERR_OVFL;}
		dataouttmp = datatmp / data2tmp;
		// This check is required for floor division.
		if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
			dataouttmp = dataouttmp - 1;
		}
		data1[x] = datatmp - data2tmp * dataouttmp;
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s datatmp, data2tmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	for (x = 0; x < arraylen; x++) {
		datatmp = data1[x];
		data2tmp = data2[x];
		// Math error check.
		if (data2tmp == 0) {return ARR_ERR_ZERODIV;}
		if ((data2tmp == -1) && (datatmp == %(intminvalue)s)) {return ARR_ERR_OVFL;}
		dataouttmp = datatmp / data2tmp;
		// This check is required for floor division.
		if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
			dataouttmp = dataouttmp - 1;
		}
		data3[x] = datatmp - data2tmp * dataouttmp;
	}
	return ARR_NO_ERR;

}
"""

# ==============================================================================

# ==============================================================================

# For unsigned integer.
ops_mod_uint = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	if (param == 0) {return ARR_ERR_ZERODIV;}		// Math error check.
	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] %% param;
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	// Math error check.
	if (param == 0) {return ARR_ERR_ZERODIV;}
	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] %% param;
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	for (x = 0; x < arraylen; x++) {
		// Math error check.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data2[x] = param %% data2[x];
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	for (x = 0; x < arraylen; x++) {
		// Math error check.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data3[x] = param %% data2[x];
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data1[x] = data1[x] %% data2[x];
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data3[x] = data1[x] %% data2[x];
	}
	return ARR_NO_ERR;

}
"""


# ==============================================================================


# ==============================================================================

# For floating point.
ops_mod_float = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] - param * %(modfloor)s(data1[x] / param);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] - param * %(modfloor)s(data1[x] / param);
			if (!isfinite(data1[x])) {
				if (param == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] - param * %(modfloor)s(data1[x] / param);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] - param * %(modfloor)s(data1[x] / param);
			if (!isfinite(data3[x])) {
				if (param == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s datatmp;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = param - data2[x] * %(modfloor)s(param / data2[x]);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			data2[x] = param - data2[x] * %(modfloor)s(param / data2[x]);
			if (!isfinite(data2[x])) {
				if (datatmp == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = param - data2[x] * %(modfloor)s(param / data2[x]);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data3[x] = param - data2[x] * %(modfloor)s(param / data2[x]);
			if (!isfinite(data3[x])) {
				if (data2[x] == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] - data2[x] * %(modfloor)s(data1[x] / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = data1[x] - data2[x] * %(modfloor)s(data1[x] / data2[x]);
			if (!isfinite(data1[x])) {
				if (data2[x] == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] - data2[x] * %(modfloor)s(data1[x] / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x] - data2[x] * %(modfloor)s(data1[x] / data2[x]);
			if (!isfinite(data3[x])) {
				if (data2[x] == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}
"""

# ==============================================================================

# ==============================================================================

# For signed and unsigned integer.
ops_pow_int = """

%(powtemplate)s

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_%(funcmodifier)s(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_%(funcmodifier)s(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_%(funcmodifier)s(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_%(funcmodifier)s(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_%(funcmodifier)s(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_%(funcmodifier)s(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_%(funcmodifier)s(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_%(funcmodifier)s(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_%(funcmodifier)s(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_%(funcmodifier)s(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_%(funcmodifier)s(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_%(funcmodifier)s(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}
"""

# ==============================================================================


# ==============================================================================

# For floating point.
ops_pow_float = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = %(copname)s(data1[x], param);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data1[x] = %(copname)s(data1[x], param);
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(data1[x], param);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(data1[x], param);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = %(copname)s(param, data2[x]);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data2[x] = %(copname)s(param, data2[x]);
			if (!isfinite(data2[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(param, data2[x]);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(param, data2[x]);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = %(copname)s(data1[x], data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = %(copname)s(data1[x], data2[x]);
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(data1[x], data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(data1[x], data2[x]);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}
"""

# ==============================================================================


# The operations using SIMD. This handles multiple different SIMD operations.
ops_simdsupport = """
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
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, resultslice;
	%(arraytype)s opvals[%(simdwidth)s];


	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		opvals[y] = param;
	}
	datasliceright = %(vldinstr)s opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr1)s &data1[x], %(vstinstr2)s resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] %(copname)s param;
	}

}



// param_arr_num_arr
void %(funclabel)s_%(funcmodifier)s_2_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, resultslice;
	%(arraytype)s opvals[%(simdwidth)s];


	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		opvals[y] = param;
	}
	datasliceright = %(vldinstr)s opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data1[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr1)s &data3[x], %(vstinstr2)s resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] %(copname)s param;
	}

}



// param_num_arr_none
void %(funclabel)s_%(funcmodifier)s_3_simd(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, resultslice;
	%(arraytype)s opvals[%(simdwidth)s];


	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		opvals[y] = param;
	}
	datasliceleft = %(vldinstr)s opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceright = %(vldinstr)s &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr1)s &data2[x], %(vstinstr2)s resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data2[x] = param %(copname)s data2[x];
	}

}



// param_num_arr_arr
void %(funclabel)s_%(funcmodifier)s_4_simd(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t x; 
	unsigned int y;

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, resultslice;
	%(arraytype)s opvals[%(simdwidth)s];


	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		opvals[y] = param;
	}
	datasliceleft = %(vldinstr)s opvals);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceright = %(vldinstr)s &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr1)s &data3[x], %(vstinstr2)s resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = param %(copname)s data2[x];
	}

}



// param_arr_arr_none
void %(funclabel)s_%(funcmodifier)s_5_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data1[x]);
		datasliceright = %(vldinstr)s &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr1)s &data1[x], %(vstinstr2)s resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data1[x] = data1[x] %(copname)s data2[x];
	}

}



// param_arr_arr_arr
void %(funclabel)s_%(funcmodifier)s_6_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data1[x]);
		datasliceright = %(vldinstr)s &data2[x]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		resultslice = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr1)s &data3[x], %(vstinstr2)s resultslice);
	}

	// Get the max value within the left over elements at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		data3[x] = data1[x] %(copname)s data2[x];
	}

}
#endif

/*--------------------------------------------------------------------------- */
"""

# ==============================================================================

# This is the set of function calls used to call each operator function.
opscall = """
		// %(funcmodifier)s
		case '%(arraycode)s' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = %(funclabel)s_%(funcmodifier)s_1(arraydata.arraylength,%(nosimdparam)s arraydata.array1.%(arraycode)s, arraydata.param.%(arraycode)s, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = %(funclabel)s_%(funcmodifier)s_2(arraydata.arraylength,%(nosimdparam)s arraydata.array1.%(arraycode)s, arraydata.param.%(arraycode)s, arraydata.array3.%(arraycode)s, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = %(funclabel)s_%(funcmodifier)s_3(arraydata.arraylength,%(nosimdparam)s arraydata.param.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = %(funclabel)s_%(funcmodifier)s_4(arraydata.arraylength,%(nosimdparam)s arraydata.param.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.array3.%(arraycode)s, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = %(funclabel)s_%(funcmodifier)s_5(arraydata.arraylength,%(nosimdparam)s arraydata.array1.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = %(funclabel)s_%(funcmodifier)s_6(arraydata.arraylength,%(nosimdparam)s arraydata.array1.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.array3.%(arraycode)s, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}
"""


# ==============================================================================


mathops_params = """
/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;

	// This is used to hold the parsed parameters.
	struct args_params_2 arraydata = ARGSINIT_TWO;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_two(self, args, keywds, 1, %(getsimdparam)s, "%(funclabel)s");

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


	// Signal the errors.
	if (resultcode == ARR_ERR_ZERODIV) {
		ErrMsgZeroDiv();
		return NULL;
	}

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
Equivalent to:          [x %(pyoperator)s param for x in array1] \\n\\
or                      [param %(pyoperator)s y for y in array2] \\n\\
or                      [x %(pyoperator)s y for x, y in zip(array1, array2)] \\n\\
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
  %(funclabel)s(array1, param, matherrors=False) \\n\\
%(helpsimd1)s\\n\\
\\n\\
* array1 - The first input data array to be examined. If no output  \\n\\
  array is provided the results will overwrite the input data.  \\n\\
* param - A non-array numeric parameter.  \\n\\
* array2 - A second input data array. Each element in this array is  \\n\\
  applied to the corresponding element in the first array.  \\n\\
* outparray - The output array. This parameter is optional.  \\n\\
* maxlen - Limit the length of the array used. This must be a valid  \\n\\
  positive integer. If a zero or negative length, or a value which is  \\n\\
  greater than the actual length of the array is specified, this  \\n\\
  parameter is ignored.  \\n\\
* matherrors - If true, arithmetic error checking is disabled. The  \\n\\
  default is false. \\n\\
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

# These are used for the pow function only.

powtemplatesigned = """
/*--------------------------------------------------------------------------- */

// Note: The guard calculations for negative need to use abs(x) instead of -x
// because of problems with Microsoft MSVS 2010. MSVS was confused by negating
// a negative number with minimum integers (e.g. INT_MIN) and producing a
// positive result.

// Return x raised to the power of y.
%(arraytype)s arith_pow_%(funcmodifier)s(%(arraytype)s x, %(arraytype)s y, char *errflag) {
	%(arraytype)s i, z, ovtmp1, ovtmp2;
	z = 1;
	*errflag = 0;

	// We don't allow negative powers for integers.
	if (y < 0) {
		*errflag = ARR_ERR_VALUE_ERR;
		return z;
	}

	// Special case for raise to the power of zero.
	if (y == 0) { return 1; }

	// We need this special case to avoid dividing by zero.
	if (x == 0) {return 0;}

	if (x > 0) {
		ovtmp1 = %(intmaxvalue)s / x;
		for (i = 0; i < y; i++) {
			if (z > ovtmp1) {*errflag = ARR_ERR_OVFL; return z;}
			z = z * x;
		}
	} else {
		ovtmp1 = %(intmaxvalue)s / %(abs)s(x);
		ovtmp2 = %(intminvalue)s / %(abs)s(x);
		for (i = 0; i < y; i++) {
			if ((z > ovtmp1) || (z < ovtmp2)) {*errflag = ARR_ERR_OVFL; return z;}
			z = z * x;
		}
	}
	return z;
}

"""


powtemplateunsigned = """
// Return x raised to the power of y.
%(arraytype)s arith_pow_%(funcmodifier)s(%(arraytype)s x, %(arraytype)s y, char *errflag) {
	%(arraytype)s i, z, ovtmp1;
	z = 1;
	*errflag = 0;

	// Special case for raise to the power of zero.
	if (y == 0) { return 1; }

	// We need this special case to avoid dividing by zero.
	if (x == 0) {return 0;}

	ovtmp1 = %(intmaxvalue)s / x;
	for (i = 0; i < y; i++) {
		if (z > ovtmp1) {*errflag = ARR_ERR_OVFL; return z;}
		z = z * x;
	}
	return z;
}

/*--------------------------------------------------------------------------- */
"""


# ==============================================================================

# These are the C functions used to calculate absolute value (abs).
absfunc = {
	'b' : 'abs',
	'B' : '',
	'h' : 'abs',
	'H' : '',
	'i' : 'abs',
	'I' : '',
	'l' : 'labs',
	'L' : '',
	'q' : 'llabs',
	'Q' : '',
	'f' : '',
	'd' : ''
}



# ==============================================================================

# This is required for SIMD operations only.
includeoptions_both = '''#include "simddefs.h"

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
'''


# This is required for SIMD operations only.
includeoptions_arm = '''#include "simddefs.h"

#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
#include "arm_neon.h"
#endif

#if defined(AF_HASSIMD_ARMv7_32BIT)
#include "%(funclabel)s_simd_armv7.h"
#endif

#if defined(AF_HASSIMD_ARM_AARCH64)
#include "%(funclabel)s_simd_armv8.h"
#endif
'''


# SIMD call template. This has to handle multiple template strings,
# and so is presented as a dictionary to allow it to be handled
# iteratively. 

SIMD_call = {
'simd_call_1' : '''\n%(simdplatform)s
		// SIMD version.
		if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
			%(funclabel)s_%(funcmodifier)s_1_simd(arraylen, data1, param);
			return ARR_NO_ERR;
		}
#endif\n''',

'simd_call_2' : '''\n%(simdplatform)s
		// SIMD version.
		if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
			%(funclabel)s_%(funcmodifier)s_2_simd(arraylen, data1, param, data3);
			return ARR_NO_ERR;
		}
#endif\n''',

'simd_call_3' : '''\n%(simdplatform)s
		// SIMD version.
		if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
			%(funclabel)s_%(funcmodifier)s_3_simd(arraylen, param, data2);
			return ARR_NO_ERR;
		}
#endif\n''',

'simd_call_4' : '''\n%(simdplatform)s
		// SIMD version.
		if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
			%(funclabel)s_%(funcmodifier)s_4_simd(arraylen, param, data2, data3);
			return ARR_NO_ERR;
		}
#endif\n''',

'simd_call_5' : '''\n%(simdplatform)s
		// SIMD version.
		if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
			%(funclabel)s_%(funcmodifier)s_5_simd(arraylen, data1, data2);
			return ARR_NO_ERR;
		}
#endif\n''',

'simd_call_6' : '''\n%(simdplatform)s
		// SIMD version.
		if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
			%(funclabel)s_%(funcmodifier)s_6_simd(arraylen, data1, data2, data3);
			return ARR_NO_ERR;
		}
#endif\n'''
}


# This is used to insert the "nosimd" parameter in parameter declarations. 
nosimddecl = ' int nosimd,'

# This one is used in the actual function call. 
nosimdparam = ' arraydata.nosimd,'


# The following are used to fill in template data which handles whether
# a function requires SIMD related template data or not. 
helpsimd1_template = '  %(funclabel)s(array, param, nosimd=False)'

helpsimd2_template = '''* nosimd - If True, SIMD acceleration is disabled. This parameter is \\n\\
  optional. The default is FALSE. \\n\\n'''

# ==============================================================================

# Which opstemplate is valid for which operation. Each math operation requires
# different templates for signed int, unsigned int, and float.
opstemplates = {
	'+' : {'int' : ops_add_int,
			'uint' : ops_add_uint,
			'float' : ops_op_float
		},
	'-' : {'int' : ops_sub_int,
			'uint' : ops_sub_uint,
			'float' : ops_op_float
		},
	'*' : {'int' : ops_mul_int,
			'uint' : ops_mul_uint,
			'float' : ops_op_float
		},
	'/' : {'int' : ops_truediv_int,
			'uint' : ops_truediv_uint,
			'float' : ops_truediv_float
		},
	'//' : {'int' : ops_floordiv_int,
			'uint' : ops_floordiv_uint,
			'float' : ops_floordiv_float
		},
	'%' : {'int' : ops_mod_int,
			'uint' : ops_mod_uint,
			'float' : ops_mod_float
		},

	'**' : {'int' : ops_pow_int,
			'uint' : ops_pow_int,
			'float' : ops_pow_float
		},

}

# ==============================================================================

# ==============================================================================


# Various SIMD instruction information which varies according to array type.
# For x86-64.

simdattr_x86 = {
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
	'B' : '(v16qi) __builtin_ia32_lddqu((char *) ', 
	'h' : '(v8hi) __builtin_ia32_lddqu((char *) ', 
	'H' : '(v8hi) __builtin_ia32_lddqu((char *) ', 
	'i' : '(v4si) __builtin_ia32_lddqu((char *) ', 
	'I' : '(v4si) __builtin_ia32_lddqu((char *) ', 
	'f' : '(v4sf) __builtin_ia32_loadups(',
	'd' : '(v2df) __builtin_ia32_loadupd(',
}


vstinstr1_x86 = {
	'b' : '__builtin_ia32_storedqu((char *)', 
	'B' : '__builtin_ia32_storedqu((char *)',
	'h' : '__builtin_ia32_storedqu((char *)',
	'H' : '__builtin_ia32_storedqu((char *)',
	'i' : '__builtin_ia32_storedqu((char *)',
	'I' : '__builtin_ia32_storedqu((char *)',
	'f' : '__builtin_ia32_storeups(',
	'd' : '__builtin_ia32_storeupd(',
}


vstinstr2_x86 = {
	'b' : '', 
	'B' : '', 
	'h' : '(v16qi) ', 
	'H' : '(v16qi) ', 
	'i' : '(v16qi) ', 
	'I' : '(v16qi) ', 
	'f' : '(v4sf)',
	'd' : '(v2df)',
}


# SIMD operations.
simdop_x86 = {
	'b' : {'add' : '(v16qi) __builtin_ia32_paddb128', 
			'sub' : '(v16qi) __builtin_ia32_psubb128'},
	'h' : {'add' : '(v8hi) __builtin_ia32_paddw128', 
			'sub' : '(v8hi) __builtin_ia32_psubw128'},
	'i' : {'add' : '(v4si) __builtin_ia32_paddd128', 
			'sub' : '(v4si) __builtin_ia32_psubd128'},
	'f' : {'add' : '__builtin_ia32_addps', 
			'sub' : '__builtin_ia32_subps'},
	'd' : {'add' : '__builtin_ia32_addpd', 
			'sub' : '__builtin_ia32_subpd'},
}


# Which functions support x86 SIMD.
x86_simdfuncnames = set(itertools.chain.from_iterable([x.keys() for x in simdop_x86.values()]))


# A list of which array types are supported by x86 SIMD instructions.
def x86_simdtypes(funcname):
	return [x for x in simdop_x86.keys() if funcname in simdop_x86[x]]



# ==============================================================================

# For ARM NEON ARMv7 32 bit.
# Not all possible array types have been implemented as benchmarking
# has shown that SIMD is actually slower for array types with larger
# word sizes.

simdattr_armv7 = {
	'b' : 'int8x8_t',
	'B' : 'uint8x8_t',
	'h' : 'int16x4_t',
	'H' : 'uint16x4_t',
}


vldinstr_armv7 = {
	'b' : 'vld1_s8(',
	'B' : 'vld1_u8(',
	'h' : 'vld1_s16(',
	'H' : 'vld1_u16(',
}

vstinstr1_armv7 = {
	'b' : 'vst1_s8(',
	'B' : 'vst1_u8(',
	'h' : 'vst1_s16(',
	'H' : 'vst1_u16(',
}

vstinstr2_armv7 = {
	'b' : '',
	'B' : '',
	'h' : '',
	'H' : '',
}

vstinstr2_armv7 = {
	'b' : '',
	'B' : '',
	'h' : '',
	'H' : '',
}


# SIMD operations.
simdop_armv7 = {
	'b' : {'add' : 'vadd_s8', 
			'mul' : 'vmul_s8',
			'sub' : 'vsub_s8'},
	'B' : {'add' : 'vadd_u8', 
			'mul' : 'vmul_u8',
			'sub' : 'vsub_u8'},
	'h' : {'add' : 'vadd_s16', 
			'mul' : 'vmul_s16',
			'sub' : 'vsub_s16'},
	'H' : {'add' : 'vadd_u16', 
			'mul' : 'vmul_u16',
			'sub' : 'vsub_u16'},
}

# Which functions support ARM SIMD.
armv7_simdfuncnames = set(itertools.chain.from_iterable([x.keys() for x in simdop_armv7.values()]))

# A list of which array types are supported by ARM SIMD instructions.
def armv7_simdtypes(funcname):
	return [x for x in simdop_armv7.keys() if funcname in simdop_armv7[x]]

# ==============================================================================


# For ARM NEON ARMv8 64 bit.
# Not all possible array types have been implemented as benchmarking
# has shown that SIMD is actually slower for array types with larger
# word sizes.

simdattr_armv8 = {
	'b' : 'int8x16_t',
	'B' : 'uint8x16_t',
	'h' : 'int16x8_t',
	'H' : 'uint16x8_t',
	'i' : 'int32x4_t',
	'I' : 'uint32x4_t',
	'f' : 'float32x4_t',
}


vldinstr_armv8 = {
	'b' : 'vld1q_s8(',
	'B' : 'vld1q_u8(',
	'h' : 'vld1q_s16(',
	'H' : 'vld1q_u16(',
	'i' : 'vld1q_s32(',
	'I' : 'vld1q_u32(',
	'f' : 'vld1q_f32(',
}

vstinstr1_armv8 = {
	'b' : 'vst1q_s8(',
	'B' : 'vst1q_u8(',
	'h' : 'vst1q_s16(',
	'H' : 'vst1q_u16(',
	'i' : 'vst1q_s32(',
	'I' : 'vst1q_u32(',
	'f' : 'vst1q_f32(',
}

vstinstr2_armv8 = {
	'b' : '',
	'B' : '',
	'h' : '',
	'H' : '',
	'i' : '',
	'I' : '',
	'f' : '',
}

vstinstr2_armv8 = {
	'b' : '',
	'B' : '',
	'h' : '',
	'H' : '',
	'i' : '',
	'I' : '',
	'f' : '',
}


# SIMD operations.
simdop_armv8 = {
	'b' : {'add' : 'vaddq_s8', 
			'mul' : 'vmulq_s8',
			'sub' : 'vsubq_s8'},
	'B' : {'add' : 'vaddq_u8', 
			'mul' : 'vmulq_u8',
			'sub' : 'vsubq_u8'},
	'h' : {'add' : 'vaddq_s16', 
			'mul' : 'vmulq_s16',
			'sub' : 'vsubq_s16'},
	'H' : {'add' : 'vaddq_u16', 
			'mul' : 'vmulq_u16',
			'sub' : 'vsubq_u16'},
	'i' : {'add' : 'vaddq_s32', 
			'mul' : 'vmulq_s32',
			'sub' : 'vsubq_s32'},
	'I' : {'add' : 'vaddq_u32', 
			'mul' : 'vmulq_u32',
			'sub' : 'vsubq_u32'},
	'f' : {'add' : 'vaddq_f32', 
			'mul' : 'vmulq_f32',
			'sub' : 'vsubq_f32'},
}

# Which functions support ARM SIMD.
armv8_simdfuncnames = set(itertools.chain.from_iterable([x.keys() for x in simdop_armv8.values()]))

# A list of which array types are supported by ARM SIMD instructions.
def armv8_simdtypes(funcname):
	return [x for x in simdop_armv8.keys() if funcname in simdop_armv8[x]]

# ==============================================================================


# Width of array elements.
simdwidth = {'b' : 'CHARSIMDSIZE',
		'B' : 'CHARSIMDSIZE',
		'h' : 'SHORTSIMDSIZE',
		'H' : 'SHORTSIMDSIZE',
		'i' : 'INTSIMDSIZE',
		'I' : 'INTSIMDSIZE',
		'f' : 'FLOATSIMDSIZE',
		'd' : 'DOUBLESIMDSIZE',
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
def findsimdplatform(arraycode, funcname):

	hasx86 = arraycode in x86_simdtypes(funcname)
	hasarmv7 = arraycode in armv7_simdtypes(funcname)
	hasarmv8 = arraycode in armv8_simdtypes(funcname)

	# Only the platforms combinations which are used currently are defined here.
	if hasx86 and hasarmv7 and hasarmv8:
		return SIMD_platform_x86_ARM
	elif hasx86 and (not hasarmv7) and (not hasarmv8):
		return SIMD_platform_x86
	elif hasx86 and (not hasarmv7) and hasarmv8:
		return SIMD_platform_x86_ARMv8
	elif (not hasx86) and hasarmv7 and hasarmv8:
		return SIMD_platform_ARM
	elif (not hasx86) and (not hasarmv7) and hasarmv8:
		return SIMD_platform_ARM64v8
	else:
		print('Error: Template error in findsimdplatform: %s %s' % (arraycode, funcname))
		return 'Error: Template error, this should not be here.'

# ==============================================================================

# ==============================================================================


# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.

funclist = [x for x in oplist if x['c_code_template'] in ['template_mathop', 'template_mathop_simd']]


# ==============================================================================

for func in funclist:

	# Create the source code based on templates.
	funcname = func['funcname']
	filename = funcname + '.c'
	pyoperator = func['pyoperator']

	# Functions using SIMD.
	hassimd_x86 = funcname in x86_simdfuncnames
	hassimd_arm = funcname in armv7_simdfuncnames

	with open(filename, 'w') as f:

		funcdata = {'funclabel' : funcname, 'includeoptions' : ''}
		if hassimd_x86:
			funcdata['includeoptions'] = includeoptions_both % {'funclabel' : funcname}
		elif hassimd_arm:
			funcdata['includeoptions'] = includeoptions_arm % {'funclabel' : funcname}
			
		f.write(mathops_head % funcdata)
		opscalltext = []

			

		# Check each array type.
		for arraycode in codegen_common.arraycodes:
			arraytype = codegen_common.arraytypes[arraycode]
			funcmodifier = arraytype.replace(' ', '_')

			funcdata['funcmodifier'] = funcmodifier
			funcdata['arraytype'] = arraytype
			funcdata['intmaxvalue'] = codegen_common.maxvalue[arraycode]
			funcdata['intminvalue'] = codegen_common.minvalue[arraycode]

			# This is used for pow only.
			funcdata['abs'] = absfunc[arraycode]

			# This is used for mod only.
			if (arraycode == 'f') and (pyoperator == '%'):
				funcdata['modfloor'] = 'floorf'
			elif (arraycode == 'd') and (pyoperator == '%'):
				funcdata['modfloor'] = 'floor'
			else:
				funcdata['modfloor'] = ''


			# The way that powtemplate works requires that all the data in
			# 'funcdata' is defind before we get to powtemplate.
			if arraycode == 'f':
				funcdata['copname'] = func['c_operator_f']
				ops_calc = opstemplates[pyoperator]['float']
			elif arraycode == 'd':
				funcdata['copname'] = func['c_operator_d']
				ops_calc = opstemplates[pyoperator]['float']
			elif arraycode in codegen_common.unsignedint:
				 funcdata['copname'] = func['c_operator_i']
				 ops_calc = opstemplates[pyoperator]['uint']
				 funcdata['powtemplate'] = powtemplateunsigned % funcdata
			elif arraycode in codegen_common.signedint:
				 funcdata['copname'] = func['c_operator_i']
				 ops_calc = opstemplates[pyoperator]['int']
				 funcdata['powtemplate'] = powtemplatesigned % funcdata
			else:
				print('Error - Unsupported array code.', arraycode)


			# Prepare the SIMD templates.
			if arraycode in (set(x86_simdtypes(funcname)) | set(armv7_simdtypes(funcname)) | set(armv8_simdtypes(funcname))):
				simdfuncdata = {'simdwidth' : simdwidth[arraycode], 
					'funclabel' : funcname,
					'funcmodifier' : funcmodifier,
					'simdplatform' : findsimdplatform(arraycode, funcname)}
				funcdata.update(dict([(x, y % simdfuncdata) for x,y in SIMD_call.items()]))
				funcdata['nosimddecl'] = nosimddecl
				funcdata['nosimdparam'] = nosimdparam
			else:
				funcdata.update(dict([(x, '') for x,y in SIMD_call.items()]))
				funcdata['nosimddecl'] = ''
				funcdata['nosimdparam'] = ''


			f.write(ops_calc % funcdata)

			# This is the call to the functions for this array type. This
			# is inserted into another template below.
			funcdata['arraycode'] = arraycode
			opscalltext.append(opscall % funcdata)

		if hassimd_x86 or hassimd_arm:
			helpsimd1 = helpsimd1_template % {'funclabel' : funcname}
			helpsimd2 = helpsimd2_template
			getsimdparam = '1'
		else:
			helpsimd1 = ''
			helpsimd2 = ''
			getsimdparam = '0'


		supportedarrays = codegen_common.FormatDocsArrayTypes(func['arraytypes'])

		f.write(mathops_params % {'funclabel' : funcname, 
				'opcodedocs' : func['opcodedocs'], 
				'supportedarrays' : supportedarrays,
				'pyoperator' : pyoperator,
				'matherrors' : ', '.join(func['matherrors'].split(',')),
				'opscall' : ''.join(opscalltext),
				'getsimdparam' : getsimdparam,
				'helpsimd1' : helpsimd1,
				'helpsimd2' : helpsimd2})


# ==============================================================================


# ==============================================================================

# This outputs the SIMD version for x86-64.

# The original date of the SIMD C code.
simdcodedate = '1-Apr-2019'
simdfilename = '_simd_x86'

# Get just the functions which support SIMD.
simdlist = [x for x in oplist if x['funcname'] in x86_simdfuncnames]

for func in simdlist:

	outputlist = []

	funcname = func['funcname']

	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname


	# Output the generated code.
	for arraycode in x86_simdtypes(funcname):

		arraytype = codegen_common.arraytypes[arraycode]

		# The main template values.
		funcdata = {'funclabel' : funcname,
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'arraycode' : arraycode,
					'arraytype' : codegen_common.arraytypes[arraycode],
					'simdplatform' : SIMD_platform_x86,

					'simdwidth' : simdwidth[arraycode],
					'simdattr' : simdattr_x86[arraycode],
					'vldinstr' : vldinstr_x86[arraycode],
					'vstinstr1' : vstinstr1_x86[arraycode],
					'vstinstr2' : vstinstr2_x86[arraycode],
					'vopinstr' : simdop_x86[arraycode][funcname],
					}

		# Get the correct operator. Some operations use operators, and
		# some use C function names. 
		if arraycode == 'f':
			funcdata['copname'] = func['c_operator_f']
		elif arraycode == 'd':
			funcdata['copname'] = func['c_operator_d']
		elif arraycode in codegen_common.intarrays:
			 funcdata['copname'] = func['c_operator_i']
		else:
			print('Error - Unsupported array code.', arraycode)


		# Start of function definition.
		outputlist.append(ops_simdsupport % funcdata)




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

# This outputs the SIMD version for ARM NEON ARMv7 32 bit.

# The original date of the SIMD C code.
simdcodedate = '8-Oct-2019'
simdfilename = '_simd_armv7'

# Get just the functions which support SIMD.
simdlist = [x for x in oplist if x['funcname'] in armv7_simdfuncnames]


for func in simdlist:

	outputlist = []

	funcname = func['funcname']

	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname


	# Output the generated code.
	for arraycode in armv7_simdtypes(funcname):


		arraytype = codegen_common.arraytypes[arraycode]

		# The main template values.
		funcdata = {'funclabel' : funcname,
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'arraycode' : arraycode,
					'arraytype' : codegen_common.arraytypes[arraycode],
					'simdplatform' : SIMD_platform_ARMv7,

					'simdwidth' : simdwidth[arraycode],
					'simdattr' : simdattr_armv7[arraycode],
					'vldinstr' : vldinstr_armv7[arraycode],
					'vstinstr1' : vstinstr1_armv7[arraycode],
					'vstinstr2' : vstinstr2_armv7[arraycode],
					'vopinstr' : simdop_armv7[arraycode][funcname],
					}

		# Get the correct operator.
		if arraycode == 'f':
			funcdata['copname'] = func['c_operator_f']
		elif arraycode == 'd':
			funcdata['copname'] = func['c_operator_d']
		elif arraycode in codegen_common.intarrays:
			 funcdata['copname'] = func['c_operator_i']
		else:
			print('Error - Unsupported array code.', arraycode)


		# Start of function definition.
		outputlist.append(ops_simdsupport % funcdata)




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

# This outputs the SIMD version for ARM NEON ARMv8 64 bit.

# The original date of the SIMD C code.
simdcodedate = '26-Mar-2020'
simdfilename = '_simd_armv8'

# Get just the functions which support SIMD.
simdlist = [x for x in oplist if x['funcname'] in armv8_simdfuncnames]


for func in simdlist:

	outputlist = []

	funcname = func['funcname']

	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname


	# Output the generated code.
	for arraycode in armv8_simdtypes(funcname):


		arraytype = codegen_common.arraytypes[arraycode]

		# The main template values.
		funcdata = {'funclabel' : funcname,
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'arraycode' : arraycode,
					'arraytype' : codegen_common.arraytypes[arraycode],
					'simdplatform' : SIMD_platform_ARM64v8,

					'simdwidth' : simdwidth[arraycode],
					'simdattr' : simdattr_armv8[arraycode],
					'vldinstr' : vldinstr_armv8[arraycode],
					'vstinstr1' : vstinstr1_armv8[arraycode],
					'vstinstr2' : vstinstr2_armv8[arraycode],
					'vopinstr' : simdop_armv8[arraycode][funcname],
					}

		# Get the correct operator.
		if arraycode == 'f':
			funcdata['copname'] = func['c_operator_f']
		elif arraycode == 'd':
			funcdata['copname'] = func['c_operator_d']
		elif arraycode in codegen_common.intarrays:
			 funcdata['copname'] = func['c_operator_i']
		else:
			print('Error - Unsupported array code.', arraycode)


		# Start of function definition.
		outputlist.append(ops_simdsupport % funcdata)




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

