//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   lt_simd_arm.h
// Purpose:  Calculate the lt of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     06-Oct-2019
// Ver:      19-Oct-2019.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2019    Michael Griffin    <m12.griffin@gmail.com>
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


char lt_signed_char_1_simd(Py_ssize_t arraylen, signed char *data1, signed char param);
char lt_signed_char_3_simd(Py_ssize_t arraylen, signed char param, signed char *data2);
char lt_signed_char_5_simd(Py_ssize_t arraylen, signed char *data1, signed char *data2);
char lt_unsigned_char_1_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char param);
char lt_unsigned_char_3_simd(Py_ssize_t arraylen, unsigned char param, unsigned char *data2);
char lt_unsigned_char_5_simd(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2);
char lt_signed_short_1_simd(Py_ssize_t arraylen, signed short *data1, signed short param);
char lt_signed_short_3_simd(Py_ssize_t arraylen, signed short param, signed short *data2);
char lt_signed_short_5_simd(Py_ssize_t arraylen, signed short *data1, signed short *data2);
char lt_unsigned_short_1_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short param);
char lt_unsigned_short_3_simd(Py_ssize_t arraylen, unsigned short param, unsigned short *data2);
char lt_unsigned_short_5_simd(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2);


