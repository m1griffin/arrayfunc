#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for amax, amin.
# Language: Python 3.6
# Date:     12-May-2019
#
###############################################################################
#
#   Copyright 2014 - 2019    Michael Griffin    <m12.griffin@gmail.com>
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

ops_head = """//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   %(funclabel)s.c
// Purpose:  Calculate the %(funclabel)s of values in an array.
// Language: C
// Date:     12-May-2019.
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

#include "arrayparams_booloutsimd.h"

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

# The basic template for the operation.
opstemplate = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The %(optype)simum value found.
*/
%(resultcasts)s a%(optype)s_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data) { 

	// array index counter. 
	Py_ssize_t x; 
	%(arraytype)s %(optype)sfound;

	%(optype)sfound = data[0];
	for(x = 0; x < arraylen; x++) {
		if (data[x] %(compare_ops)s %(optype)sfound) {
			%(optype)sfound = data[x];
		}
	}

	return (%(resultcasts)s) %(optype)sfound;
}
/*--------------------------------------------------------------------------- */

"""



template_simdsupport = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The %(optype)simum value found.
*/
%(simdplatform)s
%(resultcasts)s a%(optype)s_%(funcmodifier)s_simd(Py_ssize_t arraylen, %(arraytype)s *data) { 

	// array index counter. 
	Py_ssize_t x, alignedlength; 
	unsigned int y;
	%(arraytype)s %(optype)sfound;

	%(arraytype)s %(optype)svals[%(simdwidth)s];
	%(simdattr)s %(optype)sslice, dataslice;


	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen %% %(simdwidth)s);

	// Initialise the comparison values.
	%(optype)sslice = %(vldinstr)s &data[0]);

	// Use SIMD.
	for(x = %(simdwidth)s; x < alignedlength; x += %(simdwidth)s) {
		dataslice = %(vldinstr)s &data[x]);
		%(optype)sslice = %(simdop)s (%(optype)sslice, dataslice);
	}

	// Find the %(optype)s within the slice.
	%(vstinstr1)s %(optype)svals, %(vstinstr2)s  %(optype)sslice);
	%(optype)sfound = %(optype)svals[0];
	for (y = 1; y < %(simdwidth)s; y++) {
		if (%(optype)svals[y] %(compare_ops)s %(optype)sfound) {
			%(optype)sfound = %(optype)svals[y];
		}
	}

	// Get the %(optype)s value within the left over elements at the end of the array.
	for(x = alignedlength; x < arraylen; x++) {
		if (data[x] %(compare_ops)s %(optype)sfound) {
			%(optype)sfound = data[x];
		}
	}

	return (%(resultcasts)s) %(optype)sfound;
}
#endif
/*--------------------------------------------------------------------------- */

"""

# Select using either the SIMD or non-SIMD version.
template_opselect = """
/*--------------------------------------------------------------------------- */
/* For array code: %(arraycode)s
   arraylen = The length of the data arrays.
   data = The input data array.
   Returns: The %(optype)simum value found.
*/
%(resultcasts)s a%(optype)s_%(funcmodifier)s_select(Py_ssize_t arraylen, int nosimd, %(arraytype)s *data) { 

	%(simdplatform)s
	if (!nosimd && (arraylen >= (%(simdwidth)s * 2))) {
		return %(funclabel)s_%(funcmodifier)s_simd(arraylen, data);
	} else {
	#endif
		return %(funclabel)s_%(funcmodifier)s(arraylen, data);
	%(simdplatform)s
	}
	#endif

}
/*--------------------------------------------------------------------------- */

