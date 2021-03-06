//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   takewhile.c
// Purpose:  Select values from an array starting from the beginning and stopping
//           when the criteria fails.
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

#include "arrayerrs.h"
#include "arrayparams_base.h"
#include "arrayops.h"

#include "arrayparams_droptakefilter.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: b
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_eq_signed_char(Py_ssize_t arraylen, signed char *data, signed char *dataout, signed char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: b
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_gt_signed_char(Py_ssize_t arraylen, signed char *data, signed char *dataout, signed char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: b
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ge_signed_char(Py_ssize_t arraylen, signed char *data, signed char *dataout, signed char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: b
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_lt_signed_char(Py_ssize_t arraylen, signed char *data, signed char *dataout, signed char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: b
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_le_signed_char(Py_ssize_t arraylen, signed char *data, signed char *dataout, signed char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: b
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ne_signed_char(Py_ssize_t arraylen, signed char *data, signed char *dataout, signed char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_select_signed_char(signed int opcode, Py_ssize_t arraylen, signed char *data, signed char *dataout, signed char param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return takewhile_eq_signed_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return takewhile_gt_signed_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return takewhile_ge_signed_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return takewhile_lt_signed_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return takewhile_le_signed_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return takewhile_ne_signed_char(arraylen, data, dataout, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: B
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_eq_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char *dataout, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: B
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_gt_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char *dataout, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: B
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ge_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char *dataout, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: B
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_lt_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char *dataout, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: B
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_le_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char *dataout, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: B
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ne_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char *dataout, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_select_unsigned_char(signed int opcode, Py_ssize_t arraylen, unsigned char *data, unsigned char *dataout, unsigned char param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return takewhile_eq_unsigned_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return takewhile_gt_unsigned_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return takewhile_ge_unsigned_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return takewhile_lt_unsigned_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return takewhile_le_unsigned_char(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return takewhile_ne_unsigned_char(arraylen, data, dataout, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: h
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_eq_signed_short(Py_ssize_t arraylen, signed short *data, signed short *dataout, signed short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: h
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_gt_signed_short(Py_ssize_t arraylen, signed short *data, signed short *dataout, signed short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: h
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ge_signed_short(Py_ssize_t arraylen, signed short *data, signed short *dataout, signed short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: h
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_lt_signed_short(Py_ssize_t arraylen, signed short *data, signed short *dataout, signed short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: h
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_le_signed_short(Py_ssize_t arraylen, signed short *data, signed short *dataout, signed short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: h
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ne_signed_short(Py_ssize_t arraylen, signed short *data, signed short *dataout, signed short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_select_signed_short(signed int opcode, Py_ssize_t arraylen, signed short *data, signed short *dataout, signed short param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return takewhile_eq_signed_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return takewhile_gt_signed_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return takewhile_ge_signed_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return takewhile_lt_signed_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return takewhile_le_signed_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return takewhile_ne_signed_short(arraylen, data, dataout, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: H
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_eq_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short *dataout, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: H
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_gt_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short *dataout, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: H
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ge_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short *dataout, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: H
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_lt_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short *dataout, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: H
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_le_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short *dataout, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: H
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ne_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short *dataout, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_select_unsigned_short(signed int opcode, Py_ssize_t arraylen, unsigned short *data, unsigned short *dataout, unsigned short param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return takewhile_eq_unsigned_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return takewhile_gt_unsigned_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return takewhile_ge_unsigned_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return takewhile_lt_unsigned_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return takewhile_le_unsigned_short(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return takewhile_ne_unsigned_short(arraylen, data, dataout, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: i
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_eq_signed_int(Py_ssize_t arraylen, signed int *data, signed int *dataout, signed int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: i
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_gt_signed_int(Py_ssize_t arraylen, signed int *data, signed int *dataout, signed int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: i
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ge_signed_int(Py_ssize_t arraylen, signed int *data, signed int *dataout, signed int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: i
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_lt_signed_int(Py_ssize_t arraylen, signed int *data, signed int *dataout, signed int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: i
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_le_signed_int(Py_ssize_t arraylen, signed int *data, signed int *dataout, signed int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: i
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ne_signed_int(Py_ssize_t arraylen, signed int *data, signed int *dataout, signed int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_select_signed_int(signed int opcode, Py_ssize_t arraylen, signed int *data, signed int *dataout, signed int param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return takewhile_eq_signed_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return takewhile_gt_signed_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return takewhile_ge_signed_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return takewhile_lt_signed_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return takewhile_le_signed_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return takewhile_ne_signed_int(arraylen, data, dataout, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: I
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_eq_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int *dataout, unsigned int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: I
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_gt_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int *dataout, unsigned int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: I
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ge_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int *dataout, unsigned int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: I
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_lt_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int *dataout, unsigned int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: I
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_le_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int *dataout, unsigned int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: I
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ne_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int *dataout, unsigned int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: I
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_select_unsigned_int(signed int opcode, Py_ssize_t arraylen, unsigned int *data, unsigned int *dataout, unsigned int param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return takewhile_eq_unsigned_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return takewhile_gt_unsigned_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return takewhile_ge_unsigned_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return takewhile_lt_unsigned_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return takewhile_le_unsigned_int(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return takewhile_ne_unsigned_int(arraylen, data, dataout, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: l
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_eq_signed_long(Py_ssize_t arraylen, signed long *data, signed long *dataout, signed long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: l
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_gt_signed_long(Py_ssize_t arraylen, signed long *data, signed long *dataout, signed long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: l
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ge_signed_long(Py_ssize_t arraylen, signed long *data, signed long *dataout, signed long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: l
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_lt_signed_long(Py_ssize_t arraylen, signed long *data, signed long *dataout, signed long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: l
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_le_signed_long(Py_ssize_t arraylen, signed long *data, signed long *dataout, signed long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: l
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ne_signed_long(Py_ssize_t arraylen, signed long *data, signed long *dataout, signed long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: l
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_select_signed_long(signed int opcode, Py_ssize_t arraylen, signed long *data, signed long *dataout, signed long param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return takewhile_eq_signed_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return takewhile_gt_signed_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return takewhile_ge_signed_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return takewhile_lt_signed_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return takewhile_le_signed_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return takewhile_ne_signed_long(arraylen, data, dataout, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: L
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_eq_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long *dataout, unsigned long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: L
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_gt_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long *dataout, unsigned long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: L
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ge_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long *dataout, unsigned long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: L
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_lt_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long *dataout, unsigned long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: L
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_le_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long *dataout, unsigned long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: L
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ne_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long *dataout, unsigned long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: L
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_select_unsigned_long(signed int opcode, Py_ssize_t arraylen, unsigned long *data, unsigned long *dataout, unsigned long param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return takewhile_eq_unsigned_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return takewhile_gt_unsigned_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return takewhile_ge_unsigned_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return takewhile_lt_unsigned_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return takewhile_le_unsigned_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return takewhile_ne_unsigned_long(arraylen, data, dataout, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: q
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_eq_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: q
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_gt_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: q
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ge_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: q
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_lt_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: q
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_le_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: q
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ne_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: q
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_select_signed_long_long(signed int opcode, Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return takewhile_eq_signed_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return takewhile_gt_signed_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return takewhile_ge_signed_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return takewhile_lt_signed_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return takewhile_le_signed_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return takewhile_ne_signed_long_long(arraylen, data, dataout, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: Q
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_eq_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long *dataout, unsigned long long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: Q
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_gt_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long *dataout, unsigned long long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: Q
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ge_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long *dataout, unsigned long long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: Q
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_lt_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long *dataout, unsigned long long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: Q
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_le_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long *dataout, unsigned long long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: Q
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ne_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long *dataout, unsigned long long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: Q
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_select_unsigned_long_long(signed int opcode, Py_ssize_t arraylen, unsigned long long *data, unsigned long long *dataout, unsigned long long param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return takewhile_eq_unsigned_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return takewhile_gt_unsigned_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return takewhile_ge_unsigned_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return takewhile_lt_unsigned_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return takewhile_le_unsigned_long_long(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return takewhile_ne_unsigned_long_long(arraylen, data, dataout, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: f
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_eq_float(Py_ssize_t arraylen, float *data, float *dataout, float param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: f
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_gt_float(Py_ssize_t arraylen, float *data, float *dataout, float param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: f
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ge_float(Py_ssize_t arraylen, float *data, float *dataout, float param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: f
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_lt_float(Py_ssize_t arraylen, float *data, float *dataout, float param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: f
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_le_float(Py_ssize_t arraylen, float *data, float *dataout, float param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: f
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ne_float(Py_ssize_t arraylen, float *data, float *dataout, float param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_select_float(signed int opcode, Py_ssize_t arraylen, float *data, float *dataout, float param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return takewhile_eq_float(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return takewhile_gt_float(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return takewhile_ge_float(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return takewhile_lt_float(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return takewhile_le_float(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return takewhile_ne_float(arraylen, data, dataout, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: d
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_eq_double(Py_ssize_t arraylen, double *data, double *dataout, double param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] == param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: d
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_gt_double(Py_ssize_t arraylen, double *data, double *dataout, double param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] > param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: d
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ge_double(Py_ssize_t arraylen, double *data, double *dataout, double param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] >= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: d
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_lt_double(Py_ssize_t arraylen, double *data, double *dataout, double param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] < param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: d
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_le_double(Py_ssize_t arraylen, double *data, double *dataout, double param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] <= param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: d
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_ne_double(Py_ssize_t arraylen, double *data, double *dataout, double param1) { 

	// array index counter. 
	Py_ssize_t index; 

	for(index = 0; index < arraylen; index++) {
		if (!(data[index] != param1)) {
			return index;
		}
		dataout[index] = data[index];
	}
	return index;

}

/*--------------------------------------------------------------------------- */
/* For array code: d
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t takewhile_select_double(signed int opcode, Py_ssize_t arraylen, double *data, double *dataout, double param1) { 

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			return takewhile_eq_double(arraylen, data, dataout, param1);
			break;
		}
		// AF_GT
		case OP_AF_GT: {
			return takewhile_gt_double(arraylen, data, dataout, param1);
			break;
		}
		// AF_GE
		case OP_AF_GE: {
			return takewhile_ge_double(arraylen, data, dataout, param1);
			break;
		}
		// AF_LT
		case OP_AF_LT: {
			return takewhile_lt_double(arraylen, data, dataout, param1);
			break;
		}
		// AF_LE
		case OP_AF_LE: {
			return takewhile_le_double(arraylen, data, dataout, param1);
			break;
		}
		// AF_NE
		case OP_AF_NE: {
			return takewhile_ne_double(arraylen, data, dataout, param1);
			break;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_takewhile(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	Py_ssize_t resultcode = 0;

	// This is used to hold the parsed parameters.
	struct args_params_droptakefilter arraydata = ARGSINIT_DROPTAKEFILTER;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_droptakefilter(self, args, keywds, "takewhile");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}


	// The length of the data array.
	if (arraydata.arraylength < 1) {
		// Release the buffers. 
		releasebuffers_droptakefilter(arraydata);
		ErrMsgArrayLengthErr();
		return NULL;
	}



	/* Call the C function */
	switch(arraydata.arraytype) {
		// signed char
		case 'b' : {
			resultcode = takewhile_select_signed_char(arraydata.opcode, arraydata.arraylength, arraydata.array1.b, arraydata.array2.b, arraydata.param.b);
			break;
		}
		// unsigned char
		case 'B' : {
			resultcode = takewhile_select_unsigned_char(arraydata.opcode, arraydata.arraylength, arraydata.array1.B, arraydata.array2.B, arraydata.param.B);
			break;
		}
		// signed short
		case 'h' : {
			resultcode = takewhile_select_signed_short(arraydata.opcode, arraydata.arraylength, arraydata.array1.h, arraydata.array2.h, arraydata.param.h);
			break;
		}
		// unsigned short
		case 'H' : {
			resultcode = takewhile_select_unsigned_short(arraydata.opcode, arraydata.arraylength, arraydata.array1.H, arraydata.array2.H, arraydata.param.H);
			break;
		}
		// signed int
		case 'i' : {
			resultcode = takewhile_select_signed_int(arraydata.opcode, arraydata.arraylength, arraydata.array1.i, arraydata.array2.i, arraydata.param.i);
			break;
		}
		// unsigned int
		case 'I' : {
			resultcode = takewhile_select_unsigned_int(arraydata.opcode, arraydata.arraylength, arraydata.array1.I, arraydata.array2.I, arraydata.param.I);
			break;
		}
		// signed long
		case 'l' : {
			resultcode = takewhile_select_signed_long(arraydata.opcode, arraydata.arraylength, arraydata.array1.l, arraydata.array2.l, arraydata.param.l);
			break;
		}
		// unsigned long
		case 'L' : {
			resultcode = takewhile_select_unsigned_long(arraydata.opcode, arraydata.arraylength, arraydata.array1.L, arraydata.array2.L, arraydata.param.L);
			break;
		}
		// signed long long
		case 'q' : {
			resultcode = takewhile_select_signed_long_long(arraydata.opcode, arraydata.arraylength, arraydata.array1.q, arraydata.array2.q, arraydata.param.q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultcode = takewhile_select_unsigned_long_long(arraydata.opcode, arraydata.arraylength, arraydata.array1.Q, arraydata.array2.Q, arraydata.param.Q);
			break;
		}
		// float
		case 'f' : {
			resultcode = takewhile_select_float(arraydata.opcode, arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.param.f);
			break;
		}
		// double
		case 'd' : {
			resultcode = takewhile_select_double(arraydata.opcode, arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.param.d);
			break;
		}
		// We don't know this code.
		default: {
			releasebuffers_droptakefilter(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_droptakefilter(arraydata);


	// Return the number of items filtered through.
	return PyLong_FromSsize_t(resultcode);


}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(takewhile__doc__,
"takewhile \n\
_____________________________ \n\
\n\
Select values from an array starting from the beginning and stopping \n\
when the criteria fails. \n\
\n\
======================  ============================================== \n\
Equivalent to:          itertools.takewhile(lambda x: x < param, array) \n\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
  result = takewhile(opstr, array, outparray, param) \n\
  result = takewhile(opstr, array, outparray, param, maxlen=y) \n\
\n\
* opstr - The arithmetic comparison operation as a string. \n\
          These are: '==', '>', '>=', '<', '<=', '!='. \n\
* array - The input data array to be examined. \n\
* outparray - The output array. \n\
* param - A non-array numeric parameter. \n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored. \n\
* result - An integer count of the number of items filtered into outparray. \n\
");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "takewhile" is the name seen inside of Python. 
 "py_takewhile" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef takewhile_methods[] = {
	{"takewhile",  (PyCFunction)py_takewhile, METH_VARARGS | METH_KEYWORDS, takewhile__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef takewhilemodule = {
    PyModuleDef_HEAD_INIT,
    "takewhile",
    NULL,
    -1,
    takewhile_methods
};

PyMODINIT_FUNC PyInit_takewhile(void)
{
    return PyModule_Create(&takewhilemodule);
};

/*--------------------------------------------------------------------------- */

