//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   afilter_common.h
// Purpose:  Filter based on a test condition.
//           Common platform independent code.
// Language: C
// Date:     09-May-2014
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


Py_ssize_t afilter_signed_char(signed int opcode, Py_ssize_t arraylen, signed char *data, signed char *dataout, signed char param1);
Py_ssize_t afilter_unsigned_char(signed int opcode, Py_ssize_t arraylen, unsigned char *data, unsigned char *dataout, unsigned char param1);
Py_ssize_t afilter_signed_short(signed int opcode, Py_ssize_t arraylen, signed short *data, signed short *dataout, signed short param1);
Py_ssize_t afilter_unsigned_short(signed int opcode, Py_ssize_t arraylen, unsigned short *data, unsigned short *dataout, unsigned short param1);
Py_ssize_t afilter_signed_int(signed int opcode, Py_ssize_t arraylen, signed int *data, signed int *dataout, signed int param1);
Py_ssize_t afilter_unsigned_int(signed int opcode, Py_ssize_t arraylen, unsigned int *data, unsigned int *dataout, unsigned int param1);
Py_ssize_t afilter_signed_long(signed int opcode, Py_ssize_t arraylen, signed long *data, signed long *dataout, signed long param1);
Py_ssize_t afilter_unsigned_long(signed int opcode, Py_ssize_t arraylen, unsigned long *data, unsigned long *dataout, unsigned long param1);
Py_ssize_t afilter_signed_long_long(signed int opcode, Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1);
Py_ssize_t afilter_unsigned_long_long(signed int opcode, Py_ssize_t arraylen, unsigned long long *data, unsigned long long *dataout, unsigned long long param1);
Py_ssize_t afilter_float(signed int opcode, Py_ssize_t arraylen, float *data, float *dataout, float param1);
Py_ssize_t afilter_double(signed int opcode, Py_ssize_t arraylen, double *data, double *dataout, double param1);

