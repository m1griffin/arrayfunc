#!/usr/bin/python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for math pow operations. 
#			parameter.
# Language: Python 3.8
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



# ==============================================================================

# For signed integer.
ops_pow_int_signed = """

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

	// Next we need to deal with a series of special cases.

	// Special case for raise to the power of zero.
	if (y == 0) { return 1; }

	// We need this special case to avoid dividing by zero.
	if (x == 0) { return 0; }

	// This special case handles limitations of the algorithm with
	// the minimum integer. 
	if ((x == %(intminvalue)s) && (y == 1)) { return %(intminvalue)s; }

	// Special case for base of 1. This helps in instances with 
	// very large powers where otherwise the algorithm will grind
	// away for a long time before returning.
	if (x == 1) { return 1; }

	// Same as above, but for -1. We have to account for odd and even powers.
	if (x == -1) {
		// Odd if there is a remainder.
		if (y %% 2) { 
			return -1; 
		} else {
			return 1;
		}
	}

%(powoverflowspecialcase)s
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

	// Negative powers are not allowed.
	if (param < 0) { return ARR_ERR_VALUE_ERR; }

	if (!ignoreerrors) {
		switch (param) {
			// Anything to the power of 0 is one.
			case 0 : { 
				for (x = 0; x < arraylen; x++) {
					data1[x] = 1;
				}
				break;
			}

			// Special optimized version for powers of 1.
			case 1 : { 
				// Since this effectively changes nothing, we can do nothing.
				break;
			}

			// Special optimized version for powers of 2.
			case 2 : { 
				for (x = 0; x < arraylen; x++) {
					if ((data1[x] > %(pow2max)s) || (data1[x] < %(pow2min)s)) { return ARR_ERR_OVFL; }
					data1[x] = data1[x] * data1[x];
				}
				break;
			}

			// Special optimized version for powers of 3.
			case 3 : { 
				for (x = 0; x < arraylen; x++) {
					if ((data1[x] > %(pow3max)s) || (data1[x] < %(pow3min)s)) { return ARR_ERR_OVFL; }
					data1[x] = data1[x] * data1[x] * data1[x];
				}
				break;
			}

			// General algorithm which covers all other powers.
			default : {
				// Math error checking enabled.
				for (x = 0; x < arraylen; x++) {
					data1[x] = arith_pow_%(funcmodifier)s(data1[x], param, &errflag);
					if (errflag != 0) { return ARR_ERR_OVFL; }
				}
				break;
			}
		}

	} else {
		// Ignore errors. We only do this with the non-optimised version. 
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_%(funcmodifier)s(data1[x], param, &errflag);
		}
	}

	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;

	// Negative powers are not allowed.
	if (param < 0) { return ARR_ERR_VALUE_ERR; }

	if (!ignoreerrors) {
		switch (param) {
			// Anything to the power of 0 is one.
			case 0 : { 
				for (x = 0; x < arraylen; x++) {
					data3[x] = 1;
				}
				break;
			}

			// Special optimized version for powers of 1.
			case 1 : { 
				for (x = 0; x < arraylen; x++) {
					data3[x] = data1[x];
				}
				break;
			}

			// Special optimized version for powers of 2.
			case 2 : { 
				for (x = 0; x < arraylen; x++) {
					if ((data1[x] > %(pow2max)s) || (data1[x] < %(pow2min)s)) { return ARR_ERR_OVFL; }
					data3[x] = data1[x] * data1[x];
				}
				break;
			}

			// Special optimized version for powers of 3.
			case 3 : { 
				for (x = 0; x < arraylen; x++) {
					if ((data1[x] > %(pow3max)s) || (data1[x] < %(pow3min)s)) { return ARR_ERR_OVFL; }
					data3[x] = data1[x] * data1[x] * data1[x];
				}
				break;
			}

			// General algorithm which covers all other powers.
			default : {
				for (x = 0; x < arraylen; x++) {
					data3[x] = arith_pow_%(funcmodifier)s(data1[x], param, &errflag);
					if (errflag != 0) { return ARR_ERR_OVFL; }
				}
				break;
			}
		}

	} else {
		// Ignore errors. We only do this with the non-optimised version. 
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_%(funcmodifier)s(data1[x], param, &errflag);
		}
	}

	return ARR_NO_ERR;

}

"""


