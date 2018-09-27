//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   aall_simd_x86.c
// Purpose:  Returns True if all elements in an array meet the selected criteria.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     01-May-2017
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

#include "simddefs.h"
#include "arrayops.h"

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
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
#ifdef AF_HASSIMD
signed int aall_signed_char_simd(signed int opcode, Py_ssize_t arraylen, signed char *data, signed char param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v16qi compslice, dataslice, eqslice, gtslice;
	signed char compvals[CHARSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < CHARSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	compslice = (v16qi) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % CHARSIMDSIZE);


	switch(opcode) {
	// AF_EQ
	case OP_AF_EQ: {
		for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
			dataslice = (v16qi) __builtin_ia32_lddqu((char *) &data[index]);
			eqslice = __builtin_ia32_pcmpeqb128(dataslice, compslice);
			if (__builtin_ia32_pmovmskb128((v16qi) eqslice) != 0xffff) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] == param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_GT
	case OP_AF_GT: {
		for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
			dataslice = (v16qi) __builtin_ia32_lddqu((char *) &data[index]);
			gtslice = __builtin_ia32_pcmpgtb128(dataslice, compslice);
			if (__builtin_ia32_pmovmskb128((v16qi) gtslice) != 0xffff) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] > param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_GTE
	case OP_AF_GTE: {
		for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
			dataslice = (v16qi) __builtin_ia32_lddqu((char *) &data[index]);
			eqslice = __builtin_ia32_pcmpeqb128(dataslice, compslice);
			gtslice = __builtin_ia32_pcmpgtb128(dataslice, compslice);
			if ((__builtin_ia32_pmovmskb128((v16qi) gtslice) | __builtin_ia32_pmovmskb128((v16qi) eqslice)) != 0xffff) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] >= param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_LT
	case OP_AF_LT: {
		for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
			dataslice = (v16qi) __builtin_ia32_lddqu((char *) &data[index]);
			eqslice = __builtin_ia32_pcmpeqb128(dataslice, compslice);
			gtslice = __builtin_ia32_pcmpgtb128(dataslice, compslice);
			if ((__builtin_ia32_pmovmskb128((v16qi) gtslice) | __builtin_ia32_pmovmskb128((v16qi) eqslice)) != 0x0000) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] < param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_LTE
	case OP_AF_LTE: {
		for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
			dataslice = (v16qi) __builtin_ia32_lddqu((char *) &data[index]);
			gtslice = __builtin_ia32_pcmpgtb128(dataslice, compslice);
			if (__builtin_ia32_pmovmskb128((v16qi) gtslice) != 0x0000) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] <= param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_NE
	case OP_AF_NE: {
		for(index = 0; index < alignedlength; index += CHARSIMDSIZE) {
			dataslice = (v16qi) __builtin_ia32_lddqu((char *) &data[index]);
			eqslice = __builtin_ia32_pcmpeqb128(dataslice, compslice);
			if (__builtin_ia32_pmovmskb128((v16qi) eqslice) == 0xffff) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
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
#endif
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: h
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
#ifdef AF_HASSIMD
signed int aall_signed_short_simd(signed int opcode, Py_ssize_t arraylen, signed short *data, signed short param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v8hi compslice, dataslice, eqslice, gtslice;
	signed short compvals[SHORTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < SHORTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	compslice = (v8hi) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % SHORTSIMDSIZE);


	switch(opcode) {
	// AF_EQ
	case OP_AF_EQ: {
		for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
			dataslice = (v8hi) __builtin_ia32_lddqu((char *) &data[index]);
			eqslice = __builtin_ia32_pcmpeqw128(dataslice, compslice);
			if (__builtin_ia32_pmovmskb128((v16qi) eqslice) != 0xffff) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] == param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_GT
	case OP_AF_GT: {
		for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
			dataslice = (v8hi) __builtin_ia32_lddqu((char *) &data[index]);
			gtslice = __builtin_ia32_pcmpgtw128(dataslice, compslice);
			if (__builtin_ia32_pmovmskb128((v16qi) gtslice) != 0xffff) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] > param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_GTE
	case OP_AF_GTE: {
		for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
			dataslice = (v8hi) __builtin_ia32_lddqu((char *) &data[index]);
			eqslice = __builtin_ia32_pcmpeqw128(dataslice, compslice);
			gtslice = __builtin_ia32_pcmpgtw128(dataslice, compslice);
			if ((__builtin_ia32_pmovmskb128((v16qi) gtslice) | __builtin_ia32_pmovmskb128((v16qi) eqslice)) != 0xffff) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] >= param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_LT
	case OP_AF_LT: {
		for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
			dataslice = (v8hi) __builtin_ia32_lddqu((char *) &data[index]);
			eqslice = __builtin_ia32_pcmpeqw128(dataslice, compslice);
			gtslice = __builtin_ia32_pcmpgtw128(dataslice, compslice);
			if ((__builtin_ia32_pmovmskb128((v16qi) gtslice) | __builtin_ia32_pmovmskb128((v16qi) eqslice)) != 0x0000) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] < param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_LTE
	case OP_AF_LTE: {
		for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
			dataslice = (v8hi) __builtin_ia32_lddqu((char *) &data[index]);
			gtslice = __builtin_ia32_pcmpgtw128(dataslice, compslice);
			if (__builtin_ia32_pmovmskb128((v16qi) gtslice) != 0x0000) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] <= param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_NE
	case OP_AF_NE: {
		for(index = 0; index < alignedlength; index += SHORTSIMDSIZE) {
			dataslice = (v8hi) __builtin_ia32_lddqu((char *) &data[index]);
			eqslice = __builtin_ia32_pcmpeqw128(dataslice, compslice);
			if (__builtin_ia32_pmovmskb128((v16qi) eqslice) == 0xffff) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
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
#endif
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: i
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
#ifdef AF_HASSIMD
signed int aall_signed_int_simd(signed int opcode, Py_ssize_t arraylen, signed int *data, signed int param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4si compslice, dataslice, eqslice, gtslice;
	signed int compvals[INTSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < INTSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	compslice = (v4si) __builtin_ia32_lddqu((char *) compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % INTSIMDSIZE);


	switch(opcode) {
	// AF_EQ
	case OP_AF_EQ: {
		for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
			dataslice = (v4si) __builtin_ia32_lddqu((char *) &data[index]);
			eqslice = __builtin_ia32_pcmpeqd128(dataslice, compslice);
			if (__builtin_ia32_pmovmskb128((v16qi) eqslice) != 0xffff) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] == param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_GT
	case OP_AF_GT: {
		for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
			dataslice = (v4si) __builtin_ia32_lddqu((char *) &data[index]);
			gtslice = __builtin_ia32_pcmpgtd128(dataslice, compslice);
			if (__builtin_ia32_pmovmskb128((v16qi) gtslice) != 0xffff) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] > param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_GTE
	case OP_AF_GTE: {
		for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
			dataslice = (v4si) __builtin_ia32_lddqu((char *) &data[index]);
			eqslice = __builtin_ia32_pcmpeqd128(dataslice, compslice);
			gtslice = __builtin_ia32_pcmpgtd128(dataslice, compslice);
			if ((__builtin_ia32_pmovmskb128((v16qi) gtslice) | __builtin_ia32_pmovmskb128((v16qi) eqslice)) != 0xffff) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] >= param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_LT
	case OP_AF_LT: {
		for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
			dataslice = (v4si) __builtin_ia32_lddqu((char *) &data[index]);
			eqslice = __builtin_ia32_pcmpeqd128(dataslice, compslice);
			gtslice = __builtin_ia32_pcmpgtd128(dataslice, compslice);
			if ((__builtin_ia32_pmovmskb128((v16qi) gtslice) | __builtin_ia32_pmovmskb128((v16qi) eqslice)) != 0x0000) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] < param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_LTE
	case OP_AF_LTE: {
		for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
			dataslice = (v4si) __builtin_ia32_lddqu((char *) &data[index]);
			gtslice = __builtin_ia32_pcmpgtd128(dataslice, compslice);
			if (__builtin_ia32_pmovmskb128((v16qi) gtslice) != 0x0000) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] <= param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_NE
	case OP_AF_NE: {
		for(index = 0; index < alignedlength; index += INTSIMDSIZE) {
			dataslice = (v4si) __builtin_ia32_lddqu((char *) &data[index]);
			eqslice = __builtin_ia32_pcmpeqd128(dataslice, compslice);
			if (__builtin_ia32_pmovmskb128((v16qi) eqslice) == 0xffff) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
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
#endif
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: f
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
#ifdef AF_HASSIMD
signed int aall_float_simd(signed int opcode, Py_ssize_t arraylen, float *data, float param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v4sf compslice, dataslice, resultslice;
	float compvals[FLOATSIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < FLOATSIMDSIZE; y++) {
		compvals[y] = param1;
	}
	compslice = (v4sf) __builtin_ia32_loadups(compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % FLOATSIMDSIZE);


	switch(opcode) {
	// AF_EQ
	case OP_AF_EQ: {
		for(index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
			dataslice = (v4sf) __builtin_ia32_loadups(&data[index]);
			resultslice = __builtin_ia32_cmpeqps(dataslice, compslice);
			if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] == param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_GT
	case OP_AF_GT: {
		for(index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
			dataslice = (v4sf) __builtin_ia32_loadups(&data[index]);
			resultslice = __builtin_ia32_cmpgtps(dataslice, compslice);
			if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] > param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_GTE
	case OP_AF_GTE: {
		for(index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
			dataslice = (v4sf) __builtin_ia32_loadups(&data[index]);
			resultslice = __builtin_ia32_cmpgeps(dataslice, compslice);
			if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] >= param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_LT
	case OP_AF_LT: {
		for(index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
			dataslice = (v4sf) __builtin_ia32_loadups(&data[index]);
			resultslice = __builtin_ia32_cmpltps(dataslice, compslice);
			if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] < param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_LTE
	case OP_AF_LTE: {
		for(index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
			dataslice = (v4sf) __builtin_ia32_loadups(&data[index]);
			resultslice = __builtin_ia32_cmpleps(dataslice, compslice);
			if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] <= param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_NE
	case OP_AF_NE: {
		for(index = 0; index < alignedlength; index += FLOATSIMDSIZE) {
			dataslice = (v4sf) __builtin_ia32_loadups(&data[index]);
			resultslice = __builtin_ia32_cmpneqps(dataslice, compslice);
			if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
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
#endif
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* For array code: d
   opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   param1 = The parameter to be applied to each array element.
   Returns 1 if the condition was true for all array elements, ARR_ERR_NOTFOUND
		 if it was false at least once, or an error code if the opcode was invalid.
*/
#ifdef AF_HASSIMD
signed int aall_double_simd(signed int opcode, Py_ssize_t arraylen, double *data, double param1) { 

	// array index counter. 
	Py_ssize_t index; 

	// SIMD related variables.
	Py_ssize_t alignedlength;
	unsigned int y;

	v2df compslice, dataslice, resultslice;
	double compvals[DOUBLESIMDSIZE];

	// Initialise the comparison values.
	for (y = 0; y < DOUBLESIMDSIZE; y++) {
		compvals[y] = param1;
	}
	compslice = (v2df) __builtin_ia32_loadupd(compvals);

	// Calculate array lengths for arrays whose lengths which are not even
	// multipes of the SIMD slice length.
	alignedlength = arraylen - (arraylen % DOUBLESIMDSIZE);


	switch(opcode) {
	// AF_EQ
	case OP_AF_EQ: {
		for(index = 0; index < alignedlength; index += DOUBLESIMDSIZE) {
			dataslice = (v2df) __builtin_ia32_loadupd(&data[index]);
			resultslice = __builtin_ia32_cmpeqpd(dataslice, compslice);
			if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] == param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_GT
	case OP_AF_GT: {
		for(index = 0; index < alignedlength; index += DOUBLESIMDSIZE) {
			dataslice = (v2df) __builtin_ia32_loadupd(&data[index]);
			resultslice = __builtin_ia32_cmpgtpd(dataslice, compslice);
			if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] > param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_GTE
	case OP_AF_GTE: {
		for(index = 0; index < alignedlength; index += DOUBLESIMDSIZE) {
			dataslice = (v2df) __builtin_ia32_loadupd(&data[index]);
			resultslice = __builtin_ia32_cmpgepd(dataslice, compslice);
			if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] >= param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_LT
	case OP_AF_LT: {
		for(index = 0; index < alignedlength; index += DOUBLESIMDSIZE) {
			dataslice = (v2df) __builtin_ia32_loadupd(&data[index]);
			resultslice = __builtin_ia32_cmpltpd(dataslice, compslice);
			if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] < param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_LTE
	case OP_AF_LTE: {
		for(index = 0; index < alignedlength; index += DOUBLESIMDSIZE) {
			dataslice = (v2df) __builtin_ia32_loadupd(&data[index]);
			resultslice = __builtin_ia32_cmplepd(dataslice, compslice);
			if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
			if (!(data[index] <= param1)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		return 1;

	}
	// AF_NE
	case OP_AF_NE: {
		for(index = 0; index < alignedlength; index += DOUBLESIMDSIZE) {
			dataslice = (v2df) __builtin_ia32_loadupd(&data[index]);
			resultslice = __builtin_ia32_cmpneqpd(dataslice, compslice);
			if (!(__builtin_ia32_pmovmskb128((v16qi) resultslice) == 0xffff)) {
				return ARR_ERR_NOTFOUND;
			}
		}

		// Get the max value within the left over elements at the end of the array.
		for(index = alignedlength; index < arraylen; index++) {
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
#endif
/*--------------------------------------------------------------------------- */
