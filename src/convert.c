//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   convert.c
// Purpose:  Convert arrays between data types.
// Language: C
// Date:     08-May-2014
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

#include <limits.h>
#include <float.h>

#include "arrayfunc.h"
#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */


// Provide a struct for returning data from parsing Python arguments.
struct args_param {
	char array1type;
	char param1type;
	char error;
};


// The list of keyword arguments. All argument must be listed, whether we 
// intend to use them for keywords or not. 
static char *kwlist[] = {"data", "dataout", "maxlen", NULL};

/*--------------------------------------------------------------------------- */

// Auto-generated code goes below.

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
// MS VC 2010 seems to have bugs when converting large floating point values 
// to large unsigned long long integers. Values larger than 2**63 do not covert
// correctly. This problem does not occur with GCC. 
#ifdef _MSC_VER
	return ARR_ERR_PLATFORM;
#endif
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
// MS VC 2010 seems to have bugs when converting large floating point values 
// to large unsigned long long integers. Values larger than 2**63 do not covert
// correctly. This problem does not occur with GCC. 
#ifdef _MSC_VER
	return ARR_ERR_PLATFORM;
#endif
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


/*--------------------------------------------------------------------------- */


/* The wrapper to the underlying C function */
static PyObject *py_convert(PyObject *self, PyObject *args, PyObject *keywds) {

	// The arrays of data we work on. 
	union dataarrays data, dataout;

	// The buffers are arrays of bytes.
	Py_buffer datapy, dataoutpy;

	// The length of the data array.
	Py_ssize_t databufflength, dataoutbufflength;

	// The arrays as objects, so we can examine their types.
	PyObject *dataobj, *dataoutobj;

	// Codes indicating the types of arrays.
	char itemcode, arraycode;

	// How long the array is.
	Py_ssize_t arraylength, arrayoutlength;
	// Number of elements to work on. If zero or less, ignore this parameter.
	Py_ssize_t arraymaxlen = 0;

	struct arrayparamstypes arr1type = {0, 0, ' '};
	struct arrayparamstypes arr2type = {0, 0, ' '};

	// The error code returned by the function.
	signed int resultcode;

	// -------------------------------------------------------------------------



	/* Import the raw objects. */
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "OO|l:convert", kwlist, 
			&dataobj, &dataoutobj, &arraymaxlen)) {
		ErrMsgParameterError();
		return NULL;
	}


	// Test if the first parameter is an array or bytes.
	arr1type = paramarraytype(dataobj);
	if (!arr1type.isarray) {
		ErrMsgArrayorBytesExpected();
		return NULL;
	} else {
		// Get the array code type character.
		itemcode = arr1type.arraycode;
	}


	// Test if the second parameter is an array or bytes.
	arr2type = paramarraytype(dataoutobj);
	if (!arr2type.isarray) {
		ErrMsgArrayorBytesExpected();
		return NULL;
	} else {
		// Get the array code type character.
		arraycode = arr2type.arraycode;
	}


	// Now we will fetch the actual data.
	if (!PyArg_ParseTupleAndKeywords(args, keywds, "y*y*|l:convert", kwlist, 
			&datapy, &dataoutpy, &arraymaxlen)) {
		return NULL;
	}


	// Assign the buffer to a union which lets us get at them as typed data.
	data.buf = datapy.buf;
	dataout.buf = dataoutpy.buf;


	// The length of the data array.
	databufflength = datapy.len;
	dataoutbufflength = dataoutpy.len;
	arraylength = calcarraylength(itemcode, databufflength);
	if (arraylength < 1) {
		PyBuffer_Release(&datapy);
		PyBuffer_Release(&dataoutpy);
		ErrMsgArrayLengthErr();
		return NULL;
	}

	// Get the length of the output array. We need to compare the number of
	// elements rather than just the number of bytes, because the two
	// array types may not be the same. 
	arrayoutlength = calcarraylength(arraycode, dataoutbufflength);

	// Check to make sure the input and output arrays are of equal length.
	if (arraylength != arrayoutlength) {
		PyBuffer_Release(&datapy);
		PyBuffer_Release(&dataoutpy);
		ErrMsgArrayLengthMismatch();
		return NULL;
	}


	// Adjust the length of array being operated on, if necessary.
	arraylength = adjustarraymaxlen(arraylength, arraymaxlen);



	/* Call the C function */
	switch(itemcode) {
		// signed char
		case 'b' : {
			resultcode = convert_signed_char(arraycode, arraylength, data.b, dataout);
			break;
		}
		// unsigned char
		case 'B' : {
			resultcode = convert_unsigned_char(arraycode, arraylength, data.B, dataout);
			break;
		}
		// signed short
		case 'h' : {
			resultcode = convert_signed_short(arraycode, arraylength, data.h, dataout);
			break;
		}
		// unsigned short
		case 'H' : {
			resultcode = convert_unsigned_short(arraycode, arraylength, data.H, dataout);
			break;
		}
		// signed int
		case 'i' : {
			resultcode = convert_signed_int(arraycode, arraylength, data.i, dataout);
			break;
		}
		// unsigned int
		case 'I' : {
			resultcode = convert_unsigned_int(arraycode, arraylength, data.I, dataout);
			break;
		}
		// signed long
		case 'l' : {
			resultcode = convert_signed_long(arraycode, arraylength, data.l, dataout);
			break;
		}
		// unsigned long
		case 'L' : {
			resultcode = convert_unsigned_long(arraycode, arraylength, data.L, dataout);
			break;
		}
		// signed long long
		case 'q' : {
			resultcode = convert_signed_long_long(arraycode, arraylength, data.q, dataout);
			break;
		}
		// unsigned long long
		case 'Q' : {
			resultcode = convert_unsigned_long_long(arraycode, arraylength, data.Q, dataout);
			break;
		}
		// float
		case 'f' : {
			resultcode = convert_float(arraycode, arraylength, data.f, dataout);
			break;
		}
		// double
		case 'd' : {
			resultcode = convert_double(arraycode, arraylength, data.d, dataout);
			break;
		}
		// We don't know this code.
		default: {
			// Release the buffers. 
			PyBuffer_Release(&datapy);
			PyBuffer_Release(&dataoutpy);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}


	// Release the buffers. 
	PyBuffer_Release(&datapy);
	PyBuffer_Release(&dataoutpy);


	// Signal the errors.
	switch (resultcode) {
		case ARR_ERR_INVALIDOP : {
			ErrMsgConversionNotValidforthisType();
			return NULL;
		}
		case ARR_ERR_OVFL : {
			ErrMsgArithOverflowCalc();
			return NULL;
		}
		case ARR_ERR_VALUE_ERR : {
			ErrMsgNaNError();
			return NULL;
		}
		case ARR_ERR_PLATFORM : {
			ErrMsgOperatorNotValidforthisPlatform();
			return NULL;
		}
	}


	// Return NONE.
	Py_RETURN_NONE;


}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(convert__doc__,
"Convert arrays between data types. The data will be converted into the \n\
form required by the output array. If any values in the input array are \n\
outside the range of the output array type, an exception will be \n\
raised. When floating point values are converted to integers, the value \n\
will be truncated. \n\
\n\
convert(inparray, outparray)\n\
convert(inparray, outparray, maxlen=y)\n\
\n\
* inparray - The input data array to be examined.\n\
* outparray - The output array.\n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored.");


/* A list of all the methods defined by this module. 
 "convert" is the name seen inside of Python. 
 "py_convert" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef convert_methods[] = {
	{"convert",  (PyCFunction) py_convert, METH_VARARGS | METH_KEYWORDS, convert__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef convertmodule = {
    PyModuleDef_HEAD_INIT,
    "convert",
    NULL,
    -1,
    convert_methods
};

PyMODINIT_FUNC PyInit_convert(void)
{
    return PyModule_Create(&convertmodule);
};

/*--------------------------------------------------------------------------- */
