#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for math add operations. 
#			parameter.
# Language: Python 3.4
# Date:     30-Dec-2017
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

mathops_head = """//------------------------------------------------------------------------------
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
signed int %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data1, %(arraytype)s param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

%(simdplatform)s
	signed int errorstate;


	// SIMD version. 
	if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			%(funclabel)s_%(funcmodifier)s_1_simd(arraylen, data1, param);
		} else {
			errorstate = %(funclabel)s_%(funcmodifier)s_1_simd_ovfl(arraylen, data1, param);
			if (errorstate) {return ARR_ERR_ARITHMETIC;}
		}

	} else {
#endif
		// Math error checking disabled.
		if (ignoreerrors) {
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

%(simdplatform)s
	}
#endif

	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

%(simdplatform)s
	signed int errorstate;


	// SIMD version. 
	if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			%(funclabel)s_%(funcmodifier)s_2_simd(arraylen, data1, param, data3);
		} else {
			errorstate = %(funclabel)s_%(funcmodifier)s_2_simd_ovfl(arraylen, data1, param, data3);
			if (errorstate) {return ARR_ERR_ARITHMETIC;}
		}

	} else {
#endif
		// Math error checking disabled.
		if (ignoreerrors) {
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

%(simdplatform)s
	}
#endif

	return ARR_NO_ERR;

}


// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, int nosimd, %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

%(simdplatform)s
	signed int errorstate;


	// SIMD version. 
	if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			%(funclabel)s_%(funcmodifier)s_3_simd(arraylen, param, data2);
		} else {
			errorstate = %(funclabel)s_%(funcmodifier)s_3_simd_ovfl(arraylen, param, data2);
			if (errorstate) {return ARR_ERR_ARITHMETIC;}
		}

	} else {
#endif
		// Math error checking disabled.
		if (ignoreerrors) {
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

%(simdplatform)s
	}
#endif

	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, int nosimd, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

%(simdplatform)s
	signed int errorstate;


	// SIMD version. 
	if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			%(funclabel)s_%(funcmodifier)s_4_simd(arraylen, param, data2, data3);
		} else {
			errorstate = %(funclabel)s_%(funcmodifier)s_4_simd_ovfl(arraylen, param, data2, data3);
			if (errorstate) {return ARR_ERR_ARITHMETIC;}
		}

	} else {
#endif
		// Math error checking disabled.
		if (ignoreerrors) {
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

%(simdplatform)s
	}
#endif

	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

%(simdplatform)s
	signed int errorstate;


	// SIMD version. 
	if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			%(funclabel)s_%(funcmodifier)s_5_simd(arraylen, data1, data2);
		} else {
			errorstate = %(funclabel)s_%(funcmodifier)s_5_simd_ovfl(arraylen, data1, data2);
			if (errorstate) {return ARR_ERR_ARITHMETIC;}
		}

	} else {
#endif
		// Math error checking disabled.
		if (ignoreerrors) {
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

%(simdplatform)s
	}
#endif

	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

%(simdplatform)s
	signed int errorstate;


	// SIMD version. 
	if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			%(funclabel)s_%(funcmodifier)s_6_simd(arraylen, data1, data2, data3);
		} else {
			errorstate = %(funclabel)s_%(funcmodifier)s_6_simd_ovfl(arraylen, data1, data2, data3);
			if (errorstate) {return ARR_ERR_ARITHMETIC;}
		}

	} else {
#endif
		// Math error checking disabled.
		if (ignoreerrors) {
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

%(simdplatform)s
	}
#endif

	return ARR_NO_ERR;

}

"""


# ==============================================================================


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
	%(arraytype)s ovlimit;

%(simd_call_1_ovfl)s

		// Non-SIMD version.
		// Math error checking disabled.
		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] %(copname)s param;
			}
		} else {
		// Math error checking enabled.
			ovlimit = ovlimit_%(funcmodifier)s(param);
			for (x = 0; x < arraylen; x++) {
				if (pos_willoverflow(data1[x], ovlimit)) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] %(copname)s param;
			}
		}

%(simd_call_close)s

	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovlimit;

%(simd_call_2_ovfl)s

		// Non-SIMD version.
		// Math error checking disabled.
		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data3[x] = data1[x] %(copname)s param;
			}
		} else {
		// Math error checking enabled.
			ovlimit = ovlimit_%(funcmodifier)s(param);
			for (x = 0; x < arraylen; x++) {
				if (pos_willoverflow(data1[x], ovlimit)) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] %(copname)s param;
			}
		}

%(simd_call_close)s

	return ARR_NO_ERR;

}

// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovlimit;

%(simd_call_3_ovfl)s

		// Non-SIMD version.
		// Math error checking disabled.
		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data2[x] = param %(copname)s data2[x];
			}
		} else {
		// Math error checking enabled.
			ovlimit = ovlimit_%(funcmodifier)s(param);
			for (x = 0; x < arraylen; x++) {
				if (pos_willoverflow(data2[x], ovlimit)) {return ARR_ERR_OVFL;}
				data2[x] = param %(copname)s data2[x];
			}
		}

%(simd_call_close)s

	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovlimit;

%(simd_call_4_ovfl)s

		// Non-SIMD version.
		// Math error checking disabled.
		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data3[x] = param %(copname)s data2[x];
			}
		} else {
		// Math error checking enabled.
			ovlimit = ovlimit_%(funcmodifier)s(param);
			for (x = 0; x < arraylen; x++) {
				if (pos_willoverflow(data2[x], ovlimit)) {return ARR_ERR_OVFL;}
				data3[x] = param %(copname)s data2[x];
			}
		}

%(simd_call_close)s

	return ARR_NO_ERR;

}

// param_arr_arr_none
signed int %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovlimit;

%(simd_call_5_ovfl)s

		// Non-SIMD version.
		// Math error checking disabled.
		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data1[x] = data1[x] %(copname)s data2[x];
			}
		} else {
		// Math error checking enabled.
			for (x = 0; x < arraylen; x++) {
				ovlimit = ovlimit_%(funcmodifier)s(data2[x]);
				if (pos_willoverflow(data1[x], ovlimit)) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] %(copname)s data2[x];
			}
		}

%(simd_call_close)s

	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovlimit;

%(simd_call_6_ovfl)s

		// Non-SIMD version.
		// Math error checking disabled.
		if (ignoreerrors) {
			for (x = 0; x < arraylen; x++) {
				data3[x] = data1[x] %(copname)s data2[x];
			}
		} else {
		// Math error checking enabled.
			for (x = 0; x < arraylen; x++) {
				ovlimit = ovlimit_%(funcmodifier)s(data2[x]);
				if (pos_willoverflow(data1[x], ovlimit)) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] %(copname)s data2[x];
			}
		}

%(simd_call_close)s

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
	%(arraytype)s ovlimit;

%(simd_call_1_ovfl)s

		// Non-SIMD version.
		// Math error checking disabled.
		if (ignoreerrors) {
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
				ovlimit = pos_ovlimit_%(funcmodifier)s(param);
				for (x = 0; x < arraylen; x++) {
					if ( pos_willoverflow(data1[x], ovlimit) ) {return ARR_ERR_OVFL;}
					data1[x] = data1[x] %(copname)s param; 
				}
			}
			if (param < 0) {
				ovlimit = neg_ovlimit_%(funcmodifier)s(param);
				for (x = 0; x < arraylen; x++) {
					if ( neg_willoverflow(data1[x], ovlimit) ) {return ARR_ERR_OVFL;}
					data1[x] = data1[x] %(copname)s param; 
				}
			}
		}

%(simd_call_close)s

	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovlimit;

%(simd_call_2_ovfl)s

		// Non-SIMD version.
		// Math error checking disabled.
		if (ignoreerrors) {
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
				ovlimit = pos_ovlimit_%(funcmodifier)s(param);
				for (x = 0; x < arraylen; x++) {
					if ( pos_willoverflow(data1[x], ovlimit) ) {return ARR_ERR_OVFL;}
					data3[x] = data1[x] %(copname)s param; 
				}
			}
			if (param < 0) {
				ovlimit = neg_ovlimit_%(funcmodifier)s(param);
				for (x = 0; x < arraylen; x++) {
					if ( neg_willoverflow(data1[x], ovlimit) ) {return ARR_ERR_OVFL;}
					data3[x] = data1[x] %(copname)s param; 
				}
			}
		}

%(simd_call_close)s

	return ARR_NO_ERR;

}

// param_num_arr_none
signed int %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovlimit;

%(simd_call_3_ovfl)s

		// Non-SIMD version.
		// Math error checking disabled.
		if (ignoreerrors) {
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
				ovlimit = pos_ovlimit_%(funcmodifier)s(param);
				for (x = 0; x < arraylen; x++) {
					if ( pos_willoverflow(data2[x], ovlimit) ) {return ARR_ERR_OVFL;}
					data2[x] = data2[x] %(copname)s param; 
				}
			}
			if (param < 0) {
				ovlimit = neg_ovlimit_%(funcmodifier)s(param);
				for (x = 0; x < arraylen; x++) {
					if ( neg_willoverflow(data2[x], ovlimit) ) {return ARR_ERR_OVFL;}
					data2[x] = data2[x] %(copname)s param; 
				}
			}
		}

%(simd_call_close)s

	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen,%(nosimddecl)s %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	%(arraytype)s ovlimit;

%(simd_call_4_ovfl)s

		// Non-SIMD version.
		// Math error checking disabled.
		if (ignoreerrors) {
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
				ovlimit = pos_ovlimit_%(funcmodifier)s(param);
				for (x = 0; x < arraylen; x++) {
					if ( pos_willoverflow(data2[x], ovlimit) ) {return ARR_ERR_OVFL;}
					data3[x] = data2[x] %(copname)s param; 
				}
			}
			if (param < 0) {
				ovlimit = neg_ovlimit_%(funcmodifier)s(param);
				for (x = 0; x < arraylen; x++) {
					if ( neg_willoverflow(data2[x], ovlimit) ) {return ARR_ERR_OVFL;}
					data3[x] = data2[x] %(copname)s param; 
				}
			}
		}

%(simd_call_close)s

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
			if (loop_willoverflow_%(funcmodifier)s(data1[x], data2[x])) {return ARR_ERR_OVFL;}
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
			if (loop_willoverflow_%(funcmodifier)s(data1[x], data2[x])) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] %(copname)s data2[x];
			}
		}

	return ARR_NO_ERR;

}
"""


# ==============================================================================


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

# This should be created once only as it is not type dependent. 
# It also includes the parameter descriptions for the type dependent
# macros, so it needs to appear first.
int_ovcheck = """
/*--------------------------------------------------------------------------- */
/* The integer overflow limit check. 
   val = The parameter value being checked. 
   ovlimit = The previously calculated overflow limit.
   Returns True if overflow will happen. 
*/
// For when ovlimit was calculated on a positive value (pos_ovlimit_).
#define pos_willoverflow(val, ovlimit) ( val > ovlimit )
// For when ovlimit was calculated on a negative value (neg_ovlimit_).
#define neg_willoverflow(val, ovlimit) ( val < ovlimit )


/*--------------------------------------------------------------------------- */
/* ovlimit_*
   Calculate the maximum value an integer can be without overflowing.
   This is used for equations where we need to know the maximum value 
   (magnitude for either +ve or -ve) which can be used in a calculation 
   without it overflowing. 
   val = The parameter value being checked.
   Returns the overflow limit. 

   loop_willoverflow_*
   This combined ovlimit and pos_willoverflow and neg_willoverflow. Use
   this in loops where both sides of the equation are arraya and the 
   limit must be recalculated every iteration.
   lval, rval = The respective current values of the arrays.
   Returns True if the current operation will result in an integer overflow.

*/"""

# Create this for each signed integers type.
intov_macros_signed = """
/*--------------------------------------------------------------------------- */
// For %(arraytype)s.
// For when val is positive or negative. Do not use in loops.
#define ovlimit_%(funcmodifier)s(val) (val >= 0) ? ( %(intmaxvalue)s - val ) : ( %(intminvalue)s - val )
// For when val is positive. Use when called in loops.
#define pos_ovlimit_%(funcmodifier)s(val) %(intmaxvalue)s - val
// For when val is negative. Use when called in loops.
#define neg_ovlimit_%(funcmodifier)s(val) %(intminvalue)s - val

// For use in loops when both parameters are arrays and are changing. 
#define loop_willoverflow_%(funcmodifier)s(lval, rval) \\
							(((rval > 0) && (lval > (%(intmaxvalue)s - rval))) \\
							|| ((rval < 0) && (lval < (%(intminvalue)s - rval))))

"""

# Create this for each unsigned integers type.
intov_macros_unsigned = """
/*--------------------------------------------------------------------------- */
// For %(arraytype)s.
// For unsigned. Can use in loops and outside loops.
#define ovlimit_%(funcmodifier)s(val) ( %(intmaxvalue)s - val )

#define loop_willoverflow_%(funcmodifier)s(lval, rval) (lval > (%(intmaxvalue)s - rval))

