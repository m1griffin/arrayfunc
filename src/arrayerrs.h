//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayerrs.h
// Purpose:  Common error definitions.
// Language: C
// Date:     06-May-2014
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

// No error
#define ARR_NO_ERR 0
// The operation requested is not valid for this function.
#define ARR_ERR_INVALIDOP -1
// An arithmetic overflow occurred during a calculation. 
#define ARR_ERR_OVFL -2
// Floating point error of any kind.
#define ARR_ERR_ARITHMETIC -3
// One or more missing optional parameters are required for this function. 
#define ARR_ERR_PARAMMISSING -4
// The item requested was not found.
#define ARR_ERR_NOTFOUND -5
// A value was invalid for the requested operation.
#define ARR_ERR_VALUE_ERR -6
// The operation requested is not valid for this platform.
#define ARR_ERR_PLATFORM -7
// Divide by zero error.
#define ARR_ERR_ZERODIV -8

/*--------------------------------------------------------------------------- */

// The following functions are used to provide standardized error messages. 

void ErrMsgArithCalc(void);
void ErrMsgZeroDiv(void);
void ErrMsgArrayLengthErr(void);
void ErrMsgArrayLengthMismatch(void);
void ErrMsgArithOverflowCalc(void);
void ErrMsgArithOverflowParam(void);
void ErrMsgArrayAndParamMismatch(void);
void ErrMsgArrayTypeMismatch(void);
void ErrMsgUnknownArrayType(void);
void ErrMsgTypeExpectFloat(void);
void ErrMsgTypeExpectInt(void);
void ErrMsgArrayExpected(void);
void ErrMsgOperatorNotValidforthisFunction(void);
void ErrMsgOperatorNotValidforthisPlatform(void);
void ErrMsgParameterError(void);
void ErrMsgParameterMissing(void);
void ErrMsgParameterNotValidforthisOperation(void);

void ErrMsgArrayLengthInput(void);
void ErrMsgArrayLengthOutput(void);
void ErrMsgArrayLengthSelector(void);

void ErrMsgConversionNotValidforthisType(void);
void ErrMsgNaNError(void);

void ErrMsgOutputArrayTypeInvalid(void);

/*--------------------------------------------------------------------------- */
