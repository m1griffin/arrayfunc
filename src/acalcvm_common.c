//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   acalc_common.c
// Purpose:  Common code for acalc.
// Language: C
// Date:     20-Jan-2016.
//
//------------------------------------------------------------------------------
//
//   Copyright 2015 - 2016    Michael Griffin    <m12.griffin@gmail.com>
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
// This must be defined before "Python.h" in order for the pointers in the
// argument parsing functions to work properly. 
#define PY_SSIZE_T_CLEAN

#include "Python.h"

#include <math.h>
#include <limits.h>

#include "arithcalcs.h"
#include "arrayfunc.h"
#include "arrayerrs.h"

#include "acalcvm_common.h"


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
#define CALCOP_FLOAT_MATH_POW 40
#define CALCOP_FLOAT_MATH_RADIANS 41
#define CALCOP_FLOAT_MATH_SIN 42
#define CALCOP_FLOAT_MATH_SINH 43
#define CALCOP_FLOAT_MATH_SQRT 44
#define CALCOP_FLOAT_MATH_TAN 45
#define CALCOP_FLOAT_MATH_TANH 46
#define CALCOP_FLOAT_MATH_TRUNC 47


/*--------------------------------------------------------------------------- */


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

// Auto generated goes below.

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   codearraylen = The length of the byte code array.
   codearray = The array of byte codes.
   varoffsetsarray = The array of variable offsets.
   vararray = The array of variable values.
   constarray = The array of constant values.
   vmstack = The array used for the stack.
   vmstacksize = The maximum size of the stack provided.
   vmstacksegments = The number of stack "segments" used when interating in "chunks".
   disableovfl = If true, disable arithmetic overflow checking (default is false).
   Return = 0 if OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int exequation_signed_char(Py_ssize_t arraylen, signed char *data, signed char *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, signed char *vararray, signed char *constarray,
			signed char *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl) {


	// Index into op code array.
	unsigned int opindex = 0;
	// Index into data array.
	Py_ssize_t dataindex = 0;
	// Keep track of number of loop iterations.
	Py_ssize_t looptarget, loopremainder;
	// The number of times through the outer loop.
	Py_ssize_t stridecounter = 0;


	unsigned int stackpointer, slicestride, x;

	signed char dataouttmp;	// Used for overflow calculations.

	char errflag = 0;


	stackpointer = 0;

	// Number of full iterations through the outer loop required.
	looptarget = arraylen / vmstacksegments;
	// Number of array elements left over for the end of the array if the
	// array size is not evenly divisible.
	loopremainder = arraylen % vmstacksegments;


	// The outer loop covers the entire data array.
	while(dataindex < arraylen) {

		// Reset the op code index and stack pointer for the next iteration.
		opindex = 0;
		stackpointer = 0;

		// The number of elements we go through in the inner loop may be differnt
		// during the last iteration.
		if (stridecounter < looptarget) { 
			slicestride = vmstacksegments; 
		} else {
			slicestride = (unsigned int) loopremainder;
		}


		// We go through the bytes codes once in sequence.
		// The middle loop goes through the interpreter instructions.
		while(opindex < codearraylen) {

			switch (codearray[opindex]) {
				// unknown
				case CALCOP_INT_UNKNOWN: {
					return CALC_ERR_UNKNOWNOP;
					}
				// pusharray
				case CALCOP_INT_PUSHARRAY: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = data[dataindex + x];
					}
					break;
					}
				// pushvar
				case CALCOP_INT_PUSHVAR: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = vararray[varoffsetsarray[opindex]];
					}
					break;
					}
				// pushconst
				case CALCOP_INT_PUSHCONST: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = constarray[opindex];
					}
					break;
					}
				// add
				case CALCOP_INT_ADD: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > 0) && (vmstack[stackpointer + vmstacksegments + x] > (SCHAR_MAX - vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] < 0) && (vmstack[stackpointer + vmstacksegments + x] < (SCHAR_MIN - vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					}
					break;
					}
				// sub
				case CALCOP_INT_SUB: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > 0) && (vmstack[stackpointer + vmstacksegments + x] < (SCHAR_MIN + vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] < 0) && (vmstack[stackpointer + vmstacksegments + x] > (SCHAR_MAX + vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					}
					break;
					}
				// mult
				case CALCOP_INT_MULT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > 0) && ((vmstack[stackpointer + vmstacksegments + x] > (SCHAR_MAX / vmstack[stackpointer + x])) || (vmstack[stackpointer + vmstacksegments + x] < (SCHAR_MIN / vmstack[stackpointer + x])))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] < -1) && ((vmstack[stackpointer + vmstacksegments + x] < (SCHAR_MAX / vmstack[stackpointer + x])) || (vmstack[stackpointer + vmstacksegments + x] > (SCHAR_MIN / vmstack[stackpointer + x])))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] == -1) && (vmstack[stackpointer + vmstacksegments + x] == SCHAR_MIN)) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					}
					break;
					}
				// div
				case CALCOP_INT_DIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						// Cannot disable divide by zero checking because this causes a crash.
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							if ((vmstack[stackpointer + x] == -1) && (vmstack[stackpointer + vmstacksegments + x] == SCHAR_MIN)) {return CALC_ERR_OVFL;}		// Overflow check.
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						}
					}
					break;
					}
				// floordiv
				case CALCOP_INT_FLOORDIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							dataouttmp = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
							// This check is required for floor division.
							if (((vmstack[stackpointer + vmstacksegments + x] < 0) != (vmstack[stackpointer + x] < 0)) && ((dataouttmp * vmstack[stackpointer + x]) != vmstack[stackpointer + vmstacksegments + x])) { 
								vmstack[stackpointer + x] = dataouttmp - 1; 
							} else {
								vmstack[stackpointer + x] = dataouttmp;
							}
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							if ((vmstack[stackpointer + x] == -1) && (vmstack[stackpointer + vmstacksegments + x] == SCHAR_MIN)) {return CALC_ERR_OVFL;}		// Overflow check.
							dataouttmp = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
							// This check is required for floor division.
							if (((vmstack[stackpointer + vmstacksegments + x] < 0) != (vmstack[stackpointer + x] < 0)) && ((dataouttmp * vmstack[stackpointer + x]) != vmstack[stackpointer + vmstacksegments + x])) { 
								vmstack[stackpointer + x] = dataouttmp - 1; 
							} else {
								vmstack[stackpointer + x] = dataouttmp;
							}
						}
					}
					break;
					}
				// mod
				case CALCOP_INT_MOD: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						dataouttmp = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						// This check is required for floor division.
						if (((vmstack[stackpointer + vmstacksegments + x] < 0) != (vmstack[stackpointer + x] < 0)) && ((dataouttmp * vmstack[stackpointer + x]) != vmstack[stackpointer + vmstacksegments + x])) { 
							dataouttmp = dataouttmp - 1;
						}
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x] * dataouttmp;
					}
					break;
					}
				// uadd
				case CALCOP_INT_UADD: {
					// No overflow checking required for this.
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = +vmstack[stackpointer + x];
					}
					break;
					}
				// usub
				case CALCOP_INT_USUB: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = -vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == SCHAR_MIN) {return CALC_ERR_OVFL;}		// Overflow check.
							vmstack[stackpointer + x] = -vmstack[stackpointer + x];
						}
					}
					break;
					}
				// pow
				case CALCOP_INT_POW: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_signed_char(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_signed_char(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitand
				case CALCOP_INT_BITAND: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitor
				case CALCOP_INT_BITOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitxor
				case CALCOP_INT_BITXOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// invert
				case CALCOP_INT_INVERT: {
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = ~vmstack[stackpointer + x];
					}
					break;
					}
				// lshift
				case CALCOP_INT_LSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// rshift
				case CALCOP_INT_RSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// abs
				case CALCOP_INT_ABS: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + x] >= 0 ? vmstack[stackpointer + x] : -vmstack[stackpointer + x]; 
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == SCHAR_MIN) {return CALC_ERR_ARITHMETIC;}		// Overflow check.
							vmstack[stackpointer + x] = vmstack[stackpointer + x] >= 0 ? vmstack[stackpointer + x] : -vmstack[stackpointer + x]; 
						}
					}
					break;
					}
				// math.factorial
				case CALCOP_INT_MATH_FACTORIAL: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_signed_char(vmstack[stackpointer + x], &errflag);
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_signed_char(vmstack[stackpointer + x], &errflag);
							if (errflag != 0) return CALC_ERR_ARITHMETIC;
						}
					}
					break;
					}

			}
			// Increment the op code index to the next instruction.
			opindex++;
		}

		// Store the calculation result.
		for(x = 0; x < slicestride; x++) {
			dataout[dataindex + x] = vmstack[stackpointer + x];
		}

		// Increment the data index array.
		dataindex = dataindex + vmstacksegments;

		// Count up the number of outer loops we need to go through.
		stridecounter++;

	}


	return CALC_NO_ERR;

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   codearraylen = The length of the byte code array.
   codearray = The array of byte codes.
   varoffsetsarray = The array of variable offsets.
   vararray = The array of variable values.
   constarray = The array of constant values.
   vmstack = The array used for the stack.
   vmstacksize = The maximum size of the stack provided.
   vmstacksegments = The number of stack "segments" used when interating in "chunks".
   disableovfl = If true, disable arithmetic overflow checking (default is false).
   Return = 0 if OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int exequation_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, unsigned char *vararray, unsigned char *constarray,
			unsigned char *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl) {


	// Index into op code array.
	unsigned int opindex = 0;
	// Index into data array.
	Py_ssize_t dataindex = 0;
	// Keep track of number of loop iterations.
	Py_ssize_t looptarget, loopremainder;
	// The number of times through the outer loop.
	Py_ssize_t stridecounter = 0;


	unsigned int stackpointer, slicestride, x;


	char errflag = 0;


	stackpointer = 0;

	// Number of full iterations through the outer loop required.
	looptarget = arraylen / vmstacksegments;
	// Number of array elements left over for the end of the array if the
	// array size is not evenly divisible.
	loopremainder = arraylen % vmstacksegments;


	// The outer loop covers the entire data array.
	while(dataindex < arraylen) {

		// Reset the op code index and stack pointer for the next iteration.
		opindex = 0;
		stackpointer = 0;

		// The number of elements we go through in the inner loop may be differnt
		// during the last iteration.
		if (stridecounter < looptarget) { 
			slicestride = vmstacksegments; 
		} else {
			slicestride = (unsigned int) loopremainder;
		}


		// We go through the bytes codes once in sequence.
		// The middle loop goes through the interpreter instructions.
		while(opindex < codearraylen) {

			switch (codearray[opindex]) {
				// unknown
				case CALCOP_INT_UNKNOWN: {
					return CALC_ERR_UNKNOWNOP;
					}
				// pusharray
				case CALCOP_INT_PUSHARRAY: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = data[dataindex + x];
					}
					break;
					}
				// pushvar
				case CALCOP_INT_PUSHVAR: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = vararray[varoffsetsarray[opindex]];
					}
					break;
					}
				// pushconst
				case CALCOP_INT_PUSHCONST: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = constarray[opindex];
					}
					break;
					}
				// add
				case CALCOP_INT_ADD: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + vmstacksegments + x] > (UCHAR_MAX - vmstack[stackpointer + x])) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					}
					break;
					}
				// sub
				case CALCOP_INT_SUB: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + vmstacksegments + x] < vmstack[stackpointer + x]) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					}
					break;
					}
				// mult
				case CALCOP_INT_MULT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] != 0) && (vmstack[stackpointer + vmstacksegments + x] > (UCHAR_MAX / vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					}
					break;
					}
				// div
				case CALCOP_INT_DIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
					}
					break;
					}
				// floordiv
				case CALCOP_INT_FLOORDIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
					}
					break;
					}
				// mod
				case CALCOP_INT_MOD: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] % vmstack[stackpointer + x];
					}
					break;
					}
				// uadd
				case CALCOP_INT_UADD: {
					// No overflow checking required for this.
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = +vmstack[stackpointer + x];
					}
					break;
					}
				// usub
				case CALCOP_INT_USUB: {
					return CALC_ERR_INVALIDOP;
					}
				// pow
				case CALCOP_INT_POW: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_unsigned_char(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_unsigned_char(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitand
				case CALCOP_INT_BITAND: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitor
				case CALCOP_INT_BITOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitxor
				case CALCOP_INT_BITXOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// invert
				case CALCOP_INT_INVERT: {
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = ~vmstack[stackpointer + x];
					}
					break;
					}
				// lshift
				case CALCOP_INT_LSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// rshift
				case CALCOP_INT_RSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// abs
				case CALCOP_INT_ABS: {
					break;
					}
				// math.factorial
				case CALCOP_INT_MATH_FACTORIAL: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_unsigned_char(vmstack[stackpointer + x], &errflag);
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_unsigned_char(vmstack[stackpointer + x], &errflag);
							if (errflag != 0) return CALC_ERR_ARITHMETIC;
						}
					}
					break;
					}

			}
			// Increment the op code index to the next instruction.
			opindex++;
		}

		// Store the calculation result.
		for(x = 0; x < slicestride; x++) {
			dataout[dataindex + x] = vmstack[stackpointer + x];
		}

		// Increment the data index array.
		dataindex = dataindex + vmstacksegments;

		// Count up the number of outer loops we need to go through.
		stridecounter++;

	}


	return CALC_NO_ERR;

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   codearraylen = The length of the byte code array.
   codearray = The array of byte codes.
   varoffsetsarray = The array of variable offsets.
   vararray = The array of variable values.
   constarray = The array of constant values.
   vmstack = The array used for the stack.
   vmstacksize = The maximum size of the stack provided.
   vmstacksegments = The number of stack "segments" used when interating in "chunks".
   disableovfl = If true, disable arithmetic overflow checking (default is false).
   Return = 0 if OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int exequation_signed_short(Py_ssize_t arraylen, signed short *data, signed short *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, signed short *vararray, signed short *constarray,
			signed short *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl) {


	// Index into op code array.
	unsigned int opindex = 0;
	// Index into data array.
	Py_ssize_t dataindex = 0;
	// Keep track of number of loop iterations.
	Py_ssize_t looptarget, loopremainder;
	// The number of times through the outer loop.
	Py_ssize_t stridecounter = 0;


	unsigned int stackpointer, slicestride, x;

	signed short dataouttmp;	// Used for overflow calculations.

	char errflag = 0;


	stackpointer = 0;

	// Number of full iterations through the outer loop required.
	looptarget = arraylen / vmstacksegments;
	// Number of array elements left over for the end of the array if the
	// array size is not evenly divisible.
	loopremainder = arraylen % vmstacksegments;


	// The outer loop covers the entire data array.
	while(dataindex < arraylen) {

		// Reset the op code index and stack pointer for the next iteration.
		opindex = 0;
		stackpointer = 0;

		// The number of elements we go through in the inner loop may be differnt
		// during the last iteration.
		if (stridecounter < looptarget) { 
			slicestride = vmstacksegments; 
		} else {
			slicestride = (unsigned int) loopremainder;
		}


		// We go through the bytes codes once in sequence.
		// The middle loop goes through the interpreter instructions.
		while(opindex < codearraylen) {

			switch (codearray[opindex]) {
				// unknown
				case CALCOP_INT_UNKNOWN: {
					return CALC_ERR_UNKNOWNOP;
					}
				// pusharray
				case CALCOP_INT_PUSHARRAY: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = data[dataindex + x];
					}
					break;
					}
				// pushvar
				case CALCOP_INT_PUSHVAR: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = vararray[varoffsetsarray[opindex]];
					}
					break;
					}
				// pushconst
				case CALCOP_INT_PUSHCONST: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = constarray[opindex];
					}
					break;
					}
				// add
				case CALCOP_INT_ADD: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > 0) && (vmstack[stackpointer + vmstacksegments + x] > (SHRT_MAX - vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] < 0) && (vmstack[stackpointer + vmstacksegments + x] < (SHRT_MIN - vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					}
					break;
					}
				// sub
				case CALCOP_INT_SUB: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > 0) && (vmstack[stackpointer + vmstacksegments + x] < (SHRT_MIN + vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] < 0) && (vmstack[stackpointer + vmstacksegments + x] > (SHRT_MAX + vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					}
					break;
					}
				// mult
				case CALCOP_INT_MULT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > 0) && ((vmstack[stackpointer + vmstacksegments + x] > (SHRT_MAX / vmstack[stackpointer + x])) || (vmstack[stackpointer + vmstacksegments + x] < (SHRT_MIN / vmstack[stackpointer + x])))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] < -1) && ((vmstack[stackpointer + vmstacksegments + x] < (SHRT_MAX / vmstack[stackpointer + x])) || (vmstack[stackpointer + vmstacksegments + x] > (SHRT_MIN / vmstack[stackpointer + x])))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] == -1) && (vmstack[stackpointer + vmstacksegments + x] == SHRT_MIN)) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					}
					break;
					}
				// div
				case CALCOP_INT_DIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						// Cannot disable divide by zero checking because this causes a crash.
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							if ((vmstack[stackpointer + x] == -1) && (vmstack[stackpointer + vmstacksegments + x] == SHRT_MIN)) {return CALC_ERR_OVFL;}		// Overflow check.
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						}
					}
					break;
					}
				// floordiv
				case CALCOP_INT_FLOORDIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							dataouttmp = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
							// This check is required for floor division.
							if (((vmstack[stackpointer + vmstacksegments + x] < 0) != (vmstack[stackpointer + x] < 0)) && ((dataouttmp * vmstack[stackpointer + x]) != vmstack[stackpointer + vmstacksegments + x])) { 
								vmstack[stackpointer + x] = dataouttmp - 1; 
							} else {
								vmstack[stackpointer + x] = dataouttmp;
							}
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							if ((vmstack[stackpointer + x] == -1) && (vmstack[stackpointer + vmstacksegments + x] == SHRT_MIN)) {return CALC_ERR_OVFL;}		// Overflow check.
							dataouttmp = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
							// This check is required for floor division.
							if (((vmstack[stackpointer + vmstacksegments + x] < 0) != (vmstack[stackpointer + x] < 0)) && ((dataouttmp * vmstack[stackpointer + x]) != vmstack[stackpointer + vmstacksegments + x])) { 
								vmstack[stackpointer + x] = dataouttmp - 1; 
							} else {
								vmstack[stackpointer + x] = dataouttmp;
							}
						}
					}
					break;
					}
				// mod
				case CALCOP_INT_MOD: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						dataouttmp = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						// This check is required for floor division.
						if (((vmstack[stackpointer + vmstacksegments + x] < 0) != (vmstack[stackpointer + x] < 0)) && ((dataouttmp * vmstack[stackpointer + x]) != vmstack[stackpointer + vmstacksegments + x])) { 
							dataouttmp = dataouttmp - 1;
						}
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x] * dataouttmp;
					}
					break;
					}
				// uadd
				case CALCOP_INT_UADD: {
					// No overflow checking required for this.
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = +vmstack[stackpointer + x];
					}
					break;
					}
				// usub
				case CALCOP_INT_USUB: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = -vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == SHRT_MIN) {return CALC_ERR_OVFL;}		// Overflow check.
							vmstack[stackpointer + x] = -vmstack[stackpointer + x];
						}
					}
					break;
					}
				// pow
				case CALCOP_INT_POW: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_signed_short(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_signed_short(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitand
				case CALCOP_INT_BITAND: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitor
				case CALCOP_INT_BITOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitxor
				case CALCOP_INT_BITXOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// invert
				case CALCOP_INT_INVERT: {
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = ~vmstack[stackpointer + x];
					}
					break;
					}
				// lshift
				case CALCOP_INT_LSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// rshift
				case CALCOP_INT_RSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// abs
				case CALCOP_INT_ABS: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + x] >= 0 ? vmstack[stackpointer + x] : -vmstack[stackpointer + x]; 
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == SHRT_MIN) {return CALC_ERR_ARITHMETIC;}		// Overflow check.
							vmstack[stackpointer + x] = vmstack[stackpointer + x] >= 0 ? vmstack[stackpointer + x] : -vmstack[stackpointer + x]; 
						}
					}
					break;
					}
				// math.factorial
				case CALCOP_INT_MATH_FACTORIAL: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_signed_short(vmstack[stackpointer + x], &errflag);
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_signed_short(vmstack[stackpointer + x], &errflag);
							if (errflag != 0) return CALC_ERR_ARITHMETIC;
						}
					}
					break;
					}

			}
			// Increment the op code index to the next instruction.
			opindex++;
		}

		// Store the calculation result.
		for(x = 0; x < slicestride; x++) {
			dataout[dataindex + x] = vmstack[stackpointer + x];
		}

		// Increment the data index array.
		dataindex = dataindex + vmstacksegments;

		// Count up the number of outer loops we need to go through.
		stridecounter++;

	}


	return CALC_NO_ERR;

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   codearraylen = The length of the byte code array.
   codearray = The array of byte codes.
   varoffsetsarray = The array of variable offsets.
   vararray = The array of variable values.
   constarray = The array of constant values.
   vmstack = The array used for the stack.
   vmstacksize = The maximum size of the stack provided.
   vmstacksegments = The number of stack "segments" used when interating in "chunks".
   disableovfl = If true, disable arithmetic overflow checking (default is false).
   Return = 0 if OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int exequation_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, unsigned short *vararray, unsigned short *constarray,
			unsigned short *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl) {


	// Index into op code array.
	unsigned int opindex = 0;
	// Index into data array.
	Py_ssize_t dataindex = 0;
	// Keep track of number of loop iterations.
	Py_ssize_t looptarget, loopremainder;
	// The number of times through the outer loop.
	Py_ssize_t stridecounter = 0;


	unsigned int stackpointer, slicestride, x;


	char errflag = 0;


	stackpointer = 0;

	// Number of full iterations through the outer loop required.
	looptarget = arraylen / vmstacksegments;
	// Number of array elements left over for the end of the array if the
	// array size is not evenly divisible.
	loopremainder = arraylen % vmstacksegments;


	// The outer loop covers the entire data array.
	while(dataindex < arraylen) {

		// Reset the op code index and stack pointer for the next iteration.
		opindex = 0;
		stackpointer = 0;

		// The number of elements we go through in the inner loop may be differnt
		// during the last iteration.
		if (stridecounter < looptarget) { 
			slicestride = vmstacksegments; 
		} else {
			slicestride = (unsigned int) loopremainder;
		}


		// We go through the bytes codes once in sequence.
		// The middle loop goes through the interpreter instructions.
		while(opindex < codearraylen) {

			switch (codearray[opindex]) {
				// unknown
				case CALCOP_INT_UNKNOWN: {
					return CALC_ERR_UNKNOWNOP;
					}
				// pusharray
				case CALCOP_INT_PUSHARRAY: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = data[dataindex + x];
					}
					break;
					}
				// pushvar
				case CALCOP_INT_PUSHVAR: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = vararray[varoffsetsarray[opindex]];
					}
					break;
					}
				// pushconst
				case CALCOP_INT_PUSHCONST: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = constarray[opindex];
					}
					break;
					}
				// add
				case CALCOP_INT_ADD: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + vmstacksegments + x] > (USHRT_MAX - vmstack[stackpointer + x])) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					}
					break;
					}
				// sub
				case CALCOP_INT_SUB: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + vmstacksegments + x] < vmstack[stackpointer + x]) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					}
					break;
					}
				// mult
				case CALCOP_INT_MULT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] != 0) && (vmstack[stackpointer + vmstacksegments + x] > (USHRT_MAX / vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					}
					break;
					}
				// div
				case CALCOP_INT_DIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
					}
					break;
					}
				// floordiv
				case CALCOP_INT_FLOORDIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
					}
					break;
					}
				// mod
				case CALCOP_INT_MOD: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] % vmstack[stackpointer + x];
					}
					break;
					}
				// uadd
				case CALCOP_INT_UADD: {
					// No overflow checking required for this.
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = +vmstack[stackpointer + x];
					}
					break;
					}
				// usub
				case CALCOP_INT_USUB: {
					return CALC_ERR_INVALIDOP;
					}
				// pow
				case CALCOP_INT_POW: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_unsigned_short(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_unsigned_short(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitand
				case CALCOP_INT_BITAND: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitor
				case CALCOP_INT_BITOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitxor
				case CALCOP_INT_BITXOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// invert
				case CALCOP_INT_INVERT: {
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = ~vmstack[stackpointer + x];
					}
					break;
					}
				// lshift
				case CALCOP_INT_LSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// rshift
				case CALCOP_INT_RSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// abs
				case CALCOP_INT_ABS: {
					break;
					}
				// math.factorial
				case CALCOP_INT_MATH_FACTORIAL: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_unsigned_short(vmstack[stackpointer + x], &errflag);
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_unsigned_short(vmstack[stackpointer + x], &errflag);
							if (errflag != 0) return CALC_ERR_ARITHMETIC;
						}
					}
					break;
					}

			}
			// Increment the op code index to the next instruction.
			opindex++;
		}

		// Store the calculation result.
		for(x = 0; x < slicestride; x++) {
			dataout[dataindex + x] = vmstack[stackpointer + x];
		}

		// Increment the data index array.
		dataindex = dataindex + vmstacksegments;

		// Count up the number of outer loops we need to go through.
		stridecounter++;

	}


	return CALC_NO_ERR;

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   codearraylen = The length of the byte code array.
   codearray = The array of byte codes.
   varoffsetsarray = The array of variable offsets.
   vararray = The array of variable values.
   constarray = The array of constant values.
   vmstack = The array used for the stack.
   vmstacksize = The maximum size of the stack provided.
   vmstacksegments = The number of stack "segments" used when interating in "chunks".
   disableovfl = If true, disable arithmetic overflow checking (default is false).
   Return = 0 if OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int exequation_signed_int(Py_ssize_t arraylen, signed int *data, signed int *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, signed int *vararray, signed int *constarray,
			signed int *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl) {


	// Index into op code array.
	unsigned int opindex = 0;
	// Index into data array.
	Py_ssize_t dataindex = 0;
	// Keep track of number of loop iterations.
	Py_ssize_t looptarget, loopremainder;
	// The number of times through the outer loop.
	Py_ssize_t stridecounter = 0;


	unsigned int stackpointer, slicestride, x;

	signed int dataouttmp;	// Used for overflow calculations.

	char errflag = 0;


	stackpointer = 0;

	// Number of full iterations through the outer loop required.
	looptarget = arraylen / vmstacksegments;
	// Number of array elements left over for the end of the array if the
	// array size is not evenly divisible.
	loopremainder = arraylen % vmstacksegments;


	// The outer loop covers the entire data array.
	while(dataindex < arraylen) {

		// Reset the op code index and stack pointer for the next iteration.
		opindex = 0;
		stackpointer = 0;

		// The number of elements we go through in the inner loop may be differnt
		// during the last iteration.
		if (stridecounter < looptarget) { 
			slicestride = vmstacksegments; 
		} else {
			slicestride = (unsigned int) loopremainder;
		}


		// We go through the bytes codes once in sequence.
		// The middle loop goes through the interpreter instructions.
		while(opindex < codearraylen) {

			switch (codearray[opindex]) {
				// unknown
				case CALCOP_INT_UNKNOWN: {
					return CALC_ERR_UNKNOWNOP;
					}
				// pusharray
				case CALCOP_INT_PUSHARRAY: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = data[dataindex + x];
					}
					break;
					}
				// pushvar
				case CALCOP_INT_PUSHVAR: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = vararray[varoffsetsarray[opindex]];
					}
					break;
					}
				// pushconst
				case CALCOP_INT_PUSHCONST: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = constarray[opindex];
					}
					break;
					}
				// add
				case CALCOP_INT_ADD: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > 0) && (vmstack[stackpointer + vmstacksegments + x] > (INT_MAX - vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] < 0) && (vmstack[stackpointer + vmstacksegments + x] < (INT_MIN - vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					}
					break;
					}
				// sub
				case CALCOP_INT_SUB: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > 0) && (vmstack[stackpointer + vmstacksegments + x] < (INT_MIN + vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] < 0) && (vmstack[stackpointer + vmstacksegments + x] > (INT_MAX + vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					}
					break;
					}
				// mult
				case CALCOP_INT_MULT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > 0) && ((vmstack[stackpointer + vmstacksegments + x] > (INT_MAX / vmstack[stackpointer + x])) || (vmstack[stackpointer + vmstacksegments + x] < (INT_MIN / vmstack[stackpointer + x])))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] < -1) && ((vmstack[stackpointer + vmstacksegments + x] < (INT_MAX / vmstack[stackpointer + x])) || (vmstack[stackpointer + vmstacksegments + x] > (INT_MIN / vmstack[stackpointer + x])))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] == -1) && (vmstack[stackpointer + vmstacksegments + x] == INT_MIN)) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					}
					break;
					}
				// div
				case CALCOP_INT_DIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						// Cannot disable divide by zero checking because this causes a crash.
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							if ((vmstack[stackpointer + x] == -1) && (vmstack[stackpointer + vmstacksegments + x] == INT_MIN)) {return CALC_ERR_OVFL;}		// Overflow check.
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						}
					}
					break;
					}
				// floordiv
				case CALCOP_INT_FLOORDIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							dataouttmp = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
							// This check is required for floor division.
							if (((vmstack[stackpointer + vmstacksegments + x] < 0) != (vmstack[stackpointer + x] < 0)) && ((dataouttmp * vmstack[stackpointer + x]) != vmstack[stackpointer + vmstacksegments + x])) { 
								vmstack[stackpointer + x] = dataouttmp - 1; 
							} else {
								vmstack[stackpointer + x] = dataouttmp;
							}
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							if ((vmstack[stackpointer + x] == -1) && (vmstack[stackpointer + vmstacksegments + x] == INT_MIN)) {return CALC_ERR_OVFL;}		// Overflow check.
							dataouttmp = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
							// This check is required for floor division.
							if (((vmstack[stackpointer + vmstacksegments + x] < 0) != (vmstack[stackpointer + x] < 0)) && ((dataouttmp * vmstack[stackpointer + x]) != vmstack[stackpointer + vmstacksegments + x])) { 
								vmstack[stackpointer + x] = dataouttmp - 1; 
							} else {
								vmstack[stackpointer + x] = dataouttmp;
							}
						}
					}
					break;
					}
				// mod
				case CALCOP_INT_MOD: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						dataouttmp = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						// This check is required for floor division.
						if (((vmstack[stackpointer + vmstacksegments + x] < 0) != (vmstack[stackpointer + x] < 0)) && ((dataouttmp * vmstack[stackpointer + x]) != vmstack[stackpointer + vmstacksegments + x])) { 
							dataouttmp = dataouttmp - 1;
						}
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x] * dataouttmp;
					}
					break;
					}
				// uadd
				case CALCOP_INT_UADD: {
					// No overflow checking required for this.
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = +vmstack[stackpointer + x];
					}
					break;
					}
				// usub
				case CALCOP_INT_USUB: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = -vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == INT_MIN) {return CALC_ERR_OVFL;}		// Overflow check.
							vmstack[stackpointer + x] = -vmstack[stackpointer + x];
						}
					}
					break;
					}
				// pow
				case CALCOP_INT_POW: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_signed_int(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_signed_int(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitand
				case CALCOP_INT_BITAND: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitor
				case CALCOP_INT_BITOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitxor
				case CALCOP_INT_BITXOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// invert
				case CALCOP_INT_INVERT: {
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = ~vmstack[stackpointer + x];
					}
					break;
					}
				// lshift
				case CALCOP_INT_LSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// rshift
				case CALCOP_INT_RSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// abs
				case CALCOP_INT_ABS: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + x] >= 0 ? vmstack[stackpointer + x] : -vmstack[stackpointer + x]; 
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == INT_MIN) {return CALC_ERR_ARITHMETIC;}		// Overflow check.
							vmstack[stackpointer + x] = vmstack[stackpointer + x] >= 0 ? vmstack[stackpointer + x] : -vmstack[stackpointer + x]; 
						}
					}
					break;
					}
				// math.factorial
				case CALCOP_INT_MATH_FACTORIAL: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_signed_int(vmstack[stackpointer + x], &errflag);
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_signed_int(vmstack[stackpointer + x], &errflag);
							if (errflag != 0) return CALC_ERR_ARITHMETIC;
						}
					}
					break;
					}

			}
			// Increment the op code index to the next instruction.
			opindex++;
		}

		// Store the calculation result.
		for(x = 0; x < slicestride; x++) {
			dataout[dataindex + x] = vmstack[stackpointer + x];
		}

		// Increment the data index array.
		dataindex = dataindex + vmstacksegments;

		// Count up the number of outer loops we need to go through.
		stridecounter++;

	}


	return CALC_NO_ERR;

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   codearraylen = The length of the byte code array.
   codearray = The array of byte codes.
   varoffsetsarray = The array of variable offsets.
   vararray = The array of variable values.
   constarray = The array of constant values.
   vmstack = The array used for the stack.
   vmstacksize = The maximum size of the stack provided.
   vmstacksegments = The number of stack "segments" used when interating in "chunks".
   disableovfl = If true, disable arithmetic overflow checking (default is false).
   Return = 0 if OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int exequation_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, unsigned int *vararray, unsigned int *constarray,
			unsigned int *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl) {


	// Index into op code array.
	unsigned int opindex = 0;
	// Index into data array.
	Py_ssize_t dataindex = 0;
	// Keep track of number of loop iterations.
	Py_ssize_t looptarget, loopremainder;
	// The number of times through the outer loop.
	Py_ssize_t stridecounter = 0;


	unsigned int stackpointer, slicestride, x;


	char errflag = 0;


	stackpointer = 0;

	// Number of full iterations through the outer loop required.
	looptarget = arraylen / vmstacksegments;
	// Number of array elements left over for the end of the array if the
	// array size is not evenly divisible.
	loopremainder = arraylen % vmstacksegments;


	// The outer loop covers the entire data array.
	while(dataindex < arraylen) {

		// Reset the op code index and stack pointer for the next iteration.
		opindex = 0;
		stackpointer = 0;

		// The number of elements we go through in the inner loop may be differnt
		// during the last iteration.
		if (stridecounter < looptarget) { 
			slicestride = vmstacksegments; 
		} else {
			slicestride = (unsigned int) loopremainder;
		}


		// We go through the bytes codes once in sequence.
		// The middle loop goes through the interpreter instructions.
		while(opindex < codearraylen) {

			switch (codearray[opindex]) {
				// unknown
				case CALCOP_INT_UNKNOWN: {
					return CALC_ERR_UNKNOWNOP;
					}
				// pusharray
				case CALCOP_INT_PUSHARRAY: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = data[dataindex + x];
					}
					break;
					}
				// pushvar
				case CALCOP_INT_PUSHVAR: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = vararray[varoffsetsarray[opindex]];
					}
					break;
					}
				// pushconst
				case CALCOP_INT_PUSHCONST: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = constarray[opindex];
					}
					break;
					}
				// add
				case CALCOP_INT_ADD: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + vmstacksegments + x] > (UINT_MAX - vmstack[stackpointer + x])) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					}
					break;
					}
				// sub
				case CALCOP_INT_SUB: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + vmstacksegments + x] < vmstack[stackpointer + x]) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					}
					break;
					}
				// mult
				case CALCOP_INT_MULT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] != 0) && (vmstack[stackpointer + vmstacksegments + x] > (UINT_MAX / vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					}
					break;
					}
				// div
				case CALCOP_INT_DIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
					}
					break;
					}
				// floordiv
				case CALCOP_INT_FLOORDIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
					}
					break;
					}
				// mod
				case CALCOP_INT_MOD: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] % vmstack[stackpointer + x];
					}
					break;
					}
				// uadd
				case CALCOP_INT_UADD: {
					// No overflow checking required for this.
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = +vmstack[stackpointer + x];
					}
					break;
					}
				// usub
				case CALCOP_INT_USUB: {
					return CALC_ERR_INVALIDOP;
					}
				// pow
				case CALCOP_INT_POW: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_unsigned_int(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_unsigned_int(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitand
				case CALCOP_INT_BITAND: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitor
				case CALCOP_INT_BITOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitxor
				case CALCOP_INT_BITXOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// invert
				case CALCOP_INT_INVERT: {
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = ~vmstack[stackpointer + x];
					}
					break;
					}
				// lshift
				case CALCOP_INT_LSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// rshift
				case CALCOP_INT_RSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// abs
				case CALCOP_INT_ABS: {
					break;
					}
				// math.factorial
				case CALCOP_INT_MATH_FACTORIAL: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_unsigned_int(vmstack[stackpointer + x], &errflag);
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_unsigned_int(vmstack[stackpointer + x], &errflag);
							if (errflag != 0) return CALC_ERR_ARITHMETIC;
						}
					}
					break;
					}

			}
			// Increment the op code index to the next instruction.
			opindex++;
		}

		// Store the calculation result.
		for(x = 0; x < slicestride; x++) {
			dataout[dataindex + x] = vmstack[stackpointer + x];
		}

		// Increment the data index array.
		dataindex = dataindex + vmstacksegments;

		// Count up the number of outer loops we need to go through.
		stridecounter++;

	}


	return CALC_NO_ERR;

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   codearraylen = The length of the byte code array.
   codearray = The array of byte codes.
   varoffsetsarray = The array of variable offsets.
   vararray = The array of variable values.
   constarray = The array of constant values.
   vmstack = The array used for the stack.
   vmstacksize = The maximum size of the stack provided.
   vmstacksegments = The number of stack "segments" used when interating in "chunks".
   disableovfl = If true, disable arithmetic overflow checking (default is false).
   Return = 0 if OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int exequation_signed_long(Py_ssize_t arraylen, signed long *data, signed long *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, signed long *vararray, signed long *constarray,
			signed long *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl) {


	// Index into op code array.
	unsigned int opindex = 0;
	// Index into data array.
	Py_ssize_t dataindex = 0;
	// Keep track of number of loop iterations.
	Py_ssize_t looptarget, loopremainder;
	// The number of times through the outer loop.
	Py_ssize_t stridecounter = 0;


	unsigned int stackpointer, slicestride, x;

	signed long dataouttmp;	// Used for overflow calculations.

	char errflag = 0;


	stackpointer = 0;

	// Number of full iterations through the outer loop required.
	looptarget = arraylen / vmstacksegments;
	// Number of array elements left over for the end of the array if the
	// array size is not evenly divisible.
	loopremainder = arraylen % vmstacksegments;


	// The outer loop covers the entire data array.
	while(dataindex < arraylen) {

		// Reset the op code index and stack pointer for the next iteration.
		opindex = 0;
		stackpointer = 0;

		// The number of elements we go through in the inner loop may be differnt
		// during the last iteration.
		if (stridecounter < looptarget) { 
			slicestride = vmstacksegments; 
		} else {
			slicestride = (unsigned int) loopremainder;
		}


		// We go through the bytes codes once in sequence.
		// The middle loop goes through the interpreter instructions.
		while(opindex < codearraylen) {

			switch (codearray[opindex]) {
				// unknown
				case CALCOP_INT_UNKNOWN: {
					return CALC_ERR_UNKNOWNOP;
					}
				// pusharray
				case CALCOP_INT_PUSHARRAY: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = data[dataindex + x];
					}
					break;
					}
				// pushvar
				case CALCOP_INT_PUSHVAR: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = vararray[varoffsetsarray[opindex]];
					}
					break;
					}
				// pushconst
				case CALCOP_INT_PUSHCONST: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = constarray[opindex];
					}
					break;
					}
				// add
				case CALCOP_INT_ADD: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > 0) && (vmstack[stackpointer + vmstacksegments + x] > (LONG_MAX - vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] < 0) && (vmstack[stackpointer + vmstacksegments + x] < (LONG_MIN - vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					}
					break;
					}
				// sub
				case CALCOP_INT_SUB: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > 0) && (vmstack[stackpointer + vmstacksegments + x] < (LONG_MIN + vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] < 0) && (vmstack[stackpointer + vmstacksegments + x] > (LONG_MAX + vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					}
					break;
					}
				// mult
				case CALCOP_INT_MULT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > 0) && ((vmstack[stackpointer + vmstacksegments + x] > (LONG_MAX / vmstack[stackpointer + x])) || (vmstack[stackpointer + vmstacksegments + x] < (LONG_MIN / vmstack[stackpointer + x])))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] < -1) && ((vmstack[stackpointer + vmstacksegments + x] < (LONG_MAX / vmstack[stackpointer + x])) || (vmstack[stackpointer + vmstacksegments + x] > (LONG_MIN / vmstack[stackpointer + x])))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] == -1) && (vmstack[stackpointer + vmstacksegments + x] == LONG_MIN)) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					}
					break;
					}
				// div
				case CALCOP_INT_DIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						// Cannot disable divide by zero checking because this causes a crash.
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							if ((vmstack[stackpointer + x] == -1) && (vmstack[stackpointer + vmstacksegments + x] == LONG_MIN)) {return CALC_ERR_OVFL;}		// Overflow check.
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						}
					}
					break;
					}
				// floordiv
				case CALCOP_INT_FLOORDIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							dataouttmp = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
							// This check is required for floor division.
							if (((vmstack[stackpointer + vmstacksegments + x] < 0) != (vmstack[stackpointer + x] < 0)) && ((dataouttmp * vmstack[stackpointer + x]) != vmstack[stackpointer + vmstacksegments + x])) { 
								vmstack[stackpointer + x] = dataouttmp - 1; 
							} else {
								vmstack[stackpointer + x] = dataouttmp;
							}
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							if ((vmstack[stackpointer + x] == -1) && (vmstack[stackpointer + vmstacksegments + x] == LONG_MIN)) {return CALC_ERR_OVFL;}		// Overflow check.
							dataouttmp = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
							// This check is required for floor division.
							if (((vmstack[stackpointer + vmstacksegments + x] < 0) != (vmstack[stackpointer + x] < 0)) && ((dataouttmp * vmstack[stackpointer + x]) != vmstack[stackpointer + vmstacksegments + x])) { 
								vmstack[stackpointer + x] = dataouttmp - 1; 
							} else {
								vmstack[stackpointer + x] = dataouttmp;
							}
						}
					}
					break;
					}
				// mod
				case CALCOP_INT_MOD: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						dataouttmp = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						// This check is required for floor division.
						if (((vmstack[stackpointer + vmstacksegments + x] < 0) != (vmstack[stackpointer + x] < 0)) && ((dataouttmp * vmstack[stackpointer + x]) != vmstack[stackpointer + vmstacksegments + x])) { 
							dataouttmp = dataouttmp - 1;
						}
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x] * dataouttmp;
					}
					break;
					}
				// uadd
				case CALCOP_INT_UADD: {
					// No overflow checking required for this.
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = +vmstack[stackpointer + x];
					}
					break;
					}
				// usub
				case CALCOP_INT_USUB: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = -vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == LONG_MIN) {return CALC_ERR_OVFL;}		// Overflow check.
							vmstack[stackpointer + x] = -vmstack[stackpointer + x];
						}
					}
					break;
					}
				// pow
				case CALCOP_INT_POW: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_signed_long(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_signed_long(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitand
				case CALCOP_INT_BITAND: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitor
				case CALCOP_INT_BITOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitxor
				case CALCOP_INT_BITXOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// invert
				case CALCOP_INT_INVERT: {
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = ~vmstack[stackpointer + x];
					}
					break;
					}
				// lshift
				case CALCOP_INT_LSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// rshift
				case CALCOP_INT_RSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// abs
				case CALCOP_INT_ABS: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + x] >= 0 ? vmstack[stackpointer + x] : -vmstack[stackpointer + x]; 
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == LONG_MIN) {return CALC_ERR_ARITHMETIC;}		// Overflow check.
							vmstack[stackpointer + x] = vmstack[stackpointer + x] >= 0 ? vmstack[stackpointer + x] : -vmstack[stackpointer + x]; 
						}
					}
					break;
					}
				// math.factorial
				case CALCOP_INT_MATH_FACTORIAL: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_signed_long(vmstack[stackpointer + x], &errflag);
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_signed_long(vmstack[stackpointer + x], &errflag);
							if (errflag != 0) return CALC_ERR_ARITHMETIC;
						}
					}
					break;
					}

			}
			// Increment the op code index to the next instruction.
			opindex++;
		}

		// Store the calculation result.
		for(x = 0; x < slicestride; x++) {
			dataout[dataindex + x] = vmstack[stackpointer + x];
		}

		// Increment the data index array.
		dataindex = dataindex + vmstacksegments;

		// Count up the number of outer loops we need to go through.
		stridecounter++;

	}


	return CALC_NO_ERR;

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   codearraylen = The length of the byte code array.
   codearray = The array of byte codes.
   varoffsetsarray = The array of variable offsets.
   vararray = The array of variable values.
   constarray = The array of constant values.
   vmstack = The array used for the stack.
   vmstacksize = The maximum size of the stack provided.
   vmstacksegments = The number of stack "segments" used when interating in "chunks".
   disableovfl = If true, disable arithmetic overflow checking (default is false).
   Return = 0 if OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int exequation_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, unsigned long *vararray, unsigned long *constarray,
			unsigned long *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl) {


	// Index into op code array.
	unsigned int opindex = 0;
	// Index into data array.
	Py_ssize_t dataindex = 0;
	// Keep track of number of loop iterations.
	Py_ssize_t looptarget, loopremainder;
	// The number of times through the outer loop.
	Py_ssize_t stridecounter = 0;


	unsigned int stackpointer, slicestride, x;


	char errflag = 0;


	stackpointer = 0;

	// Number of full iterations through the outer loop required.
	looptarget = arraylen / vmstacksegments;
	// Number of array elements left over for the end of the array if the
	// array size is not evenly divisible.
	loopremainder = arraylen % vmstacksegments;


	// The outer loop covers the entire data array.
	while(dataindex < arraylen) {

		// Reset the op code index and stack pointer for the next iteration.
		opindex = 0;
		stackpointer = 0;

		// The number of elements we go through in the inner loop may be differnt
		// during the last iteration.
		if (stridecounter < looptarget) { 
			slicestride = vmstacksegments; 
		} else {
			slicestride = (unsigned int) loopremainder;
		}


		// We go through the bytes codes once in sequence.
		// The middle loop goes through the interpreter instructions.
		while(opindex < codearraylen) {

			switch (codearray[opindex]) {
				// unknown
				case CALCOP_INT_UNKNOWN: {
					return CALC_ERR_UNKNOWNOP;
					}
				// pusharray
				case CALCOP_INT_PUSHARRAY: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = data[dataindex + x];
					}
					break;
					}
				// pushvar
				case CALCOP_INT_PUSHVAR: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = vararray[varoffsetsarray[opindex]];
					}
					break;
					}
				// pushconst
				case CALCOP_INT_PUSHCONST: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = constarray[opindex];
					}
					break;
					}
				// add
				case CALCOP_INT_ADD: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + vmstacksegments + x] > (ULONG_MAX - vmstack[stackpointer + x])) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					}
					break;
					}
				// sub
				case CALCOP_INT_SUB: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + vmstacksegments + x] < vmstack[stackpointer + x]) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					}
					break;
					}
				// mult
				case CALCOP_INT_MULT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] != 0) && (vmstack[stackpointer + vmstacksegments + x] > (ULONG_MAX / vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					}
					break;
					}
				// div
				case CALCOP_INT_DIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
					}
					break;
					}
				// floordiv
				case CALCOP_INT_FLOORDIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
					}
					break;
					}
				// mod
				case CALCOP_INT_MOD: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] % vmstack[stackpointer + x];
					}
					break;
					}
				// uadd
				case CALCOP_INT_UADD: {
					// No overflow checking required for this.
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = +vmstack[stackpointer + x];
					}
					break;
					}
				// usub
				case CALCOP_INT_USUB: {
					return CALC_ERR_INVALIDOP;
					}
				// pow
				case CALCOP_INT_POW: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_unsigned_long(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_unsigned_long(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitand
				case CALCOP_INT_BITAND: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitor
				case CALCOP_INT_BITOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitxor
				case CALCOP_INT_BITXOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// invert
				case CALCOP_INT_INVERT: {
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = ~vmstack[stackpointer + x];
					}
					break;
					}
				// lshift
				case CALCOP_INT_LSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// rshift
				case CALCOP_INT_RSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// abs
				case CALCOP_INT_ABS: {
					break;
					}
				// math.factorial
				case CALCOP_INT_MATH_FACTORIAL: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_unsigned_long(vmstack[stackpointer + x], &errflag);
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_unsigned_long(vmstack[stackpointer + x], &errflag);
							if (errflag != 0) return CALC_ERR_ARITHMETIC;
						}
					}
					break;
					}

			}
			// Increment the op code index to the next instruction.
			opindex++;
		}

		// Store the calculation result.
		for(x = 0; x < slicestride; x++) {
			dataout[dataindex + x] = vmstack[stackpointer + x];
		}

		// Increment the data index array.
		dataindex = dataindex + vmstacksegments;

		// Count up the number of outer loops we need to go through.
		stridecounter++;

	}


	return CALC_NO_ERR;

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   codearraylen = The length of the byte code array.
   codearray = The array of byte codes.
   varoffsetsarray = The array of variable offsets.
   vararray = The array of variable values.
   constarray = The array of constant values.
   vmstack = The array used for the stack.
   vmstacksize = The maximum size of the stack provided.
   vmstacksegments = The number of stack "segments" used when interating in "chunks".
   disableovfl = If true, disable arithmetic overflow checking (default is false).
   Return = 0 if OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int exequation_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, signed long long *vararray, signed long long *constarray,
			signed long long *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl) {


	// Index into op code array.
	unsigned int opindex = 0;
	// Index into data array.
	Py_ssize_t dataindex = 0;
	// Keep track of number of loop iterations.
	Py_ssize_t looptarget, loopremainder;
	// The number of times through the outer loop.
	Py_ssize_t stridecounter = 0;


	unsigned int stackpointer, slicestride, x;

	signed long long dataouttmp;	// Used for overflow calculations.

	char errflag = 0;


	stackpointer = 0;

	// Number of full iterations through the outer loop required.
	looptarget = arraylen / vmstacksegments;
	// Number of array elements left over for the end of the array if the
	// array size is not evenly divisible.
	loopremainder = arraylen % vmstacksegments;


	// The outer loop covers the entire data array.
	while(dataindex < arraylen) {

		// Reset the op code index and stack pointer for the next iteration.
		opindex = 0;
		stackpointer = 0;

		// The number of elements we go through in the inner loop may be differnt
		// during the last iteration.
		if (stridecounter < looptarget) { 
			slicestride = vmstacksegments; 
		} else {
			slicestride = (unsigned int) loopremainder;
		}


		// We go through the bytes codes once in sequence.
		// The middle loop goes through the interpreter instructions.
		while(opindex < codearraylen) {

			switch (codearray[opindex]) {
				// unknown
				case CALCOP_INT_UNKNOWN: {
					return CALC_ERR_UNKNOWNOP;
					}
				// pusharray
				case CALCOP_INT_PUSHARRAY: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = data[dataindex + x];
					}
					break;
					}
				// pushvar
				case CALCOP_INT_PUSHVAR: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = vararray[varoffsetsarray[opindex]];
					}
					break;
					}
				// pushconst
				case CALCOP_INT_PUSHCONST: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = constarray[opindex];
					}
					break;
					}
				// add
				case CALCOP_INT_ADD: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > 0) && (vmstack[stackpointer + vmstacksegments + x] > (LLONG_MAX - vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] < 0) && (vmstack[stackpointer + vmstacksegments + x] < (LLONG_MIN - vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					}
					break;
					}
				// sub
				case CALCOP_INT_SUB: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > 0) && (vmstack[stackpointer + vmstacksegments + x] < (LLONG_MIN + vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] < 0) && (vmstack[stackpointer + vmstacksegments + x] > (LLONG_MAX + vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					}
					break;
					}
				// mult
				case CALCOP_INT_MULT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > 0) && ((vmstack[stackpointer + vmstacksegments + x] > (LLONG_MAX / vmstack[stackpointer + x])) || (vmstack[stackpointer + vmstacksegments + x] < (LLONG_MIN / vmstack[stackpointer + x])))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] < -1) && ((vmstack[stackpointer + vmstacksegments + x] < (LLONG_MAX / vmstack[stackpointer + x])) || (vmstack[stackpointer + vmstacksegments + x] > (LLONG_MIN / vmstack[stackpointer + x])))) {return CALC_ERR_OVFL;}
							if ((vmstack[stackpointer + x] == -1) && (vmstack[stackpointer + vmstacksegments + x] == LLONG_MIN)) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					}
					break;
					}
				// div
				case CALCOP_INT_DIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						// Cannot disable divide by zero checking because this causes a crash.
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							if ((vmstack[stackpointer + x] == -1) && (vmstack[stackpointer + vmstacksegments + x] == LLONG_MIN)) {return CALC_ERR_OVFL;}		// Overflow check.
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						}
					}
					break;
					}
				// floordiv
				case CALCOP_INT_FLOORDIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							dataouttmp = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
							// This check is required for floor division.
							if (((vmstack[stackpointer + vmstacksegments + x] < 0) != (vmstack[stackpointer + x] < 0)) && ((dataouttmp * vmstack[stackpointer + x]) != vmstack[stackpointer + vmstacksegments + x])) { 
								vmstack[stackpointer + x] = dataouttmp - 1; 
							} else {
								vmstack[stackpointer + x] = dataouttmp;
							}
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
							if ((vmstack[stackpointer + x] == -1) && (vmstack[stackpointer + vmstacksegments + x] == LLONG_MIN)) {return CALC_ERR_OVFL;}		// Overflow check.
							dataouttmp = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
							// This check is required for floor division.
							if (((vmstack[stackpointer + vmstacksegments + x] < 0) != (vmstack[stackpointer + x] < 0)) && ((dataouttmp * vmstack[stackpointer + x]) != vmstack[stackpointer + vmstacksegments + x])) { 
								vmstack[stackpointer + x] = dataouttmp - 1; 
							} else {
								vmstack[stackpointer + x] = dataouttmp;
							}
						}
					}
					break;
					}
				// mod
				case CALCOP_INT_MOD: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						dataouttmp = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						// This check is required for floor division.
						if (((vmstack[stackpointer + vmstacksegments + x] < 0) != (vmstack[stackpointer + x] < 0)) && ((dataouttmp * vmstack[stackpointer + x]) != vmstack[stackpointer + vmstacksegments + x])) { 
							dataouttmp = dataouttmp - 1;
						}
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x] * dataouttmp;
					}
					break;
					}
				// uadd
				case CALCOP_INT_UADD: {
					// No overflow checking required for this.
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = +vmstack[stackpointer + x];
					}
					break;
					}
				// usub
				case CALCOP_INT_USUB: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = -vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == LLONG_MIN) {return CALC_ERR_OVFL;}		// Overflow check.
							vmstack[stackpointer + x] = -vmstack[stackpointer + x];
						}
					}
					break;
					}
				// pow
				case CALCOP_INT_POW: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_signed_long_long(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_signed_long_long(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitand
				case CALCOP_INT_BITAND: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitor
				case CALCOP_INT_BITOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitxor
				case CALCOP_INT_BITXOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// invert
				case CALCOP_INT_INVERT: {
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = ~vmstack[stackpointer + x];
					}
					break;
					}
				// lshift
				case CALCOP_INT_LSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// rshift
				case CALCOP_INT_RSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// abs
				case CALCOP_INT_ABS: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + x] >= 0 ? vmstack[stackpointer + x] : -vmstack[stackpointer + x]; 
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + x] == LLONG_MIN) {return CALC_ERR_ARITHMETIC;}		// Overflow check.
							vmstack[stackpointer + x] = vmstack[stackpointer + x] >= 0 ? vmstack[stackpointer + x] : -vmstack[stackpointer + x]; 
						}
					}
					break;
					}
				// math.factorial
				case CALCOP_INT_MATH_FACTORIAL: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_signed_long_long(vmstack[stackpointer + x], &errflag);
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_signed_long_long(vmstack[stackpointer + x], &errflag);
							if (errflag != 0) return CALC_ERR_ARITHMETIC;
						}
					}
					break;
					}

			}
			// Increment the op code index to the next instruction.
			opindex++;
		}

		// Store the calculation result.
		for(x = 0; x < slicestride; x++) {
			dataout[dataindex + x] = vmstack[stackpointer + x];
		}

		// Increment the data index array.
		dataindex = dataindex + vmstacksegments;

		// Count up the number of outer loops we need to go through.
		stridecounter++;

	}


	return CALC_NO_ERR;

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   codearraylen = The length of the byte code array.
   codearray = The array of byte codes.
   varoffsetsarray = The array of variable offsets.
   vararray = The array of variable values.
   constarray = The array of constant values.
   vmstack = The array used for the stack.
   vmstacksize = The maximum size of the stack provided.
   vmstacksegments = The number of stack "segments" used when interating in "chunks".
   disableovfl = If true, disable arithmetic overflow checking (default is false).
   Return = 0 if OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int exequation_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, unsigned long long *vararray, unsigned long long *constarray,
			unsigned long long *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl) {


	// Index into op code array.
	unsigned int opindex = 0;
	// Index into data array.
	Py_ssize_t dataindex = 0;
	// Keep track of number of loop iterations.
	Py_ssize_t looptarget, loopremainder;
	// The number of times through the outer loop.
	Py_ssize_t stridecounter = 0;


	unsigned int stackpointer, slicestride, x;


	char errflag = 0;


	stackpointer = 0;

	// Number of full iterations through the outer loop required.
	looptarget = arraylen / vmstacksegments;
	// Number of array elements left over for the end of the array if the
	// array size is not evenly divisible.
	loopremainder = arraylen % vmstacksegments;


	// The outer loop covers the entire data array.
	while(dataindex < arraylen) {

		// Reset the op code index and stack pointer for the next iteration.
		opindex = 0;
		stackpointer = 0;

		// The number of elements we go through in the inner loop may be differnt
		// during the last iteration.
		if (stridecounter < looptarget) { 
			slicestride = vmstacksegments; 
		} else {
			slicestride = (unsigned int) loopremainder;
		}


		// We go through the bytes codes once in sequence.
		// The middle loop goes through the interpreter instructions.
		while(opindex < codearraylen) {

			switch (codearray[opindex]) {
				// unknown
				case CALCOP_INT_UNKNOWN: {
					return CALC_ERR_UNKNOWNOP;
					}
				// pusharray
				case CALCOP_INT_PUSHARRAY: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = data[dataindex + x];
					}
					break;
					}
				// pushvar
				case CALCOP_INT_PUSHVAR: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = vararray[varoffsetsarray[opindex]];
					}
					break;
					}
				// pushconst
				case CALCOP_INT_PUSHCONST: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = constarray[opindex];
					}
					break;
					}
				// add
				case CALCOP_INT_ADD: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + vmstacksegments + x] > (ULLONG_MAX - vmstack[stackpointer + x])) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					}
					break;
					}
				// sub
				case CALCOP_INT_SUB: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if (vmstack[stackpointer + vmstacksegments + x] < vmstack[stackpointer + x]) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					}
					break;
					}
				// mult
				case CALCOP_INT_MULT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] != 0) && (vmstack[stackpointer + vmstacksegments + x] > (ULLONG_MAX / vmstack[stackpointer + x]))) {return CALC_ERR_OVFL;}
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					}
					break;
					}
				// div
				case CALCOP_INT_DIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
					}
					break;
					}
				// floordiv
				case CALCOP_INT_FLOORDIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
					}
					break;
					}
				// mod
				case CALCOP_INT_MOD: {
					stackpointer = stackpointer - vmstacksegments;
					// Cannot disable divide by zero checking because this causes a crash.
					for(x = 0; x < slicestride; x++) {
						if (vmstack[stackpointer + x] == 0) {return CALC_ERR_OVFL;}		// Overflow check.
						vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] % vmstack[stackpointer + x];
					}
					break;
					}
				// uadd
				case CALCOP_INT_UADD: {
					// No overflow checking required for this.
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = +vmstack[stackpointer + x];
					}
					break;
					}
				// usub
				case CALCOP_INT_USUB: {
					return CALC_ERR_INVALIDOP;
					}
				// pow
				case CALCOP_INT_POW: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_unsigned_long_long(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = arith_pow_unsigned_long_long(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x], &errflag);
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitand
				case CALCOP_INT_BITAND: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] & vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitor
				case CALCOP_INT_BITOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] | vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// bitxor
				case CALCOP_INT_BITXOR: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] ^ vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// invert
				case CALCOP_INT_INVERT: {
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = ~vmstack[stackpointer + x];
					}
					break;
					}
				// lshift
				case CALCOP_INT_LSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] << vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// rshift
				case CALCOP_INT_RSHIFT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] >> vmstack[stackpointer + x];
							if (errflag != 0) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// abs
				case CALCOP_INT_ABS: {
					break;
					}
				// math.factorial
				case CALCOP_INT_MATH_FACTORIAL: {
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_unsigned_long_long(vmstack[stackpointer + x], &errflag);
						}
					} else {
					// Overflow checking enabled.
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = factorial_unsigned_long_long(vmstack[stackpointer + x], &errflag);
							if (errflag != 0) return CALC_ERR_ARITHMETIC;
						}
					}
					break;
					}

			}
			// Increment the op code index to the next instruction.
			opindex++;
		}

		// Store the calculation result.
		for(x = 0; x < slicestride; x++) {
			dataout[dataindex + x] = vmstack[stackpointer + x];
		}

		// Increment the data index array.
		dataindex = dataindex + vmstacksegments;

		// Count up the number of outer loops we need to go through.
		stridecounter++;

	}


	return CALC_NO_ERR;

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   codearraylen = The length of the byte code array.
   codearray = The array of byte codes.
   varoffsetsarray = The array of variable offsets.
   vararray = The array of variable values.
   constarray = The array of constant values.
   vmstack = The array used for the stack.
   vmstacksize = The maximum size of the stack provided.
   vmstacksegments = The number of stack "segments" used when interating in "chunks".
   disableovfl = If true, disable arithmetic overflow checking (default is false).
   Return = 0 if OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int exequation_float(Py_ssize_t arraylen, float *data, float *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, float *vararray, float *constarray,
			float *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl) {


	// Index into op code array.
	unsigned int opindex = 0;
	// Index into data array.
	Py_ssize_t dataindex = 0;
	// Keep track of number of loop iterations.
	Py_ssize_t looptarget, loopremainder;
	// The number of times through the outer loop.
	Py_ssize_t stridecounter = 0;


	unsigned int stackpointer, slicestride, x;




	stackpointer = 0;

	// Number of full iterations through the outer loop required.
	looptarget = arraylen / vmstacksegments;
	// Number of array elements left over for the end of the array if the
	// array size is not evenly divisible.
	loopremainder = arraylen % vmstacksegments;


	// The outer loop covers the entire data array.
	while(dataindex < arraylen) {

		// Reset the op code index and stack pointer for the next iteration.
		opindex = 0;
		stackpointer = 0;

		// The number of elements we go through in the inner loop may be differnt
		// during the last iteration.
		if (stridecounter < looptarget) { 
			slicestride = vmstacksegments; 
		} else {
			slicestride = (unsigned int) loopremainder;
		}


		// We go through the bytes codes once in sequence.
		// The middle loop goes through the interpreter instructions.
		while(opindex < codearraylen) {

			switch (codearray[opindex]) {
				// unknown
				case CALCOP_FLOAT_UNKNOWN: {
					return CALC_ERR_UNKNOWNOP;
					}
				// pusharray
				case CALCOP_FLOAT_PUSHARRAY: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = data[dataindex + x];
					}
					break;
					}
				// pushvar
				case CALCOP_FLOAT_PUSHVAR: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = vararray[varoffsetsarray[opindex]];
					}
					break;
					}
				// pushconst
				case CALCOP_FLOAT_PUSHCONST: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = constarray[opindex];
					}
					break;
					}
				// add
				case CALCOP_FLOAT_ADD: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// sub
				case CALCOP_FLOAT_SUB: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// mult
				case CALCOP_FLOAT_MULT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// div
				case CALCOP_FLOAT_DIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// floordiv
				case CALCOP_FLOAT_FLOORDIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = floorf(vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = floorf(vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// mod
				case CALCOP_FLOAT_MOD: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x] * floorf(vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x] * floorf(vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// uadd
				case CALCOP_FLOAT_UADD: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = +vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = +vmstack[stackpointer + x];
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// usub
				case CALCOP_FLOAT_USUB: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = -vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = -vmstack[stackpointer + x];
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// pow
				case CALCOP_FLOAT_POW: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = powf(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = powf(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// abs
				case CALCOP_FLOAT_ABS: {
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = fabsf(vmstack[stackpointer + x]);
					}
					break;
					}
				// math.acos
				case CALCOP_FLOAT_MATH_ACOS: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = acosf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = acosf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.acosh
				case CALCOP_FLOAT_MATH_ACOSH: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = acoshf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = acoshf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}
				// math.asin
				case CALCOP_FLOAT_MATH_ASIN: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = asinf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = asinf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.asinh
				case CALCOP_FLOAT_MATH_ASINH: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = asinhf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = asinhf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}
				// math.atan
				case CALCOP_FLOAT_MATH_ATAN: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = atanf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = atanf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.atan2
				case CALCOP_FLOAT_MATH_ATAN2: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = atan2f(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = atan2f(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// math.atanh
				case CALCOP_FLOAT_MATH_ATANH: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = atanhf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = atanhf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}
				// math.ceil
				case CALCOP_FLOAT_MATH_CEIL: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = ceilf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = ceilf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.copysign
				case CALCOP_FLOAT_MATH_COPYSIGN: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = copysignf(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = copysignf(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// math.cos
				case CALCOP_FLOAT_MATH_COS: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = cosf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = cosf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.cosh
				case CALCOP_FLOAT_MATH_COSH: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = coshf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = coshf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.degrees
				case CALCOP_FLOAT_MATH_DEGREES: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = radtodeg_f * vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = radtodeg_f * vmstack[stackpointer + x];
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.erf
				case CALCOP_FLOAT_MATH_ERF: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = erff(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = erff(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}
				// math.erfc
				case CALCOP_FLOAT_MATH_ERFC: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = erfcf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = erfcf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}
				// math.exp
				case CALCOP_FLOAT_MATH_EXP: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = expf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = expf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.expm1
				case CALCOP_FLOAT_MATH_EXPM1: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = expm1f(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = expm1f(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}
				// math.fabs
				case CALCOP_FLOAT_MATH_FABS: {
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = fabsf(vmstack[stackpointer + x]);
					}
					break;
					}
				// math.floor
				case CALCOP_FLOAT_MATH_FLOOR: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = floorf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = floorf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.fmod
				case CALCOP_FLOAT_MATH_FMOD: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = fmodf(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = fmodf(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// math.gamma
				case CALCOP_FLOAT_MATH_GAMMA: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = tgammaf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = tgammaf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}
				// math.hypot
				case CALCOP_FLOAT_MATH_HYPOT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = hypotf(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = hypotf(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// math.ldexp
				case CALCOP_FLOAT_MATH_LDEXP: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = ldexpf(vmstack[stackpointer + vmstacksegments + x], (int) vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > INT_MAX) || (vmstack[stackpointer + x] < INT_MIN)) {
								return CALC_ERR_OVFL;
							}
							vmstack[stackpointer + x] = ldexpf(vmstack[stackpointer + vmstacksegments + x], (int) vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// math.lgamma
				case CALCOP_FLOAT_MATH_LGAMMA: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = lgammaf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = lgammaf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}
				// math.log
				case CALCOP_FLOAT_MATH_LOG: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = logf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = logf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.log10
				case CALCOP_FLOAT_MATH_LOG10: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = log10f(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = log10f(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.log1p
				case CALCOP_FLOAT_MATH_LOG1P: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = log1pf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = log1pf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}
				// math.pow
				case CALCOP_FLOAT_MATH_POW: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = powf(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = powf(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// math.radians
				case CALCOP_FLOAT_MATH_RADIANS: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = degtorad_f * vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = degtorad_f * vmstack[stackpointer + x];
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.sin
				case CALCOP_FLOAT_MATH_SIN: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = sinf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = sinf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.sinh
				case CALCOP_FLOAT_MATH_SINH: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = sinhf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = sinhf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.sqrt
				case CALCOP_FLOAT_MATH_SQRT: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = sqrtf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = sqrtf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.tan
				case CALCOP_FLOAT_MATH_TAN: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = tanf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = tanf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.tanh
				case CALCOP_FLOAT_MATH_TANH: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = tanhf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = tanhf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.trunc
				case CALCOP_FLOAT_MATH_TRUNC: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = truncf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = truncf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}

			}
			// Increment the op code index to the next instruction.
			opindex++;
		}

		// Store the calculation result.
		for(x = 0; x < slicestride; x++) {
			dataout[dataindex + x] = vmstack[stackpointer + x];
		}

		// Increment the data index array.
		dataindex = dataindex + vmstacksegments;

		// Count up the number of outer loops we need to go through.
		stridecounter++;

	}


	return CALC_NO_ERR;

}
/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   codearraylen = The length of the byte code array.
   codearray = The array of byte codes.
   varoffsetsarray = The array of variable offsets.
   vararray = The array of variable values.
   constarray = The array of constant values.
   vmstack = The array used for the stack.
   vmstacksize = The maximum size of the stack provided.
   vmstacksegments = The number of stack "segments" used when interating in "chunks".
   disableovfl = If true, disable arithmetic overflow checking (default is false).
   Return = 0 if OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int exequation_double(Py_ssize_t arraylen, double *data, double *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, double *vararray, double *constarray,
			double *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl) {


	// Index into op code array.
	unsigned int opindex = 0;
	// Index into data array.
	Py_ssize_t dataindex = 0;
	// Keep track of number of loop iterations.
	Py_ssize_t looptarget, loopremainder;
	// The number of times through the outer loop.
	Py_ssize_t stridecounter = 0;


	unsigned int stackpointer, slicestride, x;




	stackpointer = 0;

	// Number of full iterations through the outer loop required.
	looptarget = arraylen / vmstacksegments;
	// Number of array elements left over for the end of the array if the
	// array size is not evenly divisible.
	loopremainder = arraylen % vmstacksegments;


	// The outer loop covers the entire data array.
	while(dataindex < arraylen) {

		// Reset the op code index and stack pointer for the next iteration.
		opindex = 0;
		stackpointer = 0;

		// The number of elements we go through in the inner loop may be differnt
		// during the last iteration.
		if (stridecounter < looptarget) { 
			slicestride = vmstacksegments; 
		} else {
			slicestride = (unsigned int) loopremainder;
		}


		// We go through the bytes codes once in sequence.
		// The middle loop goes through the interpreter instructions.
		while(opindex < codearraylen) {

			switch (codearray[opindex]) {
				// unknown
				case CALCOP_FLOAT_UNKNOWN: {
					return CALC_ERR_UNKNOWNOP;
					}
				// pusharray
				case CALCOP_FLOAT_PUSHARRAY: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = data[dataindex + x];
					}
					break;
					}
				// pushvar
				case CALCOP_FLOAT_PUSHVAR: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = vararray[varoffsetsarray[opindex]];
					}
					break;
					}
				// pushconst
				case CALCOP_FLOAT_PUSHCONST: {
					stackpointer = stackpointer + vmstacksegments;
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = constarray[opindex];
					}
					break;
					}
				// add
				case CALCOP_FLOAT_ADD: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] + vmstack[stackpointer + x];
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// sub
				case CALCOP_FLOAT_SUB: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x];
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// mult
				case CALCOP_FLOAT_MULT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] * vmstack[stackpointer + x];
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// div
				case CALCOP_FLOAT_DIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x];
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// floordiv
				case CALCOP_FLOAT_FLOORDIV: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = floor(vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = floor(vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// mod
				case CALCOP_FLOAT_MOD: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x] * floor(vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = vmstack[stackpointer + vmstacksegments + x] - vmstack[stackpointer + x] * floor(vmstack[stackpointer + vmstacksegments + x] / vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// uadd
				case CALCOP_FLOAT_UADD: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = +vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = +vmstack[stackpointer + x];
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// usub
				case CALCOP_FLOAT_USUB: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = -vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = -vmstack[stackpointer + x];
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// pow
				case CALCOP_FLOAT_POW: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = pow(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = pow(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// abs
				case CALCOP_FLOAT_ABS: {
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = fabs(vmstack[stackpointer + x]);
					}
					break;
					}
				// math.acos
				case CALCOP_FLOAT_MATH_ACOS: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = acos(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = acos(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.acosh
				case CALCOP_FLOAT_MATH_ACOSH: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = acosh(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = acosh(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}
				// math.asin
				case CALCOP_FLOAT_MATH_ASIN: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = asin(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = asin(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.asinh
				case CALCOP_FLOAT_MATH_ASINH: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = asinh(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = asinh(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}
				// math.atan
				case CALCOP_FLOAT_MATH_ATAN: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = atan(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = atan(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.atan2
				case CALCOP_FLOAT_MATH_ATAN2: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = atan2(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = atan2(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// math.atanh
				case CALCOP_FLOAT_MATH_ATANH: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = atanh(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = atanh(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}
				// math.ceil
				case CALCOP_FLOAT_MATH_CEIL: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = ceil(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = ceil(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.copysign
				case CALCOP_FLOAT_MATH_COPYSIGN: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = copysign(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = copysign(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// math.cos
				case CALCOP_FLOAT_MATH_COS: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = cos(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = cos(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.cosh
				case CALCOP_FLOAT_MATH_COSH: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = cosh(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = cosh(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.degrees
				case CALCOP_FLOAT_MATH_DEGREES: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = radtodeg_d * vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = radtodeg_d * vmstack[stackpointer + x];
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.erf
				case CALCOP_FLOAT_MATH_ERF: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = erf(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = erf(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}
				// math.erfc
				case CALCOP_FLOAT_MATH_ERFC: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = erfc(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = erfc(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}
				// math.exp
				case CALCOP_FLOAT_MATH_EXP: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = exp(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = exp(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.expm1
				case CALCOP_FLOAT_MATH_EXPM1: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = expm1(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = expm1(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}
				// math.fabs
				case CALCOP_FLOAT_MATH_FABS: {
					for(x = 0; x < slicestride; x++) {
						vmstack[stackpointer + x] = fabs(vmstack[stackpointer + x]);
					}
					break;
					}
				// math.floor
				case CALCOP_FLOAT_MATH_FLOOR: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = floor(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = floor(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.fmod
				case CALCOP_FLOAT_MATH_FMOD: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = fmod(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = fmod(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// math.gamma
				case CALCOP_FLOAT_MATH_GAMMA: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = tgamma(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = tgamma(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}
				// math.hypot
				case CALCOP_FLOAT_MATH_HYPOT: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = hypot(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = hypot(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// math.ldexp
				case CALCOP_FLOAT_MATH_LDEXP: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = ldexp(vmstack[stackpointer + vmstacksegments + x], (int) vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							if ((vmstack[stackpointer + x] > INT_MAX) || (vmstack[stackpointer + x] < INT_MIN)) {
								return CALC_ERR_OVFL;
							}
							vmstack[stackpointer + x] = ldexp(vmstack[stackpointer + vmstacksegments + x], (int) vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// math.lgamma
				case CALCOP_FLOAT_MATH_LGAMMA: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = lgamma(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = lgamma(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}
				// math.log
				case CALCOP_FLOAT_MATH_LOG: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = log(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = log(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.log10
				case CALCOP_FLOAT_MATH_LOG10: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = log10(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = log10(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.log1p
				case CALCOP_FLOAT_MATH_LOG1P: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = log1p(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = log1p(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}
				// math.pow
				case CALCOP_FLOAT_MATH_POW: {
					stackpointer = stackpointer - vmstacksegments;
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = pow(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = pow(vmstack[stackpointer + vmstacksegments + x], vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break;
					}
				// math.radians
				case CALCOP_FLOAT_MATH_RADIANS: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = degtorad_d * vmstack[stackpointer + x];
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = degtorad_d * vmstack[stackpointer + x];
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.sin
				case CALCOP_FLOAT_MATH_SIN: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = sin(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = sin(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.sinh
				case CALCOP_FLOAT_MATH_SINH: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = sinh(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = sinh(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.sqrt
				case CALCOP_FLOAT_MATH_SQRT: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = sqrt(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = sqrt(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.tan
				case CALCOP_FLOAT_MATH_TAN: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = tan(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = tan(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.tanh
				case CALCOP_FLOAT_MATH_TANH: { 
					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = tanh(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = tanh(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					}
				// math.trunc
				case CALCOP_FLOAT_MATH_TRUNC: { 
					// This op is not supported by MSVC 2010.
					#ifdef _MSC_VER
						return ARR_ERR_PLATFORM;
					#else

					// Overflow checking disabled.
					if (disableovfl) {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = trunc(vmstack[stackpointer + x]);
						}
					} else {
						for(x = 0; x < slicestride; x++) {
							vmstack[stackpointer + x] = trunc(vmstack[stackpointer + x]);
							if (!isfinite(vmstack[stackpointer + x])) {return CALC_ERR_ARITHMETIC;}
						}
					}
					break; 
					#endif

					}

			}
			// Increment the op code index to the next instruction.
			opindex++;
		}

		// Store the calculation result.
		for(x = 0; x < slicestride; x++) {
			dataout[dataindex + x] = vmstack[stackpointer + x];
		}

		// Increment the data index array.
		dataindex = dataindex + vmstacksegments;

		// Count up the number of outer loops we need to go through.
		stridecounter++;

	}


	return CALC_NO_ERR;

}
/*--------------------------------------------------------------------------- */

