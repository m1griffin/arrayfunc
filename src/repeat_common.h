//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   repeat_common.h
// Purpose:  Fill an array with a specified value.
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


void repeat_signed_char(Py_ssize_t arraylen, signed char *data, signed char fillvalue);
void repeat_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char fillvalue);
void repeat_signed_short(Py_ssize_t arraylen, signed short *data, signed short fillvalue);
void repeat_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short fillvalue);
void repeat_signed_int(Py_ssize_t arraylen, signed int *data, signed int fillvalue);
void repeat_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int fillvalue);
void repeat_signed_long(Py_ssize_t arraylen, signed long *data, signed long fillvalue);
void repeat_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long fillvalue);
void repeat_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long fillvalue);
void repeat_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long fillvalue);
void repeat_float(Py_ssize_t arraylen, float *data, float fillvalue);
void repeat_double(Py_ssize_t arraylen, double *data, double fillvalue);

