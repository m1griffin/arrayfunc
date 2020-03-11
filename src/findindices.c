//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   findindices.c
// Purpose:  Calculate the findindices of values in an array.
// Language: C
// Date:     15-Nov-2017.
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

#include "arrayparams_findindices.h"


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
Py_ssize_t findindices_eq_signed_char(Py_ssize_t arraylen, signed char *data, signed long long *dataout, signed char param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] == param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_gt_signed_char(Py_ssize_t arraylen, signed char *data, signed long long *dataout, signed char param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] > param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ge_signed_char(Py_ssize_t arraylen, signed char *data, signed long long *dataout, signed char param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] >= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_lt_signed_char(Py_ssize_t arraylen, signed char *data, signed long long *dataout, signed char param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] < param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_le_signed_char(Py_ssize_t arraylen, signed char *data, signed long long *dataout, signed char param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] <= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ne_signed_char(Py_ssize_t arraylen, signed char *data, signed long long *dataout, signed char param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] != param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_select_signed_char(signed int opcode, Py_ssize_t arraylen, signed char *data, signed long long *dataout, signed char param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return findindices_eq_signed_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return findindices_gt_signed_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return findindices_ge_signed_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return findindices_lt_signed_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return findindices_le_signed_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return findindices_ne_signed_char(arraylen, data, dataout, param1);
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
Py_ssize_t findindices_eq_unsigned_char(Py_ssize_t arraylen, unsigned char *data, signed long long *dataout, unsigned char param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] == param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_gt_unsigned_char(Py_ssize_t arraylen, unsigned char *data, signed long long *dataout, unsigned char param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] > param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ge_unsigned_char(Py_ssize_t arraylen, unsigned char *data, signed long long *dataout, unsigned char param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] >= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_lt_unsigned_char(Py_ssize_t arraylen, unsigned char *data, signed long long *dataout, unsigned char param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] < param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_le_unsigned_char(Py_ssize_t arraylen, unsigned char *data, signed long long *dataout, unsigned char param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] <= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ne_unsigned_char(Py_ssize_t arraylen, unsigned char *data, signed long long *dataout, unsigned char param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] != param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_select_unsigned_char(signed int opcode, Py_ssize_t arraylen, unsigned char *data, signed long long *dataout, unsigned char param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return findindices_eq_unsigned_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return findindices_gt_unsigned_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return findindices_ge_unsigned_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return findindices_lt_unsigned_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return findindices_le_unsigned_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return findindices_ne_unsigned_char(arraylen, data, dataout, param1);
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
Py_ssize_t findindices_eq_signed_short(Py_ssize_t arraylen, signed short *data, signed long long *dataout, signed short param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] == param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_gt_signed_short(Py_ssize_t arraylen, signed short *data, signed long long *dataout, signed short param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] > param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ge_signed_short(Py_ssize_t arraylen, signed short *data, signed long long *dataout, signed short param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] >= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_lt_signed_short(Py_ssize_t arraylen, signed short *data, signed long long *dataout, signed short param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] < param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_le_signed_short(Py_ssize_t arraylen, signed short *data, signed long long *dataout, signed short param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] <= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ne_signed_short(Py_ssize_t arraylen, signed short *data, signed long long *dataout, signed short param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] != param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_select_signed_short(signed int opcode, Py_ssize_t arraylen, signed short *data, signed long long *dataout, signed short param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return findindices_eq_signed_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return findindices_gt_signed_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return findindices_ge_signed_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return findindices_lt_signed_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return findindices_le_signed_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return findindices_ne_signed_short(arraylen, data, dataout, param1);
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
Py_ssize_t findindices_eq_unsigned_short(Py_ssize_t arraylen, unsigned short *data, signed long long *dataout, unsigned short param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] == param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_gt_unsigned_short(Py_ssize_t arraylen, unsigned short *data, signed long long *dataout, unsigned short param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] > param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ge_unsigned_short(Py_ssize_t arraylen, unsigned short *data, signed long long *dataout, unsigned short param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] >= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_lt_unsigned_short(Py_ssize_t arraylen, unsigned short *data, signed long long *dataout, unsigned short param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] < param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_le_unsigned_short(Py_ssize_t arraylen, unsigned short *data, signed long long *dataout, unsigned short param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] <= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ne_unsigned_short(Py_ssize_t arraylen, unsigned short *data, signed long long *dataout, unsigned short param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] != param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_select_unsigned_short(signed int opcode, Py_ssize_t arraylen, unsigned short *data, signed long long *dataout, unsigned short param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return findindices_eq_unsigned_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return findindices_gt_unsigned_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return findindices_ge_unsigned_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return findindices_lt_unsigned_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return findindices_le_unsigned_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return findindices_ne_unsigned_short(arraylen, data, dataout, param1);
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
Py_ssize_t findindices_eq_signed_int(Py_ssize_t arraylen, signed int *data, signed long long *dataout, signed int param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] == param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_gt_signed_int(Py_ssize_t arraylen, signed int *data, signed long long *dataout, signed int param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] > param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ge_signed_int(Py_ssize_t arraylen, signed int *data, signed long long *dataout, signed int param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] >= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_lt_signed_int(Py_ssize_t arraylen, signed int *data, signed long long *dataout, signed int param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] < param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_le_signed_int(Py_ssize_t arraylen, signed int *data, signed long long *dataout, signed int param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] <= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ne_signed_int(Py_ssize_t arraylen, signed int *data, signed long long *dataout, signed int param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] != param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_select_signed_int(signed int opcode, Py_ssize_t arraylen, signed int *data, signed long long *dataout, signed int param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return findindices_eq_signed_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return findindices_gt_signed_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return findindices_ge_signed_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return findindices_lt_signed_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return findindices_le_signed_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return findindices_ne_signed_int(arraylen, data, dataout, param1);
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
Py_ssize_t findindices_eq_unsigned_int(Py_ssize_t arraylen, unsigned int *data, signed long long *dataout, unsigned int param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] == param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_gt_unsigned_int(Py_ssize_t arraylen, unsigned int *data, signed long long *dataout, unsigned int param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] > param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ge_unsigned_int(Py_ssize_t arraylen, unsigned int *data, signed long long *dataout, unsigned int param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] >= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_lt_unsigned_int(Py_ssize_t arraylen, unsigned int *data, signed long long *dataout, unsigned int param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] < param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_le_unsigned_int(Py_ssize_t arraylen, unsigned int *data, signed long long *dataout, unsigned int param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] <= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ne_unsigned_int(Py_ssize_t arraylen, unsigned int *data, signed long long *dataout, unsigned int param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] != param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_select_unsigned_int(signed int opcode, Py_ssize_t arraylen, unsigned int *data, signed long long *dataout, unsigned int param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return findindices_eq_unsigned_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return findindices_gt_unsigned_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return findindices_ge_unsigned_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return findindices_lt_unsigned_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return findindices_le_unsigned_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return findindices_ne_unsigned_int(arraylen, data, dataout, param1);
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
Py_ssize_t findindices_eq_signed_long(Py_ssize_t arraylen, signed long *data, signed long long *dataout, signed long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] == param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_gt_signed_long(Py_ssize_t arraylen, signed long *data, signed long long *dataout, signed long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] > param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ge_signed_long(Py_ssize_t arraylen, signed long *data, signed long long *dataout, signed long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] >= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_lt_signed_long(Py_ssize_t arraylen, signed long *data, signed long long *dataout, signed long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] < param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_le_signed_long(Py_ssize_t arraylen, signed long *data, signed long long *dataout, signed long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] <= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ne_signed_long(Py_ssize_t arraylen, signed long *data, signed long long *dataout, signed long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] != param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_select_signed_long(signed int opcode, Py_ssize_t arraylen, signed long *data, signed long long *dataout, signed long param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return findindices_eq_signed_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return findindices_gt_signed_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return findindices_ge_signed_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return findindices_lt_signed_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return findindices_le_signed_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return findindices_ne_signed_long(arraylen, data, dataout, param1);
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
Py_ssize_t findindices_eq_unsigned_long(Py_ssize_t arraylen, unsigned long *data, signed long long *dataout, unsigned long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] == param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_gt_unsigned_long(Py_ssize_t arraylen, unsigned long *data, signed long long *dataout, unsigned long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] > param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ge_unsigned_long(Py_ssize_t arraylen, unsigned long *data, signed long long *dataout, unsigned long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] >= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_lt_unsigned_long(Py_ssize_t arraylen, unsigned long *data, signed long long *dataout, unsigned long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] < param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_le_unsigned_long(Py_ssize_t arraylen, unsigned long *data, signed long long *dataout, unsigned long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] <= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ne_unsigned_long(Py_ssize_t arraylen, unsigned long *data, signed long long *dataout, unsigned long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] != param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_select_unsigned_long(signed int opcode, Py_ssize_t arraylen, unsigned long *data, signed long long *dataout, unsigned long param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return findindices_eq_unsigned_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return findindices_gt_unsigned_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return findindices_ge_unsigned_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return findindices_lt_unsigned_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return findindices_le_unsigned_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return findindices_ne_unsigned_long(arraylen, data, dataout, param1);
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
Py_ssize_t findindices_eq_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] == param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_gt_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] > param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ge_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] >= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_lt_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] < param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_le_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] <= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ne_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] != param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_select_signed_long_long(signed int opcode, Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return findindices_eq_signed_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return findindices_gt_signed_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return findindices_ge_signed_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return findindices_lt_signed_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return findindices_le_signed_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return findindices_ne_signed_long_long(arraylen, data, dataout, param1);
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
Py_ssize_t findindices_eq_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, signed long long *dataout, unsigned long long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] == param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_gt_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, signed long long *dataout, unsigned long long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] > param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ge_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, signed long long *dataout, unsigned long long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] >= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_lt_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, signed long long *dataout, unsigned long long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] < param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_le_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, signed long long *dataout, unsigned long long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] <= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ne_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, signed long long *dataout, unsigned long long param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] != param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_select_unsigned_long_long(signed int opcode, Py_ssize_t arraylen, unsigned long long *data, signed long long *dataout, unsigned long long param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return findindices_eq_unsigned_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return findindices_gt_unsigned_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return findindices_ge_unsigned_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return findindices_lt_unsigned_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return findindices_le_unsigned_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return findindices_ne_unsigned_long_long(arraylen, data, dataout, param1);
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
Py_ssize_t findindices_eq_float(Py_ssize_t arraylen, float *data, signed long long *dataout, float param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] == param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_gt_float(Py_ssize_t arraylen, float *data, signed long long *dataout, float param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] > param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ge_float(Py_ssize_t arraylen, float *data, signed long long *dataout, float param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] >= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_lt_float(Py_ssize_t arraylen, float *data, signed long long *dataout, float param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] < param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_le_float(Py_ssize_t arraylen, float *data, signed long long *dataout, float param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] <= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ne_float(Py_ssize_t arraylen, float *data, signed long long *dataout, float param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] != param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_select_float(signed int opcode, Py_ssize_t arraylen, float *data, signed long long *dataout, float param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return findindices_eq_float(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return findindices_gt_float(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return findindices_ge_float(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return findindices_lt_float(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return findindices_le_float(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return findindices_ne_float(arraylen, data, dataout, param1);
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
Py_ssize_t findindices_eq_double(Py_ssize_t arraylen, double *data, signed long long *dataout, double param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] == param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_gt_double(Py_ssize_t arraylen, double *data, signed long long *dataout, double param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] > param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ge_double(Py_ssize_t arraylen, double *data, signed long long *dataout, double param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] >= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_lt_double(Py_ssize_t arraylen, double *data, signed long long *dataout, double param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] < param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_le_double(Py_ssize_t arraylen, double *data, signed long long *dataout, double param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] <= param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_ne_double(Py_ssize_t arraylen, double *data, signed long long *dataout, double param1) { 
	// array index counter.
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;


	for(index = 0; index < arraylen; index++) {
		if (data[index] != param1) {
			dataout[outindex] = (signed long long) index;
			outindex++;
		}
	}

	return outindex;

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
Py_ssize_t findindices_select_double(signed int opcode, Py_ssize_t arraylen, double *data, signed long long *dataout, double param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return findindices_eq_double(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return findindices_gt_double(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return findindices_ge_double(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return findindices_lt_double(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return findindices_le_double(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return findindices_ne_double(arraylen, data, dataout, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_findindices(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	Py_ssize_t resultcode = 0;

	// This is used to hold the parsed parameters.
	struct args_params_findindices arraydata = ARGSINIT_FINDINDICES;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_findindices(self, args, keywds, "findindices");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}


	// The length of the data array.
	if (arraydata.arraylength < 1) {
		// Release the buffers. 
		releasebuffers_findindices(arraydata);
		ErrMsgArrayLengthErr();
		return NULL;
	}



	/* Call the C function */
	switch(arraydata.arraytype) {
		// signed char
		case 'b' : {
			resultcode = findindices_select_signed_char(arraydata.opcode, arraydata.arraylength, arraydata.array1.b, arraydata.array2.q, arraydata.param.b);
			break;
		}
		// unsigned char
		case 'B' : {
			resultcode = findindices_select_unsigned_char(arraydata.opcode, arraydata.arraylength, arraydata.array1.B, arraydata.array2.q, arraydata.param.B);
			break;
		}
		// signed short
		case 'h' : {
			resultcode = findindices_select_signed_short(arraydata.opcode, arraydata.arraylength, arraydata.array1.h, arraydata.array2.q, arraydata.param.h);
			break;
		}
		// unsigned short
		case 'H' : {
			resultcode = findindices_select_unsigned_short(arraydata.opcode, arraydata.arraylength, arraydata.array1.H, arraydata.array2.q, arraydata.param.H);
			break;
		}
		// signed int
		case 'i' : {
			resultcode = findindices_select_signed_int(arraydata.opcode, arraydata.arraylength, arraydata.array1.i, arraydata.array2.q, arraydata.param.i);
			break;
		}
		// unsigned int
		case 'I' : {
			resultcode = findindices_select_unsigned_int(arraydata.opcode, arraydata.arraylength, arraydata.array1.I, arraydata.array2.q, arraydata.param.I);
			break;
		}
		// signed long
		case 'l' : {
			resultcode = findindices_select_signed_long(arraydata.opcode, arraydata.arraylength, arraydata.array1.l, arraydata.array2.q, arraydata.param.l);
			break;
		}
		// unsigned long
		case 'L' : {
			resultcode = findindices_select_unsigned_long(arraydata.opcode, arraydata.arraylength, arraydata.array1.L, arraydata.array2.q, arraydata.param.L);
			break;
		}
		// signed long long
		case 'q' : {
			resultcode = findindices_select_signed_long_long(arraydata.opcode, arraydata.arraylength, arraydata.array1.q, arraydata.array2.q, arraydata.param.q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultcode = findindices_select_unsigned_long_long(arraydata.opcode, arraydata.arraylength, arraydata.array1.Q, arraydata.array2.q, arraydata.param.Q);
			break;
		}
		// float
		case 'f' : {
			resultcode = findindices_select_float(arraydata.opcode, arraydata.arraylength, arraydata.array1.f, arraydata.array2.q, arraydata.param.f);
			break;
		}
		// double
		case 'd' : {
			resultcode = findindices_select_double(arraydata.opcode, arraydata.arraylength, arraydata.array1.d, arraydata.array2.q, arraydata.param.d);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_findindices(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_findindices(arraydata);


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
PyDoc_STRVAR(findindices__doc__,
"findindices \n\
_____________________________ \n\
\n\
Searches an array for the array indices which meet the specified \n\
criteria and writes the results to a second array. Also returns the \n\
number of matches found. \n\
\n\
======================  ============================================== \n\
Equivalent to:          [x for x,y in enumerate(inparray) if y == param] \n\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
  result = findindices(opstr, array, arrayout, param) \n\
  result = findindices(opstr, array, arrayout, param, maxlen=y) \n\
\n\
* opstr - The arithmetic comparison operation as a string. \n\
          These are: '==', '>', '>=', '<', '<=', '!='. \n\
* array - The input data array to be examined. \n\
* arrayout - The output array. This must be an integer array of array \n\
  type 'q' (signed long long). \n\
* param - A non-array numeric parameter. \n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored. \n\
* result - An integer indicating the number of matches found. \n\
");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "findindices" is the name seen inside of Python. 
 "py_findindices" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef findindices_methods[] = {
	{"findindices",  (PyCFunction)py_findindices, METH_VARARGS | METH_KEYWORDS, findindices__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef findindicesmodule = {
    PyModuleDef_HEAD_INIT,
    "findindices",
    NULL,
    -1,
    findindices_methods
};

PyMODINIT_FUNC PyInit_findindices(void)
{
    return PyModule_Create(&findindicesmodule);
};

/*--------------------------------------------------------------------------- */

