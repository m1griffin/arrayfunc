//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   aall.c
// Purpose:  Returns True if all elements in an array meet the selected criteria.
// Language: C
// Date:     08-May-2014
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
// This must be defined before "Python.h" in order for the pointers in the
// argument parsing functions to work properly. 
#define PY_SSIZE_T_CLEAN

#include "Python.h"

#include "arrayfunc.h"
#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */


// Provide a struct for returning data from parsing Python arguments.
struct args_param {
	char array1type;
	char param1type;
	char error;
};


// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist[] = {"op", "data", "param", "maxlen", NULL};



/*--------------------------------------------------------------------------- */

// Auto generated code goes below.


/*--------------------------------------------------------------------------- */
/* opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
signed int aall_signed_char(signed int opcode, Py_ssize_t arraylen, signed char *data, signed char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] == param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] > param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] >= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] < param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] <= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] != param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
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
   param1 = The parameter to be applied to each array element.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
signed int aall_unsigned_char(signed int opcode, Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] == param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] > param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] >= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] < param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] <= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] != param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
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
   param1 = The parameter to be applied to each array element.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
signed int aall_signed_short(signed int opcode, Py_ssize_t arraylen, signed short *data, signed short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] == param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] > param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] >= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] < param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] <= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] != param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
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
   param1 = The parameter to be applied to each array element.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
signed int aall_unsigned_short(signed int opcode, Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] == param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] > param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] >= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] < param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] <= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] != param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
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
   param1 = The parameter to be applied to each array element.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
signed int aall_signed_int(signed int opcode, Py_ssize_t arraylen, signed int *data, signed int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] == param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] > param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] >= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] < param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] <= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] != param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
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
   param1 = The parameter to be applied to each array element.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
signed int aall_unsigned_int(signed int opcode, Py_ssize_t arraylen, unsigned int *data, unsigned int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] == param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] > param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] >= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] < param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] <= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] != param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
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
   param1 = The parameter to be applied to each array element.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
signed int aall_signed_long(signed int opcode, Py_ssize_t arraylen, signed long *data, signed long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] == param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] > param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] >= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] < param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] <= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] != param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
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
   param1 = The parameter to be applied to each array element.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
signed int aall_unsigned_long(signed int opcode, Py_ssize_t arraylen, unsigned long *data, unsigned long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] == param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] > param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] >= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] < param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] <= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] != param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
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
   param1 = The parameter to be applied to each array element.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
signed int aall_signed_long_long(signed int opcode, Py_ssize_t arraylen, signed long long *data, signed long long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] == param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] > param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] >= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] < param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] <= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] != param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
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
   param1 = The parameter to be applied to each array element.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
signed int aall_unsigned_long_long(signed int opcode, Py_ssize_t arraylen, unsigned long long *data, unsigned long long param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] == param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] > param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] >= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] < param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] <= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] != param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
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
   param1 = The parameter to be applied to each array element.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
signed int aall_float(signed int opcode, Py_ssize_t arraylen, float *data, float param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] == param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] > param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] >= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] < param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] <= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] != param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
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
   param1 = The parameter to be applied to each array element.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
signed int aall_double(signed int opcode, Py_ssize_t arraylen, double *data, double param1) { 

	// array index counter. 
	Py_ssize_t index; 

	switch(opcode) {
		// af_eq
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] == param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gt
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] > param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_gte
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] >= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lt
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] < param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_lte
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] <= param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
		}
		// af_ne
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (!(data[index] != param1)) {
					return ARR_ERR_NOTFOUND;
				}
			}
			return 1;
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
	struct arrayparamstypes arrtype = {0, 0, ' '};
	signed int opcode;


	/* Import the raw objects. */
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "iOO|n:aall", kwlist, 
			&opcode, &dataobj, &param1obj, &arraymaxlen)) {
		argtypes.error = 1;
		return argtypes;
	}

	// Test if the second parameter is an array or bytes.
	arrtype = paramarraytype(dataobj);
	if (!arrtype.isarray) {
		argtypes.error = 2;
		return argtypes;
	} else {
		// Get the array code type character.
		argtypes.array1type = arrtype.arraycode;
	}


	// Get the parameter type codes.
	argtypes.param1type = paramtypecode(param1obj->ob_type->tp_name);


	return argtypes;

}


/*--------------------------------------------------------------------------- */


