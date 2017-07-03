//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   findindex.c
// Purpose:  Returns the index of the first value in an array to meet the specified criteria.
// Language: C
// Date:     10-May-2014
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2017    Michael Griffin    <m12.griffin@gmail.com>
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

#include "arrayfunc.h"
#include "arrayerrs.h"
#include "simddefs.h"

#ifdef AF_HASSIMD
#include "findindex_simd_x86.h"
#endif

/*--------------------------------------------------------------------------- */

// Provide a struct for returning data from parsing Python arguments.
struct args_param {
	char array1type;
	char param1type;
	char error;
};

// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist[] = {"op", "data", "param", "maxlen", "nosimd", NULL};

/*--------------------------------------------------------------------------- */

// Auto-generated code goes below.

/*--------------------------------------------------------------------------- */
/* For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the array index of the found item, 
	or a negative integer as an error code.
*/
Py_ssize_t findindex_signed_char(signed int opcode, Py_ssize_t arraylen, signed char *data, signed char param1, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t index; 


#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
		return findindex_signed_char_simd(opcode, arraylen, data, param1);
	}
#endif

	switch(opcode) {
	// af_eq
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gt
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gte
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lt
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lte
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_ne
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
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
   Returns 0 or a positive integer indicating the array index of the found item, 
	or a negative integer as an error code.
*/
Py_ssize_t findindex_unsigned_char(signed int opcode, Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
	// af_eq
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gt
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gte
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lt
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lte
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_ne
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
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
   Returns 0 or a positive integer indicating the array index of the found item, 
	or a negative integer as an error code.
*/
Py_ssize_t findindex_signed_short(signed int opcode, Py_ssize_t arraylen, signed short *data, signed short param1, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t index; 


#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
		return findindex_signed_short_simd(opcode, arraylen, data, param1);
	}
#endif

	switch(opcode) {
	// af_eq
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gt
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gte
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lt
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lte
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_ne
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
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
   Returns 0 or a positive integer indicating the array index of the found item, 
	or a negative integer as an error code.
*/
Py_ssize_t findindex_unsigned_short(signed int opcode, Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
	// af_eq
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gt
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gte
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lt
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lte
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_ne
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
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
   Returns 0 or a positive integer indicating the array index of the found item, 
	or a negative integer as an error code.
*/
Py_ssize_t findindex_signed_int(signed int opcode, Py_ssize_t arraylen, signed int *data, signed int param1, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t index; 


#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
		return findindex_signed_int_simd(opcode, arraylen, data, param1);
	}
#endif

	switch(opcode) {
	// af_eq
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gt
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gte
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lt
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lte
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_ne
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
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
   Returns 0 or a positive integer indicating the array index of the found item, 
	or a negative integer as an error code.
*/
Py_ssize_t findindex_unsigned_int(signed int opcode, Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
	// af_eq
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gt
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gte
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lt
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lte
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_ne
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
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
   Returns 0 or a positive integer indicating the array index of the found item, 
	or a negative integer as an error code.
*/
Py_ssize_t findindex_signed_long(signed int opcode, Py_ssize_t arraylen, signed long *data, signed long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
	// af_eq
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gt
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gte
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lt
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lte
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_ne
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
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
   Returns 0 or a positive integer indicating the array index of the found item, 
	or a negative integer as an error code.
*/
Py_ssize_t findindex_unsigned_long(signed int opcode, Py_ssize_t arraylen, unsigned long *data, unsigned long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
	// af_eq
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gt
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gte
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lt
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lte
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_ne
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
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
   Returns 0 or a positive integer indicating the array index of the found item, 
	or a negative integer as an error code.
*/
Py_ssize_t findindex_signed_long_long(signed int opcode, Py_ssize_t arraylen, signed long long *data, signed long long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
	// af_eq
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gt
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gte
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lt
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lte
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_ne
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
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
   Returns 0 or a positive integer indicating the array index of the found item, 
	or a negative integer as an error code.
*/
Py_ssize_t findindex_unsigned_long_long(signed int opcode, Py_ssize_t arraylen, unsigned long long *data, unsigned long long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
	// af_eq
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gt
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gte
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lt
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lte
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_ne
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
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
   Returns 0 or a positive integer indicating the array index of the found item, 
	or a negative integer as an error code.
*/
Py_ssize_t findindex_float(signed int opcode, Py_ssize_t arraylen, float *data, float param1, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t index; 


#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (FLOATSIMDSIZE * 2))) {
		return findindex_float_simd(opcode, arraylen, data, param1);
	}
#endif

	switch(opcode) {
	// af_eq
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gt
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gte
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lt
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lte
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_ne
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
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
   Returns 0 or a positive integer indicating the array index of the found item, 
	or a negative integer as an error code.
*/
Py_ssize_t findindex_double(signed int opcode, Py_ssize_t arraylen, double *data, double param1, unsigned int nosimd) { 

	// array index counter. 
	Py_ssize_t index; 


#ifdef AF_HASSIMD
	// SIMD version.
	if (!nosimd && (arraylen >= (DOUBLESIMDSIZE * 2))) {
		return findindex_double_simd(opcode, arraylen, data, param1);
	}
#endif

	switch(opcode) {
	// af_eq
	case OP_AF_EQ: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] == param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gt
	case OP_AF_GT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] > param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_gte
	case OP_AF_GTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] >= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lt
	case OP_AF_LT: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] < param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_lte
	case OP_AF_LTE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] <= param1) {
				return index;
			}
		}
		return ARR_ERR_NOTFOUND;
	}
	// af_ne
	case OP_AF_NE: {
		for(index = 0; index < arraylen; index++) {
			if (data[index] != param1) {
				return index;
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

/* Parse the Python arguments to objects, and then extract the object parameters
 * to determine their types. This lets us handle different data types as 
 * parameters.
 * This version expects the following parameters:
 * args (PyObject) = The positional arguments.
 * Returns a structure containing the results of each parameter.
*/
struct args_param parsepyargs_parm(PyObject *args, PyObject *keywds) {

	PyObject *dataobj, *param1obj;

	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	struct args_param argtypes = {' ', ' ', 0};
	struct arrayparamstypes arr1type = {0, 0, ' '};
	signed int opcode;
	unsigned int nosimd = 0;

	/* Import the raw objects. */
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "iOO|ni:findindex", kwlist, 
			&opcode, &dataobj, &param1obj, &arraymaxlen, &nosimd)) {
		argtypes.error = 1;
		return argtypes;
	}

	// Test if the second parameter is an array or bytes.
	arr1type = paramarraytype(dataobj);
	if (!arr1type.isarray) {
		argtypes.error = 2;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.array1type = arr1type.arraycode;
	}


	// Get the parameter type codes.
	argtypes.param1type = paramtypecode(param1obj->ob_type->tp_name);


	return argtypes;

}


/*--------------------------------------------------------------------------- */


/* The wrapper to the underlying C function */
static PyObject *py_findindex(PyObject *self, PyObject *args, PyObject *keywds)
{


	// The array of data we work on. 
	union dataarrays data;

	// The input buffers are arrays of bytes.
	Py_buffer datapy;

	// The length of the data array.
	Py_ssize_t databufflength;


	// Codes indicating the type of array and the operation desired.
	char itemcode;
	signed int opcode;

	// How long the array is.
	Py_ssize_t arraylength;
	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	// The parameter version is available in all possible types.
	struct paramsvals param1py;

	// PyArg_ParseTuple does not match directly to the array codes. We need to
	// use some temporary variables of alternate types to parse the parameter 
	// data.
	// PyArg_ParseTuple does not check for overflow of unsigned parameters.
	signed long param1tmp_l;

	// This is used to hold the results from inspecting the Python args.
	struct args_param argtypes;

	// The error code returned by the function.
	Py_ssize_t resultcode;

	// If true, disable using SIMD.
	unsigned int nosimd = 0;


	// -------------------------------------------------------------------------


	// Check the parameters to see what they are.
	argtypes = parsepyargs_parm(args, keywds);



	// There was an error reading the parameter types.
	if (argtypes.error) {
		ErrMsgParameterError();
		return NULL;
	}


	// Check if the array and parameter types are compatible.
	if (!paramcompatok(argtypes.array1type, argtypes.param1type)) {
		ErrMsgArrayAndParamMismatch();
		return NULL;
	}

	itemcode = argtypes.array1type;

	// Now we will fetch the actual data depending on the array type.
	switch (itemcode) {
		// signed char
		case 'b' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*l|ni:findindex", kwlist, 
					&opcode, &datapy, &param1tmp_l, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(issignedcharrange(param1tmp_l))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			} else {
				param1py.b = (signed char) param1tmp_l;
			}
			break;
		}
		// unsigned char
		case 'B' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*l|ni:findindex", kwlist, 
					&opcode, &datapy, &param1tmp_l, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isunsignedcharrange(param1tmp_l))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			} else {
				param1py.B = (unsigned char) param1tmp_l;
			}
			break;
		}
		// signed short
		case 'h' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*h|ni:findindex", kwlist, 
					&opcode, &datapy, &param1py.h, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			break;
		}
		// unsigned short
		case 'H' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*l|ni:findindex", kwlist, 
					&opcode, &datapy, &param1tmp_l, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isunsignedshortrange(param1tmp_l))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			} else {
				param1py.H = (unsigned short) param1tmp_l;
			}
			break;
		}
		// signed int
		case 'i' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*i|ni:findindex", kwlist, 
					&opcode, &datapy, &param1py.i, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			break;
		}
		// unsigned int
		case 'I' : {
			// With architectures where signed long is larger than unsigned int, we
			// can use the larger signed value to test for overflow. If they are the
			// same size, then we cannot check for overflow.
			if (sizeof(signed long) > sizeof(unsigned int)) {
				// The format string and parameter names depend on the expected data types.
				if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*l|ni:findindex", kwlist, 
						&opcode, &datapy, &param1tmp_l, &arraymaxlen, &nosimd)) {
					return NULL;
				}
				// Check the data range manually.
				if (!(isunsignedintrange(param1tmp_l))) {
					PyBuffer_Release(&datapy);
					ErrMsgArithOverflowParam();
					return NULL;
				} else {
					param1py.I = (unsigned int) param1tmp_l;
				}
			} else {
				// The format string and parameter names depend on the expected data types.
				if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*I|ni:findindex", kwlist, 
						&opcode, &datapy, &param1py.I, &arraymaxlen, &nosimd)) {
					return NULL;
				}
			}
			break;
		}
		// signed long
		case 'l' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*l|ni:findindex", kwlist, 
					&opcode, &datapy, &param1py.l, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			break;
		}
		// unsigned long
		case 'L' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*k|ni:findindex", kwlist, 
					&opcode, &datapy, &param1py.L, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			break;
		}
		// signed long long
		case 'q' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*L|ni:findindex", kwlist, 
					&opcode, &datapy, &param1py.q, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			break;
		}
		// unsigned long long
		case 'Q' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*K|ni:findindex", kwlist, 
					&opcode, &datapy, &param1py.Q, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			break;
		}
		// float
		case 'f' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*f|ni:findindex", kwlist, 
					&opcode, &datapy, &param1py.f, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isfinite(param1py.f))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			}
			break;
		}
		// double
		case 'd' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*d|ni:findindex", kwlist, 
					&opcode, &datapy, &param1py.d, &arraymaxlen, &nosimd)) {
				return NULL;
			}
			// Check the data range manually.
			if (!(isfinite(param1py.d))) {
				PyBuffer_Release(&datapy);
				ErrMsgArithOverflowParam();
				return NULL;
			}
			break;
		}
		// We don't know this code.
		default: {
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}


	// Assign the buffer to a union which lets us get at them as typed data.
	data.buf = datapy.buf;

	// The length of the data array.
	databufflength = datapy.len;
	arraylength = calcarraylength(itemcode, databufflength);
	if (arraylength < 1) {
		// Release the buffers. 
		PyBuffer_Release(&datapy);
		ErrMsgArrayLengthErr();
		return NULL;
	}


	// Adjust the length of array being operated on, if necessary.
	arraylength = adjustarraymaxlen(arraylength, arraymaxlen);



	/* Call the C function */
	switch(itemcode) {
		// signed char
		case 'b' : {
			resultcode = findindex_signed_char(opcode, arraylength, data.b, param1py.b, nosimd);
			break;
		}
		// unsigned char
		case 'B' : {
			resultcode = findindex_unsigned_char(opcode, arraylength, data.B, param1py.B);
			break;
		}
		// signed short
		case 'h' : {
			resultcode = findindex_signed_short(opcode, arraylength, data.h, param1py.h, nosimd);
			break;
		}
		// unsigned short
		case 'H' : {
			resultcode = findindex_unsigned_short(opcode, arraylength, data.H, param1py.H);
			break;
		}
		// signed int
		case 'i' : {
			resultcode = findindex_signed_int(opcode, arraylength, data.i, param1py.i, nosimd);
			break;
		}
		// unsigned int
		case 'I' : {
			resultcode = findindex_unsigned_int(opcode, arraylength, data.I, param1py.I);
			break;
		}
		// signed long
		case 'l' : {
			resultcode = findindex_signed_long(opcode, arraylength, data.l, param1py.l);
			break;
		}
		// unsigned long
		case 'L' : {
			resultcode = findindex_unsigned_long(opcode, arraylength, data.L, param1py.L);
			break;
		}
		// signed long long
		case 'q' : {
			resultcode = findindex_signed_long_long(opcode, arraylength, data.q, param1py.q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultcode = findindex_unsigned_long_long(opcode, arraylength, data.Q, param1py.Q);
			break;
		}
		// float
		case 'f' : {
			resultcode = findindex_float(opcode, arraylength, data.f, param1py.f, nosimd);
			break;
		}
		// double
		case 'd' : {
			resultcode = findindex_double(opcode, arraylength, data.d, param1py.d, nosimd);
			break;
		}
		// We don't know this code.
		default: {
			PyBuffer_Release(&datapy);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}


	// Release the buffers. 
	PyBuffer_Release(&datapy);

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
"Returns the index of the first value in an array to meet the specified \n\
criteria.\n\
\n\
x = findindex(op, inparray, rparam)\n\
x = findindex(op, inparray, rparam, maxlen=y)\n\
\n\
* op - The arithmetic comparison operation.\n\
* inparray - The input data array to be examined.\n\
* rparam - The parameter to be applied to 'op'. \n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored.\n\
* nosimd - If true, disable SIMD. \n\
* x - The resulting index. This will be negative if no match was found.");


/* A list of all the methods defined by this module. 
 "findindex" is the name seen inside of Python. 
 "py_findindex" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef findindex_methods[] = {
	{"findindex",  (PyCFunction) py_findindex, METH_VARARGS | METH_KEYWORDS, findindex__doc__}, 
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
