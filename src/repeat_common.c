//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   repeat_common.c
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

/*--------------------------------------------------------------------------- */
// This must be defined before "Python.h" in order for the pointers in the
// argument parsing functions to work properly. 
#define PY_SSIZE_T_CLEAN

#include "Python.h"

#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// Auto generated code goes below.

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_signed_char(Py_ssize_t arraylen, signed char *data, signed char fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_signed_short(Py_ssize_t arraylen, signed short *data, signed short fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_signed_int(Py_ssize_t arraylen, signed int *data, signed int fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_signed_long(Py_ssize_t arraylen, signed long *data, signed long fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_float(Py_ssize_t arraylen, float *data, float fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}

/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   fillvalue = The value to fill the data array.
*/
void repeat_double(Py_ssize_t arraylen, double *data, double fillvalue) { 

	// array index counter. 
	Py_ssize_t x; 

	for(x = 0; x < arraylen; x++) {
		data[x] = fillvalue;
	}
}
