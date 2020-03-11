//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   factorial.c
// Purpose:  Calculate the factorial of values in an array.
// Language: C
// Date:     15-Nov-2017.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2019    Michael Griffin    <m12.griffin@gmail.com>
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
#include "arrayparams_one.h"

/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// Calculate factorials.
// We are making some assumptions here about the sizes of integers.
// Instead of calculating factorials using a loop, we create a series of 
// look-up tables. This seems to be about 5 to 20 times faster than using
// a loop and test method.


// Factorial data.

// The default value to return when a factorial calculation was in error.
#define DEFAULT_FACT 0

// Signed and unsigned chars.
#define MAX_SC_FACT 5
signed char fact_sc_data[] = {1, 1, 2, 6, 24, 120};
#define MAX_USC_FACT 5
unsigned char fact_usc_data[] = {1, 1, 2, 6, 24, 120};

// Signed and unsigned shorts.
#define MAX_SS_FACT 7
signed short fact_ss_data[] = {1, 1, 2, 6, 24, 120, 720, 5040};
#define MAX_USS_FACT 8
unsigned short fact_uss_data[] = {1, 1, 2, 6, 24, 120, 720, 5040, 40320};


// Signed and unsigned ints.
#define MAX_SI_FACT 12
signed int fact_si_data[] = {1, 1, 2, 6, 24, 120, 720, 5040, 5040, 40320, 362880, 3628800, 39916800, 479001600};
#define MAX_USI_FACT 12
unsigned int fact_usi_data[] = {1, 1, 2, 6, 24, 120, 720, 5040, 5040, 40320, 362880, 3628800, 39916800, 479001600};


// Signed and unsigned long.
// Check if long integer is 8 bytes.
#if LONG_MAX == 9223372036854775807

#define MAX_SL_FACT 20
signed long fact_sl_data[] = {1, 1, 2, 6, 24, 120, 720, 5040, 5040, 40320, 362880, 
				3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 
				20922789888000, 355687428096000, 6402373705728000, 121645100408832000,
				2432902008176640000};
#define MAX_USL_FACT 20
unsigned long fact_usl_data[] = {1, 1, 2, 6, 24, 120, 720, 5040, 5040, 40320, 362880, 
				3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 
				20922789888000, 355687428096000, 6402373705728000, 121645100408832000,
				2432902008176640000};

// Long integers are assumed to be 4 bytes.
#else

#define MAX_SL_FACT 12
signed long fact_sl_data[] = {1, 1, 2, 6, 24, 120, 720, 5040};
#define MAX_USL_FACT 12
unsigned long fact_usl_data[] = {1, 1, 2, 6, 24, 120, 720, 5040, 5040, 40320, 362880, 3628800, 39916800, 479001600};

#endif // End for long integer.

#define MAX_SLL_FACT 20
signed long long fact_sll_data[] = {1, 1, 2, 6, 24, 120, 720, 5040, 5040, 40320, 362880, 
				3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 
				20922789888000, 355687428096000, 6402373705728000, 121645100408832000,
				2432902008176640000};
#define MAX_USLL_FACT 20
unsigned long long fact_usll_data[] = {1, 1, 2, 6, 24, 120, 720, 5040, 5040, 40320, 362880, 
				3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 
				20922789888000, 355687428096000, 6402373705728000, 121645100408832000,
				2432902008176640000};

/*--------------------------------------------------------------------------- */


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int factorial_signed_char(Py_ssize_t arraylen, signed char *data, signed char *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Factorial is not defined for negative values, and there is
	// a limit to the size of factorial that can be calculated.

	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SC_FACT)) {
					dataout[x] = DEFAULT_FACT;
				} else {
					dataout[x] = fact_sc_data[data[x]];
				}
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SC_FACT)) {
					data[x] = DEFAULT_FACT;
				} else {
					data[x] = fact_sc_data[data[x]];
				}
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SC_FACT)) {
					return ARR_ERR_OVFL;
				}
				dataout[x] = fact_sc_data[data[x]];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SC_FACT)) {
					return ARR_ERR_OVFL;
				}
				data[x] = fact_sc_data[data[x]];
			}
		}
	}

	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int factorial_unsigned_char(Py_ssize_t arraylen, unsigned char *data, unsigned char *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Factorial is not defined for negative values, and there is
	// a limit to the size of factorial that can be calculated.

	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USC_FACT) {
					dataout[x] = DEFAULT_FACT;
				} else {
					dataout[x] = fact_usc_data[data[x]];
				}
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USC_FACT) {
					data[x] = DEFAULT_FACT;
				} else {
					data[x] = fact_usc_data[data[x]];
				}
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USC_FACT) {
					return ARR_ERR_OVFL;
				}
				dataout[x] = fact_usc_data[data[x]];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USC_FACT) {
					return ARR_ERR_OVFL;
				}
				data[x] = fact_usc_data[data[x]];
			}
		}
	}

	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int factorial_signed_short(Py_ssize_t arraylen, signed short *data, signed short *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Factorial is not defined for negative values, and there is
	// a limit to the size of factorial that can be calculated.

	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SS_FACT)) {
					dataout[x] = DEFAULT_FACT;
				} else {
					dataout[x] = fact_ss_data[data[x]];
				}
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SS_FACT)) {
					data[x] = DEFAULT_FACT;
				} else {
					data[x] = fact_ss_data[data[x]];
				}
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SS_FACT)) {
					return ARR_ERR_OVFL;
				}
				dataout[x] = fact_ss_data[data[x]];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SS_FACT)) {
					return ARR_ERR_OVFL;
				}
				data[x] = fact_ss_data[data[x]];
			}
		}
	}

	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int factorial_unsigned_short(Py_ssize_t arraylen, unsigned short *data, unsigned short *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Factorial is not defined for negative values, and there is
	// a limit to the size of factorial that can be calculated.

	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USS_FACT) {
					dataout[x] = DEFAULT_FACT;
				} else {
					dataout[x] = fact_uss_data[data[x]];
				}
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USS_FACT) {
					data[x] = DEFAULT_FACT;
				} else {
					data[x] = fact_uss_data[data[x]];
				}
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USS_FACT) {
					return ARR_ERR_OVFL;
				}
				dataout[x] = fact_uss_data[data[x]];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USS_FACT) {
					return ARR_ERR_OVFL;
				}
				data[x] = fact_uss_data[data[x]];
			}
		}
	}

	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int factorial_signed_int(Py_ssize_t arraylen, signed int *data, signed int *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Factorial is not defined for negative values, and there is
	// a limit to the size of factorial that can be calculated.

	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SI_FACT)) {
					dataout[x] = DEFAULT_FACT;
				} else {
					dataout[x] = fact_si_data[data[x]];
				}
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SI_FACT)) {
					data[x] = DEFAULT_FACT;
				} else {
					data[x] = fact_si_data[data[x]];
				}
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SI_FACT)) {
					return ARR_ERR_OVFL;
				}
				dataout[x] = fact_si_data[data[x]];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SI_FACT)) {
					return ARR_ERR_OVFL;
				}
				data[x] = fact_si_data[data[x]];
			}
		}
	}

	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int factorial_unsigned_int(Py_ssize_t arraylen, unsigned int *data, unsigned int *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Factorial is not defined for negative values, and there is
	// a limit to the size of factorial that can be calculated.

	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USI_FACT) {
					dataout[x] = DEFAULT_FACT;
				} else {
					dataout[x] = fact_usi_data[data[x]];
				}
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USI_FACT) {
					data[x] = DEFAULT_FACT;
				} else {
					data[x] = fact_usi_data[data[x]];
				}
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USI_FACT) {
					return ARR_ERR_OVFL;
				}
				dataout[x] = fact_usi_data[data[x]];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USI_FACT) {
					return ARR_ERR_OVFL;
				}
				data[x] = fact_usi_data[data[x]];
			}
		}
	}

	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int factorial_signed_long(Py_ssize_t arraylen, signed long *data, signed long *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Factorial is not defined for negative values, and there is
	// a limit to the size of factorial that can be calculated.

	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SL_FACT)) {
					dataout[x] = DEFAULT_FACT;
				} else {
					dataout[x] = fact_sl_data[data[x]];
				}
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SL_FACT)) {
					data[x] = DEFAULT_FACT;
				} else {
					data[x] = fact_sl_data[data[x]];
				}
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SL_FACT)) {
					return ARR_ERR_OVFL;
				}
				dataout[x] = fact_sl_data[data[x]];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SL_FACT)) {
					return ARR_ERR_OVFL;
				}
				data[x] = fact_sl_data[data[x]];
			}
		}
	}

	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int factorial_unsigned_long(Py_ssize_t arraylen, unsigned long *data, unsigned long *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Factorial is not defined for negative values, and there is
	// a limit to the size of factorial that can be calculated.

	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USL_FACT) {
					dataout[x] = DEFAULT_FACT;
				} else {
					dataout[x] = fact_usl_data[data[x]];
				}
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USL_FACT) {
					data[x] = DEFAULT_FACT;
				} else {
					data[x] = fact_usl_data[data[x]];
				}
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USL_FACT) {
					return ARR_ERR_OVFL;
				}
				dataout[x] = fact_usl_data[data[x]];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USL_FACT) {
					return ARR_ERR_OVFL;
				}
				data[x] = fact_usl_data[data[x]];
			}
		}
	}

	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int factorial_signed_long_long(Py_ssize_t arraylen, signed long long *data, signed long long *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Factorial is not defined for negative values, and there is
	// a limit to the size of factorial that can be calculated.

	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SLL_FACT)) {
					dataout[x] = DEFAULT_FACT;
				} else {
					dataout[x] = fact_sll_data[data[x]];
				}
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SLL_FACT)) {
					data[x] = DEFAULT_FACT;
				} else {
					data[x] = fact_sll_data[data[x]];
				}
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SLL_FACT)) {
					return ARR_ERR_OVFL;
				}
				dataout[x] = fact_sll_data[data[x]];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if ((data[x] < 0) || (data[x] > MAX_SLL_FACT)) {
					return ARR_ERR_OVFL;
				}
				data[x] = fact_sll_data[data[x]];
			}
		}
	}

	return ARR_NO_ERR;

}


