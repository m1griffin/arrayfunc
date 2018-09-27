//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   findindices_common.h
// Purpose:  Searches an array for the array indices which meet the specified 
//           criteria and writes the results to a second array. Also returns the 
//           number of matches found.
//           Common platform independent code.
// Language: C
// Date:     11-May-2014
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


Py_ssize_t findindices_signed_char(signed int opcode, Py_ssize_t arraylen, signed char *data, signed long long *dataout, signed char param1);
Py_ssize_t findindices_unsigned_char(signed int opcode, Py_ssize_t arraylen, unsigned char *data, signed long long *dataout, unsigned char param1);
Py_ssize_t findindices_signed_short(signed int opcode, Py_ssize_t arraylen, signed short *data, signed long long *dataout, signed short param1);
Py_ssize_t findindices_unsigned_short(signed int opcode, Py_ssize_t arraylen, unsigned short *data, signed long long *dataout, unsigned short param1);
Py_ssize_t findindices_signed_int(signed int opcode, Py_ssize_t arraylen, signed int *data, signed long long *dataout, signed int param1);
Py_ssize_t findindices_unsigned_int(signed int opcode, Py_ssize_t arraylen, unsigned int *data, signed long long *dataout, unsigned int param1);
Py_ssize_t findindices_signed_long(signed int opcode, Py_ssize_t arraylen, signed long *data, signed long long *dataout, signed long param1);
Py_ssize_t findindices_unsigned_long(signed int opcode, Py_ssize_t arraylen, unsigned long *data, signed long long *dataout, unsigned long param1);
Py_ssize_t findindices_signed_long_long(signed int opcode, Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1);
Py_ssize_t findindices_unsigned_long_long(signed int opcode, Py_ssize_t arraylen, unsigned long long *data, signed long long *dataout, unsigned long long param1);
Py_ssize_t findindices_float(signed int opcode, Py_ssize_t arraylen, float *data, signed long long *dataout, float param1);
Py_ssize_t findindices_double(signed int opcode, Py_ssize_t arraylen, double *data, signed long long *dataout, double param1);