# For unsigned integer.
ops_pow_int_unsigned = """

/*--------------------------------------------------------------------------- */
// Return x raised to the power of y.
%(arraytype)s arith_pow_%(funcmodifier)s(%(arraytype)s x, %(arraytype)s y, char *errflag) {
	%(arraytype)s i, z, ovtmp1;
	z = 1;
	*errflag = 0;

	// Special case for raise to the power of zero.
	if (y == 0) { return 1; }

	// We need this special case to avoid dividing by zero.
	if (x == 0) {return 0;}

	// Special case for base of 1. This helps in instances with 
	// very large powers where otherwise the algorithm will grind
	// away for a long time before returning.
	if (x == 1) { return 1; }

	ovtmp1 = %(intmaxvalue)s / x;
	for (i = 0; i < y; i++) {
		if (z > ovtmp1) {*errflag = ARR_ERR_OVFL; return z;}
		z = z * x;
	}
	return z;
}



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


	if (!ignoreerrors) {
		switch (param) {
			// Anything to the power of 0 is one.
			case 0 : { 
				for (x = 0; x < arraylen; x++) {
					data1[x] = 1;
				}
				break;
			}

			// Special optimized version for powers of 1.
			case 1 : { 
				// Since this effectively changes nothing, we can do nothing.
				break;
			}

			// Special optimized version for powers of 2.
			case 2 : { 
				for (x = 0; x < arraylen; x++) {
					if (data1[x] > %(pow2max)s) { return ARR_ERR_OVFL; }
					data1[x] = data1[x] * data1[x];
				}
				break;
			}

			// Special optimized version for powers of 3.
			case 3 : { 
				for (x = 0; x < arraylen; x++) {
					if (data1[x] > %(pow3max)s) { return ARR_ERR_OVFL; }
					data1[x] = data1[x] * data1[x] * data1[x];
				}
				break;
			}

			// General algorithm which covers all other powers.
			default : {
				// Math error checking enabled.
				for (x = 0; x < arraylen; x++) {
					data1[x] = arith_pow_%(funcmodifier)s(data1[x], param, &errflag);
					if (errflag != 0) { return ARR_ERR_OVFL; }
				}
				break;
			}
		}

	} else {
		// Ignore errors. We only do this with the non-optimised version. 
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_%(funcmodifier)s(data1[x], param, &errflag);
		}
	}

	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;

	// Negative powers are not allowed.
	if (param < 0) { return ARR_ERR_VALUE_ERR; }

	if (!ignoreerrors) {
		switch (param) {
			// Anything to the power of 0 is one.
			case 0 : { 
				for (x = 0; x < arraylen; x++) {
					data3[x] = 1;
				}
				break;
			}

			// Special optimized version for powers of 1.
			case 1 : { 
				for (x = 0; x < arraylen; x++) {
					data3[x] = data1[x];
				}
				break;
			}

			// Special optimized version for powers of 2.
			case 2 : { 
				for (x = 0; x < arraylen; x++) {
					if (data1[x] > %(pow2max)s) { return ARR_ERR_OVFL; }
					data3[x] = data1[x] * data1[x];
				}
				break;
			}

			// Special optimized version for powers of 3.
			case 3 : { 
				for (x = 0; x < arraylen; x++) {
					if (data1[x] > %(pow3max)s) { return ARR_ERR_OVFL; }
					data3[x] = data1[x] * data1[x] * data1[x];
				}
				break;
			}

			// General algorithm which covers all other powers.
			default : {
				for (x = 0; x < arraylen; x++) {
					data3[x] = arith_pow_%(funcmodifier)s(data1[x], param, &errflag);
					if (errflag != 0) { return ARR_ERR_OVFL; }
				}
				break;
			}
		}

	} else {
		// Ignore errors. We only do this with the non-optimised version. 
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_%(funcmodifier)s(data1[x], param, &errflag);
		}
	}

	return ARR_NO_ERR;

}


"""


