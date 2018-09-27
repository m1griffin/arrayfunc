//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   convert_common.c
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

/*--------------------------------------------------------------------------- */
// This must be defined before "Python.h" in order for the pointers in the
// argument parsing functions to work properly. 
#define PY_SSIZE_T_CLEAN

#include "Python.h"

#include <float.h>
#include "convguardbands.h"
#include "arrayparams_base.h"

#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// Auto generated code goes below.

/*--------------------------------------------------------------------------- */
/* arraycode = The type code used by the destination array.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The converted output array.
   Return = 0 if converted OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int convert_signed_char(char arraycode, Py_ssize_t arraylen, signed char *data, union dataarrays dataout) {

	// array index counter.
	Py_ssize_t x;

	switch(arraycode) {

		// signed char
		case 'b': {
			for(x = 0; x < arraylen; x++) {
				dataout.b[x] = data[x];
			}
			return 0;
		}

		// unsigned char
		case 'B': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.B[x] = (unsigned char) data[x];
			}
			return 0;
		}

		// signed short
		case 'h': {
			for(x = 0; x < arraylen; x++) {
				dataout.h[x] = (signed short) data[x];
			}
			return 0;
		}

		// unsigned short
		case 'H': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.H[x] = (unsigned short) data[x];
			}
			return 0;
		}

		// signed int
		case 'i': {
			for(x = 0; x < arraylen; x++) {
				dataout.i[x] = (signed int) data[x];
			}
			return 0;
		}

		// unsigned int
		case 'I': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.I[x] = (unsigned int) data[x];
			}
			return 0;
		}

		// signed long
		case 'l': {
			for(x = 0; x < arraylen; x++) {
				dataout.l[x] = (signed long) data[x];
			}
			return 0;
		}

		// unsigned long
		case 'L': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.L[x] = (unsigned long) data[x];
			}
			return 0;
		}

		// signed long long
		case 'q': {
			for(x = 0; x < arraylen; x++) {
				dataout.q[x] = (signed long long) data[x];
			}
			return 0;
		}

		// unsigned long long
		case 'Q': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.Q[x] = (unsigned long long) data[x];
			}
			return 0;
		}

		// float
		case 'f': {
			for(x = 0; x < arraylen; x++) {
				dataout.f[x] = (float) data[x];
			}
			return 0;
		}

		// double
		case 'd': {
			for(x = 0; x < arraylen; x++) {
				dataout.d[x] = (double) data[x];
			}
			return 0;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;

}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* arraycode = The type code used by the destination array.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The converted output array.
   Return = 0 if converted OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int convert_unsigned_char(char arraycode, Py_ssize_t arraylen, unsigned char *data, union dataarrays dataout) {

	// array index counter.
	Py_ssize_t x;

	switch(arraycode) {

		// signed char
		case 'b': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > SCHAR_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.b[x] = (signed char) data[x];
			}
			return 0;
		}

		// unsigned char
		case 'B': {
			for(x = 0; x < arraylen; x++) {
				dataout.B[x] = data[x];
			}
			return 0;
		}

		// signed short
		case 'h': {
			for(x = 0; x < arraylen; x++) {
				dataout.h[x] = (signed short) data[x];
			}
			return 0;
		}

		// unsigned short
		case 'H': {
			for(x = 0; x < arraylen; x++) {
				dataout.H[x] = (unsigned short) data[x];
			}
			return 0;
		}

		// signed int
		case 'i': {
			for(x = 0; x < arraylen; x++) {
				dataout.i[x] = (signed int) data[x];
			}
			return 0;
		}

		// unsigned int
		case 'I': {
			for(x = 0; x < arraylen; x++) {
				dataout.I[x] = (unsigned int) data[x];
			}
			return 0;
		}

		// signed long
		case 'l': {
			for(x = 0; x < arraylen; x++) {
				dataout.l[x] = (signed long) data[x];
			}
			return 0;
		}

		// unsigned long
		case 'L': {
			for(x = 0; x < arraylen; x++) {
				dataout.L[x] = (unsigned long) data[x];
			}
			return 0;
		}

		// signed long long
		case 'q': {
			for(x = 0; x < arraylen; x++) {
				dataout.q[x] = (signed long long) data[x];
			}
			return 0;
		}

		// unsigned long long
		case 'Q': {
			for(x = 0; x < arraylen; x++) {
				dataout.Q[x] = (unsigned long long) data[x];
			}
			return 0;
		}

		// float
		case 'f': {
			for(x = 0; x < arraylen; x++) {
				dataout.f[x] = (float) data[x];
			}
			return 0;
		}

		// double
		case 'd': {
			for(x = 0; x < arraylen; x++) {
				dataout.d[x] = (double) data[x];
			}
			return 0;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;

}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* arraycode = The type code used by the destination array.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The converted output array.
   Return = 0 if converted OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int convert_signed_short(char arraycode, Py_ssize_t arraylen, signed short *data, union dataarrays dataout) {

	// array index counter.
	Py_ssize_t x;

	switch(arraycode) {

		// signed char
		case 'b': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > SCHAR_MAX) || (data[x] < SCHAR_MIN)) {
					return ARR_ERR_OVFL;
				}
				dataout.b[x] = (signed char) data[x];
			}
			return 0;
		}

		// unsigned char
		case 'B': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.B[x] = (unsigned char) data[x];
			}
			return 0;
		}

		// signed short
		case 'h': {
			for(x = 0; x < arraylen; x++) {
				dataout.h[x] = data[x];
			}
			return 0;
		}

		// unsigned short
		case 'H': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.H[x] = (unsigned short) data[x];
			}
			return 0;
		}

		// signed int
		case 'i': {
			for(x = 0; x < arraylen; x++) {
				dataout.i[x] = (signed int) data[x];
			}
			return 0;
		}

		// unsigned int
		case 'I': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.I[x] = (unsigned int) data[x];
			}
			return 0;
		}

		// signed long
		case 'l': {
			for(x = 0; x < arraylen; x++) {
				dataout.l[x] = (signed long) data[x];
			}
			return 0;
		}

		// unsigned long
		case 'L': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.L[x] = (unsigned long) data[x];
			}
			return 0;
		}

		// signed long long
		case 'q': {
			for(x = 0; x < arraylen; x++) {
				dataout.q[x] = (signed long long) data[x];
			}
			return 0;
		}

		// unsigned long long
		case 'Q': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.Q[x] = (unsigned long long) data[x];
			}
			return 0;
		}

		// float
		case 'f': {
			for(x = 0; x < arraylen; x++) {
				dataout.f[x] = (float) data[x];
			}
			return 0;
		}

		// double
		case 'd': {
			for(x = 0; x < arraylen; x++) {
				dataout.d[x] = (double) data[x];
			}
			return 0;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;

}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* arraycode = The type code used by the destination array.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The converted output array.
   Return = 0 if converted OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int convert_unsigned_short(char arraycode, Py_ssize_t arraylen, unsigned short *data, union dataarrays dataout) {

	// array index counter.
	Py_ssize_t x;

	switch(arraycode) {

		// signed char
		case 'b': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > SCHAR_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.b[x] = (signed char) data[x];
			}
			return 0;
		}

		// unsigned char
		case 'B': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > UCHAR_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.B[x] = (unsigned char) data[x];
			}
			return 0;
		}

		// signed short
		case 'h': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > SHRT_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.h[x] = (signed short) data[x];
			}
			return 0;
		}

		// unsigned short
		case 'H': {
			for(x = 0; x < arraylen; x++) {
				dataout.H[x] = data[x];
			}
			return 0;
		}

		// signed int
		case 'i': {
			for(x = 0; x < arraylen; x++) {
				dataout.i[x] = (signed int) data[x];
			}
			return 0;
		}

		// unsigned int
		case 'I': {
			for(x = 0; x < arraylen; x++) {
				dataout.I[x] = (unsigned int) data[x];
			}
			return 0;
		}

		// signed long
		case 'l': {
			for(x = 0; x < arraylen; x++) {
				dataout.l[x] = (signed long) data[x];
			}
			return 0;
		}

		// unsigned long
		case 'L': {
			for(x = 0; x < arraylen; x++) {
				dataout.L[x] = (unsigned long) data[x];
			}
			return 0;
		}

		// signed long long
		case 'q': {
			for(x = 0; x < arraylen; x++) {
				dataout.q[x] = (signed long long) data[x];
			}
			return 0;
		}

		// unsigned long long
		case 'Q': {
			for(x = 0; x < arraylen; x++) {
				dataout.Q[x] = (unsigned long long) data[x];
			}
			return 0;
		}

		// float
		case 'f': {
			for(x = 0; x < arraylen; x++) {
				dataout.f[x] = (float) data[x];
			}
			return 0;
		}

		// double
		case 'd': {
			for(x = 0; x < arraylen; x++) {
				dataout.d[x] = (double) data[x];
			}
			return 0;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;

}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* arraycode = The type code used by the destination array.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The converted output array.
   Return = 0 if converted OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int convert_signed_int(char arraycode, Py_ssize_t arraylen, signed int *data, union dataarrays dataout) {

	// array index counter.
	Py_ssize_t x;

	switch(arraycode) {

		// signed char
		case 'b': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > SCHAR_MAX) || (data[x] < SCHAR_MIN)) {
					return ARR_ERR_OVFL;
				}
				dataout.b[x] = (signed char) data[x];
			}
			return 0;
		}

		// unsigned char
		case 'B': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.B[x] = (unsigned char) data[x];
			}
			return 0;
		}

		// signed short
		case 'h': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > SHRT_MAX) || (data[x] < SHRT_MIN)) {
					return ARR_ERR_OVFL;
				}
				dataout.h[x] = (signed short) data[x];
			}
			return 0;
		}

		// unsigned short
		case 'H': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.H[x] = (unsigned short) data[x];
			}
			return 0;
		}

		// signed int
		case 'i': {
			for(x = 0; x < arraylen; x++) {
				dataout.i[x] = data[x];
			}
			return 0;
		}

		// unsigned int
		case 'I': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.I[x] = (unsigned int) data[x];
			}
			return 0;
		}

		// signed long
		case 'l': {
			for(x = 0; x < arraylen; x++) {
				dataout.l[x] = (signed long) data[x];
			}
			return 0;
		}

		// unsigned long
		case 'L': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.L[x] = (unsigned long) data[x];
			}
			return 0;
		}

		// signed long long
		case 'q': {
			for(x = 0; x < arraylen; x++) {
				dataout.q[x] = (signed long long) data[x];
			}
			return 0;
		}

		// unsigned long long
		case 'Q': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.Q[x] = (unsigned long long) data[x];
			}
			return 0;
		}

		// float
		case 'f': {
			for(x = 0; x < arraylen; x++) {
				dataout.f[x] = (float) data[x];
			}
			return 0;
		}

		// double
		case 'd': {
			for(x = 0; x < arraylen; x++) {
				dataout.d[x] = (double) data[x];
			}
			return 0;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;

}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* arraycode = The type code used by the destination array.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The converted output array.
   Return = 0 if converted OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int convert_unsigned_int(char arraycode, Py_ssize_t arraylen, unsigned int *data, union dataarrays dataout) {

	// array index counter.
	Py_ssize_t x;

	switch(arraycode) {

		// signed char
		case 'b': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > SCHAR_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.b[x] = (signed char) data[x];
			}
			return 0;
		}

		// unsigned char
		case 'B': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > UCHAR_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.B[x] = (unsigned char) data[x];
			}
			return 0;
		}

		// signed short
		case 'h': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > SHRT_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.h[x] = (signed short) data[x];
			}
			return 0;
		}

		// unsigned short
		case 'H': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > USHRT_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.H[x] = (unsigned short) data[x];
			}
			return 0;
		}

		// signed int
		case 'i': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > INT_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.i[x] = (signed int) data[x];
			}
			return 0;
		}

		// unsigned int
		case 'I': {
			for(x = 0; x < arraylen; x++) {
				dataout.I[x] = data[x];
			}
			return 0;
		}

		// signed long
		case 'l': {
			for(x = 0; x < arraylen; x++) {
				dataout.l[x] = (signed long) data[x];
			}
			return 0;
		}

		// unsigned long
		case 'L': {
			for(x = 0; x < arraylen; x++) {
				dataout.L[x] = (unsigned long) data[x];
			}
			return 0;
		}

		// signed long long
		case 'q': {
			for(x = 0; x < arraylen; x++) {
				dataout.q[x] = (signed long long) data[x];
			}
			return 0;
		}

		// unsigned long long
		case 'Q': {
			for(x = 0; x < arraylen; x++) {
				dataout.Q[x] = (unsigned long long) data[x];
			}
			return 0;
		}

		// float
		case 'f': {
			for(x = 0; x < arraylen; x++) {
				dataout.f[x] = (float) data[x];
			}
			return 0;
		}

		// double
		case 'd': {
			for(x = 0; x < arraylen; x++) {
				dataout.d[x] = (double) data[x];
			}
			return 0;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;

}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* arraycode = The type code used by the destination array.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The converted output array.
   Return = 0 if converted OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int convert_signed_long(char arraycode, Py_ssize_t arraylen, signed long *data, union dataarrays dataout) {

	// array index counter.
	Py_ssize_t x;

	switch(arraycode) {

		// signed char
		case 'b': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > SCHAR_MAX) || (data[x] < SCHAR_MIN)) {
					return ARR_ERR_OVFL;
				}
				dataout.b[x] = (signed char) data[x];
			}
			return 0;
		}

		// unsigned char
		case 'B': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.B[x] = (unsigned char) data[x];
			}
			return 0;
		}

		// signed short
		case 'h': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > SHRT_MAX) || (data[x] < SHRT_MIN)) {
					return ARR_ERR_OVFL;
				}
				dataout.h[x] = (signed short) data[x];
			}
			return 0;
		}

		// unsigned short
		case 'H': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.H[x] = (unsigned short) data[x];
			}
			return 0;
		}

		// signed int
		case 'i': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > INT_MAX) || (data[x] < INT_MIN)) {
					return ARR_ERR_OVFL;
				}
				dataout.i[x] = (signed int) data[x];
			}
			return 0;
		}

		// unsigned int
		case 'I': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.I[x] = (unsigned int) data[x];
			}
			return 0;
		}

		// signed long
		case 'l': {
			for(x = 0; x < arraylen; x++) {
				dataout.l[x] = data[x];
			}
			return 0;
		}

		// unsigned long
		case 'L': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.L[x] = (unsigned long) data[x];
			}
			return 0;
		}

		// signed long long
		case 'q': {
			for(x = 0; x < arraylen; x++) {
				dataout.q[x] = (signed long long) data[x];
			}
			return 0;
		}

		// unsigned long long
		case 'Q': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.Q[x] = (unsigned long long) data[x];
			}
			return 0;
		}

		// float
		case 'f': {
			for(x = 0; x < arraylen; x++) {
				dataout.f[x] = (float) data[x];
			}
			return 0;
		}

		// double
		case 'd': {
			for(x = 0; x < arraylen; x++) {
				dataout.d[x] = (double) data[x];
			}
			return 0;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;

}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* arraycode = The type code used by the destination array.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The converted output array.
   Return = 0 if converted OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int convert_unsigned_long(char arraycode, Py_ssize_t arraylen, unsigned long *data, union dataarrays dataout) {

	// array index counter.
	Py_ssize_t x;

	switch(arraycode) {

		// signed char
		case 'b': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > SCHAR_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.b[x] = (signed char) data[x];
			}
			return 0;
		}

		// unsigned char
		case 'B': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > UCHAR_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.B[x] = (unsigned char) data[x];
			}
			return 0;
		}

		// signed short
		case 'h': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > SHRT_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.h[x] = (signed short) data[x];
			}
			return 0;
		}

		// unsigned short
		case 'H': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > USHRT_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.H[x] = (unsigned short) data[x];
			}
			return 0;
		}

		// signed int
		case 'i': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > INT_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.i[x] = (signed int) data[x];
			}
			return 0;
		}

		// unsigned int
		case 'I': {
			for(x = 0; x < arraylen; x++) {
				dataout.I[x] = (unsigned int) data[x];
			}
			return 0;
		}

		// signed long
		case 'l': {
			for(x = 0; x < arraylen; x++) {
				dataout.l[x] = (signed long) data[x];
			}
			return 0;
		}

		// unsigned long
		case 'L': {
			for(x = 0; x < arraylen; x++) {
				dataout.L[x] = data[x];
			}
			return 0;
		}

		// signed long long
		case 'q': {
			for(x = 0; x < arraylen; x++) {
				dataout.q[x] = (signed long long) data[x];
			}
			return 0;
		}

		// unsigned long long
		case 'Q': {
			for(x = 0; x < arraylen; x++) {
				dataout.Q[x] = (unsigned long long) data[x];
			}
			return 0;
		}

		// float
		case 'f': {
			for(x = 0; x < arraylen; x++) {
				dataout.f[x] = (float) data[x];
			}
			return 0;
		}

		// double
		case 'd': {
			for(x = 0; x < arraylen; x++) {
				dataout.d[x] = (double) data[x];
			}
			return 0;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;

}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* arraycode = The type code used by the destination array.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The converted output array.
   Return = 0 if converted OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int convert_signed_long_long(char arraycode, Py_ssize_t arraylen, signed long long *data, union dataarrays dataout) {

	// array index counter.
	Py_ssize_t x;

	switch(arraycode) {

		// signed char
		case 'b': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > SCHAR_MAX) || (data[x] < SCHAR_MIN)) {
					return ARR_ERR_OVFL;
				}
				dataout.b[x] = (signed char) data[x];
			}
			return 0;
		}

		// unsigned char
		case 'B': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.B[x] = (unsigned char) data[x];
			}
			return 0;
		}

		// signed short
		case 'h': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > SHRT_MAX) || (data[x] < SHRT_MIN)) {
					return ARR_ERR_OVFL;
				}
				dataout.h[x] = (signed short) data[x];
			}
			return 0;
		}

		// unsigned short
		case 'H': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.H[x] = (unsigned short) data[x];
			}
			return 0;
		}

		// signed int
		case 'i': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > INT_MAX) || (data[x] < INT_MIN)) {
					return ARR_ERR_OVFL;
				}
				dataout.i[x] = (signed int) data[x];
			}
			return 0;
		}

		// unsigned int
		case 'I': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.I[x] = (unsigned int) data[x];
			}
			return 0;
		}

		// signed long
		case 'l': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > LONG_MAX) || (data[x] < LONG_MIN)) {
					return ARR_ERR_OVFL;
				}
				dataout.l[x] = (signed long) data[x];
			}
			return 0;
		}

		// unsigned long
		case 'L': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.L[x] = (unsigned long) data[x];
			}
			return 0;
		}

		// signed long long
		case 'q': {
			for(x = 0; x < arraylen; x++) {
				dataout.q[x] = data[x];
			}
			return 0;
		}

		// unsigned long long
		case 'Q': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] < 0) {
					return ARR_ERR_OVFL;
				}
				dataout.Q[x] = (unsigned long long) data[x];
			}
			return 0;
		}

		// float
		case 'f': {
			for(x = 0; x < arraylen; x++) {
				dataout.f[x] = (float) data[x];
			}
			return 0;
		}

		// double
		case 'd': {
			for(x = 0; x < arraylen; x++) {
				dataout.d[x] = (double) data[x];
			}
			return 0;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;

}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* arraycode = The type code used by the destination array.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The converted output array.
   Return = 0 if converted OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int convert_unsigned_long_long(char arraycode, Py_ssize_t arraylen, unsigned long long *data, union dataarrays dataout) {

	// array index counter.
	Py_ssize_t x;

	switch(arraycode) {

		// signed char
		case 'b': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > SCHAR_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.b[x] = (signed char) data[x];
			}
			return 0;
		}

		// unsigned char
		case 'B': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > UCHAR_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.B[x] = (unsigned char) data[x];
			}
			return 0;
		}

		// signed short
		case 'h': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > SHRT_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.h[x] = (signed short) data[x];
			}
			return 0;
		}

		// unsigned short
		case 'H': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > USHRT_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.H[x] = (unsigned short) data[x];
			}
			return 0;
		}

		// signed int
		case 'i': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > INT_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.i[x] = (signed int) data[x];
			}
			return 0;
		}

		// unsigned int
		case 'I': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > UINT_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.I[x] = (unsigned int) data[x];
			}
			return 0;
		}

		// signed long
		case 'l': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > LONG_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.l[x] = (signed long) data[x];
			}
			return 0;
		}

		// unsigned long
		case 'L': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > ULONG_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.L[x] = (unsigned long) data[x];
			}
			return 0;
		}

		// signed long long
		case 'q': {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > LLONG_MAX) {
					return ARR_ERR_OVFL;
				}
				dataout.q[x] = (signed long long) data[x];
			}
			return 0;
		}

		// unsigned long long
		case 'Q': {
			for(x = 0; x < arraylen; x++) {
				dataout.Q[x] = data[x];
			}
			return 0;
		}

		// float
		case 'f': {
			for(x = 0; x < arraylen; x++) {
				dataout.f[x] = (float) data[x];
			}
			return 0;
		}

		// double
		case 'd': {
			for(x = 0; x < arraylen; x++) {
				dataout.d[x] = (double) data[x];
			}
			return 0;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;

}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* arraycode = The type code used by the destination array.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The converted output array.
   Return = 0 if converted OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int convert_float(char arraycode, Py_ssize_t arraylen, float *data, union dataarrays dataout) {

	// array index counter.
	Py_ssize_t x;

	switch(arraycode) {

		// signed char
		case 'b': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > SCHAR_MAX) || (data[x] < SCHAR_MIN) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.b[x] = (signed char) data[x];
			}
			return 0;
		}

		// unsigned char
		case 'B': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > UCHAR_MAX) || (data[x] < 0) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.B[x] = (unsigned char) data[x];
			}
			return 0;
		}

		// signed short
		case 'h': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > SHRT_MAX) || (data[x] < SHRT_MIN) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.h[x] = (signed short) data[x];
			}
			return 0;
		}

		// unsigned short
		case 'H': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > USHRT_MAX) || (data[x] < 0) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.H[x] = (unsigned short) data[x];
			}
			return 0;
		}

		// signed int
		case 'i': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > INT_MAX_GUARD_F) || (data[x] < INT_MIN_GUARD_F) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.i[x] = (signed int) data[x];
			}
			return 0;
		}

		// unsigned int
		case 'I': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > UINT_MAX_GUARD_F) || (data[x] < 0) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.I[x] = (unsigned int) data[x];
			}
			return 0;
		}

		// signed long
		case 'l': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > LONG_MAX_GUARD_F) || (data[x] < LONG_MIN_GUARD_F) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.l[x] = (signed long) data[x];
			}
			return 0;
		}

		// unsigned long
		case 'L': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > ULONG_MAX_GUARD_F) || (data[x] < 0) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.L[x] = (unsigned long) data[x];
			}
			return 0;
		}

		// signed long long
		case 'q': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > LLONG_MAX_GUARD_F) || (data[x] < LLONG_MIN_GUARD_F) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.q[x] = (signed long long) data[x];
			}
			return 0;
		}

		// unsigned long long
		case 'Q': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > ULLONG_MAX_GUARD_F) || (data[x] < 0) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.Q[x] = (unsigned long long) data[x];
			}
			return 0;
		}

		// float
		case 'f': {
			for(x = 0; x < arraylen; x++) {
				dataout.f[x] = data[x];
			}
			return 0;
		}

		// double
		case 'd': {
			for(x = 0; x < arraylen; x++) {
				dataout.d[x] = (double) data[x];
			}
			return 0;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;

}
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* arraycode = The type code used by the destination array.
   arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The converted output array.
   Return = 0 if converted OK, ARR_ERR_OVFL if the data was out of range.
*/
signed int convert_double(char arraycode, Py_ssize_t arraylen, double *data, union dataarrays dataout) {

	// array index counter.
	Py_ssize_t x;

	switch(arraycode) {

		// signed char
		case 'b': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > SCHAR_MAX) || (data[x] < SCHAR_MIN) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.b[x] = (signed char) data[x];
			}
			return 0;
		}

		// unsigned char
		case 'B': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > UCHAR_MAX) || (data[x] < 0) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.B[x] = (unsigned char) data[x];
			}
			return 0;
		}

		// signed short
		case 'h': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > SHRT_MAX) || (data[x] < SHRT_MIN) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.h[x] = (signed short) data[x];
			}
			return 0;
		}

		// unsigned short
		case 'H': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > USHRT_MAX) || (data[x] < 0) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.H[x] = (unsigned short) data[x];
			}
			return 0;
		}

		// signed int
		case 'i': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > INT_MAX) || (data[x] < INT_MIN) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.i[x] = (signed int) data[x];
			}
			return 0;
		}

		// unsigned int
		case 'I': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > UINT_MAX) || (data[x] < 0) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.I[x] = (unsigned int) data[x];
			}
			return 0;
		}

		// signed long
		case 'l': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > LONG_MAX_GUARD_D) || (data[x] < LONG_MIN_GUARD_D) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.l[x] = (signed long) data[x];
			}
			return 0;
		}

		// unsigned long
		case 'L': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > ULONG_MAX_GUARD_D) || (data[x] < 0) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.L[x] = (unsigned long) data[x];
			}
			return 0;
		}

		// signed long long
		case 'q': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > LLONG_MAX_GUARD_D) || (data[x] < LLONG_MIN_GUARD_D) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.q[x] = (signed long long) data[x];
			}
			return 0;
		}

		// unsigned long long
		case 'Q': {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] > ULLONG_MAX_GUARD_D) || (data[x] < 0) || (!isfinite(data[x]))) {
					return ARR_ERR_OVFL;
				}
				dataout.Q[x] = (unsigned long long) data[x];
			}
			return 0;
		}

		// float
		case 'f': {
			for(x = 0; x < arraylen; x++) {
				// NaN, inf, and -inf must be passed through.
				if (isfinite(data[x]) && ((data[x] > FLT_MAX) || (data[x] < -FLT_MAX))) {
					return ARR_ERR_OVFL;
				}
				dataout.f[x] = (float) data[x];
			}
			return 0;
		}

		// double
		case 'd': {
			for(x = 0; x < arraylen; x++) {
				dataout.d[x] = data[x];
			}
			return 0;
		}
	}

	// The operation code is unknown.
	return ARR_ERR_INVALIDOP;

}
/*--------------------------------------------------------------------------- */
