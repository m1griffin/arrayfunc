//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   convert_common.h
// Purpose:  Convert arrays between data types.
//           Common platform independent code.
// Language: C
// Date:     08-May-2014
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


signed int convert_signed_char(char arraycode, Py_ssize_t arraylen, signed char *data, union dataarrays dataout);
signed int convert_unsigned_char(char arraycode, Py_ssize_t arraylen, unsigned char *data, union dataarrays dataout);
signed int convert_signed_short(char arraycode, Py_ssize_t arraylen, signed short *data, union dataarrays dataout);
signed int convert_unsigned_short(char arraycode, Py_ssize_t arraylen, unsigned short *data, union dataarrays dataout);
signed int convert_signed_int(char arraycode, Py_ssize_t arraylen, signed int *data, union dataarrays dataout);
signed int convert_unsigned_int(char arraycode, Py_ssize_t arraylen, unsigned int *data, union dataarrays dataout);
signed int convert_signed_long(char arraycode, Py_ssize_t arraylen, signed long *data, union dataarrays dataout);
signed int convert_unsigned_long(char arraycode, Py_ssize_t arraylen, unsigned long *data, union dataarrays dataout);
signed int convert_signed_long_long(char arraycode, Py_ssize_t arraylen, signed long long *data, union dataarrays dataout);
signed int convert_unsigned_long_long(char arraycode, Py_ssize_t arraylen, unsigned long long *data, union dataarrays dataout);
signed int convert_float(char arraycode, Py_ssize_t arraylen, float *data, union dataarrays dataout);
signed int convert_double(char arraycode, Py_ssize_t arraylen, double *data, union dataarrays dataout);

