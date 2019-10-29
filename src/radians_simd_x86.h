//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   radians_simd_x86.h
// Purpose:  Calculate the radians of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     24-Mar-2019
// Ver:      20-Oct-2019.
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


void radians_float_1_simd(Py_ssize_t arraylen, float *data);
void radians_float_2_simd(Py_ssize_t arraylen, float *data, float *dataout);
void radians_double_1_simd(Py_ssize_t arraylen, double *data);
void radians_double_2_simd(Py_ssize_t arraylen, double *data, double *dataout);


