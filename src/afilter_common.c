//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   afilter_common.c
// Purpose:  Filter based on a test condition.
//           Common platform independent code.
// Language: C
// Date:     09-May-2014
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
Py_ssize_t afilter_signed_char(signed int opcode, Py_ssize_t arraylen, signed char *data, signed char *dataout, signed char param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GT
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GTE
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LT
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LTE
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_NE
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
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
Py_ssize_t afilter_unsigned_char(signed int opcode, Py_ssize_t arraylen, unsigned char *data, unsigned char *dataout, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GT
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GTE
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LT
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LTE
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_NE
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
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
Py_ssize_t afilter_signed_short(signed int opcode, Py_ssize_t arraylen, signed short *data, signed short *dataout, signed short param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GT
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GTE
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LT
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LTE
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_NE
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
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
Py_ssize_t afilter_unsigned_short(signed int opcode, Py_ssize_t arraylen, unsigned short *data, unsigned short *dataout, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GT
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GTE
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LT
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LTE
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_NE
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
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
Py_ssize_t afilter_signed_int(signed int opcode, Py_ssize_t arraylen, signed int *data, signed int *dataout, signed int param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GT
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GTE
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LT
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LTE
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_NE
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
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
Py_ssize_t afilter_unsigned_int(signed int opcode, Py_ssize_t arraylen, unsigned int *data, unsigned int *dataout, unsigned int param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GT
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GTE
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LT
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LTE
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_NE
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
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
Py_ssize_t afilter_signed_long(signed int opcode, Py_ssize_t arraylen, signed long *data, signed long *dataout, signed long param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GT
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GTE
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LT
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LTE
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_NE
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
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
Py_ssize_t afilter_unsigned_long(signed int opcode, Py_ssize_t arraylen, unsigned long *data, unsigned long *dataout, unsigned long param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GT
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GTE
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LT
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LTE
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_NE
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
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
Py_ssize_t afilter_signed_long_long(signed int opcode, Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GT
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GTE
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LT
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LTE
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_NE
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
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
Py_ssize_t afilter_unsigned_long_long(signed int opcode, Py_ssize_t arraylen, unsigned long long *data, unsigned long long *dataout, unsigned long long param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GT
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GTE
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LT
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LTE
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_NE
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
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
Py_ssize_t afilter_float(signed int opcode, Py_ssize_t arraylen, float *data, float *dataout, float param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GT
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GTE
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LT
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LTE
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_NE
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
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
Py_ssize_t afilter_double(signed int opcode, Py_ssize_t arraylen, double *data, double *dataout, double param1) { 

	// array index counter. 
	Py_ssize_t index, outindex; 

	// We need a separate index for the output array, because the input and
	// output indexes may not be the same.
	outindex = 0;

	switch(opcode) {
		// AF_EQ
		case OP_AF_EQ: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] == param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GT
		case OP_AF_GT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] > param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_GTE
		case OP_AF_GTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] >= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LT
		case OP_AF_LT: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] < param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_LTE
		case OP_AF_LTE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] <= param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
		// AF_NE
		case OP_AF_NE: {
			for(index = 0; index < arraylen; index++) {
				if (data[index] != param1) {
					dataout[outindex] = data[index];
					outindex++;
				}
			}
			return outindex;
		}
	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */
