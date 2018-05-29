//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_base.c
// Purpose:  Common functions for arrayfunc.
// Language: C
// Date:     28-Nov-2017
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2017    Michael Griffin    <m12.griffin@gmail.com>
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

#include "Python.h"

#include <string.h>
#include <limits.h>

#include "arrayerrs.h"

#include "arrayparams_base.h"


/*--------------------------------------------------------------------------- */

// Return true if the array code is an integer type.
char isintarraycode(char arraycode) {
	return (strchr("bBhHiIlLqQ", arraycode) != NULL);
}


// Return true if the array code is for a signed integer array.
char issignedintarraycode(char arraycode) {
	return (strchr("bhilq", arraycode) != NULL);
}


// Return true if the array code is a float type.
char isfloatarraycode(char arraycode) {
	return arraycode == 'f';
}

// Return true if the array code is an double type.
char isdoublearraycode(char arraycode) {
	return arraycode == 'd';
}


/*--------------------------------------------------------------------------- */

/* Determines if the Python object is an array.
 * dataobj = The object to be tested.
 * Returns TRUE if an array, otherwise returns FALSE.
*/
char isarrayobjtype(PyObject *dataobj) {

	if (dataobj == NULL) { return 0; }

	// Check if is an array.
	return (strcmp(dataobj->ob_type->tp_name, "array.array") == 0);

}


/*--------------------------------------------------------------------------- */
/* Returns the type code of an array object. 
 * dataobj = The array object to be tested.
 * Returns the array type code, or zero if error.
*/
char lookuparraycode(PyObject *dataobj) {

	PyObject *arraycodeobj;

	if (dataobj == NULL) { return 0; }

	// Check if is an array.
	if (!isarrayobjtype(dataobj)) { return 0; }

	arraycodeobj = PyObject_GetAttrString(dataobj, "typecode");

	// These are the array types we recognise.
	if (!PyUnicode_CompareWithASCIIString(arraycodeobj, "b")) { return 'b'; }
	if (!PyUnicode_CompareWithASCIIString(arraycodeobj, "B")) { return 'B'; }
	if (!PyUnicode_CompareWithASCIIString(arraycodeobj, "h")) { return 'h'; }
	if (!PyUnicode_CompareWithASCIIString(arraycodeobj, "H")) { return 'H'; }
	if (!PyUnicode_CompareWithASCIIString(arraycodeobj, "i")) { return 'i'; }
	if (!PyUnicode_CompareWithASCIIString(arraycodeobj, "I")) { return 'I'; }
	if (!PyUnicode_CompareWithASCIIString(arraycodeobj, "l")) { return 'l'; }
	if (!PyUnicode_CompareWithASCIIString(arraycodeobj, "L")) { return 'L'; }
	if (!PyUnicode_CompareWithASCIIString(arraycodeobj, "q")) { return 'q'; }
	if (!PyUnicode_CompareWithASCIIString(arraycodeobj, "Q")) { return 'Q'; }
	if (!PyUnicode_CompareWithASCIIString(arraycodeobj, "f")) { return 'f'; }
	if (!PyUnicode_CompareWithASCIIString(arraycodeobj, "d")) { return 'd'; }

	// We didn't find anything.
	return 0;

}


/*--------------------------------------------------------------------------- */


/* Determines if the Python object is an integer array.
 * dataobj = The object to be tested.
 * Returns TRUE if an integer array, otherwise returns FALSE.
*/
char isintarrayobjtype(PyObject *dataobj) {

	if (dataobj == NULL) { return 0; }

	// Check if is an array.
	if (!isarrayobjtype(dataobj)) { return 0; }

	return isintarraycode(lookuparraycode(dataobj));

}


/* Determines if the Python object is a float array (array code 'f'). 
 * dataobj = The object to be tested.
 * Returns TRUE if a Python float array, otherwise returns FALSE.
*/
char isfloatarrayobjtype(PyObject *dataobj) {

	if (dataobj == NULL) { return 0; }

	// Check if is an array.
	if (!isarrayobjtype(dataobj)) { return 0; }

	return isfloatarraycode(lookuparraycode(dataobj));

}