/*--------------------------------------------------------------------------- */
/* arraylen = The length of the data arrays.
   data = The input data array.
   dataout = The output data array.
   ignoreerrors = If true, disable arithmetic math error checking (default is false).
   hasoutputarray = If true, the output goes into the second array.
*/
signed int factorial_unsigned_long_long(Py_ssize_t arraylen, unsigned long long *data, unsigned long long *dataout, unsigned int ignoreerrors, bool hasoutputarray) {

	// array index counter.
	Py_ssize_t x;


	// Factorial is not defined for negative values, and there is
	// a limit to the size of factorial that can be calculated.

	// Math error checking disabled.
	if (ignoreerrors) {
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USLL_FACT) {
					dataout[x] = DEFAULT_FACT;
				} else {
					dataout[x] = fact_usll_data[data[x]];
				}
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USLL_FACT) {
					data[x] = DEFAULT_FACT;
				} else {
					data[x] = fact_usll_data[data[x]];
				}
			}
		}
	} else {
	// Math error checking enabled.
		if (hasoutputarray) {		
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USLL_FACT) {
					return ARR_ERR_OVFL;
				}
				dataout[x] = fact_usll_data[data[x]];
			}
		} else {
			for(x = 0; x < arraylen; x++) {
				if (data[x] > MAX_USLL_FACT) {
					return ARR_ERR_OVFL;
				}
				data[x] = fact_usll_data[data[x]];
			}
		}
	}

	return ARR_NO_ERR;

}



/*--------------------------------------------------------------------------- */

