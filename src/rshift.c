//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   rshift.c
// Purpose:  Calculate the rshift of values in an array.
// Language: C
// Date:     15-Nov-2017.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2021    Michael Griffin    <m12.griffin@gmail.com>
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

#include "arrayparams_two.h"


#include "simddefs.h"

#ifdef AF_HASSIMD_X86
#include "rshift_simd_x86.h"
#endif

#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
#include "arm_neon.h"
#endif

#if defined(AF_HASSIMD_ARMv7_32BIT)
#include "rshift_simd_armv7.h"
#endif

#if defined(AF_HASSIMD_ARM_AARCH64)
#include "rshift_simd_armv8.h"
#endif

/*--------------------------------------------------------------------------- */

// Function specific macros and other definitions.
#include "rshift_defs.h"

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD acceleration.
*/
// param_arr_num_none
void rshift_signed_char_1(Py_ssize_t arraylen, int nosimd, signed char *data1, signed char param) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, CHARSIMDSIZE)) {
		rshift_signed_char_1_simd(arraylen, data1, param);
		return;
	}
#endif

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> param;
	}


}

// param_arr_num_arr
void rshift_signed_char_2(Py_ssize_t arraylen, int nosimd, signed char *data1, signed char param, signed char *data3) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, CHARSIMDSIZE)) {
		rshift_signed_char_2_simd(arraylen, data1, param, data3);
		return;
	}
#endif

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> param;
	}

}

// param_num_arr_none
void rshift_signed_char_3(Py_ssize_t arraylen, int nosimd, signed char param, signed char *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data2[x] = param >> data2[x];
	}

}

// param_num_arr_arr
void rshift_signed_char_4(Py_ssize_t arraylen, int nosimd, signed char param, signed char *data2, signed char *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = param >> data2[x];
	}

}



// param_arr_arr_none
void rshift_signed_char_5(Py_ssize_t arraylen, int nosimd, signed char *data1, signed char *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> data2[x];
	}

}

// param_arr_arr_arr
void rshift_signed_char_6(Py_ssize_t arraylen, int nosimd, signed char *data1, signed char *data2, signed char *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> data2[x];
	}

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD acceleration.
*/
// param_arr_num_none
void rshift_unsigned_char_1(Py_ssize_t arraylen, int nosimd, unsigned char *data1, unsigned char param) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, CHARSIMDSIZE)) {
		rshift_unsigned_char_1_simd(arraylen, data1, param);
		return;
	}
#endif

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> param;
	}


}

// param_arr_num_arr
void rshift_unsigned_char_2(Py_ssize_t arraylen, int nosimd, unsigned char *data1, unsigned char param, unsigned char *data3) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, CHARSIMDSIZE)) {
		rshift_unsigned_char_2_simd(arraylen, data1, param, data3);
		return;
	}
#endif

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> param;
	}

}

// param_num_arr_none
void rshift_unsigned_char_3(Py_ssize_t arraylen, int nosimd, unsigned char param, unsigned char *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data2[x] = param >> data2[x];
	}

}

// param_num_arr_arr
void rshift_unsigned_char_4(Py_ssize_t arraylen, int nosimd, unsigned char param, unsigned char *data2, unsigned char *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = param >> data2[x];
	}

}



// param_arr_arr_none
void rshift_unsigned_char_5(Py_ssize_t arraylen, int nosimd, unsigned char *data1, unsigned char *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> data2[x];
	}

}

// param_arr_arr_arr
void rshift_unsigned_char_6(Py_ssize_t arraylen, int nosimd, unsigned char *data1, unsigned char *data2, unsigned char *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> data2[x];
	}

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD acceleration.
*/
// param_arr_num_none
void rshift_signed_short_1(Py_ssize_t arraylen, int nosimd, signed short *data1, signed short param) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, SHORTSIMDSIZE)) {
		rshift_signed_short_1_simd(arraylen, data1, param);
		return;
	}
#endif

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> param;
	}


}

// param_arr_num_arr
void rshift_signed_short_2(Py_ssize_t arraylen, int nosimd, signed short *data1, signed short param, signed short *data3) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, SHORTSIMDSIZE)) {
		rshift_signed_short_2_simd(arraylen, data1, param, data3);
		return;
	}
#endif

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> param;
	}

}

// param_num_arr_none
void rshift_signed_short_3(Py_ssize_t arraylen, int nosimd, signed short param, signed short *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data2[x] = param >> data2[x];
	}

}

