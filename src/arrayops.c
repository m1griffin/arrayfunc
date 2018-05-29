//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayops.c
// Purpose:  Functions for parsing parameters for functions which use compare
//            compare operations.
// Language: C
// Date:     28-May-2018
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

//------------------------------------------------------------------------------

#include "Python.h"

#include "arrayops.h"

//------------------------------------------------------------------------------


// Translate the command object to an integer.
// Parameters: opstr (PyObject) = The command string. 
// 	Returns: An integer corresponding to the decoded command. This will be
//		negative if there is no match.
signed int opstrdecode(PyObject *opstr) {

	if (!PyUnicode_CompareWithASCIIString(opstr, "==")) return OP_AF_EQ;
	if (!PyUnicode_CompareWithASCIIString(opstr, ">")) return OP_AF_GT;
	if (!PyUnicode_CompareWithASCIIString(opstr, ">=")) return OP_AF_GTE;
	if (!PyUnicode_CompareWithASCIIString(opstr, "<")) return OP_AF_LT;
	if (!PyUnicode_CompareWithASCIIString(opstr, "<=")) return OP_AF_LTE;
	if (!PyUnicode_CompareWithASCIIString(opstr, "!=")) return OP_AF_NE;

	return -1;
}

//------------------------------------------------------------------------------


/* Convert the parameter type name string to a parameter code.
 * paramobj = The parameter object. This is expected to be a Python integer
 * 			or float object.
 * Returns a character code.
 * 'i' = int, 'f' = float, 0 = unknown.
*/
char paramtypecode(PyObject *paramobj) {

	// Integer types (including long).
	if (strcmp(paramobj->ob_type->tp_name, "int") == 0) {
		return 'i';
	}

	// Floating point, including float or double.
	if (strcmp(paramobj->ob_type->tp_name, "float") == 0) {
		return 'f';
	}

	// We don't know what this is.
	return 0;

}

//------------------------------------------------------------------------------


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
