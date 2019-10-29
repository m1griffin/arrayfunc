#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for math operators with one variable.
# Language: Python 3.4
# Date:     18-Mar-2018
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

uniops_head = """//------------------------------------------------------------------------------
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
#include "arrayparams_onesimd.h"

#include "simddefs.h"

#ifdef AF_HASSIMD_X86
#include "%(funclabel)s_simd_x86.h"
#endif

#ifdef AF_HASSIMD_ARM
#include "arm_neon.h"
#include "%(funclabel)s_simd_arm.h"
#endif

/*--------------------------------------------------------------------------- */
"""


# ==============================================================================

# For inverting integer.
uniops_invert_int = """
/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   hasoutputarray = If true, the output goes into the second array.
   nosimd = If true, disable SIMD acceleration.
*/
void %(funclabel)s_%(funcmodifier)s(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data, %(arraytype)s *dataout, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;

%(simd_call)s
	if (hasoutputarray) {		
		for(x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
	} else {
		for(x = 0; x < arraylen; x++) {
			data[x] = ~data[x];
		}
	}

}

"""
# ==============================================================================


# ==============================================================================

# The actual invert operations using SIMD operations.
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
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = ~datasliceleft;
		// Store the result.
		%(vstinstr1)s &data[index], %(vstinstr2)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		data[index] = ~data[index];
	}

}
#endif


// param_arr_arr
%(simdplatform)s
void %(funclabel)s_%(funcmodifier)s_2_simd(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s *dataout) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	%(simdattr)s datasliceleft;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for(index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s &data[index]);
		// The actual SIMD operation. The compiler generates the correct instruction.
		datasliceleft = ~datasliceleft;
		// Store the result.
		%(vstinstr1)s &dataout[index], %(vstinstr2)s datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for(index = alignedlength; index < arraylen; index++) {
		dataout[index] = ~data[index];
	}

}
#endif

"""


# SIMD call template.
SIMD_call = '''\n%(simdplatform)s
	// SIMD version.
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		if (hasoutputarray) {
			%(funclabel)s_%(funcmodifier)s_2_simd(arraylen, data, dataout);
		} else {
			%(funclabel)s_%(funcmodifier)s_1_simd(arraylen, data);
		}
		return;
	}
#endif\n'''


# ==============================================================================

# This is the set of function calls used to call each operator function.
opscall = """
		// %(funcmodifier)s
		case '%(arraycode)s' : {
			%(funclabel)s_%(funcmodifier)s(arraydata.arraylength, arraydata.nosimd, arraydata.array1.%(arraycode)s, arraydata.array2.%(arraycode)s, arraydata.hasoutputarray);
			break;
		}
"""



invert_params = """

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// This is used to hold the parsed parameters.
	struct args_params_1 arraydata = ARGSINIT_ONE;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_one(self, args, keywds, 0, "%(funclabel)s");

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
    %(funclabel)s(array1) \\n\\
    %(funclabel)s(array1, outparray) \\n\\
    %(funclabel)s(array1, maxlen=y) \\n\\
    %(funclabel)s(array1, nosimd=False) \\n\\
 \\n\\
* array1 - The first input data array to be examined. If no output  \\n\\
  array is provided the results will overwrite the input data.  \\n\\
* outparray - The output array. This parameter is optional.  \\n\\
* maxlen - Limit the length of the array used. This must be a valid  \\n\\
  positive integer. If a zero or negative length, or a value which is  \\n\\
  greater than the actual length of the array is specified, this  \\n\\
  parameter is ignored.  \\n\\
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

# These get substituted into function call templates.
SIMD_platform_x86 = '#if defined(AF_HASSIMD_X86)'
SIMD_platform_x86_ARM = '#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM)'
SIMD_platform_ARM = '#if defined(AF_HASSIMD_ARM)'

# ==============================================================================


