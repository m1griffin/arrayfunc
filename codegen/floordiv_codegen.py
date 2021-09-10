#!/usr/bin/python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for math floordiv operations. 
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


# Create the source code based on templates.
funcname = 'floordiv'
filename = funcname + '.c'
pyoperator = '//'
copname = '/'

c_operator_i = '/'
c_operator_f = 'floorf'
c_operator_d = 'floor'


# This code generator script does not use data read from the spreadsheet.
arraytypesdocs = 'si,ui,f'
opcodedocs = 'x / y'
matherrorsdocs = 'OverflowError,ArithmeticError,ZeroDivisionError'

# These are the templates for each type specific operation. 
float_template = ops_floordiv_float
uint_template = ops_floordiv_uint
int_template = ops_floordiv_int

# ==============================================================================

with open(filename, 'w') as f:

	funcdata = {'funclabel' : funcname, 
				'includeoptions' : '',
				'copname' : copname,
				'nosimddecl' : '',
				'nosimdparam' : '',
				}
		
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


		if arraycode == 'd':
			ops_calc = float_template
			funcdata['copname'] = c_operator_d
		elif arraycode == 'f':
			ops_calc = float_template
			funcdata['copname'] = c_operator_f
		elif arraycode in codegen_common.unsignedint:
			ops_calc = uint_template
			funcdata['copname'] = c_operator_i
		elif arraycode in codegen_common.signedint:
			ops_calc = int_template
			funcdata['copname'] = c_operator_i
		else:
			print('Error - Unsupported array code.', arraycode)



		f.write(ops_calc % funcdata)

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