"""

# ==============================================================================


# ==============================================================================

# The operations using SIMD. This handles multiple different SIMD operations.
# This version does not check for overflow.
ops_simdsupport = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   This version is without overflow checking.
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

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_%(funcmodifier)s(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data1[x]);
		// The actual SIMD operation. 
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

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceright = initvec_%(funcmodifier)s(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data1[x]);
		// The actual SIMD operation.
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

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_%(funcmodifier)s(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceright = %(vldinstr)s &data2[x]);
		// The actual SIMD operation.
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

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, resultslice;


	// Initialise the comparison values.
	datasliceleft = initvec_%(funcmodifier)s(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceright = %(vldinstr)s &data2[x]);
		// The actual SIMD operation.
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
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data1[x]);
		datasliceright = %(vldinstr)s &data2[x]);
		// The actual SIMD operation.
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
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data1[x]);
		datasliceright = %(vldinstr)s &data2[x]);
		// The actual SIMD operation.
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


# ==============================================================================

# The signed operations using SIMD. This handles multiple different SIMD operations.
# This version checks for overflow but does NOT do array to array.
ops_simdsupport_ovfl_signed = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   This version supports overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   Returns 1 if overflow occurred, else returns 0.
*/
// param_arr_num_none
%(simdplatform)s
char %(funclabel)s_%(funcmodifier)s_1_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(arraytype)s ovlimit;
	%(simdattr)s datasliceleft, datasliceright, resultslice, ovflvec;
	%(ovflsimdattr)s ovcheck;
	%(simd_ovflchk_extravars)s


	// We don't need to do anything if param is zero.
	if (param == 0) {
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_%(funcmodifier)s(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// param is positive.
	if (param > 0) {

		// Used to calculate overflow.
		ovlimit = pos_ovlimit_%(funcmodifier)s(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_%(funcmodifier)s(ovlimit);


		for (x = 0; x < alignedlength; x += %(simdwidth)s) {
			// Load the data into the vector register.
			datasliceleft = %(vldinstr)s &data1[x]);

			// Check for overflow. 
			%(ovf_check1)s
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = %(vopinstr)s(datasliceleft, datasliceright);

			// Store the result.
			%(vstinstr1)s &data1[x], %(vstinstr2)s resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( pos_willoverflow(data1[x], ovlimit) ) {return 1;}
			data1[x] = data1[x] + param; 
		}

	}


	// param is negative.
	if (param < 0) {

		// Used to calculate overflow.
		ovlimit = neg_ovlimit_%(funcmodifier)s(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_%(funcmodifier)s(ovlimit);


		for (x = 0; x < alignedlength; x += %(simdwidth)s) {
			// Load the data into the vector register.
			datasliceleft = %(vldinstr)s &data1[x]);

			// Check for overflow. 
			%(ovf_check2)s
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = %(vopinstr)s(datasliceleft, datasliceright);

			// Store the result.
			%(vstinstr1)s &data1[x], %(vstinstr2)s resultslice);

		}
	
		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( neg_willoverflow(data1[x], ovlimit) ) {return 1;}
			data1[x] = data1[x] + param; 
		}
	}

	return 0;

}



// param_arr_num_arr
char %(funclabel)s_%(funcmodifier)s_2_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(arraytype)s ovlimit;
	%(simdattr)s datasliceleft, datasliceright, resultslice, ovflvec;
	%(ovflsimdattr)s ovcheck;
	%(simd_ovflchk_extravars)s


	// We don't need to do anything if param is zero, just copy the data.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = data1[x];
		}
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_%(funcmodifier)s(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// param is positive.
	if (param > 0) {

		// Used to calculate overflow.
		ovlimit = pos_ovlimit_%(funcmodifier)s(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_%(funcmodifier)s(ovlimit);


		for (x = 0; x < alignedlength; x += %(simdwidth)s) {
			// Load the data into the vector register.
			datasliceleft = %(vldinstr)s &data1[x]);

			// Check for overflow. 
			%(ovf_check1)s
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = %(vopinstr)s(datasliceleft, datasliceright);

			// Store the result.
			%(vstinstr1)s &data3[x], %(vstinstr2)s resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( pos_willoverflow(data1[x], ovlimit) ) {return 1;}
			data3[x] = data1[x] + param; 
		}
	}


	// param is negative.
	if (param < 0) {

		// Used to calculate overflow.
		ovlimit = neg_ovlimit_%(funcmodifier)s(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_%(funcmodifier)s(ovlimit);


		for (x = 0; x < alignedlength; x += %(simdwidth)s) {
			// Load the data into the vector register.
			datasliceleft = %(vldinstr)s &data1[x]);

			// Check for overflow. 
			%(ovf_check2)s
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = %(vopinstr)s(datasliceleft, datasliceright);

			// Store the result.
			%(vstinstr1)s &data3[x], %(vstinstr2)s resultslice);

		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( neg_willoverflow(data1[x], ovlimit) ) {return 1;}
			data3[x] = data1[x] + param; 
		}
	}

	return 0;

}



// param_num_arr_none
char %(funclabel)s_%(funcmodifier)s_3_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(arraytype)s ovlimit;
	%(simdattr)s datasliceleft, datasliceright, resultslice, ovflvec;
	%(ovflsimdattr)s ovcheck;
	%(simd_ovflchk_extravars)s


	// We don't need to do anything if param is zero.
	if (param == 0) {
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_%(funcmodifier)s(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// param is positive.
	if (param > 0) {

		ovlimit = pos_ovlimit_%(funcmodifier)s(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_%(funcmodifier)s(ovlimit);


		for (x = 0; x < alignedlength; x += %(simdwidth)s) {
			// Load the data into the vector register.
			datasliceleft = %(vldinstr)s &data2[x]);

			// Check for overflow. 
			%(ovf_check1)s
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = %(vopinstr)s(datasliceleft, datasliceright);

			// Store the result.
			%(vstinstr1)s &data2[x], %(vstinstr2)s resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( pos_willoverflow(data2[x], ovlimit) ) {return 1;}
			data2[x] = data2[x] + param; 
		}
	}


	// param is negative.
	if (param < 0) {

		// Used to calculate overflow.
		ovlimit = neg_ovlimit_%(funcmodifier)s(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_%(funcmodifier)s(ovlimit);


		for (x = 0; x < alignedlength; x += %(simdwidth)s) {
			// Load the data into the vector register.
			datasliceleft = %(vldinstr)s &data2[x]);

			// Check for overflow. 
			%(ovf_check2)s
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = %(vopinstr)s(datasliceleft, datasliceright);

			// Store the result.
			%(vstinstr1)s &data2[x], %(vstinstr2)s resultslice);

		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( neg_willoverflow(data2[x], ovlimit) ) {return 1;}
			data2[x] = data2[x] + param;
		}
	}

	return 0;

}



// param_num_arr_arr
char %(funclabel)s_%(funcmodifier)s_4_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(arraytype)s ovlimit;
	%(simdattr)s datasliceleft, datasliceright, resultslice, ovflvec;
	%(ovflsimdattr)s ovcheck;
	%(simd_ovflchk_extravars)s


	// We don't need to do anything if param is zero, just copy the data.
	if (param == 0) {
		for (x = 0; x < arraylen; x++) {
		data3[x] = data2[x];
		}
		return 0;
	}


	// Initialise the param values.
	datasliceright = initvec_%(funcmodifier)s(param);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// param is positive.
	if (param > 0) {

		// Used to calculate overflow.
		ovlimit = pos_ovlimit_%(funcmodifier)s(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_%(funcmodifier)s(ovlimit);


		for (x = 0; x < alignedlength; x += %(simdwidth)s) {
			// Load the data into the vector register.
			datasliceleft = %(vldinstr)s &data2[x]);

			// Check for overflow. 
			%(ovf_check1)s
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = %(vopinstr)s(datasliceleft, datasliceright);

			// Store the result.
			%(vstinstr1)s &data3[x], %(vstinstr2)s resultslice);
		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( pos_willoverflow(data2[x], ovlimit) ) {return 1;}
			data3[x] = data2[x] + param;
		}
	}


	// param is negative.
	if (param < 0) {

		// Used to calculate overflow.
		ovlimit = neg_ovlimit_%(funcmodifier)s(param);

		// This is used for detecting a potential overflow condition.
		ovflvec = initvec_%(funcmodifier)s(ovlimit);


		for (x = 0; x < alignedlength; x += %(simdwidth)s) {
			// Load the data into the vector register.
			datasliceleft = %(vldinstr)s &data2[x]);

			// Check for overflow. 
			%(ovf_check2)s
				return 1;
			}

			// The actual SIMD operation. 
			resultslice = %(vopinstr)s(datasliceleft, datasliceright);

			// Store the result.
			%(vstinstr1)s &data3[x], %(vstinstr2)s resultslice);

		}

		// Handle the values left over at the end of the array.
		for (x = alignedlength; x < arraylen; x++) {
			if ( neg_willoverflow(data2[x], ovlimit) ) {return 1;}
			data3[x] = data2[x] + param; 
		}
	}

	return 0;

}
#endif

"""



# ==============================================================================

# The unsigned operations using SIMD. This handles multiple different SIMD operations.
# This version checks for overflow and DOES do array to array.
ops_simdsupport_ovfl_unsigned = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   This version is with overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num_none
%(simdplatform)s
char %(funclabel)s_%(funcmodifier)s_1_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(arraytype)s ovlimit;
	%(simdattr)s datasliceleft, datasliceright, resultslice, ovflvec;
	%(ovflsimdattr)s ovcheck;
	%(simd_ovflchk_extravars)s


	// Initialise the comparison values.
	datasliceright = initvec_%(funcmodifier)s(param);


	// Used to calculate overflow.
	ovlimit = ovlimit_%(funcmodifier)s(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_%(funcmodifier)s(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data1[x]);

		// Check for overflow. 
		%(ovf_check1)s
			return 1;
		}

		// The actual SIMD operation. 
		resultslice = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr1)s &data1[x], %(vstinstr2)s resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( pos_willoverflow(data1[x], ovlimit) ) {return 1;}
		data1[x] = data1[x] + param;
	}

	return 0;

}



// param_arr_num_arr
char %(funclabel)s_%(funcmodifier)s_2_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(arraytype)s ovlimit;
	%(simdattr)s datasliceleft, datasliceright, resultslice, ovflvec;
	%(ovflsimdattr)s ovcheck;
	%(simd_ovflchk_extravars)s


	// Initialise the comparison values.
	datasliceright = initvec_%(funcmodifier)s(param);


	// Used to calculate overflow.
	ovlimit = ovlimit_%(funcmodifier)s(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_%(funcmodifier)s(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data1[x]);

		// Check for overflow. 
		%(ovf_check1)s
			return 1;
		}

		// The actual SIMD operation.
		resultslice = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr1)s &data3[x], %(vstinstr2)s resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( pos_willoverflow(data1[x], ovlimit) ) {return 1;}
		data3[x] = data1[x] + param;
	}

	return 0;

}



