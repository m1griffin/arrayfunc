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
//   Copyright 2014 - 2019    Michael Griffin    <m12.griffin@gmail.com>
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

#include "arrayparams_comp.h"

#include "simddefs.h"

#ifdef AF_HASSIMD
#include "%(funclabel)s_simd_x86.h"
#endif

/*--------------------------------------------------------------------------- */
"""

# ==============================================================================

# The actual compare operations.
ops_comp = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
char %(funclabel)s_%(funcmodifier)s_1(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data1, %(arraytype)s param) {

	// array index counter.
	Py_ssize_t x;
%(simd_call_1)s
	for(x = 0; x < arraylen; x++) {
		if (!(data1[x] %(copname)s param)) { return 0; }
	}

	return 1;

}


// param_num_arr
char %(funclabel)s_%(funcmodifier)s_3(Py_ssize_t arraylen, int nosimd, %(arraytype)s param, %(arraytype)s *data2) {

	// array index counter.
	Py_ssize_t x;
%(simd_call_3)s
	for(x = 0; x < arraylen; x++) {
		if (!(param %(copname)s data2[x])) { return 0; }
	}

	return 1;

}


// param_arr_arr
char %(funclabel)s_%(funcmodifier)s_5(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data1, %(arraytype)s *data2) {

	// array index counter.
	Py_ssize_t x;
%(simd_call_5)s
	for(x = 0; x < arraylen; x++) {
		if (!(data1[x] %(copname)s data2[x])) { return 0; }
	}

	return 1;

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
   param = The parameter to be applied to each array element.
*/
// param_arr_num
#ifdef AF_HASSIMD
char %(funclabel)s_%(funcmodifier)s_1_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s param) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright, resultslice;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param;
	}
	datasliceright = (%(simdattr)s) %(simdload)s(%(simdcast)scompvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += %(simdwidth)s) {
		datasliceleft = (%(simdattr)s) %(simdload)s(%(simdcast)s&data1[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft %(compare_ops)s datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] %(compare_ops)s param)) {
			return 0;
		}
	}

	return 1;

}


// param_num_arr
char %(funclabel)s_%(funcmodifier)s_3_simd(Py_ssize_t arraylen, %(arraytype)s param, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	%(simdattr)s datasliceleft, datasliceright, resultslice;
	%(arraytype)s compvals[%(simdwidth)s];

	// Initialise the comparison values.
	for (y = 0; y < %(simdwidth)s; y++) {
		compvals[y] = param;
	}
	datasliceleft = (%(simdattr)s) %(simdload)s(%(simdcast)scompvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += %(simdwidth)s) {
		datasliceright = (%(simdattr)s) %(simdload)s(%(simdcast)s&data2[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft %(compare_ops)s datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(param %(compare_ops)s data2[index])) {
			return 0;
		}
	}

	return 1;

}


// param_arr_arr
char %(funclabel)s_%(funcmodifier)s_5_simd(Py_ssize_t arraylen, %(arraytype)s *data1, %(arraytype)s *data2) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft, datasliceright, resultslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += %(simdwidth)s) {
		datasliceleft = (%(simdattr)s) %(simdload)s(%(simdcast)s&data1[index]);
		datasliceright = (%(simdattr)s) %(simdload)s(%(simdcast)s&data2[index]);
		// The actual SIMD operation. The compiler generates the correct SIMD
		// operations, and stores them as a vector.
		resultslice = datasliceleft %(compare_ops)s datasliceright;
		// Compare the results of the SIMD operation.
		if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
			return 0;
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		if (!(data1[index] %(compare_ops)s data2[index])) {
			return 0;
		}
	}

	return 1;

}

#endif

"""

# ==============================================================================


# ==============================================================================

# This is the set of function calls used to call each operator function.
compcall = """
		// %(funcmodifier)s
		case '%(arraycode)s' : {
			switch (arraydata.paramcat) {
				case param_arr_num : {
					resultcode = %(funclabel)s_%(funcmodifier)s_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.%(arraycode)s, arraydata.param.%(arraycode)s);
					break;
				}
				case param_num_arr : {
					resultcode = %(funclabel)s_%(funcmodifier)s_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.%(arraycode)s, arraydata.array2.%(arraycode)s);
					break;
				}
				case param_arr_arr : {
					resultcode = %(funclabel)s_%(funcmodifier)s_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.%(arraycode)s, arraydata.array2.%(arraycode)s);
					break;
				}
			}
			break;
		}
"""


# ==============================================================================


