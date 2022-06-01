//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   simddefs.h
// Purpose:  Common declarations for arrayfunc SIMD operations.
// Language: C
// Date:     11-May-2016
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2022    Michael Griffin    <m12.griffin@gmail.com>
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


// If this is not GCC, we don't use the SIMD features as they are not 
// compatible with the GCC syntax. We have to check that it is not Clang,
// as LLVM Clang will claim to be GCC.
// LLVM Clang has limited SIMD support. For Windows, this library is normally
// distributed as a precompiled binary and the very wide range of x86 versions
// makes relying on SIMD problematic.
#if defined(__GNUC__) && !defined(__clang__)

// If this is x86 but not 64 bit, we don't use SIMD features. 
#if defined(__x86_64__)
#define AF_HASSIMD_X86
#endif

// For Rasberry Pi 3 and 32 bit OS.
#if defined(__arm__) && defined(__ARM_ARCH_7A__)
#define AF_HASSIMD_ARMv7_32BIT
#endif

// For 64 bit ARM on Rasberry Pi 3 with a 64 bit OS.
#if defined(__aarch64__)
#define AF_HASSIMD_ARM_AARCH64
#endif

#endif

/*--------------------------------------------------------------------------- */

// On x86 32 bit platforms there is an apparent compiler bug which can cause 
// float (32 bit floating point) to exceed the valid range when two floats
// of the maximum value are added together instead of the result being 
// infinity. This has been observed with Debian 32 bit in a VM and Alpine 
// 32 bit on a Via C3. A fix has been implemented which triggers infinity.
#if defined(__i386__)
#define AF_FIXFLOAT_i386
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

// This is for ARM NEON 32 bit only, with 64 bit SIMD registers.
#ifdef AF_HASSIMD_ARMv7_32BIT

#define CHARSIMDSIZE 8
#define SHORTSIMDSIZE 4
#define INTSIMDSIZE 2
#define FLOATSIMDSIZE 2

#endif

/*--------------------------------------------------------------------------- */


// This is for ARM NEON 64 bit only, with 128 bit SIMD registers.
#ifdef AF_HASSIMD_ARM_AARCH64

#define CHARSIMDSIZE 16
#define SHORTSIMDSIZE 8
#define INTSIMDSIZE 4
#define FLOATSIMDSIZE 4

#endif

/*--------------------------------------------------------------------------- */

/*   calcalignedlength
   Calculate the aligned length of the array. This is the length which is
   evenly divisible by the SIMD register. Any array elements after this
   one must be dealt with using non-SIMD clean-up code.
   arraylen = The length of the array in number of elements.
   simdwidth = The width of the SIMD registers for this data type.
   Returns the length of the array which can be processed using SIMD.
*/

#define calcalignedlength(arraylen, simdwidth) (arraylen - (arraylen % simdwidth))


/*   enoughforsimd
   Calculate whether the array to be processed is big enough to be handled by
   SIMD. We make the minimum size for this bigger than the actual minimum as
   the overhead for setting up SIMD does not justify very small arrays. The
   minimum size used here is arbitrary and was not tested with benchmarks.
   arraylen = The length of the array in number of elements.
   simdwidth = The width of the SIMD registers for this data type.
*/

#define enoughforsimd(arraylen, simdwidth) (arraylen >= (simdwidth * 2))

/*--------------------------------------------------------------------------- */
