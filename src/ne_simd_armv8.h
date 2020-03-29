//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   ne_simd_armv8.h
// Purpose:  Calculate the ne of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     22-Mar-2020
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


char ne_signed_char_1_simd(Py_ssize_t arraylen, signed char *data1, signed char param);
char ne_signed_char_3_simd(Py_ssize_t arraylen, signed char param, signed char *data2);
char ne_signed_char_5_simd(Py_ssize_t arraylen, signed char *data1, signed char *data2);
char ne_unsigned_char_1_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param);
char ne_unsigned_char_3_simd(Py_ssize_t arraylen, unsigned char param, unsigned char *data2);
char ne_unsigned_char_5_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2);
char ne_signed_short_1_simd(Py_ssize_t arraylen, signed short *data1, signed short param);
char ne_signed_short_3_simd(Py_ssize_t arraylen, signed short param, signed short *data2);
char ne_signed_short_5_simd(Py_ssize_t arraylen, signed short *data1, signed short *data2);
char ne_unsigned_short_1_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param);
char ne_unsigned_short_3_simd(Py_ssize_t arraylen, unsigned short param, unsigned short *data2);
char ne_unsigned_short_5_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2);
char ne_signed_int_1_simd(Py_ssize_t arraylen, signed int *data1, signed int param);
char ne_signed_int_3_simd(Py_ssize_t arraylen, signed int param, signed int *data2);
char ne_signed_int_5_simd(Py_ssize_t arraylen, signed int *data1, signed int *data2);
char ne_unsigned_int_1_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param);
char ne_unsigned_int_3_simd(Py_ssize_t arraylen, unsigned int param, unsigned int *data2);
char ne_unsigned_int_5_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2);
char ne_float_1_simd(Py_ssize_t arraylen, float *data1, float param);
char ne_float_3_simd(Py_ssize_t arraylen, float param, float *data2);
char ne_float_5_simd(Py_ssize_t arraylen, float *data1, float *data2);


