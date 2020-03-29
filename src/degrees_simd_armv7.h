//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   degrees_simd_armv7.h
// Purpose:  Calculate the degrees of values in an array.
//           This file provides an SIMD version of the functions.
// Language: C
// Date:     02-Oct-2019
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


void degrees_float_1_simd(Py_ssize_t arraylen, float *data);
void degrees_float_2_simd(Py_ssize_t arraylen, float *data, float *dataout);


