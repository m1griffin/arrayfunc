//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   compress_common.h
// Purpose:  Copy values from an array, using a selector array to filter values.
//           Common platform independent code.
// Language: C
// Date:     10-May-2014
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


Py_ssize_t compress_signed_char(Py_ssize_t datalen, signed char *data, 
			Py_ssize_t outlen, signed char *dataout, 
			Py_ssize_t selectorlen, signed char *selector);
Py_ssize_t compress_unsigned_char(Py_ssize_t datalen, unsigned char *data, 
			Py_ssize_t outlen, unsigned char *dataout, 
			Py_ssize_t selectorlen, unsigned char *selector);
Py_ssize_t compress_signed_short(Py_ssize_t datalen, signed short *data, 
			Py_ssize_t outlen, signed short *dataout, 
			Py_ssize_t selectorlen, signed short *selector);
Py_ssize_t compress_unsigned_short(Py_ssize_t datalen, unsigned short *data, 
			Py_ssize_t outlen, unsigned short *dataout, 
			Py_ssize_t selectorlen, unsigned short *selector);
Py_ssize_t compress_signed_int(Py_ssize_t datalen, signed int *data, 
			Py_ssize_t outlen, signed int *dataout, 
			Py_ssize_t selectorlen, signed int *selector);
Py_ssize_t compress_unsigned_int(Py_ssize_t datalen, unsigned int *data, 
			Py_ssize_t outlen, unsigned int *dataout, 
			Py_ssize_t selectorlen, unsigned int *selector);
Py_ssize_t compress_signed_long(Py_ssize_t datalen, signed long *data, 
			Py_ssize_t outlen, signed long *dataout, 
			Py_ssize_t selectorlen, signed long *selector);
Py_ssize_t compress_unsigned_long(Py_ssize_t datalen, unsigned long *data, 
			Py_ssize_t outlen, unsigned long *dataout, 
			Py_ssize_t selectorlen, unsigned long *selector);
Py_ssize_t compress_signed_long_long(Py_ssize_t datalen, signed long long *data, 
			Py_ssize_t outlen, signed long long *dataout, 
			Py_ssize_t selectorlen, signed long long *selector);
Py_ssize_t compress_unsigned_long_long(Py_ssize_t datalen, unsigned long long *data, 
			Py_ssize_t outlen, unsigned long long *dataout, 
			Py_ssize_t selectorlen, unsigned long long *selector);
Py_ssize_t compress_float(Py_ssize_t datalen, float *data, 
			Py_ssize_t outlen, float *dataout, 
			Py_ssize_t selectorlen, float *selector);
Py_ssize_t compress_double(Py_ssize_t datalen, double *data, 
			Py_ssize_t outlen, double *dataout, 
			Py_ssize_t selectorlen, double *selector);

