//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   amax_common.h
// Purpose:  Find the maximum value in an array.
//           Common platform independent code.
// Language: C
// Date:     04-May-2014
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


signed char amax_signed_char(Py_ssize_t arraylen, signed char *data, unsigned int nosimd);
unsigned char amax_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned int nosimd);
signed short amax_signed_short(Py_ssize_t arraylen, signed short *data, unsigned int nosimd);
unsigned short amax_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned int nosimd);
signed int amax_signed_int(Py_ssize_t arraylen, signed int *data, unsigned int nosimd);
unsigned int amax_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int nosimd);
signed long amax_signed_long(Py_ssize_t arraylen, signed long *data, unsigned int nosimd);
unsigned long amax_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned int nosimd);
signed long long amax_signed_long_long(Py_ssize_t arraylen, signed long long *data, unsigned int nosimd);
unsigned long long amax_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned int nosimd);
float amax_float(Py_ssize_t arraylen, float *data, unsigned int nosimd);
double amax_double(Py_ssize_t arraylen, double *data, unsigned int nosimd);

