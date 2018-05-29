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
//   Copyright 2014 - 2018    Michael Griffin    <m12.griffin@gmail.com>
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
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s param;
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s param;
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
		for(x = 0; x < arraylen; x++) {
			data2[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data2[x] = param %(copname)s data2[x];
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = param %(copname)s data2[x];
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
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s data2[x];
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		ovtmp = %(intmaxvalue)s - param;
		for(x = 0; x < arraylen; x++) {
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] %(copname)s param;
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		ovtmp = %(intmaxvalue)s - param;
		for(x = 0; x < arraylen; x++) {
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] %(copname)s param;
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = %(intmaxvalue)s - data2[x];
			if (param > ovtmp) {return ARR_ERR_OVFL;}
			data2[x] = param %(copname)s data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = %(intmaxvalue)s - data2[x];
			if (param > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = param %(copname)s data2[x];
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = %(intmaxvalue)s - data2[x];
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] %(copname)s data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
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
			for(x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] %(copname)s param; 
			}
		}
		if (param < 0) {
			ovtmp = %(intminvalue)s - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] < ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] %(copname)s param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data3[x] = data1[x]; 
			}
		}
		if (param > 0) {
			ovtmp = %(intmaxvalue)s - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] %(copname)s param; 
			}
		}
		if (param < 0) {
			ovtmp = %(intminvalue)s - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] < ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] %(copname)s param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
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
			for(x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = data2[x] %(copname)s param; 
			}
		}
		if (param < 0) {
			ovtmp = %(intminvalue)s - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = data2[x] %(copname)s param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data3[x] = data2[x]; 
			}
		}
		if (param > 0) {
			ovtmp = %(intmaxvalue)s - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data2[x] %(copname)s param; 
			}
		}
		if (param < 0) {
			ovtmp = %(intminvalue)s - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data2[x] %(copname)s param; 
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
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && (data1[x] > (%(intmaxvalue)s - data2[x]))) {return ARR_ERR_OVFL;}
			if ((data2[x] < 0) && (data1[x] < (%(intminvalue)s - data2[x]))) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] %(copname)s data2[x];
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if (data1[x] < param) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] %(copname)s param;
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if (data1[x] < param) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] %(copname)s param;
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
		for(x = 0; x < arraylen; x++) {
			data2[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if (param < data2[x]) {return ARR_ERR_OVFL;}
			data2[x] = param %(copname)s data2[x];
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if (param < data2[x]) {return ARR_ERR_OVFL;}
			data3[x] = param %(copname)s data2[x];
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
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if (data1[x] < data2[x]) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] %(copname)s data2[x];
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
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
			for(x = 0; x < arraylen; x++) {
				if (data1[x] < ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] %(copname)s param; 
			}
		}
		if (param < 0) {
			ovtmp = %(intmaxvalue)s + param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] %(copname)s param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data3[x] = data1[x]; 
			}
		}
		if (param > 0) {
			ovtmp = %(intminvalue)s + param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] < ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] %(copname)s param; 
			}
		}
		if (param < 0) {
			ovtmp = %(intmaxvalue)s + param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] %(copname)s param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				if (data2[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
				data2[x] = -data2[x]; 
			}
		}
		if (param > 0) {
			ovtmp = param - %(intmaxvalue)s;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = param %(copname)s data2[x]; 
			}
		}
		if (param < 0) {
			ovtmp = param - %(intminvalue)s;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = param %(copname)s data2[x]; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				if (data2[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
				data3[x] = -data2[x]; 
			}
		}
		if (param > 0) {
			ovtmp = param - %(intmaxvalue)s;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = param %(copname)s data2[x]; 
			}
		}
		if (param < 0) {
			ovtmp = param - %(intminvalue)s;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = param %(copname)s data2[x]; 
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
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && (data1[x] < (%(intminvalue)s + data2[x]))) {return ARR_ERR_OVFL;}
			if ((data2[x] < 0) && (data1[x] > (%(intmaxvalue)s + data2[x]))) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] %(copname)s data2[x];
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp1, ovtmp2;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * param; 
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data1[x] = 0;
			}
		} else {
			// Signed integers do not have a symetrical range (e.g. -128 to 127). 
			if (param == -1) {
				for(x = 0; x < arraylen; x++) {
					if (data1[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
					data1[x] = data1[x] * param; 
				}
			} else {
				ovtmp1 = %(intmaxvalue)s / param;
				ovtmp2 = %(intminvalue)s / param;
				if (param > 0) {
					for(x = 0; x < arraylen; x++) {
						if ((data1[x] > ovtmp1) || (data1[x] < ovtmp2)) {return ARR_ERR_OVFL;}
						data1[x] = data1[x] * param; 
					}
				}
				if (param < 0) {
					for(x = 0; x < arraylen; x++) {
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
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp1, ovtmp2;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] * param; 
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data3[x] = 0;
			}
		} else {
			// Signed integers do not have a symetrical range (e.g. -128 to 127). 
			if (param == -1) {
				for(x = 0; x < arraylen; x++) {
					if (data1[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
					data3[x] = data1[x] * param; 
				}
			} else {
				ovtmp1 = %(intmaxvalue)s / param;
				ovtmp2 = %(intminvalue)s / param;
				if (param > 0) {
					for(x = 0; x < arraylen; x++) {
						if ((data1[x] > ovtmp1) || (data1[x] < ovtmp2)) {return ARR_ERR_OVFL;}
						data3[x] = data1[x] * param; 
					}
				}
				if (param < 0) {
					for(x = 0; x < arraylen; x++) {
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
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp1, ovtmp2;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = data2[x] * param; 
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data2[x] = 0;
			}
		} else {
			// Signed integers do not have a symetrical range (e.g. -128 to 127). 
			if (param == -1) {
				for(x = 0; x < arraylen; x++) {
					if (data2[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
					data2[x] = data2[x] * param; 
				}
			} else {
				ovtmp1 = %(intmaxvalue)s / param;
				ovtmp2 = %(intminvalue)s / param;
				if (param > 0) {
					for(x = 0; x < arraylen; x++) {
						if ((data2[x] > ovtmp1) || (data2[x] < ovtmp2)) {return ARR_ERR_OVFL;}
						data2[x] = data2[x] * param; 
					}
				}
				if (param < 0) {
					for(x = 0; x < arraylen; x++) {
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
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp1, ovtmp2;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data2[x] * param; 
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data3[x] = 0;
			}
		} else {
			// Signed integers do not have a symetrical range (e.g. -128 to 127). 
			if (param == -1) {
				for(x = 0; x < arraylen; x++) {
					if (data2[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
					data3[x] = data2[x] * param; 
				}
			} else {
				ovtmp1 = %(intmaxvalue)s / param;
				ovtmp2 = %(intminvalue)s / param;
				if (param > 0) {
					for(x = 0; x < arraylen; x++) {
						if ((data2[x] > ovtmp1) || (data2[x] < ovtmp2)) {return ARR_ERR_OVFL;}
						data3[x] = data2[x] * param; 
					}
				}
				if (param < 0) {
					for(x = 0; x < arraylen; x++) {
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
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && ((data1[x] > (%(intmaxvalue)s / data2[x])) || (data1[x] < (%(intminvalue)s / data2[x])))) {return ARR_ERR_OVFL;}
			if ((data2[x] < -1) && ((data1[x] < (%(intmaxvalue)s / data2[x])) || (data1[x] > (%(intminvalue)s / data2[x])))) {return ARR_ERR_OVFL;}
			if ((data2[x] == -1) && (data1[x] == %(intminvalue)s)) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] * data2[x];
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] * data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * param; 
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data1[x] = 0; 
			}
		} else {
			ovtmp = %(intmaxvalue)s / param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] * param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] * param; 
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data3[x] = 0; 
			}
		} else {
			ovtmp = %(intmaxvalue)s / param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] * param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = data2[x] * param; 
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data2[x] = 0; 
			}
		} else {
			ovtmp = %(intmaxvalue)s / param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = data2[x] * param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data2[x] * param; 
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data3[x] = 0; 
			}
		} else {
			ovtmp = %(intmaxvalue)s / param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data2[x] * param; 
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
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] * data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((data2[x] != 0) && (data1[x] > (%(intmaxvalue)s / data2[x]))) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] * data2[x];
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] * data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			if (data1[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] / param; 
		}
	} else {
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			if (data1[x] == %(intminvalue)s) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] / param; 
		}
	} else {
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			// Math error check.
			if (data2[x] == 0)  {return ARR_ERR_ZERODIV;}
			if (data2[x] == -1) {return ARR_ERR_OVFL;}
			data2[x] = param / data2[x];
		}
	} else {
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			// Math error check.
			if (data2[x] == 0)  {return ARR_ERR_ZERODIV;}
			if (data2[x] == -1) {return ARR_ERR_OVFL;}
			data3[x] = param / data2[x];
		}
	} else {
		for(x = 0; x < arraylen; x++) {
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
	for(x = 0; x < arraylen; x++) {
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
	for(x = 0; x < arraylen; x++) {
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

	for(x = 0; x < arraylen; x++) {
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

	for(x = 0; x < arraylen; x++) {
		data3[x] = data1[x] / param;
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for(x = 0; x < arraylen; x++) {
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


	for(x = 0; x < arraylen; x++) {
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


	for(x = 0; x < arraylen; x++) {
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


	for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s param;
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data2[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = param %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] %(copname)s data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
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
	for(x = 0; x < arraylen; x++) {
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
	for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data1[x] = %(copname)s(data1[x] / param);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(data1[x] / param);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data2[x] = %(copname)s(param / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(param / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data1[x] = %(copname)s(data1[x] / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(data1[x] / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
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
	for(x = 0; x < arraylen; x++) {
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
	for(x = 0; x < arraylen; x++) {
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
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	if (param == 0) {return ARR_ERR_ZERODIV;}		// Math error check.
	for(x = 0; x < arraylen; x++) {
		data1[x] = data1[x] %% param;
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	// Math error check.
	if (param == 0) {return ARR_ERR_ZERODIV;}
	for(x = 0; x < arraylen; x++) {
		data3[x] = data1[x] %% param;
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	for(x = 0; x < arraylen; x++) {
		// Math error check.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data2[x] = param %% data2[x];
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	for(x = 0; x < arraylen; x++) {
		// Math error check.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data3[x] = param %% data2[x];
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for(x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data1[x] = data1[x] %% data2[x];
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] - param * floor(data1[x] / param);
		}
	} else {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] - param * floor(data1[x] / param);
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] - param * floor(data1[x] / param);
		}
	} else {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] - param * floor(data1[x] / param);
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
		for(x = 0; x < arraylen; x++) {
			data2[x] = param - data2[x] * floor(param / data2[x]);
		}
	} else {
		for(x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			data2[x] = param - data2[x] * floor(param / data2[x]);
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = param - data2[x] * floor(param / data2[x]);
		}
	} else {
		for(x = 0; x < arraylen; x++) {
			data3[x] = param - data2[x] * floor(param / data2[x]);
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
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] - data2[x] * floor(data1[x] / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] - data2[x] * floor(data1[x] / data2[x]);
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] - data2[x] * floor(data1[x] / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] - data2[x] * floor(data1[x] / data2[x]);
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
		for(x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_%(funcmodifier)s(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_%(funcmodifier)s(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_%(funcmodifier)s(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_%(funcmodifier)s(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_%(funcmodifier)s(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_%(funcmodifier)s(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data1[x] = %(copname)s(data1[x], param);
		}
	} else {
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(data1[x], param);
		}
	} else {
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data2[x] = %(copname)s(param, data2[x]);
		}
	} else {
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(param, data2[x]);
		}
	} else {
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data1[x] = %(copname)s(data1[x], data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
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
		for(x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(data1[x], data2[x]);
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = %(copname)s(data1[x], data2[x]);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}
"""

# ==============================================================================



# ==============================================================================

# This is the set of function calls used to call each operator function.
opscall = """
		// %(funcmodifier)s
		case '%(arraycode)s' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = %(funclabel)s_%(funcmodifier)s_1(arraydata.arraylength, arraydata.array1.%(arraycode)s, arraydata.param.%(arraycode)s, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = %(funclabel)s_%(funcmodifier)s_2(arraydata.arraylength, arraydata.array1.%(arraycode)s, arraydata.param.%(arraycode)s, arraydata.array3.%(arraycode)s, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = %(funclabel)s_%(funcmodifier)s_3(arraydata.arraylength, arraydata.param.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = %(funclabel)s_%(funcmodifier)s_4(arraydata.arraylength, arraydata.param.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.array3.%(arraycode)s, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = %(funclabel)s_%(funcmodifier)s_5(arraydata.arraylength, arraydata.array1.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = %(funclabel)s_%(funcmodifier)s_6(arraydata.arraylength, arraydata.array1.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.array3.%(arraycode)s, arraydata.ignoreerrors);
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
	arraydata = getparams_two(self, args, keywds, "%(funclabel)s");

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
Equivalent to:          %(opcodedocs)s \\n\\
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
\\n");

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

	# For floordiv, uint is the same as with truediv, but float differs.
	'//' : {'int' : ops_floordiv_int,
			'uint' : ops_truediv_uint,
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


# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.

funclist = [x for x in oplist if x['c_code_template'] in ['template_mathop']]


# ==============================================================================

for func in funclist:


	# Create the source code based on templates.
	filename = func['funcname'] + '.c'
	with open(filename, 'w') as f:
		funcdata = {'funclabel' : func['funcname']}
		f.write(mathops_head % {'funclabel' : func['funcname']})
		opscalltext = []

			

		# Check each array type.
		for arraycode in codegen_common.arraycodes:
			funcdata['funcmodifier'] = codegen_common.arraytypes[arraycode].replace(' ', '_')
			funcdata['arraytype'] = codegen_common.arraytypes[arraycode]
			funcdata['intmaxvalue'] = codegen_common.maxvalue[arraycode]
			funcdata['intminvalue'] = codegen_common.minvalue[arraycode]

			# This is used for pow only.
			funcdata['abs'] = absfunc[arraycode]

			# The way that powtemplate works requires that all the data in
			# 'funcdata' is defind before we get to powtemplate.
			if arraycode == 'f':
				funcdata['copname'] = func['c_operator_f']
				ops_calc = opstemplates[func['pyoperator']]['float']
			elif arraycode == 'd':
				funcdata['copname'] = func['c_operator_d']
				ops_calc = opstemplates[func['pyoperator']]['float']
			elif arraycode in codegen_common.unsignedint:
				 funcdata['copname'] = func['c_operator_i']
				 ops_calc = opstemplates[func['pyoperator']]['uint']
				 funcdata['powtemplate'] = powtemplateunsigned % funcdata
			elif arraycode in codegen_common.signedint:
				 funcdata['copname'] = func['c_operator_i']
				 ops_calc = opstemplates[func['pyoperator']]['int']
				 funcdata['powtemplate'] = powtemplatesigned % funcdata
			else:
				print('Error - Unsupported array code.', arraycode)



			f.write(ops_calc % funcdata)

			# This is the call to the functions for this array type. This
			# is inserted into another template below.
			funcdata['arraycode'] = arraycode
			opscalltext.append(opscall % funcdata)

		
		supportedarrays = codegen_common.FormatDocsArrayTypes(func['arraytypes'])

		f.write(mathops_params % {'funclabel' : func['funcname'], 
				'opcodedocs' : func['opcodedocs'], 
				'supportedarrays' : supportedarrays,
				'matherrors' : ', '.join(func['matherrors'].split(',')),
				'opscall' : ''.join(opscalltext)})


# ==============================================================================


