//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   acalc_common.h
// Purpose:  Common code for acalc.
// Language: C
// Date:     22-Jan-2016.
//
//------------------------------------------------------------------------------
//
//   Copyright 2016    Michael Griffin    <m12.griffin@gmail.com>
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

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */

// No error
#define CALC_NO_ERR 0
// The operation requested is not valid for this function.
#define CALC_ERR_INVALIDOP -1
// An arithmetic overflow occurred during a calculation. 
#define CALC_ERR_OVFL -2
// Floating point error of any kind.
#define CALC_ERR_ARITHMETIC -3
// Interpreter stack overflow or underflow.
#define CALC_ERR_STACKOVFL_ERR -4
// Uknown interpreter op code.
#define CALC_ERR_UNKNOWNOP -5
// The operation requested is not valid for this platform.
#define CALC_ERR_PLATFORM -7


/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// ACalc interpreter stack overflow or underflow.
void ErrMsgACalcStackOverflow(void);

// ACalc interpreter uknown op code.
void ErrMsgACalcUnknownOpCode(void);

// ACalc interpreter variable offset array overflow or underflow.
void ErrMsgACalcVarOffsetOverflow(void);

// The operator is invalid for this array type.
void ErrMsgACalcInvalidOpTypeArray(void);

/*--------------------------------------------------------------------------- */

signed int exequation_signed_char(Py_ssize_t arraylen, signed char *data, signed char *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, signed char *vararray, signed char *constarray,
			signed char *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl);

signed int exequation_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, unsigned char *vararray, unsigned char *constarray,
			unsigned char *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl);

signed int exequation_signed_short(Py_ssize_t arraylen, signed short *data, signed short *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, signed short *vararray, signed short *constarray,
			signed short *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl);

signed int exequation_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, unsigned short *vararray, unsigned short *constarray,
			unsigned short *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl);

signed int exequation_signed_int(Py_ssize_t arraylen, signed int *data, signed int *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, signed int *vararray, signed int *constarray,
			signed int *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl);

signed int exequation_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, unsigned int *vararray, unsigned int *constarray,
			unsigned int *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl);

signed int exequation_signed_long(Py_ssize_t arraylen, signed long *data, signed long *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, signed long *vararray, signed long *constarray,
			signed long *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl);

signed int exequation_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, unsigned long *vararray, unsigned long *constarray,
			unsigned long *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl);

signed int exequation_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, signed long long *vararray, signed long long *constarray,
			signed long long *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl);

signed int exequation_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, unsigned long long *vararray, unsigned long long *constarray,
			unsigned long long *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl);

signed int exequation_float(Py_ssize_t arraylen, float *data, float *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, float *vararray, float *constarray,
			float *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl);

signed int exequation_double(Py_ssize_t arraylen, double *data, double *dataout, 
			unsigned int codearraylen, unsigned int *codearray, 
			unsigned int *varoffsetsarray, double *vararray, double *constarray,
			double *vmstack, unsigned int vmstacksize, unsigned int vmstacksegments, unsigned int disableovfl);


/*--------------------------------------------------------------------------- */
