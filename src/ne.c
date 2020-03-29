//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   ne.c
// Purpose:  Calculate the ne of values in an array.
// Language: C
// Date:     15-Nov-2017.
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

#include <limits.h>
#include <math.h>

#include "arrayerrs.h"

#include "arrayparams_base.h"

#include "arrayparams_comp.h"

#include "simddefs.h"

#ifdef AF_HASSIMD_X86
#include "ne_simd_x86.h"
#endif

#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
#include "arm_neon.h"
#endif

#if defined(AF_HASSIMD_ARMv7_32BIT)
#include "ne_simd_armv7.h"
#endif

#if defined(AF_HASSIMD_ARM_AARCH64)
#include "ne_simd_armv8.h"
#endif

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
char ne_signed_char_1(Py_ssize_t arraylen, int nosimd, signed char *data1, signed char param) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
		return ne_signed_char_1_simd(arraylen, data1, param);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != param)) { return 0; }
	}

	return 1;

}


// param_num_arr
char ne_signed_char_3(Py_ssize_t arraylen, int nosimd, signed char param, signed char *data2) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
		return ne_signed_char_3_simd(arraylen, param, data2);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(param != data2[x])) { return 0; }
	}

	return 1;

}


// param_arr_arr
char ne_signed_char_5(Py_ssize_t arraylen, int nosimd, signed char *data1, signed char *data2) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
		return ne_signed_char_5_simd(arraylen, data1, data2);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != data2[x])) { return 0; }
	}

	return 1;

}


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
char ne_unsigned_char_1(Py_ssize_t arraylen, int nosimd, unsigned char *data1, unsigned char param) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
		return ne_unsigned_char_1_simd(arraylen, data1, param);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != param)) { return 0; }
	}

	return 1;

}


// param_num_arr
char ne_unsigned_char_3(Py_ssize_t arraylen, int nosimd, unsigned char param, unsigned char *data2) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
		return ne_unsigned_char_3_simd(arraylen, param, data2);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(param != data2[x])) { return 0; }
	}

	return 1;

}


// param_arr_arr
char ne_unsigned_char_5(Py_ssize_t arraylen, int nosimd, unsigned char *data1, unsigned char *data2) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (CHARSIMDSIZE * 2))) {
		return ne_unsigned_char_5_simd(arraylen, data1, data2);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != data2[x])) { return 0; }
	}

	return 1;

}


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
char ne_signed_short_1(Py_ssize_t arraylen, int nosimd, signed short *data1, signed short param) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
		return ne_signed_short_1_simd(arraylen, data1, param);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != param)) { return 0; }
	}

	return 1;

}


// param_num_arr
char ne_signed_short_3(Py_ssize_t arraylen, int nosimd, signed short param, signed short *data2) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
		return ne_signed_short_3_simd(arraylen, param, data2);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(param != data2[x])) { return 0; }
	}

	return 1;

}


// param_arr_arr
char ne_signed_short_5(Py_ssize_t arraylen, int nosimd, signed short *data1, signed short *data2) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
		return ne_signed_short_5_simd(arraylen, data1, data2);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != data2[x])) { return 0; }
	}

	return 1;

}


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
char ne_unsigned_short_1(Py_ssize_t arraylen, int nosimd, unsigned short *data1, unsigned short param) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
		return ne_unsigned_short_1_simd(arraylen, data1, param);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != param)) { return 0; }
	}

	return 1;

}


// param_num_arr
char ne_unsigned_short_3(Py_ssize_t arraylen, int nosimd, unsigned short param, unsigned short *data2) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
		return ne_unsigned_short_3_simd(arraylen, param, data2);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(param != data2[x])) { return 0; }
	}

	return 1;

}


// param_arr_arr
char ne_unsigned_short_5(Py_ssize_t arraylen, int nosimd, unsigned short *data1, unsigned short *data2) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (SHORTSIMDSIZE * 2))) {
		return ne_unsigned_short_5_simd(arraylen, data1, data2);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != data2[x])) { return 0; }
	}

	return 1;

}


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
char ne_signed_int_1(Py_ssize_t arraylen, int nosimd, signed int *data1, signed int param) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
		return ne_signed_int_1_simd(arraylen, data1, param);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != param)) { return 0; }
	}

	return 1;

}


// param_num_arr
char ne_signed_int_3(Py_ssize_t arraylen, int nosimd, signed int param, signed int *data2) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
		return ne_signed_int_3_simd(arraylen, param, data2);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(param != data2[x])) { return 0; }
	}

	return 1;

}


