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
	PyErr_SetString(PyExc_ArithmeticError, "Arithmetic error in calculation.");
}

void ErrMsgArrayLengthErr(void) {
	PyErr_SetString(PyExc_IndexError, "Array length error.");
}

void ErrMsgArrayLengthMismatch(void) {
	PyErr_SetString(PyExc_IndexError, "Array length mismatch.");
}

void ErrMsgArithOverflowCalc(void) {
	PyErr_SetString(PyExc_OverflowError, "Arithmetic overflow in calculation.");
}

void ErrMsgArithOverflowParam(void) {
	PyErr_SetString(PyExc_OverflowError, "Arithmetic overflow in parameter.");
}

void ErrMsgArrayAndParamMismatch(void) {
	PyErr_SetString(PyExc_TypeError, "Array and parameter type mismatch.");
}

void ErrMsgArrayTypeMismatch(void) {
	PyErr_SetString(PyExc_TypeError, "Array type mismatch.");
}

void ErrMsgUnknownArrayType(void) {
	PyErr_SetString(PyExc_TypeError, "Unknown array type.");
}

void ErrMsgArrayorBytesExpected(void) {
	PyErr_SetString(PyExc_TypeError, "array.array or bytes expected.");
}

void ErrMsgOperatorNotValidforthisFunction(void) {
	PyErr_SetString(PyExc_ValueError, "Operator not valid for this function.");
}

void ErrMsgOperatorNotValidforthisPlatform(void) {
	PyErr_SetString(PyExc_ValueError, "Operator not valid for this platform.");
}

void ErrMsgParameterError(void) {
	PyErr_SetString(PyExc_TypeError, "Parameter error.");
}

void ErrMsgParameterMissing(void) {
	PyErr_SetString(PyExc_TypeError, "Parameter missing.");
}

void ErrMsgParameterNotValidforthisOperation(void) {
	PyErr_SetString(PyExc_ValueError, "Parameter not valid for this operation.");
}



// Used for compress.
void ErrMsgArrayLengthInput(void) {
	PyErr_SetString(PyExc_IndexError, "Input array length error.");
}

void ErrMsgArrayLengthOutput(void) {
	PyErr_SetString(PyExc_IndexError, "Output length error.");
}

void ErrMsgArrayLengthSelector(void) {
	PyErr_SetString(PyExc_IndexError, "Selector length error.");
}


// Used for convert.
void ErrMsgConversionNotValidforthisType(void) {
	PyErr_SetString(PyExc_ValueError, "Conversion not valid for this type.");
}

void ErrMsgNaNError(void) {
	PyErr_SetString(PyExc_ValueError, "Cannot convert float NaN to integer.");
}


// Used for findindices. 
void ErrMsgOutputArrayTypeInvalid(void) {
	PyErr_SetString(PyExc_TypeError, "Output array type invalid.");
}


// Used for arraylimits and arrayguardbands.
void ErrMsgSourceArrayNotFloat(void) {
	PyErr_SetString(PyExc_TypeError, "Source array code type is not a float or double.");
}

void ErrMsgUnknownDestinationArrayTypeCode(void) {
	PyErr_SetString(PyExc_TypeError, "Unknown destination array code type.");
}

void ErrMsgUknownDestinationCode(void) {
	PyErr_SetString(PyExc_TypeError, "Unknown destination itemcode.");
}

void ErrMsgUknownLimitType(void) {
	PyErr_SetString(PyExc_TypeError, "Unknown limit type.");
}

void ErrMsgUknownItemCode(void) {
	PyErr_SetString(PyExc_TypeError, "Unknown itemcode.");
}

void ErrMsgUknownSourceItemcode(void) {
	PyErr_SetString(PyExc_TypeError, "Unknown source itemcode.");
}


/*--------------------------------------------------------------------------- */