// param_num_arr_arr
void rshift_signed_short_4(Py_ssize_t arraylen, int nosimd, signed short param, signed short *data2, signed short *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = param >> data2[x];
	}

}



// param_arr_arr_none
void rshift_signed_short_5(Py_ssize_t arraylen, int nosimd, signed short *data1, signed short *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> data2[x];
	}

}

// param_arr_arr_arr
void rshift_signed_short_6(Py_ssize_t arraylen, int nosimd, signed short *data1, signed short *data2, signed short *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> data2[x];
	}

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD acceleration.
*/
// param_arr_num_none
void rshift_unsigned_short_1(Py_ssize_t arraylen, int nosimd, unsigned short *data1, unsigned short param) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, SHORTSIMDSIZE)) {
		rshift_unsigned_short_1_simd(arraylen, data1, param);
		return;
	}
#endif

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> param;
	}


}

// param_arr_num_arr
void rshift_unsigned_short_2(Py_ssize_t arraylen, int nosimd, unsigned short *data1, unsigned short param, unsigned short *data3) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, SHORTSIMDSIZE)) {
		rshift_unsigned_short_2_simd(arraylen, data1, param, data3);
		return;
	}
#endif

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> param;
	}

}

// param_num_arr_none
void rshift_unsigned_short_3(Py_ssize_t arraylen, int nosimd, unsigned short param, unsigned short *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data2[x] = param >> data2[x];
	}

}

// param_num_arr_arr
void rshift_unsigned_short_4(Py_ssize_t arraylen, int nosimd, unsigned short param, unsigned short *data2, unsigned short *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = param >> data2[x];
	}

}



// param_arr_arr_none
void rshift_unsigned_short_5(Py_ssize_t arraylen, int nosimd, unsigned short *data1, unsigned short *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> data2[x];
	}

}

// param_arr_arr_arr
void rshift_unsigned_short_6(Py_ssize_t arraylen, int nosimd, unsigned short *data1, unsigned short *data2, unsigned short *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> data2[x];
	}

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD acceleration.
*/
// param_arr_num_none
void rshift_signed_int_1(Py_ssize_t arraylen, int nosimd, signed int *data1, signed int param) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, INTSIMDSIZE)) {
		rshift_signed_int_1_simd(arraylen, data1, param);
		return;
	}
#endif

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> param;
	}


}

// param_arr_num_arr
void rshift_signed_int_2(Py_ssize_t arraylen, int nosimd, signed int *data1, signed int param, signed int *data3) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, INTSIMDSIZE)) {
		rshift_signed_int_2_simd(arraylen, data1, param, data3);
		return;
	}
#endif

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> param;
	}

}

// param_num_arr_none
void rshift_signed_int_3(Py_ssize_t arraylen, int nosimd, signed int param, signed int *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data2[x] = param >> data2[x];
	}

}

// param_num_arr_arr
void rshift_signed_int_4(Py_ssize_t arraylen, int nosimd, signed int param, signed int *data2, signed int *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = param >> data2[x];
	}

}



// param_arr_arr_none
void rshift_signed_int_5(Py_ssize_t arraylen, int nosimd, signed int *data1, signed int *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> data2[x];
	}

}

// param_arr_arr_arr
void rshift_signed_int_6(Py_ssize_t arraylen, int nosimd, signed int *data1, signed int *data2, signed int *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> data2[x];
	}

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD acceleration.
*/
// param_arr_num_none
void rshift_unsigned_int_1(Py_ssize_t arraylen, int nosimd, unsigned int *data1, unsigned int param) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, INTSIMDSIZE)) {
		rshift_unsigned_int_1_simd(arraylen, data1, param);
		return;
	}
#endif

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> param;
	}


}

// param_arr_num_arr
void rshift_unsigned_int_2(Py_ssize_t arraylen, int nosimd, unsigned int *data1, unsigned int param, unsigned int *data3) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && enoughforsimd(arraylen, INTSIMDSIZE)) {
		rshift_unsigned_int_2_simd(arraylen, data1, param, data3);
		return;
	}
#endif

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> param;
	}

}

// param_num_arr_none
void rshift_unsigned_int_3(Py_ssize_t arraylen, int nosimd, unsigned int param, unsigned int *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data2[x] = param >> data2[x];
	}

}

// param_num_arr_arr
void rshift_unsigned_int_4(Py_ssize_t arraylen, int nosimd, unsigned int param, unsigned int *data2, unsigned int *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = param >> data2[x];
	}

}



// param_arr_arr_none
void rshift_unsigned_int_5(Py_ssize_t arraylen, int nosimd, unsigned int *data1, unsigned int *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> data2[x];
	}

}

// param_arr_arr_arr
void rshift_unsigned_int_6(Py_ssize_t arraylen, int nosimd, unsigned int *data1, unsigned int *data2, unsigned int *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> data2[x];
	}

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD acceleration.
*/
// param_arr_num_none
void rshift_signed_long_1(Py_ssize_t arraylen, int nosimd, signed long *data1, signed long param) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> param;
	}


}

// param_arr_num_arr
void rshift_signed_long_2(Py_ssize_t arraylen, int nosimd, signed long *data1, signed long param, signed long *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> param;
	}

}

// param_num_arr_none
void rshift_signed_long_3(Py_ssize_t arraylen, int nosimd, signed long param, signed long *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data2[x] = param >> data2[x];
	}

}

// param_num_arr_arr
void rshift_signed_long_4(Py_ssize_t arraylen, int nosimd, signed long param, signed long *data2, signed long *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = param >> data2[x];
	}

}



// param_arr_arr_none
void rshift_signed_long_5(Py_ssize_t arraylen, int nosimd, signed long *data1, signed long *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> data2[x];
	}

}

// param_arr_arr_arr
void rshift_signed_long_6(Py_ssize_t arraylen, int nosimd, signed long *data1, signed long *data2, signed long *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> data2[x];
	}

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD acceleration.
*/
// param_arr_num_none
void rshift_unsigned_long_1(Py_ssize_t arraylen, int nosimd, unsigned long *data1, unsigned long param) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> param;
	}


}

// param_arr_num_arr
void rshift_unsigned_long_2(Py_ssize_t arraylen, int nosimd, unsigned long *data1, unsigned long param, unsigned long *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> param;
	}

}

// param_num_arr_none
void rshift_unsigned_long_3(Py_ssize_t arraylen, int nosimd, unsigned long param, unsigned long *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data2[x] = param >> data2[x];
	}

}

// param_num_arr_arr
void rshift_unsigned_long_4(Py_ssize_t arraylen, int nosimd, unsigned long param, unsigned long *data2, unsigned long *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = param >> data2[x];
	}

}



// param_arr_arr_none
void rshift_unsigned_long_5(Py_ssize_t arraylen, int nosimd, unsigned long *data1, unsigned long *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> data2[x];
	}

}

// param_arr_arr_arr
void rshift_unsigned_long_6(Py_ssize_t arraylen, int nosimd, unsigned long *data1, unsigned long *data2, unsigned long *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> data2[x];
	}

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD acceleration.
*/
// param_arr_num_none
void rshift_signed_long_long_1(Py_ssize_t arraylen, int nosimd, signed long long *data1, signed long long param) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> param;
	}


}

// param_arr_num_arr
void rshift_signed_long_long_2(Py_ssize_t arraylen, int nosimd, signed long long *data1, signed long long param, signed long long *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> param;
	}

}

// param_num_arr_none
void rshift_signed_long_long_3(Py_ssize_t arraylen, int nosimd, signed long long param, signed long long *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data2[x] = param >> data2[x];
	}

}

// param_num_arr_arr
void rshift_signed_long_long_4(Py_ssize_t arraylen, int nosimd, signed long long param, signed long long *data2, signed long long *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = param >> data2[x];
	}

}



// param_arr_arr_none
void rshift_signed_long_long_5(Py_ssize_t arraylen, int nosimd, signed long long *data1, signed long long *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> data2[x];
	}

}

// param_arr_arr_arr
void rshift_signed_long_long_6(Py_ssize_t arraylen, int nosimd, signed long long *data1, signed long long *data2, signed long long *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> data2[x];
	}

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   nosimd = If true, disable SIMD acceleration.
*/
// param_arr_num_none
void rshift_unsigned_long_long_1(Py_ssize_t arraylen, int nosimd, unsigned long long *data1, unsigned long long param) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> param;
	}


}

// param_arr_num_arr
void rshift_unsigned_long_long_2(Py_ssize_t arraylen, int nosimd, unsigned long long *data1, unsigned long long param, unsigned long long *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> param;
	}

}

// param_num_arr_none
void rshift_unsigned_long_long_3(Py_ssize_t arraylen, int nosimd, unsigned long long param, unsigned long long *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data2[x] = param >> data2[x];
	}

}

// param_num_arr_arr
void rshift_unsigned_long_long_4(Py_ssize_t arraylen, int nosimd, unsigned long long param, unsigned long long *data2, unsigned long long *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = param >> data2[x];
	}

}



// param_arr_arr_none
void rshift_unsigned_long_long_5(Py_ssize_t arraylen, int nosimd, unsigned long long *data1, unsigned long long *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] >> data2[x];
	}

}

// param_arr_arr_arr
void rshift_unsigned_long_long_6(Py_ssize_t arraylen, int nosimd, unsigned long long *data1, unsigned long long *data2, unsigned long long *data3) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] >> data2[x];
	}

}

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_rshift(PyObject *self, PyObject *args, PyObject *keywds) {


	// This is used to hold the parsed parameters.
	struct args_params_2 arraydata = ARGSINIT_TWO;


	// -----------------------------------------------------


	// Get the parameters passed from Python. Does not have "matherrors". 
	// Some functions using this template do have "nosimd".
	arraydata = getparams_two(self, args, keywds, 0, 1, "rshift");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}

	// Call the C function.
	switch(arraydata.arraytype) {

		// signed_char
		case 'b' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					rshift_signed_char_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.b, arraydata.param.b);
					break;
				}
				case param_arr_num_arr : {
					rshift_signed_char_2(arraydata.arraylength, arraydata.nosimd, arraydata.array1.b, arraydata.param.b, arraydata.array3.b);
					break;
				}
				case param_num_arr_none : {
					rshift_signed_char_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.b, arraydata.array2.b);
					break;
				}
				case param_num_arr_arr : {
					rshift_signed_char_4(arraydata.arraylength, arraydata.nosimd, arraydata.param.b, arraydata.array2.b, arraydata.array3.b);
					break;
				}
				case param_arr_arr_none : {
					rshift_signed_char_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.b, arraydata.array2.b);
					break;
				}
				case param_arr_arr_arr : {
					rshift_signed_char_6(arraydata.arraylength, arraydata.nosimd, arraydata.array1.b, arraydata.array2.b, arraydata.array3.b);
					break;
				}
			}
			break;
		}

		// unsigned_char
		case 'B' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					rshift_unsigned_char_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.B, arraydata.param.B);
					break;
				}
				case param_arr_num_arr : {
					rshift_unsigned_char_2(arraydata.arraylength, arraydata.nosimd, arraydata.array1.B, arraydata.param.B, arraydata.array3.B);
					break;
				}
				case param_num_arr_none : {
					rshift_unsigned_char_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.B, arraydata.array2.B);
					break;
				}
				case param_num_arr_arr : {
					rshift_unsigned_char_4(arraydata.arraylength, arraydata.nosimd, arraydata.param.B, arraydata.array2.B, arraydata.array3.B);
					break;
				}
				case param_arr_arr_none : {
					rshift_unsigned_char_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.B, arraydata.array2.B);
					break;
				}
				case param_arr_arr_arr : {
					rshift_unsigned_char_6(arraydata.arraylength, arraydata.nosimd, arraydata.array1.B, arraydata.array2.B, arraydata.array3.B);
					break;
				}
			}
			break;
		}

		// signed_short
		case 'h' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					rshift_signed_short_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.h, arraydata.param.h);
					break;
				}
				case param_arr_num_arr : {
					rshift_signed_short_2(arraydata.arraylength, arraydata.nosimd, arraydata.array1.h, arraydata.param.h, arraydata.array3.h);
					break;
				}
				case param_num_arr_none : {
					rshift_signed_short_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.h, arraydata.array2.h);
					break;
				}
				case param_num_arr_arr : {
					rshift_signed_short_4(arraydata.arraylength, arraydata.nosimd, arraydata.param.h, arraydata.array2.h, arraydata.array3.h);
					break;
				}
				case param_arr_arr_none : {
					rshift_signed_short_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.h, arraydata.array2.h);
					break;
				}
				case param_arr_arr_arr : {
					rshift_signed_short_6(arraydata.arraylength, arraydata.nosimd, arraydata.array1.h, arraydata.array2.h, arraydata.array3.h);
					break;
				}
			}
			break;
		}

		// unsigned_short
		case 'H' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					rshift_unsigned_short_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.H, arraydata.param.H);
					break;
				}
				case param_arr_num_arr : {
					rshift_unsigned_short_2(arraydata.arraylength, arraydata.nosimd, arraydata.array1.H, arraydata.param.H, arraydata.array3.H);
					break;
				}
				case param_num_arr_none : {
					rshift_unsigned_short_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.H, arraydata.array2.H);
					break;
				}
				case param_num_arr_arr : {
					rshift_unsigned_short_4(arraydata.arraylength, arraydata.nosimd, arraydata.param.H, arraydata.array2.H, arraydata.array3.H);
					break;
				}
				case param_arr_arr_none : {
					rshift_unsigned_short_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.H, arraydata.array2.H);
					break;
				}
				case param_arr_arr_arr : {
					rshift_unsigned_short_6(arraydata.arraylength, arraydata.nosimd, arraydata.array1.H, arraydata.array2.H, arraydata.array3.H);
					break;
				}
			}
			break;
		}

		// signed_int
		case 'i' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					rshift_signed_int_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.i, arraydata.param.i);
					break;
				}
				case param_arr_num_arr : {
					rshift_signed_int_2(arraydata.arraylength, arraydata.nosimd, arraydata.array1.i, arraydata.param.i, arraydata.array3.i);
					break;
				}
				case param_num_arr_none : {
					rshift_signed_int_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.i, arraydata.array2.i);
					break;
				}
				case param_num_arr_arr : {
					rshift_signed_int_4(arraydata.arraylength, arraydata.nosimd, arraydata.param.i, arraydata.array2.i, arraydata.array3.i);
					break;
				}
				case param_arr_arr_none : {
					rshift_signed_int_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.i, arraydata.array2.i);
					break;
				}
				case param_arr_arr_arr : {
					rshift_signed_int_6(arraydata.arraylength, arraydata.nosimd, arraydata.array1.i, arraydata.array2.i, arraydata.array3.i);
					break;
				}
			}
			break;
		}

		// unsigned_int
		case 'I' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					rshift_unsigned_int_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.I, arraydata.param.I);
					break;
				}
				case param_arr_num_arr : {
					rshift_unsigned_int_2(arraydata.arraylength, arraydata.nosimd, arraydata.array1.I, arraydata.param.I, arraydata.array3.I);
					break;
				}
				case param_num_arr_none : {
					rshift_unsigned_int_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.I, arraydata.array2.I);
					break;
				}
				case param_num_arr_arr : {
					rshift_unsigned_int_4(arraydata.arraylength, arraydata.nosimd, arraydata.param.I, arraydata.array2.I, arraydata.array3.I);
					break;
				}
				case param_arr_arr_none : {
					rshift_unsigned_int_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.I, arraydata.array2.I);
					break;
				}
				case param_arr_arr_arr : {
					rshift_unsigned_int_6(arraydata.arraylength, arraydata.nosimd, arraydata.array1.I, arraydata.array2.I, arraydata.array3.I);
					break;
				}
			}
			break;
		}

		// signed_long
		case 'l' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					rshift_signed_long_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.l, arraydata.param.l);
					break;
				}
				case param_arr_num_arr : {
					rshift_signed_long_2(arraydata.arraylength, arraydata.nosimd, arraydata.array1.l, arraydata.param.l, arraydata.array3.l);
					break;
				}
				case param_num_arr_none : {
					rshift_signed_long_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.l, arraydata.array2.l);
					break;
				}
				case param_num_arr_arr : {
					rshift_signed_long_4(arraydata.arraylength, arraydata.nosimd, arraydata.param.l, arraydata.array2.l, arraydata.array3.l);
					break;
				}
				case param_arr_arr_none : {
					rshift_signed_long_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.l, arraydata.array2.l);
					break;
				}
				case param_arr_arr_arr : {
					rshift_signed_long_6(arraydata.arraylength, arraydata.nosimd, arraydata.array1.l, arraydata.array2.l, arraydata.array3.l);
					break;
				}
			}
			break;
		}

		// unsigned_long
		case 'L' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					rshift_unsigned_long_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.L, arraydata.param.L);
					break;
				}
				case param_arr_num_arr : {
					rshift_unsigned_long_2(arraydata.arraylength, arraydata.nosimd, arraydata.array1.L, arraydata.param.L, arraydata.array3.L);
					break;
				}
				case param_num_arr_none : {
					rshift_unsigned_long_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.L, arraydata.array2.L);
					break;
				}
				case param_num_arr_arr : {
					rshift_unsigned_long_4(arraydata.arraylength, arraydata.nosimd, arraydata.param.L, arraydata.array2.L, arraydata.array3.L);
					break;
				}
				case param_arr_arr_none : {
					rshift_unsigned_long_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.L, arraydata.array2.L);
					break;
				}
				case param_arr_arr_arr : {
					rshift_unsigned_long_6(arraydata.arraylength, arraydata.nosimd, arraydata.array1.L, arraydata.array2.L, arraydata.array3.L);
					break;
				}
			}
			break;
		}

		// signed_long_long
		case 'q' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					rshift_signed_long_long_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.q, arraydata.param.q);
					break;
				}
				case param_arr_num_arr : {
					rshift_signed_long_long_2(arraydata.arraylength, arraydata.nosimd, arraydata.array1.q, arraydata.param.q, arraydata.array3.q);
					break;
				}
				case param_num_arr_none : {
					rshift_signed_long_long_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.q, arraydata.array2.q);
					break;
				}
				case param_num_arr_arr : {
					rshift_signed_long_long_4(arraydata.arraylength, arraydata.nosimd, arraydata.param.q, arraydata.array2.q, arraydata.array3.q);
					break;
				}
				case param_arr_arr_none : {
					rshift_signed_long_long_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.q, arraydata.array2.q);
					break;
				}
				case param_arr_arr_arr : {
					rshift_signed_long_long_6(arraydata.arraylength, arraydata.nosimd, arraydata.array1.q, arraydata.array2.q, arraydata.array3.q);
					break;
				}
			}
			break;
		}

		// unsigned_long_long
		case 'Q' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					rshift_unsigned_long_long_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.Q, arraydata.param.Q);
					break;
				}
				case param_arr_num_arr : {
					rshift_unsigned_long_long_2(arraydata.arraylength, arraydata.nosimd, arraydata.array1.Q, arraydata.param.Q, arraydata.array3.Q);
					break;
				}
				case param_num_arr_none : {
					rshift_unsigned_long_long_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.Q, arraydata.array2.Q);
					break;
				}
				case param_num_arr_arr : {
					rshift_unsigned_long_long_4(arraydata.arraylength, arraydata.nosimd, arraydata.param.Q, arraydata.array2.Q, arraydata.array3.Q);
					break;
				}
				case param_arr_arr_none : {
					rshift_unsigned_long_long_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.Q, arraydata.array2.Q);
					break;
				}
				case param_arr_arr_arr : {
					rshift_unsigned_long_long_6(arraydata.arraylength, arraydata.nosimd, arraydata.array1.Q, arraydata.array2.Q, arraydata.array3.Q);
					break;
				}
			}
			break;
		}

		// Wrong array type code.
		default: {
			releasebuffers_two(arraydata);
			ErrMsgTypeExpectFloat();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_two(arraydata);


	// Everything was successful.
	Py_RETURN_NONE;

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(rshift__doc__,
"rshift \n\
_____________________________ \n\
\n\
Calculate rshift over the values in an array.  \n\
\n\
======================  ============================================== \n\
Equivalent to:          [x x >> y param for x in array1] \n\
or                      [param x >> y x for x in array1] \n\
or                      [x x >> y y for x,y in zip(array1, array2)] \n\
======================  ============================================== \n\
\n\
======================  ============================================== \n\
Array types supported:  b, B, h, H, i, I, l, L, q, Q \n\
Exceptions raised:       \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
  rshift(array1, param) \n\
  rshift(array1, param, outparray) \n\
  rshift(param, array1) \n\
  rshift(param, array1, outparray) \n\
  rshift(array1, array2) \n\
  rshift(array1, array2, outparray) \n\
  rshift(array1, param, maxlen=y) \n\
  rshift(array1, param, nosimd=False) \n\\n\
\n\
* array1 - The first input data array to be examined. If no output \n\
  array is provided the results will overwrite the input data.  \n\
* param - A non-array numeric parameter.  \n\
* array2 - A second input data array. Each element in this array is  \n\
  applied to the corresponding element in the first array.  \n\
* outparray - The output array. This parameter is optional.  \n\
* maxlen - Limit the length of the array used. This must be a valid  \n\
  positive integer. If a zero or negative length, or a value which is  \n\
  greater than the actual length of the array is specified, this  \n\
  parameter is ignored.  \n\
* nosimd - If True, SIMD acceleration is disabled. This parameter is \n\
  optional. The default is FALSE.  \n\
");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "rshift" is the name seen inside of Python. 
 "py_rshift" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef rshift_methods[] = {
	{"rshift",  (PyCFunction)py_rshift, METH_VARARGS | METH_KEYWORDS, rshift__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef rshiftmodule = {
    PyModuleDef_HEAD_INIT,
    "rshift",
    NULL,
    -1,
    rshift_methods
};

PyMODINIT_FUNC PyInit_rshift(void)
{
    return PyModule_Create(&rshiftmodule);
};

/*--------------------------------------------------------------------------- */

