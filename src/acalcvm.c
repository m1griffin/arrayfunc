//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   acalcvm.c
// Purpose:  Calculate an equation over an array of doubles using an interpreter.
// Language: C
// Date:     24-Dec-2015
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2015    Michael Griffin    <m12.griffin@gmail.com>
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
#include <float.h>


#include "acalcvm_common.h"
#include "arrayfunc.h"
#include "arrayerrs.h"

#include "acalcvm_common.h"

/*--------------------------------------------------------------------------- */

// Provide a struct for returning data from parsing Python arguments.
struct args_param {
	char codearraytype;
	char varoffsetarraytype;
	char vararraytype;
	char constarraytype;
	char stackarraytype;
	char dataarraytype;
	char dataoutarraytype;
	char error;
};


// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist[] = {"code", "varoffset", "vars", "const", "vmstack", "data", "dataout", "vmstacksegments", "disovfl", "maxlen", NULL};

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// These arrays are used to track the effects that each op code has on the 
// interpreter stack. This is used to check for stack overflow. Since there are
// no conditional operators, control flow is completely predicatble. This means
// we can check the program for stack overflow once in advance, and not have to
// check when actually performing calculations. 
// We also need the maximum op code value so we can check if there is an invalid
// op code so we don't overflow the look-up table when checking.

signed int intstackcodes[] = {0, 1, 1, 1, -1, -1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, 0, -1, -1, 0, 0};
signed int floatstackcodes[] = {0, 1, 1, 1, -1, -1, -1, -1, -1, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0};

// We need the maximum op code value so we can check if there is an invalid
// op code so we don't overflow the look-up table when checking.

#define OPCODEMAXINT 20
#define OPCODEMAXFLOAT 47

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* Parse the Python arguments to objects, and then extract the object parameters
 * to determine their types. This lets us handle different data types as 
 * parameters.
 * This version expects the following parameters:
 * args (PyObject) = The positional arguments.
 * keywds (PyObject) = The keyword arguments.
 * Returns a structure containing the results of each parameter.
*/
struct args_param parsepyargs_parm(PyObject *args, PyObject *keywds) {

	// The arrays as objects, so we can examine their types.
	PyObject *dataobj, *dataoutobj, *codeobj, *varoffsetsobj, *varobj, 
			*constobj, *stackobj;


	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	struct args_param argtypes = {' ', ' ', ' ', ' ', ' ', ' ', ' ', 0};
	struct arrayparamstypes codearraytype = {0, 0, ' '};
	struct arrayparamstypes varoffsetarraytype = {0, 0, ' '};
	struct arrayparamstypes vararraytype = {0, 0, ' '};
	struct arrayparamstypes constarraytype = {0, 0, ' '};
	struct arrayparamstypes stackarraytype = {0, 0, ' '};
	struct arrayparamstypes dataarraytype = {0, 0, ' '};
	struct arrayparamstypes dataoutarraytype = {0, 0, ' '};

	unsigned int disableovfl = 0;
	unsigned int vmstacksegments = 0;


	// Import the raw objects. 
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "OOOOOOOi|in:acalcvm", kwlist, 
			&codeobj, &varoffsetsobj, &varobj, &constobj, &stackobj, 
			&dataobj, &dataoutobj, &vmstacksegments, &disableovfl, &arraymaxlen)) {
		argtypes.error = 1;
		return argtypes;
	}



	// Test if the first parameter is an array or bytes.
	codearraytype = paramarraytype(codeobj);
	if (!codearraytype.isarray) {
		argtypes.error = 2;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.codearraytype = codearraytype.arraycode;
	}


	// Test if the second parameter is an array or bytes.
	varoffsetarraytype = paramarraytype(varoffsetsobj);
	if (!varoffsetarraytype.isarray) {
		argtypes.error = 3;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.varoffsetarraytype = varoffsetarraytype.arraycode;
	}


	// Test if the third parameter is an array or bytes.
	vararraytype = paramarraytype(varobj);
	if (!vararraytype.isarray) {
		argtypes.error = 4;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.vararraytype = vararraytype.arraycode;
	}


	// Test if the fourth parameter is an array or bytes.
	constarraytype = paramarraytype(constobj);
	if (!constarraytype.isarray) {
		argtypes.error = 5;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.constarraytype = constarraytype.arraycode;
	}


	// Test if the fifth parameter is an array or bytes.
	stackarraytype = paramarraytype(stackobj);
	if (!stackarraytype.isarray) {
		argtypes.error = 6;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.stackarraytype = stackarraytype.arraycode;
	}


	// Test if the sixth parameter is an array or bytes.
	dataarraytype = paramarraytype(dataobj);
	if (!dataarraytype.isarray) {
		argtypes.error = 7;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.dataarraytype = dataarraytype.arraycode;
	}


	// Test if the seventh parameter is an array or bytes.
	dataoutarraytype = paramarraytype(dataoutobj);
	if (!dataoutarraytype.isarray) {
		argtypes.error = 8;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.dataoutarraytype = dataoutarraytype.arraycode;
	}

	return argtypes;

}