/* Determines if the Python object is a double array (array code 'd'). 
 * dataobj = The object to be tested.
 * Returns TRUE if a Python double array, otherwise returns FALSE.
*/
char isdoublearrayobjtype(PyObject *dataobj) {

	if (dataobj == NULL) { return 0; }

	// Check if is an array.
	if (!isarrayobjtype(dataobj)) { return 0; }

	return isdoublearraycode(lookuparraycode(dataobj));

}



/* Determines if the Python object is an integer.
 * dataobj = The object to be tested.
 * Returns TRUE if an integer, otherwise returns FALSE.
*/
char isintobjtype(PyObject *dataobj) {

	if (dataobj == NULL) { return 0; }

	// Check if is an int.
	return (strcmp(dataobj->ob_type->tp_name, "int") == 0);

}


/* Determines if the Python object is a float.
 * dataobj = The object to be tested.
 * Returns TRUE if a float, otherwise returns FALSE.
*/
char isfloatobjtype(PyObject *dataobj) {

	if (dataobj == NULL) { return 0; }

	// Check if is a float.
	return (strcmp(dataobj->ob_type->tp_name, "float") == 0);

}


/* Determines if the Python object is null. This will indicate that no
 * 	parameter was provided.
 * dataobj = The object to be tested.
 * Returns TRUE if a float, otherwise returns FALSE.
*/
char isnullobjtype(PyObject *dataobj) {

	// Check if is null.
	return (dataobj == NULL);

}


/* Determines if the Python object is an integer or float type.
 * dataobj = The object to be tested.
 * Returns TRUE if the queried type, otherwise returns FALSE.
*/
char isnumberobjcat(PyObject *dataobj) {

	if (dataobj == NULL) { return 0; }

	// Check if is an integer or float.
	return (isintobjtype(dataobj) || isfloatobjtype(dataobj));

}


/*--------------------------------------------------------------------------- */



/*--------------------------------------------------------------------------- */

/* 	Calculate the number of data array elements from the buffer length and the
	specified array type.
	itemcode = The code specifying the array type.
	bufferlength = The number of bytes in the buffer.
	Returns = The number of array elements, or zero if error.
 */
Py_ssize_t calcarraylength(char itemcode, Py_ssize_t bufferlength) {
	switch(itemcode) {
		// signed char
		case 'b' : {
			return bufferlength / sizeof(signed char);
		}
		// unsigned char
		case 'B' : {
			return bufferlength / sizeof(unsigned char);
		}
		// signed short
		case 'h' : {
			return bufferlength / sizeof(signed short);
		}
		// unsigned short
		case 'H' : {
			return bufferlength / sizeof(unsigned short);
		}
		// signed int
		case 'i' : {
			return bufferlength / sizeof(signed int);
		}
		// unsigned int
		case 'I' : {
			return bufferlength / sizeof(unsigned int);
		}
		// signed long
		case 'l' : {
			return bufferlength / sizeof(signed long);
		}
		// unsigned long
		case 'L' : {
			return bufferlength / sizeof(unsigned long);
		}
		// signed long long
		case 'q' : {
			return bufferlength / sizeof(signed long long);
		}
		// unsigned long long
		case 'Q' : {
			return bufferlength / sizeof(unsigned long long);
		}
		// float
		case 'f' : {
			return bufferlength / sizeof(float);
		}
		// double
		case 'd' : {
			return bufferlength / sizeof(double);
		}
	}

	return 0;
}

/*--------------------------------------------------------------------------- */


/* Determines whether to iterate over the entire length of the array, or if
   only part of the array is to be used. If for example an array which was
   filtered as part of a previous step is to be operated on, only part of the
   array may contain valid data.
*/
Py_ssize_t adjustarraymaxlen(Py_ssize_t arraylength, Py_ssize_t arraymaxlen) {
	if ((arraymaxlen > 0) && (arraymaxlen < arraylength)) {
		return arraymaxlen;
	} else {
		return arraylength;
	}
}


/*--------------------------------------------------------------------------- */

