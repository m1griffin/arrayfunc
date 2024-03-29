#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for math operators with one variable.
# Language: Python 3.4
# Date:     18-Mar-2018
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

uniops_head = """//------------------------------------------------------------------------------
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
		for (x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data[x] = ~data[x];
		}
	}

}

"""
# ==============================================================================


# ==============================================================================

# The actual invert operations using SIMD operations. x86-64 version.
ops_simdsupport_x86 = """
/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
*/
// param_arr_none
#if defined(AF_HASSIMD_X86)
void %(funclabel)s_%(funcmodifier)s_1_simd(Py_ssize_t arraylen, %(arraytype)s *data) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2di datasliceleft;
	v2di vopmask = {-1, -1};


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = (v2di) __builtin_ia32_lddqu((char *)  &data[index]);
		// The actual SIMD operation. 
		datasliceleft = __builtin_ia32_pxor128(datasliceleft, vopmask);
		// Store the result.
		__builtin_ia32_storedqu((char *) &data[index], (v16qi) datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data[index] = ~data[index];
	}

}


// param_arr_arr
void %(funclabel)s_%(funcmodifier)s_2_simd(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s *dataout) {

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;

	v2di datasliceleft;
	v2di vopmask = {-1, -1};


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = (v2di) __builtin_ia32_lddqu((char *)  &data[index]);
		// The actual SIMD operation. 
		datasliceleft = __builtin_ia32_pxor128(datasliceleft, vopmask);
		// Store the result.
		__builtin_ia32_storedqu((char *) &dataout[index], (v16qi) datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		dataout[index] = ~data[index];
	}

}
#endif

"""

# The actual invert operations using SIMD operations. ARM version.
ops_simdsupport_arm = """
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
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s(&data[index]);
		// The actual SIMD operation. 
		datasliceleft = %(vopinstr)s(datasliceleft);
		// Store the result.
		%(vstinstr)s(&data[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		data[index] = ~data[index];
	}

}


// param_arr_arr
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
	for (index = 0; index < alignedlength; index += %(simdwidth)s) {
		// Load the data into the vector register.
		datasliceleft = %(vldinstr)s(&data[index]);
		// The actual SIMD operation. 
		datasliceleft = %(vopinstr)s(datasliceleft);
		// Store the result.
		%(vstinstr)s(&dataout[index], datasliceleft);
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
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

# ==============================================================================


# Various SIMD instruction information which varies according to array type.
# For x86-64.

# The actual SIMD instructions are embedded in the template. 
SIMD_x86_support = ('b', 'B', 'h', 'H', 'i', 'I')

# ==============================================================================

# For ARM NEON ARMv7 32 bit.

simdattr_armv7 = {
	'b' : ' int8x8_t', 
	'B' : 'uint8x8_t', 
	'h' : 'int16x4_t', 
	'H' : 'uint16x4_t', 
	'i' : 'int32x2_t ', 
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

vopinstr_armv7 = {
	'b' : 'vmvn_s8',
	'B' : 'vmvn_u8',
	'h' : 'vmvn_s16',
	'H' : 'vmvn_u16',
	'i' : 'vmvn_s32',
	'I' : 'vmvn_u32',
}


SIMD_armv7_support = simdattr_armv7.keys()


# ==============================================================================

# For ARM NEON armv8 64 bit.

simdattr_armv8 = {
	'b' : ' int8x16_t', 
	'B' : 'uint8x16_t', 
	'h' : 'int16x8_t', 
	'H' : 'uint16x8_t', 
	'i' : 'int32x4_t ', 
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

vopinstr_armv8 = {
	'b' : 'vmvnq_s8',
	'B' : 'vmvnq_u8',
	'h' : 'vmvnq_s16',
	'H' : 'vmvnq_u16',
	'i' : 'vmvnq_s32',
	'I' : 'vmvnq_u32',
}


SIMD_armv8_support = simdattr_armv8.keys()

# ==============================================================================

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
	else:
		return 'Error: Template error, this should not be here.'

# ==============================================================================

# ==============================================================================

# Read in the op codes.
opdata = codegen_common.ReadINI('affuncdata.ini')

funcname = 'invert'
func = opdata[funcname]


# ==============================================================================


# Create the source code based on templates.
filename = funcname + '.c'
with open(filename, 'w') as f:
	funcdata = {'funclabel' : funcname}
	f.write(uniops_head % {'funclabel' : funcname})
	opscalltext = []


	# Check each array type. The types of arrays supported must be looked up.
	for arraycode in codegen_common.intarrays:
		funcdata['funcmodifier'] = codegen_common.arraytypes[arraycode].replace(' ', '_')
		funcdata['arraytype'] = codegen_common.arraytypes[arraycode]
		funcdata['intmaxvalue'] = codegen_common.maxvalue[arraycode]
		funcdata['intminvalue'] = codegen_common.minvalue[arraycode]

		if arraycode in (set(SIMD_x86_support) | set(SIMD_armv7_support) | set(SIMD_armv8_support)):
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

	f.write(invert_params % {'funclabel' : funcname, 
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

outputlist = []

# This provides the description in the header of the file.
maindescription = 'Calculate the %s of values in an array.' % funcname


# Output the generated code.
for arraycode in SIMD_x86_support:

	arraytype = codegen_common.arraytypes[arraycode]

	# The compare_ops symbols is the same for integer and floating point.
	datavals = {'funclabel' : funcname,
				'arraytype' : arraytype, 
				'funcmodifier' : arraytype.replace(' ', '_'),
				'simdwidth' : simdwidth[arraycode],
				}


	# Start of function definition.
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

# This outputs the SIMD version for ARM NEON ARMv7 32 bit.
simdcodedate = '08-Oct-2019'
simdfilename = '_simd_armv7'

# This outputs the SIMD version.

outputlist = []

# This provides the description in the header of the file.
maindescription = 'Calculate the %s of values in an array.' % funcname


# Output the generated code.
for arraycode in SIMD_armv7_support:

	arraytype = codegen_common.arraytypes[arraycode]

	# The compare_ops symbols is the same for integer and floating point.
	datavals = {'funclabel' : funcname,
				'arraytype' : arraytype, 
				'funcmodifier' : arraytype.replace(' ', '_'),
				'simdplatform' : SIMD_platform_ARMv7,
				'simdwidth' : simdwidth[arraycode],
				'simdattr' : simdattr_armv7[arraycode],
				'vldinstr' : vldinstr_armv7[arraycode],
				'vstinstr' : vstinstr_armv7[arraycode],
				'vopinstr' : vopinstr_armv7[arraycode],
				}


	# Start of function definition.
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

# This outputs the SIMD version for ARM NEON ARMv8 64 bit.
simdcodedate = '25-Mar-2020'
simdfilename = '_simd_armv8'

# This outputs the SIMD version.


outputlist = []

# This provides the description in the header of the file.
maindescription = 'Calculate the %s of values in an array.' % funcname


# Output the generated code.
for arraycode in SIMD_armv8_support:

	arraytype = codegen_common.arraytypes[arraycode]

	# The compare_ops symbols is the same for integer and floating point.
	datavals = {'funclabel' : funcname,
				'arraytype' : arraytype, 
				'funcmodifier' : arraytype.replace(' ', '_'),
				'simdplatform' : SIMD_platform_ARM64v8,
				'simdwidth' : simdwidth[arraycode],
				'simdattr' : simdattr_armv8[arraycode],
				'vldinstr' : vldinstr_armv8[arraycode],
				'vstinstr' : vstinstr_armv8[arraycode],
				'vopinstr' : vopinstr_armv8[arraycode],
				}


	# Start of function definition.
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