/*--------------------------------------------------------------------------- */

// Release the buffers.
void releasebuffers(Py_buffer *datapy, Py_buffer *dataoutpy, Py_buffer *codearraypy, 
					Py_buffer *varoffsetsarraypy, Py_buffer *vararraypy, 
					Py_buffer *constarraypy, Py_buffer *vmstackpy) {

	PyBuffer_Release(datapy);
	PyBuffer_Release(dataoutpy);
	PyBuffer_Release(codearraypy);
	PyBuffer_Release(varoffsetsarraypy);
	PyBuffer_Release(vararraypy);
	PyBuffer_Release(constarraypy);
	PyBuffer_Release(vmstackpy);
}

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// Check that the interpreter stack will not overflow. We do this by looking up
// what effect that op code has on the stack and adding this to a running total.
// If the running total is ever out of range, we return this as an error. 
// This allows us to check for overflow (or underflow) once instead of checking
// during each calculation in the array.
//
//   datarraycode = The array type code for the data array.
//   vmstacksize = The length of the interpreter stack.
//   codearray = The array of byte codes.
//   codearraysize = The length of the byte code array.
//   Return = 0 if OK, CALC_ERR_STACKOVFL_ERR if the stack would overflow, or 
//				CALC_ERR_UNKNOWNOP if an unknown op code is encountered.
int checkstackerror(char datarraycode, int vmstacksize, unsigned int *codearray, int codearraysize) {

	// This accumulates the current level in the stack.
	int stacklevel = 0;
	int i, intdata;
	unsigned int opcodemax;


	intdata = !((datarraycode == 'f') || (datarraycode == 'd'));

	// The first operation should be a push of some sort, which adds to the stack.
	if (intdata) {
		if (intstackcodes[codearray[0]] < 1) { return CALC_ERR_STACKOVFL_ERR; }
		opcodemax = OPCODEMAXINT;
	} else {
		if (floatstackcodes[codearray[0]] < 1) { return CALC_ERR_STACKOVFL_ERR; }
		opcodemax = OPCODEMAXFLOAT;
	}

	// Check if the op code is valid. This also makes sure we don't overflow
	// the look-up table used to check the stack effects.
	for (i=0; i < codearraysize; i++) {
		if (codearray[i] > opcodemax) {
			return CALC_ERR_UNKNOWNOP;
		}

		// The stack may be affected by the current op code.
		if (intdata) {
			stacklevel = stacklevel + intstackcodes[codearray[i]];
		} else {
			stacklevel = stacklevel + floatstackcodes[codearray[i]];
		}

		if ((stacklevel < 1) || (stacklevel > (vmstacksize - 2))) {
			return CALC_ERR_STACKOVFL_ERR;
		}
	}

	// No errors were found.
	return 0;

}

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

// Check that the array of variable offsets will not overflow. We do this by 
// checking that all array offsets are within range. The variable offset array
// is the same length as the byte code array.
// This allows us to check for overflow (or underflow) once instead of checking
// during each calculation in the array.
//
//   vararraylen = The length of the variable array.
//   varoffsetslen = The length of the variable offset array.
//   varoffsetsarray = The array of variable offsets.
//   Return = 0 if OK, else 1.
int checkvaroffsets(unsigned int vararraylen, unsigned int varoffsetslen, unsigned int *varoffsetsarray) {

	unsigned int i;

	for (i = 0; i < varoffsetslen; i++) {
		if (varoffsetsarray[i] >= varoffsetslen) {
			return 1;
		}
	}

	// No errors were found.
	return 0;

}

/*--------------------------------------------------------------------------- */


