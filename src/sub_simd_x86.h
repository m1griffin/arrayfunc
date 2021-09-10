//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   sub_simd_x86.h
// Purpose:  Calculate the sub of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     1-Apr-2019
// Ver:      06-Sep-2021.
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


void sub_signed_char_1_simd(Py_ssize_t arraylen, signed char *data1, signed char param);
void sub_signed_char_2_simd(Py_ssize_t arraylen, signed char *data1, signed char param, signed char *data3);
void sub_signed_char_3_simd(Py_ssize_t arraylen, signed char param, signed char *data2);
void sub_signed_char_4_simd(Py_ssize_t arraylen, signed char param, signed char *data2, signed char *data3);
void sub_signed_char_5_simd(Py_ssize_t arraylen, signed char *data1, signed char *data2);
void sub_signed_char_6_simd(Py_ssize_t arraylen, signed char *data1, signed char *data2, signed char *data3);
char sub_signed_char_1_simd_ovfl(Py_ssize_t arraylen, signed char *data1, signed char param);
char sub_signed_char_2_simd_ovfl(Py_ssize_t arraylen, signed char *data1, signed char param, signed char *data3);
char sub_signed_char_3_simd_ovfl(Py_ssize_t arraylen, signed char param, signed char *data2);
char sub_signed_char_4_simd_ovfl(Py_ssize_t arraylen, signed char param, signed char *data2, signed char *data3);
void sub_signed_short_1_simd(Py_ssize_t arraylen, signed short *data1, signed short param);
void sub_signed_short_2_simd(Py_ssize_t arraylen, signed short *data1, signed short param, signed short *data3);
void sub_signed_short_3_simd(Py_ssize_t arraylen, signed short param, signed short *data2);
void sub_signed_short_4_simd(Py_ssize_t arraylen, signed short param, signed short *data2, signed short *data3);
void sub_signed_short_5_simd(Py_ssize_t arraylen, signed short *data1, signed short *data2);
void sub_signed_short_6_simd(Py_ssize_t arraylen, signed short *data1, signed short *data2, signed short *data3);
char sub_signed_short_1_simd_ovfl(Py_ssize_t arraylen, signed short *data1, signed short param);
char sub_signed_short_2_simd_ovfl(Py_ssize_t arraylen, signed short *data1, signed short param, signed short *data3);
char sub_signed_short_3_simd_ovfl(Py_ssize_t arraylen, signed short param, signed short *data2);
char sub_signed_short_4_simd_ovfl(Py_ssize_t arraylen, signed short param, signed short *data2, signed short *data3);
void sub_signed_int_1_simd(Py_ssize_t arraylen, signed int *data1, signed int param);
void sub_signed_int_2_simd(Py_ssize_t arraylen, signed int *data1, signed int param, signed int *data3);
void sub_signed_int_3_simd(Py_ssize_t arraylen, signed int param, signed int *data2);
void sub_signed_int_4_simd(Py_ssize_t arraylen, signed int param, signed int *data2, signed int *data3);
void sub_signed_int_5_simd(Py_ssize_t arraylen, signed int *data1, signed int *data2);
void sub_signed_int_6_simd(Py_ssize_t arraylen, signed int *data1, signed int *data2, signed int *data3);
char sub_signed_int_1_simd_ovfl(Py_ssize_t arraylen, signed int *data1, signed int param);
char sub_signed_int_2_simd_ovfl(Py_ssize_t arraylen, signed int *data1, signed int param, signed int *data3);
char sub_signed_int_3_simd_ovfl(Py_ssize_t arraylen, signed int param, signed int *data2);
char sub_signed_int_4_simd_ovfl(Py_ssize_t arraylen, signed int param, signed int *data2, signed int *data3);
void sub_float_1_simd(Py_ssize_t arraylen, float *data1, float param);
void sub_float_2_simd(Py_ssize_t arraylen, float *data1, float param, float *data3);
void sub_float_3_simd(Py_ssize_t arraylen, float param, float *data2);
void sub_float_4_simd(Py_ssize_t arraylen, float param, float *data2, float *data3);
void sub_float_5_simd(Py_ssize_t arraylen, float *data1, float *data2);
void sub_float_6_simd(Py_ssize_t arraylen, float *data1, float *data2, float *data3);
void sub_double_1_simd(Py_ssize_t arraylen, double *data1, double param);
void sub_double_2_simd(Py_ssize_t arraylen, double *data1, double param, double *data3);
void sub_double_3_simd(Py_ssize_t arraylen, double param, double *data2);
void sub_double_4_simd(Py_ssize_t arraylen, double param, double *data2, double *data3);
void sub_double_5_simd(Py_ssize_t arraylen, double *data1, double *data2);
void sub_double_6_simd(Py_ssize_t arraylen, double *data1, double *data2, double *data3);


