#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for math operations. 
# Language: Python 3.4
# Date:     30-Dec-2017
#
###############################################################################
#
#   Copyright 2014 - 2018    Michael Griffin    <m12.griffin@gmail.com>
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

# This is to be included only for those functions which use SIMD.
simdinclude = """

#include "simddefs.h"

#ifdef AF_HASSIMD
#include "%(funclabel)s_simd_x86.h"
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
	for(x = 0; x < arraylen; x++) {
		data1[x] = data1[x] %(copname)s param;
	}


}

// param_arr_num_arr
void %(funclabel)s_%(funcmodifier)s_2(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data1, %(arraytype)s param, %(arraytype)s *data3) {

	// array index counter.
	Py_ssize_t x;
%(simd_call_2)s
	for(x = 0; x < arraylen; x++) {
		data3[x] = data1[x] %(copname)s param;
	}

}

// param_num_arr_none
void %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, int nosimd, %(arraytype)s param, %(arraytype)s *data2) {

	// array index counter.
	Py_ssize_t x;
%(simd_call_3)s
	for(x = 0; x < arraylen; x++) {
		data2[x] = param %(copname)s data2[x];
	}

}

// param_num_arr_arr
void %(funclabel)s_%(funcmodifier)s_4(Py_ssize_t arraylen, int nosimd, %(arraytype)s param, %(arraytype)s *data2, %(arraytype)s *data3) {

	// array index counter.
	Py_ssize_t x;
%(simd_call_4)s
	for(x = 0; x < arraylen; x++) {
		data3[x] = param %(copname)s data2[x];
	}

}



// param_arr_arr_none
void %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data1, %(arraytype)s *data2) {

	// array index counter.
	Py_ssize_t x;
%(simd_call_5)s
	for(x = 0; x < arraylen; x++) {
		data1[x] = data1[x] %(copname)s data2[x];
	}

}

// param_arr_arr_arr
void %(funclabel)s_%(funcmodifier)s_6(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data1, %(arraytype)s *data2, %(arraytype)s *data3) {

	// array index counter.
	Py_ssize_t x;
%(simd_call_6)s
	for(x = 0; x < arraylen; x++) {
		data3[x] = data1[x] %(copname)s data2[x];
	}

}
"""


# ==============================================================================


# ==============================================================================

# The actual compare operations using SIMD operations.
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
#ifdef AF_HASSIMD
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
	for(index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = (%(simdattr)s) __builtin_ia32_lddqu((char *) &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft %(copname)s datasliceright;
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[index], %(simdstorecast)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] %(copname)s param;
	}

}
#endif


// param_arr_num_arr
#ifdef AF_HASSIMD
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
	for(index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = (%(simdattr)s) __builtin_ia32_lddqu((char *) &data1[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft %(copname)s datasliceright;
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[index], %(simdstorecast)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] %(copname)s param;
	}

}
#endif


// param_num_arr_none
#ifdef AF_HASSIMD
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
	for(index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceright = (%(simdattr)s) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceright = datasliceleft %(copname)s datasliceright;
		// Store the result.
		__builtin_ia32_storedqu((char *) &data2[index], %(simdstorecast)s datasliceright);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data2[index] = param %(copname)s data2[index];
	}

}
#endif


// param_num_arr_arr
#ifdef AF_HASSIMD
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
	for(index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceright = (%(simdattr)s) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceright = datasliceleft %(copname)s datasliceright;
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[index], %(simdstorecast)s datasliceright);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = param %(copname)s data2[index];
	}

}
#endif


// param_arr_arr_none
#ifdef AF_HASSIMD
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
	for(index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = (%(simdattr)s) __builtin_ia32_lddqu((char *) &data1[index]);
		datasliceright = (%(simdattr)s) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft %(copname)s datasliceright;
		// Store the result.
		__builtin_ia32_storedqu((char *) &data1[index], %(simdstorecast)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data1[index] = data1[index] %(copname)s data2[index];
	}

}
#endif