# Various SIMD instruction information which varies according to array type.
# For x86-64.
simdvalues_x86 = {
'b' : {'simdattr' : 'v16qi', 
		'vldinstr' : '(v16qi) __builtin_ia32_lddqu((char *) ', 
		'vstinstr1' : '__builtin_ia32_storedqu((char *) ',
		'vstinstr2' : ''},
'B' : {'simdattr' : 'v16qi', 
		'vldinstr' : '(v16qi) __builtin_ia32_lddqu((char *) ', 
		'vstinstr1' : '__builtin_ia32_storedqu((char *) ',
		'vstinstr2' : ''},
'h' : {'simdattr' : 'v8hi', 
		'vldinstr' : '(v8hi) __builtin_ia32_lddqu((char *) ', 
		'vstinstr1' : '__builtin_ia32_storedqu((char *) ',
		'vstinstr2' : '(v16qi) '},
'H' : {'simdattr' : 'v8hi', 
		'vldinstr' : '(v8hi) __builtin_ia32_lddqu((char *) ', 
		'vstinstr1' : '__builtin_ia32_storedqu((char *) ',
		'vstinstr2' : '(v16qi) '},
'i' : {'simdattr' : 'v4si', 
		'vldinstr' : '(v4si) __builtin_ia32_lddqu((char *) ', 
		'vstinstr1' : '__builtin_ia32_storedqu((char *) ',
		'vstinstr2' : '(v16qi) '},
'I' : {'simdattr' : 'v4si', 
		'vldinstr' : '(v4si) __builtin_ia32_lddqu((char *) ', 
		'vstinstr1' : '__builtin_ia32_storedqu((char *) ',
		'vstinstr2' : '(v16qi) '},
}


# For ARM NEON.
simdvalues_arm = {
'b' : {'simdattr' : ' int8x8_t', 
		'vldinstr' : 'vld1_s8(', 
		'vstinstr1' : 'vst1_s8(',
		'vstinstr2' : ''},
'B' : {'simdattr' : 'uint8x8_t', 
		'vldinstr' : 'vld1_u8(', 
		'vstinstr1' : 'vst1_u8(',
		'vstinstr2' : ''},
'h' : {'simdattr' : 'int16x4_t', 
		'vldinstr' : 'vld1_s16(', 
		'vstinstr1' : 'vst1_s16(',
		'vstinstr2' : ''},
'H' : {'simdattr' : 'uint16x4_t', 
		'vldinstr' : 'vld1_u16(', 
		'vstinstr1' : ' vst1_u16(',
		'vstinstr2' : ''},
'i' : {'simdattr' : 'int32x2_t ', 
		'vldinstr' : 'vld1_s32(', 
		'vstinstr1' : 'vst1_s32(',
		'vstinstr2' : ''},
'I' : {'simdattr' : 'uint32x2_t', 
		'vldinstr' : 'vld1_u32(', 
		'vstinstr1' : 'vst1_u32(',
		'vstinstr2' : ''},
}



# Width of array elements.
simdwidth = {'b' : 'CHARSIMDSIZE',
		'B' : 'CHARSIMDSIZE',
		'h' : 'SHORTSIMDSIZE',
		'H' : 'SHORTSIMDSIZE',
		'i' : 'INTSIMDSIZE',
		'I' : 'INTSIMDSIZE',
		}

# ==============================================================================

# Return the platform SIMD enable C macro. 
# This is for the platform independent file, and not the plaform specific
# SIMD files.
def findsimdplatform(arraycode):

	# The calls to SIMD support code are platform dependent.
	if (arraycode in simdvalues_x86) and (arraycode not in simdvalues_arm):
		return SIMD_platform_x86
	elif (arraycode in simdvalues_x86) and (arraycode in simdvalues_arm):
		return SIMD_platform_x86_ARM
	else:
		return 'Error: Template error, this should not be here.'

# ==============================================================================

# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.

funclist = [x for x in oplist if x['c_code_template'] == 'template_invert']

# ==============================================================================


