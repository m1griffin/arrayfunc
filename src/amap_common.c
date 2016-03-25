//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   amap_common.c
// Purpose:  Common code for amap and amapi.
// Language: C
// Date:     09-Apr-2014
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
#include "arrayerrs.h"
#include "arrayfunc.h"

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

// The auto-generated code goes below.

/*--------------------------------------------------------------------------- */
/* opcode = The operator or function code to select what to execute.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   paramcount = The number of valid parameters (normally 0 or 1).
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int map_signed_char(signed int opcode, Py_ssize_t arraylen, signed char *data, signed char *dataout, signed char param1, unsigned int paramcount, unsigned int disableovfl) {

	// array index counter.
	Py_ssize_t x;

	char errflag = 0;

	signed char ovtmp1, ovtmp2, datatmp, dataouttmp;	// Used for overflow calculations.


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = data[x]; 
				}
			}
			if (param1 > 0) {
				ovtmp1 = SCHAR_MAX - param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] + param1; 
				}
			}
			if (param1 < 0) {
				ovtmp1 = SCHAR_MIN - param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] < ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] + param1; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] / param1;
			}
		} else {
		// Overflow checking enabled.
			ovtmp1 = (param1 == -1);		// Overflow check.
			for(x = 0; x < arraylen; x++) {
				if (ovtmp1 && (data[x] == SCHAR_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] / param1; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = param1 / data[x];
			}
		} else {
		// Overflow checking enabled.
			ovtmp1 = (param1 == SCHAR_MIN);		// Overflow check.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if (ovtmp1 && (data[x] == -1)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = param1 / data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				dataouttmp = datatmp / param1;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * param1) != datatmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				if ((param1 == -1) && (datatmp == SCHAR_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = datatmp / param1;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * param1) != datatmp)) { 
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
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = param1 / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * datatmp) != param1)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((datatmp == -1) && (param1 == SCHAR_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = param1 / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * datatmp) != param1)) { 
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
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			dataouttmp = datatmp / param1;
			// This check is required for floor division.
			if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * param1) != datatmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = datatmp - param1 * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataouttmp = param1 / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * datatmp) != param1)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = param1 - datatmp * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = 0; 
				}
			} else {
				// Signed integers do not have a symetrical range (e.g. -128 to 127). 
				if (param1 == -1) {
					for(x = 0; x < arraylen; x++) {
						if (data[x] == SCHAR_MIN) {return ARR_ERR_OVFL;}
						dataout[x] = data[x] * param1; 
					}
				} else {
					ovtmp1 = SCHAR_MAX / param1;
					ovtmp2 = SCHAR_MIN / param1;
					if (param1 > 0) {
						for(x = 0; x < arraylen; x++) {
							if ((data[x] > ovtmp1) || (data[x] < ovtmp2)) {return ARR_ERR_OVFL;}
							dataout[x] = data[x] * param1; 
						}
					}
					if (param1 < -1) {
						for(x = 0; x < arraylen; x++) {
							if ((data[x] < ovtmp1) || (data[x] > ovtmp2)) {return ARR_ERR_OVFL;}
							dataout[x] = data[x] * param1; 
						}
					}
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_neg
	case OP_AF_NEG: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == SCHAR_MIN) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = -data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_char(data[x], param1, &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_char(data[x], param1, &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_pow_r
	case OP_AF_POW_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_char(param1, data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_char(param1, data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_sub
	case OP_AF_SUB: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = data[x]; 
				}
			}
			if (param1 > 0) {
				ovtmp1 = SCHAR_MIN + param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] < ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] - param1; 
				}
			}
			if (param1 < 0) {
				ovtmp1 = SCHAR_MAX + param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] - param1; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x];
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					if (data[x] == SCHAR_MIN) {return ARR_ERR_OVFL;}
					dataout[x] = -data[x]; 
				}
			}
			if (param1 > 0) {
				ovtmp1 = param1 - SCHAR_MAX;
				for(x = 0; x < arraylen; x++) {
					if (data[x] < ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = param1 - data[x]; 
				}
			}
			if (param1 < 0) {
				ovtmp1 = param1 - SCHAR_MIN;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = param1 - data[x]; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & param1;
		}
		return ARR_NO_ERR; 
	}
	// af_or
	case OP_AF_OR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | param1;
		}
		return ARR_NO_ERR; 
	}
	// af_xor
	case OP_AF_XOR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ param1;
		}
		return ARR_NO_ERR; 
	}
	// af_invert
	case OP_AF_INVERT: { 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_eq
	case OP_AF_EQ: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gt
	case OP_AF_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gte
	case OP_AF_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lt
	case OP_AF_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lte
	case OP_AF_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_ne
	case OP_AF_NE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 << data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> param1;
		}
		return ARR_NO_ERR; 
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 >> data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_abs
	case OP_AF_ABS: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] >= 0 ? data[x] : -data[x]; 
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == SCHAR_MIN) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] >= 0 ? data[x] : -data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// math_factorial
	case OP_MATH_FACTORIAL: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_signed_char(data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_signed_char(data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1 ? param1 : data[x];
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
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   paramcount = The number of valid parameters (normally 0 or 1).
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int map_unsigned_char(signed int opcode, Py_ssize_t arraylen, unsigned char *data, unsigned char *dataout, unsigned char param1, unsigned int paramcount, unsigned int disableovfl) {

	// array index counter.
	Py_ssize_t x;

	char errflag = 0;

	unsigned char ovtmp1;	// Used for overflow calculations.


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + param1;
			}
		} else {
		// Overflow checking enabled.
			ovtmp1 = UCHAR_MAX - param1;		// Overflow check.
			for(x = 0; x < arraylen; x++) {
				if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] + param1; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] / param1;
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = param1 / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] / param1;
		}
		return ARR_NO_ERR;
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = param1 / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mod
	case OP_AF_MOD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] % param1;
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = param1 % data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = 0; 
				}
			} else {
				ovtmp1 = UCHAR_MAX / param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] * param1; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_char(data[x], param1, &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_char(data[x], param1, &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_pow_r
	case OP_AF_POW_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_char(param1, data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_char(param1, data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_sub
	case OP_AF_SUB: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1;
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] < param1) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] - param1; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (param1 < data[x]) {return ARR_ERR_OVFL;}
				dataout[x] = param1 - data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & param1;
		}
		return ARR_NO_ERR; 
	}
	// af_or
	case OP_AF_OR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | param1;
		}
		return ARR_NO_ERR; 
	}
	// af_xor
	case OP_AF_XOR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ param1;
		}
		return ARR_NO_ERR; 
	}
	// af_invert
	case OP_AF_INVERT: { 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_eq
	case OP_AF_EQ: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gt
	case OP_AF_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gte
	case OP_AF_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lt
	case OP_AF_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lte
	case OP_AF_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_ne
	case OP_AF_NE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 << data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> param1;
		}
		return ARR_NO_ERR; 
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 >> data[x];
		}
		return ARR_NO_ERR; 
	}
	// math_factorial
	case OP_MATH_FACTORIAL: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_unsigned_char(data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_unsigned_char(data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1 ? param1 : data[x];
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
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   paramcount = The number of valid parameters (normally 0 or 1).
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int map_signed_short(signed int opcode, Py_ssize_t arraylen, signed short *data, signed short *dataout, signed short param1, unsigned int paramcount, unsigned int disableovfl) {

	// array index counter.
	Py_ssize_t x;

	char errflag = 0;

	signed short ovtmp1, ovtmp2, datatmp, dataouttmp;	// Used for overflow calculations.


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = data[x]; 
				}
			}
			if (param1 > 0) {
				ovtmp1 = SHRT_MAX - param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] + param1; 
				}
			}
			if (param1 < 0) {
				ovtmp1 = SHRT_MIN - param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] < ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] + param1; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] / param1;
			}
		} else {
		// Overflow checking enabled.
			ovtmp1 = (param1 == -1);		// Overflow check.
			for(x = 0; x < arraylen; x++) {
				if (ovtmp1 && (data[x] == SHRT_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] / param1; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = param1 / data[x];
			}
		} else {
		// Overflow checking enabled.
			ovtmp1 = (param1 == SHRT_MIN);		// Overflow check.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if (ovtmp1 && (data[x] == -1)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = param1 / data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				dataouttmp = datatmp / param1;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * param1) != datatmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				if ((param1 == -1) && (datatmp == SHRT_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = datatmp / param1;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * param1) != datatmp)) { 
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
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = param1 / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * datatmp) != param1)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((datatmp == -1) && (param1 == SHRT_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = param1 / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * datatmp) != param1)) { 
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
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			dataouttmp = datatmp / param1;
			// This check is required for floor division.
			if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * param1) != datatmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = datatmp - param1 * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataouttmp = param1 / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * datatmp) != param1)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = param1 - datatmp * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = 0; 
				}
			} else {
				// Signed integers do not have a symetrical range (e.g. -128 to 127). 
				if (param1 == -1) {
					for(x = 0; x < arraylen; x++) {
						if (data[x] == SHRT_MIN) {return ARR_ERR_OVFL;}
						dataout[x] = data[x] * param1; 
					}
				} else {
					ovtmp1 = SHRT_MAX / param1;
					ovtmp2 = SHRT_MIN / param1;
					if (param1 > 0) {
						for(x = 0; x < arraylen; x++) {
							if ((data[x] > ovtmp1) || (data[x] < ovtmp2)) {return ARR_ERR_OVFL;}
							dataout[x] = data[x] * param1; 
						}
					}
					if (param1 < -1) {
						for(x = 0; x < arraylen; x++) {
							if ((data[x] < ovtmp1) || (data[x] > ovtmp2)) {return ARR_ERR_OVFL;}
							dataout[x] = data[x] * param1; 
						}
					}
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_neg
	case OP_AF_NEG: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == SHRT_MIN) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = -data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_short(data[x], param1, &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_short(data[x], param1, &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_pow_r
	case OP_AF_POW_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_short(param1, data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_short(param1, data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_sub
	case OP_AF_SUB: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = data[x]; 
				}
			}
			if (param1 > 0) {
				ovtmp1 = SHRT_MIN + param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] < ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] - param1; 
				}
			}
			if (param1 < 0) {
				ovtmp1 = SHRT_MAX + param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] - param1; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x];
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					if (data[x] == SHRT_MIN) {return ARR_ERR_OVFL;}
					dataout[x] = -data[x]; 
				}
			}
			if (param1 > 0) {
				ovtmp1 = param1 - SHRT_MAX;
				for(x = 0; x < arraylen; x++) {
					if (data[x] < ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = param1 - data[x]; 
				}
			}
			if (param1 < 0) {
				ovtmp1 = param1 - SHRT_MIN;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = param1 - data[x]; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & param1;
		}
		return ARR_NO_ERR; 
	}
	// af_or
	case OP_AF_OR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | param1;
		}
		return ARR_NO_ERR; 
	}
	// af_xor
	case OP_AF_XOR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ param1;
		}
		return ARR_NO_ERR; 
	}
	// af_invert
	case OP_AF_INVERT: { 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_eq
	case OP_AF_EQ: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gt
	case OP_AF_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gte
	case OP_AF_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lt
	case OP_AF_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lte
	case OP_AF_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_ne
	case OP_AF_NE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 << data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> param1;
		}
		return ARR_NO_ERR; 
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 >> data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_abs
	case OP_AF_ABS: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] >= 0 ? data[x] : -data[x]; 
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == SHRT_MIN) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] >= 0 ? data[x] : -data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// math_factorial
	case OP_MATH_FACTORIAL: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_signed_short(data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_signed_short(data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1 ? param1 : data[x];
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
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   paramcount = The number of valid parameters (normally 0 or 1).
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int map_unsigned_short(signed int opcode, Py_ssize_t arraylen, unsigned short *data, unsigned short *dataout, unsigned short param1, unsigned int paramcount, unsigned int disableovfl) {

	// array index counter.
	Py_ssize_t x;

	char errflag = 0;

	unsigned short ovtmp1;	// Used for overflow calculations.


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + param1;
			}
		} else {
		// Overflow checking enabled.
			ovtmp1 = USHRT_MAX - param1;		// Overflow check.
			for(x = 0; x < arraylen; x++) {
				if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] + param1; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] / param1;
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = param1 / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] / param1;
		}
		return ARR_NO_ERR;
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = param1 / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mod
	case OP_AF_MOD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] % param1;
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = param1 % data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = 0; 
				}
			} else {
				ovtmp1 = USHRT_MAX / param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] * param1; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_short(data[x], param1, &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_short(data[x], param1, &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_pow_r
	case OP_AF_POW_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_short(param1, data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_short(param1, data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_sub
	case OP_AF_SUB: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1;
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] < param1) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] - param1; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (param1 < data[x]) {return ARR_ERR_OVFL;}
				dataout[x] = param1 - data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & param1;
		}
		return ARR_NO_ERR; 
	}
	// af_or
	case OP_AF_OR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | param1;
		}
		return ARR_NO_ERR; 
	}
	// af_xor
	case OP_AF_XOR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ param1;
		}
		return ARR_NO_ERR; 
	}
	// af_invert
	case OP_AF_INVERT: { 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_eq
	case OP_AF_EQ: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gt
	case OP_AF_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gte
	case OP_AF_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lt
	case OP_AF_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lte
	case OP_AF_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_ne
	case OP_AF_NE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 << data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> param1;
		}
		return ARR_NO_ERR; 
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 >> data[x];
		}
		return ARR_NO_ERR; 
	}
	// math_factorial
	case OP_MATH_FACTORIAL: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_unsigned_short(data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_unsigned_short(data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1 ? param1 : data[x];
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
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   paramcount = The number of valid parameters (normally 0 or 1).
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int map_signed_int(signed int opcode, Py_ssize_t arraylen, signed int *data, signed int *dataout, signed int param1, unsigned int paramcount, unsigned int disableovfl) {

	// array index counter.
	Py_ssize_t x;

	char errflag = 0;

	signed int ovtmp1, ovtmp2, datatmp, dataouttmp;	// Used for overflow calculations.


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = data[x]; 
				}
			}
			if (param1 > 0) {
				ovtmp1 = INT_MAX - param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] + param1; 
				}
			}
			if (param1 < 0) {
				ovtmp1 = INT_MIN - param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] < ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] + param1; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] / param1;
			}
		} else {
		// Overflow checking enabled.
			ovtmp1 = (param1 == -1);		// Overflow check.
			for(x = 0; x < arraylen; x++) {
				if (ovtmp1 && (data[x] == INT_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] / param1; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = param1 / data[x];
			}
		} else {
		// Overflow checking enabled.
			ovtmp1 = (param1 == INT_MIN);		// Overflow check.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if (ovtmp1 && (data[x] == -1)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = param1 / data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				dataouttmp = datatmp / param1;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * param1) != datatmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				if ((param1 == -1) && (datatmp == INT_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = datatmp / param1;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * param1) != datatmp)) { 
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
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = param1 / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * datatmp) != param1)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((datatmp == -1) && (param1 == INT_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = param1 / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * datatmp) != param1)) { 
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
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			dataouttmp = datatmp / param1;
			// This check is required for floor division.
			if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * param1) != datatmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = datatmp - param1 * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataouttmp = param1 / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * datatmp) != param1)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = param1 - datatmp * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = 0; 
				}
			} else {
				// Signed integers do not have a symetrical range (e.g. -128 to 127). 
				if (param1 == -1) {
					for(x = 0; x < arraylen; x++) {
						if (data[x] == INT_MIN) {return ARR_ERR_OVFL;}
						dataout[x] = data[x] * param1; 
					}
				} else {
					ovtmp1 = INT_MAX / param1;
					ovtmp2 = INT_MIN / param1;
					if (param1 > 0) {
						for(x = 0; x < arraylen; x++) {
							if ((data[x] > ovtmp1) || (data[x] < ovtmp2)) {return ARR_ERR_OVFL;}
							dataout[x] = data[x] * param1; 
						}
					}
					if (param1 < -1) {
						for(x = 0; x < arraylen; x++) {
							if ((data[x] < ovtmp1) || (data[x] > ovtmp2)) {return ARR_ERR_OVFL;}
							dataout[x] = data[x] * param1; 
						}
					}
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_neg
	case OP_AF_NEG: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == INT_MIN) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = -data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_int(data[x], param1, &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_int(data[x], param1, &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_pow_r
	case OP_AF_POW_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_int(param1, data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_int(param1, data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_sub
	case OP_AF_SUB: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = data[x]; 
				}
			}
			if (param1 > 0) {
				ovtmp1 = INT_MIN + param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] < ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] - param1; 
				}
			}
			if (param1 < 0) {
				ovtmp1 = INT_MAX + param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] - param1; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x];
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					if (data[x] == INT_MIN) {return ARR_ERR_OVFL;}
					dataout[x] = -data[x]; 
				}
			}
			if (param1 > 0) {
				ovtmp1 = param1 - INT_MAX;
				for(x = 0; x < arraylen; x++) {
					if (data[x] < ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = param1 - data[x]; 
				}
			}
			if (param1 < 0) {
				ovtmp1 = param1 - INT_MIN;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = param1 - data[x]; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & param1;
		}
		return ARR_NO_ERR; 
	}
	// af_or
	case OP_AF_OR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | param1;
		}
		return ARR_NO_ERR; 
	}
	// af_xor
	case OP_AF_XOR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ param1;
		}
		return ARR_NO_ERR; 
	}
	// af_invert
	case OP_AF_INVERT: { 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_eq
	case OP_AF_EQ: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gt
	case OP_AF_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gte
	case OP_AF_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lt
	case OP_AF_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lte
	case OP_AF_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_ne
	case OP_AF_NE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 << data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> param1;
		}
		return ARR_NO_ERR; 
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 >> data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_abs
	case OP_AF_ABS: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] >= 0 ? data[x] : -data[x]; 
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == INT_MIN) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] >= 0 ? data[x] : -data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// math_factorial
	case OP_MATH_FACTORIAL: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_signed_int(data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_signed_int(data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1 ? param1 : data[x];
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
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   paramcount = The number of valid parameters (normally 0 or 1).
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int map_unsigned_int(signed int opcode, Py_ssize_t arraylen, unsigned int *data, unsigned int *dataout, unsigned int param1, unsigned int paramcount, unsigned int disableovfl) {

	// array index counter.
	Py_ssize_t x;

	char errflag = 0;

	unsigned int ovtmp1;	// Used for overflow calculations.


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + param1;
			}
		} else {
		// Overflow checking enabled.
			ovtmp1 = UINT_MAX - param1;		// Overflow check.
			for(x = 0; x < arraylen; x++) {
				if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] + param1; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] / param1;
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = param1 / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] / param1;
		}
		return ARR_NO_ERR;
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = param1 / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mod
	case OP_AF_MOD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] % param1;
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = param1 % data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = 0; 
				}
			} else {
				ovtmp1 = UINT_MAX / param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] * param1; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_int(data[x], param1, &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_int(data[x], param1, &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_pow_r
	case OP_AF_POW_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_int(param1, data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_int(param1, data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_sub
	case OP_AF_SUB: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1;
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] < param1) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] - param1; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (param1 < data[x]) {return ARR_ERR_OVFL;}
				dataout[x] = param1 - data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & param1;
		}
		return ARR_NO_ERR; 
	}
	// af_or
	case OP_AF_OR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | param1;
		}
		return ARR_NO_ERR; 
	}
	// af_xor
	case OP_AF_XOR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ param1;
		}
		return ARR_NO_ERR; 
	}
	// af_invert
	case OP_AF_INVERT: { 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_eq
	case OP_AF_EQ: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gt
	case OP_AF_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gte
	case OP_AF_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lt
	case OP_AF_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lte
	case OP_AF_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_ne
	case OP_AF_NE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 << data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> param1;
		}
		return ARR_NO_ERR; 
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 >> data[x];
		}
		return ARR_NO_ERR; 
	}
	// math_factorial
	case OP_MATH_FACTORIAL: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_unsigned_int(data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_unsigned_int(data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1 ? param1 : data[x];
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
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   paramcount = The number of valid parameters (normally 0 or 1).
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int map_signed_long(signed int opcode, Py_ssize_t arraylen, signed long *data, signed long *dataout, signed long param1, unsigned int paramcount, unsigned int disableovfl) {

	// array index counter.
	Py_ssize_t x;

	char errflag = 0;

	signed long ovtmp1, ovtmp2, datatmp, dataouttmp;	// Used for overflow calculations.


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = data[x]; 
				}
			}
			if (param1 > 0) {
				ovtmp1 = LONG_MAX - param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] + param1; 
				}
			}
			if (param1 < 0) {
				ovtmp1 = LONG_MIN - param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] < ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] + param1; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] / param1;
			}
		} else {
		// Overflow checking enabled.
			ovtmp1 = (param1 == -1);		// Overflow check.
			for(x = 0; x < arraylen; x++) {
				if (ovtmp1 && (data[x] == LONG_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] / param1; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = param1 / data[x];
			}
		} else {
		// Overflow checking enabled.
			ovtmp1 = (param1 == LONG_MIN);		// Overflow check.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if (ovtmp1 && (data[x] == -1)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = param1 / data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				dataouttmp = datatmp / param1;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * param1) != datatmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				if ((param1 == -1) && (datatmp == LONG_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = datatmp / param1;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * param1) != datatmp)) { 
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
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = param1 / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * datatmp) != param1)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((datatmp == -1) && (param1 == LONG_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = param1 / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * datatmp) != param1)) { 
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
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			dataouttmp = datatmp / param1;
			// This check is required for floor division.
			if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * param1) != datatmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = datatmp - param1 * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataouttmp = param1 / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * datatmp) != param1)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = param1 - datatmp * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = 0; 
				}
			} else {
				// Signed integers do not have a symetrical range (e.g. -128 to 127). 
				if (param1 == -1) {
					for(x = 0; x < arraylen; x++) {
						if (data[x] == LONG_MIN) {return ARR_ERR_OVFL;}
						dataout[x] = data[x] * param1; 
					}
				} else {
					ovtmp1 = LONG_MAX / param1;
					ovtmp2 = LONG_MIN / param1;
					if (param1 > 0) {
						for(x = 0; x < arraylen; x++) {
							if ((data[x] > ovtmp1) || (data[x] < ovtmp2)) {return ARR_ERR_OVFL;}
							dataout[x] = data[x] * param1; 
						}
					}
					if (param1 < -1) {
						for(x = 0; x < arraylen; x++) {
							if ((data[x] < ovtmp1) || (data[x] > ovtmp2)) {return ARR_ERR_OVFL;}
							dataout[x] = data[x] * param1; 
						}
					}
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_neg
	case OP_AF_NEG: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == LONG_MIN) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = -data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_long(data[x], param1, &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_long(data[x], param1, &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_pow_r
	case OP_AF_POW_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_long(param1, data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_long(param1, data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_sub
	case OP_AF_SUB: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = data[x]; 
				}
			}
			if (param1 > 0) {
				ovtmp1 = LONG_MIN + param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] < ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] - param1; 
				}
			}
			if (param1 < 0) {
				ovtmp1 = LONG_MAX + param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] - param1; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x];
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					if (data[x] == LONG_MIN) {return ARR_ERR_OVFL;}
					dataout[x] = -data[x]; 
				}
			}
			if (param1 > 0) {
				ovtmp1 = param1 - LONG_MAX;
				for(x = 0; x < arraylen; x++) {
					if (data[x] < ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = param1 - data[x]; 
				}
			}
			if (param1 < 0) {
				ovtmp1 = param1 - LONG_MIN;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = param1 - data[x]; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & param1;
		}
		return ARR_NO_ERR; 
	}
	// af_or
	case OP_AF_OR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | param1;
		}
		return ARR_NO_ERR; 
	}
	// af_xor
	case OP_AF_XOR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ param1;
		}
		return ARR_NO_ERR; 
	}
	// af_invert
	case OP_AF_INVERT: { 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_eq
	case OP_AF_EQ: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gt
	case OP_AF_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gte
	case OP_AF_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lt
	case OP_AF_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lte
	case OP_AF_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_ne
	case OP_AF_NE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 << data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> param1;
		}
		return ARR_NO_ERR; 
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 >> data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_abs
	case OP_AF_ABS: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] >= 0 ? data[x] : -data[x]; 
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == LONG_MIN) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] >= 0 ? data[x] : -data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// math_factorial
	case OP_MATH_FACTORIAL: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_signed_long(data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_signed_long(data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1 ? param1 : data[x];
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
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   paramcount = The number of valid parameters (normally 0 or 1).
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int map_unsigned_long(signed int opcode, Py_ssize_t arraylen, unsigned long *data, unsigned long *dataout, unsigned long param1, unsigned int paramcount, unsigned int disableovfl) {

	// array index counter.
	Py_ssize_t x;

	char errflag = 0;

	unsigned long ovtmp1;	// Used for overflow calculations.


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + param1;
			}
		} else {
		// Overflow checking enabled.
			ovtmp1 = ULONG_MAX - param1;		// Overflow check.
			for(x = 0; x < arraylen; x++) {
				if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] + param1; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] / param1;
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = param1 / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] / param1;
		}
		return ARR_NO_ERR;
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = param1 / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mod
	case OP_AF_MOD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] % param1;
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = param1 % data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = 0; 
				}
			} else {
				ovtmp1 = ULONG_MAX / param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] * param1; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_long(data[x], param1, &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_long(data[x], param1, &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_pow_r
	case OP_AF_POW_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_long(param1, data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_long(param1, data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_sub
	case OP_AF_SUB: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1;
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] < param1) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] - param1; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (param1 < data[x]) {return ARR_ERR_OVFL;}
				dataout[x] = param1 - data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & param1;
		}
		return ARR_NO_ERR; 
	}
	// af_or
	case OP_AF_OR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | param1;
		}
		return ARR_NO_ERR; 
	}
	// af_xor
	case OP_AF_XOR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ param1;
		}
		return ARR_NO_ERR; 
	}
	// af_invert
	case OP_AF_INVERT: { 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_eq
	case OP_AF_EQ: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gt
	case OP_AF_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gte
	case OP_AF_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lt
	case OP_AF_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lte
	case OP_AF_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_ne
	case OP_AF_NE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 << data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> param1;
		}
		return ARR_NO_ERR; 
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 >> data[x];
		}
		return ARR_NO_ERR; 
	}
	// math_factorial
	case OP_MATH_FACTORIAL: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_unsigned_long(data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_unsigned_long(data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1 ? param1 : data[x];
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
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   paramcount = The number of valid parameters (normally 0 or 1).
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int map_signed_long_long(signed int opcode, Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1, unsigned int paramcount, unsigned int disableovfl) {

	// array index counter.
	Py_ssize_t x;

	char errflag = 0;

	signed long long ovtmp1, ovtmp2, datatmp, dataouttmp;	// Used for overflow calculations.


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = data[x]; 
				}
			}
			if (param1 > 0) {
				ovtmp1 = LLONG_MAX - param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] + param1; 
				}
			}
			if (param1 < 0) {
				ovtmp1 = LLONG_MIN - param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] < ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] + param1; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] / param1;
			}
		} else {
		// Overflow checking enabled.
			ovtmp1 = (param1 == -1);		// Overflow check.
			for(x = 0; x < arraylen; x++) {
				if (ovtmp1 && (data[x] == LLONG_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] / param1; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = param1 / data[x];
			}
		} else {
		// Overflow checking enabled.
			ovtmp1 = (param1 == LLONG_MIN);		// Overflow check.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if (ovtmp1 && (data[x] == -1)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = param1 / data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				dataouttmp = datatmp / param1;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * param1) != datatmp)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				if ((param1 == -1) && (datatmp == LLONG_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = datatmp / param1;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * param1) != datatmp)) { 
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
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = param1 / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * datatmp) != param1)) { 
					dataout[x] = dataouttmp - 1; 
				} else {
					dataout[x] = dataouttmp;
				}
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				datatmp = data[x];
				if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
				if ((datatmp == -1) && (param1 == LLONG_MIN)) {return ARR_ERR_OVFL;}		// Overflow check.
				dataouttmp = param1 / datatmp;
				// This check is required for floor division.
				if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * datatmp) != param1)) { 
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
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			dataouttmp = datatmp / param1;
			// This check is required for floor division.
			if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * param1) != datatmp)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = datatmp - param1 * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			datatmp = data[x];
			if (datatmp == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataouttmp = param1 / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param1 < 0)) && ((dataouttmp * datatmp) != param1)) { 
				dataouttmp = dataouttmp - 1;
			}
			dataout[x] = param1 - datatmp * dataouttmp;
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = 0; 
				}
			} else {
				// Signed integers do not have a symetrical range (e.g. -128 to 127). 
				if (param1 == -1) {
					for(x = 0; x < arraylen; x++) {
						if (data[x] == LLONG_MIN) {return ARR_ERR_OVFL;}
						dataout[x] = data[x] * param1; 
					}
				} else {
					ovtmp1 = LLONG_MAX / param1;
					ovtmp2 = LLONG_MIN / param1;
					if (param1 > 0) {
						for(x = 0; x < arraylen; x++) {
							if ((data[x] > ovtmp1) || (data[x] < ovtmp2)) {return ARR_ERR_OVFL;}
							dataout[x] = data[x] * param1; 
						}
					}
					if (param1 < -1) {
						for(x = 0; x < arraylen; x++) {
							if ((data[x] < ovtmp1) || (data[x] > ovtmp2)) {return ARR_ERR_OVFL;}
							dataout[x] = data[x] * param1; 
						}
					}
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_neg
	case OP_AF_NEG: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == LLONG_MIN) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = -data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_long_long(data[x], param1, &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_long_long(data[x], param1, &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_pow_r
	case OP_AF_POW_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_long_long(param1, data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_signed_long_long(param1, data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_sub
	case OP_AF_SUB: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = data[x]; 
				}
			}
			if (param1 > 0) {
				ovtmp1 = LLONG_MIN + param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] < ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] - param1; 
				}
			}
			if (param1 < 0) {
				ovtmp1 = LLONG_MAX + param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] - param1; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x];
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					if (data[x] == LLONG_MIN) {return ARR_ERR_OVFL;}
					dataout[x] = -data[x]; 
				}
			}
			if (param1 > 0) {
				ovtmp1 = param1 - LLONG_MAX;
				for(x = 0; x < arraylen; x++) {
					if (data[x] < ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = param1 - data[x]; 
				}
			}
			if (param1 < 0) {
				ovtmp1 = param1 - LLONG_MIN;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = param1 - data[x]; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & param1;
		}
		return ARR_NO_ERR; 
	}
	// af_or
	case OP_AF_OR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | param1;
		}
		return ARR_NO_ERR; 
	}
	// af_xor
	case OP_AF_XOR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ param1;
		}
		return ARR_NO_ERR; 
	}
	// af_invert
	case OP_AF_INVERT: { 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_eq
	case OP_AF_EQ: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gt
	case OP_AF_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gte
	case OP_AF_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lt
	case OP_AF_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lte
	case OP_AF_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_ne
	case OP_AF_NE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 << data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> param1;
		}
		return ARR_NO_ERR; 
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 >> data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_abs
	case OP_AF_ABS: {
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] >= 0 ? data[x] : -data[x]; 
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] == LLONG_MIN) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] >= 0 ? data[x] : -data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// math_factorial
	case OP_MATH_FACTORIAL: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_signed_long_long(data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_signed_long_long(data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1 ? param1 : data[x];
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
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   paramcount = The number of valid parameters (normally 0 or 1).
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int map_unsigned_long_long(signed int opcode, Py_ssize_t arraylen, unsigned long long *data, unsigned long long *dataout, unsigned long long param1, unsigned int paramcount, unsigned int disableovfl) {

	// array index counter.
	Py_ssize_t x;

	char errflag = 0;

	unsigned long long ovtmp1;	// Used for overflow calculations.


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + param1;
			}
		} else {
		// Overflow checking enabled.
			ovtmp1 = ULLONG_MAX - param1;		// Overflow check.
			for(x = 0; x < arraylen; x++) {
				if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}		// Overflow check.
				dataout[x] = data[x] + param1; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_div
	case OP_AF_DIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] / param1;
		}
		return ARR_NO_ERR;
	}
	// af_div_r
	case OP_AF_DIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = param1 / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] / param1;
		}
		return ARR_NO_ERR;
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = param1 / data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mod
	case OP_AF_MOD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		if (param1 == 0) {return ARR_ERR_OVFL;}		// Overflow check.
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] % param1;
		}
		return ARR_NO_ERR;
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Cannot disable divide by zero checking because this causes a crash.
		for(x = 0; x < arraylen; x++) {
			if (data[x] == 0) {return ARR_ERR_OVFL;}		// Overflow check.
			dataout[x] = param1 % data[x];
		}
		return ARR_NO_ERR;
	}
	// af_mult
	case OP_AF_MULT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * param1;
			}
		} else {
		// Overflow checking enabled.
			if (param1 == 0) {
				for(x = 0; x < arraylen; x++) {
					dataout[x] = 0; 
				}
			} else {
				ovtmp1 = ULLONG_MAX / param1;
				for(x = 0; x < arraylen; x++) {
					if (data[x] > ovtmp1) {return ARR_ERR_OVFL;}
					dataout[x] = data[x] * param1; 
				}
			}
		}
		return ARR_NO_ERR;
	}
	// af_pow
	case OP_AF_POW: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_long_long(data[x], param1, &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_long_long(data[x], param1, &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_pow_r
	case OP_AF_POW_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_long_long(param1, data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = arith_pow_unsigned_long_long(param1, data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// af_sub
	case OP_AF_SUB: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1;
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (data[x] < param1) {return ARR_ERR_OVFL;}
				dataout[x] = data[x] - param1; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				if (param1 < data[x]) {return ARR_ERR_OVFL;}
				dataout[x] = param1 - data[x]; 
			}
		}
		return ARR_NO_ERR;
	}
	// af_and
	case OP_AF_AND: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] & param1;
		}
		return ARR_NO_ERR; 
	}
	// af_or
	case OP_AF_OR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] | param1;
		}
		return ARR_NO_ERR; 
	}
	// af_xor
	case OP_AF_XOR: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] ^ param1;
		}
		return ARR_NO_ERR; 
	}
	// af_invert
	case OP_AF_INVERT: { 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = ~data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_eq
	case OP_AF_EQ: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] == param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gt
	case OP_AF_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1;
		}
		return ARR_NO_ERR; 
	}
	// af_gte
	case OP_AF_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lt
	case OP_AF_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lte
	case OP_AF_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1;
		}
		return ARR_NO_ERR; 
	}
	// af_ne
	case OP_AF_NE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] != param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift
	case OP_AF_LSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] << param1;
		}
		return ARR_NO_ERR; 
	}
	// af_lshift_r
	case OP_AF_LSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 << data[x];
		}
		return ARR_NO_ERR; 
	}
	// af_rshift
	case OP_AF_RSHIFT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >> param1;
		}
		return ARR_NO_ERR; 
	}
	// af_rshift_r
	case OP_AF_RSHIFT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = param1 >> data[x];
		}
		return ARR_NO_ERR; 
	}
	// math_factorial
	case OP_MATH_FACTORIAL: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_unsigned_long_long(data[x], &errflag);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = factorial_unsigned_long_long(data[x], &errflag);
				if (errflag != 0) return ARR_ERR_OVFL;
			}
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1 ? param1 : data[x];
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
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   paramcount = The number of valid parameters (normally 0 or 1).
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int map_float(signed int opcode, Py_ssize_t arraylen, float *data, float *dataout, float param1, unsigned int paramcount, unsigned int disableovfl) {

	// array index counter.
	Py_ssize_t x;


	int paramtmp;	// Used for temporary type conversion calculations.


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + param1;
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + param1;
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_div
	case OP_AF_DIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] / param1;
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] / param1;
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_div_r
	case OP_AF_DIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 / data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 / data[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floorf(data[x] / param1);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floorf(data[x] / param1);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floorf(param1 / data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floorf(param1 / data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_mod
	case OP_AF_MOD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1 * floorf(data[x] / param1);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1 * floorf(data[x] / param1);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x] * floorf(param1 / data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x] * floorf(param1 / data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_mult
	case OP_AF_MULT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * param1;
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * param1;
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_neg
	case OP_AF_NEG: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_pow
	case OP_AF_POW: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = powf(data[x], param1);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = powf(data[x], param1);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_pow_r
	case OP_AF_POW_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = powf(param1, data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = powf(param1, data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_sub
	case OP_AF_SUB: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1;
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1;
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_eq
	case OP_AF_EQ: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (float) (data[x] == param1);
		}
		return ARR_NO_ERR;
	}
	// af_gt
	case OP_AF_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (float) (data[x] > param1);
		}
		return ARR_NO_ERR;
	}
	// af_gte
	case OP_AF_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (float) (data[x] >= param1);
		}
		return ARR_NO_ERR;
	}
	// af_lt
	case OP_AF_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (float) (data[x] < param1);
		}
		return ARR_NO_ERR;
	}
	// af_lte
	case OP_AF_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (float) (data[x] <= param1);
		}
		return ARR_NO_ERR;
	}
	// af_ne
	case OP_AF_NE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (float) (data[x] != param1);
		}
		return ARR_NO_ERR;
	}
	// af_abs
	case OP_AF_ABS: { 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= 0.0 ? data[x] : -data[x];
		}
		return ARR_NO_ERR; 
	}
	// math_acos
	case OP_MATH_ACOS: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = acosf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = acosf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_acosh
	case OP_MATH_ACOSH: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = acoshf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = acoshf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_asin
	case OP_MATH_ASIN: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = asinf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = asinf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_asinh
	case OP_MATH_ASINH: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = asinhf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = asinhf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_atan
	case OP_MATH_ATAN: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atanf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atanf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_atan2
	case OP_MATH_ATAN2: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atan2f(data[x], param1);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atan2f(data[x], param1);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_atan2_r
	case OP_MATH_ATAN2_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atan2f(param1, data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atan2f(param1, data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_atanh
	case OP_MATH_ATANH: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atanhf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atanhf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_ceil
	case OP_MATH_CEIL: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = ceilf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = ceilf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_copysign
	case OP_MATH_COPYSIGN: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = copysignf(data[x], param1);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = copysignf(data[x], param1);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_cos
	case OP_MATH_COS: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = cosf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = cosf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_cosh
	case OP_MATH_COSH: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = coshf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = coshf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_degrees
	case OP_MATH_DEGREES: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = radtodeg_f * data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = radtodeg_f * data[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_erf
	case OP_MATH_ERF: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = erff(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = erff(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_erfc
	case OP_MATH_ERFC: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = erfcf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = erfcf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_exp
	case OP_MATH_EXP: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = expf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = expf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_expm1
	case OP_MATH_EXPM1: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = expm1f(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = expm1f(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_fabs
	case OP_MATH_FABS: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fabsf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fabsf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_floor
	case OP_MATH_FLOOR: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floorf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floorf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_fmod
	case OP_MATH_FMOD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fmodf(data[x], param1);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fmodf(data[x], param1);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_fmod_r
	case OP_MATH_FMOD_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fmodf(param1, data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fmodf(param1, data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_gamma
	case OP_MATH_GAMMA: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = tgammaf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = tgammaf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_hypot
	case OP_MATH_HYPOT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = hypotf(data[x], param1);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = hypotf(data[x], param1);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_hypot_r
	case OP_MATH_HYPOT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = hypotf(param1, data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = hypotf(param1, data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_isinf
	case OP_MATH_ISINF: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		for(x = 0; x < arraylen; x++) {
			dataout[x] = (float) !(isfinite(data[x]) || isnan(data[x]));
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_isnan
	case OP_MATH_ISNAN: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		for(x = 0; x < arraylen; x++) {
			dataout[x] = (float) isnan(data[x]);
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_ldexp
	case OP_MATH_LDEXP: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		if ((param1 > INT_MAX) || (param1 < INT_MIN)) {
			return ARR_ERR_OVFL;
		}
		paramtmp = (int) param1;
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = ldexpf(data[x], paramtmp);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = ldexpf(data[x], paramtmp);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_lgamma
	case OP_MATH_LGAMMA: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = lgammaf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = lgammaf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_log
	case OP_MATH_LOG: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = logf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = logf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_log10
	case OP_MATH_LOG10: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = log10f(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = log10f(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_log1p
	case OP_MATH_LOG1P: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = log1pf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = log1pf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_pow
	case OP_MATH_POW: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = powf(data[x], param1);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = powf(data[x], param1);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_pow_r
	case OP_MATH_POW_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = powf(param1, data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = powf(param1, data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_radians
	case OP_MATH_RADIANS: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = degtorad_f * data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = degtorad_f * data[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_sin
	case OP_MATH_SIN: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = sinf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = sinf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_sinh
	case OP_MATH_SINH: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = sinhf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = sinhf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_sqrt
	case OP_MATH_SQRT: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = sqrtf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = sqrtf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_tan
	case OP_MATH_TAN: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = tanf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = tanf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_tanh
	case OP_MATH_TANH: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = tanhf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = tanhf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_trunc
	case OP_MATH_TRUNC: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = truncf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = truncf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1 ? param1 : data[x];
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
   dataout = The output data array.
   param1 = The parameter to be applied to each array element.
   paramcount = The number of valid parameters (normally 0 or 1).
   disableovfl = If true, disable arithmetic overflow checking (default is false).
*/
signed int map_double(signed int opcode, Py_ssize_t arraylen, double *data, double *dataout, double param1, unsigned int paramcount, unsigned int disableovfl) {

	// array index counter.
	Py_ssize_t x;


	int paramtmp;	// Used for temporary type conversion calculations.


	switch(opcode) {

	// af_add
	case OP_AF_ADD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + param1;
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] + param1;
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_div
	case OP_AF_DIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] / param1;
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] / param1;
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_div_r
	case OP_AF_DIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 / data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 / data[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_floordiv
	case OP_AF_FLOORDIV: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floor(data[x] / param1);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floor(data[x] / param1);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_floordiv_r
	case OP_AF_FLOORDIV_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floor(param1 / data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floor(param1 / data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_mod
	case OP_AF_MOD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1 * floor(data[x] / param1);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1 * floor(data[x] / param1);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_mod_r
	case OP_AF_MOD_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x] * floor(param1 / data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x] * floor(param1 / data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_mult
	case OP_AF_MULT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * param1;
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] * param1;
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_neg
	case OP_AF_NEG: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = -data[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_pow
	case OP_AF_POW: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = pow(data[x], param1);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = pow(data[x], param1);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_pow_r
	case OP_AF_POW_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = pow(param1, data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = pow(param1, data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_sub
	case OP_AF_SUB: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1;
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = data[x] - param1;
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_sub_r
	case OP_AF_SUB_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = param1 - data[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// af_eq
	case OP_AF_EQ: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (double) (data[x] == param1);
		}
		return ARR_NO_ERR;
	}
	// af_gt
	case OP_AF_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (double) (data[x] > param1);
		}
		return ARR_NO_ERR;
	}
	// af_gte
	case OP_AF_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (double) (data[x] >= param1);
		}
		return ARR_NO_ERR;
	}
	// af_lt
	case OP_AF_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (double) (data[x] < param1);
		}
		return ARR_NO_ERR;
	}
	// af_lte
	case OP_AF_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (double) (data[x] <= param1);
		}
		return ARR_NO_ERR;
	}
	// af_ne
	case OP_AF_NE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		for(x = 0; x < arraylen; x++) {
			dataout[x] = (double) (data[x] != param1);
		}
		return ARR_NO_ERR;
	}
	// af_abs
	case OP_AF_ABS: { 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= 0.0 ? data[x] : -data[x];
		}
		return ARR_NO_ERR; 
	}
	// math_acos
	case OP_MATH_ACOS: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = acos(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = acos(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_acosh
	case OP_MATH_ACOSH: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = acosh(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = acosh(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_asin
	case OP_MATH_ASIN: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = asin(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = asin(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_asinh
	case OP_MATH_ASINH: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = asinh(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = asinh(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_atan
	case OP_MATH_ATAN: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atan(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atan(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_atan2
	case OP_MATH_ATAN2: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atan2(data[x], param1);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atan2(data[x], param1);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_atan2_r
	case OP_MATH_ATAN2_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atan2(param1, data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atan2(param1, data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_atanh
	case OP_MATH_ATANH: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atanh(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = atanh(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_ceil
	case OP_MATH_CEIL: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = ceil(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = ceil(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_copysign
	case OP_MATH_COPYSIGN: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = copysign(data[x], param1);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = copysign(data[x], param1);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_cos
	case OP_MATH_COS: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = cos(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = cos(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_cosh
	case OP_MATH_COSH: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = cosh(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = cosh(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_degrees
	case OP_MATH_DEGREES: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = radtodeg_d * data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = radtodeg_d * data[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_erf
	case OP_MATH_ERF: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = erf(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = erf(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_erfc
	case OP_MATH_ERFC: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = erfc(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = erfc(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_exp
	case OP_MATH_EXP: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = exp(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = exp(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_expm1
	case OP_MATH_EXPM1: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = expm1(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = expm1(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_fabs
	case OP_MATH_FABS: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fabs(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fabs(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_floor
	case OP_MATH_FLOOR: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floor(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = floor(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_fmod
	case OP_MATH_FMOD: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fmod(data[x], param1);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fmod(data[x], param1);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_fmod_r
	case OP_MATH_FMOD_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fmod(param1, data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = fmod(param1, data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_gamma
	case OP_MATH_GAMMA: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = tgamma(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = tgamma(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_hypot
	case OP_MATH_HYPOT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = hypot(data[x], param1);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = hypot(data[x], param1);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_hypot_r
	case OP_MATH_HYPOT_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = hypot(param1, data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = hypot(param1, data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_isinf
	case OP_MATH_ISINF: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		for(x = 0; x < arraylen; x++) {
			dataout[x] = (double) !(isfinite(data[x]) || isnan(data[x]));
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_isnan
	case OP_MATH_ISNAN: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		for(x = 0; x < arraylen; x++) {
			dataout[x] = (double) isnan(data[x]);
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_ldexp
	case OP_MATH_LDEXP: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;}
		if ((param1 > INT_MAX) || (param1 < INT_MIN)) {
			return ARR_ERR_OVFL;
		}
		paramtmp = (int) param1;
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = ldexp(data[x], paramtmp);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = ldexp(data[x], paramtmp);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR;
	}
	// math_lgamma
	case OP_MATH_LGAMMA: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = lgamma(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = lgamma(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_log
	case OP_MATH_LOG: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = log(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = log(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_log10
	case OP_MATH_LOG10: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = log10(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = log10(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_log1p
	case OP_MATH_LOG1P: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = log1p(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = log1p(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// math_pow
	case OP_MATH_POW: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = pow(data[x], param1);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = pow(data[x], param1);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_pow_r
	case OP_MATH_POW_R: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = pow(param1, data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = pow(param1, data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_radians
	case OP_MATH_RADIANS: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = degtorad_d * data[x];
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = degtorad_d * data[x];
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_sin
	case OP_MATH_SIN: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = sin(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = sin(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_sinh
	case OP_MATH_SINH: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = sinh(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = sinh(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_sqrt
	case OP_MATH_SQRT: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = sqrt(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = sqrt(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_tan
	case OP_MATH_TAN: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = tan(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = tan(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_tanh
	case OP_MATH_TANH: { 
		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = tanh(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = tanh(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
	}
	// math_trunc
	case OP_MATH_TRUNC: { 
		// This op is not supported by MSVC 2010.
		#ifdef _MSC_VER
			return ARR_ERR_PLATFORM;
		#else

		// Overflow checking disabled.
		if (disableovfl) {
			for(x = 0; x < arraylen; x++) {
				dataout[x] = trunc(data[x]);
			}
		} else {
		// Overflow checking enabled.
			for(x = 0; x < arraylen; x++) {
				dataout[x] = trunc(data[x]);
				if (!isfinite(dataout[x])) {return ARR_ERR_ARITHMETIC;}
			}
		}
		return ARR_NO_ERR; 
		#endif

	}
	// aops_subst_gt
	case OP_AOPS_SUBST_GT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] > param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_gte
	case OP_AOPS_SUBST_GTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] >= param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lt
	case OP_AOPS_SUBST_LT: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] < param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}
	// aops_subst_lte
	case OP_AOPS_SUBST_LTE: {
		if (paramcount < 1) {return ARR_ERR_PARAMMISSING;} 
		for(x = 0; x < arraylen; x++) {
			dataout[x] = data[x] <= param1 ? param1 : data[x];
		}
		return ARR_NO_ERR; 
	}

	}
	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;
}
/*--------------------------------------------------------------------------- */

