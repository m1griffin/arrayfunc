//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   convguardbands.h
// Purpose:  Guard bands for converting data.
// Language: C
// Date:     30-Apr-2014
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


// Long integers may be either 32 or 64 bits, depending upon CPU architecture
// and OS/compiler.
// Array types 'l' and 'L' are 8 byte integers.
#if LONG_MAX == LLONG_MAX

// Double precision (double) to long integers. A double has 52 bits of precision.
#define LONG_MAX_GUARD_D (LONG_MAX - 0xfff)
#define LONG_MIN_GUARD_D (LONG_MIN + 0x1000)
#define ULONG_MAX_GUARD_D (ULONG_MAX - 0xfff)

// Single precision (float) to long integers. A single has 23 bits of precision.
#define LONG_MAX_GUARD_F (LONG_MAX - 0x1ffffffffff)
#define LONG_MIN_GUARD_F (LONG_MIN + 0x20000000000)
#define ULONG_MAX_GUARD_F (ULONG_MAX - 0x1ffffffffff)

// Array types 'l' and 'L' are 4 byte integers.
#else

// Double precision (double) to long integers. A double has 52 bits of precision.
#define LONG_MAX_GUARD_D LONG_MAX
#define LONG_MIN_GUARD_D LONG_MIN
#define ULONG_MAX_GUARD_D ULONG_MAX

// Single precision (float) to long integers. A single has 23 bits of precision.
#define LONG_MAX_GUARD_F (LONG_MAX - 0x1ff)
#define LONG_MIN_GUARD_F (LONG_MIN + 0x200)
#define ULONG_MAX_GUARD_F (ULONG_MAX - 0x1ff)

#endif


// Other array types are always the same size on supported platforms.
// Single precision (float) to integers. A single has 23 bits of precision.
#define INT_MAX_GUARD_F (INT_MAX - 0x1ff)
#define INT_MIN_GUARD_F (INT_MIN + 0x200)
#define UINT_MAX_GUARD_F (UINT_MAX - 0x1ff)


// Single precision (float) to long long integers. A single has 23 bits of precision.
#define LLONG_MAX_GUARD_F (LLONG_MAX - 0x1ffffffffff)
#define LLONG_MIN_GUARD_F (LLONG_MIN + 0x20000000000)
#define ULLONG_MAX_GUARD_F (ULLONG_MAX - 0x1ffffffffff)


// Double precision (double) to long long integers. A double has 52 bits of precision.
#define LLONG_MAX_GUARD_D (LLONG_MAX - 0xfff)
#define LLONG_MIN_GUARD_D (LLONG_MIN + 0x1000)
#define ULLONG_MAX_GUARD_D (ULLONG_MAX - 0xfff)


/*--------------------------------------------------------------------------- */
