//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayfunc.c
// Purpose:  Common functions for arrayfunc.
// Language: C
// Date:     30-Apr-2014
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

#include "Python.h"

#include <string.h>
#include <limits.h>

#include "arrayfunc.h"

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

/* Compare the parameter type to the array type to see if they are compatible.
 * arraytype = The array type character code.
 * paramtype = The parameter code.
 * Returns True if OK.
*/
char paramcompatok(char arraytype, char paramtype) {

	// Most types require an integer.
	if (strchr("bBhHiIlLqQ", arraytype) != NULL) {
		return paramtype == 'i';
	}

	// Floating point.
	if (strchr("fd", arraytype) != NULL) {
		return paramtype == 'f';
	}

	return 0;

}

/*--------------------------------------------------------------------------- */


/* Concert the parameter type name string to a parameter code.
 * typename = The parameter type name string.
 * Returns a character code.
 * i = int, f = float, e = unknown.
*/
char paramtypecode(char const *typename) {

	// Integer types (including long).
	if (strcmp(typename, "int") == 0) {
		return 'i';
	}

	// Floating point, including float or double.
	if (strcmp(typename, "float") == 0) {
		return 'f';
	}


	// We don't know what this is.
	return 'e';

}

/*--------------------------------------------------------------------------- */
/* Returns the type code of an array object.
 * dataobj = The array object to be tested.
 * Returns the array type code, or zero if error.
*/
char getarraycode(PyObject *dataobj) {

	PyObject *arraycodeobj;

	if (dataobj == NULL) { return 0; }

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

/* Returns a struct with information about the array parameter.
 * dataobj = The array object to be tested.
 * Returns a struct indicating if the result was an array or bytes objectg, and 
 * 		if so, the array type code. Bytes ojbects are treated as if they were
 * 		arrays of type 'B'.
*/
struct arrayparamstypes paramarraytype(PyObject *dataobj) {

	// PyObject *arraycodeobj;
	char arraycode = 0;
	struct arrayparamstypes arrtype = {0, 0, ' '};

	if (dataobj == NULL) { return arrtype; }

	// Check if is an array.
	if (strcmp(dataobj->ob_type->tp_name, "array.array") == 0) {

		// Get the array type code letter.
		arraycode = getarraycode(dataobj);

		// Everything was OK.
		if (arraycode != 0) { 
			arrtype.ok = 1;
			arrtype.arraycode = arraycode;
			arrtype.isarray = 1;
			return arrtype;
		// We don't recognize the array code.
		} else {
			return arrtype; 
		}

	}


	// It wasn't an array, so check if it was a Python bytes object.
	// We treat byes objects as if they were unsigned chars.
	if (strcmp(dataobj->ob_type->tp_name, "bytes") == 0) {
		arrtype.ok = 1;
		arrtype.isarray = 1;
		arrtype.arraycode = 'B';
		return arrtype;
	}

	// If an array or bytes object was not detected above, then this 
	// will return as an error. 
	return arrtype;

}


/*--------------------------------------------------------------------------- */


/* Returns true if the parameter is within the correct range for a signed char.
   We need to check this to deal with some peculiarities of the format codes
   used by PyArg_ParseTuple.
*/
char issignedcharrange(signed long x) {
	return ((x <= SCHAR_MAX) && (x >= SCHAR_MIN));
}

// Returns true if the parameter is within the correct range for a signed short.
char issignedshortrange(signed long x) {
	return ((x <= SHRT_MAX) && (x >= SHRT_MIN));
}

// Returns true if the parameter is within the correct range for a signed int.
char issignedintrange(signed long x) {
	return ((x <= INT_MAX) && (x >= INT_MIN));
}


/* Unsigned data is not checked for overflow by the PyArg_ParseTuple template 
	strings. This means we must use a larger data size and then check manually
	to see if it is withing the expected range.
*/
// Returns true if the parameter is within the correct range for an unsigned char.
char isunsignedcharrange(signed long x) {
	return ((x <= UCHAR_MAX) && (x >= 0));
}

// Returns true if the parameter is within the correct range for an unsigned short.
char isunsignedshortrange(signed long x) {
	return ((x <= USHRT_MAX) && (x >= 0));
}

// Returns true if the parameter is within the correct range for an unsigned int.
char isunsignedintrange(signed long x) {
	return ((x <= UINT_MAX) && (x >= 0));
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
