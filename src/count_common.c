//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   count_common.c
// Purpose:  Fill an array with a series of values.
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
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_signed_char(Py_ssize_t arraylen, signed char *data, signed char startvalue, signed char stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	signed char increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char startvalue, unsigned char stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned char increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_signed_short(Py_ssize_t arraylen, signed short *data, signed short startvalue, signed short stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	signed short increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short startvalue, unsigned short stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned short increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_signed_int(Py_ssize_t arraylen, signed int *data, signed int startvalue, signed int stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	signed int increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int startvalue, unsigned int stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned int increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_signed_long(Py_ssize_t arraylen, signed long *data, signed long startvalue, signed long stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long startvalue, unsigned long stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long startvalue, signed long long stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	signed long long increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long startvalue, unsigned long long stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	unsigned long long increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_float(Py_ssize_t arraylen, float *data, float startvalue, float stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	float increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}

/*--------------------------------------------------------------------------- */
/* * arraylen = The length of the data arrays.
   * data = The input data array.
   * startvalue = The value to start filling the data array.
   * stepvalue = The increment value.
   * countdown = If true, count down.
*/
void count_double(Py_ssize_t arraylen, double *data, double startvalue, double stepvalue, int countdown) { 

	// array index counter. 
	Py_ssize_t x; 
	double increment;

	increment = startvalue;

	if (countdown) {
		// Count down.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment - stepvalue;
		}
	} else {
		// Count up.
		for(x = 0; x < arraylen; x++) {
			data[x] = increment;
			increment = increment + stepvalue;
		}
	}

}
