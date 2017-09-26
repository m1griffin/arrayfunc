//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   findindices_common.c
// Purpose:  Searches an array for the array indices which meet the specified 
//           criteria and writes the results to a second array. Also returns the 
//           number of matches found.
//           Common platform independent code.
// Language: C
// Date:     11-May-2014
// Ver:      24-Sep-2017.
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

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// Auto generated code goes below.

/*--------------------------------------------------------------------------- */
/* opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t findindices_signed_char(signed int opcode, Py_ssize_t arraylen, signed char *data, signed long long *dataout, signed char param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t findindices_unsigned_char(signed int opcode, Py_ssize_t arraylen, unsigned char *data, signed long long *dataout, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t findindices_signed_short(signed int opcode, Py_ssize_t arraylen, signed short *data, signed long long *dataout, signed short param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t findindices_unsigned_short(signed int opcode, Py_ssize_t arraylen, unsigned short *data, signed long long *dataout, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t findindices_signed_int(signed int opcode, Py_ssize_t arraylen, signed int *data, signed long long *dataout, signed int param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t findindices_unsigned_int(signed int opcode, Py_ssize_t arraylen, unsigned int *data, signed long long *dataout, unsigned int param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t findindices_signed_long(signed int opcode, Py_ssize_t arraylen, signed long *data, signed long long *dataout, signed long param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t findindices_unsigned_long(signed int opcode, Py_ssize_t arraylen, unsigned long *data, signed long long *dataout, unsigned long param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t findindices_signed_long_long(signed int opcode, Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t findindices_unsigned_long_long(signed int opcode, Py_ssize_t arraylen, unsigned long long *data, signed long long *dataout, unsigned long long param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t findindices_float(signed int opcode, Py_ssize_t arraylen, float *data, signed long long *dataout, float param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   Returns 0 or a positive integer indicating the number of input elements 
         copied to the output array, or an error code.
*/
Py_ssize_t findindices_double(signed int opcode, Py_ssize_t arraylen, double *data, signed long long *dataout, double param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = (signed long long) index;
					outindex++;
				}
			}
			// Did we find any matches?
			if (outindex > 0) {
				return outindex;
			} else {
				return ARR_ERR_NOTFOUND;
			}
		}
	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */
