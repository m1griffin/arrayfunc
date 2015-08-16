//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arraycalcs.c
// Purpose:  Common declarations for arrayfunc.
// Language: C
// Date:     30-Apr-2014
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

#include <math.h>
#include <limits.h>

#include "arrayfunc.h"
#include "arrayerrs.h"

/*--------------------------------------------------------------------------- */

// Calculate factorials.
// We are making some assumptions here about the sizes of integers.
// Instead of calculating factorials using a loop, we create a series of 
// look-up tables. This seems to be about 5 to 20 times faster than using
// a loop and test method.


// Factorial data.

// The default value to return when a factorial calculation was in error.
#define DEFAULT_FACT 1

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

// Return the factorial of x.
signed char factorial_signed_char(signed char x, char *errflag) {
	*errflag = 0;

	// Factorial is not defined for negative values.
	if (x < 0) {
		*errflag = ARR_ERR_VALUE_ERR;
		return DEFAULT_FACT;
	}

	// We can't calculate a factorial this big.
	if (x > MAX_SC_FACT) {
		*errflag = ARR_ERR_OVFL;
		return DEFAULT_FACT;
	}

	// Factorial can only be a limited number of values within range.
	return fact_sc_data[x];

}

// Return the factorial of x.
unsigned char factorial_unsigned_char(unsigned char x, char *errflag) {
	*errflag = 0;

	// We can't calculate a factorial this big.
	if (x > MAX_USC_FACT) {
		*errflag = ARR_ERR_OVFL;
		return DEFAULT_FACT;
	}

	// Factorial can only be a limited number of values within range.
	return fact_usc_data[x];

}



// Return the factorial of x.
signed short factorial_signed_short(signed short x, char *errflag) {
	*errflag = 0;

	// Factorial is not defined for negative values.
	if (x < 0) {
		*errflag = ARR_ERR_VALUE_ERR;
		return DEFAULT_FACT;
	}

	// We can't calculate a factorial this big.
	if (x > MAX_SS_FACT) {
		*errflag = ARR_ERR_OVFL;
		return DEFAULT_FACT;
	}

	// Factorial can only be a limited number of values within range.
	return fact_ss_data[x];

}

// Return the factorial of x.
unsigned short factorial_unsigned_short(unsigned short x, char *errflag) {
	*errflag = 0;

	// We can't calculate a factorial this big.
	if (x > MAX_USS_FACT) {
		*errflag = ARR_ERR_OVFL;
		return DEFAULT_FACT;
	}

	// Factorial can only be a limited number of values within range.
	return fact_uss_data[x];

}


// Return the factorial of x.
signed int factorial_signed_int(signed int x, char *errflag) {
	*errflag = 0;

	// Factorial is not defined for negative values.
	if (x < 0) {
		*errflag = ARR_ERR_VALUE_ERR;
		return DEFAULT_FACT;
	}

	// We can't calculate a factorial this big.
	if (x > MAX_SI_FACT) {
		*errflag = ARR_ERR_OVFL;
		return DEFAULT_FACT;
	}

	// Factorial can only be a limited number of values within range.
	return fact_si_data[x];

}

// Return the factorial of x.
unsigned int factorial_unsigned_int(unsigned int x, char *errflag) {
	*errflag = 0;

	// We can't calculate a factorial this big.
	if (x > MAX_USI_FACT) {
		*errflag = ARR_ERR_OVFL;
		return DEFAULT_FACT;
	}

	// Factorial can only be a limited number of values within range.
	return fact_usi_data[x];

}


// Return the factorial of x.
signed long factorial_signed_long(signed long x, char *errflag) {
	*errflag = 0;

	// Factorial is not defined for negative values.
	if (x < 0) {
		*errflag = ARR_ERR_VALUE_ERR;
		return DEFAULT_FACT;
	}

	// We can't calculate a factorial this big.
	if (x > MAX_SL_FACT) {
		*errflag = ARR_ERR_OVFL;
		return DEFAULT_FACT;
	}

	// Factorial can only be a limited number of values within range.
	return fact_sl_data[x];

}

// Return the factorial of x.
unsigned long factorial_unsigned_long(unsigned long x, char *errflag) {
	*errflag = 0;

	// We can't calculate a factorial this big.
	if (x > MAX_USL_FACT) {
		*errflag = ARR_ERR_OVFL;
		return DEFAULT_FACT;
	}

	// Factorial can only be a limited number of values within range.
	return fact_usl_data[x];

}

// Return the factorial of x.
signed long long factorial_signed_long_long(signed long long x, char *errflag) {
	*errflag = 0;

	// Factorial is not defined for negative values.
	if (x < 0) {
		*errflag = ARR_ERR_VALUE_ERR;
		return DEFAULT_FACT;
	}

	// We can't calculate a factorial this big.
	if (x > MAX_SLL_FACT) {
		*errflag = ARR_ERR_OVFL;
		return DEFAULT_FACT;
	}

	// Factorial can only be a limited number of values within range.
	return fact_sll_data[x];

}

// Return the factorial of x.
unsigned long long factorial_unsigned_long_long(unsigned long long x, char *errflag) {
	*errflag = 0;

	// We can't calculate a factorial this big.
	if (x > MAX_USLL_FACT) {
		*errflag = ARR_ERR_OVFL;
		return DEFAULT_FACT;
	}

	// Factorial can only be a limited number of values within range.
	return fact_usll_data[x];

}

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



// Return x raised to the power of y.
unsigned char arith_pow_unsigned_char(unsigned char x, unsigned char y, char *errflag) {
	unsigned char i, z, ovtmp1;
	z = 1;
	*errflag = 0;

	// Special case for raise to the power of zero.
	if (y == 0) { return 1; }

	// We need this special case to avoid dividing by zero.
	if (x == 0) {return 0;}

	ovtmp1 = SCHAR_MAX / x;
	for (i = 0; i < y; i++) {
		if (z > ovtmp1) {*errflag = ARR_ERR_OVFL; return z;}
		z = z * x;
	}
	return z;
}



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

// This is for compatibility with Microsoft msvc 2010.
// This is equivalent to the standard copysignf.
float ms_compat_copysignf(float x, float y) {
	char xneg, yneg;

	xneg = x < 0.0;
	yneg = y < 0.0;

	// Check if signs are different.
	if (xneg != yneg) {
		return -x;
	} else {
		return x;
	}

}

/*--------------------------------------------------------------------------- */
