//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   pow.c
// Purpose:  Calculate the pow of values in an array.
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

// Note: The guard calculations for negative need to use abs(x) instead of -x
// because of problems with Microsoft MSVS 2010. MSVS was confused by negating
// a negative number with minimum integers (e.g. INT_MIN) and producing a
// positive result.

// Return x raised to the power of y.
signed char arith_pow_signed_char(signed char x, signed char y, char *errflag) {
	signed char i, z, ovtmp1, ovtmp2;
	z = 1;
	*errflag = 0;

	// We don't allow negative powers for integers.
	if (y < 0) {
		*errflag = ARR_ERR_VALUE_ERR;
		return z;
	}

	// Special case for raise to the power of zero.
	if (y == 0) { return 1; }

	// We need this special case to avoid dividing by zero.
	if (x == 0) {return 0;}

	if (x > 0) {
		ovtmp1 = SCHAR_MAX / x;
		for (i = 0; i < y; i++) {
			if (z > ovtmp1) {*errflag = ARR_ERR_OVFL; return z;}
			z = z * x;
		}
	} else {
		ovtmp1 = SCHAR_MAX / abs(x);
		ovtmp2 = SCHAR_MIN / abs(x);
		for (i = 0; i < y; i++) {
			if ((z > ovtmp1) || (z < ovtmp2)) {*errflag = ARR_ERR_OVFL; return z;}
			z = z * x;
		}
	}
	return z;
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
signed int pow_signed_char_1(Py_ssize_t arraylen, signed char *data1, signed char param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_char(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_char(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int pow_signed_char_2(Py_ssize_t arraylen, signed char *data1, signed char param, signed char *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_char(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_char(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int pow_signed_char_3(Py_ssize_t arraylen, signed char param, signed char *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_signed_char(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_signed_char(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int pow_signed_char_4(Py_ssize_t arraylen, signed char param, signed char *data2, signed char *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_char(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_char(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int pow_signed_char_5(Py_ssize_t arraylen, signed char *data1, signed char *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_char(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_char(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int pow_signed_char_6(Py_ssize_t arraylen, signed char *data1, signed char *data2, signed char *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_char(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_char(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}



// Return x raised to the power of y.
unsigned char arith_pow_unsigned_char(unsigned char x, unsigned char y, char *errflag) {
	unsigned char i, z, ovtmp1;
	z = 1;
	*errflag = 0;

	// Special case for raise to the power of zero.
	if (y == 0) { return 1; }

	// We need this special case to avoid dividing by zero.
	if (x == 0) {return 0;}

	ovtmp1 = UCHAR_MAX / x;
	for (i = 0; i < y; i++) {
		if (z > ovtmp1) {*errflag = ARR_ERR_OVFL; return z;}
		z = z * x;
	}
	return z;
}

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
signed int pow_unsigned_char_1(Py_ssize_t arraylen, unsigned char *data1, unsigned char param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_char(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_char(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int pow_unsigned_char_2(Py_ssize_t arraylen, unsigned char *data1, unsigned char param, unsigned char *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_char(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_char(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int pow_unsigned_char_3(Py_ssize_t arraylen, unsigned char param, unsigned char *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_unsigned_char(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_unsigned_char(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int pow_unsigned_char_4(Py_ssize_t arraylen, unsigned char param, unsigned char *data2, unsigned char *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_char(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_char(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int pow_unsigned_char_5(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_char(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_char(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int pow_unsigned_char_6(Py_ssize_t arraylen, unsigned char *data1, unsigned char *data2, unsigned char *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_char(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_char(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}



/*--------------------------------------------------------------------------- */

// Note: The guard calculations for negative need to use abs(x) instead of -x
// because of problems with Microsoft MSVS 2010. MSVS was confused by negating
// a negative number with minimum integers (e.g. INT_MIN) and producing a
// positive result.

// Return x raised to the power of y.
signed short arith_pow_signed_short(signed short x, signed short y, char *errflag) {
	signed short i, z, ovtmp1, ovtmp2;
	z = 1;
	*errflag = 0;

	// We don't allow negative powers for integers.
	if (y < 0) {
		*errflag = ARR_ERR_VALUE_ERR;
		return z;
	}

	// Special case for raise to the power of zero.
	if (y == 0) { return 1; }

	// We need this special case to avoid dividing by zero.
	if (x == 0) {return 0;}

	if (x > 0) {
		ovtmp1 = SHRT_MAX / x;
		for (i = 0; i < y; i++) {
			if (z > ovtmp1) {*errflag = ARR_ERR_OVFL; return z;}
			z = z * x;
		}
	} else {
		ovtmp1 = SHRT_MAX / abs(x);
		ovtmp2 = SHRT_MIN / abs(x);
		for (i = 0; i < y; i++) {
			if ((z > ovtmp1) || (z < ovtmp2)) {*errflag = ARR_ERR_OVFL; return z;}
			z = z * x;
		}
	}
	return z;
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
signed int pow_signed_short_1(Py_ssize_t arraylen, signed short *data1, signed short param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_short(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_short(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int pow_signed_short_2(Py_ssize_t arraylen, signed short *data1, signed short param, signed short *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_short(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_short(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int pow_signed_short_3(Py_ssize_t arraylen, signed short param, signed short *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_signed_short(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_signed_short(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int pow_signed_short_4(Py_ssize_t arraylen, signed short param, signed short *data2, signed short *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_short(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_short(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int pow_signed_short_5(Py_ssize_t arraylen, signed short *data1, signed short *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_short(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_short(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int pow_signed_short_6(Py_ssize_t arraylen, signed short *data1, signed short *data2, signed short *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_short(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_short(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}



// Return x raised to the power of y.
unsigned short arith_pow_unsigned_short(unsigned short x, unsigned short y, char *errflag) {
	unsigned short i, z, ovtmp1;
	z = 1;
	*errflag = 0;

	// Special case for raise to the power of zero.
	if (y == 0) { return 1; }

	// We need this special case to avoid dividing by zero.
	if (x == 0) {return 0;}

	ovtmp1 = USHRT_MAX / x;
	for (i = 0; i < y; i++) {
		if (z > ovtmp1) {*errflag = ARR_ERR_OVFL; return z;}
		z = z * x;
	}
	return z;
}

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
signed int pow_unsigned_short_1(Py_ssize_t arraylen, unsigned short *data1, unsigned short param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_short(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_short(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int pow_unsigned_short_2(Py_ssize_t arraylen, unsigned short *data1, unsigned short param, unsigned short *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_short(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_short(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int pow_unsigned_short_3(Py_ssize_t arraylen, unsigned short param, unsigned short *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_unsigned_short(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_unsigned_short(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int pow_unsigned_short_4(Py_ssize_t arraylen, unsigned short param, unsigned short *data2, unsigned short *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_short(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_short(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int pow_unsigned_short_5(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_short(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_short(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int pow_unsigned_short_6(Py_ssize_t arraylen, unsigned short *data1, unsigned short *data2, unsigned short *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_short(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_short(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}



/*--------------------------------------------------------------------------- */

// Note: The guard calculations for negative need to use abs(x) instead of -x
// because of problems with Microsoft MSVS 2010. MSVS was confused by negating
// a negative number with minimum integers (e.g. INT_MIN) and producing a
// positive result.

// Return x raised to the power of y.
signed int arith_pow_signed_int(signed int x, signed int y, char *errflag) {
	signed int i, z, ovtmp1, ovtmp2;
	z = 1;
	*errflag = 0;

	// We don't allow negative powers for integers.
	if (y < 0) {
		*errflag = ARR_ERR_VALUE_ERR;
		return z;
	}

	// Special case for raise to the power of zero.
	if (y == 0) { return 1; }

	// We need this special case to avoid dividing by zero.
	if (x == 0) {return 0;}

	if (x > 0) {
		ovtmp1 = INT_MAX / x;
		for (i = 0; i < y; i++) {
			if (z > ovtmp1) {*errflag = ARR_ERR_OVFL; return z;}
			z = z * x;
		}
	} else {
		ovtmp1 = INT_MAX / abs(x);
		ovtmp2 = INT_MIN / abs(x);
		for (i = 0; i < y; i++) {
			if ((z > ovtmp1) || (z < ovtmp2)) {*errflag = ARR_ERR_OVFL; return z;}
			z = z * x;
		}
	}
	return z;
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
signed int pow_signed_int_1(Py_ssize_t arraylen, signed int *data1, signed int param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_int(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_int(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int pow_signed_int_2(Py_ssize_t arraylen, signed int *data1, signed int param, signed int *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_int(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_int(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int pow_signed_int_3(Py_ssize_t arraylen, signed int param, signed int *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_signed_int(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_signed_int(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int pow_signed_int_4(Py_ssize_t arraylen, signed int param, signed int *data2, signed int *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_int(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_int(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int pow_signed_int_5(Py_ssize_t arraylen, signed int *data1, signed int *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_int(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_int(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int pow_signed_int_6(Py_ssize_t arraylen, signed int *data1, signed int *data2, signed int *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_int(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_int(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}



// Return x raised to the power of y.
unsigned int arith_pow_unsigned_int(unsigned int x, unsigned int y, char *errflag) {
	unsigned int i, z, ovtmp1;
	z = 1;
	*errflag = 0;

	// Special case for raise to the power of zero.
	if (y == 0) { return 1; }

	// We need this special case to avoid dividing by zero.
	if (x == 0) {return 0;}

	ovtmp1 = UINT_MAX / x;
	for (i = 0; i < y; i++) {
		if (z > ovtmp1) {*errflag = ARR_ERR_OVFL; return z;}
		z = z * x;
	}
	return z;
}

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
signed int pow_unsigned_int_1(Py_ssize_t arraylen, unsigned int *data1, unsigned int param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_int(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_int(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int pow_unsigned_int_2(Py_ssize_t arraylen, unsigned int *data1, unsigned int param, unsigned int *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_int(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_int(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int pow_unsigned_int_3(Py_ssize_t arraylen, unsigned int param, unsigned int *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_unsigned_int(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_unsigned_int(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int pow_unsigned_int_4(Py_ssize_t arraylen, unsigned int param, unsigned int *data2, unsigned int *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_int(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_int(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int pow_unsigned_int_5(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_int(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_int(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int pow_unsigned_int_6(Py_ssize_t arraylen, unsigned int *data1, unsigned int *data2, unsigned int *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_int(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_int(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}



/*--------------------------------------------------------------------------- */

// Note: The guard calculations for negative need to use abs(x) instead of -x
// because of problems with Microsoft MSVS 2010. MSVS was confused by negating
// a negative number with minimum integers (e.g. INT_MIN) and producing a
// positive result.

// Return x raised to the power of y.
signed long arith_pow_signed_long(signed long x, signed long y, char *errflag) {
	signed long i, z, ovtmp1, ovtmp2;
	z = 1;
	*errflag = 0;

	// We don't allow negative powers for integers.
	if (y < 0) {
		*errflag = ARR_ERR_VALUE_ERR;
		return z;
	}

	// Special case for raise to the power of zero.
	if (y == 0) { return 1; }

	// We need this special case to avoid dividing by zero.
	if (x == 0) {return 0;}

	if (x > 0) {
		ovtmp1 = LONG_MAX / x;
		for (i = 0; i < y; i++) {
			if (z > ovtmp1) {*errflag = ARR_ERR_OVFL; return z;}
			z = z * x;
		}
	} else {
		ovtmp1 = LONG_MAX / labs(x);
		ovtmp2 = LONG_MIN / labs(x);
		for (i = 0; i < y; i++) {
			if ((z > ovtmp1) || (z < ovtmp2)) {*errflag = ARR_ERR_OVFL; return z;}
			z = z * x;
		}
	}
	return z;
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
signed int pow_signed_long_1(Py_ssize_t arraylen, signed long *data1, signed long param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_long(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_long(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int pow_signed_long_2(Py_ssize_t arraylen, signed long *data1, signed long param, signed long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_long(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_long(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int pow_signed_long_3(Py_ssize_t arraylen, signed long param, signed long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_signed_long(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_signed_long(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int pow_signed_long_4(Py_ssize_t arraylen, signed long param, signed long *data2, signed long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_long(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_long(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int pow_signed_long_5(Py_ssize_t arraylen, signed long *data1, signed long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_long(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_long(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int pow_signed_long_6(Py_ssize_t arraylen, signed long *data1, signed long *data2, signed long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_long(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_long(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}



// Return x raised to the power of y.
unsigned long arith_pow_unsigned_long(unsigned long x, unsigned long y, char *errflag) {
	unsigned long i, z, ovtmp1;
	z = 1;
	*errflag = 0;

	// Special case for raise to the power of zero.
	if (y == 0) { return 1; }

	// We need this special case to avoid dividing by zero.
	if (x == 0) {return 0;}

	ovtmp1 = ULONG_MAX / x;
	for (i = 0; i < y; i++) {
		if (z > ovtmp1) {*errflag = ARR_ERR_OVFL; return z;}
		z = z * x;
	}
	return z;
}

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
signed int pow_unsigned_long_1(Py_ssize_t arraylen, unsigned long *data1, unsigned long param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_long(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_long(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int pow_unsigned_long_2(Py_ssize_t arraylen, unsigned long *data1, unsigned long param, unsigned long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_long(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_long(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int pow_unsigned_long_3(Py_ssize_t arraylen, unsigned long param, unsigned long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_unsigned_long(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_unsigned_long(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int pow_unsigned_long_4(Py_ssize_t arraylen, unsigned long param, unsigned long *data2, unsigned long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_long(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_long(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int pow_unsigned_long_5(Py_ssize_t arraylen, unsigned long *data1, unsigned long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_long(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_long(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int pow_unsigned_long_6(Py_ssize_t arraylen, unsigned long *data1, unsigned long *data2, unsigned long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_long(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_long(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}



/*--------------------------------------------------------------------------- */

// Note: The guard calculations for negative need to use abs(x) instead of -x
// because of problems with Microsoft MSVS 2010. MSVS was confused by negating
// a negative number with minimum integers (e.g. INT_MIN) and producing a
// positive result.

// Return x raised to the power of y.
signed long long arith_pow_signed_long_long(signed long long x, signed long long y, char *errflag) {
	signed long long i, z, ovtmp1, ovtmp2;
	z = 1;
	*errflag = 0;

	// We don't allow negative powers for integers.
	if (y < 0) {
		*errflag = ARR_ERR_VALUE_ERR;
		return z;
	}

	// Special case for raise to the power of zero.
	if (y == 0) { return 1; }

	// We need this special case to avoid dividing by zero.
	if (x == 0) {return 0;}

	if (x > 0) {
		ovtmp1 = LLONG_MAX / x;
		for (i = 0; i < y; i++) {
			if (z > ovtmp1) {*errflag = ARR_ERR_OVFL; return z;}
			z = z * x;
		}
	} else {
		ovtmp1 = LLONG_MAX / llabs(x);
		ovtmp2 = LLONG_MIN / llabs(x);
		for (i = 0; i < y; i++) {
			if ((z > ovtmp1) || (z < ovtmp2)) {*errflag = ARR_ERR_OVFL; return z;}
			z = z * x;
		}
	}
	return z;
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
signed int pow_signed_long_long_1(Py_ssize_t arraylen, signed long long *data1, signed long long param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_long_long(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_long_long(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int pow_signed_long_long_2(Py_ssize_t arraylen, signed long long *data1, signed long long param, signed long long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_long_long(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_long_long(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int pow_signed_long_long_3(Py_ssize_t arraylen, signed long long param, signed long long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_signed_long_long(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_signed_long_long(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int pow_signed_long_long_4(Py_ssize_t arraylen, signed long long param, signed long long *data2, signed long long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_long_long(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_long_long(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int pow_signed_long_long_5(Py_ssize_t arraylen, signed long long *data1, signed long long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_long_long(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_signed_long_long(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int pow_signed_long_long_6(Py_ssize_t arraylen, signed long long *data1, signed long long *data2, signed long long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_long_long(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_signed_long_long(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}



// Return x raised to the power of y.
unsigned long long arith_pow_unsigned_long_long(unsigned long long x, unsigned long long y, char *errflag) {
	unsigned long long i, z, ovtmp1;
	z = 1;
	*errflag = 0;

	// Special case for raise to the power of zero.
	if (y == 0) { return 1; }

	// We need this special case to avoid dividing by zero.
	if (x == 0) {return 0;}

	ovtmp1 = ULLONG_MAX / x;
	for (i = 0; i < y; i++) {
		if (z > ovtmp1) {*errflag = ARR_ERR_OVFL; return z;}
		z = z * x;
	}
	return z;
}

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
signed int pow_unsigned_long_long_1(Py_ssize_t arraylen, unsigned long long *data1, unsigned long long param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_long_long(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_long_long(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int pow_unsigned_long_long_2(Py_ssize_t arraylen, unsigned long long *data1, unsigned long long param, unsigned long long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_long_long(data1[x], param, &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_long_long(data1[x], param, &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int pow_unsigned_long_long_3(Py_ssize_t arraylen, unsigned long long param, unsigned long long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_unsigned_long_long(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data2[x] = arith_pow_unsigned_long_long(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int pow_unsigned_long_long_4(Py_ssize_t arraylen, unsigned long long param, unsigned long long *data2, unsigned long long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_long_long(param, data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_long_long(param, data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int pow_unsigned_long_long_5(Py_ssize_t arraylen, unsigned long long *data1, unsigned long long *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_long_long(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = arith_pow_unsigned_long_long(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int pow_unsigned_long_long_6(Py_ssize_t arraylen, unsigned long long *data1, unsigned long long *data2, unsigned long long *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;
	char errflag = 0;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_long_long(data1[x], data2[x], &errflag);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = arith_pow_unsigned_long_long(data1[x], data2[x], &errflag);
			if (errflag != 0) return ARR_ERR_OVFL;
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
signed int pow_float_1(Py_ssize_t arraylen, float *data1, float param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = powf(data1[x], param);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data1[x] = powf(data1[x], param);
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int pow_float_2(Py_ssize_t arraylen, float *data1, float param, float *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = powf(data1[x], param);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data3[x] = powf(data1[x], param);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int pow_float_3(Py_ssize_t arraylen, float param, float *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = powf(param, data2[x]);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data2[x] = powf(param, data2[x]);
			if (!isfinite(data2[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int pow_float_4(Py_ssize_t arraylen, float param, float *data2, float *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = powf(param, data2[x]);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data3[x] = powf(param, data2[x]);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int pow_float_5(Py_ssize_t arraylen, float *data1, float *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = powf(data1[x], data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = powf(data1[x], data2[x]);
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int pow_float_6(Py_ssize_t arraylen, float *data1, float *data2, float *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = powf(data1[x], data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = powf(data1[x], data2[x]);
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
signed int pow_double_1(Py_ssize_t arraylen, double *data1, double param, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = pow(data1[x], param);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data1[x] = pow(data1[x], param);
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_num_arr
signed int pow_double_2(Py_ssize_t arraylen, double *data1, double param, double *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = pow(data1[x], param);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data3[x] = pow(data1[x], param);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_none
signed int pow_double_3(Py_ssize_t arraylen, double param, double *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data2[x] = pow(param, data2[x]);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data2[x] = pow(param, data2[x]);
			if (!isfinite(data2[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_num_arr_arr
signed int pow_double_4(Py_ssize_t arraylen, double param, double *data2, double *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = pow(param, data2[x]);
		}
	} else {
		for (x = 0; x < arraylen; x++) {
			data3[x] = pow(param, data2[x]);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_none
signed int pow_double_5(Py_ssize_t arraylen, double *data1, double *data2, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data1[x] = pow(data1[x], data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data1[x] = pow(data1[x], data2[x]);
			if (!isfinite(data1[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}


// param_arr_arr_arr
signed int pow_double_6(Py_ssize_t arraylen, double *data1, double *data2, double *data3, unsigned int ignoreerrors) {

	// array index counter.
	Py_ssize_t x;


	// Math error checking disabled.
	if (ignoreerrors) {
		for (x = 0; x < arraylen; x++) {
			data3[x] = pow(data1[x], data2[x]);
		}
	} else {
	// Math error checking enabled.
		for (x = 0; x < arraylen; x++) {
			data3[x] = pow(data1[x], data2[x]);
			if (!isfinite(data3[x])) {return ARR_ERR_ARITHMETIC;}
		}
	}
	return ARR_NO_ERR;

}

/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_pow(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;

	// This is used to hold the parsed parameters.
	struct args_params_2 arraydata = ARGSINIT_TWO;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_two(self, args, keywds, 1, 0, "pow");

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
					resultcode = pow_signed_char_1(arraydata.arraylength, arraydata.array1.b, arraydata.param.b, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = pow_signed_char_2(arraydata.arraylength, arraydata.array1.b, arraydata.param.b, arraydata.array3.b, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = pow_signed_char_3(arraydata.arraylength, arraydata.param.b, arraydata.array2.b, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = pow_signed_char_4(arraydata.arraylength, arraydata.param.b, arraydata.array2.b, arraydata.array3.b, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = pow_signed_char_5(arraydata.arraylength, arraydata.array1.b, arraydata.array2.b, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = pow_signed_char_6(arraydata.arraylength, arraydata.array1.b, arraydata.array2.b, arraydata.array3.b, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// unsigned_char
		case 'B' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = pow_unsigned_char_1(arraydata.arraylength, arraydata.array1.B, arraydata.param.B, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = pow_unsigned_char_2(arraydata.arraylength, arraydata.array1.B, arraydata.param.B, arraydata.array3.B, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = pow_unsigned_char_3(arraydata.arraylength, arraydata.param.B, arraydata.array2.B, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = pow_unsigned_char_4(arraydata.arraylength, arraydata.param.B, arraydata.array2.B, arraydata.array3.B, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = pow_unsigned_char_5(arraydata.arraylength, arraydata.array1.B, arraydata.array2.B, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = pow_unsigned_char_6(arraydata.arraylength, arraydata.array1.B, arraydata.array2.B, arraydata.array3.B, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// signed_short
		case 'h' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = pow_signed_short_1(arraydata.arraylength, arraydata.array1.h, arraydata.param.h, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = pow_signed_short_2(arraydata.arraylength, arraydata.array1.h, arraydata.param.h, arraydata.array3.h, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = pow_signed_short_3(arraydata.arraylength, arraydata.param.h, arraydata.array2.h, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = pow_signed_short_4(arraydata.arraylength, arraydata.param.h, arraydata.array2.h, arraydata.array3.h, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = pow_signed_short_5(arraydata.arraylength, arraydata.array1.h, arraydata.array2.h, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = pow_signed_short_6(arraydata.arraylength, arraydata.array1.h, arraydata.array2.h, arraydata.array3.h, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// unsigned_short
		case 'H' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = pow_unsigned_short_1(arraydata.arraylength, arraydata.array1.H, arraydata.param.H, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = pow_unsigned_short_2(arraydata.arraylength, arraydata.array1.H, arraydata.param.H, arraydata.array3.H, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = pow_unsigned_short_3(arraydata.arraylength, arraydata.param.H, arraydata.array2.H, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = pow_unsigned_short_4(arraydata.arraylength, arraydata.param.H, arraydata.array2.H, arraydata.array3.H, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = pow_unsigned_short_5(arraydata.arraylength, arraydata.array1.H, arraydata.array2.H, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = pow_unsigned_short_6(arraydata.arraylength, arraydata.array1.H, arraydata.array2.H, arraydata.array3.H, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// signed_int
		case 'i' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = pow_signed_int_1(arraydata.arraylength, arraydata.array1.i, arraydata.param.i, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = pow_signed_int_2(arraydata.arraylength, arraydata.array1.i, arraydata.param.i, arraydata.array3.i, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = pow_signed_int_3(arraydata.arraylength, arraydata.param.i, arraydata.array2.i, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = pow_signed_int_4(arraydata.arraylength, arraydata.param.i, arraydata.array2.i, arraydata.array3.i, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = pow_signed_int_5(arraydata.arraylength, arraydata.array1.i, arraydata.array2.i, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = pow_signed_int_6(arraydata.arraylength, arraydata.array1.i, arraydata.array2.i, arraydata.array3.i, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// unsigned_int
		case 'I' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = pow_unsigned_int_1(arraydata.arraylength, arraydata.array1.I, arraydata.param.I, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = pow_unsigned_int_2(arraydata.arraylength, arraydata.array1.I, arraydata.param.I, arraydata.array3.I, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = pow_unsigned_int_3(arraydata.arraylength, arraydata.param.I, arraydata.array2.I, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = pow_unsigned_int_4(arraydata.arraylength, arraydata.param.I, arraydata.array2.I, arraydata.array3.I, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = pow_unsigned_int_5(arraydata.arraylength, arraydata.array1.I, arraydata.array2.I, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = pow_unsigned_int_6(arraydata.arraylength, arraydata.array1.I, arraydata.array2.I, arraydata.array3.I, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// signed_long
		case 'l' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = pow_signed_long_1(arraydata.arraylength, arraydata.array1.l, arraydata.param.l, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = pow_signed_long_2(arraydata.arraylength, arraydata.array1.l, arraydata.param.l, arraydata.array3.l, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = pow_signed_long_3(arraydata.arraylength, arraydata.param.l, arraydata.array2.l, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = pow_signed_long_4(arraydata.arraylength, arraydata.param.l, arraydata.array2.l, arraydata.array3.l, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = pow_signed_long_5(arraydata.arraylength, arraydata.array1.l, arraydata.array2.l, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = pow_signed_long_6(arraydata.arraylength, arraydata.array1.l, arraydata.array2.l, arraydata.array3.l, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// unsigned_long
		case 'L' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = pow_unsigned_long_1(arraydata.arraylength, arraydata.array1.L, arraydata.param.L, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = pow_unsigned_long_2(arraydata.arraylength, arraydata.array1.L, arraydata.param.L, arraydata.array3.L, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = pow_unsigned_long_3(arraydata.arraylength, arraydata.param.L, arraydata.array2.L, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = pow_unsigned_long_4(arraydata.arraylength, arraydata.param.L, arraydata.array2.L, arraydata.array3.L, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = pow_unsigned_long_5(arraydata.arraylength, arraydata.array1.L, arraydata.array2.L, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = pow_unsigned_long_6(arraydata.arraylength, arraydata.array1.L, arraydata.array2.L, arraydata.array3.L, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// signed_long_long
		case 'q' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = pow_signed_long_long_1(arraydata.arraylength, arraydata.array1.q, arraydata.param.q, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = pow_signed_long_long_2(arraydata.arraylength, arraydata.array1.q, arraydata.param.q, arraydata.array3.q, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = pow_signed_long_long_3(arraydata.arraylength, arraydata.param.q, arraydata.array2.q, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = pow_signed_long_long_4(arraydata.arraylength, arraydata.param.q, arraydata.array2.q, arraydata.array3.q, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = pow_signed_long_long_5(arraydata.arraylength, arraydata.array1.q, arraydata.array2.q, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = pow_signed_long_long_6(arraydata.arraylength, arraydata.array1.q, arraydata.array2.q, arraydata.array3.q, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// unsigned_long_long
		case 'Q' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = pow_unsigned_long_long_1(arraydata.arraylength, arraydata.array1.Q, arraydata.param.Q, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = pow_unsigned_long_long_2(arraydata.arraylength, arraydata.array1.Q, arraydata.param.Q, arraydata.array3.Q, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = pow_unsigned_long_long_3(arraydata.arraylength, arraydata.param.Q, arraydata.array2.Q, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = pow_unsigned_long_long_4(arraydata.arraylength, arraydata.param.Q, arraydata.array2.Q, arraydata.array3.Q, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = pow_unsigned_long_long_5(arraydata.arraylength, arraydata.array1.Q, arraydata.array2.Q, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = pow_unsigned_long_long_6(arraydata.arraylength, arraydata.array1.Q, arraydata.array2.Q, arraydata.array3.Q, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// float
		case 'f' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = pow_float_1(arraydata.arraylength, arraydata.array1.f, arraydata.param.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = pow_float_2(arraydata.arraylength, arraydata.array1.f, arraydata.param.f, arraydata.array3.f, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = pow_float_3(arraydata.arraylength, arraydata.param.f, arraydata.array2.f, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = pow_float_4(arraydata.arraylength, arraydata.param.f, arraydata.array2.f, arraydata.array3.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = pow_float_5(arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = pow_float_6(arraydata.arraylength, arraydata.array1.f, arraydata.array2.f, arraydata.array3.f, arraydata.ignoreerrors);
					break;
				}
			}
			break;
		}

		// double
		case 'd' : {
			switch (arraydata.paramcat) {
				case param_arr_num_none : {
					resultcode = pow_double_1(arraydata.arraylength, arraydata.array1.d, arraydata.param.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_num_arr : {
					resultcode = pow_double_2(arraydata.arraylength, arraydata.array1.d, arraydata.param.d, arraydata.array3.d, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_none : {
					resultcode = pow_double_3(arraydata.arraylength, arraydata.param.d, arraydata.array2.d, arraydata.ignoreerrors);
					break;
				}
				case param_num_arr_arr : {
					resultcode = pow_double_4(arraydata.arraylength, arraydata.param.d, arraydata.array2.d, arraydata.array3.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_none : {
					resultcode = pow_double_5(arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.ignoreerrors);
					break;
				}
				case param_arr_arr_arr : {
					resultcode = pow_double_6(arraydata.arraylength, arraydata.array1.d, arraydata.array2.d, arraydata.array3.d, arraydata.ignoreerrors);
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
PyDoc_STRVAR(pow__doc__,
"pow \n\
_____________________________ \n\
\n\
Calculate pow over the values in an array.  \n\
\n\
======================  ============================================== \n\
Equivalent to:          [x ** param for x in array1] \n\
or                      [param ** y for y in array2] \n\
or                      [x ** y for x, y in zip(array1, array2)] \n\
======================  ============================================== \n\
\n\
======================  ============================================== \n\
Array types supported:  b, B, h, H, i, I, l, L, q, Q, f, d \n\
Exceptions raised:      OverflowError, ArithmeticError \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
  pow(array1, param) \n\
  pow(array1, param, outparray) \n\
  pow(param, array1) \n\
  pow(param, array1, outparray) \n\
  pow(array1, array2) \n\
  pow(array1, array2, outparray) \n\
  pow(array1, param, maxlen=y) \n\
  pow(array1, param, matherrors=False) \n\
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
 "pow" is the name seen inside of Python. 
 "py_pow" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef pow_methods[] = {
	{"pow",  (PyCFunction)py_pow, METH_VARARGS | METH_KEYWORDS, pow__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef powmodule = {
    PyModuleDef_HEAD_INIT,
    "pow",
    NULL,
    -1,
    pow_methods
};

PyMODINIT_FUNC PyInit_pow(void)
{
    return PyModule_Create(&powmodule);
};

/*--------------------------------------------------------------------------- */