// param_arr_arr
char ne_signed_int_5(Py_ssize_t arraylen, int nosimd, signed int *data1, signed int *data2) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
		return ne_signed_int_5_simd(arraylen, data1, data2);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != data2[x])) { return 0; }
	}

	return 1;

}


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
char ne_unsigned_int_1(Py_ssize_t arraylen, int nosimd, unsigned int *data1, unsigned int param) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
		return ne_unsigned_int_1_simd(arraylen, data1, param);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != param)) { return 0; }
	}

	return 1;

}


// param_num_arr
char ne_unsigned_int_3(Py_ssize_t arraylen, int nosimd, unsigned int param, unsigned int *data2) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
		return ne_unsigned_int_3_simd(arraylen, param, data2);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(param != data2[x])) { return 0; }
	}

	return 1;

}


// param_arr_arr
char ne_unsigned_int_5(Py_ssize_t arraylen, int nosimd, unsigned int *data1, unsigned int *data2) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (INTSIMDSIZE * 2))) {
		return ne_unsigned_int_5_simd(arraylen, data1, data2);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != data2[x])) { return 0; }
	}

	return 1;

}


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
char ne_signed_long_1(Py_ssize_t arraylen, int nosimd, signed long *data1, signed long param) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != param)) { return 0; }
	}

	return 1;

}


// param_num_arr
char ne_signed_long_3(Py_ssize_t arraylen, int nosimd, signed long param, signed long *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		if (!(param != data2[x])) { return 0; }
	}

	return 1;

}


// param_arr_arr
char ne_signed_long_5(Py_ssize_t arraylen, int nosimd, signed long *data1, signed long *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != data2[x])) { return 0; }
	}

	return 1;

}


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
char ne_unsigned_long_1(Py_ssize_t arraylen, int nosimd, unsigned long *data1, unsigned long param) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != param)) { return 0; }
	}

	return 1;

}


// param_num_arr
char ne_unsigned_long_3(Py_ssize_t arraylen, int nosimd, unsigned long param, unsigned long *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		if (!(param != data2[x])) { return 0; }
	}

	return 1;

}


// param_arr_arr
char ne_unsigned_long_5(Py_ssize_t arraylen, int nosimd, unsigned long *data1, unsigned long *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != data2[x])) { return 0; }
	}

	return 1;

}


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
char ne_signed_long_long_1(Py_ssize_t arraylen, int nosimd, signed long long *data1, signed long long param) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != param)) { return 0; }
	}

	return 1;

}


// param_num_arr
char ne_signed_long_long_3(Py_ssize_t arraylen, int nosimd, signed long long param, signed long long *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		if (!(param != data2[x])) { return 0; }
	}

	return 1;

}


// param_arr_arr
char ne_signed_long_long_5(Py_ssize_t arraylen, int nosimd, signed long long *data1, signed long long *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != data2[x])) { return 0; }
	}

	return 1;

}


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
char ne_unsigned_long_long_1(Py_ssize_t arraylen, int nosimd, unsigned long long *data1, unsigned long long param) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != param)) { return 0; }
	}

	return 1;

}


// param_num_arr
char ne_unsigned_long_long_3(Py_ssize_t arraylen, int nosimd, unsigned long long param, unsigned long long *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		if (!(param != data2[x])) { return 0; }
	}

	return 1;

}


// param_arr_arr
char ne_unsigned_long_long_5(Py_ssize_t arraylen, int nosimd, unsigned long long *data1, unsigned long long *data2) {

	// array index counter.
	Py_ssize_t x;

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != data2[x])) { return 0; }
	}

	return 1;

}


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
char ne_float_1(Py_ssize_t arraylen, int nosimd, float *data1, float param) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (FLOATSIMDSIZE * 2))) {
		return ne_float_1_simd(arraylen, data1, param);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != param)) { return 0; }
	}

	return 1;

}


// param_num_arr
char ne_float_3(Py_ssize_t arraylen, int nosimd, float param, float *data2) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (FLOATSIMDSIZE * 2))) {
		return ne_float_3_simd(arraylen, param, data2);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(param != data2[x])) { return 0; }
	}

	return 1;

}


// param_arr_arr
char ne_float_5(Py_ssize_t arraylen, int nosimd, float *data1, float *data2) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86) || defined(AF_HASSIMD_ARM_AARCH64)
	// SIMD version.
	if (!nosimd && (arraylen >= (FLOATSIMDSIZE * 2))) {
		return ne_float_5_simd(arraylen, data1, data2);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != data2[x])) { return 0; }
	}

	return 1;

}


