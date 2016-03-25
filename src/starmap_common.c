//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   starmap_common.c
// Purpose:  Common code for starmap and starmapi.
// Language: C
// Date:     02-Jun-2014.
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

#include <math.h>
#include <limits.h>

#include "arithcalcs.h"
#include "arrayfunc.h"
#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */

// Auto-generated code goes below.

/*--------------------------------------------------------------------------- */
/* opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   data2 = The second input data array.
   dataout = The output data array.
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int starmap_signed_char(signed int opcode, Py_ssize_t arraylen, signed char *data, signed char *data2, signed char *dataout, unsigned int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	signed char datatmp, data2tmp, dataouttmp;
	char errflag = 0;


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] > 0) && (data[x] > (SCHAR_MAX - data2[x]))) {return ARR_ERR_OVFL;}
				if ((data2[x] < 0) && (data[x] < (SCHAR_MIN - data2[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] + data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] / data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((data2[x] == -1) && (data[x] == SCHAR_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] / data2[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data2[x] / data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((data2[x] == SCHAR_MIN) && (data[x] == -1)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data2[x] / data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (data2tmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = datatmp / data2tmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (data2tmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((data2tmp == -1) && (datatmp == SCHAR_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = datatmp / data2tmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = data2tmp / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * datatmp) != data2tmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((datatmp == -1) && (data2tmp == SCHAR_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = data2tmp / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * datatmp) != data2tmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_mod
	case OP_AF_MOD: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			data2tmp = data2[x];
			if (data2tmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataouttmp = datatmp / data2tmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = datatmp - data2tmp * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			data2tmp = data2[x];
			if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataouttmp = data2tmp / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * datatmp) != data2tmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = data2tmp - datatmp * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * data2[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] > 0) && ((data[x] > (SCHAR_MAX / data2[x])) || (data[x] < (SCHAR_MIN / data2[x])))) {return ARR_ERR_OVFL;}
				if ((data2[x] < -1) && ((data[x] < (SCHAR_MAX / data2[x])) || (data[x] > (SCHAR_MIN / data2[x])))) {return ARR_ERR_OVFL;}
				if ((data2[x] == -1) && (data[x] == SCHAR_MIN)) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] * data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_char(data[x], data2[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_char(data[x], data2[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow_r
	case OP_AF_POW_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_char(data2[x], data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_char(data2[x], data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub
	case OP_AF_SUB: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] > 0) && (data[x] < (SCHAR_MIN + data2[x]))) {return ARR_ERR_OVFL;}
				if ((data2[x] < 0) && (data[x] > (SCHAR_MAX + data2[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] - data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > 0) && (data2[x] < (SCHAR_MIN + data[x]))) {return ARR_ERR_OVFL;}
				if ((data[x] < 0) && (data2[x] > (SCHAR_MAX + data[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data2[x] - data[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_or
	case OP_AF_OR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_xor
	case OP_AF_XOR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_eq
	case OP_AF_EQ: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gt
	case OP_AF_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gte
	case OP_AF_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lt
	case OP_AF_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lte
	case OP_AF_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_ne
	case OP_AF_NE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] << data[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] >> data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
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
   data2 = The second input data array.
   dataout = The output data array.
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int starmap_unsigned_char(signed int opcode, Py_ssize_t arraylen, unsigned char *data, unsigned char *data2, unsigned char *dataout, unsigned int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 

	char errflag = 0;


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] > (UCHAR_MAX - data2[x])) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] + data2[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data[x] / data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data2[x] / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data[x] / data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data2[x] / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mod
	case OP_AF_MOD: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data[x] % data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data2[x] % data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] != 0) && (data[x] > (UCHAR_MAX / data2[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] * data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_char(data[x], data2[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_char(data[x], data2[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow_r
	case OP_AF_POW_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_char(data2[x], data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_char(data2[x], data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub
	case OP_AF_SUB: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] < data2[x]) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] - data2[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < data[x]) {return ARR_ERR_OVFL;}
				dataout[x] = data2[x] - data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_or
	case OP_AF_OR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_xor
	case OP_AF_XOR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_eq
	case OP_AF_EQ: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gt
	case OP_AF_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gte
	case OP_AF_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lt
	case OP_AF_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lte
	case OP_AF_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_ne
	case OP_AF_NE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] << data[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] >> data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
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
   data2 = The second input data array.
   dataout = The output data array.
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int starmap_signed_short(signed int opcode, Py_ssize_t arraylen, signed short *data, signed short *data2, signed short *dataout, unsigned int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	signed short datatmp, data2tmp, dataouttmp;
	char errflag = 0;


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] > 0) && (data[x] > (SHRT_MAX - data2[x]))) {return ARR_ERR_OVFL;}
				if ((data2[x] < 0) && (data[x] < (SHRT_MIN - data2[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] + data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] / data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((data2[x] == -1) && (data[x] == SHRT_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] / data2[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data2[x] / data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((data2[x] == SHRT_MIN) && (data[x] == -1)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data2[x] / data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (data2tmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = datatmp / data2tmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (data2tmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((data2tmp == -1) && (datatmp == SHRT_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = datatmp / data2tmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = data2tmp / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * datatmp) != data2tmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((datatmp == -1) && (data2tmp == SHRT_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = data2tmp / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * datatmp) != data2tmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_mod
	case OP_AF_MOD: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			data2tmp = data2[x];
			if (data2tmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataouttmp = datatmp / data2tmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = datatmp - data2tmp * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			data2tmp = data2[x];
			if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataouttmp = data2tmp / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * datatmp) != data2tmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = data2tmp - datatmp * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * data2[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] > 0) && ((data[x] > (SHRT_MAX / data2[x])) || (data[x] < (SHRT_MIN / data2[x])))) {return ARR_ERR_OVFL;}
				if ((data2[x] < -1) && ((data[x] < (SHRT_MAX / data2[x])) || (data[x] > (SHRT_MIN / data2[x])))) {return ARR_ERR_OVFL;}
				if ((data2[x] == -1) && (data[x] == SHRT_MIN)) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] * data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_short(data[x], data2[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_short(data[x], data2[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow_r
	case OP_AF_POW_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_short(data2[x], data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_short(data2[x], data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub
	case OP_AF_SUB: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] > 0) && (data[x] < (SHRT_MIN + data2[x]))) {return ARR_ERR_OVFL;}
				if ((data2[x] < 0) && (data[x] > (SHRT_MAX + data2[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] - data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > 0) && (data2[x] < (SHRT_MIN + data[x]))) {return ARR_ERR_OVFL;}
				if ((data[x] < 0) && (data2[x] > (SHRT_MAX + data[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data2[x] - data[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_or
	case OP_AF_OR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_xor
	case OP_AF_XOR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_eq
	case OP_AF_EQ: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gt
	case OP_AF_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gte
	case OP_AF_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lt
	case OP_AF_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lte
	case OP_AF_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_ne
	case OP_AF_NE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] << data[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] >> data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
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
   data2 = The second input data array.
   dataout = The output data array.
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int starmap_unsigned_short(signed int opcode, Py_ssize_t arraylen, unsigned short *data, unsigned short *data2, unsigned short *dataout, unsigned int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 

	char errflag = 0;


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] > (USHRT_MAX - data2[x])) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] + data2[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data[x] / data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data2[x] / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data[x] / data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data2[x] / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mod
	case OP_AF_MOD: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data[x] % data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data2[x] % data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] != 0) && (data[x] > (USHRT_MAX / data2[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] * data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_short(data[x], data2[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_short(data[x], data2[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow_r
	case OP_AF_POW_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_short(data2[x], data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_short(data2[x], data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub
	case OP_AF_SUB: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] < data2[x]) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] - data2[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < data[x]) {return ARR_ERR_OVFL;}
				dataout[x] = data2[x] - data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_or
	case OP_AF_OR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_xor
	case OP_AF_XOR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_eq
	case OP_AF_EQ: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gt
	case OP_AF_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gte
	case OP_AF_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lt
	case OP_AF_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lte
	case OP_AF_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_ne
	case OP_AF_NE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] << data[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] >> data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
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
   data2 = The second input data array.
   dataout = The output data array.
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int starmap_signed_int(signed int opcode, Py_ssize_t arraylen, signed int *data, signed int *data2, signed int *dataout, unsigned int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	signed int datatmp, data2tmp, dataouttmp;
	char errflag = 0;


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] > 0) && (data[x] > (INT_MAX - data2[x]))) {return ARR_ERR_OVFL;}
				if ((data2[x] < 0) && (data[x] < (INT_MIN - data2[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] + data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] / data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((data2[x] == -1) && (data[x] == INT_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] / data2[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data2[x] / data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((data2[x] == INT_MIN) && (data[x] == -1)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data2[x] / data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (data2tmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = datatmp / data2tmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (data2tmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((data2tmp == -1) && (datatmp == INT_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = datatmp / data2tmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = data2tmp / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * datatmp) != data2tmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((datatmp == -1) && (data2tmp == INT_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = data2tmp / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * datatmp) != data2tmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_mod
	case OP_AF_MOD: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			data2tmp = data2[x];
			if (data2tmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataouttmp = datatmp / data2tmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = datatmp - data2tmp * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			data2tmp = data2[x];
			if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataouttmp = data2tmp / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * datatmp) != data2tmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = data2tmp - datatmp * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * data2[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] > 0) && ((data[x] > (INT_MAX / data2[x])) || (data[x] < (INT_MIN / data2[x])))) {return ARR_ERR_OVFL;}
				if ((data2[x] < -1) && ((data[x] < (INT_MAX / data2[x])) || (data[x] > (INT_MIN / data2[x])))) {return ARR_ERR_OVFL;}
				if ((data2[x] == -1) && (data[x] == INT_MIN)) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] * data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_int(data[x], data2[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_int(data[x], data2[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow_r
	case OP_AF_POW_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_int(data2[x], data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_int(data2[x], data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub
	case OP_AF_SUB: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] > 0) && (data[x] < (INT_MIN + data2[x]))) {return ARR_ERR_OVFL;}
				if ((data2[x] < 0) && (data[x] > (INT_MAX + data2[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] - data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > 0) && (data2[x] < (INT_MIN + data[x]))) {return ARR_ERR_OVFL;}
				if ((data[x] < 0) && (data2[x] > (INT_MAX + data[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data2[x] - data[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_or
	case OP_AF_OR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_xor
	case OP_AF_XOR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_eq
	case OP_AF_EQ: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gt
	case OP_AF_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gte
	case OP_AF_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lt
	case OP_AF_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lte
	case OP_AF_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_ne
	case OP_AF_NE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] << data[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] >> data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
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
   data2 = The second input data array.
   dataout = The output data array.
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int starmap_unsigned_int(signed int opcode, Py_ssize_t arraylen, unsigned int *data, unsigned int *data2, unsigned int *dataout, unsigned int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 

	char errflag = 0;


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] > (UINT_MAX - data2[x])) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] + data2[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data[x] / data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data2[x] / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data[x] / data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data2[x] / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mod
	case OP_AF_MOD: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data[x] % data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data2[x] % data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] != 0) && (data[x] > (UINT_MAX / data2[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] * data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_int(data[x], data2[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_int(data[x], data2[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow_r
	case OP_AF_POW_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_int(data2[x], data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_int(data2[x], data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub
	case OP_AF_SUB: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] < data2[x]) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] - data2[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < data[x]) {return ARR_ERR_OVFL;}
				dataout[x] = data2[x] - data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_or
	case OP_AF_OR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_xor
	case OP_AF_XOR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_eq
	case OP_AF_EQ: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gt
	case OP_AF_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gte
	case OP_AF_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lt
	case OP_AF_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lte
	case OP_AF_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_ne
	case OP_AF_NE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] << data[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] >> data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
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
   data2 = The second input data array.
   dataout = The output data array.
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int starmap_signed_long(signed int opcode, Py_ssize_t arraylen, signed long *data, signed long *data2, signed long *dataout, unsigned int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long datatmp, data2tmp, dataouttmp;
	char errflag = 0;


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] > 0) && (data[x] > (LONG_MAX - data2[x]))) {return ARR_ERR_OVFL;}
				if ((data2[x] < 0) && (data[x] < (LONG_MIN - data2[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] + data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] / data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((data2[x] == -1) && (data[x] == LONG_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] / data2[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data2[x] / data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((data2[x] == LONG_MIN) && (data[x] == -1)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data2[x] / data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (data2tmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = datatmp / data2tmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (data2tmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((data2tmp == -1) && (datatmp == LONG_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = datatmp / data2tmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = data2tmp / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * datatmp) != data2tmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((datatmp == -1) && (data2tmp == LONG_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = data2tmp / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * datatmp) != data2tmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_mod
	case OP_AF_MOD: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			data2tmp = data2[x];
			if (data2tmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataouttmp = datatmp / data2tmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = datatmp - data2tmp * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			data2tmp = data2[x];
			if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataouttmp = data2tmp / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * datatmp) != data2tmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = data2tmp - datatmp * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * data2[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] > 0) && ((data[x] > (LONG_MAX / data2[x])) || (data[x] < (LONG_MIN / data2[x])))) {return ARR_ERR_OVFL;}
				if ((data2[x] < -1) && ((data[x] < (LONG_MAX / data2[x])) || (data[x] > (LONG_MIN / data2[x])))) {return ARR_ERR_OVFL;}
				if ((data2[x] == -1) && (data[x] == LONG_MIN)) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] * data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_long(data[x], data2[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_long(data[x], data2[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow_r
	case OP_AF_POW_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_long(data2[x], data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_long(data2[x], data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub
	case OP_AF_SUB: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] > 0) && (data[x] < (LONG_MIN + data2[x]))) {return ARR_ERR_OVFL;}
				if ((data2[x] < 0) && (data[x] > (LONG_MAX + data2[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] - data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > 0) && (data2[x] < (LONG_MIN + data[x]))) {return ARR_ERR_OVFL;}
				if ((data[x] < 0) && (data2[x] > (LONG_MAX + data[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data2[x] - data[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_or
	case OP_AF_OR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_xor
	case OP_AF_XOR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_eq
	case OP_AF_EQ: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gt
	case OP_AF_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gte
	case OP_AF_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lt
	case OP_AF_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lte
	case OP_AF_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_ne
	case OP_AF_NE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] << data[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] >> data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
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
   data2 = The second input data array.
   dataout = The output data array.
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int starmap_unsigned_long(signed int opcode, Py_ssize_t arraylen, unsigned long *data, unsigned long *data2, unsigned long *dataout, unsigned int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 

	char errflag = 0;


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] > (ULONG_MAX - data2[x])) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] + data2[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data[x] / data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data2[x] / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data[x] / data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data2[x] / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mod
	case OP_AF_MOD: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data[x] % data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data2[x] % data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] != 0) && (data[x] > (ULONG_MAX / data2[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] * data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_long(data[x], data2[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_long(data[x], data2[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow_r
	case OP_AF_POW_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_long(data2[x], data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_long(data2[x], data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub
	case OP_AF_SUB: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] < data2[x]) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] - data2[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < data[x]) {return ARR_ERR_OVFL;}
				dataout[x] = data2[x] - data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_or
	case OP_AF_OR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_xor
	case OP_AF_XOR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_eq
	case OP_AF_EQ: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gt
	case OP_AF_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gte
	case OP_AF_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lt
	case OP_AF_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lte
	case OP_AF_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_ne
	case OP_AF_NE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] << data[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] >> data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
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
   data2 = The second input data array.
   dataout = The output data array.
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int starmap_signed_long_long(signed int opcode, Py_ssize_t arraylen, signed long long *data, signed long long *data2, signed long long *dataout, unsigned int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long long datatmp, data2tmp, dataouttmp;
	char errflag = 0;


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] > 0) && (data[x] > (LLONG_MAX - data2[x]))) {return ARR_ERR_OVFL;}
				if ((data2[x] < 0) && (data[x] < (LLONG_MIN - data2[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] + data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] / data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((data2[x] == -1) && (data[x] == LLONG_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] / data2[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data2[x] / data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((data2[x] == LLONG_MIN) && (data[x] == -1)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data2[x] / data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (data2tmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = datatmp / data2tmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (data2tmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((data2tmp == -1) && (datatmp == LLONG_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = datatmp / data2tmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = data2tmp / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * datatmp) != data2tmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				data2tmp = data2[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((datatmp == -1) && (data2tmp == LLONG_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = data2tmp / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * datatmp) != data2tmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_mod
	case OP_AF_MOD: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			data2tmp = data2[x];
			if (data2tmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataouttmp = datatmp / data2tmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = datatmp - data2tmp * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			data2tmp = data2[x];
			if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataouttmp = data2tmp / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * datatmp) != data2tmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = data2tmp - datatmp * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * data2[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] > 0) && ((data[x] > (LLONG_MAX / data2[x])) || (data[x] < (LLONG_MIN / data2[x])))) {return ARR_ERR_OVFL;}
				if ((data2[x] < -1) && ((data[x] < (LLONG_MAX / data2[x])) || (data[x] > (LLONG_MIN / data2[x])))) {return ARR_ERR_OVFL;}
				if ((data2[x] == -1) && (data[x] == LLONG_MIN)) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] * data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_long_long(data[x], data2[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_long_long(data[x], data2[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow_r
	case OP_AF_POW_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_long_long(data2[x], data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_long_long(data2[x], data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub
	case OP_AF_SUB: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] > 0) && (data[x] < (LLONG_MIN + data2[x]))) {return ARR_ERR_OVFL;}
				if ((data2[x] < 0) && (data[x] > (LLONG_MAX + data2[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] - data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > 0) && (data2[x] < (LLONG_MIN + data[x]))) {return ARR_ERR_OVFL;}
				if ((data[x] < 0) && (data2[x] > (LLONG_MAX + data[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data2[x] - data[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_or
	case OP_AF_OR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_xor
	case OP_AF_XOR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_eq
	case OP_AF_EQ: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gt
	case OP_AF_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gte
	case OP_AF_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lt
	case OP_AF_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lte
	case OP_AF_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_ne
	case OP_AF_NE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] << data[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] >> data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
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
   data2 = The second input data array.
   dataout = The output data array.
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int starmap_unsigned_long_long(signed int opcode, Py_ssize_t arraylen, unsigned long long *data, unsigned long long *data2, unsigned long long *dataout, unsigned int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 

	char errflag = 0;


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] > (ULLONG_MAX - data2[x])) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] + data2[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data[x] / data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data2[x] / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data[x] / data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data2[x] / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mod
	case OP_AF_MOD: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data2[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data[x] % data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = data2[x] % data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if ((data2[x] != 0) && (data[x] > (ULLONG_MAX / data2[x]))) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] * data2[x];
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_long_long(data[x], data2[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_long_long(data[x], data2[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow_r
	case OP_AF_POW_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_long_long(data2[x], data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_long_long(data2[x], data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub
	case OP_AF_SUB: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] < data2[x]) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] - data2[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < data[x]) {return ARR_ERR_OVFL;}
				dataout[x] = data2[x] - data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_or
	case OP_AF_OR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_xor
	case OP_AF_XOR: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_eq
	case OP_AF_EQ: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gt
	case OP_AF_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_gte
	case OP_AF_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lt
	case OP_AF_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lte
	case OP_AF_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_ne
	case OP_AF_NE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] << data[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> data2[x];
		}
		return ARR_NO_ERR;
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data2[x] >> data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
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
   data2 = The second input data array.
   dataout = The output data array.
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int starmap_float(signed int opcode, Py_ssize_t arraylen, float *data, float *data2, float *dataout, unsigned int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 



	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + data2[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] / data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] / data2[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] / data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] / data[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floorf(data[x] / data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floorf(data[x] / data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floorf(data2[x] / data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floorf(data2[x] / data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_mod
	case OP_AF_MOD: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x] * floorf(data[x] / data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x] * floorf(data[x] / data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x] * floorf(data2[x] / data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x] * floorf(data2[x] / data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * data2[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = powf(data[x], data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = powf(data[x], data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow_r
	case OP_AF_POW_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = powf(data2[x], data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = powf(data2[x], data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub
	case OP_AF_SUB: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_eq
	case OP_AF_EQ: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (float) (data[x] == data2[x]);
		}
		return ARR_NO_ERR;
	}
	// af_gt
	case OP_AF_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (float) (data[x] > data2[x]);
		}
		return ARR_NO_ERR;
	}
	// af_gte
	case OP_AF_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (float) (data[x] >= data2[x]);
		}
		return ARR_NO_ERR;
	}
	// af_lt
	case OP_AF_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (float) (data[x] < data2[x]);
		}
		return ARR_NO_ERR;
	}
	// af_lte
	case OP_AF_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (float) (data[x] <= data2[x]);
		}
		return ARR_NO_ERR;
	}
	// af_ne
	case OP_AF_NE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (float) (data[x] != data2[x]);
		}
		return ARR_NO_ERR;
	}
	// math_atan2
	case OP_MATH_ATAN2: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atan2f(data[x], data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atan2f(data[x], data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_atan2_r
	case OP_MATH_ATAN2_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atan2f(data2[x], data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atan2f(data2[x], data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_copysign
	case OP_MATH_COPYSIGN: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = copysignf(data[x], data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = copysignf(data[x], data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_fmod
	case OP_MATH_FMOD: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fmodf(data[x], data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fmodf(data[x], data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_fmod_r
	case OP_MATH_FMOD_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fmodf(data2[x], data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fmodf(data2[x], data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_hypot
	case OP_MATH_HYPOT: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = hypotf(data[x], data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = hypotf(data[x], data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_hypot_r
	case OP_MATH_HYPOT_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = hypotf(data2[x], data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = hypotf(data2[x], data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_ldexp
	case OP_MATH_LDEXP: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (!isfinite(data2[x]) || (data2[x] > INT_MAX) || (data2[x] < INT_MIN)) {
					return ARR_ERR_OVFL;
				}
				dataout[x] = ldexpf(data[x], (int) data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (!isfinite(data2[x]) || (data2[x] > INT_MAX) || (data2[x] < INT_MIN)) {
					return ARR_ERR_OVFL;
				}
				dataout[x] = ldexpf(data[x], (int) data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_pow
	case OP_MATH_POW: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = powf(data[x], data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = powf(data[x], data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_pow_r
	case OP_MATH_POW_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = powf(data2[x], data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = powf(data2[x], data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
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
   data2 = The second input data array.
   dataout = The output data array.
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int starmap_double(signed int opcode, Py_ssize_t arraylen, double *data, double *data2, double *dataout, unsigned int disableovfl) { 

	// array index counter. 
	Py_ssize_t x; 



	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + data2[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] / data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] / data2[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] / data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] / data[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floor(data[x] / data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floor(data[x] / data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floor(data2[x] / data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floor(data2[x] / data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_mod
	case OP_AF_MOD: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x] * floor(data[x] / data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x] * floor(data[x] / data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x] * floor(data2[x] / data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x] * floor(data2[x] / data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * data2[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = pow(data[x], data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = pow(data[x], data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow_r
	case OP_AF_POW_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = pow(data2[x], data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = pow(data2[x], data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub
	case OP_AF_SUB: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - data2[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data2[x] - data[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// af_eq
	case OP_AF_EQ: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (double) (data[x] == data2[x]);
		}
		return ARR_NO_ERR;
	}
	// af_gt
	case OP_AF_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (double) (data[x] > data2[x]);
		}
		return ARR_NO_ERR;
	}
	// af_gte
	case OP_AF_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (double) (data[x] >= data2[x]);
		}
		return ARR_NO_ERR;
	}
	// af_lt
	case OP_AF_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (double) (data[x] < data2[x]);
		}
		return ARR_NO_ERR;
	}
	// af_lte
	case OP_AF_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (double) (data[x] <= data2[x]);
		}
		return ARR_NO_ERR;
	}
	// af_ne
	case OP_AF_NE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (double) (data[x] != data2[x]);
		}
		return ARR_NO_ERR;
	}
	// math_atan2
	case OP_MATH_ATAN2: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atan2(data[x], data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atan2(data[x], data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_atan2_r
	case OP_MATH_ATAN2_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atan2(data2[x], data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atan2(data2[x], data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_copysign
	case OP_MATH_COPYSIGN: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = copysign(data[x], data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = copysign(data[x], data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_fmod
	case OP_MATH_FMOD: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fmod(data[x], data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fmod(data[x], data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_fmod_r
	case OP_MATH_FMOD_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fmod(data2[x], data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fmod(data2[x], data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_hypot
	case OP_MATH_HYPOT: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = hypot(data[x], data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = hypot(data[x], data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_hypot_r
	case OP_MATH_HYPOT_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = hypot(data2[x], data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = hypot(data2[x], data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_ldexp
	case OP_MATH_LDEXP: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (!isfinite(data2[x]) || (data2[x] > INT_MAX) || (data2[x] < INT_MIN)) {
					return ARR_ERR_OVFL;
				}
				dataout[x] = ldexp(data[x], (int) data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (!isfinite(data2[x]) || (data2[x] > INT_MAX) || (data2[x] < INT_MIN)) {
					return ARR_ERR_OVFL;
				}
				dataout[x] = ldexp(data[x], (int) data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_pow
	case OP_MATH_POW: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = pow(data[x], data2[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = pow(data[x], data2[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_pow_r
	case OP_MATH_POW_R: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = pow(data2[x], data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = pow(data2[x], data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= data2[x] ? data2[x] : data[x];
		}
		return ARR_NO_ERR;
	}

	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */
