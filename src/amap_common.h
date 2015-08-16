//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   amap_common.h
// Purpose:  Common code for amap and amapi.
// Language: C
// Date:     09-Apr-2014
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2015    Michael Griffin    <m12.griffin@gmail.com>
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

/*--------------------------------------------------------------------------- */
// This must be defined before "Python.h" in order for the pointers in the
// argument parsing functions to work properly. 
#define PY_SSIZE_T_CLEAN

#include "Python.h"

#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */

signed int map_signed_char(signed int opcode, Py_ssize_t arraylen, signed char *data, signed char *dataout, signed char param1, unsigned int paramcount, unsigned int disableovfl);
signed int map_unsigned_char(signed int opcode, Py_ssize_t arraylen, unsigned char *data, unsigned char *dataout, unsigned char param1, unsigned int paramcount, unsigned int disableovfl);
signed int map_signed_short(signed int opcode, Py_ssize_t arraylen, signed short *data, signed short *dataout, signed short param1, unsigned int paramcount, unsigned int disableovfl);
signed int map_unsigned_short(signed int opcode, Py_ssize_t arraylen, unsigned short *data, unsigned short *dataout, unsigned short param1, unsigned int paramcount, unsigned int disableovfl);
signed int map_signed_int(signed int opcode, Py_ssize_t arraylen, signed int *data, signed int *dataout, signed int param1, unsigned int paramcount, unsigned int disableovfl);
signed int map_unsigned_int(signed int opcode, Py_ssize_t arraylen, unsigned int *data, unsigned int *dataout, unsigned int param1, unsigned int paramcount, unsigned int disableovfl);
signed int map_signed_long(signed int opcode, Py_ssize_t arraylen, signed long *data, signed long *dataout, signed long param1, unsigned int paramcount, unsigned int disableovfl);
signed int map_unsigned_long(signed int opcode, Py_ssize_t arraylen, unsigned long *data, unsigned long *dataout, unsigned long param1, unsigned int paramcount, unsigned int disableovfl);
signed int map_signed_long_long(signed int opcode, Py_ssize_t arraylen, signed long long *data, signed long long *dataout, signed long long param1, unsigned int paramcount, unsigned int disableovfl);
signed int map_unsigned_long_long(signed int opcode, Py_ssize_t arraylen, unsigned long long *data, unsigned long long *dataout, unsigned long long param1, unsigned int paramcount, unsigned int disableovfl);
signed int map_float(signed int opcode, Py_ssize_t arraylen, float *data, float *dataout, float param1, unsigned int paramcount, unsigned int disableovfl);
signed int map_double(signed int opcode, Py_ssize_t arraylen, double *data, double *dataout, double param1, unsigned int paramcount, unsigned int disableovfl);

/*--------------------------------------------------------------------------- */
