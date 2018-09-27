//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   cycle_common.h
// Purpose:  Fill an array with a series of values, repeating as necessary.
//           Common platform independent code.
// Language: C
// Date:     07-May-2014
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


void cycle_signed_char(Py_ssize_t arraylen, signed char *data, signed char startvalue, signed char stopvalue, signed char stepvalue);
void cycle_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char startvalue, unsigned char stopvalue, unsigned char stepvalue);
void cycle_signed_short(Py_ssize_t arraylen, signed short *data, signed short startvalue, signed short stopvalue, signed short stepvalue);
void cycle_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short startvalue, unsigned short stopvalue, unsigned short stepvalue);
void cycle_signed_int(Py_ssize_t arraylen, signed int *data, signed int startvalue, signed int stopvalue, signed int stepvalue);
void cycle_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int startvalue, unsigned int stopvalue, unsigned int stepvalue);
void cycle_signed_long(Py_ssize_t arraylen, signed long *data, signed long startvalue, signed long stopvalue, signed long stepvalue);
void cycle_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long startvalue, unsigned long stopvalue, unsigned long stepvalue);
void cycle_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long startvalue, signed long long stopvalue, signed long long stepvalue);
void cycle_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long startvalue, unsigned long long stopvalue, unsigned long long stepvalue);
void cycle_float(Py_ssize_t arraylen, float *data, float startvalue, float stopvalue, float stepvalue);
void cycle_double(Py_ssize_t arraylen, double *data, double startvalue, double stopvalue, double stepvalue);