// The wrapper to the underlying C function 
static PyObject *py_acalcvm(PyObject *self, PyObject *args, PyObject *keywds) {

	// The arrays of data we work on. 
	union dataarrays data, dataout, codearray, varoffsetsarray, vararray, 
			constarray, vmstackarray;

	// The buffers are arrays of bytes.
	Py_buffer datapy, dataoutpy, codearraypy, varoffsetsarraypy, vararraypy, 
			constarraypy, vmstackpy;

	// The length of the interpreter control arrays.
	Py_ssize_t codearraylen;
	unsigned int codearraysize, vmstacksize, vmstacksegments;


	// How long the array is.
	Py_ssize_t arraylength;
	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;


	// This is used to hold the results from inspecting the Python args.
	struct args_param argtypes;


	// The error code returned by the function.
	signed int resultcode;
	// The result of the stack check.
	signed int stackerror;

	// Codes indicating the type of array.
	char datarraycode;
	// If true, *disabled* overflow checking.
	unsigned int disableovfl = 0;


	// -------------------------------------------------------------------------



	// Check the parameters to see what they are.
	argtypes = parsepyargs_parm(args, keywds);


	// There was an error reading the parameter types.
	if (argtypes.error) {
		ErrMsgParameterError();
		return NULL;
	}


	// Check the data array types are consistent.
	if ((argtypes.dataarraytype != argtypes.dataoutarraytype) || 
		(argtypes.dataarraytype != argtypes.vararraytype) ||
		(argtypes.dataarraytype != argtypes.constarraytype) ||
		(argtypes.dataarraytype != argtypes.stackarraytype)) {
		ErrMsgArrayTypeMismatch();
		return NULL;
	}


	// Check that the code array and variable offset arrays are the correct type.
	if ((argtypes.codearraytype != argtypes.varoffsetarraytype) || (argtypes.codearraytype != 'I')) {
		ErrMsgArrayTypeMismatch();
		return NULL;
	}


	// The item code tells us what data type we are handling.
	datarraycode = argtypes.dataarraytype;



	// Now we will fetch the actual data.
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "y*y*y*y*y*y*y*i|in:acalcvm", kwlist, 
			&codearraypy, &varoffsetsarraypy, &vararraypy, &constarraypy, &vmstackpy, 
			&datapy, &dataoutpy, &vmstacksegments, &disableovfl, &arraymaxlen)) {
		return NULL;
	}



	// Assign the buffer to a union which lets us get at them as typed data.
	data.buf = datapy.buf;
	dataout.buf = dataoutpy.buf;
	codearray.buf = codearraypy.buf;
	varoffsetsarray.buf = varoffsetsarraypy.buf;
	vararray.buf = vararraypy.buf;
	constarray.buf = constarraypy.buf;
	vmstackarray.buf = vmstackpy.buf;




	// The length of the data array.
	arraylength = calcarraylength(datarraycode, datapy.len);
	if (arraylength < 1) {
		// Release the buffers. 
		releasebuffers(&datapy, &dataoutpy, &codearraypy, &varoffsetsarraypy, 
					&vararraypy, &constarraypy, &vmstackpy);
		ErrMsgArrayLengthErr();
		return NULL;
	}



	// Check to make sure the input and output arrays are of equal length.
	if (datapy.len != dataoutpy.len) {
		// Release the buffers. 
		releasebuffers(&datapy, &dataoutpy, &codearraypy, &varoffsetsarraypy, 
					&vararraypy, &constarraypy, &vmstackpy);
		return NULL;
	}

	// Check the interpreter arrays for length.
	codearraylen = calcarraylength('I', codearraypy.len);
	if (codearraylen < 1) {
		// Release the buffers. 
		releasebuffers(&datapy, &dataoutpy, &codearraypy, &varoffsetsarraypy, 
					&vararraypy, &constarraypy, &vmstackpy);
		ErrMsgArrayLengthErr();
		return NULL;
	}


	// Check to make sure the interpreter control arrays are of equal length.
	if ((codearraylen != calcarraylength('I', varoffsetsarraypy.len)) || 
			(codearraylen != calcarraylength(datarraycode, constarraypy.len))) {
		// Release the buffers. 
		releasebuffers(&datapy, &dataoutpy, &codearraypy, &varoffsetsarraypy, 
					&vararraypy, &constarraypy, &vmstackpy);
		ErrMsgArrayLengthMismatch();
		return NULL;
	}



	// Check the op code array to see if the program will cause a stack overflow.
	vmstacksize = ((int) calcarraylength(datarraycode, vmstackpy.len)) / vmstacksegments;
	stackerror = checkstackerror(datarraycode, vmstacksize, codearray.I, (int) codearraylen);
	if (stackerror) {
		// Release the buffers. 
		releasebuffers(&datapy, &dataoutpy, &codearraypy, &varoffsetsarraypy, 
					&vararraypy, &constarraypy, &vmstackpy);

		if (stackerror == CALC_ERR_STACKOVFL_ERR) {
			ErrMsgACalcStackOverflow();
		} else {
			ErrMsgACalcUnknownOpCode();
		}
		return NULL;
	}



	// Check the var offset array to see if the program will cause a array overflow.
	if (checkvaroffsets((unsigned int) calcarraylength(datarraycode, vararraypy.len), 
			(unsigned int) calcarraylength('I', varoffsetsarraypy.len), varoffsetsarray.I)) {
		// Release the buffers. 
		releasebuffers(&datapy, &dataoutpy, &codearraypy, &varoffsetsarraypy, 
					&vararraypy, &constarraypy, &vmstackpy);

		ErrMsgACalcVarOffsetOverflow();
		return NULL;
	}



	// Adjust the length of array being operated on, if necessary.
	arraylength = adjustarraymaxlen(arraylength, arraymaxlen);

	codearraysize = (unsigned int) codearraylen;



	// Call the C function 
	switch(datarraycode) {
		// signed char
		case 'b' : {
			resultcode = exequation_signed_char(arraylength, data.b, dataout.b, 
						codearraysize, codearray.I, 
						varoffsetsarray.I, vararray.b, constarray.b,
						vmstackarray.b, vmstacksize, vmstacksegments, disableovfl);
			break;
		}
		// unsigned char
		case 'B' : {
			resultcode = exequation_unsigned_char(arraylength, data.B, dataout.B, 
						codearraysize, codearray.I, 
						varoffsetsarray.I, vararray.B, constarray.B,
						vmstackarray.B, vmstacksize, vmstacksegments, disableovfl);
			break;
		}
		// signed short
		case 'h' : {
			resultcode = exequation_signed_short(arraylength, data.h, dataout.h, 
						codearraysize, codearray.I, 
						varoffsetsarray.I, vararray.h, constarray.h,
						vmstackarray.h, vmstacksize, vmstacksegments, disableovfl);
			break;
		}
		// unsigned short
		case 'H' : {
			resultcode = exequation_unsigned_short(arraylength, data.H, dataout.H, 
						codearraysize, codearray.I, 
						varoffsetsarray.I, vararray.H, constarray.H,
						vmstackarray.H, vmstacksize, vmstacksegments, disableovfl);
			break;
		}
		// signed int
		case 'i' : {
			resultcode = exequation_signed_int(arraylength, data.i, dataout.i, 
						codearraysize, codearray.I, 
						varoffsetsarray.I, vararray.i, constarray.i,
						vmstackarray.i, vmstacksize, vmstacksegments, disableovfl);
			break;
		}
		// unsigned int
		case 'I' : {
			resultcode = exequation_unsigned_int(arraylength, data.I, dataout.I, 
						codearraysize, codearray.I, 
						varoffsetsarray.I, vararray.I, constarray.I,
						vmstackarray.I, vmstacksize, vmstacksegments, disableovfl);
			break;
		}
		// signed long
		case 'l' : {
			resultcode = exequation_signed_long(arraylength, data.l, dataout.l, 
						codearraysize, codearray.I, 
						varoffsetsarray.I, vararray.l, constarray.l,
						vmstackarray.l, vmstacksize, vmstacksegments, disableovfl);
			break;
		}
		// unsigned long
		case 'L' : {
			resultcode = exequation_unsigned_long(arraylength, data.L, dataout.L, 
						codearraysize, codearray.I, 
						varoffsetsarray.I, vararray.L, constarray.L,
						vmstackarray.L, vmstacksize, vmstacksegments, disableovfl);
			break;
		}
		// signed long long
		case 'q' : {
			resultcode = exequation_signed_long_long(arraylength, data.q, dataout.q, 
						codearraysize, codearray.I, 
						varoffsetsarray.I, vararray.q, constarray.q,
						vmstackarray.q, vmstacksize, vmstacksegments, disableovfl);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultcode = exequation_unsigned_long_long(arraylength, data.Q, dataout.Q, 
						codearraysize, codearray.I, 
						varoffsetsarray.I, vararray.Q, constarray.Q,
						vmstackarray.Q, vmstacksize, vmstacksegments, disableovfl);
			break;
		}
		// float
		case 'f' : {
			resultcode = exequation_float(arraylength, data.f, dataout.f, 
						codearraysize, codearray.I, 
						varoffsetsarray.I, vararray.f, constarray.f,
						vmstackarray.f, vmstacksize, vmstacksegments, disableovfl);
			break;
		}
		// double
		case 'd' : {
			resultcode = exequation_double(arraylength, data.d, dataout.d, 
					codearraysize, codearray.I, 
					varoffsetsarray.I, vararray.d, constarray.d, 
					vmstackarray.d, vmstacksize, vmstacksegments, disableovfl);
			break;
		}
		// We don't know this code.
		default: {
			// Release the buffers. 
			releasebuffers(&datapy, &dataoutpy, &codearraypy, &varoffsetsarraypy, 
						&vararraypy, &constarraypy, &vmstackpy);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}




	// Release the buffers. 
	releasebuffers(&datapy, &dataoutpy, &codearraypy, &varoffsetsarraypy, 
				&vararraypy, &constarraypy, &vmstackpy);



	// Signal the errors.
	switch (resultcode) {
		case CALC_ERR_INVALIDOP : {
			ErrMsgACalcInvalidOpTypeArray();
			return NULL;
		}
		case CALC_ERR_OVFL : {
			ErrMsgArithOverflowCalc();
			return NULL;
		}
		case CALC_ERR_STACKOVFL_ERR : {
			ErrMsgACalcStackOverflow();
		}
		case CALC_ERR_UNKNOWNOP : {
			ErrMsgACalcUnknownOpCode();
		}
		case CALC_ERR_ARITHMETIC: {
			ErrMsgArithOverflowCalc();
			return NULL;
		}
		case CALC_ERR_PLATFORM : {
			ErrMsgOperatorNotValidforthisPlatform();
			return NULL;
		}
	}



	// Return NONE. This indicates no exception.
	Py_RETURN_NONE;


}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(acalcvm__doc__,
"Arraycalc calculates numerical equations across an array. This module is  \n\
intended to be called by the compiler class and not called directly by the \n\
user. \n\
\n\
arraycalc.acalcvm(codearray, varoffsetarray, vararray, constarray, vmstack, \n\
                 dataarray, dataoutarray, vmstacksegments, disovfl=False) \n\
\n\
* codearray - array.array('I') - The executable byte codes.\n\
* varoffsetarray - array.array('I') - The offsets pointing to the variable \n\
                    array.\n\
* vararray - array.array - This stores the variables. \n\
* constarray - array.array - This stores the constants. \n\
* vmstack - array.array - The interpreter stack. \n\
* dataarray - The input data array to be examined.\n\
* dataoutarray - The output array.\n\
* vmstacksegments - integer - The number of array elements to work on at \n\
                    each time. \n\
* disovfl - If this keyword parameter is True, integer overflow checking \n\
  will be disabled. This is an optional parameter. \n\
\n\
The arrays vararray, constarray, vmstack, dataarray, and dataoutarray must \n\
all be of the same array type. Dataarray and dataoutarray must be the same \n\
length. Codearray, constarray, and varoffsetarray must be the same length. \n\
Vararray must be long enough to hold all the variables. Vmstack must be \n\
long enough to not overflow, multiplied by vmstacksegments. ");

/* A list of all the methods defined by this module. 
 "acalcvm" is the name seen inside of Python. 
 "py_acalcvm" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef acalcvm_methods[] = {
	{"acalcvm",  (PyCFunction) py_acalcvm, METH_VARARGS | METH_KEYWORDS, acalcvm__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef acalcvmmodule = {
    PyModuleDef_HEAD_INIT,
    "acalcvm",
    NULL,
    -1,
    acalcvm_methods
};

PyMODINIT_FUNC PyInit_acalcvm(void)
{
    return PyModule_Create(&acalcvmmodule);
};

/*--------------------------------------------------------------------------- */
