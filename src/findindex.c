//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   findindex.c
// Purpose:  Calculate the findindex of values in an array.
// Language: C
// Date:     15-Nov-2017.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2020    Michael Griffin    <m12.griffin@gmail.com>
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

#include <limits.h>
#include <math.h>

#include "arrayerrs.h"

#include "arrayparams_base.h"
#include "arrayops.h"

#include "arrayparams_allany.h"

#include "simddefs.h"

#ifdef AF_HASSIMD_X86
#include "findindex_simd_x86.h"
#endif

#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
#include "arm_neon.h"
#endif

#if defined(AF_HASSIMD_ARMv7_32BIT)
#include "findindex_simd_armv7.h"
#endif

#if defined(AF_HASSIMD_ARM_AARCH64)
#include "findindex_simd_armv8.h"
#endif


/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_eq_signed_char(Py_ssize_t arraylen, signed char *data, signed char param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_gt_signed_char(Py_ssize_t arraylen, signed char *data, signed char param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ge_signed_char(Py_ssize_t arraylen, signed char *data, signed char param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_lt_signed_char(Py_ssize_t arraylen, signed char *data, signed char param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_le_signed_char(Py_ssize_t arraylen, signed char *data, signed char param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ne_signed_char(Py_ssize_t arraylen, signed char *data, signed char param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
Py_ssize_t findindex_select_signed_char(signed int opcode, Py_ssize_t arraylen, unsigned int nosimd, signed char *data, signed char param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
				return findindex_eq_signed_char_simd(arraylen, data, param1);
			}
#endif
			return findindex_eq_signed_char(arraylen, data, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
				return findindex_gt_signed_char_simd(arraylen, data, param1);
			}
#endif
			return findindex_gt_signed_char(arraylen, data, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
				return findindex_ge_signed_char_simd(arraylen, data, param1);
			}
#endif
			return findindex_ge_signed_char(arraylen, data, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
				return findindex_lt_signed_char_simd(arraylen, data, param1);
			}
#endif
			return findindex_lt_signed_char(arraylen, data, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
				return findindex_le_signed_char_simd(arraylen, data, param1);
			}
#endif
			return findindex_le_signed_char(arraylen, data, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
				return findindex_ne_signed_char_simd(arraylen, data, param1);
			}
#endif
			return findindex_ne_signed_char(arraylen, data, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_eq_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_gt_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ge_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_lt_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_le_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ne_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
Py_ssize_t findindex_select_unsigned_char(signed int opcode, Py_ssize_t arraylen, unsigned int nosimd, unsigned char *data, unsigned char param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
				return findindex_eq_unsigned_char_simd(arraylen, data, param1);
			}
#endif
			return findindex_eq_unsigned_char(arraylen, data, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
				return findindex_gt_unsigned_char_simd(arraylen, data, param1);
			}
#endif
			return findindex_gt_unsigned_char(arraylen, data, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
				return findindex_ge_unsigned_char_simd(arraylen, data, param1);
			}
#endif
			return findindex_ge_unsigned_char(arraylen, data, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
				return findindex_lt_unsigned_char_simd(arraylen, data, param1);
			}
#endif
			return findindex_lt_unsigned_char(arraylen, data, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
				return findindex_le_unsigned_char_simd(arraylen, data, param1);
			}
#endif
			return findindex_le_unsigned_char(arraylen, data, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
				return findindex_ne_unsigned_char_simd(arraylen, data, param1);
			}
#endif
			return findindex_ne_unsigned_char(arraylen, data, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_eq_signed_short(Py_ssize_t arraylen, signed short *data, signed short param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_gt_signed_short(Py_ssize_t arraylen, signed short *data, signed short param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ge_signed_short(Py_ssize_t arraylen, signed short *data, signed short param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_lt_signed_short(Py_ssize_t arraylen, signed short *data, signed short param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_le_signed_short(Py_ssize_t arraylen, signed short *data, signed short param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ne_signed_short(Py_ssize_t arraylen, signed short *data, signed short param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
Py_ssize_t findindex_select_signed_short(signed int opcode, Py_ssize_t arraylen, unsigned int nosimd, signed short *data, signed short param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
				return findindex_eq_signed_short_simd(arraylen, data, param1);
			}
#endif
			return findindex_eq_signed_short(arraylen, data, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
				return findindex_gt_signed_short_simd(arraylen, data, param1);
			}
#endif
			return findindex_gt_signed_short(arraylen, data, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
				return findindex_ge_signed_short_simd(arraylen, data, param1);
			}
#endif
			return findindex_ge_signed_short(arraylen, data, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
				return findindex_lt_signed_short_simd(arraylen, data, param1);
			}
#endif
			return findindex_lt_signed_short(arraylen, data, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
				return findindex_le_signed_short_simd(arraylen, data, param1);
			}
#endif
			return findindex_le_signed_short(arraylen, data, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
				return findindex_ne_signed_short_simd(arraylen, data, param1);
			}
#endif
			return findindex_ne_signed_short(arraylen, data, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_eq_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_gt_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ge_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_lt_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_le_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ne_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
Py_ssize_t findindex_select_unsigned_short(signed int opcode, Py_ssize_t arraylen, unsigned int nosimd, unsigned short *data, unsigned short param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
				return findindex_eq_unsigned_short_simd(arraylen, data, param1);
			}
#endif
			return findindex_eq_unsigned_short(arraylen, data, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
				return findindex_gt_unsigned_short_simd(arraylen, data, param1);
			}
#endif
			return findindex_gt_unsigned_short(arraylen, data, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
				return findindex_ge_unsigned_short_simd(arraylen, data, param1);
			}
#endif
			return findindex_ge_unsigned_short(arraylen, data, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
				return findindex_lt_unsigned_short_simd(arraylen, data, param1);
			}
#endif
			return findindex_lt_unsigned_short(arraylen, data, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
				return findindex_le_unsigned_short_simd(arraylen, data, param1);
			}
#endif
			return findindex_le_unsigned_short(arraylen, data, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
				return findindex_ne_unsigned_short_simd(arraylen, data, param1);
			}
#endif
			return findindex_ne_unsigned_short(arraylen, data, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_eq_signed_int(Py_ssize_t arraylen, signed int *data, signed int param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_gt_signed_int(Py_ssize_t arraylen, signed int *data, signed int param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ge_signed_int(Py_ssize_t arraylen, signed int *data, signed int param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_lt_signed_int(Py_ssize_t arraylen, signed int *data, signed int param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_le_signed_int(Py_ssize_t arraylen, signed int *data, signed int param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ne_signed_int(Py_ssize_t arraylen, signed int *data, signed int param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
Py_ssize_t findindex_select_signed_int(signed int opcode, Py_ssize_t arraylen, unsigned int nosimd, signed int *data, signed int param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
				return findindex_eq_signed_int_simd(arraylen, data, param1);
			}
#endif
			return findindex_eq_signed_int(arraylen, data, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
				return findindex_gt_signed_int_simd(arraylen, data, param1);
			}
#endif
			return findindex_gt_signed_int(arraylen, data, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
				return findindex_ge_signed_int_simd(arraylen, data, param1);
			}
#endif
			return findindex_ge_signed_int(arraylen, data, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
				return findindex_lt_signed_int_simd(arraylen, data, param1);
			}
#endif
			return findindex_lt_signed_int(arraylen, data, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
				return findindex_le_signed_int_simd(arraylen, data, param1);
			}
#endif
			return findindex_le_signed_int(arraylen, data, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
				return findindex_ne_signed_int_simd(arraylen, data, param1);
			}
#endif
			return findindex_ne_signed_int(arraylen, data, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_eq_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_gt_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ge_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_lt_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_le_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ne_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
Py_ssize_t findindex_select_unsigned_int(signed int opcode, Py_ssize_t arraylen, unsigned int nosimd, unsigned int *data, unsigned int param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
				return findindex_eq_unsigned_int_simd(arraylen, data, param1);
			}
#endif
			return findindex_eq_unsigned_int(arraylen, data, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
				return findindex_gt_unsigned_int_simd(arraylen, data, param1);
			}
#endif
			return findindex_gt_unsigned_int(arraylen, data, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
				return findindex_ge_unsigned_int_simd(arraylen, data, param1);
			}
#endif
			return findindex_ge_unsigned_int(arraylen, data, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
				return findindex_lt_unsigned_int_simd(arraylen, data, param1);
			}
#endif
			return findindex_lt_unsigned_int(arraylen, data, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
				return findindex_le_unsigned_int_simd(arraylen, data, param1);
			}
#endif
			return findindex_le_unsigned_int(arraylen, data, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
				return findindex_ne_unsigned_int_simd(arraylen, data, param1);
			}
#endif
			return findindex_ne_unsigned_int(arraylen, data, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: l
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_eq_signed_long(Py_ssize_t arraylen, signed long *data, signed long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: l
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_gt_signed_long(Py_ssize_t arraylen, signed long *data, signed long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: l
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ge_signed_long(Py_ssize_t arraylen, signed long *data, signed long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: l
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_lt_signed_long(Py_ssize_t arraylen, signed long *data, signed long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: l
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_le_signed_long(Py_ssize_t arraylen, signed long *data, signed long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: l
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ne_signed_long(Py_ssize_t arraylen, signed long *data, signed long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: l
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
Py_ssize_t findindex_select_signed_long(signed int opcode, Py_ssize_t arraylen, unsigned int nosimd, signed long *data, signed long param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {

			return findindex_eq_signed_long(arraylen, data, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {

			return findindex_gt_signed_long(arraylen, data, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {

			return findindex_ge_signed_long(arraylen, data, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {

			return findindex_lt_signed_long(arraylen, data, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {

			return findindex_le_signed_long(arraylen, data, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {

			return findindex_ne_signed_long(arraylen, data, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: L
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_eq_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: L
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_gt_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: L
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ge_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: L
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_lt_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: L
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_le_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: L
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ne_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: L
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
Py_ssize_t findindex_select_unsigned_long(signed int opcode, Py_ssize_t arraylen, unsigned int nosimd, unsigned long *data, unsigned long param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {

			return findindex_eq_unsigned_long(arraylen, data, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {

			return findindex_gt_unsigned_long(arraylen, data, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {

			return findindex_ge_unsigned_long(arraylen, data, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {

			return findindex_lt_unsigned_long(arraylen, data, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {

			return findindex_le_unsigned_long(arraylen, data, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {

			return findindex_ne_unsigned_long(arraylen, data, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: q
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_eq_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: q
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_gt_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: q
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ge_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: q
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_lt_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: q
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_le_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: q
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ne_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: q
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
Py_ssize_t findindex_select_signed_long_long(signed int opcode, Py_ssize_t arraylen, unsigned int nosimd, signed long long *data, signed long long param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {

			return findindex_eq_signed_long_long(arraylen, data, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {

			return findindex_gt_signed_long_long(arraylen, data, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {

			return findindex_ge_signed_long_long(arraylen, data, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {

			return findindex_lt_signed_long_long(arraylen, data, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {

			return findindex_le_signed_long_long(arraylen, data, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {

			return findindex_ne_signed_long_long(arraylen, data, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: Q
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_eq_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: Q
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_gt_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: Q
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ge_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: Q
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_lt_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: Q
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_le_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: Q
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ne_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: Q
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
Py_ssize_t findindex_select_unsigned_long_long(signed int opcode, Py_ssize_t arraylen, unsigned int nosimd, unsigned long long *data, unsigned long long param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {

			return findindex_eq_unsigned_long_long(arraylen, data, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {

			return findindex_gt_unsigned_long_long(arraylen, data, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {

			return findindex_ge_unsigned_long_long(arraylen, data, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {

			return findindex_lt_unsigned_long_long(arraylen, data, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {

			return findindex_le_unsigned_long_long(arraylen, data, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {

			return findindex_ne_unsigned_long_long(arraylen, data, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_eq_float(Py_ssize_t arraylen, float *data, float param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_gt_float(Py_ssize_t arraylen, float *data, float param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ge_float(Py_ssize_t arraylen, float *data, float param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_lt_float(Py_ssize_t arraylen, float *data, float param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_le_float(Py_ssize_t arraylen, float *data, float param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ne_float(Py_ssize_t arraylen, float *data, float param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
Py_ssize_t findindex_select_float(signed int opcode, Py_ssize_t arraylen, unsigned int nosimd, float *data, float param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (FLOATSIMDSIZE * 2))) {
				return findindex_eq_float_simd(arraylen, data, param1);
			}
#endif
			return findindex_eq_float(arraylen, data, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (FLOATSIMDSIZE * 2))) {
				return findindex_gt_float_simd(arraylen, data, param1);
			}
#endif
			return findindex_gt_float(arraylen, data, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (FLOATSIMDSIZE * 2))) {
				return findindex_ge_float_simd(arraylen, data, param1);
			}
#endif
			return findindex_ge_float(arraylen, data, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (FLOATSIMDSIZE * 2))) {
				return findindex_lt_float_simd(arraylen, data, param1);
			}
#endif
			return findindex_lt_float(arraylen, data, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (FLOATSIMDSIZE * 2))) {
				return findindex_le_float_simd(arraylen, data, param1);
			}
#endif
			return findindex_le_float(arraylen, data, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
			// SIMD version.
			if (!nosimd && (arraylen >= (FLOATSIMDSIZE * 2))) {
				return findindex_ne_float_simd(arraylen, data, param1);
			}
#endif
			return findindex_ne_float(arraylen, data, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: d
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_eq_double(Py_ssize_t arraylen, double *data, double param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: d
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_gt_double(Py_ssize_t arraylen, double *data, double param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: d
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ge_double(Py_ssize_t arraylen, double *data, double param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: d
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_lt_double(Py_ssize_t arraylen, double *data, double param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: d
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_le_double(Py_ssize_t arraylen, double *data, double param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: d
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
Py_ssize_t findindex_ne_double(Py_ssize_t arraylen, double *data, double param1) { 
	// array index counter.
	Py_ssize_t index;

		for (index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;

}

/*--------------------------------------------------------------------------- */
/* For array code: d
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
Py_ssize_t findindex_select_double(signed int opcode, Py_ssize_t arraylen, unsigned int nosimd, double *data, double param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
#if defined(AF_HASSIMD_X86)
			// SIMD version.
			if (!nosimd && (arraylen >= (DOUBLESIMDSIZE * 2))) {
				return findindex_eq_double_simd(arraylen, data, param1);
			}
#endif
			return findindex_eq_double(arraylen, data, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
#if defined(AF_HASSIMD_X86)
			// SIMD version.
			if (!nosimd && (arraylen >= (DOUBLESIMDSIZE * 2))) {
				return findindex_gt_double_simd(arraylen, data, param1);
			}
#endif
			return findindex_gt_double(arraylen, data, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
#if defined(AF_HASSIMD_X86)
			// SIMD version.
			if (!nosimd && (arraylen >= (DOUBLESIMDSIZE * 2))) {
				return findindex_ge_double_simd(arraylen, data, param1);
			}
#endif
			return findindex_ge_double(arraylen, data, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
#if defined(AF_HASSIMD_X86)
			// SIMD version.
			if (!nosimd && (arraylen >= (DOUBLESIMDSIZE * 2))) {
				return findindex_lt_double_simd(arraylen, data, param1);
			}
#endif
			return findindex_lt_double(arraylen, data, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
#if defined(AF_HASSIMD_X86)
			// SIMD version.
			if (!nosimd && (arraylen >= (DOUBLESIMDSIZE * 2))) {
				return findindex_le_double_simd(arraylen, data, param1);
			}
#endif
			return findindex_le_double(arraylen, data, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
#if defined(AF_HASSIMD_X86)
			// SIMD version.
			if (!nosimd && (arraylen >= (DOUBLESIMDSIZE * 2))) {
				return findindex_ne_double_simd(arraylen, data, param1);
			}
#endif
			return findindex_ne_double(arraylen, data, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_findindex(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	Py_ssize_t resultcode = 0;

	// This is used to hold the parsed parameters.
	struct args_params_allany arraydata = ARGSINIT_ALLANY;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_allany(self, args, keywds, "findindex");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}


	// The length of the data array.
	if (arraydata.arraylength < 1) {
		// Release the buffers. 
		releasebuffers_allany(arraydata);
		ErrMsgArrayLengthErr();
		return NULL;
	}



	/* Call the C function */
	switch(arraydata.arraytype) {
		// signed char
		case 'b' : {
			resultcode = findindex_select_signed_char(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.b, arraydata.param.b);
			break;
		}
		// unsigned char
		case 'B' : {
			resultcode = findindex_select_unsigned_char(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.B, arraydata.param.B);
			break;
		}
		// signed short
		case 'h' : {
			resultcode = findindex_select_signed_short(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.h, arraydata.param.h);
			break;
		}
		// unsigned short
		case 'H' : {
			resultcode = findindex_select_unsigned_short(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.H, arraydata.param.H);
			break;
		}
		// signed int
		case 'i' : {
			resultcode = findindex_select_signed_int(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.i, arraydata.param.i);
			break;
		}
		// unsigned int
		case 'I' : {
			resultcode = findindex_select_unsigned_int(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.I, arraydata.param.I);
			break;
		}
		// signed long
		case 'l' : {
			resultcode = findindex_select_signed_long(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.l, arraydata.param.l);
			break;
		}
		// unsigned long
		case 'L' : {
			resultcode = findindex_select_unsigned_long(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.L, arraydata.param.L);
			break;
		}
		// signed long long
		case 'q' : {
			resultcode = findindex_select_signed_long_long(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.q, arraydata.param.q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultcode = findindex_select_unsigned_long_long(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.Q, arraydata.param.Q);
			break;
		}
		// float
		case 'f' : {
			resultcode = findindex_select_float(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.f, arraydata.param.f);
			break;
		}
		// double
		case 'd' : {
			resultcode = findindex_select_double(arraydata.opcode, arraydata.arraylength, arraydata.nosimd, arraydata.array1.d, arraydata.param.d);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_allany(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_allany(arraydata);


	// Signal the errors.
	if (resultcode == ARR_ERR_INVALIDOP) {
		ErrMsgOperatorNotValidforthisFunction();
		return NULL;
	}



	// Adjust the result code if the data was not found, so that we don't leak
	// internal error codes to user space (and cause problems if they change).
	if (resultcode < 0) {
		resultcode = -1;
	}

	// Return the number of items filtered through.
	return PyLong_FromSsize_t(resultcode);


}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(findindex__doc__,
"findindex \n\
_____________________________ \n\
\n\
Calculate findindex over the values in an array.  \n\
\n\
======================  ============================================== \n\
Equivalent to:          [x for x,y in enumerate(array) if y > param][0] \n\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
  result = findindex(opstr, array, param) \n\
  result = findindex(opstr, array, param, maxlen=y) \n\
  result = findindex(opstr, array, param, nosimd=False) \n\
\n\
* opstr - The arithmetic comparison operation as a string. \n\
          These are: '==', '>', '>=', '<', '<=', '!='. \n\
* array - The input data array to be examined. \n\
* param - A non-array numeric parameter. \n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored. \n\
* nosimd - If True, SIMD acceleration is disabled if present. \n\
  The default is False (SIMD acceleration is enabled if present). \n\
* result - The resulting index. This will be negative if no match was found. \n\
");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "findindex" is the name seen inside of Python. 
 "py_findindex" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef findindex_methods[] = {
	{"findindex",  (PyCFunction)py_findindex, METH_VARARGS | METH_KEYWORDS, findindex__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef findindexmodule = {
    PyModuleDef_HEAD_INIT,
    "findindex",
    NULL,
    -1,
    findindex_methods
};

PyMODINIT_FUNC PyInit_findindex(void)
{
    return PyModule_Create(&findindexmodule);
};

/*--------------------------------------------------------------------------- */

