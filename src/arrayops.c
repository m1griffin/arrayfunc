//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayops.c
// Purpose:  Compare parameter string decoding.
// Language: C
// Date:     28-May-2018
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
	if (!PyUnicode_CompareWithASCIIString(opstr, ">=")) return OP_AF_GE;
	if (!PyUnicode_CompareWithASCIIString(opstr, "<")) return OP_AF_LT;
	if (!PyUnicode_CompareWithASCIIString(opstr, "<=")) return OP_AF_LE;
	if (!PyUnicode_CompareWithASCIIString(opstr, "!=")) return OP_AF_NE;

	return -1;
}

//------------------------------------------------------------------------------