// param_num_arr_none
char %(funclabel)s_%(funcmodifier)s_3_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(arraytype)s ovlimit;
	%(simdattr)s datasliceleft, datasliceright, resultslice, ovflvec;
	%(ovflsimdattr)s ovcheck;
	%(simd_ovflchk_extravars)s


	// Initialise the comparison values.
	datasliceright = initvec_%(funcmodifier)s(param);

	// Used to calculate overflow.
	ovlimit = ovlimit_%(funcmodifier)s(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_%(funcmodifier)s(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data2[x]);

		// Check for overflow. 
		%(ovf_check1)s
			return 1;
		}

		// The actual SIMD operation.
		resultslice = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr1)s &data2[x], %(vstinstr2)s resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( pos_willoverflow(data2[x], ovlimit) ) {return 1;}
		data2[x] = param + data2[x];
	}

	return 0;

}



// param_num_arr_arr
char %(funclabel)s_%(funcmodifier)s_4_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(arraytype)s ovlimit;
	%(simdattr)s datasliceleft, datasliceright, resultslice, ovflvec;
	%(ovflsimdattr)s ovcheck;
	%(simd_ovflchk_extravars)s


	// Initialise the comparison values.
	datasliceright = initvec_%(funcmodifier)s(param);


	// Used to calculate overflow.
	ovlimit = ovlimit_%(funcmodifier)s(param);

	// This is used for detecting a potential overflow condition.
	ovflvec = initvec_%(funcmodifier)s(ovlimit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data2[x]);

		// Check for overflow. 
		%(ovf_check1)s
			return 1;
		}

		// The actual SIMD operation.
		resultslice = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr1)s &data3[x], %(vstinstr2)s resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( pos_willoverflow(data2[x], ovlimit) ) {return 1;}
		data3[x] = param + data2[x];
	}

	return 0;

}



// param_arr_arr_none
char %(funclabel)s_%(funcmodifier)s_5_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	static %(arraytype)s ovcompvals[%(simdwidth)s] = {%(simdovintmaxvals)s};
	%(simdattr)s datasliceleft, datasliceright, resultslice, ovcompslice, ovflvec;
	%(ovflsimdattr)s ovcheck;
	%(simd_ovflchk_extravars)s


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Used to check for overflows.
	ovcompslice = %(vldinstr)s ovcompvals);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data1[x]);
		datasliceright = %(vldinstr)s &data2[x]);

		// Subtract the right hand value.
		ovflvec = %(vsubinstr)s(ovcompslice, datasliceright);

		// Check for overflow. 
		%(ovf_check1)s
			return 1;
		}

		// The actual SIMD operation.
		resultslice = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr1)s &data1[x], %(vstinstr2)s resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( loop_willoverflow_%(funcmodifier)s(data1[x], data2[x]) ) {return 1;}
		data1[x] = data1[x] + data2[x];
	}

	return 0;

}



// param_arr_arr_arr
char %(funclabel)s_%(funcmodifier)s_6_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	static %(arraytype)s ovcompvals[%(simdwidth)s] = {%(simdovintmaxvals)s};
	%(simdattr)s datasliceleft, datasliceright, resultslice, ovcompslice, ovflvec;
	%(ovflsimdattr)s ovcheck;
	%(simd_ovflchk_extravars)s


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Used to check for overflows.
	ovcompslice = %(vldinstr)s ovcompvals);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data1[x]);
		datasliceright = %(vldinstr)s &data2[x]);

		// Subtract the right hand value.
		ovflvec = %(vsubinstr)s(ovcompslice, datasliceright);

		// Check for overflow. 
		%(ovf_check1)s
			return 1;
		}

		// The actual SIMD operation.
		resultslice = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr1)s &data3[x], %(vstinstr2)s resultslice);
	}

	// Handle the values left over at the end of the array.
	for (x = alignedlength; x < arraylen; x++) {
		if ( loop_willoverflow_%(funcmodifier)s(data1[x], data2[x]) ) {return 1;}
		data3[x] = data1[x] + data2[x];
	}

	return 0;

}
#endif

/*--------------------------------------------------------------------------- */
"""



# ==============================================================================

# The floating point operations using SIMD. This includes overflow conditions.
ops_simdsupport_ovfl_float = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   This version is without overflow checking.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   Returns 1 if overflow occurred, else returns 0.
*/
// param_arr_num_none
%(simdplatform)s
char %(funclabel)s_%(funcmodifier)s_1_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, resultslice, checkslice;

	%(arraytype)s checkvecresults[%(simdwidth)s];
	%(arraytype)s checksliceinit[%(simdwidth)s] = {0.0};


	// Initialise the comparison values.
	datasliceright = initvec_%(funcmodifier)s(param);

	// This is used to check for errors by accumulating non-finite values.
	checkslice = %(vldinstr)s checksliceinit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data1[x]);
		// The actual SIMD operation. 
		resultslice = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr1)s &data1[x], %(vstinstr2)s resultslice);

		// Check the result. None-finite errors should accumulate.
		checkslice = %(simdmul)s(checkslice, resultslice);
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
		data1[x] = data1[x] %(copname)s param;
		if (!isfinite(data1[x])) {return 1;}
	}

	return 0;

}



// param_arr_num_arr
char %(funclabel)s_%(funcmodifier)s_2_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, resultslice, checkslice;

	%(arraytype)s checkvecresults[%(simdwidth)s];
	%(arraytype)s checksliceinit[%(simdwidth)s] = {0.0};


	// Initialise the comparison values.
	datasliceright = initvec_%(funcmodifier)s(param);

	// This is used to check for errors by accumulating non-finite values.
	checkslice = %(vldinstr)s checksliceinit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data1[x]);
		// The actual SIMD operation.
		resultslice = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr1)s &data3[x], %(vstinstr2)s resultslice);

		// Check the result. None-finite errors should accumulate.
		checkslice = %(simdmul)s(checkslice, resultslice);
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
		data3[x] = data1[x] %(copname)s param;
		if (!isfinite(data3[x])) {return 1;}
	}

	return 0;

}



// param_num_arr_none
char %(funclabel)s_%(funcmodifier)s_3_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, resultslice, checkslice;

	%(arraytype)s checkvecresults[%(simdwidth)s];
	%(arraytype)s checksliceinit[%(simdwidth)s] = {0.0};


	// Initialise the comparison values.
	datasliceleft = initvec_%(funcmodifier)s(param);

	// This is used to check for errors by accumulating non-finite values.
	checkslice = %(vldinstr)s checksliceinit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceright = %(vldinstr)s &data2[x]);
		// The actual SIMD operation.
		resultslice = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr1)s &data2[x], %(vstinstr2)s resultslice);

		// Check the result. None-finite errors should accumulate.
		checkslice = %(simdmul)s(checkslice, resultslice);
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
		data2[x] = param %(copname)s data2[x];
		if (!isfinite(data2[x])) {return 1;}
	}

	return 0;

}



// param_num_arr_arr
char %(funclabel)s_%(funcmodifier)s_4_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, resultslice, checkslice;

	%(arraytype)s checkvecresults[%(simdwidth)s];
	%(arraytype)s checksliceinit[%(simdwidth)s] = {0.0};


	// Initialise the comparison values.
	datasliceleft = initvec_%(funcmodifier)s(param);

	// This is used to check for errors by accumulating non-finite values.
	checkslice = %(vldinstr)s checksliceinit);


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = calcalignedlength(arraylen, %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (x = 0; x < alignedlength; x += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceright = %(vldinstr)s &data2[x]);
		// The actual SIMD operation.
		resultslice = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr1)s &data3[x], %(vstinstr2)s resultslice);

		// Check the result. None-finite errors should accumulate.
		checkslice = %(simdmul)s(checkslice, resultslice);
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
		data3[x] = param %(copname)s data2[x];
		if (!isfinite(data3[x])) {return 1;}
	}

	return 0;

}



// param_arr_arr_none
char %(funclabel)s_%(funcmodifier)s_5_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, resultslice, checkslice;

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
		datasliceleft = %(vldinstr)s &data1[x]);
		datasliceright = %(vldinstr)s &data2[x]);
		// The actual SIMD operation.
		resultslice = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr1)s &data1[x], %(vstinstr2)s resultslice);

		// Check the result. None-finite errors should accumulate.
		checkslice = %(simdmul)s(checkslice, resultslice);
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
		data1[x] = data1[x] %(copname)s data2[x];
		if (!isfinite(data1[x])) {return 1;}
	}

	return 0;

}



// param_arr_arr_arr
char %(funclabel)s_%(funcmodifier)s_6_simd_ovfl(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3) {

	// array index counter. 
	Py_ssize_t x; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, resultslice, checkslice;

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
		datasliceleft = %(vldinstr)s &data1[x]);
		datasliceright = %(vldinstr)s &data2[x]);
		// The actual SIMD operation.
		resultslice = %(vopinstr)s(datasliceleft, datasliceright);
		// Store the result.
		%(vstinstr1)s &data3[x], %(vstinstr2)s resultslice);

		// Check the result. None-finite errors should accumulate.
		checkslice = %(simdmul)s(checkslice, resultslice);
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
		data3[x] = data1[x] %(copname)s data2[x];
		if (!isfinite(data3[x])) {return 1;}
	}

	return 0;

}
#endif

/*--------------------------------------------------------------------------- */
"""

