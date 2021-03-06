//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   amax_simd_x86.h
// Purpose:  Calculate the amax of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     16-Apr-2019
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


signed long long amax_signed_char_simd(Py_ssize_t arraylen, signed char *data);
unsigned long long amax_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data);
signed long long amax_signed_short_simd(Py_ssize_t arraylen, signed short *data);
unsigned long long amax_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data);
signed long long amax_signed_int_simd(Py_ssize_t arraylen, signed int *data);
unsigned long long amax_unsigned_int_simd(Py_ssize_t arraylen, unsigned int *data);
double amax_float_simd(Py_ssize_t arraylen, float *data);
double amax_double_simd(Py_ssize_t arraylen, double *data);


