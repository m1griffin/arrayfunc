//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   findindex_simd_armv7.c
// Purpose:  Calculate the findindex of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     07-Oct-2019
// Ver:      27-Mar-2020.
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

#include "simddefs.h"
#ifdef AF_HASSIMD_ARMv7_32BIT
#include "arm_neon.h"
#endif

#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// Auto generated code goes below.

/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_eq_signed_char_simd(Py_ssize_t arraylen, signed char *data, signed char param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int8x8_t datasliceleft, datasliceright;
	uint8x8_t resultslice;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_s8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1_s8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceq_s8(datasliceleft, datasliceright);
		if (vreinterpret_u64_u8(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] == param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] == param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_gt_signed_char_simd(Py_ssize_t arraylen, signed char *data, signed char param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int8x8_t datasliceleft, datasliceright;
	uint8x8_t resultslice;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_s8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1_s8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcgt_s8(datasliceleft, datasliceright);
		if (vreinterpret_u64_u8(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] > param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] > param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_ge_signed_char_simd(Py_ssize_t arraylen, signed char *data, signed char param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int8x8_t datasliceleft, datasliceright;
	uint8x8_t resultslice;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_s8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1_s8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcge_s8(datasliceleft, datasliceright);
		if (vreinterpret_u64_u8(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] >= param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] >= param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_lt_signed_char_simd(Py_ssize_t arraylen, signed char *data, signed char param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int8x8_t datasliceleft, datasliceright;
	uint8x8_t resultslice;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_s8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1_s8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vclt_s8(datasliceleft, datasliceright);
		if (vreinterpret_u64_u8(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] < param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] < param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_le_signed_char_simd(Py_ssize_t arraylen, signed char *data, signed char param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int8x8_t datasliceleft, datasliceright;
	uint8x8_t resultslice;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_s8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1_s8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcle_s8(datasliceleft, datasliceright);
		if (vreinterpret_u64_u8(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] <= param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] <= param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: b
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_ne_signed_char_simd(Py_ssize_t arraylen, signed char *data, signed char param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int8x8_t datasliceleft, datasliceright;
	uint8x8_t resultslice;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_s8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1_s8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceq_s8(datasliceleft, datasliceright);
		if (vreinterpret_u64_u8(resultslice) != 0xffffffffffffffff) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] != param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] != param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_eq_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint8x8_t datasliceleft, datasliceright;
	uint8x8_t resultslice;
	unsigned char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_u8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1_u8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceq_u8(datasliceleft, datasliceright);
		if (vreinterpret_u64_u8(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] == param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] == param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_gt_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint8x8_t datasliceleft, datasliceright;
	uint8x8_t resultslice;
	unsigned char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_u8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1_u8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcgt_u8(datasliceleft, datasliceright);
		if (vreinterpret_u64_u8(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] > param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] > param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_ge_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint8x8_t datasliceleft, datasliceright;
	uint8x8_t resultslice;
	unsigned char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_u8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1_u8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcge_u8(datasliceleft, datasliceright);
		if (vreinterpret_u64_u8(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] >= param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] >= param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_lt_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint8x8_t datasliceleft, datasliceright;
	uint8x8_t resultslice;
	unsigned char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_u8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1_u8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vclt_u8(datasliceleft, datasliceright);
		if (vreinterpret_u64_u8(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] < param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] < param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_le_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint8x8_t datasliceleft, datasliceright;
	uint8x8_t resultslice;
	unsigned char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_u8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1_u8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcle_u8(datasliceleft, datasliceright);
		if (vreinterpret_u64_u8(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] <= param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] <= param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: B
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_ne_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint8x8_t datasliceleft, datasliceright;
	uint8x8_t resultslice;
	unsigned char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_u8( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += CHARSIMDSIZE) {
		datasliceleft = vld1_u8( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceq_u8(datasliceleft, datasliceright);
		if (vreinterpret_u64_u8(resultslice) != 0xffffffffffffffff) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] != param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] != param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_eq_signed_short_simd(Py_ssize_t arraylen, signed short *data, signed short param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int16x4_t datasliceleft, datasliceright;
	uint16x4_t resultslice;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_s16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1_s16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceq_s16(datasliceleft, datasliceright);
		if (vreinterpret_u64_u16(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] == param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] == param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_gt_signed_short_simd(Py_ssize_t arraylen, signed short *data, signed short param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int16x4_t datasliceleft, datasliceright;
	uint16x4_t resultslice;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_s16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1_s16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcgt_s16(datasliceleft, datasliceright);
		if (vreinterpret_u64_u16(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] > param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] > param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_ge_signed_short_simd(Py_ssize_t arraylen, signed short *data, signed short param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int16x4_t datasliceleft, datasliceright;
	uint16x4_t resultslice;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_s16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1_s16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcge_s16(datasliceleft, datasliceright);
		if (vreinterpret_u64_u16(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] >= param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] >= param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_lt_signed_short_simd(Py_ssize_t arraylen, signed short *data, signed short param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int16x4_t datasliceleft, datasliceright;
	uint16x4_t resultslice;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_s16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1_s16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vclt_s16(datasliceleft, datasliceright);
		if (vreinterpret_u64_u16(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] < param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] < param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_le_signed_short_simd(Py_ssize_t arraylen, signed short *data, signed short param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int16x4_t datasliceleft, datasliceright;
	uint16x4_t resultslice;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_s16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1_s16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcle_s16(datasliceleft, datasliceright);
		if (vreinterpret_u64_u16(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] <= param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] <= param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_ne_signed_short_simd(Py_ssize_t arraylen, signed short *data, signed short param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	int16x4_t datasliceleft, datasliceright;
	uint16x4_t resultslice;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_s16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1_s16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceq_s16(datasliceleft, datasliceright);
		if (vreinterpret_u64_u16(resultslice) != 0xffffffffffffffff) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] != param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] != param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_eq_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint16x4_t datasliceleft, datasliceright;
	uint16x4_t resultslice;
	unsigned short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_u16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1_u16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceq_u16(datasliceleft, datasliceright);
		if (vreinterpret_u64_u16(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] == param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] == param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_gt_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint16x4_t datasliceleft, datasliceright;
	uint16x4_t resultslice;
	unsigned short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_u16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1_u16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcgt_u16(datasliceleft, datasliceright);
		if (vreinterpret_u64_u16(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] > param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] > param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_ge_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint16x4_t datasliceleft, datasliceright;
	uint16x4_t resultslice;
	unsigned short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_u16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1_u16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcge_u16(datasliceleft, datasliceright);
		if (vreinterpret_u64_u16(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] >= param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] >= param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_lt_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint16x4_t datasliceleft, datasliceright;
	uint16x4_t resultslice;
	unsigned short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_u16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1_u16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vclt_u16(datasliceleft, datasliceright);
		if (vreinterpret_u64_u16(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] < param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] < param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_le_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint16x4_t datasliceleft, datasliceright;
	uint16x4_t resultslice;
	unsigned short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_u16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1_u16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vcle_u16(datasliceleft, datasliceright);
		if (vreinterpret_u64_u16(resultslice) != 0x0000000000000000) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] <= param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] <= param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif


/*--------------------------------------------------------------------------- */
/* ARMv7 32 bit SIMD.
   For array code: H
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD.
   Returns the array index of the first matching instance, or ARR_ERR_NOTFOUND,
		if it was not found.
*/
#if defined(AF_HASSIMD_ARMv7_32BIT)
Py_ssize_t findindex_ne_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short param1) { 

	// array index counter. 
	Py_ssize_t index, fineindex; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	uint16x4_t datasliceleft, datasliceright;
	uint16x4_t resultslice;
	unsigned short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	datasliceright = vld1_u16( compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);

	// Perform the main operation using SIMD instructions.
	for (index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
		datasliceleft = vld1_u16( &data[index]);
		// The actual SIMD operation. 
		resultslice = vceq_u16(datasliceleft, datasliceright);
		if (vreinterpret_u64_u16(resultslice) != 0xffffffffffffffff) {
			// Home in on the exact location.
			for (fineindex = index; fineindex < alignedlength; fineindex++) {
				if (data[fineindex] != param1) {
					return fineindex;
				}
			}
		}
	}

	// Get the max value within the left over elements at the end of the array.
	for (index = alignedlength; index < arraylen; index++) {
		if (data[index] != param1) {
			return index;
		}
	}

	return ARR_ERR_NOTFOUND;

}

#endif

