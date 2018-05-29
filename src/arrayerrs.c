//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayerrs.h
// Purpose:  Common error definitions.
// Language: C
// Date:     03-Nov-2014
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

/*--------------------------------------------------------------------------- */

// The following functions are used to provide standardized error messages. 

// Standard messages. 
void ErrMsgArithCalc(void) {
	PyErr_SetString(PyExc_ArithmeticError, "arithmetic error in calculation.");
}

void ErrMsgZeroDiv(void) {
	PyErr_SetString(PyExc_ZeroDivisionError, "zero division error in calculation.");
}

void ErrMsgArrayLengthErr(void) {
	PyErr_SetString(PyExc_IndexError, "array length error.");
}

void ErrMsgArrayLengthMismatch(void) {
	PyErr_SetString(PyExc_IndexError, "array length mismatch.");
}

void ErrMsgArithOverflowCalc(void) {
	PyErr_SetString(PyExc_OverflowError, "arithmetic overflow in calculation.");
}

void ErrMsgArithOverflowParam(void) {
	PyErr_SetString(PyExc_OverflowError, "arithmetic overflow in parameter.");
}

void ErrMsgArrayAndParamMismatch(void) {
	PyErr_SetString(PyExc_TypeError, "array and parameter type mismatch.");
}

void ErrMsgArrayTypeMismatch(void) {
	PyErr_SetString(PyExc_TypeError, "array type mismatch.");
}

void ErrMsgUnknownArrayType(void) {
	PyErr_SetString(PyExc_TypeError, "unknown array type.");
}

void ErrMsgTypeExpectFloat(void) {
	PyErr_SetString(PyExc_TypeError, "requires float or double data parameters.");
}

void ErrMsgTypeExpectInt(void) {
	PyErr_SetString(PyExc_TypeError, "requires integer data parameters.");
}

void ErrMsgArrayExpected(void) {
	PyErr_SetString(PyExc_TypeError, "array.array expected.");
}

void ErrMsgOperatorNotValidforthisFunction(void) {
	PyErr_SetString(PyExc_ValueError, "operator not valid for this function.");
}

void ErrMsgOperatorNotValidforthisPlatform(void) {
	PyErr_SetString(PyExc_ValueError, "operator not valid for this platform.");
}

void ErrMsgParameterError(void) {
	PyErr_SetString(PyExc_TypeError, "parameter error.");
}

void ErrMsgParameterMissing(void) {
	PyErr_SetString(PyExc_TypeError, "parameter missing.");
}

void ErrMsgParameterNotValidforthisOperation(void) {
	PyErr_SetString(PyExc_ValueError, "parameter not valid for this operation.");
}



// Used for compress.
void ErrMsgArrayLengthInput(void) {
	PyErr_SetString(PyExc_IndexError, "input array length error.");
}

void ErrMsgArrayLengthOutput(void) {
	PyErr_SetString(PyExc_IndexError, "output length error.");
}

void ErrMsgArrayLengthSelector(void) {
	PyErr_SetString(PyExc_IndexError, "selector length error.");
}


// Used for convert.
void ErrMsgConversionNotValidforthisType(void) {
	PyErr_SetString(PyExc_ValueError, "conversion not valid for this type.");
}

void ErrMsgNaNError(void) {
	PyErr_SetString(PyExc_ValueError, "cannot convert float NaN to integer.");
}


// Used for findindices. 
void ErrMsgOutputArrayTypeInvalid(void) {
	PyErr_SetString(PyExc_TypeError, "output array type invalid.");
}


/*--------------------------------------------------------------------------- */

