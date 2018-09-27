//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   aany_simd_x86.h
// Purpose:  Returns True if any elements in an array meet the selected criteria.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     01-May-2017
// Ver:      19-Jun-2018.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2018    Michael Griffin    <m12.griffin@gmail.com>
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


signed int aany_signed_char_simd(signed int opcode, Py_ssize_t arraylen, signed char *data, signed char param1);
signed int aany_signed_short_simd(signed int opcode, Py_ssize_t arraylen, signed short *data, signed short param1);
signed int aany_signed_int_simd(signed int opcode, Py_ssize_t arraylen, signed int *data, signed int param1);
signed int aany_float_simd(signed int opcode, Py_ssize_t arraylen, float *data, float param1);
signed int aany_double_simd(signed int opcode, Py_ssize_t arraylen, double *data, double param1);


