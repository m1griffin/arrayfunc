//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   neg_simd_armv7.h
// Purpose:  Calculate the neg of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     08-Oct-2019
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


void neg_signed_char_1_simd(Py_ssize_t arraylen, signed char *data);
void neg_signed_char_2_simd(Py_ssize_t arraylen, signed char *data, signed char *dataout);
char neg_signed_char_1_simd_ovfl(Py_ssize_t arraylen, signed char *data);
char neg_signed_char_2_simd_ovfl(Py_ssize_t arraylen, signed char *data, signed char *dataout);
void neg_signed_short_1_simd(Py_ssize_t arraylen, signed short *data);
void neg_signed_short_2_simd(Py_ssize_t arraylen, signed short *data, signed short *dataout);
char neg_signed_short_1_simd_ovfl(Py_ssize_t arraylen, signed short *data);
char neg_signed_short_2_simd_ovfl(Py_ssize_t arraylen, signed short *data, signed short *dataout);


