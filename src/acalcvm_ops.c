//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   acalcvm_ops.h
// Purpose:  Common code for acalc.
// Language: C
// Date:     22-Jan-2016.
//
//------------------------------------------------------------------------------
//
//   Copyright 2016-2017    Michael Griffin    <m12.griffin@gmail.com>
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
// This must be defined before "Python.h" in order for the pointers in the
// argument parsing functions to work properly. 
#define PY_SSIZE_T_CLEAN

#include "Python.h"

/*--------------------------------------------------------------------------- */

// ACalc interpreter stack overflow or underflow.
void ErrMsgACalcStackOverflow(void) {
	PyErr_SetString(PyExc_ValueError, "ACalc vm stack overflow or underflow.");
}

// ACalc interpreter uknown op code.
void ErrMsgACalcUnknownOpCode(void) {
	PyErr_SetString(PyExc_ValueError, "ACalc vm uknown op code.");
}

// ACalc interpreter variable offset array overflow or underflow.
void ErrMsgACalcVarOffsetOverflow(void) {
	PyErr_SetString(PyExc_ValueError, "ACalc vm variable array overflow.");
}

// The operator is invalid for this array type.
void ErrMsgACalcInvalidOpTypeArray(void) {
	PyErr_SetString(PyExc_ValueError, "ACalc vm operator is invalid for array type.");
}

/*--------------------------------------------------------------------------- */
