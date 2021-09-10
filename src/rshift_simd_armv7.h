//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   rshift_simd_armv7.h
// Purpose:  Calculate the rshift of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     05-Oct-2019
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


void rshift_signed_char_1_simd(Py_ssize_t arraylen, signed char *data1, signed char param);
void rshift_signed_char_2_simd(Py_ssize_t arraylen, signed char *data1, signed char param, signed char *data3);
void rshift_unsigned_char_1_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param);
void rshift_unsigned_char_2_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param, unsigned char *data3);
void rshift_signed_short_1_simd(Py_ssize_t arraylen, signed short *data1, signed short param);
void rshift_signed_short_2_simd(Py_ssize_t arraylen, signed short *data1, signed short param, signed short *data3);
void rshift_unsigned_short_1_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param);
void rshift_unsigned_short_2_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param, unsigned short *data3);
void rshift_signed_int_1_simd(Py_ssize_t arraylen, signed int *data1, signed int param);
void rshift_signed_int_2_simd(Py_ssize_t arraylen, signed int *data1, signed int param, signed int *data3);
void rshift_unsigned_int_1_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param);
void rshift_unsigned_int_2_simd(Py_ssize_t arraylen, unsigned int *data1, unsigned int param, unsigned int *data3);