/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   param = The parameter to be applied to each array element.
*/
// param_arr_num
char ne_double_1(Py_ssize_t arraylen, int nosimd, double *data1, double param) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86)
	// SIMD version.
	if (!nosimd && (arraylen >= (DOUBLESIMDSIZE * 2))) {
		return ne_double_1_simd(arraylen, data1, param);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != param)) { return 0; }
	}

	return 1;

}


// param_num_arr
char ne_double_3(Py_ssize_t arraylen, int nosimd, double param, double *data2) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86)
	// SIMD version.
	if (!nosimd && (arraylen >= (DOUBLESIMDSIZE * 2))) {
		return ne_double_3_simd(arraylen, param, data2);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(param != data2[x])) { return 0; }
	}

	return 1;

}


// param_arr_arr
char ne_double_5(Py_ssize_t arraylen, int nosimd, double *data1, double *data2) {

	// array index counter.
	Py_ssize_t x;

#if defined(AF_HASSIMD_X86)
	// SIMD version.
	if (!nosimd && (arraylen >= (DOUBLESIMDSIZE * 2))) {
		return ne_double_5_simd(arraylen, data1, data2);
	}
#endif

	for (x = 0; x < arraylen; x++) {
		if (!(data1[x] != data2[x])) { return 0; }
	}

	return 1;

}


