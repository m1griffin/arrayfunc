//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   asum_common.h
// Purpose:  Sum all the values in an array.
//           Common platform independent code.
// Language: C
// Date:     15-May-2014
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


signed long asum_signed_char(Py_ssize_t arraylen, signed char *data, signed int *errflag, signed int ignoreerrors);
unsigned long asum_unsigned_char(Py_ssize_t arraylen, unsigned char *data, signed int *errflag, signed int ignoreerrors);
signed long asum_signed_short(Py_ssize_t arraylen, signed short *data, signed int *errflag, signed int ignoreerrors);
unsigned long asum_unsigned_short(Py_ssize_t arraylen, unsigned short *data, signed int *errflag, signed int ignoreerrors);
signed long asum_signed_int(Py_ssize_t arraylen, signed int *data, signed int *errflag, signed int ignoreerrors);
unsigned long asum_unsigned_int(Py_ssize_t arraylen, unsigned int *data, signed int *errflag, signed int ignoreerrors);
signed long asum_signed_long(Py_ssize_t arraylen, signed long *data, signed int *errflag, signed int ignoreerrors);
unsigned long asum_unsigned_long(Py_ssize_t arraylen, unsigned long *data, signed int *errflag, signed int ignoreerrors);
signed long long asum_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed int *errflag, signed int ignoreerrors);
unsigned long long asum_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, signed int *errflag, signed int ignoreerrors);
float asum_float(Py_ssize_t arraylen, float *data, signed int *errflag, signed int ignoreerrors, unsigned int nosimd);
double asum_double(Py_ssize_t arraylen, double *data, signed int *errflag, signed int ignoreerrors, unsigned int nosimd);