comp_params = """
/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	char resultcode = 0;

	// This is used to hold the parsed parameters.
	struct args_params_comp arraydata = ARGSINIT_COMP;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_comp(self, args, keywds, "%(funclabel)s");

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
			releasebuffers_comp(arraydata);
			ErrMsgTypeExpectFloat();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_comp(arraydata);


	// Return whether compare was OK.
	if (resultcode) {
		Py_RETURN_TRUE;
	} else {
		Py_RETURN_FALSE;
	}

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
  result = %(funclabel)s(array1, param) \\n\\
  result = %(funclabel)s(param, array1) \\n\\
  result = %(funclabel)s(array1, array2) \\n\\
  result = %(funclabel)s(array1, param, maxlen=y) \\n\\
  result = %(funclabel)s(array1, param, nosimd=False) \\n\\
\\n\\
* array1 - The first input data array to be examined. If no output  \\n\\
  array is provided the results will overwrite the input data.  \\n\\
* param - A non-array numeric parameter.  \\n\\
* array2 - A second input data array. Each element in this array is  \\n\\
  applied to the corresponding element in the first array.  \\n\\
* maxlen - Limit the length of the array used. This must be a valid  \\n\\
  positive integer. If a zero or negative length, or a value which is  \\n\\
  greater than the actual length of the array is specified, this  \\n\\
  parameter is ignored.  \\n\\
* nosimd - If True, SIMD acceleration is disabled if present.  \\n\\
  The default is False (SIMD acceleration is enabled if present). \\n\\
* result - A boolean value corresponding to the result of all the \\n\\
  comparison operations. If all comparison operations result in true, \\n\\
  the return value will be true. If any of them result in false, the \\n\\
  return value will be false. \\n\\
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

# SIMD call, version 1.
SIMD_call_1 = '''\n#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		return %(funclabel)s_%(funcmodifier)s_1_simd(arraylen, data1, param);
	}
#endif\n'''

# SIMD call, version 3.
SIMD_call_3 = '''\n#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		return %(funclabel)s_%(funcmodifier)s_3_simd(arraylen, param, data2);
	}
#endif\n'''


# SIMD call, version 5.
SIMD_call_5 = '''\n#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		return %(funclabel)s_%(funcmodifier)s_5_simd(arraylen, data1, data2);
	}
#endif\n'''


# ==============================================================================

# Various SIMD instruction information which varies according to array type.
simdvalues = {
'b' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v16qi', 'simdwidth' : 'CHARSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu'},
'B' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v16qi', 'simdwidth' : 'CHARSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu'},
'h' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v8hi', 'simdwidth' : 'SHORTSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu'},
'H' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v8hi', 'simdwidth' : 'SHORTSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu'},
'i' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v4si', 'simdwidth' : 'INTSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu'},
'I' : {'hassimd' : True, 'simdcast' : '(char *) ', 'simdattr' : 'v4si', 'simdwidth' : 'INTSIMDSIZE', 'simdload' : '__builtin_ia32_lddqu'},
'l' : {'hassimd' : False},
'L' : {'hassimd' : False},
'q' : {'hassimd' : False},
'Q' : {'hassimd' : False},
'f' : {'hassimd' : True, 'simdcast' : '', 'simdattr' : 'v4sf', 'simdwidth' : 'FLOATSIMDSIZE', 'simdload' : '__builtin_ia32_loadups'},
'd' : {'hassimd' : True, 'simdcast' : '', 'simdattr' : 'v2df', 'simdwidth' : 'DOUBLESIMDSIZE', 'simdload' : '__builtin_ia32_loadupd'},
}


# ==============================================================================


# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.

funclist = [x for x in oplist if x['c_code_template'] in ['template_comp']]


# ==============================================================================


for func in funclist:

	funcname = func['funcname']

	# Create the source code based on templates.
	filename = funcname + '.c'
	with open(filename, 'w') as f:
		funcdata = {'funclabel' : funcname}
		f.write(mathops_head % {'funclabel' : funcname})
		opscalltext = []



		# Check each array type.
		for arraycode in codegen_common.arraycodes:
			funcdata['funcmodifier'] = codegen_common.arraytypes[arraycode].replace(' ', '_')
			funcdata['arraytype'] = codegen_common.arraytypes[arraycode]

			if arraycode == 'f':
				funcdata['copname'] = func['c_operator_f']
			elif arraycode == 'd':
				funcdata['copname'] = func['c_operator_d']
			elif arraycode in codegen_common.intarrays:
				 funcdata['copname'] = func['c_operator_i']
			else:
				print('Error - Unsupported array code.', arraycode)


			# Each call to an SIMD function comes in three different versions due
			# to there being three different parameter formats.
			if simdvalues[arraycode]['hassimd']:
				simdfunccall = {'simdwidth' : simdvalues[arraycode]['simdwidth'], 
					'funclabel' : funcdata['funclabel'],
					'funcmodifier' : funcdata['funcmodifier']}
				simd_call_1 = SIMD_call_1 % simdfunccall
				simd_call_3 = SIMD_call_3 % simdfunccall
				simd_call_5 = SIMD_call_5 % simdfunccall
			else:
				simd_call_1 = ''
				simd_call_3 = ''
				simd_call_5 = ''


			funcdata['simd_call_1'] = simd_call_1
			funcdata['simd_call_3'] = simd_call_3
			funcdata['simd_call_5'] = simd_call_5

			f.write(ops_comp % funcdata)

			# This is the call to the functions for this array type. This
			# is inserted into another template below.
			funcdata['arraycode'] = arraycode
			opscalltext.append(compcall % funcdata)

		supportedarrays = codegen_common.FormatDocsArrayTypes(func['arraytypes'])

		f.write(comp_params % {'funclabel' : func['funcname'], 
				'opcodedocs' : func['opcodedocs'], 
				'supportedarrays' : supportedarrays,
				'matherrors' : ', '.join(func['matherrors'].split(',')),
				'opscall' : ''.join(opscalltext),
				'simd_call_1' : simd_call_1,
				'simd_call_3' : simd_call_3,
				'simd_call_5' : simd_call_5})



# ==============================================================================

# ==============================================================================

# The original date of the SIMD C code.
simdcodedate = '16-Jan-2018'
simdfilename = '_simd_x86'

# This outputs the SIMD version.

for func in funclist:

	outputlist = []

	funcname = func['funcname']

	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname


	# Output the generated code.
	for funtypes in codegen_common.arraycodes:

		if simdvalues[funtypes]['hassimd']:
			arraytype = codegen_common.arraytypes[funtypes]

			# The compare_ops symbols is the same for integer and floating point.
			datavals = {'funclabel' : funcname,
						'arraytype' : arraytype, 
						'funcmodifier' : arraytype.replace(' ', '_'),
						'arraycode' : funtypes,
						'arraytype' : codegen_common.arraytypes[funtypes],
						'compare_ops' : func['c_operator_i'],
						}


			# Start of function definition.
			datavals.update(simdvalues[funtypes])
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

