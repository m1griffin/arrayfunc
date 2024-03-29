//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   sqrt_simd_x86.h
// Purpose:  Calculate the sqrt of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     24-Mar-2019
// Ver:      31-Oct-2021.
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


void sqrt_float_1_simd(Py_ssize_t arraylen, float *data);
void sqrt_float_2_simd(Py_ssize_t arraylen, float *data, float *dataout);
char sqrt_float_1_simd_ovfl(Py_ssize_t arraylen, float *data);
char sqrt_float_2_simd_ovfl(Py_ssize_t arraylen, float *data, float *dataout);
void sqrt_double_1_simd(Py_ssize_t arraylen, double *data);
void sqrt_double_2_simd(Py_ssize_t arraylen, double *data, double *dataout);
char sqrt_double_1_simd_ovfl(Py_ssize_t arraylen, double *data);
char sqrt_double_2_simd_ovfl(Py_ssize_t arraylen, double *data, double *dataout);


