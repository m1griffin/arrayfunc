#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for count, cycle, and repeat.
# Language: Python 3.6
# Date:     04-Jun-2019
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


func_head = """//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   %(funclabel)s.c
// Purpose:  %(description)s
// Language: C
// Date:     04-Jun-2019.
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

#include "arrayerrs.h"

#include "arrayparams_base.h"

#include "arrayparams_cntcycrep.h"

/*--------------------------------------------------------------------------- */
"""

# ==============================================================================


ops_count_signed = """
/*--------------------------------------------------------------------------- */
/* For arraycode: %(arraycode)s
   * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * hasstep = If true, use the provided step value, otherwise use a default step.
*/
void count_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s startvalue, %(arraytype)s stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x; 
	%(arraytype)s increment, step;

	increment = startvalue;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1%(decimalfiller)s;
	}

	// Count down.
	for(x = 0; x < arraylen; x++) {
		data[x] = increment;
		increment = increment + step;
	}

}
"""



ops_count_unsigned = """
/*--------------------------------------------------------------------------- */
/* For arraycode: %(arraycode)s
   * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * hasstep = If true, use the provided step value, otherwise use a default step.
*/
void count_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s startvalue, %(stepparamctypecode)s stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x; 
	%(arraytype)s increment, step;

	increment = startvalue;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue >= 0 ? stepvalue : -stepvalue;
	} else {
		step = 1;
	}

	if (hasstep && (stepvalue < 0)) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
		}
	}

}
"""

# ==============================================================================


# ==============================================================================

ops_cycle = """
/*--------------------------------------------------------------------------- */
/* For arraycode: %(arraycode)s
   arraylen = The length of the data arrays.
   data = The input data array.
   startvalue = The value to start filling the data array.
   stopvalue = The value to stop incrementing and begin again from startvalue.
   stepvalue = The increment value.
   hasstep = If true, use the provided step value, otherwise use a default step.
   Returns nothing (void).
*/
void cycle_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s startvalue, %(arraytype)s stopvalue, %(arraytype)s stepvalue, char hasstep) { 

	// array index counter. 
	Py_ssize_t x;
	// Temporary value for cycling through the range.
	%(arraytype)s increment, step;

	// If the user does not provide a "step" value, use a default.
	if (hasstep) {
		step = stepvalue;
	} else {
		step = 1%(decimalfiller)s;
	}

	// Count up.
	if (startvalue <= stopvalue) {
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + step;
			if (increment > stopvalue) {
				increment = startvalue;
			}
		}
	} else {
	// Count down.
		increment = startvalue;
		for (x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - step;
			if (increment < stopvalue) {
				increment = startvalue;
			}
		}
	}

}
"""


# ==============================================================================

# ==============================================================================

ops_repeat = """
/*--------------------------------------------------------------------------- */
/* For arraycode: %(arraycode)s
   arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_%(funcmodifier)s(Py_ssize_t arraylen, %(arraytype)s *data, %(arraytype)s fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}
"""

# ==============================================================================


# ==============================================================================


call_params1 = """
/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_%(funclabel)s(PyObject *self, PyObject *args, PyObject *keywds) {


	// This is used to hold the parsed parameters.
	struct args_params_cntcycrep arraydata = ARGSINIT_CNTCYCREP;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_%(funclabel)s(self, args, keywds, "%(funclabel)s");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}


	// The length of the data array.
	if (arraydata.arraylength < 1) {
		// Release the buffers. 
		releasebuffers_cntcycrep(arraydata);
		ErrMsgArrayLengthErr();
		return NULL;
	}



	/* Call the C function */
	switch(arraydata.arraytype) {"""

# The function calls to each implementation function gets inserted in between here. 

# The rest of the switch statement picks up here.
call_params2 = """
		// We don't know this code.
		default: {
			releasebuffers_cntcycrep(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_cntcycrep(arraydata);

	// Everything was successful.
	Py_RETURN_NONE;


}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(%(funclabel)s__doc__,
"%(funcdesc)s \\n\\
_____________________________ \\n\\
\\n\\
%(funcdesc)s \\n\\
\\n\\
======================  ============================================== \\n\\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \\n\\
Exceptions raised:      None \\n\\
======================  ============================================== \\n\\
\\n\\
Call formats: \\n\\
\\n\\
  %(funcparamdesc)s \\n\\
\\n\\
%(paramdesc)s");


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


# Calling the implementation functions.
countcall = '''
		// %(arraytype)s
		case '%(arraycode)s' : {
			count_%(funcmodifier)s(arraydata.arraylength, arraydata.array1.%(arraycode)s, arraydata.param1.%(arraycode)s, arraydata.param2.%(stepparampytypecode)s, arraydata.hasparam2);
			break;
		}'''

cyclecall = '''
		// %(arraytype)s
		case '%(arraycode)s' : {
			cycle_%(funcmodifier)s(arraydata.arraylength, arraydata.array1.%(arraycode)s, arraydata.param1.%(arraycode)s, arraydata.param2.%(arraycode)s, arraydata.param3.%(arraycode)s, arraydata.hasparam3);
			break;
		}'''

repeatcall = '''
		// %(arraytype)s
		case '%(arraycode)s' : {
			repeat_%(funcmodifier)s(arraydata.arraylength, arraydata.array1.%(arraycode)s, arraydata.param1.%(arraycode)s);
			break;
		}'''

func_calls = {'count' : countcall, 
			'cycle' : cyclecall, 
			'repeat' : repeatcall
}


# ==============================================================================




# The functions which are implemented by this program.
completefuncnames = ('count', 'cycle', 'repeat')

# The templates to use. 
# We need to handle signed and unsigned separately due to a special
# case for count.
ops_calls_signed = {'count' : ops_count_signed, 
			'cycle' : ops_cycle, 
			'repeat' : ops_repeat
}

ops_calls_unsigned = {'count' : ops_count_unsigned, 
			'cycle' : ops_cycle, 
			'repeat' : ops_repeat
}


# How many additional parameters there are besides the array. 
paramnumb = {'count' : 2, 
			'cycle' : 3, 
			'repeat' : 1
}



# Descriptions of each function. These are inserted into the C source code files.
funcdesc = {'count' : 'Fill an array with evenly spaced values using a start and step values.', 
			'cycle' : 'Fill an array with a series of values, repeating as necessary.', 
			'repeat' : 'Fill an array with a specified value.'
}


# The call format.
funcparamdesc = {'count' : 'count(array, start, step).', 
			'cycle' : 'cycle(array, start, stop, step)', 
			'repeat' : 'repeat(array, value)'
}

# The description of the parameters.
paramdesc = {'count' : '''* array - The output array. \\n\\
* start - The numeric value to start from. \\n\\
* step - The value to increment by when creating each element. This \\n\\
  parameter is optional. If it is omitted, a value of 1 is assumed. A \\n\\
  negative step value will cause the function to count down.''', 
			'cycle' : '''* array - The output array. \\n\\
* start - The numeric value to start from. \\n\\
* stop - The value at which to stop incrementing. If stop is less than \\n\\
  start, cycle will count down. \\n\\
* step - The value to increment by when creating each element. This \\n\\
  parameter is optional. If it is omitted, a value of 1 is assumed. The\\n\\
  sign is ignored and the absolute value used when incrementing.''', 
			'repeat' : '''* array - The output array. \\n\\
* value - The value to use to fill the array.'''
}



# The integer type to use for the "step" parameter.
stepparamctypecode = {'b' : 'signed char', 'B' : 'signed char', 
	'h' : 'signed short', 'H' : 'signed short', 
	'i' : 'signed int', 'I' : 'signed int', 
	'l' : 'signed long', 'L' : 'signed long', 
	'q' : 'signed long long', 'Q' : 'signed long long', 
	'f' : 'float', 'd' : 'double'}

# The arraycode to use for the "step" parameter.
stepparampytypecode = {'b' : 'b', 'B' : 'b',
					'h' : 'h', 'H' : 'h',
					'i' : 'i', 'I' : 'i',
					'l' : 'l', 'L' : 'l',
					'q' : 'q', 'Q' : 'q',
					'f' : 'f', 'd' : 'd'}


# ==============================================================================


# Create the source code based on templates.
for funcname in completefuncnames:

	filename = funcname + '.c'
	with open(filename, 'w') as f:
		funcdata = {'funclabel' : funcname}
		f.write(func_head % {'funclabel' : funcname, 'description' : funcdesc[funcname]})


		# Check each array type.
		for arraycode in codegen_common.arraycodes:
			funcdata = {'funcmodifier' : codegen_common.arraytypes[arraycode].replace(' ', '_'),
					'arraytype' : codegen_common.arraytypes[arraycode],
					'arraycode' : arraycode,
					'description' : funcdesc[funcname],
					'stepparamctypecode' : stepparamctypecode[arraycode]}

			# This is required for count only.
			if arraycode in codegen_common.floatarrays:
				funcdata['decimalfiller'] = '.0'
			else:
				funcdata['decimalfiller'] = ''

			# Count needs special handling for unsigned arrays.
			if arraycode in codegen_common.unsignedint:
				ops_calls = ops_calls_unsigned
			else:
				ops_calls = ops_calls_signed

			f.write(ops_calls[funcname] % funcdata)


		# Start of the boilerplate, and parse the parameters.
		f.write(call_params1 % {'funclabel' : funcname,
							'funcdesc' : funcdesc[funcname],
							'funcparamdesc' : funcparamdesc[funcname],
							'paramdesc' : paramdesc[funcname],
							'paramnumb' : paramnumb[funcname]})

		# Call each implementation function in a switch statement.
		for arraycode in codegen_common.arraycodes:
			funcdata = {'funcmodifier' : codegen_common.arraytypes[arraycode].replace(' ', '_'),
					'arraytype' : codegen_common.arraytypes[arraycode],
					'arraycode' : arraycode,
					'stepparampytypecode' : stepparampytypecode[arraycode]}
			f.write(func_calls[funcname] % funcdata)


		# The boilerplate at the end.
		f.write(call_params2 % {'funclabel' : funcname,
							'funcdesc' : funcdesc[funcname],
							'funcparamdesc' : funcparamdesc[funcname],
							'paramdesc' : paramdesc[funcname]})



# ==============================================================================
