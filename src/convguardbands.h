//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   convguardbands.h
// Purpose:  Guard bands for converting data.
// Language: C
// Date:     30-Apr-2014
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

#include <math.h>

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
'q'		signed long long	int 	8		8		8
'Q'		unsigned long long	int 	8		8		8
'f' 	float 				float 	4		4		4
'd' 	double 				float 	8		8		8

An extra "guard value" is added or subtracted from each maximum or minimum
value to account for the limited resolution (precision) of floating point 
numbers.
double precision (double) = 52 bits of precision.
single precision (float) = 23 bits of precision.
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


// Single precision (float) to long long integers. A single has 24 bits of precision.
#define LLONG_MAX_GUARD_F (LLONG_MAX - 0xffffffffff)
#define LLONG_MIN_GUARD_F (LLONG_MIN + 0xffffffffff)
#define ULLONG_MAX_GUARD_F (ULLONG_MAX - 0x1ffffffffff)

// Double precision (double) to long long integers. A double has 53 bits of precision.
#define LLONG_MAX_GUARD_D (LLONG_MAX - 0xfff)
#define LLONG_MIN_GUARD_D (LLONG_MIN + 0xfff)
#define ULLONG_MAX_GUARD_D (ULLONG_MAX - 0x1fff)


/*--------------------------------------------------------------------------- */
