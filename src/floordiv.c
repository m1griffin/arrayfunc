//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   floordiv.c
// Purpose:  Calculate the floordiv of values in an array.
// Language: C
// Date:     15-Nov-2017.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2021    Michael Griffin    <m12.griffin@gmail.com>
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
signed int floordiv_signed_char_1(Py_ssize_t arraylen, signed char *data1, signed char param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed char datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Math error check.
	if (param == 0) {return ARR_ERR_ZERODIV;}

	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == -1) {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			// Math error check.
			if (datatmp == SCHAR_MIN) {return ARR_ERR_OVFL;}
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data1[x] = dataouttmp - 1; 
			} else {
				data1[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data1[x] = dataouttmp - 1; 
			} else {
				data1[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int floordiv_signed_char_2(Py_ssize_t arraylen, signed char *data1, signed char param, signed char *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed char datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Math error check.
	if (param == 0) {return ARR_ERR_ZERODIV;}

	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == -1) {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			// Math error check.
			if (datatmp == SCHAR_MIN) {return ARR_ERR_OVFL;}
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int floordiv_signed_char_3(Py_ssize_t arraylen, signed char param, signed char *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed char datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == SCHAR_MIN) {
		for (x = 0; x < arraylen; x++) {
			// Math error check.
			datatmp = data2[x];
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			if (datatmp == -1) {return ARR_ERR_OVFL;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data2[x] = dataouttmp - 1; 
			} else {
				data2[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			// Math error check.
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data2[x] = dataouttmp - 1; 
			} else {
				data2[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int floordiv_signed_char_4(Py_ssize_t arraylen, signed char param, signed char *data2, signed char *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed char datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == SCHAR_MIN) {
		for (x = 0; x < arraylen; x++) {
			// Math error check.
			datatmp = data2[x];
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			if (datatmp == -1) {return ARR_ERR_OVFL;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			// Math error check.
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int floordiv_signed_char_5(Py_ssize_t arraylen, signed char *data1, signed char *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed char datatmp, data2tmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	for (x = 0; x < arraylen; x++) {
		datatmp = data1[x];
		data2tmp = data2[x];
		// Math error check.
		if (data2tmp == 0) {return ARR_ERR_ZERODIV;}
		// Math error check.
		if ((data2tmp == -1) && (datatmp == SCHAR_MIN)) {return ARR_ERR_OVFL;}
		dataouttmp = datatmp / data2tmp;
		// This check is required for floor division.
		if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
			data1[x] = dataouttmp - 1; 
		} else {
			data1[x] = dataouttmp;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int floordiv_signed_char_6(Py_ssize_t arraylen, signed char *data1, signed char *data2, signed char *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed char datatmp, data2tmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	for (x = 0; x < arraylen; x++) {
		datatmp = data1[x];
		data2tmp = data2[x];
		// Math error check.
		if (data2tmp == 0) {return ARR_ERR_ZERODIV;}
		// Math error check.
		if ((data2tmp == -1) && (datatmp == SCHAR_MIN)) {return ARR_ERR_OVFL;}
		dataouttmp = datatmp / data2tmp;
		// This check is required for floor division.
		if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
			data3[x] = dataouttmp - 1; 
		} else {
			data3[x] = dataouttmp;
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
signed int floordiv_unsigned_char_1(Py_ssize_t arraylen, unsigned char *data1, unsigned char param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	if (param == 0) {return ARR_ERR_ZERODIV;}		// Math error check.

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] / param;
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int floordiv_unsigned_char_2(Py_ssize_t arraylen, unsigned char *data1, unsigned char param, unsigned char *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	if (param == 0) {return ARR_ERR_ZERODIV;}		// Math error check.

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] / param;
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int floordiv_unsigned_char_3(Py_ssize_t arraylen, unsigned char param, unsigned char *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data2[x] = param / data2[x];
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int floordiv_unsigned_char_4(Py_ssize_t arraylen, unsigned char param, unsigned char *data2, unsigned char *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data3[x] = param / data2[x];
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int floordiv_unsigned_char_5(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data1[x] = data1[x] / data2[x];
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int floordiv_unsigned_char_6(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2, unsigned char *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data3[x] = data1[x] / data2[x];
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
signed int floordiv_signed_short_1(Py_ssize_t arraylen, signed short *data1, signed short param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed short datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Math error check.
	if (param == 0) {return ARR_ERR_ZERODIV;}

	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == -1) {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			// Math error check.
			if (datatmp == SHRT_MIN) {return ARR_ERR_OVFL;}
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data1[x] = dataouttmp - 1; 
			} else {
				data1[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data1[x] = dataouttmp - 1; 
			} else {
				data1[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int floordiv_signed_short_2(Py_ssize_t arraylen, signed short *data1, signed short param, signed short *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed short datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Math error check.
	if (param == 0) {return ARR_ERR_ZERODIV;}

	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == -1) {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			// Math error check.
			if (datatmp == SHRT_MIN) {return ARR_ERR_OVFL;}
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int floordiv_signed_short_3(Py_ssize_t arraylen, signed short param, signed short *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed short datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == SHRT_MIN) {
		for (x = 0; x < arraylen; x++) {
			// Math error check.
			datatmp = data2[x];
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			if (datatmp == -1) {return ARR_ERR_OVFL;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data2[x] = dataouttmp - 1; 
			} else {
				data2[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			// Math error check.
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data2[x] = dataouttmp - 1; 
			} else {
				data2[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int floordiv_signed_short_4(Py_ssize_t arraylen, signed short param, signed short *data2, signed short *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed short datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == SHRT_MIN) {
		for (x = 0; x < arraylen; x++) {
			// Math error check.
			datatmp = data2[x];
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			if (datatmp == -1) {return ARR_ERR_OVFL;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			// Math error check.
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int floordiv_signed_short_5(Py_ssize_t arraylen, signed short *data1, signed short *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed short datatmp, data2tmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	for (x = 0; x < arraylen; x++) {
		datatmp = data1[x];
		data2tmp = data2[x];
		// Math error check.
		if (data2tmp == 0) {return ARR_ERR_ZERODIV;}
		// Math error check.
		if ((data2tmp == -1) && (datatmp == SHRT_MIN)) {return ARR_ERR_OVFL;}
		dataouttmp = datatmp / data2tmp;
		// This check is required for floor division.
		if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
			data1[x] = dataouttmp - 1; 
		} else {
			data1[x] = dataouttmp;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int floordiv_signed_short_6(Py_ssize_t arraylen, signed short *data1, signed short *data2, signed short *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed short datatmp, data2tmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	for (x = 0; x < arraylen; x++) {
		datatmp = data1[x];
		data2tmp = data2[x];
		// Math error check.
		if (data2tmp == 0) {return ARR_ERR_ZERODIV;}
		// Math error check.
		if ((data2tmp == -1) && (datatmp == SHRT_MIN)) {return ARR_ERR_OVFL;}
		dataouttmp = datatmp / data2tmp;
		// This check is required for floor division.
		if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
			data3[x] = dataouttmp - 1; 
		} else {
			data3[x] = dataouttmp;
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
signed int floordiv_unsigned_short_1(Py_ssize_t arraylen, unsigned short *data1, unsigned short param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	if (param == 0) {return ARR_ERR_ZERODIV;}		// Math error check.

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] / param;
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int floordiv_unsigned_short_2(Py_ssize_t arraylen, unsigned short *data1, unsigned short param, unsigned short *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	if (param == 0) {return ARR_ERR_ZERODIV;}		// Math error check.

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] / param;
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int floordiv_unsigned_short_3(Py_ssize_t arraylen, unsigned short param, unsigned short *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data2[x] = param / data2[x];
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int floordiv_unsigned_short_4(Py_ssize_t arraylen, unsigned short param, unsigned short *data2, unsigned short *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data3[x] = param / data2[x];
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int floordiv_unsigned_short_5(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data1[x] = data1[x] / data2[x];
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int floordiv_unsigned_short_6(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2, unsigned short *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data3[x] = data1[x] / data2[x];
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
signed int floordiv_signed_int_1(Py_ssize_t arraylen, signed int *data1, signed int param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed int datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Math error check.
	if (param == 0) {return ARR_ERR_ZERODIV;}

	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == -1) {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			// Math error check.
			if (datatmp == INT_MIN) {return ARR_ERR_OVFL;}
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data1[x] = dataouttmp - 1; 
			} else {
				data1[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data1[x] = dataouttmp - 1; 
			} else {
				data1[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int floordiv_signed_int_2(Py_ssize_t arraylen, signed int *data1, signed int param, signed int *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed int datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Math error check.
	if (param == 0) {return ARR_ERR_ZERODIV;}

	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == -1) {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			// Math error check.
			if (datatmp == INT_MIN) {return ARR_ERR_OVFL;}
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int floordiv_signed_int_3(Py_ssize_t arraylen, signed int param, signed int *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed int datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == INT_MIN) {
		for (x = 0; x < arraylen; x++) {
			// Math error check.
			datatmp = data2[x];
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			if (datatmp == -1) {return ARR_ERR_OVFL;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data2[x] = dataouttmp - 1; 
			} else {
				data2[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			// Math error check.
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data2[x] = dataouttmp - 1; 
			} else {
				data2[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int floordiv_signed_int_4(Py_ssize_t arraylen, signed int param, signed int *data2, signed int *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed int datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == INT_MIN) {
		for (x = 0; x < arraylen; x++) {
			// Math error check.
			datatmp = data2[x];
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			if (datatmp == -1) {return ARR_ERR_OVFL;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			// Math error check.
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int floordiv_signed_int_5(Py_ssize_t arraylen, signed int *data1, signed int *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed int datatmp, data2tmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	for (x = 0; x < arraylen; x++) {
		datatmp = data1[x];
		data2tmp = data2[x];
		// Math error check.
		if (data2tmp == 0) {return ARR_ERR_ZERODIV;}
		// Math error check.
		if ((data2tmp == -1) && (datatmp == INT_MIN)) {return ARR_ERR_OVFL;}
		dataouttmp = datatmp / data2tmp;
		// This check is required for floor division.
		if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
			data1[x] = dataouttmp - 1; 
		} else {
			data1[x] = dataouttmp;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int floordiv_signed_int_6(Py_ssize_t arraylen, signed int *data1, signed int *data2, signed int *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed int datatmp, data2tmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	for (x = 0; x < arraylen; x++) {
		datatmp = data1[x];
		data2tmp = data2[x];
		// Math error check.
		if (data2tmp == 0) {return ARR_ERR_ZERODIV;}
		// Math error check.
		if ((data2tmp == -1) && (datatmp == INT_MIN)) {return ARR_ERR_OVFL;}
		dataouttmp = datatmp / data2tmp;
		// This check is required for floor division.
		if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
			data3[x] = dataouttmp - 1; 
		} else {
			data3[x] = dataouttmp;
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
signed int floordiv_unsigned_int_1(Py_ssize_t arraylen, unsigned int *data1, unsigned int param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	if (param == 0) {return ARR_ERR_ZERODIV;}		// Math error check.

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] / param;
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int floordiv_unsigned_int_2(Py_ssize_t arraylen, unsigned int *data1, unsigned int param, unsigned int *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	if (param == 0) {return ARR_ERR_ZERODIV;}		// Math error check.

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] / param;
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int floordiv_unsigned_int_3(Py_ssize_t arraylen, unsigned int param, unsigned int *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data2[x] = param / data2[x];
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int floordiv_unsigned_int_4(Py_ssize_t arraylen, unsigned int param, unsigned int *data2, unsigned int *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data3[x] = param / data2[x];
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int floordiv_unsigned_int_5(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data1[x] = data1[x] / data2[x];
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int floordiv_unsigned_int_6(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2, unsigned int *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data3[x] = data1[x] / data2[x];
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
signed int floordiv_signed_long_1(Py_ssize_t arraylen, signed long *data1, signed long param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Math error check.
	if (param == 0) {return ARR_ERR_ZERODIV;}

	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == -1) {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			// Math error check.
			if (datatmp == LONG_MIN) {return ARR_ERR_OVFL;}
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data1[x] = dataouttmp - 1; 
			} else {
				data1[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data1[x] = dataouttmp - 1; 
			} else {
				data1[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int floordiv_signed_long_2(Py_ssize_t arraylen, signed long *data1, signed long param, signed long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Math error check.
	if (param == 0) {return ARR_ERR_ZERODIV;}

	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == -1) {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			// Math error check.
			if (datatmp == LONG_MIN) {return ARR_ERR_OVFL;}
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int floordiv_signed_long_3(Py_ssize_t arraylen, signed long param, signed long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == LONG_MIN) {
		for (x = 0; x < arraylen; x++) {
			// Math error check.
			datatmp = data2[x];
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			if (datatmp == -1) {return ARR_ERR_OVFL;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data2[x] = dataouttmp - 1; 
			} else {
				data2[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			// Math error check.
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data2[x] = dataouttmp - 1; 
			} else {
				data2[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int floordiv_signed_long_4(Py_ssize_t arraylen, signed long param, signed long *data2, signed long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == LONG_MIN) {
		for (x = 0; x < arraylen; x++) {
			// Math error check.
			datatmp = data2[x];
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			if (datatmp == -1) {return ARR_ERR_OVFL;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			// Math error check.
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int floordiv_signed_long_5(Py_ssize_t arraylen, signed long *data1, signed long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long datatmp, data2tmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	for (x = 0; x < arraylen; x++) {
		datatmp = data1[x];
		data2tmp = data2[x];
		// Math error check.
		if (data2tmp == 0) {return ARR_ERR_ZERODIV;}
		// Math error check.
		if ((data2tmp == -1) && (datatmp == LONG_MIN)) {return ARR_ERR_OVFL;}
		dataouttmp = datatmp / data2tmp;
		// This check is required for floor division.
		if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
			data1[x] = dataouttmp - 1; 
		} else {
			data1[x] = dataouttmp;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int floordiv_signed_long_6(Py_ssize_t arraylen, signed long *data1, signed long *data2, signed long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long datatmp, data2tmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	for (x = 0; x < arraylen; x++) {
		datatmp = data1[x];
		data2tmp = data2[x];
		// Math error check.
		if (data2tmp == 0) {return ARR_ERR_ZERODIV;}
		// Math error check.
		if ((data2tmp == -1) && (datatmp == LONG_MIN)) {return ARR_ERR_OVFL;}
		dataouttmp = datatmp / data2tmp;
		// This check is required for floor division.
		if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
			data3[x] = dataouttmp - 1; 
		} else {
			data3[x] = dataouttmp;
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
signed int floordiv_unsigned_long_1(Py_ssize_t arraylen, unsigned long *data1, unsigned long param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	if (param == 0) {return ARR_ERR_ZERODIV;}		// Math error check.

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] / param;
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int floordiv_unsigned_long_2(Py_ssize_t arraylen, unsigned long *data1, unsigned long param, unsigned long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	if (param == 0) {return ARR_ERR_ZERODIV;}		// Math error check.

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] / param;
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int floordiv_unsigned_long_3(Py_ssize_t arraylen, unsigned long param, unsigned long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data2[x] = param / data2[x];
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int floordiv_unsigned_long_4(Py_ssize_t arraylen, unsigned long param, unsigned long *data2, unsigned long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data3[x] = param / data2[x];
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int floordiv_unsigned_long_5(Py_ssize_t arraylen, unsigned long *data1, unsigned long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data1[x] = data1[x] / data2[x];
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int floordiv_unsigned_long_6(Py_ssize_t arraylen, unsigned long *data1, unsigned long *data2, unsigned long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data3[x] = data1[x] / data2[x];
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
signed int floordiv_signed_long_long_1(Py_ssize_t arraylen, signed long long *data1, signed long long param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long long datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Math error check.
	if (param == 0) {return ARR_ERR_ZERODIV;}

	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == -1) {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			// Math error check.
			if (datatmp == LLONG_MIN) {return ARR_ERR_OVFL;}
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data1[x] = dataouttmp - 1; 
			} else {
				data1[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data1[x] = dataouttmp - 1; 
			} else {
				data1[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int floordiv_signed_long_long_2(Py_ssize_t arraylen, signed long long *data1, signed long long param, signed long long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long long datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Math error check.
	if (param == 0) {return ARR_ERR_ZERODIV;}

	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == -1) {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			// Math error check.
			if (datatmp == LLONG_MIN) {return ARR_ERR_OVFL;}
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data1[x];
			dataouttmp = datatmp / param;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * param) != datatmp)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int floordiv_signed_long_long_3(Py_ssize_t arraylen, signed long long param, signed long long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long long datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == LLONG_MIN) {
		for (x = 0; x < arraylen; x++) {
			// Math error check.
			datatmp = data2[x];
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			if (datatmp == -1) {return ARR_ERR_OVFL;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data2[x] = dataouttmp - 1; 
			} else {
				data2[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			// Math error check.
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data2[x] = dataouttmp - 1; 
			} else {
				data2[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int floordiv_signed_long_long_4(Py_ssize_t arraylen, signed long long param, signed long long *data2, signed long long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long long datatmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	if (param == LLONG_MIN) {
		for (x = 0; x < arraylen; x++) {
			// Math error check.
			datatmp = data2[x];
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			if (datatmp == -1) {return ARR_ERR_OVFL;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			// Math error check.
			if (datatmp == 0) {return ARR_ERR_ZERODIV;}
			dataouttmp = param / datatmp;
			// This check is required for floor division.
			if (((datatmp < 0) != (param < 0)) && ((dataouttmp * datatmp) != param)) { 
				data3[x] = dataouttmp - 1; 
			} else {
				data3[x] = dataouttmp;
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int floordiv_signed_long_long_5(Py_ssize_t arraylen, signed long long *data1, signed long long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long long datatmp, data2tmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	for (x = 0; x < arraylen; x++) {
		datatmp = data1[x];
		data2tmp = data2[x];
		// Math error check.
		if (data2tmp == 0) {return ARR_ERR_ZERODIV;}
		// Math error check.
		if ((data2tmp == -1) && (datatmp == LLONG_MIN)) {return ARR_ERR_OVFL;}
		dataouttmp = datatmp / data2tmp;
		// This check is required for floor division.
		if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
			data1[x] = dataouttmp - 1; 
		} else {
			data1[x] = dataouttmp;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int floordiv_signed_long_long_6(Py_ssize_t arraylen, signed long long *data1, signed long long *data2, signed long long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	signed long long datatmp, data2tmp, dataouttmp;


	// Cannot disable divide by zero checking because this causes a crash.
	// Division of min-int by -1 produces a similar error as division by 0.
	for (x = 0; x < arraylen; x++) {
		datatmp = data1[x];
		data2tmp = data2[x];
		// Math error check.
		if (data2tmp == 0) {return ARR_ERR_ZERODIV;}
		// Math error check.
		if ((data2tmp == -1) && (datatmp == LLONG_MIN)) {return ARR_ERR_OVFL;}
		dataouttmp = datatmp / data2tmp;
		// This check is required for floor division.
		if (((datatmp < 0) != (data2tmp < 0)) && ((dataouttmp * data2tmp) != datatmp)) { 
			data3[x] = dataouttmp - 1; 
		} else {
			data3[x] = dataouttmp;
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
signed int floordiv_unsigned_long_long_1(Py_ssize_t arraylen, unsigned long long *data1, unsigned long long param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	if (param == 0) {return ARR_ERR_ZERODIV;}		// Math error check.

	for (x = 0; x < arraylen; x++) {
		data1[x] = data1[x] / param;
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int floordiv_unsigned_long_long_2(Py_ssize_t arraylen, unsigned long long *data1, unsigned long long param, unsigned long long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Cannot disable divide by zero checking because this causes a crash.
	if (param == 0) {return ARR_ERR_ZERODIV;}		// Math error check.

	for (x = 0; x < arraylen; x++) {
		data3[x] = data1[x] / param;
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int floordiv_unsigned_long_long_3(Py_ssize_t arraylen, unsigned long long param, unsigned long long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data2[x] = param / data2[x];
	}
	return ARR_NO_ERR;

}

// param_num_arr_arr
signed int floordiv_unsigned_long_long_4(Py_ssize_t arraylen, unsigned long long param, unsigned long long *data2, unsigned long long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data3[x] = param / data2[x];
	}
	return ARR_NO_ERR;

}



// param_arr_arr_none
signed int floordiv_unsigned_long_long_5(Py_ssize_t arraylen, unsigned long long *data1, unsigned long long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data1[x] = data1[x] / data2[x];
	}
	return ARR_NO_ERR;

}

// param_arr_arr_arr
signed int floordiv_unsigned_long_long_6(Py_ssize_t arraylen, unsigned long long *data1, unsigned long long *data2, unsigned long long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	for (x = 0; x < arraylen; x++) {
		// Cannot disable divide by zero checking because this causes a crash.
		if (data2[x] == 0) {return ARR_ERR_ZERODIV;}
		data3[x] = data1[x] / data2[x];
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
signed int floordiv_float_1(Py_ssize_t arraylen, float *data1, float param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {

		for (x = 0; x < arraylen; x++) {
			data1[x] = floorf(data1[x] / param);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = floorf(data1[x] / param);
			if (!isfinite(data1[x])) {
				if (param == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int floordiv_float_2(Py_ssize_t arraylen, float *data1, float param, float *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {

		for (x = 0; x < arraylen; x++) {
			data3[x] = floorf(data1[x] / param);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = floorf(data1[x] / param);
			if (!isfinite(data3[x])) {
				if (param == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int floordiv_float_3(Py_ssize_t arraylen, float param, float *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	float datatmp;

	// Math error checking disabled.
	if (ignoreerrors) {

		for (x = 0; x < arraylen; x++) {
			data2[x] = floorf(param / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			data2[x] = floorf(param / data2[x]);
			if (!isfinite(data2[x])) {
				if (datatmp == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int floordiv_float_4(Py_ssize_t arraylen, float param, float *data2, float *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {

		for (x = 0; x < arraylen; x++) {
			data3[x] = floorf(param / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = floorf(param / data2[x]);
			if (!isfinite(data3[x])) {
				if (data2[x] == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int floordiv_float_5(Py_ssize_t arraylen, float *data1, float *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {

		for (x = 0; x < arraylen; x++) {
			data1[x] = floorf(data1[x] / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = floorf(data1[x] / data2[x]);
			if (!isfinite(data1[x])) {
				if (data2[x] == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int floordiv_float_6(Py_ssize_t arraylen, float *data1, float *data2, float *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {

		for (x = 0; x < arraylen; x++) {
			data3[x] = floorf(data1[x] / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = floorf(data1[x] / data2[x]);
			if (!isfinite(data3[x])) {
				if (data2[x] == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
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
signed int floordiv_double_1(Py_ssize_t arraylen, double *data1, double param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {

		for (x = 0; x < arraylen; x++) {
			data1[x] = floor(data1[x] / param);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = floor(data1[x] / param);
			if (!isfinite(data1[x])) {
				if (param == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int floordiv_double_2(Py_ssize_t arraylen, double *data1, double param, double *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {

		for (x = 0; x < arraylen; x++) {
			data3[x] = floor(data1[x] / param);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = floor(data1[x] / param);
			if (!isfinite(data3[x])) {
				if (param == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}

// param_num_arr_none
signed int floordiv_double_3(Py_ssize_t arraylen, double param, double *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	double datatmp;

	// Math error checking disabled.
	if (ignoreerrors) {

		for (x = 0; x < arraylen; x++) {
			data2[x] = floor(param / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			datatmp = data2[x];
			data2[x] = floor(param / data2[x]);
			if (!isfinite(data2[x])) {
				if (datatmp == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int floordiv_double_4(Py_ssize_t arraylen, double param, double *data2, double *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {

		for (x = 0; x < arraylen; x++) {
			data3[x] = floor(param / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = floor(param / data2[x]);
			if (!isfinite(data3[x])) {
				if (data2[x] == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int floordiv_double_5(Py_ssize_t arraylen, double *data1, double *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {

		for (x = 0; x < arraylen; x++) {
			data1[x] = floor(data1[x] / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = floor(data1[x] / data2[x]);
			if (!isfinite(data1[x])) {
				if (data2[x] == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int floordiv_double_6(Py_ssize_t arraylen, double *data1, double *data2, double *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;

	// Math error checking disabled.
	if (ignoreerrors) {

		for (x = 0; x < arraylen; x++) {
			data3[x] = floor(data1[x] / data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = floor(data1[x] / data2[x]);
			if (!isfinite(data3[x])) {
				if (data2[x] == 0.0) {
					return ARR_ERR_ZERODIV;
				} else {
					return ARR_ERR_ARITHMETIC;
				}
			}
		}
	}
	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_floordiv(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;

	// This is used to hold the parsed parameters.
	struct args_params_2 arraydata = ARGSINIT_TWO;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_two(self, args, keywds, 1, 0, "floordiv");

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
					resultcode = floordiv_signed_char_1(arraydata.arraylength, arraydata.array1.b, arraydata.param.b, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = floordiv_signed_char_2(arraydata.arraylength, arraydata.array1.b, arraydata.param.b, arraydata.array3.b, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = floordiv_signed_char_3(arraydata.arraylength, arraydata.param.b, arraydata.array2.b, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = floordiv_signed_char_4(arraydata.arraylength, arraydata.param.b, arraydata.array2.b, arraydata.array3.b, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = floordiv_signed_char_5(arraydata.arraylength, arraydata.array1.b, arraydata.array2.b, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = floordiv_signed_char_6(arraydata.arraylength, arraydata.array1.b, arraydata.array2.b, arraydata.array3.b, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// unsigned_char
		case 'B' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = floordiv_unsigned_char_1(arraydata.arraylength, arraydata.array1.B, arraydata.param.B, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = floordiv_unsigned_char_2(arraydata.arraylength, arraydata.array1.B, arraydata.param.B, arraydata.array3.B, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = floordiv_unsigned_char_3(arraydata.arraylength, arraydata.param.B, arraydata.array2.B, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = floordiv_unsigned_char_4(arraydata.arraylength, arraydata.param.B, arraydata.array2.B, arraydata.array3.B, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = floordiv_unsigned_char_5(arraydata.arraylength, arraydata.array1.B, arraydata.array2.B, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = floordiv_unsigned_char_6(arraydata.arraylength, arraydata.array1.B, arraydata.array2.B, arraydata.array3.B, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// signed_short
		case 'h' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = floordiv_signed_short_1(arraydata.arraylength, arraydata.array1.h, arraydata.param.h, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = floordiv_signed_short_2(arraydata.arraylength, arraydata.array1.h, arraydata.param.h, arraydata.array3.h, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = floordiv_signed_short_3(arraydata.arraylength, arraydata.param.h, arraydata.array2.h, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = floordiv_signed_short_4(arraydata.arraylength, arraydata.param.h, arraydata.array2.h, arraydata.array3.h, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = floordiv_signed_short_5(arraydata.arraylength, arraydata.array1.h, arraydata.array2.h, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = floordiv_signed_short_6(arraydata.arraylength, arraydata.array1.h, arraydata.array2.h, arraydata.array3.h, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// unsigned_short
		case 'H' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = floordiv_unsigned_short_1(arraydata.arraylength, arraydata.array1.H, arraydata.param.H, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = floordiv_unsigned_short_2(arraydata.arraylength, arraydata.array1.H, arraydata.param.H, arraydata.array3.H, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = floordiv_unsigned_short_3(arraydata.arraylength, arraydata.param.H, arraydata.array2.H, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = floordiv_unsigned_short_4(arraydata.arraylength, arraydata.param.H, arraydata.array2.H, arraydata.array3.H, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = floordiv_unsigned_short_5(arraydata.arraylength, arraydata.array1.H, arraydata.array2.H, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = floordiv_unsigned_short_6(arraydata.arraylength, arraydata.array1.H, arraydata.array2.H, arraydata.array3.H, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// signed_int
		case 'i' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = floordiv_signed_int_1(arraydata.arraylength, arraydata.array1.i, arraydata.param.i, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = floordiv_signed_int_2(arraydata.arraylength, arraydata.array1.i, arraydata.param.i, arraydata.array3.i, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = floordiv_signed_int_3(arraydata.arraylength, arraydata.param.i, arraydata.array2.i, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = floordiv_signed_int_4(arraydata.arraylength, arraydata.param.i, arraydata.array2.i, arraydata.array3.i, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = floordiv_signed_int_5(arraydata.arraylength, arraydata.array1.i, arraydata.array2.i, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = floordiv_signed_int_6(arraydata.arraylength, arraydata.array1.i, arraydata.array2.i, arraydata.array3.i, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// unsigned_int
		case 'I' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = floordiv_unsigned_int_1(arraydata.arraylength, arraydata.array1.I, arraydata.param.I, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = floordiv_unsigned_int_2(arraydata.arraylength, arraydata.array1.I, arraydata.param.I, arraydata.array3.I, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = floordiv_unsigned_int_3(arraydata.arraylength, arraydata.param.I, arraydata.array2.I, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = floordiv_unsigned_int_4(arraydata.arraylength, arraydata.param.I, arraydata.array2.I, arraydata.array3.I, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = floordiv_unsigned_int_5(arraydata.arraylength, arraydata.array1.I, arraydata.array2.I, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = floordiv_unsigned_int_6(arraydata.arraylength, arraydata.array1.I, arraydata.array2.I, arraydata.array3.I, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// signed_long
		case 'l' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = floordiv_signed_long_1(arraydata.arraylength, arraydata.array1.l, arraydata.param.l, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = floordiv_signed_long_2(arraydata.arraylength, arraydata.array1.l, arraydata.param.l, arraydata.array3.l, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = floordiv_signed_long_3(arraydata.arraylength, arraydata.param.l, arraydata.array2.l, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = floordiv_signed_long_4(arraydata.arraylength, arraydata.param.l, arraydata.array2.l, arraydata.array3.l, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = floordiv_signed_long_5(arraydata.arraylength, arraydata.array1.l, arraydata.array2.l, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = floordiv_signed_long_6(arraydata.arraylength, arraydata.array1.l, arraydata.array2.l, arraydata.array3.l, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// unsigned_long
		case 'L' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = floordiv_unsigned_long_1(arraydata.arraylength, arraydata.array1.L, arraydata.param.L, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = floordiv_unsigned_long_2(arraydata.arraylength, arraydata.array1.L, arraydata.param.L, arraydata.array3.L, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = floordiv_unsigned_long_3(arraydata.arraylength, arraydata.param.L, arraydata.array2.L, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = floordiv_unsigned_long_4(arraydata.arraylength, arraydata.param.L, arraydata.array2.L, arraydata.array3.L, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = floordiv_unsigned_long_5(arraydata.arraylength, arraydata.array1.L, arraydata.array2.L, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = floordiv_unsigned_long_6(arraydata.arraylength, arraydata.array1.L, arraydata.array2.L, arraydata.array3.L, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// signed_long_long
		case 'q' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = floordiv_signed_long_long_1(arraydata.arraylength, arraydata.array1.q, arraydata.param.q, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = floordiv_signed_long_long_2(arraydata.arraylength, arraydata.array1.q, arraydata.param.q, arraydata.array3.q, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = floordiv_signed_long_long_3(arraydata.arraylength, arraydata.param.q, arraydata.array2.q, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = floordiv_signed_long_long_4(arraydata.arraylength, arraydata.param.q, arraydata.array2.q, arraydata.array3.q, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = floordiv_signed_long_long_5(arraydata.arraylength, arraydata.array1.q, arraydata.array2.q, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = floordiv_signed_long_long_6(arraydata.arraylength, arraydata.array1.q, arraydata.array2.q, arraydata.array3.q, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// unsigned_long_long
		case 'Q' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = floordiv_unsigned_long_long_1(arraydata.arraylength, arraydata.array1.Q, arraydata.param.Q, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = floordiv_unsigned_long_long_2(arraydata.arraylength, arraydata.array1.Q, arraydata.param.Q, arraydata.array3.Q, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = floordiv_unsigned_long_long_3(arraydata.arraylength, arraydata.param.Q, arraydata.array2.Q, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = floordiv_unsigned_long_long_4(arraydata.arraylength, arraydata.param.Q, arraydata.array2.Q, arraydata.array3.Q, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = floordiv_unsigned_long_long_5(arraydata.arraylength, arraydata.array1.Q, arraydata.array2.Q, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = floordiv_unsigned_long_long_6(arraydata.arraylength, arraydata.array1.Q, arraydata.array2.Q, arraydata.array3.Q, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// float
		case 'f' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = floordiv_float_1(arraydata.arraylength, arraydata.array1.f, arraydata.param.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = floordiv_float_2(arraydata.arraylength, arraydata.array1.f, arraydata.param.f, arraydata.array3.f, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = floordiv_float_3(arraydata.arraylength, arraydata.param.f, arraydata.array2.f, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = floordiv_float_4(arraydata.arraylength, arraydata.param.f, arraydata.array2.f, arraydata.array3.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = floordiv_float_5(arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = floordiv_float_6(arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.array3.f, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// double
		case 'd' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = floordiv_double_1(arraydata.arraylength, arraydata.array1.d, arraydata.param.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = floordiv_double_2(arraydata.arraylength, arraydata.array1.d, arraydata.param.d, arraydata.array3.d, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = floordiv_double_3(arraydata.arraylength, arraydata.param.d, arraydata.array2.d, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = floordiv_double_4(arraydata.arraylength, arraydata.param.d, arraydata.array2.d, arraydata.array3.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = floordiv_double_5(arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = floordiv_double_6(arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.array3.d, arraydata.ignoreerrors);
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
PyDoc_STRVAR(floordiv__doc__,
"floordiv \n\
_____________________________ \n\
\n\
Calculate floordiv over the values in an array.  \n\
\n\
======================  ============================================== \n\
Equivalent to:          [x // param for x in array1] \n\
or                      [param // y for y in array2] \n\
or                      [x // y for x, y in zip(array1, array2)] \n\
======================  ============================================== \n\
\n\
======================  ============================================== \n\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \n\
Exceptions raised:      OverflowError, ArithmeticError, ZeroDivisionError \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
  floordiv(array1, param) \n\
  floordiv(array1, param, outparray) \n\
  floordiv(param, array1) \n\
  floordiv(param, array1, outparray) \n\
  floordiv(array1, array2) \n\
  floordiv(array1, array2, outparray) \n\
  floordiv(array1, param, maxlen=y) \n\
  floordiv(array1, param, matherrors=False) \n\
\n\
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
");

/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "floordiv" is the name seen inside of Python. 
 "py_floordiv" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef floordiv_methods[] = {
	{"floordiv",  (PyCFunction)py_floordiv, METH_VARARGS | METH_KEYWORDS, floordiv__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef floordivmodule = {
    PyModuleDef_HEAD_INIT,
    "floordiv",
    NULL,
    -1,
    floordiv_methods
};

PyMODINIT_FUNC PyInit_floordiv(void)
{
    return PyModule_Create(&floordivmodule);
};

/*--------------------------------------------------------------------------- */