# ==============================================================================

# ==============================================================================

# The template for overflow checks for x86_64. This requires the correct SIMD attribute
# to be insertered before itself being inserted into the next template.
simd_ovflchk1_x86 = '''// Do a greater than compare operation.
			ovcheck = %(vgtinstr)s (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {'''

simd_ovflchk2_x86 = '''// Do a less than compare operation.
			ovcheck = %(vltinstr)s (ovflvec, datasliceleft);

			// Check for overflow. 
			if (!(__builtin_ia32_pmovmskb128((v16qi) ovcheck) == 0x0000)) {'''


# The template for overflow checks for ARM NEON ARMv7 32 bit. This requires the correct SIMD size
#  and sign (e.g. u8, s16, etc.) to be insertered before itself being inserted into the next template.
simd_ovflchk1_armv7 = '''// Do a greater than compare operation.
			ovcheck = %(vgtinstr)s (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(%(vreinterpinstr)s(ovcheck) == 0x0000000000000000)) {'''

simd_ovflchk2_armv7 = '''// Do a less than compare operation.
			ovcheck = %(vltinstr)s (datasliceleft, ovflvec);

			// Check for overflow. 
			if (!(%(vreinterpinstr)s(ovcheck) == 0x0000000000000000)) {'''


# The template for overflow checks for ARM NEON ARMv8 64 bit. This requires the correct SIMD size
#  and sign (e.g. u8, s16, etc.) to be insertered before itself being inserted into the next template.
simd_ovflchk1_armv8 = '''// Do a greater than compare operation.
			ovcheck = %(vgtinstr)s (datasliceleft, ovflvec);

			// Check for overflow. 
			// Combine the result to two 64 bit vectors.
			veccombine = %(vreinterpinstr)s(ovcheck);
			// Get the high and low lanes of the combined vector.
			lowresult = vgetq_lane_u64(veccombine, 0);
			highresult = vgetq_lane_u64(veccombine, 1);
			// Check if overflow will happen.
			if ((lowresult != 0x0000000000000000) || (highresult != 0x0000000000000000)) {'''

simd_ovflchk2_armv8 = '''// Do a less than compare operation.
			ovcheck = %(vltinstr)s (datasliceleft, ovflvec);

			// Check for overflow. 
			// Combine the result to two 64 bit vectors.
			veccombine = %(vreinterpinstr)s(ovcheck);
			// Get the high and low lanes of the combined vector.
			lowresult = vgetq_lane_u64(veccombine, 0);
			highresult = vgetq_lane_u64(veccombine, 1);
			// Check if overflow will happen.
			if ((lowresult != 0x0000000000000000) || (highresult != 0x0000000000000000)) {'''


simd_ovflchk_extravars_armv8 = '''uint64x2_t veccombine;
	uint64_t highresult, lowresult;'''


# ==============================================================================


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
		if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
			%(funclabel)s_%(funcmodifier)s_1_simd(arraylen, data1, param);
			return ARR_NO_ERR;
		}
#endif\n''',

'simd_call_2' : '''\n%(simdplatform)s
		// SIMD version.
		if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
			%(funclabel)s_%(funcmodifier)s_2_simd(arraylen, data1, param, data3);
			return ARR_NO_ERR;
		}
#endif\n''',

'simd_call_3' : '''\n%(simdplatform)s
		// SIMD version.
		if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
			%(funclabel)s_%(funcmodifier)s_3_simd(arraylen, param, data2);
			return ARR_NO_ERR;
		}
#endif\n''',

'simd_call_4' : '''\n%(simdplatform)s
		// SIMD version.
		if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
			%(funclabel)s_%(funcmodifier)s_4_simd(arraylen, param, data2, data3);
			return ARR_NO_ERR;
		}
#endif\n''',

'simd_call_5' : '''\n%(simdplatform)s
		// SIMD version.
		if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
			%(funclabel)s_%(funcmodifier)s_5_simd(arraylen, data1, data2);
			return ARR_NO_ERR;
		}
#endif\n''',

'simd_call_6' : '''\n%(simdplatform)s
		// SIMD version.
		if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
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

# SIMD call template for overflow checking. This has to handle multiple 
# template strings, and so is presented as a dictionary to allow it to be handled
# iteratively. 

SIMD_call_ovfl = {
'simd_call_1_ovfl' : '''\n%(simdplatform)s
	char ovflresult;

	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			%(funclabel)s_%(funcmodifier)s_1_simd(arraylen, data1, param);
		} else {
		// Math error checking enabled.
			ovflresult = %(funclabel)s_%(funcmodifier)s_1_simd_ovfl(arraylen, data1, param);
			if (ovflresult) { return ARR_ERR_OVFL; }
		}

	} else {
#endif\n''',

'simd_call_2_ovfl' : '''\n%(simdplatform)s
	char ovflresult;

	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			%(funclabel)s_%(funcmodifier)s_2_simd(arraylen, data1, param, data3);
		} else {
		// Math error checking enabled.
			ovflresult = %(funclabel)s_%(funcmodifier)s_2_simd_ovfl(arraylen, data1, param, data3);
			if (ovflresult) { return ARR_ERR_OVFL; }
		}

	} else {
#endif\n''',

'simd_call_3_ovfl' : '''\n%(simdplatform)s
	char ovflresult;

	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			%(funclabel)s_%(funcmodifier)s_3_simd(arraylen, param, data2);
		} else {
		// Math error checking enabled.
			ovflresult = %(funclabel)s_%(funcmodifier)s_3_simd_ovfl(arraylen, param, data2);
			if (ovflresult) { return ARR_ERR_OVFL; }
		}

	} else {
#endif\n''',

'simd_call_4_ovfl' : '''\n%(simdplatform)s
	char ovflresult;

	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			%(funclabel)s_%(funcmodifier)s_4_simd(arraylen, param, data2, data3);
		} else {
		// Math error checking enabled.
			ovflresult = %(funclabel)s_%(funcmodifier)s_4_simd_ovfl(arraylen, param, data2, data3);
			if (ovflresult) { return ARR_ERR_OVFL; }
		}

	} else {
#endif\n''',

'simd_call_5_ovfl' : '''\n%(simdplatform)s
	char ovflresult;

	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			%(funclabel)s_%(funcmodifier)s_5_simd(arraylen, data1, data2);
		} else {
		// Math error checking enabled.
			ovflresult = %(funclabel)s_%(funcmodifier)s_5_simd_ovfl(arraylen, data1, data2);
			if (ovflresult) { return ARR_ERR_OVFL; }
		}

	} else {
#endif\n''',

'simd_call_6_ovfl' : '''\n%(simdplatform)s
	char ovflresult;

	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, %(simdwidth)s)) {
		// Math error checking disabled.
		if (ignoreerrors) {
			%(funclabel)s_%(funcmodifier)s_6_simd(arraylen, data1, data2, data3);
		} else {
		// Math error checking enabled.
			ovflresult = %(funclabel)s_%(funcmodifier)s_6_simd_ovfl(arraylen, data1, data2, data3);
			if (ovflresult) { return ARR_ERR_OVFL; }
		}

	} else {
#endif\n''',

'simd_call_close' : '''\n%(simdplatform)s
	}
#endif\n''',
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
	'b' : '(v16qi) __builtin_ia32_paddb128', 
	'h' : '(v8hi) __builtin_ia32_paddw128', 
	'i' : '(v4si) __builtin_ia32_paddd128', 
	'f' : '__builtin_ia32_addps', 
	'd' : '__builtin_ia32_addpd', 
}