// param_arr_arr_arr
#ifdef AF_HASSIMD
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
	for(index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = (%(simdattr)s) __builtin_ia32_lddqu((char *) &data1[index]);
		datasliceright = (%(simdattr)s) __builtin_ia32_lddqu((char *) &data2[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = datasliceleft %(copname)s datasliceright;
		// Store the result.
		__builtin_ia32_storedqu((char *) &data3[index], %(simdstorecast)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data3[index] = data1[index] %(copname)s data2[index];
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
%(helpsimd1)s\\n\\
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
SIMD_call_1 = '''\n#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		%(funclabel)s_%(funcmodifier)s_1_simd(arraylen, data1, param);
		return;
	}
#endif\n'''


# SIMD call, version 2.
SIMD_call_2 = '''\n#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		%(funclabel)s_%(funcmodifier)s_2_simd(arraylen, data1, param, data3);
		return;
	}
#endif\n'''


# SIMD call, version 3.
SIMD_call_3 = '''\n#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		%(funclabel)s_%(funcmodifier)s_3_simd(arraylen, param, data2);
		return;
	}
#endif\n'''


# SIMD call, version 4.
SIMD_call_4 = '''\n#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		%(funclabel)s_%(funcmodifier)s_4_simd(arraylen, param, data2, data3);
		return;
	}
#endif\n'''


# SIMD call, version 5.
SIMD_call_5 = '''\n#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		%(funclabel)s_%(funcmodifier)s_5_simd(arraylen, data1, data2);
		return;
	}
#endif\n'''


# SIMD call, version 6.
SIMD_call_6 = '''\n#ifdef AF_HASSIMD
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



# ==============================================================================

# ==============================================================================

# Various SIMD instruction information which varies according to array type.
simdvalues = {
'b' : {'hassimd' : True, 'simdattr' : 'v16qi', 'simdwidth' : 'CHARSIMDSIZE', 'simdstorecast' : ''},
'B' : {'hassimd' : True, 'simdattr' : 'v16qi', 'simdwidth' : 'CHARSIMDSIZE', 'simdstorecast' : ''},
'h' : {'hassimd' : True, 'simdattr' : 'v8hi', 'simdwidth' : 'SHORTSIMDSIZE', 'simdstorecast' : '(v16qi)'},
'H' : {'hassimd' : True, 'simdattr' : 'v8hi', 'simdwidth' : 'SHORTSIMDSIZE', 'simdstorecast' : '(v16qi)'},
'i' : {'hassimd' : True, 'simdattr' : 'v4si', 'simdwidth' : 'INTSIMDSIZE', 'simdstorecast' : '(v16qi)'},
'I' : {'hassimd' : True, 'simdattr' : 'v4si', 'simdwidth' : 'INTSIMDSIZE', 'simdstorecast' : '(v16qi)'},
'l' : {'hassimd' : False},
'L' : {'hassimd' : False},
'q' : {'hassimd' : False},
'Q' : {'hassimd' : False},
'f' : {'hassimd' : False},
'd' : {'hassimd' : False},
}

# This is a list of which of the functions implements SIMD.
HasSIMD = ('and_', 'or_', 'xor')


# The following are used to fill in template data which handles whether
# a function requires SIMD related template data or not. 
funcwithsimd = {'hasnosimd' : ', 1',
		'helpsimd1' : '  %(funclabel)s(array1, param, nosimd=False) \\n\\', 
		'helpsimd2' : '''* nosimd - If True, SIMD acceleration is disabled. This parameter is \\n\\
  optional. The default is FALSE.  \\n\\\n'''
		}

funcwithoutsimd= {'hasnosimd' : ', 0',
		'helpsimd1' : '', 
		'helpsimd2' : ''
		}



# ==============================================================================


# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.

funclist = [x for x in oplist if x['c_code_template'] in ('template_binop', 'template_binop2')]

# Not all functions support SIMD. This is the sublist of those that do.
simdlist = [x for x in funclist if x['funcname'] in HasSIMD]

# ==============================================================================

for func in funclist:

	# The name of the arrayfunc function.
	funcname = func['funcname']

	# Create the source code based on templates.
	filename = funcname + '.c'
	with open(filename, 'w') as f:
		funcdata = {'funclabel' : funcname}
		f.write(mathops_head % {'funclabel' : funcname})

		# This includes the SIMD data only for those functions which support SIMD.
		if funcname in HasSIMD:
			f.write(simdinclude % {'funclabel' : funcname})

		opscalltext = []


		# Check each array type.
		for arraycode in codegen_common.intarrays:
			funcdata['funcmodifier'] = codegen_common.arraytypes[arraycode].replace(' ', '_')
			funcdata['arraytype'] = codegen_common.arraytypes[arraycode]
			funcdata['copname'] = func['c_operator_i']

			# Insert the correct SIMD call template in functions which have SIMD versions.
			if (funcname in HasSIMD) and simdvalues[arraycode]['hassimd']:
				simd_call_vals = {'simdwidth' : simdvalues[arraycode]['simdwidth'], 
							'funclabel' : funcdata['funclabel'], 
							'funcmodifier' : funcdata['funcmodifier']}

				# This updates the SIMD call templates with the values for this array type.
				funcdata.update(dict([(x,y % simd_call_vals) for x,y in SIMD_call_hassimd.items()]))
			else:
				funcdata.update(SIMD_call_nosimd)

			f.write(ops_binop % funcdata)

			# This is the call to the functions for this array type. This
			# is inserted into another template below.
			funcdata['arraycode'] = arraycode
			opscalltext.append(binopscall % funcdata)

		supportedarrays = codegen_common.FormatDocsArrayTypes(func['arraytypes'])

		if funcname in HasSIMD:
			paramsimd = funcwithsimd
			helpsimd1 = paramsimd['helpsimd1'] % {'funclabel' : funcname}
		else:
			paramsimd = funcwithoutsimd
			helpsimd1 = paramsimd['helpsimd1']

		paramsdata = {'funclabel' : funcname, 
				'opcodedocs' : func['opcodedocs'], 
				'supportedarrays' : supportedarrays,
				'matherrors' : ', '.join(func['matherrors'].split(',')),
				'opscall' : ''.join(opscalltext),
				'hasnosimd' : paramsimd['hasnosimd'],
				'helpsimd1' : helpsimd1,
				'helpsimd2' : paramsimd['helpsimd2'],
				}
		f.write(binops_params % paramsdata)


# ==============================================================================


# ==============================================================================

# The original date of the SIMD C code.
simdcodedate = '12-Mar-2019'
simdfilename = '_simd_x86'

# This outputs the SIMD version.

for func in simdlist:

	outputlist = []

	funcname = func['funcname']

	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname


	# Output the generated code.
	for arraycode in codegen_common.arraycodes:

		if simdvalues[arraycode]['hassimd']:
			arraytype = codegen_common.arraytypes[arraycode]

			# The compare_ops symbols is the same for integer and floating point.
			datavals = {'funclabel' : funcname,
						'arraytype' : arraytype, 
						'funcmodifier' : arraytype.replace(' ', '_'),
						'simdattr' : simdvalues[arraycode]['simdattr'],
						'simdwidth' : simdvalues[arraycode]['simdwidth'],
						'simdstorecast' : simdvalues[arraycode]['simdstorecast'],
						'copname' :  func['c_operator_i'],
						}


			# Start of function definition.
			outputlist.append(ops_simdsupport % datavals)



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