for func in funclist:

	# Create the source code based on templates.
	filename = func['funcname'] + '.c'
	with open(filename, 'w') as f:
		funcdata = {'funclabel' : func['funcname']}
		f.write(uniops_head % {'funclabel' : func['funcname']})
		opscalltext = []


		# Check each array type. The types of arrays supported must be looked up.
		for arraycode in codegen_common.intarrays:
			funcdata['funcmodifier'] = codegen_common.arraytypes[arraycode].replace(' ', '_')
			funcdata['arraytype'] = codegen_common.arraytypes[arraycode]
			funcdata['intmaxvalue'] = codegen_common.maxvalue[arraycode]
			funcdata['intminvalue'] = codegen_common.minvalue[arraycode]

			if (arraycode in simdvalues_x86) or (arraycode in simdvalues_arm):
				simd_call_vals = {'simdwidth' : simdwidth[arraycode],
								'simdplatform' : findsimdplatform(arraycode),
								'funclabel' : funcdata['funclabel'], 
								'funcmodifier' : funcdata['funcmodifier']}

				funcdata['simd_call'] = SIMD_call % simd_call_vals
			else:
				funcdata['simd_call'] = ''

			f.write(uniops_invert_int % funcdata)

			# This is the call to the functions for this array type. This
			# is inserted into another template below.
			funcdata['arraycode'] = arraycode
			opscalltext.append(opscall % funcdata)

		supportedarrays = codegen_common.FormatDocsArrayTypes(func['arraytypes'])

		f.write(invert_params % {'funclabel' : func['funcname'], 
				'opcodedocs' : func['opcodedocs'], 
				'supportedarrays' : supportedarrays,
				'matherrors' : ', '.join(func['matherrors'].split(',')),
				'opscall' : ''.join(opscalltext)})



# ==============================================================================


# ==============================================================================

# This outputs the SIMD version for x86-64.
simdcodedate = '21-Mar-2019'
simdfilename = '_simd_x86'

# This outputs the SIMD version.

for func in funclist:

	outputlist = []

	funcname = func['funcname']

	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname


	# Output the generated code.
	for arraycode in codegen_common.arraycodes:

		if (arraycode in simdvalues_x86):
			arraytype = codegen_common.arraytypes[arraycode]

			# The compare_ops symbols is the same for integer and floating point.
			datavals = {'funclabel' : funcname,
						'arraytype' : arraytype, 
						'funcmodifier' : arraytype.replace(' ', '_'),
						'simdplatform' : SIMD_platform_x86,
						'simdwidth' : simdwidth[arraycode],
						'simdattr' : simdvalues_x86[arraycode]['simdattr'],
						'vldinstr' : simdvalues_x86[arraycode]['vldinstr'],
						'vstinstr1' : simdvalues_x86[arraycode]['vstinstr1'],
						'vstinstr2' : simdvalues_x86[arraycode]['vstinstr2'],
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



# ==============================================================================

# This outputs the SIMD version for ARM NEON.
simdcodedate = '08-Oct-2019'
simdfilename = '_simd_arm'

# This outputs the SIMD version.

for func in funclist:

	outputlist = []

	funcname = func['funcname']

	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname


	# Output the generated code.
	for arraycode in codegen_common.arraycodes:

		if (arraycode in simdvalues_arm):
			arraytype = codegen_common.arraytypes[arraycode]

			# The compare_ops symbols is the same for integer and floating point.
			datavals = {'funclabel' : funcname,
						'arraytype' : arraytype, 
						'funcmodifier' : arraytype.replace(' ', '_'),
						'simdplatform' : SIMD_platform_ARM,
						'simdwidth' : simdwidth[arraycode],
						'simdattr' : simdvalues_arm[arraycode]['simdattr'],
						'vldinstr' : simdvalues_arm[arraycode]['vldinstr'],
						'vstinstr1' : simdvalues_arm[arraycode]['vstinstr1'],
						'vstinstr2' : simdvalues_arm[arraycode]['vstinstr2'],
						}


			# Start of function definition.
			outputlist.append(ops_simdsupport % datavals)



	# This outputs the SIMD version.
	codegen_common.OutputSourceCode(funcname + simdfilename + '.c', outputlist, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate,
		'', ['simddefs', 'simdmacromsg_arm'])


	# Output the .h header file.
	headedefs = codegen_common.GenSIMDCHeaderText(outputlist, funcname)

	# Write out the file.
	codegen_common.OutputCHeader(funcname + simdfilename + '.h', headedefs, 
		maindescription, 
		codegen_common.SIMDDescription, 
		simdcodedate)

# ==============================================================================

