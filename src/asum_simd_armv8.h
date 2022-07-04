//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   asum_simd_armv8.h
// Purpose:  Calculate the asum of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     05-May-2017
// Ver:      04-Jul-2022.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2022    Michael Griffin    <m12.griffin@gmail.com>
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


long long asum_signed_char_simd(Py_ssize_t arraylen, signed char *data);
long long asum_signed_char_simd_ovfl(Py_ssize_t arraylen, signed char *data, signed int *errflag);
unsigned long long asum_unsigned_char_simd(Py_ssize_t arraylen, unsigned char *data);
unsigned long long asum_unsigned_char_simd_ovfl(Py_ssize_t arraylen, unsigned char *data, signed int *errflag);
long long asum_signed_short_simd(Py_ssize_t arraylen, signed short *data);
long long asum_signed_short_simd_ovfl(Py_ssize_t arraylen, signed short *data, signed int *errflag);
unsigned long long asum_unsigned_short_simd(Py_ssize_t arraylen, unsigned short *data);
unsigned long long asum_unsigned_short_simd_ovfl(Py_ssize_t arraylen, unsigned short *data, signed int *errflag);
float asum_float_simd(Py_ssize_t arraylen, float *data);
float asum_float_simd_ovfl(Py_ssize_t arraylen, float *data, signed int *errflag);


