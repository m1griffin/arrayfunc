//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arithcalcs.h
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


// This _USE_MATH_DEFINES is required for MSVC 2010 compatibility to enable
// the M_PI constant. This must be immediately above <math.h>.
#define _USE_MATH_DEFINES
#include <math.h>

/*--------------------------------------------------------------------------- */
// Calculate factorials.

signed char factorial_signed_char(signed char x, char *errflag);
unsigned char factorial_unsigned_char(unsigned char x, char *errflag);
signed short factorial_signed_short(signed short x, char *errflag);
unsigned short factorial_unsigned_short(unsigned short x, char *errflag);
signed int factorial_signed_int(signed int x, char *errflag);
unsigned int factorial_unsigned_int(unsigned int x, char *errflag);
signed long factorial_signed_long(signed long x, char *errflag);
unsigned long factorial_unsigned_long(unsigned long x, char *errflag);
signed long long factorial_signed_long_long(signed long long x, char *errflag);
unsigned long long factorial_unsigned_long_long(unsigned long long x, char *errflag);

/*--------------------------------------------------------------------------- */
// Calculate x raised to the power of y.

signed char arith_pow_signed_char(signed char x, signed char y, char *errflag);
unsigned char arith_pow_unsigned_char(unsigned char x, unsigned char y, char *errflag);
signed short arith_pow_signed_short(signed short x, signed short y, char *errflag);
unsigned short arith_pow_unsigned_short(unsigned short x, unsigned short y, char *errflag);
signed int arith_pow_signed_int(signed int x, signed int y, char *errflag);
unsigned int arith_pow_unsigned_int(unsigned int x, unsigned int y, char *errflag);
signed long arith_pow_signed_long(signed long x, signed long y, char *errflag);
unsigned long arith_pow_unsigned_long(unsigned long x, unsigned long y, char *errflag);
signed long long arith_pow_signed_long_long(signed long long x, signed long long y, char *errflag);
unsigned long long arith_pow_unsigned_long_long(unsigned long long x, unsigned long long y, char *errflag);

/*--------------------------------------------------------------------------- */

// Used to calculate degrees to radians and radians to degrees.
const double degtorad_d = M_PI / 180.0;
const double radtodeg_d = 180.0 / M_PI;
const float degtorad_f = (float) (M_PI / 180.0);
const float radtodeg_f = (float) (180.0 / M_PI);

/*--------------------------------------------------------------------------- */
