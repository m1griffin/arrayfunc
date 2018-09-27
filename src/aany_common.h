//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   aany_common.h
// Purpose:  Returns True if any elements in an array meet the selected criteria.
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


signed int aany_signed_char(signed int opcode, Py_ssize_t arraylen, signed char *data, signed char param1, unsigned int nosimd);
signed int aany_unsigned_char(signed int opcode, Py_ssize_t arraylen, unsigned char *data, unsigned char param1);
signed int aany_signed_short(signed int opcode, Py_ssize_t arraylen, signed short *data, signed short param1, unsigned int nosimd);
signed int aany_unsigned_short(signed int opcode, Py_ssize_t arraylen, unsigned short *data, unsigned short param1);
signed int aany_signed_int(signed int opcode, Py_ssize_t arraylen, signed int *data, signed int param1, unsigned int nosimd);
signed int aany_unsigned_int(signed int opcode, Py_ssize_t arraylen, unsigned int *data, unsigned int param1);
signed int aany_signed_long(signed int opcode, Py_ssize_t arraylen, signed long *data, signed long param1);
signed int aany_unsigned_long(signed int opcode, Py_ssize_t arraylen, unsigned long *data, unsigned long param1);
signed int aany_signed_long_long(signed int opcode, Py_ssize_t arraylen, signed long long *data, signed long long param1);
signed int aany_unsigned_long_long(signed int opcode, Py_ssize_t arraylen, unsigned long long *data, unsigned long long param1);
signed int aany_float(signed int opcode, Py_ssize_t arraylen, float *data, float param1, unsigned int nosimd);
signed int aany_double(signed int opcode, Py_ssize_t arraylen, double *data, double param1, unsigned int nosimd);

