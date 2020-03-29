//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   invert_simd_armv8.h
// Purpose:  Calculate the invert of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     25-Mar-2020
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


void invert_signed_char_1_simd(Py_ssize_t arraylen, signed char *data);
void invert_signed_char_2_simd(Py_ssize_t arraylen, signed char *data, signed char *dataout);
void invert_unsigned_char_1_simd(Py_ssize_t arraylen, unsigned char *data);
void invert_unsigned_char_2_simd(Py_ssize_t arraylen, unsigned char *data, unsigned char *dataout);
void invert_signed_short_1_simd(Py_ssize_t arraylen, signed short *data);
void invert_signed_short_2_simd(Py_ssize_t arraylen, signed short *data, signed short *dataout);
void invert_unsigned_short_1_simd(Py_ssize_t arraylen, unsigned short *data);
void invert_unsigned_short_2_simd(Py_ssize_t arraylen, unsigned short *data, unsigned short *dataout);
void invert_signed_int_1_simd(Py_ssize_t arraylen, signed int *data);
void invert_signed_int_2_simd(Py_ssize_t arraylen, signed int *data, signed int *dataout);
void invert_unsigned_int_1_simd(Py_ssize_t arraylen, unsigned int *data);
void invert_unsigned_int_2_simd(Py_ssize_t arraylen, unsigned int *data, unsigned int *dataout);


