//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   add.c
// Purpose:  Calculate the add of values in an array.
// Language: C
// Date:     15-Nov-2017.
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

#include <limits.h>
#include <math.h>

#include "arrayerrs.h"

#include "arrayparams_base.h"

#include "arrayparams_two.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int add_signed_char_1(Py_ssize_t arraylen, signed char *data1, signed char param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed char ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			return ARR_NO_ERR;
		}
		if (param > 0) {
			ovtmp = SCHAR_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = SCHAR_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] < ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int add_signed_char_2(Py_ssize_t arraylen, signed char *data1, signed char param, signed char *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed char ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data3[x] = data1[x]; 
			}
		}
		if (param > 0) {
			ovtmp = SCHAR_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = SCHAR_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] < ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int add_signed_char_3(Py_ssize_t arraylen, signed char param, signed char *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed char ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			return ARR_NO_ERR;
		}
		if (param > 0) {
			ovtmp = SCHAR_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = data2[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = SCHAR_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = data2[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int add_signed_char_4(Py_ssize_t arraylen, signed char param, signed char *data2, signed char *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed char ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data3[x] = data2[x]; 
			}
		}
		if (param > 0) {
			ovtmp = SCHAR_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data2[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = SCHAR_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data2[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int add_signed_char_5(Py_ssize_t arraylen, signed char *data1, signed char *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && (data1[x] > (SCHAR_MAX - data2[x]))) {return ARR_ERR_OVFL;}
			if ((data2[x] < 0) && (data1[x] < (SCHAR_MIN - data2[x]))) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int add_signed_char_6(Py_ssize_t arraylen, signed char *data1, signed char *data2, signed char *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && (data1[x] > (SCHAR_MAX - data2[x]))) {return ARR_ERR_OVFL;}
			if ((data2[x] < 0) && (data1[x] < (SCHAR_MIN - data2[x]))) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int add_unsigned_char_1(Py_ssize_t arraylen, unsigned char *data1, unsigned char param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned char ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		ovtmp = UCHAR_MAX - param;
		for(x = 0; x < arraylen; x++) {
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] + param;
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int add_unsigned_char_2(Py_ssize_t arraylen, unsigned char *data1, unsigned char param, unsigned char *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned char ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		ovtmp = UCHAR_MAX - param;
		for(x = 0; x < arraylen; x++) {
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] + param;
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int add_unsigned_char_3(Py_ssize_t arraylen, unsigned char param, unsigned char *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned char ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = UCHAR_MAX - data2[x];
			if (param > ovtmp) {return ARR_ERR_OVFL;}
			data2[x] = param + data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int add_unsigned_char_4(Py_ssize_t arraylen, unsigned char param, unsigned char *data2, unsigned char *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned char ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = UCHAR_MAX - data2[x];
			if (param > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = param + data2[x];
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int add_unsigned_char_5(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned char ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = UCHAR_MAX - data2[x];
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int add_unsigned_char_6(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2, unsigned char *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned char ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = UCHAR_MAX - data2[x];
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int add_signed_short_1(Py_ssize_t arraylen, signed short *data1, signed short param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed short ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			return ARR_NO_ERR;
		}
		if (param > 0) {
			ovtmp = SHRT_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = SHRT_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] < ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int add_signed_short_2(Py_ssize_t arraylen, signed short *data1, signed short param, signed short *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed short ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data3[x] = data1[x]; 
			}
		}
		if (param > 0) {
			ovtmp = SHRT_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = SHRT_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] < ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int add_signed_short_3(Py_ssize_t arraylen, signed short param, signed short *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed short ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			return ARR_NO_ERR;
		}
		if (param > 0) {
			ovtmp = SHRT_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = data2[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = SHRT_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = data2[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int add_signed_short_4(Py_ssize_t arraylen, signed short param, signed short *data2, signed short *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed short ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data3[x] = data2[x]; 
			}
		}
		if (param > 0) {
			ovtmp = SHRT_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data2[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = SHRT_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data2[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int add_signed_short_5(Py_ssize_t arraylen, signed short *data1, signed short *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && (data1[x] > (SHRT_MAX - data2[x]))) {return ARR_ERR_OVFL;}
			if ((data2[x] < 0) && (data1[x] < (SHRT_MIN - data2[x]))) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int add_signed_short_6(Py_ssize_t arraylen, signed short *data1, signed short *data2, signed short *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && (data1[x] > (SHRT_MAX - data2[x]))) {return ARR_ERR_OVFL;}
			if ((data2[x] < 0) && (data1[x] < (SHRT_MIN - data2[x]))) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int add_unsigned_short_1(Py_ssize_t arraylen, unsigned short *data1, unsigned short param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned short ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		ovtmp = USHRT_MAX - param;
		for(x = 0; x < arraylen; x++) {
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] + param;
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int add_unsigned_short_2(Py_ssize_t arraylen, unsigned short *data1, unsigned short param, unsigned short *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned short ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		ovtmp = USHRT_MAX - param;
		for(x = 0; x < arraylen; x++) {
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] + param;
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int add_unsigned_short_3(Py_ssize_t arraylen, unsigned short param, unsigned short *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned short ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = USHRT_MAX - data2[x];
			if (param > ovtmp) {return ARR_ERR_OVFL;}
			data2[x] = param + data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int add_unsigned_short_4(Py_ssize_t arraylen, unsigned short param, unsigned short *data2, unsigned short *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned short ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = USHRT_MAX - data2[x];
			if (param > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = param + data2[x];
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int add_unsigned_short_5(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned short ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = USHRT_MAX - data2[x];
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int add_unsigned_short_6(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2, unsigned short *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned short ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = USHRT_MAX - data2[x];
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int add_signed_int_1(Py_ssize_t arraylen, signed int *data1, signed int param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed int ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			return ARR_NO_ERR;
		}
		if (param > 0) {
			ovtmp = INT_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = INT_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] < ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int add_signed_int_2(Py_ssize_t arraylen, signed int *data1, signed int param, signed int *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed int ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data3[x] = data1[x]; 
			}
		}
		if (param > 0) {
			ovtmp = INT_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = INT_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] < ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int add_signed_int_3(Py_ssize_t arraylen, signed int param, signed int *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed int ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			return ARR_NO_ERR;
		}
		if (param > 0) {
			ovtmp = INT_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = data2[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = INT_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = data2[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int add_signed_int_4(Py_ssize_t arraylen, signed int param, signed int *data2, signed int *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed int ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data3[x] = data2[x]; 
			}
		}
		if (param > 0) {
			ovtmp = INT_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data2[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = INT_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data2[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int add_signed_int_5(Py_ssize_t arraylen, signed int *data1, signed int *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && (data1[x] > (INT_MAX - data2[x]))) {return ARR_ERR_OVFL;}
			if ((data2[x] < 0) && (data1[x] < (INT_MIN - data2[x]))) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int add_signed_int_6(Py_ssize_t arraylen, signed int *data1, signed int *data2, signed int *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && (data1[x] > (INT_MAX - data2[x]))) {return ARR_ERR_OVFL;}
			if ((data2[x] < 0) && (data1[x] < (INT_MIN - data2[x]))) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int add_unsigned_int_1(Py_ssize_t arraylen, unsigned int *data1, unsigned int param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned int ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		ovtmp = UINT_MAX - param;
		for(x = 0; x < arraylen; x++) {
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] + param;
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int add_unsigned_int_2(Py_ssize_t arraylen, unsigned int *data1, unsigned int param, unsigned int *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned int ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		ovtmp = UINT_MAX - param;
		for(x = 0; x < arraylen; x++) {
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] + param;
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int add_unsigned_int_3(Py_ssize_t arraylen, unsigned int param, unsigned int *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned int ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = UINT_MAX - data2[x];
			if (param > ovtmp) {return ARR_ERR_OVFL;}
			data2[x] = param + data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int add_unsigned_int_4(Py_ssize_t arraylen, unsigned int param, unsigned int *data2, unsigned int *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned int ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = UINT_MAX - data2[x];
			if (param > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = param + data2[x];
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int add_unsigned_int_5(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned int ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = UINT_MAX - data2[x];
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int add_unsigned_int_6(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2, unsigned int *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned int ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = UINT_MAX - data2[x];
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int add_signed_long_1(Py_ssize_t arraylen, signed long *data1, signed long param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			return ARR_NO_ERR;
		}
		if (param > 0) {
			ovtmp = LONG_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = LONG_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] < ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int add_signed_long_2(Py_ssize_t arraylen, signed long *data1, signed long param, signed long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data3[x] = data1[x]; 
			}
		}
		if (param > 0) {
			ovtmp = LONG_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = LONG_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] < ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int add_signed_long_3(Py_ssize_t arraylen, signed long param, signed long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			return ARR_NO_ERR;
		}
		if (param > 0) {
			ovtmp = LONG_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = data2[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = LONG_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = data2[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int add_signed_long_4(Py_ssize_t arraylen, signed long param, signed long *data2, signed long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data3[x] = data2[x]; 
			}
		}
		if (param > 0) {
			ovtmp = LONG_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data2[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = LONG_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data2[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int add_signed_long_5(Py_ssize_t arraylen, signed long *data1, signed long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && (data1[x] > (LONG_MAX - data2[x]))) {return ARR_ERR_OVFL;}
			if ((data2[x] < 0) && (data1[x] < (LONG_MIN - data2[x]))) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int add_signed_long_6(Py_ssize_t arraylen, signed long *data1, signed long *data2, signed long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && (data1[x] > (LONG_MAX - data2[x]))) {return ARR_ERR_OVFL;}
			if ((data2[x] < 0) && (data1[x] < (LONG_MIN - data2[x]))) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int add_unsigned_long_1(Py_ssize_t arraylen, unsigned long *data1, unsigned long param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		ovtmp = ULONG_MAX - param;
		for(x = 0; x < arraylen; x++) {
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] + param;
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int add_unsigned_long_2(Py_ssize_t arraylen, unsigned long *data1, unsigned long param, unsigned long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		ovtmp = ULONG_MAX - param;
		for(x = 0; x < arraylen; x++) {
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] + param;
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int add_unsigned_long_3(Py_ssize_t arraylen, unsigned long param, unsigned long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = ULONG_MAX - data2[x];
			if (param > ovtmp) {return ARR_ERR_OVFL;}
			data2[x] = param + data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int add_unsigned_long_4(Py_ssize_t arraylen, unsigned long param, unsigned long *data2, unsigned long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = ULONG_MAX - data2[x];
			if (param > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = param + data2[x];
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int add_unsigned_long_5(Py_ssize_t arraylen, unsigned long *data1, unsigned long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = ULONG_MAX - data2[x];
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int add_unsigned_long_6(Py_ssize_t arraylen, unsigned long *data1, unsigned long *data2, unsigned long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = ULONG_MAX - data2[x];
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int add_signed_long_long_1(Py_ssize_t arraylen, signed long long *data1, signed long long param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			return ARR_NO_ERR;
		}
		if (param > 0) {
			ovtmp = LLONG_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = LLONG_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] < ovtmp) {return ARR_ERR_OVFL;}
				data1[x] = data1[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int add_signed_long_long_2(Py_ssize_t arraylen, signed long long *data1, signed long long param, signed long long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data3[x] = data1[x]; 
			}
		}
		if (param > 0) {
			ovtmp = LLONG_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = LLONG_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data1[x] < ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data1[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int add_signed_long_long_3(Py_ssize_t arraylen, signed long long param, signed long long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		// If the parameter is zero, we can take a shortcut.
		if (param == 0) {
			return ARR_NO_ERR;
		}
		if (param > 0) {
			ovtmp = LLONG_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = data2[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = LLONG_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < ovtmp) {return ARR_ERR_OVFL;}
				data2[x] = data2[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int add_signed_long_long_4(Py_ssize_t arraylen, signed long long param, signed long long *data2, signed long long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		if (param == 0) {
			for(x = 0; x < arraylen; x++) {
				data3[x] = data2[x]; 
			}
		}
		if (param > 0) {
			ovtmp = LLONG_MAX - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] > ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data2[x] + param; 
			}
		}
		if (param < 0) {
			ovtmp = LLONG_MIN - param;
			for(x = 0; x < arraylen; x++) {
				if (data2[x] < ovtmp) {return ARR_ERR_OVFL;}
				data3[x] = data2[x] + param; 
			}
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int add_signed_long_long_5(Py_ssize_t arraylen, signed long long *data1, signed long long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && (data1[x] > (LLONG_MAX - data2[x]))) {return ARR_ERR_OVFL;}
			if ((data2[x] < 0) && (data1[x] < (LLONG_MIN - data2[x]))) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int add_signed_long_long_6(Py_ssize_t arraylen, signed long long *data1, signed long long *data2, signed long long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			if ((data2[x] > 0) && (data1[x] > (LLONG_MAX - data2[x]))) {return ARR_ERR_OVFL;}
			if ((data2[x] < 0) && (data1[x] < (LLONG_MIN - data2[x]))) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int add_unsigned_long_long_1(Py_ssize_t arraylen, unsigned long long *data1, unsigned long long param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned long long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		ovtmp = ULLONG_MAX - param;
		for(x = 0; x < arraylen; x++) {
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] + param;
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int add_unsigned_long_long_2(Py_ssize_t arraylen, unsigned long long *data1, unsigned long long param, unsigned long long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned long long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		ovtmp = ULLONG_MAX - param;
		for(x = 0; x < arraylen; x++) {
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] + param;
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int add_unsigned_long_long_3(Py_ssize_t arraylen, unsigned long long param, unsigned long long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned long long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = ULLONG_MAX - data2[x];
			if (param > ovtmp) {return ARR_ERR_OVFL;}
			data2[x] = param + data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int add_unsigned_long_long_4(Py_ssize_t arraylen, unsigned long long param, unsigned long long *data2, unsigned long long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned long long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = ULLONG_MAX - data2[x];
			if (param > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = param + data2[x];
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int add_unsigned_long_long_5(Py_ssize_t arraylen, unsigned long long *data1, unsigned long long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned long long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = ULLONG_MAX - data2[x];
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data1[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int add_unsigned_long_long_6(Py_ssize_t arraylen, unsigned long long *data1, unsigned long long *data2, unsigned long long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	unsigned long long ovtmp;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			ovtmp = ULLONG_MAX - data2[x];
			if (data1[x] > ovtmp) {return ARR_ERR_OVFL;}
			data3[x] = data1[x] + data2[x];
		}
	}
	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int add_float_1(Py_ssize_t arraylen, float *data1, float param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + param;
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int add_float_2(Py_ssize_t arraylen, float *data1, float param, float *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + param;
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int add_float_3(Py_ssize_t arraylen, float param, float *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data2[x] = param + data2[x];
			if (!isfinite(data2[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int add_float_4(Py_ssize_t arraylen, float param, float *data2, float *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = param + data2[x];
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int add_float_5(Py_ssize_t arraylen, float *data1, float *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + data2[x];
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int add_float_6(Py_ssize_t arraylen, float *data1, float *data2, float *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + data2[x];
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */
/* The following series of functions reflect the different parameter options possible.
   arraylen = The length of the data arrays.
   data1 = The first data array.
   data2 = The second data array.
   data3 = The third data array.
   param = The parameter to be applied to each array element.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
*/
// param_arr_num_none
signed int add_double_1(Py_ssize_t arraylen, double *data1, double param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + param;
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_num_arr
signed int add_double_2(Py_ssize_t arraylen, double *data1, double param, double *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + param;
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + param;
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int add_double_3(Py_ssize_t arraylen, double param, double *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data2[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data2[x] = param + data2[x];
			if (!isfinite(data2[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int add_double_4(Py_ssize_t arraylen, double param, double *data2, double *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = param + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = param + data2[x];
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int add_double_5(Py_ssize_t arraylen, double *data1, double *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data1[x] = data1[x] + data2[x];
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int add_double_6(Py_ssize_t arraylen, double *data1, double *data2, double *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + data2[x];
		}
	} else {
	// Math error checking enabled.
		for(x = 0; x < arraylen; x++) {
			data3[x] = data1[x] + data2[x];
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_add(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;

	// This is used to hold the parsed parameters.
	struct args_params_2 arraydata = ARGSINIT_TWO;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_two(self, args, keywds, 1, "add");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}

	// Call the C function.
	switch(arraydata.arraytype) {

		// signed_char
		case 'b' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = add_signed_char_1(arraydata.arraylength, arraydata.array1.b, arraydata.param.b, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = add_signed_char_2(arraydata.arraylength, arraydata.array1.b, arraydata.param.b, arraydata.array3.b, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = add_signed_char_3(arraydata.arraylength, arraydata.param.b, arraydata.array2.b, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = add_signed_char_4(arraydata.arraylength, arraydata.param.b, arraydata.array2.b, arraydata.array3.b, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = add_signed_char_5(arraydata.arraylength, arraydata.array1.b, arraydata.array2.b, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = add_signed_char_6(arraydata.arraylength, arraydata.array1.b, arraydata.array2.b, arraydata.array3.b, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// unsigned_char
		case 'B' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = add_unsigned_char_1(arraydata.arraylength, arraydata.array1.B, arraydata.param.B, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = add_unsigned_char_2(arraydata.arraylength, arraydata.array1.B, arraydata.param.B, arraydata.array3.B, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = add_unsigned_char_3(arraydata.arraylength, arraydata.param.B, arraydata.array2.B, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = add_unsigned_char_4(arraydata.arraylength, arraydata.param.B, arraydata.array2.B, arraydata.array3.B, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = add_unsigned_char_5(arraydata.arraylength, arraydata.array1.B, arraydata.array2.B, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = add_unsigned_char_6(arraydata.arraylength, arraydata.array1.B, arraydata.array2.B, arraydata.array3.B, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// signed_short
		case 'h' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = add_signed_short_1(arraydata.arraylength, arraydata.array1.h, arraydata.param.h, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = add_signed_short_2(arraydata.arraylength, arraydata.array1.h, arraydata.param.h, arraydata.array3.h, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = add_signed_short_3(arraydata.arraylength, arraydata.param.h, arraydata.array2.h, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = add_signed_short_4(arraydata.arraylength, arraydata.param.h, arraydata.array2.h, arraydata.array3.h, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = add_signed_short_5(arraydata.arraylength, arraydata.array1.h, arraydata.array2.h, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = add_signed_short_6(arraydata.arraylength, arraydata.array1.h, arraydata.array2.h, arraydata.array3.h, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// unsigned_short
		case 'H' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = add_unsigned_short_1(arraydata.arraylength, arraydata.array1.H, arraydata.param.H, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = add_unsigned_short_2(arraydata.arraylength, arraydata.array1.H, arraydata.param.H, arraydata.array3.H, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = add_unsigned_short_3(arraydata.arraylength, arraydata.param.H, arraydata.array2.H, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = add_unsigned_short_4(arraydata.arraylength, arraydata.param.H, arraydata.array2.H, arraydata.array3.H, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = add_unsigned_short_5(arraydata.arraylength, arraydata.array1.H, arraydata.array2.H, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = add_unsigned_short_6(arraydata.arraylength, arraydata.array1.H, arraydata.array2.H, arraydata.array3.H, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// signed_int
		case 'i' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = add_signed_int_1(arraydata.arraylength, arraydata.array1.i, arraydata.param.i, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = add_signed_int_2(arraydata.arraylength, arraydata.array1.i, arraydata.param.i, arraydata.array3.i, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = add_signed_int_3(arraydata.arraylength, arraydata.param.i, arraydata.array2.i, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = add_signed_int_4(arraydata.arraylength, arraydata.param.i, arraydata.array2.i, arraydata.array3.i, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = add_signed_int_5(arraydata.arraylength, arraydata.array1.i, arraydata.array2.i, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = add_signed_int_6(arraydata.arraylength, arraydata.array1.i, arraydata.array2.i, arraydata.array3.i, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// unsigned_int
		case 'I' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = add_unsigned_int_1(arraydata.arraylength, arraydata.array1.I, arraydata.param.I, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = add_unsigned_int_2(arraydata.arraylength, arraydata.array1.I, arraydata.param.I, arraydata.array3.I, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = add_unsigned_int_3(arraydata.arraylength, arraydata.param.I, arraydata.array2.I, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = add_unsigned_int_4(arraydata.arraylength, arraydata.param.I, arraydata.array2.I, arraydata.array3.I, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = add_unsigned_int_5(arraydata.arraylength, arraydata.array1.I, arraydata.array2.I, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = add_unsigned_int_6(arraydata.arraylength, arraydata.array1.I, arraydata.array2.I, arraydata.array3.I, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// signed_long
		case 'l' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = add_signed_long_1(arraydata.arraylength, arraydata.array1.l, arraydata.param.l, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = add_signed_long_2(arraydata.arraylength, arraydata.array1.l, arraydata.param.l, arraydata.array3.l, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = add_signed_long_3(arraydata.arraylength, arraydata.param.l, arraydata.array2.l, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = add_signed_long_4(arraydata.arraylength, arraydata.param.l, arraydata.array2.l, arraydata.array3.l, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = add_signed_long_5(arraydata.arraylength, arraydata.array1.l, arraydata.array2.l, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = add_signed_long_6(arraydata.arraylength, arraydata.array1.l, arraydata.array2.l, arraydata.array3.l, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// unsigned_long
		case 'L' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = add_unsigned_long_1(arraydata.arraylength, arraydata.array1.L, arraydata.param.L, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = add_unsigned_long_2(arraydata.arraylength, arraydata.array1.L, arraydata.param.L, arraydata.array3.L, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = add_unsigned_long_3(arraydata.arraylength, arraydata.param.L, arraydata.array2.L, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = add_unsigned_long_4(arraydata.arraylength, arraydata.param.L, arraydata.array2.L, arraydata.array3.L, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = add_unsigned_long_5(arraydata.arraylength, arraydata.array1.L, arraydata.array2.L, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = add_unsigned_long_6(arraydata.arraylength, arraydata.array1.L, arraydata.array2.L, arraydata.array3.L, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// signed_long_long
		case 'q' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = add_signed_long_long_1(arraydata.arraylength, arraydata.array1.q, arraydata.param.q, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = add_signed_long_long_2(arraydata.arraylength, arraydata.array1.q, arraydata.param.q, arraydata.array3.q, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = add_signed_long_long_3(arraydata.arraylength, arraydata.param.q, arraydata.array2.q, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = add_signed_long_long_4(arraydata.arraylength, arraydata.param.q, arraydata.array2.q, arraydata.array3.q, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = add_signed_long_long_5(arraydata.arraylength, arraydata.array1.q, arraydata.array2.q, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = add_signed_long_long_6(arraydata.arraylength, arraydata.array1.q, arraydata.array2.q, arraydata.array3.q, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// unsigned_long_long
		case 'Q' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = add_unsigned_long_long_1(arraydata.arraylength, arraydata.array1.Q, arraydata.param.Q, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = add_unsigned_long_long_2(arraydata.arraylength, arraydata.array1.Q, arraydata.param.Q, arraydata.array3.Q, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = add_unsigned_long_long_3(arraydata.arraylength, arraydata.param.Q, arraydata.array2.Q, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = add_unsigned_long_long_4(arraydata.arraylength, arraydata.param.Q, arraydata.array2.Q, arraydata.array3.Q, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = add_unsigned_long_long_5(arraydata.arraylength, arraydata.array1.Q, arraydata.array2.Q, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = add_unsigned_long_long_6(arraydata.arraylength, arraydata.array1.Q, arraydata.array2.Q, arraydata.array3.Q, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// float
		case 'f' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = add_float_1(arraydata.arraylength, arraydata.array1.f, arraydata.param.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = add_float_2(arraydata.arraylength, arraydata.array1.f, arraydata.param.f, arraydata.array3.f, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = add_float_3(arraydata.arraylength, arraydata.param.f, arraydata.array2.f, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = add_float_4(arraydata.arraylength, arraydata.param.f, arraydata.array2.f, arraydata.array3.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = add_float_5(arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = add_float_6(arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.array3.f, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// double
		case 'd' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = add_double_1(arraydata.arraylength, arraydata.array1.d, arraydata.param.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = add_double_2(arraydata.arraylength, arraydata.array1.d, arraydata.param.d, arraydata.array3.d, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = add_double_3(arraydata.arraylength, arraydata.param.d, arraydata.array2.d, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = add_double_4(arraydata.arraylength, arraydata.param.d, arraydata.array2.d, arraydata.array3.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = add_double_5(arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = add_double_6(arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.array3.d, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// Wrong array type code.
		default: {
			releasebuffers_two(arraydata);
			ErrMsgTypeExpectFloat();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_two(arraydata);


	// Signal the errors.
	if (resultcode == ARR_ERR_ZERODIV) {
		ErrMsgZeroDiv();
		return NULL;
	}

	if (resultcode == ARR_ERR_ARITHMETIC) {
		ErrMsgArithCalc();
		return NULL;
	}

	if (resultcode == ARR_ERR_OVFL) {
		ErrMsgArithOverflowCalc();
		return NULL;
	}


	// Everything was successful.
	Py_RETURN_NONE;

}


/*--------------------------------------------------------------------------- */


/* The module doc string */
PyDoc_STRVAR(add__doc__,
"add \n\
_____________________________ \n\
\n\
Calculate add over the values in an array.  \n\
\n\
======================  ============================================== \n\
Equivalent to:          x + y \n\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \n\
Exceptions raised:      OverflowError, ArithmeticError \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
  add(array1, param) \n\
  add(array1, param, outparray) \n\
  add(param, array1) \n\
  add(param, array1, outparray) \n\
  add(array1, array2) \n\
  add(array1, array2, outparray) \n\
  add(array1, param, maxlen=y) \n\
  add(array1, param, matherrors=False) \n\
\n\
* array1 - The first input data array to be examined. If no output  \n\
  array is provided the results will overwrite the input data.  \n\
* param - A non-array numeric parameter.  \n\
* array2 - A second input data array. Each element in this array is  \n\
  applied to the corresponding element in the first array.  \n\
* outparray - The output array. This parameter is optional.  \n\
* maxlen - Limit the length of the array used. This must be a valid  \n\
  positive integer. If a zero or negative length, or a value which is  \n\
  greater than the actual length of the array is specified, this  \n\
  parameter is ignored.  \n\
* matherrors - If true, arithmetic error checking is disabled. The  \n\
  default is false. \n\
\n");

/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "add" is the name seen inside of Python. 
 "py_add" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef add_methods[] = {
	{"add",  (PyCFunction)py_add, METH_VARARGS | METH_KEYWORDS, add__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef addmodule = {
    PyModuleDef_HEAD_INIT,
    "add",
    NULL,
    -1,
    add_methods
};

PyMODINIT_FUNC PyInit_add(void)
{
    return PyModule_Create(&addmodule);
};

/*--------------------------------------------------------------------------- */