/* Create the format string from two substrings, one the base format and one
 * with the name of the C extension.
 * basestr = The first part of the desired format string.
 * funcname = The name of the function to be added to the end.
 * formatstr = The output string.
 * Assert: The lengths of basestr and funcname are less than the size of formatstr.
*/
void makefmtstr(char *basestr, char *funcname, char *formatstr) {

	// Make sure there won't be a string overflow. While the sizes are fixed,
	// we could have a programming error.
	assert((strlen(basestr) + strlen(funcname)) < FMTSTRLEN);

	strcpy(formatstr, basestr);
	strncat(formatstr, funcname, strlen(funcname));

}

/*--------------------------------------------------------------------------- */


// We need to check this to deal with some peculiarities of the format codes
// used by PyArg_ParseTuple.

// Returns true if the parameter is within the correct range for a signed char.
// b
char issignedcharrange(signed long long x) {
	return ((x <= SCHAR_MAX) && (x >= SCHAR_MIN));
}

// Returns true if the parameter is within the correct range for a signed short.
// h
char issignedshortrange(signed long long x) {
	return ((x <= SHRT_MAX) && (x >= SHRT_MIN));
}

// Returns true if the parameter is within the correct range for a signed int.
// i
char issignedintrange(signed long long x) {
	return ((x <= INT_MAX) && (x >= INT_MIN));
}

// Returns true if the parameter is within the correct range for a signed long.
// l
char issignedlongrange(signed long long x) {
	return ((x <= LONG_MAX) && (x >= LONG_MIN));
}



// Unsigned data is not checked for overflow by the PyArg_ParseTuple template 
// strings. This means we must use a larger data size and then check manually
// to see if it is withing the expected range.

// Returns true if the parameter is within the correct range for an unsigned char.
// B
char isunsignedcharrange(signed long long x) {
	return ((x <= UCHAR_MAX) && (x >= 0));
}

// Returns true if the parameter is within the correct range for an unsigned short.
// H
char isunsignedshortrange(signed long long x) {
	return ((x <= USHRT_MAX) && (x >= 0));
}

// Returns true if the parameter is within the correct range for an unsigned int.
// I
char isunsignedintrange(signed long long x) {
	return ((x <= UINT_MAX) && (x >= 0));
}


/*--------------------------------------------------------------------------- */


// Check the range of values for unsigned integer numeric paramters.
// PyArg_ParseTupleAndKeywords does not check unsigned integers for overflow,
// therefore we need to add checks for this after after parsing these numbers 
// into a larger signed variable (which does check for overflow). 
// We also check for signed integers while we are at it in order to reduce the
// number of format string parsing cases needed.
// We can check for array codes b, h, i, l, B, H, and I only. 
// Also see ischeckedintcode, as this tests if the array code is one which this 
// one tests.
//
// arraytype = The array code.
// param_q = The raw parameter as a signed integer.
// parampy = A union which stores all the possible types.
// returns true if OK, false if overflow.
char intparamrangeok(char arraytype, signed long long param_q, struct paramsvals *parampy) {

	// Check if the integer falls within the expected range for that array type.
	switch (arraytype) {
		case 'b': { if (!issignedcharrange(param_q)) { return 0; }
			parampy->b = (signed char) param_q;
			return 1;
			break;
			}
		case 'h': { if (!issignedshortrange(param_q)) { return 0; }
			parampy->h = (signed short) param_q;
			return 1;
			break;
			}
		case 'i': { if (!issignedintrange(param_q)) { return 0; }
			parampy->i = (signed int) param_q;
			return 1;
			break;
			}
		case 'l': { if (!issignedlongrange(param_q)) { return 0; }
			parampy->l = (signed long) param_q;
			return 1;
			break;
			}
		case 'B': { if (!isunsignedcharrange(param_q)) { return 0; }
			parampy->B = (unsigned char) param_q;
			return 1;
			break;
			}
		case 'H': { if (!isunsignedshortrange(param_q)) { return 0; }
			parampy->H = (unsigned short) param_q;
			return 1;
			break;
			}
		case 'I': { if (!isunsignedintrange(param_q)) { return 0; }
			parampy->I = (unsigned int) param_q;
			return 1;
			break;
			}
		default: { return 0; }
	}

}


// This function checks if intparamrangeok will check this parameter type.
char ischeckedintcode(char arraycode) {
	return (strchr("bhilBHI", arraycode) != NULL);
}

/*--------------------------------------------------------------------------- */
