//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   neg_defs.h
// Purpose:  Additional macros for neg
//           
// Language: C
// Date:     26-Aug-2021
// Ver:      06-Sep-2021.
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
// For signed char.
// Use to detect if an overflow condition will occur due to negating a minimum integer. 
#define minval_loop_willoverflow_signed_char(val) (val == SCHAR_MIN)

/*--------------------------------------------------------------------------- */
// For signed short.
// Use to detect if an overflow condition will occur due to negating a minimum integer. 
#define minval_loop_willoverflow_signed_short(val) (val == SHRT_MIN)

/*--------------------------------------------------------------------------- */
// For signed int.
// Use to detect if an overflow condition will occur due to negating a minimum integer. 
#define minval_loop_willoverflow_signed_int(val) (val == INT_MIN)

/*--------------------------------------------------------------------------- */
// For signed long.
// Use to detect if an overflow condition will occur due to negating a minimum integer. 
#define minval_loop_willoverflow_signed_long(val) (val == LONG_MIN)

/*--------------------------------------------------------------------------- */
// For signed long long.
// Use to detect if an overflow condition will occur due to negating a minimum integer. 
#define minval_loop_willoverflow_signed_long_long(val) (val == LLONG_MIN)