/* The wrapper to the underlying C function */
static PyObject *py_factorial(PyObject *self, PyObject *args, PyObject *keywds) {


	// The error code returned by the function.
	signed int resultcode = -1;

	// This is used to hold the parsed parameters.
	struct args_params_1 arraydata = ARGSINIT_ONE;

	// -----------------------------------------------------


	// Get the parameters passed from Python.
	arraydata = getparams_one(self, args, keywds, 1, "factorial");

	// If there was an error, we count on the parameter parsing function to 
	// release the buffers if this was necessary.
	if (arraydata.error) {
		return NULL;
	}

	// Call the C function.
	switch(arraydata.arraytype) {

		// signed_char
		case 'b' : {
			resultcode = factorial_signed_char(arraydata.arraylength, arraydata.array1.b, arraydata.array2.b, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// unsigned_char
		case 'B' : {
			resultcode = factorial_unsigned_char(arraydata.arraylength, arraydata.array1.B, arraydata.array2.B, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// signed_short
		case 'h' : {
			resultcode = factorial_signed_short(arraydata.arraylength, arraydata.array1.h, arraydata.array2.h, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// unsigned_short
		case 'H' : {
			resultcode = factorial_unsigned_short(arraydata.arraylength, arraydata.array1.H, arraydata.array2.H, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// signed_int
		case 'i' : {
			resultcode = factorial_signed_int(arraydata.arraylength, arraydata.array1.i, arraydata.array2.i, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// unsigned_int
		case 'I' : {
			resultcode = factorial_unsigned_int(arraydata.arraylength, arraydata.array1.I, arraydata.array2.I, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// signed_long
		case 'l' : {
			resultcode = factorial_signed_long(arraydata.arraylength, arraydata.array1.l, arraydata.array2.l, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// unsigned_long
		case 'L' : {
			resultcode = factorial_unsigned_long(arraydata.arraylength, arraydata.array1.L, arraydata.array2.L, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// signed_long_long
		case 'q' : {
			resultcode = factorial_signed_long_long(arraydata.arraylength, arraydata.array1.q, arraydata.array2.q, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// unsigned_long_long
		case 'Q' : {
			resultcode = factorial_unsigned_long_long(arraydata.arraylength, arraydata.array1.Q, arraydata.array2.Q, arraydata.ignoreerrors, arraydata.hasoutputarray);
			break;
		}

		// We don't know this code.
		default: {
			releasebuffers_one(arraydata);
			ErrMsgUnknownArrayType();
			return NULL;
			break;
		}
	}

	// Release the buffers. 
	releasebuffers_one(arraydata);


	// Signal the errors.
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
PyDoc_STRVAR(factorial__doc__,
"factorial \n\
_____________________________ \n\
\n\
Calculate factorial over the values in an array.  \n\
\n\
======================  ============================================== \n\
Equivalent to:          [math.factorial(x) for x in array1] \n\
Array types supported:  b, B, h, H, i, I, l, L, q, Q \n\
Exceptions raised:      OverflowError \n\
======================  ============================================== \n\
\n\
Call formats: \n\
\n\
    factorial(array1) \n\
    factorial(array1, outparray) \n\
    factorial(array1, maxlen=y) \n\
    factorial(array1, matherrors=False)) \n\
\n\
* array1 - The first input data array to be examined. If no output \n\
  array is provided the results will overwrite the input data. \n\
* outparray - The output array. This parameter is optional. \n\
* maxlen - Limit the length of the array used. This must be a valid \n\
  positive integer. If a zero or negative length, or a value which is \n\
  greater than the actual length of the array is specified, this \n\
  parameter is ignored. \n\
* matherrors - If true, arithmetic error checking is disabled. The \n\
  default is false. \n\
");


/*--------------------------------------------------------------------------- */

/* A list of all the methods defined by this module. 
 "factorial" is the name seen inside of Python. 
 "py_factorial" is the name of the C function handling the Python call. 
 "METH_VARGS" tells Python how to call the handler. 
 The {NULL, NULL} entry indicates the end of the method definitions. */
static PyMethodDef factorial_methods[] = {
	{"factorial",  (PyCFunction)py_factorial, METH_VARARGS | METH_KEYWORDS, factorial__doc__}, 
	{NULL, NULL, 0, NULL}
};


static struct PyModuleDef factorialmodule = {
    PyModuleDef_HEAD_INIT,
    "factorial",
    NULL,
    -1,
    factorial_methods
};

PyMODINIT_FUNC PyInit_factorial(void)
{
    return PyModule_Create(&factorialmodule);
};

/*--------------------------------------------------------------------------- */

