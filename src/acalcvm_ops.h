//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   acalcvm_ops.c
// Purpose:  Common code for acalc.
// Language: C
// Date:     20-Jan-2016.
//
//------------------------------------------------------------------------------
//
//   Copyright 2015 - 2017    Michael Griffin    <m12.griffin@gmail.com>
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
#define CALC_NO_ERR 0
// The operation requested is not valid for this function.
#define CALC_ERR_INVALIDOP -1
// An arithmetic overflow occurred during a calculation. 
#define CALC_ERR_OVFL -2
// Floating point error of any kind.
#define CALC_ERR_ARITHMETIC -3
// Interpreter stack overflow or underflow.
#define CALC_ERR_STACKOVFL_ERR -4
// Uknown interpreter op code.
#define CALC_ERR_UNKNOWNOP -5
// The operation requested is not valid for this platform.
#define CALC_ERR_PLATFORM -7

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// These are the op codes for integer array types.
#define CALCOP_INT_UNKNOWN 0
#define CALCOP_INT_PUSHARRAY 1
#define CALCOP_INT_PUSHVAR 2
#define CALCOP_INT_PUSHCONST 3
#define CALCOP_INT_ADD 4
#define CALCOP_INT_SUB 5
#define CALCOP_INT_MULT 6
#define CALCOP_INT_DIV 7
#define CALCOP_INT_FLOORDIV 8
#define CALCOP_INT_MOD 9
#define CALCOP_INT_UADD 10
#define CALCOP_INT_USUB 11
#define CALCOP_INT_POW 12
#define CALCOP_INT_BITAND 13
#define CALCOP_INT_BITOR 14
#define CALCOP_INT_BITXOR 15
#define CALCOP_INT_INVERT 16
#define CALCOP_INT_LSHIFT 17
#define CALCOP_INT_RSHIFT 18
#define CALCOP_INT_ABS 19
#define CALCOP_INT_MATH_FACTORIAL 20


// These are the op codes for floating point array types.
#define CALCOP_FLOAT_UNKNOWN 0
#define CALCOP_FLOAT_PUSHARRAY 1
#define CALCOP_FLOAT_PUSHVAR 2
#define CALCOP_FLOAT_PUSHCONST 3
#define CALCOP_FLOAT_ADD 4
#define CALCOP_FLOAT_SUB 5
#define CALCOP_FLOAT_MULT 6
#define CALCOP_FLOAT_DIV 7
#define CALCOP_FLOAT_FLOORDIV 8
#define CALCOP_FLOAT_MOD 9
#define CALCOP_FLOAT_UADD 10
#define CALCOP_FLOAT_USUB 11
#define CALCOP_FLOAT_POW 12
#define CALCOP_FLOAT_ABS 13
#define CALCOP_FLOAT_MATH_ACOS 14
#define CALCOP_FLOAT_MATH_ACOSH 15
#define CALCOP_FLOAT_MATH_ASIN 16
#define CALCOP_FLOAT_MATH_ASINH 17
#define CALCOP_FLOAT_MATH_ATAN 18
#define CALCOP_FLOAT_MATH_ATAN2 19
#define CALCOP_FLOAT_MATH_ATANH 20
#define CALCOP_FLOAT_MATH_CEIL 21
#define CALCOP_FLOAT_MATH_COPYSIGN 22
#define CALCOP_FLOAT_MATH_COS 23
#define CALCOP_FLOAT_MATH_COSH 24
#define CALCOP_FLOAT_MATH_DEGREES 25
#define CALCOP_FLOAT_MATH_ERF 26
#define CALCOP_FLOAT_MATH_ERFC 27
#define CALCOP_FLOAT_MATH_EXP 28
#define CALCOP_FLOAT_MATH_EXPM1 29
#define CALCOP_FLOAT_MATH_FABS 30
#define CALCOP_FLOAT_MATH_FLOOR 31
#define CALCOP_FLOAT_MATH_FMOD 32
#define CALCOP_FLOAT_MATH_GAMMA 33
#define CALCOP_FLOAT_MATH_HYPOT 34
#define CALCOP_FLOAT_MATH_LDEXP 35
#define CALCOP_FLOAT_MATH_LGAMMA 36
#define CALCOP_FLOAT_MATH_LOG 37
#define CALCOP_FLOAT_MATH_LOG10 38
#define CALCOP_FLOAT_MATH_LOG1P 39
#define CALCOP_FLOAT_MATH_LOG2 40
#define CALCOP_FLOAT_MATH_POW 41
#define CALCOP_FLOAT_MATH_RADIANS 42
#define CALCOP_FLOAT_MATH_SIN 43
#define CALCOP_FLOAT_MATH_SINH 44
#define CALCOP_FLOAT_MATH_SQRT 45
#define CALCOP_FLOAT_MATH_TAN 46
#define CALCOP_FLOAT_MATH_TANH 47
#define CALCOP_FLOAT_MATH_TRUNC 48

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

// ACalc interpreter stack overflow or underflow.
void ErrMsgACalcStackOverflow(void);

// ACalc interpreter uknown op code.
void ErrMsgACalcUnknownOpCode(void);

// ACalc interpreter variable offset array overflow or underflow.
void ErrMsgACalcVarOffsetOverflow(void);

// The operator is invalid for this array type.
void ErrMsgACalcInvalidOpTypeArray(void);

/*--------------------------------------------------------------------------- */