# Greater than instruction for overflow checking.
# This is also used for less than by reversing the parameters.
vgtinstr_x86 = {
	'b' : '__builtin_ia32_pcmpgtb128', 
	'h' : '__builtin_ia32_pcmpgtw128', 
	'i' : '__builtin_ia32_pcmpgtd128 ', 
	'f' : '', 
	'd' : '',  
}


# This is the width of the SIMD registers in number of bits.
simdwidth_x86 = 128

# SIMD mask initialisation data.
simdovintmaxvals_x86 = {	'b' : ', '.join(['SCHAR_MIN'] * (simdwidth_x86 // 8)), 
	'h' : ', '.join(['SHRT_MIN'] * (simdwidth_x86 // 16)), 
	'i' : ', '.join(['INT_MIN'] * (simdwidth_x86 // 32)), 
}


# Multiplication, used for checking for math errors.
simdmulop_x86 = {'f' : '__builtin_ia32_mulps', 
				'd' : '__builtin_ia32_mulpd'}


# A list of which array types are supported by x86 SIMD instructions.
x86_simdtypes = tuple(simdop_x86.keys())


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
	'f' : 'float32x2_t',
}

ovflsimdattr_armv7 = {
	'b' : 'uint8x8_t',
	'B' : 'uint8x8_t',
	'h' : 'uint16x4_t',
	'H' : 'uint16x4_t',
	'f' : 'float32x2_t',
}


vldinstr_armv7 = {
	'b' : 'vld1_s8(',
	'B' : 'vld1_u8(',
	'h' : 'vld1_s16(',
	'H' : 'vld1_u16(',
	'f' : 'vld1_f32(',
}

vstinstr1_armv7 = {
	'b' : 'vst1_s8(',
	'B' : 'vst1_u8(',
	'h' : 'vst1_s16(',
	'H' : 'vst1_u16(',
	'f' : 'vst1_f32(',
}


vstinstr2_armv7 = {
	'b' : '',
	'B' : '',
	'h' : '',
	'H' : '',
	'f' : '',
}


armvecsize_armv7 = {
	'b' : 's8',
	'B' : 'u8',
	'h' : 's16',
	'H' : 'u16',
}

# SIMD operations.
simdop_armv7 = {
	'b' : 'vadd_s8', 
	'B' : 'vadd_u8', 
	'h' : 'vadd_s16', 
	'H' : 'vadd_u16', 
	'f' : 'vadd_f32', 
}


# Greater than instruction for overflow checking.
vgtinstr_armv7 = {
	'b' : 'vcgt_s8', 
	'B' : 'vcgt_u8', 
	'h' : 'vcgt_s16', 
	'H' : 'vcgt_u16', 
	'f' : '', 
}

# Less than instruction for overflow checking.
vltinstr_armv7 = {
	'b' : 'vclt_s8', 
	'B' : 'vclt_u8', 
	'h' : 'vclt_s16', 
	'H' : 'vclt_u16', 
	'f' : '', 
}

# Used to calculate overflow conditions.
vsubinstr_armv7 = {
	'b' : 'vsub_s8', 
	'B' : 'vsub_u8', 
	'h' : 'vsub_s16', 
	'H' : 'vsub_u16', 
	'f' : '', 
}


# Used to turn vector results into integers so we can examine them.
vreinterpinstr_armv7 = {
	'b' : 'vreinterpret_u64_u8', 
	'B' : 'vreinterpret_u64_u8', 
	'h' : 'vreinterpret_u64_u16', 
	'H' : 'vreinterpret_u64_u16', 
	'f' : '', 
}


# This is the width of the SIMD registers in number of bits.
simdwidth_armv7 = 64

# SIMD mask initialisation data.
simdovintmaxvals_armv7 = {
	'b' : ', '.join(['SCHAR_MIN'] * (simdwidth_armv7 // 8)), 
	'B' : ', '.join(['UCHAR_MAX'] * (simdwidth_armv7 // 8)), 
	'h' : ', '.join(['SHRT_MIN'] * (simdwidth_armv7 // 16)), 
	'H' : ', '.join(['USHRT_MAX'] * (simdwidth_armv7 // 16)), 
	'i' : ', '.join(['INT_MIN'] * (simdwidth_armv7 // 32)), 
	'I' : ', '.join(['UINT_MAX'] * (simdwidth_armv7 // 32)), 
}


# Which array types have overflow checking.
simdovfl_armv7 = ('b', 'B', 'h', 'H')

# A list of which array types are supported by ARM SIMD instructions.
armv7_simdtypes  = tuple(simdop_armv7.keys())

# Multiplication, used for checking for math errors.
simdmulop_armv7 = 'vmul_f32'


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


armvecsize_armv8 = {
	'b' : 's8',
	'B' : 'u8',
	'h' : 's16',
	'H' : 'u16',
	'i' : 's32',
	'I' : 'u32',
}


# SIMD operations.
simdop_armv8 = {
	'b' : 'vaddq_s8', 
	'B' : 'vaddq_u8', 
	'h' : 'vaddq_s16', 
	'H' : 'vaddq_u16', 
	'i' : 'vaddq_s32', 
	'I' : 'vaddq_u32', 
	'f' : 'vaddq_f32', 
}


# Greater than instruction for overflow checking.
vgtinstr_armv8 = {
	'b' : 'vcgtq_s8', 
	'B' : 'vcgtq_u8', 
	'h' : 'vcgtq_s16', 
	'H' : 'vcgtq_u16', 
	'i' : 'vcgtq_s32', 
	'I' : 'vcgtq_u32', 
	'f' : '', 
}


# Less than instruction for overflow checking.
vltinstr_armv8 = {
	'b' : 'vcltq_s8', 
	'B' : 'vcltq_u8', 
	'h' : 'vcltq_s16', 
	'H' : 'vcltq_u16', 
	'i' : 'vcltq_s32', 
	'I' : 'vcltq_u32', 
	'f' : '', 
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


# Used to calculate overflow conditions.
vsubinstr_armv8 = {
	'b' : 'vsubq_s8', 
	'B' : 'vsubq_u8', 
	'h' : 'vsubq_s16', 
	'H' : 'vsubq_u16', 
	'i' : 'vsubq_s32', 
	'I' : 'vsubq_u32', 
	'f' : '', 
}


# Which array types have overflow checking.
simdovfl_armv8 = ('b', 'B', 'h', 'H', 'i', 'I')


# This is the width of the SIMD registers in number of bits.
simdwidth_armv8 = 128

# SIMD mask initialisation data.
simdovintmaxvals_armv8 = {
	'b' : ', '.join(['SCHAR_MIN'] * (simdwidth_armv8 // 8)), 
	'B' : ', '.join(['UCHAR_MAX'] * (simdwidth_armv8 // 8)), 
	'h' : ', '.join(['SHRT_MIN'] * (simdwidth_armv8 // 16)), 
	'H' : ', '.join(['USHRT_MAX'] * (simdwidth_armv8 // 16)), 
	'i' : ', '.join(['INT_MIN'] * (simdwidth_armv8 // 32)), 
	'I' : ', '.join(['UINT_MAX'] * (simdwidth_armv8 // 32)), 
}


# A list of which array types are supported by ARM SIMD instructions.
armv8_simdtypes = tuple(simdop_armv8.keys())

# Multiplication, used for checking for math errors.
simdmulop_armv8 = 'vmulq_f32'

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
	elif (not hasx86) and hasarmv7 and hasarmv8:
		return SIMD_platform_ARM
	elif (not hasx86) and (not hasarmv7) and hasarmv8:
		return SIMD_platform_ARM64v8
	else:
		print('Error: Template error in findsimdplatform: %s %s' % (arraycode, funcname))
		return 'Error: Template error, this should not be here.'

# ==============================================================================



# ==============================================================================


# Create the source code based on templates.
funcname = 'add'
filename = funcname + '.c'
pyoperator = '+'
copname = '+'

c_operator_i = '+'
c_operator_f = '+'
c_operator_d = '+'


# This code generator script does not use data read from the spreadsheet.
arraytypesdocs = 'si,ui,f'
opcodedocs = 'x + y'
matherrorsdocs = 'OverflowError,ArithmeticError'

# These are the templates for each type specific operation. 
float_template = ops_op_float
uint_template = ops_add_uint
int_template = ops_add_int


includeoptions = includeoptions_both

macrofilename = funcname + '_defs' + '.h'

# The text to include the function specific macros.
funcdefsblock = '''
// Function specific macros and other definitions.
#include "%s"
''' % macrofilename

# ==============================================================================


# This outputs the main C file.


def CreateHeader(funcname):
	''' The header and related code. This is returned as two blocks of text.
	'''
	funcdata = {'funclabel' : funcname, 
				'includeoptions' : includeoptions_both % {'funclabel' : funcname},
				}


	headtext = mathops_head % funcdata

	# Function specific includes.
	includextext = funcdefsblock

	return headtext, includextext



def CreateArrayDataCCode(arraycode, funcname):
	''' Conventional C code for a single data type.
	This returns the data to be written later.
	It returns two blocks of text, the C code and the call code.
	'''
	arraytype = codegen_common.arraytypes[arraycode]
	funcmodifier = arraytype.replace(' ', '_')

	funcdata = {'funcmodifier' : funcmodifier,
			'funclabel' : funcname,
			'arraytype' : arraytype,
			'arraycode' : arraycode,
			'copname' : copname,
			'intmaxvalue' : codegen_common.maxvalue[arraycode],
			'intminvalue' : codegen_common.minvalue[arraycode],
		}


	if arraycode in codegen_common.floatarrays:
		ops_calc = float_template
	elif arraycode in codegen_common.unsignedint:
		 ops_calc = uint_template
	elif arraycode in codegen_common.signedint:
		 ops_calc = int_template
	else:
		print('Error - Unsupported array code.', arraycode)


	# Prepare the SIMD templates.
	if arraycode in (set(x86_simdtypes) | set(armv7_simdtypes) | set(armv8_simdtypes)):
		simdfuncdata = {'simdwidth' : simdwidth[arraycode], 
			'funclabel' : funcname,
			'funcmodifier' : funcmodifier,
			'simdplatform' : findsimdplatform(arraycode, funcname)}
		# SIMD without overflow detection.
		funcdata.update(dict([(x, y % simdfuncdata) for x,y in SIMD_call.items()]))
		# Integer SIMD with overflow detection data.
		funcdata.update(dict([(x, y % simdfuncdata) for x,y in SIMD_call_ovfl.items()]))
		funcdata['nosimddecl'] = nosimddecl
		funcdata['nosimdparam'] = nosimdparam
		funcdata['simdwidth'] = simdwidth.get(arraycode, '')
		funcdata['simdplatform'] = findsimdplatform(arraycode, funcname)
	else:
		# SIMD without overflow detection.
		funcdata.update(dict([(x, '') for x,y in SIMD_call.items()]))
		# Integer SIMD with overflow detection data.
		funcdata.update(dict([(x, '') for x,y in SIMD_call_ovfl.items()]))
		funcdata['nosimddecl'] = ''
		funcdata['nosimdparam'] = ''


	# The calculations.
	opscalctext = ops_calc % funcdata

	# This is the call to the functions for this array type. This
	# is inserted into another template below.
	funcdata['arraycode'] = arraycode
	opscalltext = opscall % funcdata

	return opscalctext, opscalltext



with open(filename, 'w') as f:

	headtext, includextext = CreateHeader(funcname)
	f.write(headtext)
	f.write(includextext)

	opscalcdatatext = []
	opscalldatatext = []


	# Check each array type.
	for arraycode in codegen_common.arraycodes:
		opscalctext, opscalltext = CreateArrayDataCCode(arraycode, funcname)

		opscalcdatatext.append(opscalctext)
		opscalldatatext.append(opscalltext)

	f.write(''.join(opscalcdatatext))


	# Write the remaining boilerplate C code. 
	helpsimd1 = helpsimd1_template % {'funclabel' : funcname}
	helpsimd2 = helpsimd2_template
	getsimdparam = '1'


	supportedarrays = codegen_common.FormatDocsArrayTypes(arraytypesdocs)

	f.write(mathops_params % {'funclabel' : funcname, 
			'opcodedocs' : opcodedocs, 
			'supportedarrays' : supportedarrays,
			'pyoperator' : pyoperator,
			'matherrors' : ', '.join(matherrorsdocs.split(',')),
			'opscall' : ''.join(opscalldatatext),
			'getsimdparam' : getsimdparam,
			'helpsimd1' : helpsimd1,
			'helpsimd2' : helpsimd2})



# ==============================================================================

# ==============================================================================

# This outputs helper macros.
macrocodedate = '08-Aug-2021'

outputlist = []

# Macro definitions.
# Not array type specific. 
outputlist.append(int_ovcheck)

# Array type specific macros.
for arraycode in codegen_common.intarrays:

	arraytype = codegen_common.arraytypes[arraycode]
	funcdata = {'arraytype' : arraytype,
				'funcmodifier' : arraytype.replace(' ', '_'),
				'intmaxvalue' : codegen_common.maxvalue[arraycode],
				'intminvalue' : codegen_common.minvalue[arraycode],
				}

	if arraycode in codegen_common.signedint:
		outputlist.append(intov_macros_signed % funcdata)
	elif arraycode in codegen_common.unsignedint:
		outputlist.append(intov_macros_unsigned % funcdata)



# Write out the file.
codegen_common.OutputCHeader(macrofilename, 
	outputlist, 
	'Additional macros for %s' % funcname, 
	'', 
	macrocodedate)


# ==============================================================================


# Write the SIMD code.

# x86
def SetSIMDData_x86(funcname):
	'''Set the SIMD template data for x86. This is for SIMD without
	overflow checking.
	'''
	outputlist = []


	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname


	# Function specific includes.
	outputlist.append(funcdefsblock)

	# Output the generated code.
	for arraycode in x86_simdtypes:

		arraytype = codegen_common.arraytypes[arraycode]

		# The main template values.
		funcdata = {'funclabel' : funcname,
					'copname' : copname,
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'arraycode' : arraycode,
					'arraytype' : codegen_common.arraytypes[arraycode],
					'simdplatform' : SIMD_platform_x86,

					'simdwidth' : simdwidth[arraycode],
					'simdattr' : simdattr_x86[arraycode],
					'ovflsimdattr' : ovflsimdattr_x86[arraycode],
					'vldinstr' : vldinstr_x86[arraycode],
					'vstinstr1' : vstinstr1_x86[arraycode],
					'vstinstr2' : vstinstr2_x86[arraycode],
					'vopinstr' : simdop_x86[arraycode],
					'vgtinstr' : vgtinstr_x86[arraycode],
					'vltinstr' : vgtinstr_x86[arraycode],
					'simd_ovflchk_extravars' : '',
					'intmaxvalue' : codegen_common.maxvalue[arraycode],
					'intminvalue' : codegen_common.minvalue[arraycode],
					}


		# Helper functions.
		outputlist.append(simd_helpers % funcdata)
		

		# No overflow checking, fill in the template.
		outputlist.append(ops_simdsupport % funcdata)

		# Overflow check. For integer arrays only.
		if arraycode in codegen_common.intarrays:
			ovf_check1 = simd_ovflchk1_x86 % funcdata
			# Add this back into the template values.
			funcdata['ovf_check1'] = ovf_check1

			ovf_check2 = simd_ovflchk2_x86 % funcdata
			# Add this back into the template values.
			funcdata['ovf_check2'] = ovf_check2

			# Overflow mask initialisation.
			funcdata['simdovintmaxvals'] = simdovintmaxvals_x86[arraycode]

			# With overflow checking, fill in the template.
			outputlist.append(ops_simdsupport_ovfl_signed % funcdata)

		# For float arrays.
		elif arraycode in codegen_common.floatarrays:
			funcdata['simdmul'] = simdmulop_x86[arraycode]
			# With overflow checking, fill in the template.
			outputlist.append(ops_simdsupport_ovfl_float % funcdata)


	return outputlist



# ARMv7
def SetSIMDData_ARMv7(funcname):
	'''Set the SIMD template data for ARMv7. This is for SIMD without
	overflow checking.
	'''
	outputlist = []


	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname


	# Function specific includes.
	outputlist.append(funcdefsblock)

	# Output the generated code.
	for arraycode in armv7_simdtypes:


		arraytype = codegen_common.arraytypes[arraycode]

		# The main template values.
		funcdata = {'funclabel' : funcname,
					'copname' : copname,
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'arraycode' : arraycode,
					'arraytype' : codegen_common.arraytypes[arraycode],
					'simdplatform' : SIMD_platform_ARMv7,

					'simdwidth' : simdwidth[arraycode],
					'simdattr' : simdattr_armv7[arraycode],
					'ovflsimdattr' : ovflsimdattr_armv7[arraycode],
					'vldinstr' : vldinstr_armv7[arraycode],
					'vstinstr1' : vstinstr1_armv7[arraycode],
					'vstinstr2' : vstinstr2_armv7[arraycode],
					'vopinstr' : simdop_armv7[arraycode],
					'vgtinstr' : vgtinstr_armv7[arraycode],
					'vltinstr' : vltinstr_armv7[arraycode],
					'vsubinstr' : vsubinstr_armv7[arraycode],
					'vreinterpinstr' : vreinterpinstr_armv7[arraycode],
					'armvecsize' : armvecsize_armv7.get(arraycode, ''),
					'simd_ovflchk_extravars' : '',
					'intmaxvalue' : codegen_common.maxvalue[arraycode],
					'intminvalue' : codegen_common.minvalue[arraycode],
					}


		# Helper functions.
		outputlist.append(simd_helpers % funcdata)

		# No overflow checking, fill in the template.
		outputlist.append(ops_simdsupport % funcdata)

		# Overflow check. For some array types only.
		if arraycode in simdovfl_armv7:
			ovf_check1 = simd_ovflchk1_armv7 % funcdata
			# Add this back into the template values.
			funcdata['ovf_check1'] = ovf_check1

			ovf_check2 = simd_ovflchk2_armv7 % funcdata
			# Add this back into the template values.
			funcdata['ovf_check2'] = ovf_check2

			# Overflow mask initialisation.
			funcdata['simdovintmaxvals'] = simdovintmaxvals_armv7[arraycode]

			# With overflow checking, fill in the template.
			# For signed intergers.
			if arraycode in codegen_common.signedint:
				outputlist.append(ops_simdsupport_ovfl_signed % funcdata)

			# For unsigned integers.
			elif arraycode in codegen_common.unsignedint:
				outputlist.append(ops_simdsupport_ovfl_unsigned % funcdata)


		# For float arrays.
		elif arraycode == 'f':
			funcdata['simdmul'] = simdmulop_armv7
			# With overflow checking, fill in the template.
			outputlist.append(ops_simdsupport_ovfl_float % funcdata)
		

	return outputlist




# ARMv8
def SetSIMDData_ARMv8(funcname):
	'''Set the SIMD template data for ARMv8. This is for SIMD without
	overflow checking.
	'''
	outputlist = []


	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname


	# Function specific includes.
	outputlist.append(funcdefsblock)

	# Output the generated code.
	for arraycode in armv8_simdtypes:


		arraytype = codegen_common.arraytypes[arraycode]

		# The main template values.
		funcdata = {'funclabel' : funcname,
					'copname' : copname,
					'arraytype' : arraytype, 
					'funcmodifier' : arraytype.replace(' ', '_'),
					'arraycode' : arraycode,
					'arraytype' : codegen_common.arraytypes[arraycode],
					'simdplatform' : SIMD_platform_ARM64v8,

					'simdwidth' : simdwidth[arraycode],
					'simdattr' : simdattr_armv8[arraycode],
					'ovflsimdattr' : ovflsimdattr_armv8[arraycode],
					'vldinstr' : vldinstr_armv8[arraycode],
					'vstinstr1' : vstinstr1_armv8[arraycode],
					'vstinstr2' : vstinstr2_armv8[arraycode],
					'vopinstr' : simdop_armv8[arraycode],
					'vgtinstr' : vgtinstr_armv8[arraycode],
					'vltinstr' : vltinstr_armv8[arraycode],
					'vsubinstr' : vsubinstr_armv8[arraycode],
					'vreinterpinstr' : vreinterpinstr_armv8[arraycode],
					'armvecsize' : armvecsize_armv8.get(arraycode, ''),
					'simd_ovflchk_extravars' : simd_ovflchk_extravars_armv8,
					'intmaxvalue' : codegen_common.maxvalue[arraycode],
					'intminvalue' : codegen_common.minvalue[arraycode],
					}


		# Helper functions.
		outputlist.append(simd_helpers % funcdata)

		# No overflow checking, fill in the template.
		outputlist.append(ops_simdsupport % funcdata)

		# Overflow check. For some array types only.
		if arraycode in simdovfl_armv8:
			ovf_check1 = simd_ovflchk1_armv8 % funcdata
			# Add this back into the template values.
			funcdata['ovf_check1'] = ovf_check1

			ovf_check2 = simd_ovflchk2_armv8 % funcdata
			# Add this back into the template values.
			funcdata['ovf_check2'] = ovf_check2

			# Overflow mask initialisation.
			funcdata['simdovintmaxvals'] = simdovintmaxvals_armv8[arraycode]

			# With overflow checking, fill in the template.
			# For signed intergers.
			if arraycode in codegen_common.signedint:
				outputlist.append(ops_simdsupport_ovfl_signed % funcdata)

			# For unsigned integers.
			elif arraycode in codegen_common.unsignedint:
				outputlist.append(ops_simdsupport_ovfl_unsigned % funcdata)

		# For float arrays.
		elif arraycode == 'f':
			funcdata['simdmul'] = simdmulop_armv8
			# With overflow checking, fill in the template.
			outputlist.append(ops_simdsupport_ovfl_float % funcdata)


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

# Function specific includes.
includextext = funcdefsblock

# x86.
simdcodedate = '1-Apr-2019'
simdfilename = '_simd_x86'
outputlist = SetSIMDData_x86(funcname)
WriteSIMDCode(funcname, 'x86', simdfilename, simdcodedate, includextext, outputlist)

simdcodedate = '8-Oct-2019'
simdfilename = '_simd_armv7'
outputlist = SetSIMDData_ARMv7(funcname)
WriteSIMDCode(funcname, 'armv7', simdfilename, simdcodedate, includextext, outputlist)

simdcodedate = '26-Mar-2020'
simdfilename = '_simd_armv8'
outputlist = SetSIMDData_ARMv8(funcname)
WriteSIMDCode(funcname, 'armv8', simdfilename, simdcodedate, includextext, outputlist)


# ==============================================================================