"""

# ==============================================================================


amaxamin_select = """
/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// This is used to hold the parsed parameters.
	struct args_params_booloutsimd arraydata = ARGSINIT_BOOLOUTSIMD;


	// The parameter version is available in all possible types.
	signed long long resultq;
	unsigned long long resultQ;
	double resultd;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_booloutsimd(self, args, keywds, "%(funclabel)s");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}


	// The length of the data array.
	if (arraydata.arraylength < 1) {
		// Release the buffers. 
		releasebuffers_booloutsimd(arraydata);
		ErrMsgArrayLengthErr();
		return NULL;
	}



	/* Call the C function */
	switch(arraydata.arraytype) {
		// signed char
		case 'b' : {
			resultq = %(funclabel)s_signed_char_select(arraydata.arraylength, arraydata.nosimd, arraydata.array1.b);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromLongLong(resultq);
			break;
		}
		// unsigned char
		case 'B' : {
			resultQ = %(funclabel)s_unsigned_char_select(arraydata.arraylength, arraydata.nosimd, arraydata.array1.B);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromUnsignedLongLong(resultQ);
			break;
		}
		// signed short
		case 'h' : {
			resultq = %(funclabel)s_signed_short_select(arraydata.arraylength, arraydata.nosimd, arraydata.array1.h);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromLongLong(resultq);
			break;
		}
		// unsigned short
		case 'H' : {
			resultQ = %(funclabel)s_unsigned_short_select(arraydata.arraylength, arraydata.nosimd, arraydata.array1.H);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromUnsignedLongLong(resultQ);
			break;
		}
		// signed int
		case 'i' : {
			resultq = %(funclabel)s_signed_int_select(arraydata.arraylength, arraydata.nosimd, arraydata.array1.i);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromLongLong(resultq);
			break;
		}
		// unsigned int
		case 'I' : {
			resultQ = %(funclabel)s_unsigned_int_select(arraydata.arraylength, arraydata.nosimd, arraydata.array1.I);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromUnsignedLongLong(resultQ);
			break;
		}
		// signed long
		case 'l' : {
			resultq = %(funclabel)s_signed_long(arraydata.arraylength, arraydata.array1.l);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromLongLong(resultq);
			break;
		}
		// unsigned long
		case 'L' : {
			resultQ = %(funclabel)s_unsigned_long(arraydata.arraylength, arraydata.array1.L);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromUnsignedLongLong(resultQ);
			break;
		}
		// signed long long
		case 'q' : {
			resultq = %(funclabel)s_signed_long_long(arraydata.arraylength, arraydata.array1.q);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromLongLong(resultq);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultQ = %(funclabel)s_unsigned_long_long(arraydata.arraylength, arraydata.array1.Q);
			releasebuffers_booloutsimd(arraydata);
			return PyLong_FromUnsignedLongLong(resultQ);
			break;
		}
		// float
		case 'f' : {
			resultd = %(funclabel)s_float_select(arraydata.arraylength, arraydata.nosimd, arraydata.array1.f);
			releasebuffers_booloutsimd(arraydata);
			return PyFloat_FromDouble(resultd);
			break;
		}
		// double
		case 'd' : {
			resultd = %(funclabel)s_double_select(arraydata.arraylength, arraydata.nosimd, arraydata.array1.d);
			releasebuffers_booloutsimd(arraydata);
			return PyFloat_FromDouble(resultd);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_booloutsimd(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_booloutsimd(arraydata);


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
Equivalent to:          %(optype)s(x) \\n\\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \\n\\
======================  ============================================== \\n\\
\\n\\
Call formats: \\n\\
\\n\\
  result = %(funclabel)s(array) \\n\\
  result = %(funclabel)s(array, maxlen=y) \\n\\
  result = %(funclabel)s(array, nosimd=False) \\n\\
\\n\\
* array - The input data array to be examined. \\n\\
* maxlen - Limit the length of the array used. This must be a valid \\n\\
  positive integer. If a zero or negative length, or a value which is \\n\\
  greater than the actual length of the array is specified, this \\n\\
  parameter is ignored. \\n\\
* nosimd - If True, SIMD acceleration is disabled if present. \\n\\
  The default is False (SIMD acceleration is enabled if present). \\n\\
* result = The  %(optype)simum of all the values in the array. \\n\\
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


maindescription = 'Returns True if all elements in an array meet the selected criteria.'

# The original date of the platform independent C code.
ccodedate = '08-May-2014'

# The original date of the SIMD C code.
simdcodedate = '01-May-2017'


# The functions which are implemented by this program.
completefuncnames = ('amax', 'amin')



# The return codes for each function.
resultcasts = {'b' : 'signed long long',
		'B' : 'unsigned long long',
		'h' : 'signed long long',
		'H' : 'unsigned long long',
		'i' : 'signed long long',
		'I' : 'unsigned long long',
		'l' : 'signed long long',
		'L' : 'unsigned long long',
		'q' : 'signed long long',
		'Q' : 'unsigned long long',
		'f' : 'double',
		'd' : 'double',
}


# The operators used to compare.
compare_ops = {'amax' : '>', 
			'amin' : '<', 
}

# The name of the function without the leading 'a'.
optype = {'amax' : 'max', 
			'amin' : 'min', 
}



# ==============================================================================

# Various SIMD instruction information which varies according to array type.


# The SIMD op.
# For x86-64.
simdops_x86 = {
	# The SIMD op for min.
	'amin' : {
		'b' : '__builtin_ia32_pminsb128',
		'B' : '__builtin_ia32_pminub128',
		'h' : '__builtin_ia32_pminsw128',
		'H' : '__builtin_ia32_pminuw128',
		'i' : '__builtin_ia32_pminsd128',
		'I' : '__builtin_ia32_pminud128',
		'f' : '__builtin_ia32_minps',
		'd' : '__builtin_ia32_minpd',
		},
		# The SIMD op for max.
	'amax' : {
		'b' : '__builtin_ia32_pmaxsb128',
		'B' : '__builtin_ia32_pmaxub128',
		'h' : '__builtin_ia32_pmaxsw128',
		'H' : '__builtin_ia32_pmaxuw128',
		'i' : '__builtin_ia32_pmaxsd128',
		'I' : '__builtin_ia32_pmaxud128',
		'f' : '__builtin_ia32_maxps',
		'd' : '__builtin_ia32_maxpd',
		},
}

# For ARM NEON.
simdops_arm = {
	# The SIMD op for min.
	'amin' : {
		'b' : 'vmin_s8',
		'B' : 'vmin_u8',
		'h' : 'vmin_s16',
		'H' : 'vmin_u16',
		'i' : 'vmin_s32',
		'I' : 'vmin_u32',
		'f' : 'vmin_f32',
		},
		# The SIMD op for max.
	'amax' : {
		'b' : 'vmax_s8',
		'B' : 'vmax_u8',
		'h' : 'vmax_s16',
		'H' : 'vmax_u16',
		'i' : 'vmax_s32',
		'I' : 'vmax_u32',
		'f' : 'vmax_f32',
		},
}


# Various SIMD instruction information which varies according to array type.
# For x86-64.
simdvalues_x86 = {
'b' : {'simdattr' : 'v16qi', 
		'vldinstr' : '(v16qi) __builtin_ia32_lddqu((char *)', 
		'vstinstr1' : '__builtin_ia32_storedqu((char *)',
		'vstinstr2' : ''},
'B' : {'simdattr' : 'v16qi', 
		'vldinstr' : '(v16qi) __builtin_ia32_lddqu((char *)', 
		'vstinstr1' : '__builtin_ia32_storedqu((char *)',
		'vstinstr2' : ''},
'h' : {'simdattr' : 'v8hi', 
		'vldinstr' : '(v8hi) __builtin_ia32_lddqu((char *)', 
		'vstinstr1' : '__builtin_ia32_storedqu((char *)',
		'vstinstr2' : '(v16qi)'},
'H' : {'simdattr' : 'v8hi', 
		'vldinstr' : '(v8hi) __builtin_ia32_lddqu((char *)', 
		'vstinstr1' : '__builtin_ia32_storedqu((char *)',
		'vstinstr2' : '(v16qi)'},
'i' : {'simdattr' : 'v4si', 
		'vldinstr' : '(v4si) __builtin_ia32_lddqu((char *)', 
		'vstinstr1' : '__builtin_ia32_storedqu((char *)',
		'vstinstr2' : '(v16qi)'},
'I' : {'simdattr' : 'v4si', 
		'vldinstr' : '(v4si) __builtin_ia32_lddqu((char *)', 
		'vstinstr1' : '__builtin_ia32_storedqu((char *)',
		'vstinstr2' : '(v16qi)'},
'f' : {'simdattr' : 'v4sf', 
		'vldinstr' : '(v4sf) __builtin_ia32_loadups(', 
		'vstinstr1' : '__builtin_ia32_storeups(',
		'vstinstr2' : '(v4sf)'},
'd' : {'simdattr' : 'v2df', 
		'vldinstr' : '(v2df) __builtin_ia32_loadupd(', 
		'vstinstr1' : '__builtin_ia32_storeupd(',
		'vstinstr2' : '(v2df)'},
}


# For ARM NEON.
simdvalues_arm = {
'b' : {'simdattr' : 'int8x8_t', 
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
'f' : {'simdattr' : 'float32x2_t', 
		'vldinstr' : 'vld1_f32(', 
		'vstinstr1' : 'vst1_f32(',
		'vstinstr2' : ''},
}



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

# ==============================================================================
# This outputs the non-SIMD version.
# Output the generated code.

# Output the functions which implement the individual non-SIMD 
# implementation functions.
for funcname in completefuncnames:

	filename = funcname + '.c'


	with open(filename, 'w') as f:
		f.write(ops_head % {'funclabel' : funcname})

		# Each type of array.
		for arraycode in codegen_common.arraycodes:
			arraytype = codegen_common.arraytypes[arraycode]
			funcmodifier = arraytype.replace(' ', '_')


			opdata = {'arraycode' : arraycode, 
					'arraytype' : arraytype, 
					'funclabel' : funcname,
					'funcmodifier' : arraytype.replace(' ', '_'), 
					'optype' : optype[funcname],
					'compare_ops' : compare_ops[funcname],
					'resultcasts' : resultcasts[arraycode],
					}

			# Select the individual operation via a switch.
			f.write(opstemplate % opdata)

			# Select using either the SIMD or non-SIMD version.
			if (arraycode in simdvalues_x86) or (arraycode in simdvalues_arm):
				opdata['simdwidth'] = simdwidth[arraycode]
				opdata['simdplatform'] = findsimdplatform(arraycode)
				f.write(template_opselect % opdata)


		#####

		# The program entry point and parameter parsing and code.
		f.write(amaxamin_select % {'funclabel' : funcname,
								'optype' : optype[funcname],
								})




# ==============================================================================

# This outputs the SIMD version for x86-64.

# The original date of the SIMD C code.
simdcodedate = '16-Apr-2019'
simdfilename = '_simd_x86'

# This outputs the SIMD version.

for funcname in completefuncnames:

	outputlist = []


	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname

	# Output the generated code.
	for arraycode in codegen_common.arraycodes:

		arraytype = codegen_common.arraytypes[arraycode]

		if arraycode in simdvalues_x86:

			outputlist.append(template_simdsupport % {'arraycode' : arraycode, 
						'optype' : optype[funcname],
						'arraytype' : arraytype, 
						'funcmodifier' : arraytype.replace(' ', '_'), 
						'resultcasts' : resultcasts[arraycode],
						'compare_ops' : compare_ops[funcname],
						'simdwidth' : simdwidth[arraycode],
						'simdplatform' : SIMD_platform_x86,
						'simdattr' : simdvalues_x86[arraycode]['simdattr'],
						'vldinstr' : simdvalues_x86[arraycode]['vldinstr'],
						'vstinstr1' : simdvalues_x86[arraycode]['vstinstr1'],
						'vstinstr2' : simdvalues_x86[arraycode]['vstinstr2'],
						'simdop' : simdops_x86[funcname][arraycode],
						})



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

# The original date of the SIMD C code.
simdcodedate = '08-Oct-2019'
simdfilename = '_simd_arm'

# This outputs the SIMD version.

for funcname in completefuncnames:

	outputlist = []


	# This provides the description in the header of the file.
	maindescription = 'Calculate the %s of values in an array.' % funcname

	# Output the generated code.
	for arraycode in codegen_common.arraycodes:

		arraytype = codegen_common.arraytypes[arraycode]

		if arraycode in simdvalues_arm:

			outputlist.append(template_simdsupport % {'arraycode' : arraycode, 
						'optype' : optype[funcname],
						'arraytype' : arraytype, 
						'funcmodifier' : arraytype.replace(' ', '_'), 
						'resultcasts' : resultcasts[arraycode],
						'compare_ops' : compare_ops[funcname],
						'simdwidth' : simdwidth[arraycode],
						'simdplatform' : SIMD_platform_ARM,
						'simdattr' : simdvalues_arm[arraycode]['simdattr'],
						'vldinstr' : simdvalues_arm[arraycode]['vldinstr'],
						'vstinstr1' : simdvalues_arm[arraycode]['vstinstr1'],
						'vstinstr2' : simdvalues_arm[arraycode]['vstinstr2'],
						'simdop' : simdops_arm[funcname][arraycode],
						})



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