/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_ne(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	char resultcode = 0;

	// This is used to hold the parsed parameters.
	struct args_params_comp arraydata = ARGSINIT_COMP;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_comp(self, args, keywds, "ne");

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
				case param_arr_num : {
					resultcode = ne_signed_char_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.b, arraydata.param.b);
					break;
				}
				case param_num_arr : {
					resultcode = ne_signed_char_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.b, arraydata.array2.b);
					break;
				}
				case param_arr_arr : {
					resultcode = ne_signed_char_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.b, arraydata.array2.b);
					break;
				}
			}
			break;
		}

		// unsigned_char
		case 'B' : {
			switch (arraydata.paramcat) {
				case param_arr_num : {
					resultcode = ne_unsigned_char_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.B, arraydata.param.B);
					break;
				}
				case param_num_arr : {
					resultcode = ne_unsigned_char_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.B, arraydata.array2.B);
					break;
				}
				case param_arr_arr : {
					resultcode = ne_unsigned_char_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.B, arraydata.array2.B);
					break;
				}
			}
			break;
		}

		// signed_short
		case 'h' : {
			switch (arraydata.paramcat) {
				case param_arr_num : {
					resultcode = ne_signed_short_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.h, arraydata.param.h);
					break;
				}
				case param_num_arr : {
					resultcode = ne_signed_short_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.h, arraydata.array2.h);
					break;
				}
				case param_arr_arr : {
					resultcode = ne_signed_short_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.h, arraydata.array2.h);
					break;
				}
			}
			break;
		}

		// unsigned_short
		case 'H' : {
			switch (arraydata.paramcat) {
				case param_arr_num : {
					resultcode = ne_unsigned_short_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.H, arraydata.param.H);
					break;
				}
				case param_num_arr : {
					resultcode = ne_unsigned_short_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.H, arraydata.array2.H);
					break;
				}
				case param_arr_arr : {
					resultcode = ne_unsigned_short_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.H, arraydata.array2.H);
					break;
				}
			}
			break;
		}

		// signed_int
		case 'i' : {
			switch (arraydata.paramcat) {
				case param_arr_num : {
					resultcode = ne_signed_int_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.i, arraydata.param.i);
					break;
				}
				case param_num_arr : {
					resultcode = ne_signed_int_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.i, arraydata.array2.i);
					break;
				}
				case param_arr_arr : {
					resultcode = ne_signed_int_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.i, arraydata.array2.i);
					break;
				}
			}
			break;
		}

		// unsigned_int
		case 'I' : {
			switch (arraydata.paramcat) {
				case param_arr_num : {
					resultcode = ne_unsigned_int_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.I, arraydata.param.I);
					break;
				}
				case param_num_arr : {
					resultcode = ne_unsigned_int_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.I, arraydata.array2.I);
					break;
				}
				case param_arr_arr : {
					resultcode = ne_unsigned_int_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.I, arraydata.array2.I);
					break;
				}
			}
			break;
		}

		// signed_long
		case 'l' : {
			switch (arraydata.paramcat) {
				case param_arr_num : {
					resultcode = ne_signed_long_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.l, arraydata.param.l);
					break;
				}
				case param_num_arr : {
					resultcode = ne_signed_long_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.l, arraydata.array2.l);
					break;
				}
				case param_arr_arr : {
					resultcode = ne_signed_long_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.l, arraydata.array2.l);
					break;
				}
			}
			break;
		}

		// unsigned_long
		case 'L' : {
			switch (arraydata.paramcat) {
				case param_arr_num : {
					resultcode = ne_unsigned_long_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.L, arraydata.param.L);
					break;
				}
				case param_num_arr : {
					resultcode = ne_unsigned_long_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.L, arraydata.array2.L);
					break;
				}
				case param_arr_arr : {
					resultcode = ne_unsigned_long_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.L, arraydata.array2.L);
					break;
				}
			}
			break;
		}

		// signed_long_long
		case 'q' : {
			switch (arraydata.paramcat) {
				case param_arr_num : {
					resultcode = ne_signed_long_long_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.q, arraydata.param.q);
					break;
				}
				case param_num_arr : {
					resultcode = ne_signed_long_long_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.q, arraydata.array2.q);
					break;
				}
				case param_arr_arr : {
					resultcode = ne_signed_long_long_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.q, arraydata.array2.q);
					break;
				}
			}
			break;
		}

		// unsigned_long_long
		case 'Q' : {
			switch (arraydata.paramcat) {
				case param_arr_num : {
					resultcode = ne_unsigned_long_long_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.Q, arraydata.param.Q);
					break;
				}
				case param_num_arr : {
					resultcode = ne_unsigned_long_long_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.Q, arraydata.array2.Q);
					break;
				}
				case param_arr_arr : {
					resultcode = ne_unsigned_long_long_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.Q, arraydata.array2.Q);
					break;
				}
			}
			break;
		}

		// float
		case 'f' : {
			switch (arraydata.paramcat) {
				case param_arr_num : {
					resultcode = ne_float_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.f, arraydata.param.f);
					break;
				}
				case param_num_arr : {
					resultcode = ne_float_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.f, arraydata.array2.f);
					break;
				}
				case param_arr_arr : {
					resultcode = ne_float_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.f, arraydata.array2.f);
					break;
				}
			}
			break;
		}

		// double
		case 'd' : {
			switch (arraydata.paramcat) {
				case param_arr_num : {
					resultcode = ne_double_1(arraydata.arraylength, arraydata.nosimd, arraydata.array1.d, arraydata.param.d);
					break;
				}
				case param_num_arr : {
					resultcode = ne_double_3(arraydata.arraylength, arraydata.nosimd, arraydata.param.d, arraydata.array2.d);
					break;
				}
				case param_arr_arr : {
					resultcode = ne_double_5(arraydata.arraylength, arraydata.nosimd, arraydata.array1.d, arraydata.array2.d);
					break;
				}
			}
			break;
		}

		// Wrong array type code.
		default: {
			releasebuffers_comp(arraydata);
			ErrMsgTypeExpectFloat();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_comp(arraydata);


	// Return whether compare was OK.
	if (resultcode) {
		Py_RETURN_TRUE;
	} else {
		Py_RETURN_FALSE;
	}

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(ne__doc__,
"ne \n\
_____________________________ \n\
\n\
Calculate ne over the values in an array.  \n\
\n\
======================  ============================================== \n\
Equivalent to:          all([x != param for x in array1]) \n\
or                      all([param != x for x in array1]) \n\
or                      all([x != y for x,y in zip(array1, array2)]) \n\
======================  ============================================== \n\
\n\
======================  ============================================== \n\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
  result = ne(array1, param) \n\
  result = ne(param, array1) \n\
  result = ne(array1, array2) \n\
  result = ne(array1, param, maxlen=y) \n\
  result = ne(array1, param, nosimd=False) \n\
\n\
* array1 - The first input data array to be examined. If no output  \n\
  array is provided the results will overwrite the input data.  \n\
* param - A non-array numeric parameter.  \n\
* array2 - A second input data array. Each element in this array is  \n\
  applied to the corresponding element in the first array.  \n\
* maxlen - Limit the length of the array used. This must be a valid  \n\
  positive integer. If a zero or negative length, or a value which is  \n\
  greater than the actual length of the array is specified, this  \n\
  parameter is ignored.  \n\
* nosimd - If True, SIMD acceleration is disabled if present.  \n\
  The default is False (SIMD acceleration is enabled if present). \n\
* result - A boolean value corresponding to the result of all the \n\
  comparison operations. If all comparison operations result in true, \n\
  the return value will be true. If any of them result in false, the \n\
  return value will be false. \n\
");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "ne" is the name seen inside of Python. 
 "py_ne" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef ne_methods[] = {
	{"ne",  (PyCFunction)py_ne, METH_VARARGS | METH_KEYWORDS, ne__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef nemodule = {
    PyModuleDef_HEAD_INIT,
    "ne",
    NULL,
    -1,
    ne_methods
};

PyMODINIT_FUNC PyInit_ne(void)
{
    return PyModule_Create(&nemodule);
};

/*--------------------------------------------------------------------------- */

