//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayfunc.h
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

#include "Python.h"

#include <math.h>

/*--------------------------------------------------------------------------- */

// These are the op codes which define operator and functions.
#define OP_AF_ADD 1
#define OP_AF_DIV 2
#define OP_AF_DIV_R 3
#define OP_AF_FLOORDIV 4
#define OP_AF_FLOORDIV_R 5
#define OP_AF_MOD 6
#define OP_AF_MOD_R 7
#define OP_AF_MULT 8
#define OP_AF_NEG 9
#define OP_AF_POW 10
#define OP_AF_POW_R 11
#define OP_AF_SUB 12
#define OP_AF_SUB_R 13
#define OP_AF_AND 14
#define OP_AF_OR 15
#define OP_AF_XOR 16
#define OP_AF_INVERT 17
#define OP_AF_EQ 18
#define OP_AF_GT 19
#define OP_AF_GTE 20
#define OP_AF_LT 21
#define OP_AF_LTE 22
#define OP_AF_NE 23
#define OP_AF_LSHIFT 24
#define OP_AF_LSHIFT_R 25
#define OP_AF_RSHIFT 26
#define OP_AF_RSHIFT_R 27
#define OP_AF_ABS 28
#define OP_MATH_ACOS 29
#define OP_MATH_ACOSH 30
#define OP_MATH_ASIN 31
#define OP_MATH_ASINH 32
#define OP_MATH_ATAN 33
#define OP_MATH_ATAN2 34
#define OP_MATH_ATAN2_R 35
#define OP_MATH_ATANH 36
#define OP_MATH_CEIL 37
#define OP_MATH_COPYSIGN 38
#define OP_MATH_COS 39
#define OP_MATH_COSH 40
#define OP_MATH_DEGREES 41
#define OP_MATH_ERF 42
#define OP_MATH_ERFC 43
#define OP_MATH_EXP 44
#define OP_MATH_EXPM1 45
#define OP_MATH_FABS 46
#define OP_MATH_FACTORIAL 47
#define OP_MATH_FLOOR 48
#define OP_MATH_FMOD 49
#define OP_MATH_FMOD_R 50
#define OP_MATH_GAMMA 51
#define OP_MATH_HYPOT 52
#define OP_MATH_HYPOT_R 53
#define OP_MATH_ISINF 54
#define OP_MATH_ISNAN 55
#define OP_MATH_LDEXP 56
#define OP_MATH_LGAMMA 57
#define OP_MATH_LOG 58
#define OP_MATH_LOG10 59
#define OP_MATH_LOG1P 60
#define OP_MATH_POW 61
#define OP_MATH_POW_R 62
#define OP_MATH_RADIANS 63
#define OP_MATH_SIN 64
#define OP_MATH_SINH 65
#define OP_MATH_SQRT 66
#define OP_MATH_TAN 67
#define OP_MATH_TANH 68
#define OP_MATH_TRUNC 69
#define OP_AOPS_SUBST_GT 70
#define OP_AOPS_SUBST_GTE 71
#define OP_AOPS_SUBST_LT 72
#define OP_AOPS_SUBST_LTE 73


/*--------------------------------------------------------------------------- */

// The data arrays. Each element represents a different data type.
union dataarrays {
	uint8_t *buf;
	signed char *b;
	unsigned char *B;
	signed short *h;
	unsigned short *H;
	signed int *i;
	unsigned int *I;
	signed long *l;
	unsigned long *L;
	signed long long *q;
	unsigned long long *Q;
	float *f;
	double *d;
};


// This is used to hold the additional non-array parameters.
struct paramsvals {
	signed char b;
	unsigned char B;
	signed short h;
	unsigned short H;
	signed int i;
	unsigned int I;
	signed long l;
	unsigned long L;
	signed long long q;
	unsigned long long Q;
	float f;
	double d;
};


// This is used to hold the type of array parameters.
struct arrayparamstypes {
	char ok;			// True if there was no error.
	char isarray;		// True if is an array or bytes.
	char arraycode;		// The array type code (or bytes).
};


/*--------------------------------------------------------------------------- */

Py_ssize_t calcarraylength(char itemcode, Py_ssize_t bufferlength);