# For signed and unsigned integer. This covers the configurations not 
# covered by the other templates. These do not have optimised versions.
ops_pow_int = """

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
	if (resultcode == ARR_ERR_ARITHMETIC) {
		ErrMsgArithCalc();
		return NULL;
	}

	if (resultcode == ARR_ERR_OVFL) {
		ErrMsgArithOverflowCalc();
		return NULL;
	}

	if (resultcode == ARR_ERR_VALUE_ERR) {
		ErrMsgParameterNotValidforthisOperation();
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

# With certain combinations of base and power and with certain word
# sizes we run into problems with the most negative integer not working
# with the algorithm. We handle this with special cases.

# array code b
specialcase_signed_char = '''

	// Special case to avoid integer overflow. 
	if ((x == -2) && (y == 7)) { return -128; }

'''

# array code h
specialcase_signed_short = '''

	// Special case to avoid integer overflow. 
	if ((x == -2) && (y == 15)) { return -32768; }
	if ((x == -8) && (y == 5)) { return -32768; }
	if ((x == -32) && (y == 3)) { return -32768; }

'''

# array code i
specialcase_signed_int = '''

	// Special case to avoid integer overflow. 
	if ((x == -2) && (y == 31)) { return -2147483648; }

'''

# array code l
# The size of this may depend upon the platform. 
# 
specialcase_signed_long = '''

	// signed long will vary in size on different platforms, being either
	// the same as signed int or the same as signed long long.
	// Assumption is LONG_MIN is either -2147483648 or -9223372036854775808
	// and LLONG_MIN == -9223372036854775808
	// We can't put these literals directly in the code below due to 
	// C compiler limitations.
#if LONG_MIN == LLONG_MIN
	// Special case to avoid integer overflow. 
	if ((x == -2) && (y == 63)) { return LLONG_MIN; }
	if ((x == -8) && (y == 21)) { return LLONG_MIN; }
	if ((x == -128) && (y == 9)) { return LLONG_MIN; }
	if ((x == -512) && (y == 7)) { return LLONG_MIN; }
	if ((x == -2097152) && (y == 3)) { return LLONG_MIN; }
#else
	// Special case to avoid integer overflow. 
	if ((x == -2) && (y == 31)) { return LONG_MIN; }

#endif

'''


# array code q
specialcase_signed_long_long = '''

	// Special case to avoid integer overflow. 
	// Assumption is LLONG_MIN == -9223372036854775808
	// We can't put these literals directly in the code below due to 
	// C compiler limitations.
	if ((x == -2) && (y == 63)) { return LLONG_MIN; }
	if ((x == -8) && (y == 21)) { return LLONG_MIN; }
	if ((x == -128) && (y == 9)) { return LLONG_MIN; }
	if ((x == -512) && (y == 7)) { return LLONG_MIN; }
	if ((x == -2097152) && (y == 3)) { return LLONG_MIN; }

'''

powoverflowspecialcase = {
	'b' : specialcase_signed_char,
	'h' : specialcase_signed_short,
	'i' : specialcase_signed_int,
	'l' : specialcase_signed_long,
	'q' : specialcase_signed_long_long,
}


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

# Limits to squares and cubes for overflow detection for each integer types.
# POW2MAX and POW2MIN refer to the maximum and mininum value which can be
# raised to the power of 2 without overflowing for that array type.
# POW3MAX and POW3MIN are the corresponding versions for raising to
# the power of 3.

pow_limits_definitions = '''
#define SCHAR_POW2MAX 11
#define SCHAR_POW2MIN -11 
#define UCHAR_POW2MAX 15

#define SSHORT_POW2MAX 181
#define SSHORT_POW2MIN -181 
#define USHORT_POW2MAX 255

#define SINT_POW2MAX 46340
#define SINT_POW2MIN -46340
#define UINT_POW2MAX 65535

// Account for 64 bit versus 32 bit word sizes.
#if LONG_MAX == LLONG_MAX

#define SLINT_POW2MAX 3037000499L
#define SLINT_POW2MIN -3037000499L
#define ULINT_POW2MAX 4294967295UL

#else

#define SLINT_POW2MAX 46340
#define SLINT_POW2MIN -46340
#define ULINT_POW2MAX 65535

#endif

#define SLLINT_POW2MAX 3037000499LL
#define SLLINT_POW2MIN -3037000499LL
#define ULLINT_POW2MAX 4294967295ULL


#define SCHAR_POW3MAX 5
#define SCHAR_POW3MIN -5 
#define UCHAR_POW3MAX 6

#define SSHORT_POW3MAX 31
#define SSHORT_POW3MIN -32 
#define USHORT_POW3MAX 40

#define SINT_POW3MAX 1290
#define SINT_POW3MIN -1290
#define UINT_POW3MAX 1625

// Account for 64 bit versus 32 bit word sizes.
#if LONG_MAX == LLONG_MAX

#define SLINT_POW3MAX 2097151
#define SLINT_POW3MIN -2097152
#define ULINT_POW3MAX 2642245

#else

#define SLINT_POW3MAX 1290
#define SLINT_POW3MIN -1290
#define ULINT_POW3MAX 1625

#endif

#define SLLINT_POW3MAX 2097151
#define SLLINT_POW3MIN -2097152
#define ULLINT_POW3MAX 2642245

'''

# Maximum and minimum limits for raising integers to powers of 2 or 3.
pow2_limits_max = {
	'b' : 'SCHAR_POW2MAX',
	'B' : 'UCHAR_POW2MAX',
	'h' : 'SSHORT_POW2MAX',
	'H' : 'USHORT_POW2MAX',
	'i' : 'SINT_POW2MAX',
	'I' : 'UINT_POW2MAX',
	'l' : 'SLINT_POW2MAX',
	'L' : 'ULINT_POW2MAX',
	'q' : 'SLLINT_POW2MAX',
	'Q' : 'ULLINT_POW2MAX',
	'f' : '',
	'd' : '',
}

pow2_limits_min = {
	'b' : 'SCHAR_POW2MIN',
	'B' : '0',
	'h' : 'SSHORT_POW2MIN',
	'H' : '0',
	'i' : 'SINT_POW2MIN',
	'I' : '0',
	'l' : 'SLINT_POW2MIN',
	'L' : '0',
	'q' : 'SLLINT_POW2MIN',
	'Q' : '0',
	'f' : '',
	'd' : '',
}

pow3_limits_max = {
	'b' : 'SCHAR_POW3MAX',
	'B' : 'UCHAR_POW3MAX',
	'h' : 'SSHORT_POW3MAX',
	'H' : 'USHORT_POW3MAX',
	'i' : 'SINT_POW3MAX',
	'I' : 'UINT_POW3MAX',
	'l' : 'SLINT_POW3MAX',
	'L' : 'ULINT_POW3MAX',
	'q' : 'SLLINT_POW3MAX',
	'Q' : 'ULLINT_POW3MAX',
	'f' : '',
	'd' : '',
}

pow3_limits_min = {
	'b' : 'SCHAR_POW3MIN',
	'B' : '0',
	'h' : 'SSHORT_POW3MIN',
	'H' : '0',
	'i' : 'SINT_POW3MIN',
	'I' : '0',
	'l' : 'SLINT_POW3MIN',
	'L' : '0',
	'q' : 'SLLINT_POW3MIN',
	'Q' : '0',
	'f' : '',
	'd' : '',
}

# ==============================================================================


# Create the source code based on templates.
funcname = 'pow'
filename = funcname + '.c'
pyoperator = '**'


# Select the correct function for floating point.
copnamefloat = {'f' : 'powf', 'd' : 'pow'}


# This code generator script does not use data read from the spreadsheet.
arraytypesdocs = 'si,ui,f'
opcodedocs = 'x**y or math.pow(x, y)'
matherrorsdocs = 'OverflowError,ArithmeticError,ValueError'

# These are the templates for each type specific operation. 
float_template = ops_pow_float
uint_template = ops_pow_int
int_template = ops_pow_int

# ==============================================================================

with open(filename, 'w') as f:

	funcdata = {'funclabel' : funcname, 
				'includeoptions' : '',
				'nosimddecl' : '',
				'nosimdparam' : '',
				}
		
	f.write(mathops_head % funcdata)
	opscalltext = []


	f.write(pow_limits_definitions)

	# Check each array type.
	for arraycode in codegen_common.arraycodes:
		arraytype = codegen_common.arraytypes[arraycode]
		funcmodifier = arraytype.replace(' ', '_')

		funcdata['funcmodifier'] = funcmodifier
		funcdata['arraytype'] = arraytype
		funcdata['intmaxvalue'] = codegen_common.maxvalue[arraycode]
		funcdata['intminvalue'] = codegen_common.minvalue[arraycode]

		# Integer overflow limits for raising to the power of 2 or 3.
		funcdata['pow2max'] = pow2_limits_max[arraycode]
		funcdata['pow2min'] = pow2_limits_min[arraycode]
		funcdata['pow3max'] = pow3_limits_max[arraycode]
		funcdata['pow3min'] = pow3_limits_min[arraycode]

		# Integer absolute value function depends on array type.
		funcdata['abs'] = absfunc[arraycode]

		# This handles special cases with signed integers.
		if arraycode in powoverflowspecialcase:
			funcdata['powoverflowspecialcase'] = powoverflowspecialcase[arraycode]


		# Handle integer arrays.
		if arraycode in codegen_common.intarrays:
			# First two equation forms for signed int.
			if arraycode in codegen_common.signedint:
				f.write(ops_pow_int_signed % funcdata)
			# First two equation forms for unsigned int.
			elif arraycode in codegen_common.unsignedint:
				f.write(ops_pow_int_unsigned % funcdata)
			else:
				print('Error - Unsupported array code.', arraycode)

			# Remaining equation forms for both signed and unsigned int.
			f.write(ops_pow_int % funcdata)

		# Handle float arrays.
		elif arraycode in codegen_common.floatarrays:
			funcdata['copname'] = copnamefloat[arraycode]
			f.write(float_template % funcdata)
		else:
			print('Error - Unsupported array code.', arraycode)


		# This is the call to the functions for this array type. This
		# is inserted into another template below.
		funcdata['arraycode'] = arraycode
		opscalltext.append(opscall % funcdata)


	helpsimd1 = ''
	helpsimd2 = ''
	getsimdparam = '0'


	supportedarrays = codegen_common.FormatDocsArrayTypes(arraytypesdocs)

	f.write(mathops_params % {'funclabel' : funcname, 
			'opcodedocs' : opcodedocs, 
			'supportedarrays' : supportedarrays,
			'pyoperator' : pyoperator,
			'matherrors' : ', '.join(matherrorsdocs.split(',')),
			'opscall' : ''.join(opscalltext),
			'getsimdparam' : getsimdparam,
			'helpsimd1' : helpsimd1,
			'helpsimd2' : helpsimd2})


# ==============================================================================
