//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   starmap_common.h
// Purpose:  Common code for starmap and starmapi.
// Language: C
// Date:     11-May-2014.
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

/*--------------------------------------------------------------------------- */

signed int starmap_signed_char(signed int opcode, Py_ssize_t arraylen, signed char *data, signed char *data2, signed char *dataout, unsigned int disableovfl);
signed int starmap_unsigned_char(signed int opcode, Py_ssize_t arraylen, unsigned char *data, unsigned char *data2, unsigned char *dataout, unsigned int disableovfl);
signed int starmap_signed_short(signed int opcode, Py_ssize_t arraylen, signed short *data, signed short *data2, signed short *dataout, unsigned int disableovfl);
signed int starmap_unsigned_short(signed int opcode, Py_ssize_t arraylen, unsigned short *data, unsigned short *data2, unsigned short *dataout, unsigned int disableovfl);
signed int starmap_signed_int(signed int opcode, Py_ssize_t arraylen, signed int *data, signed int *data2, signed int *dataout, unsigned int disableovfl);
signed int starmap_unsigned_int(signed int opcode, Py_ssize_t arraylen, unsigned int *data, unsigned int *data2, unsigned int *dataout, unsigned int disableovfl);
signed int starmap_signed_long(signed int opcode, Py_ssize_t arraylen, signed long *data, signed long *data2, signed long *dataout, unsigned int disableovfl);
signed int starmap_unsigned_long(signed int opcode, Py_ssize_t arraylen, unsigned long *data, unsigned long *data2, unsigned long *dataout, unsigned int disableovfl);
signed int starmap_signed_long_long(signed int opcode, Py_ssize_t arraylen, signed long long *data, signed long long *data2, signed long long *dataout, unsigned int disableovfl);
signed int starmap_unsigned_long_long(signed int opcode, Py_ssize_t arraylen, unsigned long long *data, unsigned long long *data2, unsigned long long *dataout, unsigned int disableovfl);
signed int starmap_float(signed int opcode, Py_ssize_t arraylen, float *data, float *data2, float *dataout, unsigned int disableovfl);
signed int starmap_double(signed int opcode, Py_ssize_t arraylen, double *data, double *data2, double *dataout, unsigned int disableovfl);

/*--------------------------------------------------------------------------- */