char paramcompatok(char arraytype, char paramtype);
char paramtypecode(char const *typename);
struct arrayparamstypes paramarraytype(PyObject *dataobj);


char issignedcharrange(signed long x);
char issignedshortrange(signed long x);
char issignedintrange(signed long x);
char isunsignedcharrange(signed long x);
char isunsignedshortrange(signed long x);
char isunsignedintrange(signed long x);

Py_ssize_t adjustarraymaxlen(Py_ssize_t arraylength, Py_ssize_t arraymaxlen);

/*--------------------------------------------------------------------------- */

// These handle magnitude limits for converting from double to long integers
// (signed and unsigned). 
/*
Array	Data						Number of bytes
Code	Type						x86-32	x-86-64	ARM-32
'b' 	signed char 		int 	1		1		1
'B' 	unsigned char 		int 	1		1		1
'h' 	signed short 		int 	2		2		2
'H' 	unsigned short 		int 	2		2		2
'i' 	signed int 			int 	4		4		4
'I' 	unsigned int 		int 	4		4		4
'l' 	signed long 		int 	4		8		4
'L' 	unsigned long 		int 	4		8		4
'q'		signed long long	int 	8		8		???
'Q'		unsigned long long	int 	8		8		???
'f' 	float 				float 	4		4		4
'd' 	double 				float 	8		8		8

An extra "guard value" is added or subtracted from each maximum or minimum
value to account for the limited resolution (precision) of floating point 
numbers.
double precision (double) = 52 bits of precision.
single precision (float) = 23 bits of precision.
Long long does not exist on some platforms.
*/


// Double precision (double) to long integers. A double has 53 bits of precision.
#define LONG_MAX_GUARD_D ((sizeof(signed long) == 8) ? LONG_MAX - 0xfff : LONG_MAX)
#define LONG_MIN_GUARD_D ((sizeof(signed long) == 8) ? LONG_MIN + 0xfff : LONG_MIN)
#define ULONG_MAX_GUARD_D ((sizeof(unsigned long) == 8) ? ULONG_MAX - 0x1fff : ULONG_MAX)

// Single precision (float) to long integers. A single has 24 bits of precision.
#define LONG_MAX_GUARD_F ((sizeof(signed long) > 4) ? ((sizeof(signed long) == 8) ? LONG_MAX - 0xffffffffff : LONG_MAX - 0xff) : LONG_MAX)
#define LONG_MIN_GUARD_F ((sizeof(signed long) > 4) ? ((sizeof(signed long) == 8) ? LONG_MIN + 0xffffffffff : LONG_MIN + 0xff) : LONG_MIN)
#define ULONG_MAX_GUARD_F ((sizeof(unsigned long) > 4) ? ((sizeof(unsigned long) == 8) ? ULONG_MAX - 0x1ffffffffff : ULONG_MAX - 0xff) : ULONG_MAX)

// Single precision (float) to integers. A single has 24 bits of precision.
#define INT_MAX_GUARD_F ((sizeof(signed int) == 4) ? INT_MAX - 0xff : INT_MAX)
#define INT_MIN_GUARD_F ((sizeof(signed int) == 4) ? INT_MIN + 0xff : INT_MIN)
#define UINT_MAX_GUARD_F ((sizeof(unsigned int) == 4) ? UINT_MAX - 0x1ff : UINT_MAX)


// Long long does not exist on all platforms.

// Single precision (float) to long long integers. A single has 24 bits of precision.
#define LLONG_MAX_GUARD_F (LLONG_MAX - 0xffffffffff)
#define LLONG_MIN_GUARD_F (LLONG_MIN + 0xffffffffff)
#define ULLONG_MAX_GUARD_F (ULLONG_MAX - 0x1ffffffffff)

// Double precision (double) to long long integers. A double has 53 bits of precision.
#define LLONG_MAX_GUARD_D (LLONG_MAX - 0xfff)
#define LLONG_MIN_GUARD_D (LLONG_MIN + 0xfff)
#define ULLONG_MAX_GUARD_D (ULLONG_MAX - 0x1fff)


/*--------------------------------------------------------------------------- */