/* The wrapper to the underlying C function */
static PyObject *py_aall(PyObject *self, PyObject *args, PyObject *keywds) {


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
	signed int resultcode;


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
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*l|n:aall", kwlist, 
					&opcode, &datapy, &param1tmp_l, &arraymaxlen)) {
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
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*l|n:aall", kwlist, 
					&opcode, &datapy, &param1tmp_l, &arraymaxlen)) {
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
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*h|n:aall", kwlist, 
					&opcode, &datapy, &param1py.h, &arraymaxlen)) {
				return NULL;
			}
			break;
		}
		// unsigned short
		case 'H' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*l|n:aall", kwlist, 
					&opcode, &datapy, &param1tmp_l, &arraymaxlen)) {
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
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*i|n:aall", kwlist, 
					&opcode, &datapy, &param1py.i, &arraymaxlen)) {
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
				if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*l|n:aall", kwlist, 
						&opcode, &datapy, &param1tmp_l, &arraymaxlen)) {
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
				if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*I|n:aall", kwlist,
						&opcode, &datapy, &param1py.I, &arraymaxlen)) {
					return NULL;
				}
			}
			break;
		}
		// signed long
		case 'l' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*l|n:aall", kwlist, 
					&opcode, &datapy, &param1py.l, &arraymaxlen)) {
				return NULL;
			}
			break;
		}
		// unsigned long
		case 'L' : {
			// The format string and parameter names depend on the expected data types.
			// We don't have a guaranteed data size larger than unsigned long, so
			// we can't manually range check it.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*k|n:aall", kwlist,
					&opcode, &datapy, &param1py.L, &arraymaxlen)) {
				return NULL;
			}
			// We can't check this data range manually.
			break;
		}
		// signed long long
		case 'q' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*L|n:aall", kwlist, 
					&opcode, &datapy, &param1py.q, &arraymaxlen)) {
				return NULL;
			}
			break;
		}
		// unsigned long long
		case 'Q' : {
			// The format string and parameter names depend on the expected data types.
			// We don't have a guaranteed data size larger than unsigned long long, so
			// we can't manually range check it.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*K|n:aall", kwlist,
					&opcode, &datapy, &param1py.Q, &arraymaxlen)) {
				return NULL;
			}
			// We can't check this data range manually.
			break;
		}
		// float
		case 'f' : {
			// The format string and parameter names depend on the expected data types.
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*f|n:aall", kwlist, 
					&opcode, &datapy, &param1py.f, &arraymaxlen)) {
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
			if (!PyArg_ParseTupleAndKeywords(args, keywds, "iy*d|n:aall", kwlist, 
					&opcode, &datapy, &param1py.d, &arraymaxlen)) {
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
			resultcode = aall_signed_char(opcode, arraylength, data.b, param1py.b);
			break;
		}
		// unsigned char
		case 'B' : {
			resultcode = aall_unsigned_char(opcode, arraylength, data.B, param1py.B);
			break;
		}
		// signed short
		case 'h' : {
			resultcode = aall_signed_short(opcode, arraylength, data.h, param1py.h);
			break;
		}
		// unsigned short
		case 'H' : {
			resultcode = aall_unsigned_short(opcode, arraylength, data.H, param1py.H);
			break;
		}
		// signed int
		case 'i' : {
			resultcode = aall_signed_int(opcode, arraylength, data.i, param1py.i);
			break;
		}
		// unsigned int
		case 'I' : {
			resultcode = aall_unsigned_int(opcode, arraylength, data.I, param1py.I);
			break;
		}
		// signed long
		case 'l' : {
			resultcode = aall_signed_long(opcode, arraylength, data.l, param1py.l);
			break;
		}
		// unsigned long
		case 'L' : {
			resultcode = aall_unsigned_long(opcode, arraylength, data.L, param1py.L);
			break;
		}
		// signed long long
		case 'q' : {
			resultcode = aall_signed_long_long(opcode, arraylength, data.q, param1py.q);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultcode = aall_unsigned_long_long(opcode, arraylength, data.Q, param1py.Q);
			break;
		}
		// float
		case 'f' : {
			resultcode = aall_float(opcode, arraylength, data.f, param1py.f);
			break;
		}
		// double
		case 'd' : {
			resultcode = aall_double(opcode, arraylength, data.d, param1py.d);
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


	// Return whether found or not.
	if (resultcode == ARR_ERR_NOTFOUND) {
		Py_RETURN_FALSE;
	} else {
		Py_RETURN_TRUE;
	}



}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(aall__doc__,
"Returns True if all elements in an array meet the selected criteria.\n\
\n\
x = aall(op, inparray, rparam)\n\
x = aall(op, inparray, rparam, maxlen=y)\n\
\n\
* op - The arithmetic comparison operation.\n\
* inparray - The input data array to be examined.\n\
* rparam - The parameter to be applied to 'op'. \n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored. \n\
* x - The boolean result.");


/* A list of all the methods defined by this module. 
 "aall" is the name seen inside of Python. 
 "py_aall" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef aall_methods[] = {
	{"aall",  (PyCFunction) py_aall, METH_VARARGS | METH_KEYWORDS, aall__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef aallmodule = {
    PyModuleDef_HEAD_INIT,
    "aall",
    NULL,
    -1,
    aall_methods
};

PyMODINIT_FUNC PyInit_aall(void)
{
    return PyModule_Create(&aallmodule);
};

/*--------------------------------------------------------------------------- */
