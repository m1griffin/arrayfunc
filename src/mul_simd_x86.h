//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   mul_simd_x86.h
// Purpose:  Calculate the mul of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     1-Apr-2019
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


void mul_float_1_simd(Py_ssize_t arraylen, float *data1, float param);
void mul_float_2_simd(Py_ssize_t arraylen, float *data1, float param, float *data3);
void mul_float_3_simd(Py_ssize_t arraylen, float param, float *data2);
void mul_float_4_simd(Py_ssize_t arraylen, float param, float *data2, float *data3);
void mul_float_5_simd(Py_ssize_t arraylen, float *data1, float *data2);
void mul_float_6_simd(Py_ssize_t arraylen, float *data1, float *data2, float *data3);
char mul_float_1_simd_ovfl(Py_ssize_t arraylen, float *data1, float param);
char mul_float_2_simd_ovfl(Py_ssize_t arraylen, float *data1, float param, float *data3);
char mul_float_3_simd_ovfl(Py_ssize_t arraylen, float param, float *data2);
char mul_float_4_simd_ovfl(Py_ssize_t arraylen, float param, float *data2, float *data3);
char mul_float_5_simd_ovfl(Py_ssize_t arraylen, float *data1, float *data2);
char mul_float_6_simd_ovfl(Py_ssize_t arraylen, float *data1, float *data2, float *data3);
void mul_double_1_simd(Py_ssize_t arraylen, double *data1, double param);
void mul_double_2_simd(Py_ssize_t arraylen, double *data1, double param, double *data3);
void mul_double_3_simd(Py_ssize_t arraylen, double param, double *data2);
void mul_double_4_simd(Py_ssize_t arraylen, double param, double *data2, double *data3);
void mul_double_5_simd(Py_ssize_t arraylen, double *data1, double *data2);
void mul_double_6_simd(Py_ssize_t arraylen, double *data1, double *data2, double *data3);
char mul_double_1_simd_ovfl(Py_ssize_t arraylen, double *data1, double param);
char mul_double_2_simd_ovfl(Py_ssize_t arraylen, double *data1, double param, double *data3);
char mul_double_3_simd_ovfl(Py_ssize_t arraylen, double param, double *data2);
char mul_double_4_simd_ovfl(Py_ssize_t arraylen, double param, double *data2, double *data3);
char mul_double_5_simd_ovfl(Py_ssize_t arraylen, double *data1, double *data2);
char mul_double_6_simd_ovfl(Py_ssize_t arraylen, double *data1, double *data2, double *data3);


