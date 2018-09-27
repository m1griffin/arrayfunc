//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   aany_common.c
// Purpose:  Returns True if any elements in an array meet the selected criteria.
//           Common platform independent code.
// Language: C
// Date:     08-May-2014
// Ver:      19-Jun-2018.
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

/*--------------------------------------------------------------------------- */
// This must be defined before "Python.h" in order for the pointers in the
// argument parsing functions to work properly. 
#define PY_SSIZE_T_CLEAN

#include "Python.h"

#include "arrayparams_base.h"
#include "arrayops.h"
#include "simddefs.h"
#ifdef AF_HASSIMD
#include "aany_simd_x86.h"
#endif

#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// Auto generated code goes below.

/*--------------------------------------------------------------------------- */
/* For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns 1 if the condition was true at least once, ARR_ERR_NOTFOUND,
		if it was not found, or an error code if the opcode was invalid.
*/
signed int aany_signed_char(signed int opcode, Py_ssize_t arraylen, signed char *data, signed char param1, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t index; 

#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
		return aany_signed_char_simd(opcode, arraylen, data, param1);
	}
#endif

	switch(opcode) {
	// AF_EQ
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GT
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GTE
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LT
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LTE
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_NE
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
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
   Returns 1 if the condition was true at least once, ARR_ERR_NOTFOUND,
		if it was not found, or an error code if the opcode was invalid.
*/
signed int aany_unsigned_char(signed int opcode, Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
	// AF_EQ
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GT
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GTE
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LT
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LTE
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_NE
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
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
   Returns 1 if the condition was true at least once, ARR_ERR_NOTFOUND,
		if it was not found, or an error code if the opcode was invalid.
*/
signed int aany_signed_short(signed int opcode, Py_ssize_t arraylen, signed short *data, signed short param1, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t index; 

#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
		return aany_signed_short_simd(opcode, arraylen, data, param1);
	}
#endif

	switch(opcode) {
	// AF_EQ
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GT
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GTE
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LT
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LTE
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_NE
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
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
   Returns 1 if the condition was true at least once, ARR_ERR_NOTFOUND,
		if it was not found, or an error code if the opcode was invalid.
*/
signed int aany_unsigned_short(signed int opcode, Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
	// AF_EQ
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GT
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GTE
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LT
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LTE
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_NE
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
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
   Returns 1 if the condition was true at least once, ARR_ERR_NOTFOUND,
		if it was not found, or an error code if the opcode was invalid.
*/
signed int aany_signed_int(signed int opcode, Py_ssize_t arraylen, signed int *data, signed int param1, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t index; 

#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
		return aany_signed_int_simd(opcode, arraylen, data, param1);
	}
#endif

	switch(opcode) {
	// AF_EQ
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GT
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GTE
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LT
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LTE
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_NE
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
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
   Returns 1 if the condition was true at least once, ARR_ERR_NOTFOUND,
		if it was not found, or an error code if the opcode was invalid.
*/
signed int aany_unsigned_int(signed int opcode, Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
	// AF_EQ
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GT
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GTE
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LT
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LTE
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_NE
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
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
   Returns 1 if the condition was true at least once, ARR_ERR_NOTFOUND,
		if it was not found, or an error code if the opcode was invalid.
*/
signed int aany_signed_long(signed int opcode, Py_ssize_t arraylen, signed long *data, signed long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
	// AF_EQ
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GT
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GTE
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LT
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LTE
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_NE
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
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
   Returns 1 if the condition was true at least once, ARR_ERR_NOTFOUND,
		if it was not found, or an error code if the opcode was invalid.
*/
signed int aany_unsigned_long(signed int opcode, Py_ssize_t arraylen, unsigned long *data, unsigned long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
	// AF_EQ
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GT
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GTE
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LT
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LTE
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_NE
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
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
   Returns 1 if the condition was true at least once, ARR_ERR_NOTFOUND,
		if it was not found, or an error code if the opcode was invalid.
*/
signed int aany_signed_long_long(signed int opcode, Py_ssize_t arraylen, signed long long *data, signed long long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
	// AF_EQ
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GT
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GTE
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LT
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LTE
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_NE
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
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
   Returns 1 if the condition was true at least once, ARR_ERR_NOTFOUND,
		if it was not found, or an error code if the opcode was invalid.
*/
signed int aany_unsigned_long_long(signed int opcode, Py_ssize_t arraylen, unsigned long long *data, unsigned long long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
	// AF_EQ
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GT
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GTE
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LT
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LTE
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_NE
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
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
   Returns 1 if the condition was true at least once, ARR_ERR_NOTFOUND,
		if it was not found, or an error code if the opcode was invalid.
*/
signed int aany_float(signed int opcode, Py_ssize_t arraylen, float *data, float param1, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t index; 

#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (FLOATSIMDSIZE * 2))) {
		return aany_float_simd(opcode, arraylen, data, param1);
	}
#endif

	switch(opcode) {
	// AF_EQ
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GT
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GTE
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LT
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LTE
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_NE
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
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
   Returns 1 if the condition was true at least once, ARR_ERR_NOTFOUND,
		if it was not found, or an error code if the opcode was invalid.
*/
signed int aany_double(signed int opcode, Py_ssize_t arraylen, double *data, double param1, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t index; 

#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (DOUBLESIMDSIZE * 2))) {
		return aany_double_simd(opcode, arraylen, data, param1);
	}
#endif

	switch(opcode) {
	// AF_EQ
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GT
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_GTE
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LT
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_LTE
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// AF_NE
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return 1;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */
