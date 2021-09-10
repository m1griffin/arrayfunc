//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   add_simd_armv8.h
// Purpose:  Calculate the add of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     26-Mar-2020
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


void add_signed_char_1_simd(Py_ssize_t arraylen, signed char *data1, signed char param);
void add_signed_char_2_simd(Py_ssize_t arraylen, signed char *data1, signed char param, signed char *data3);
void add_signed_char_3_simd(Py_ssize_t arraylen, signed char param, signed char *data2);
void add_signed_char_4_simd(Py_ssize_t arraylen, signed char param, signed char *data2, signed char *data3);
void add_signed_char_5_simd(Py_ssize_t arraylen, signed char *data1, signed char *data2);
void add_signed_char_6_simd(Py_ssize_t arraylen, signed char *data1, signed char *data2, signed char *data3);
char add_signed_char_1_simd_ovfl(Py_ssize_t arraylen, signed char *data1, signed char param);
char add_signed_char_2_simd_ovfl(Py_ssize_t arraylen, signed char *data1, signed char param, signed char *data3);
char add_signed_char_3_simd_ovfl(Py_ssize_t arraylen, signed char param, signed char *data2);
char add_signed_char_4_simd_ovfl(Py_ssize_t arraylen, signed char param, signed char *data2, signed char *data3);
void add_unsigned_char_1_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param);
void add_unsigned_char_2_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param, unsigned char *data3);
void add_unsigned_char_3_simd(Py_ssize_t arraylen, unsigned char param, unsigned char *data2);
void add_unsigned_char_4_simd(Py_ssize_t arraylen, unsigned char param, unsigned char *data2, unsigned char *data3);
void add_unsigned_char_5_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2);
void add_unsigned_char_6_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2, unsigned char *data3);
char add_unsigned_char_1_simd_ovfl(Py_ssize_t arraylen, unsigned char *data1, unsigned char param);
char add_unsigned_char_2_simd_ovfl(Py_ssize_t arraylen, unsigned char *data1, unsigned char param, unsigned char *data3);
char add_unsigned_char_3_simd_ovfl(Py_ssize_t arraylen, unsigned char param, unsigned char *data2);
char add_unsigned_char_4_simd_ovfl(Py_ssize_t arraylen, unsigned char param, unsigned char *data2, unsigned char *data3);
char add_unsigned_char_5_simd_ovfl(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2);
char add_unsigned_char_6_simd_ovfl(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2, unsigned char *data3);
void add_signed_short_1_simd(Py_ssize_t arraylen, signed short *data1, signed short param);
void add_signed_short_2_simd(Py_ssize_t arraylen, signed short *data1, signed short param, signed short *data3);
void add_signed_short_3_simd(Py_ssize_t arraylen, signed short param, signed short *data2);
void add_signed_short_4_simd(Py_ssize_t arraylen, signed short param, signed short *data2, signed short *data3);
void add_signed_short_5_simd(Py_ssize_t arraylen, signed short *data1, signed short *data2);
void add_signed_short_6_simd(Py_ssize_t arraylen, signed short *data1, signed short *data2, signed short *data3);
char add_signed_short_1_simd_ovfl(Py_ssize_t arraylen, signed short *data1, signed short param);
char add_signed_short_2_simd_ovfl(Py_ssize_t arraylen, signed short *data1, signed short param, signed short *data3);
char add_signed_short_3_simd_ovfl(Py_ssize_t arraylen, signed short param, signed short *data2);
char add_signed_short_4_simd_ovfl(Py_ssize_t arraylen, signed short param, signed short *data2, signed short *data3);
void add_unsigned_short_1_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param);
void add_unsigned_short_2_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param, unsigned short *data3);
void add_unsigned_short_3_simd(Py_ssize_t arraylen, unsigned short param, unsigned short *data2);
void add_unsigned_short_4_simd(Py_ssize_t arraylen, unsigned short param, unsigned short *data2, unsigned short *data3);
void add_unsigned_short_5_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2);
void add_unsigned_short_6_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2, unsigned short *data3);
char add_unsigned_short_1_simd_ovfl(Py_ssize_t arraylen, unsigned short *data1, unsigned short param);
char add_unsigned_short_2_simd_ovfl(Py_ssize_t arraylen, unsigned short *data1, unsigned short param, unsigned short *data3);
char add_unsigned_short_3_simd_ovfl(Py_ssize_t arraylen, unsigned short param, unsigned short *data2);
char add_unsigned_short_4_simd_ovfl(Py_ssize_t arraylen, unsigned short param, unsigned short *data2, unsigned short *data3);
char add_unsigned_short_5_simd_ovfl(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2);
char add_unsigned_short_6_simd_ovfl(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2, unsigned short *data3);
void add_signed_int_1_simd(Py_ssize_t arraylen, signed int *data1, signed int param);
void add_signed_int_2_simd(Py_ssize_t arraylen, signed int *data1, signed int param, signed int *data3);
void add_signed_int_3_simd(Py_ssize_t arraylen, signed int param, signed int *data2);
void add_signed_int_4_simd(Py_ssize_t arraylen, signed int param, signed int *data2, signed int *data3);
void add_signed_int_5_simd(Py_ssize_t arraylen, signed int *data1, signed int *data2);
void add_signed_int_6_simd(Py_ssize_t arraylen, signed int *data1, signed int *data2, signed int *data3);
char add_signed_int_1_simd_ovfl(Py_ssize_t arraylen, signed int *data1, signed int param);
char add_signed_int_2_simd_ovfl(Py_ssize_t arraylen, signed int *data1, signed int param, signed int *data3);
char add_signed_int_3_simd_ovfl(Py_ssize_t arraylen, signed int param, signed int *data2);
char add_signed_int_4_simd_ovfl(Py_ssize_t arraylen, signed int param, signed int *data2, signed int *data3);
void add_unsigned_int_1_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param);
void add_unsigned_int_2_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param, unsigned int *data3);
void add_unsigned_int_3_simd(Py_ssize_t arraylen, unsigned int param, unsigned int *data2);
void add_unsigned_int_4_simd(Py_ssize_t arraylen, unsigned int param, unsigned int *data2, unsigned int *data3);
void add_unsigned_int_5_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2);
void add_unsigned_int_6_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2, unsigned int *data3);
char add_unsigned_int_1_simd_ovfl(Py_ssize_t arraylen, unsigned int *data1, unsigned int param);
char add_unsigned_int_2_simd_ovfl(Py_ssize_t arraylen, unsigned int *data1, unsigned int param, unsigned int *data3);
char add_unsigned_int_3_simd_ovfl(Py_ssize_t arraylen, unsigned int param, unsigned int *data2);
char add_unsigned_int_4_simd_ovfl(Py_ssize_t arraylen, unsigned int param, unsigned int *data2, unsigned int *data3);
char add_unsigned_int_5_simd_ovfl(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2);
char add_unsigned_int_6_simd_ovfl(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2, unsigned int *data3);
void add_float_1_simd(Py_ssize_t arraylen, float *data1, float param);
void add_float_2_simd(Py_ssize_t arraylen, float *data1, float param, float *data3);
void add_float_3_simd(Py_ssize_t arraylen, float param, float *data2);
void add_float_4_simd(Py_ssize_t arraylen, float param, float *data2, float *data3);
void add_float_5_simd(Py_ssize_t arraylen, float *data1, float *data2);
void add_float_6_simd(Py_ssize_t arraylen, float *data1, float *data2, float *data3);


