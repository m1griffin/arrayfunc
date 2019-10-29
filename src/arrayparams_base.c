//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_base.c
// Purpose:  Common functions for arrayfunc.
// Language: C
// Date:     28-Nov-2017
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

#include "Python.h"

#include <string.h>
#include <limits.h>
#include <float.h>

#include "arrayerrs.h"

#include "arrayparams_base.h"

/*--------------------------------------------------------------------------- */


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

	strcat(strcpy(formatstr, basestr), funcname);
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
char isunsignedcharrange(unsigned long long x) {
	return (x <= UCHAR_MAX);
}

// Returns true if the parameter is within the correct range for an unsigned short.
// H
char isunsignedshortrange(unsigned long long x) {
	return (x <= USHRT_MAX);
}

// Returns true if the parameter is within the correct range for an unsigned int.
// I
char isunsignedintrange(unsigned long long x) {
	return (x <= UINT_MAX);
}

// Returns true if the parameter is within the correct range for an unsigned long.
// L
char isunsignedlongrange(unsigned long long x) {
	return (x <= ULONG_MAX);
}



// Returns true if the parameter is within the correct range for a float (single).
// f
char isfloatrange(double x) {
	// Have to check for non-finite values explicitly as these won't be 
	// covered by normal compare operations.
	if (isnan(x) || (isinf(x) != 0)) { return 1; }

	return ((x <= FLT_MAX) && (x >= -FLT_MAX));
}

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */


/* Take a single python parameter object and get the data. This could be an
   integer, float, or array.
   
   dataobj = A parameter as a PyObject (not parsed).
   paramobjdata = A structure which will be used to return the data extracted
     from dataobj. Different fields will be valid depending on what the type of
     data in dataobj was. 
   hasbuffer = If 1, a buffer handle was obtained and must be released. If 0,
     there is no buffer to be released (either not a buffer object, or was not
     obtained.
   paramoverflow = If non-zero, a parameter overflowed, otherwise OK.
   Returns 0 if OK, otherwise non-zero.

*/
int get_paramdata(PyObject *dataobj, struct paramsdata *paramobjdata, char *hasbuffer, char *paramoverflow) {

	// Used to track overflows in integer conversions.
	int intparamoverflow = 0;
	// temporary variables for parsing data.
	long long llintparam;
	unsigned long long ullintparam;
	char arraycode = 0;
	Py_buffer datapy;


	*hasbuffer = 0;
	*paramoverflow = 0;

	// Parameter is an array.
	if (PyObject_CheckBuffer(dataobj)) {
		// Check that this is actually an array and not some other buffer type.
		if (!isarrayobjtype(dataobj)) {
			paramobjdata->paramtype = paramobj_error;
			return -1;
		}

		// Not entirely sure if PyBUF_ND is the correct flag.
		if (PyObject_GetBuffer(dataobj, &datapy, PyBUF_ND)) {
			paramobjdata->paramtype = paramobj_error;
			return -1;
		}

		paramobjdata->pybuffer = datapy;

		arraycode = lookuparraycode(dataobj);
		if (arraycode) {
			paramobjdata->paramtype = paramobj_array;
			paramobjdata->arraycode = arraycode;
			paramobjdata->array.buf = datapy.buf;
			*hasbuffer = 1;
			return 0;
		} else {
			paramobjdata->paramtype = paramobj_error;
			PyBuffer_Release(&paramobjdata->pybuffer);
			*hasbuffer = 0;
			return -1;
		}

	// Not an array, so expect a number.
	} else {
		// Parameter is an integer.
		if (PyLong_Check(dataobj)) {
			// Check if a signed long long.
			llintparam = PyLong_AsLongLongAndOverflow(dataobj, &intparamoverflow);
			// No overflow, so we can treat it as a signed long long.
			if (!intparamoverflow) {
				paramobjdata->llintparam = llintparam;
				paramobjdata->paramtype = paramobj_int;
				return 0;

			// If it overflowed, it could be an unsigned long long.
			} else {
				ullintparam = PyLong_AsUnsignedLongLong(dataobj);

				// An overflow happened. The integer is too large to represent
				// as a native integer.
				if ((ullintparam == (unsigned long long)-1) && PyErr_Occurred()) {
					paramobjdata->paramtype = paramobj_error;
					*paramoverflow = 1;
					return -1;
				}

				paramobjdata->ullintparam = ullintparam;
				paramobjdata->paramtype = paramobj_uint;
				return 0;
			}

		// Parameter is expected to be a float.
		} else {
			if (PyFloat_Check(dataobj)) {
				paramobjdata->dparam = PyFloat_AS_DOUBLE(dataobj);
				paramobjdata->paramtype = paramobj_float;
				return 0;

			// Error - unknown object type.
			} else {
				paramobjdata->paramtype = paramobj_error;
				return -1;
			}
		}
	}

	// If we reach this point, something has gone wrong.
	return -2;
}


/*--------------------------------------------------------------------------- */

