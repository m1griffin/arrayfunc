//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   simddefs.h
// Purpose:  Common declarations for arrayfunc SIMD operations.
// Language: C
// Date:     11-May-2016
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

// This signals that SIMD is supported.

// If this is not 64 bit x86, we don't use SIMD features. The SIMD features
// use compiler intrinsics which are CPU architecture specific.
// If this is not GCC, we don't use the SIMD features as they are not 
// compatible with the GCC syntax. On Windows, the wide variation in SIMD 
// features makes distribution of pre-compiled 32 bit binaries difficult. 

#ifdef __x86_64__
#ifdef __GNUC__
#ifndef __clang__
#define AF_HASSIMD_X86
#endif
#endif
#endif


// This is the equivalent for ARM. We support ARMv7 only and only with GCC.
#ifdef __GNUC__
#ifndef __clang__
#ifdef __arm__
#ifdef __ARM_ARCH_7A__

#define AF_HASSIMD_ARM

#endif
#endif
#endif
#endif




/*--------------------------------------------------------------------------- */

// This is for x86-64 only with 128 bit SIMD registers.
#ifdef AF_HASSIMD_X86

typedef char v16qi __attribute__ ((vector_size (16)));
typedef short int v8hi __attribute__ ((vector_size (16)));
typedef int v4si __attribute__ ((vector_size (16)));
typedef float v4sf __attribute__ ((vector_size (16)));
typedef double v2df __attribute__ ((vector_size (16)));
typedef long long v2di __attribute__ ((vector_size (16)));


#define CHARSIMDSIZE 16
#define SHORTSIMDSIZE 8
#define INTSIMDSIZE 4
#define FLOATSIMDSIZE 4
#define DOUBLESIMDSIZE 2

#endif

/*--------------------------------------------------------------------------- */

// This is for ARM NEON only, with 64 bit SIMD registers.
#ifdef AF_HASSIMD_ARM

#define CHARSIMDSIZE 8
#define SHORTSIMDSIZE 4
#define INTSIMDSIZE 2
#define FLOATSIMDSIZE 2

#endif

/*--------------------------------------------------------------------------- */