/* Extract the numeric parameter data and check it for range.
 * arraycode = The array code for the associated array from the other
 *    parameter. The type of numeric parameter is expected to be compatible
 *    with this.
 * paramobjdata = Contains values and information about the numeric parameter
 *    we want to analyse.
 * checkedvalue = The output value cast to the correct numeric type.
 * paramoverflow = If non-zero, a parameter overflowed, otherwise OK.
 * Returns = Zero if OK, otherwise indicates an error.
*/
char get_numericparams(char arraycode, struct paramsdata *paramobjdata,
			struct paramsvals *checkedvalue, char *paramoverflow) {

	unsigned long long intparam;

	*paramoverflow = 0;

	// Make sure it is a numeric type.
	if ((paramobjdata->paramtype != paramobj_int) && 
		(paramobjdata->paramtype != paramobj_uint) &&
		 (paramobjdata->paramtype != paramobj_float))  { return -2; }


	// Is it a float?
	if (paramobjdata->paramtype == paramobj_float) {
		// Double precision float.
		if (arraycode == 'd') {
			// We can't check for overflow as this is the largest floating
			// point type we have.
			checkedvalue->d = (double) paramobjdata->dparam;
			return 0;
		}
		// Single precision float.
		if (arraycode == 'f') {
			// Overflow.
			if (!isfloatrange(paramobjdata->dparam))  { 
				*paramoverflow = 1;
				return -1; 
			}
			checkedvalue->f = (float) paramobjdata->dparam;
			return 0;
		}
		// Array code doesn't match numeric type.
		return -2;
	}
		

	// We are assuming that in checking the parameter previously we first tried
	// to make it a signed integer, but if the largest signed integer could
	// not contain it we tried to make it an unsiged integer.


	// Is it a signed integer?
	if (strchr("bhilq", arraycode) != NULL) {
		// Check if signed int data. This could also be the case if the
		// integer was too large for the largest signed integer type.
		if (paramobjdata->paramtype != paramobj_int) { 
			*paramoverflow = 1;
			return -2; 
		}

		switch(arraycode) {
			// signed char
			case 'b' : {
				// Overflow.
				if (!issignedcharrange(paramobjdata->llintparam))  { 
					*paramoverflow = 1;
					return -1; 
				}
				checkedvalue->b = (signed char) paramobjdata->llintparam;
				return 0;
			}
			// signed short
			case 'h' : {
				// Overflow.
				if (!issignedshortrange(paramobjdata->llintparam))  { 
					*paramoverflow = 1;
					return -1; 
				}
				checkedvalue->h = (signed short) paramobjdata->llintparam;
				return 0;
			}
			// signed int
			case 'i' : {
				// Overflow.
				if (!issignedintrange(paramobjdata->llintparam))  { 
					*paramoverflow = 1;
					return -1; 
				}
				checkedvalue->i = (signed int) paramobjdata->llintparam;
				return 0;
			}
			// signed long
			case 'l' : {
				// Overflow.
				if (!issignedlongrange(paramobjdata->llintparam))  { 
					*paramoverflow = 1;
					return -1; 
				}
				checkedvalue->l = (signed long) paramobjdata->llintparam;
				return 0;
			}
			// signed long long
			case 'q' : {
				// We can't check for overflow as this is the largest signed
				// integer type we have.
				checkedvalue->q = (signed long long) paramobjdata->llintparam;
				return 0;
			}
			// An unknown array type has been encountered.
			default : { return -2; }
		}
		
	}


	// Unsigned integer.
	if (strchr("BHILQ", arraycode) != NULL) {
		// The original values could have been in either the unsigned or 
		// signed range.
		if (!(paramobjdata->paramtype == paramobj_uint) && 
			!(paramobjdata->paramtype == paramobj_int)) { return -2; }

		// It was in the signed data range, so convert to unsigned type.
		if (paramobjdata->paramtype == paramobj_int) {
			intparam = (unsigned long long) paramobjdata->llintparam;
		} else {
			intparam = paramobjdata->ullintparam;
		}
			
		// We now have the integer value in the expected unsigned type and
		// it must be in valid range.
		
		switch(arraycode) {
			// unsigned char
			case 'B' : {
				// Overflow.
				if (!isunsignedcharrange(intparam))  { 
					*paramoverflow = 1;
					return -1; 
				}
				checkedvalue->B = (signed char) intparam;
				return 0;
			}
			// unsigned short
			case 'H' : {
				// Overflow.
				if (!isunsignedshortrange(intparam))  { 
					*paramoverflow = 1;
					return -1; 
				}
				checkedvalue->H = (signed short) intparam;
				return 0;
			}
			// unsigned int
			case 'I' : {
				// Overflow.
				if (!isunsignedintrange(intparam))  { 
					*paramoverflow = 1;
					return -1; 
				}
				checkedvalue->I = (signed int) intparam;
				return 0;
			}
			// unsigned long
			case 'L' : {
				// Overflow.
				if (!isunsignedlongrange(intparam))  { 
					*paramoverflow = 1;
					return -1; 
				}
				checkedvalue->L = (signed long) intparam;
				return 0;
			}
			// unsigned long long
			case 'Q' : {
				// We can't check for overflow as this is the largest signed
				// integer type we have.
				checkedvalue->Q = (signed long long) intparam;
				return 0;
			}
			// An unknown array type has been encountered.
			default : { return -2; }
		}

	} 


	// We should never reach here unless there has been a programming error.
	return -2;


}

/*--------------------------------------------------------------------------- */

// This is the same as get_paramdata, but without the paramoverflow parameter.
int get_paramdata_simple(PyObject *dataobj, struct paramsdata *paramobjdata, char *hasbuffer) {

	char paramoverflow = 0;

	return get_paramdata(dataobj, paramobjdata, hasbuffer, &paramoverflow);

}


/*--------------------------------------------------------------------------- */

// This is the same as get_numericparams, but without the paramoverflow parameter.
char get_numericparams_simple(char arraycode, struct paramsdata *paramobjdata,
			struct paramsvals *checkedvalue) {

	char paramoverflow = 0;

	return get_numericparams(arraycode, paramobjdata, checkedvalue, &paramoverflow);

}

/*--------------------------------------------------------------------------- */
