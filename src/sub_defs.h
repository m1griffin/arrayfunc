//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   sub_defs.h
// Purpose:  Additional macros for sub
//           
// Language: C
// Date:     12-Aug-2021
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
/* The integer overflow limit check. 
   val = The parameter value being checked. 
   ovlimit = The previously calculated overflow limit.
   Returns True if overflow will happen. 
*/
// For when ovlimit was calculated on a positive value (pos_ovlimit_12_).
#define pos_willoverflow(val, ovlimit) ( val < ovlimit )
// For when ovlimit was calculated on a negative value (neg_ovlimit_12_).
#define neg_willoverflow(val, ovlimit) ( val > ovlimit )


/*--------------------------------------------------------------------------- */
/* ovlimit_*
   Calculate the maximum value an integer can be without overflowing.
   This is used for equations where we need to know the maximum value 
   (magnitude for either +ve or -ve) which can be used in a calculation 
   without it overflowing. 
   val = The parameter value being checked.
   Returns the overflow limit. 

   loop_willoverflow_*
   This combined ovlimit and pos_willoverflow and neg_willoverflow. Use
   this in loops where both sides of the equation are arraya and the 
   limit must be recalculated every iteration.
   lval, rval = The respective current values of the arrays.
   Returns True if the current operation will result in an integer overflow.

*/
/*--------------------------------------------------------------------------- */
// For signed char.
// For when val is positive and the form is (array - param). Use when called in loops.
#define pos_ovlimit_12_signed_char(val) SCHAR_MIN + val
// For when val is negative and the form is (array - param). Use when called in loops.
#define neg_ovlimit_12_signed_char(val) SCHAR_MAX + val

// For when val is positive and the form is (param - array). Use when called in loops.
#define pos_ovlimit_34_signed_char(val) val - SCHAR_MAX
// For when val is negative and the form is (param - array). Use when called in loops.
#define neg_ovlimit_34_signed_char(val) val - SCHAR_MIN;


// For use in loops when both parameters are arrays and are changing. 
#define loop_willoverflow_signed_char(lval, rval) \
							(((rval > 0) && (lval < (SCHAR_MIN + rval))) \
							|| ((rval < 0) && (lval > (SCHAR_MAX + rval))))


/*--------------------------------------------------------------------------- */
// For unsigned char.
// For unsigned only. Can use in loops and outside loops.
#define loop_willoverflow_unsigned_char(lval, rval) (lval < rval)


/*--------------------------------------------------------------------------- */
// For signed short.
// For when val is positive and the form is (array - param). Use when called in loops.
#define pos_ovlimit_12_signed_short(val) SHRT_MIN + val
// For when val is negative and the form is (array - param). Use when called in loops.
#define neg_ovlimit_12_signed_short(val) SHRT_MAX + val

// For when val is positive and the form is (param - array). Use when called in loops.
#define pos_ovlimit_34_signed_short(val) val - SHRT_MAX
// For when val is negative and the form is (param - array). Use when called in loops.
#define neg_ovlimit_34_signed_short(val) val - SHRT_MIN;


// For use in loops when both parameters are arrays and are changing. 
#define loop_willoverflow_signed_short(lval, rval) \
							(((rval > 0) && (lval < (SHRT_MIN + rval))) \
							|| ((rval < 0) && (lval > (SHRT_MAX + rval))))


/*--------------------------------------------------------------------------- */
// For unsigned short.
// For unsigned only. Can use in loops and outside loops.
#define loop_willoverflow_unsigned_short(lval, rval) (lval < rval)


/*--------------------------------------------------------------------------- */
// For signed int.
// For when val is positive and the form is (array - param). Use when called in loops.
#define pos_ovlimit_12_signed_int(val) INT_MIN + val
// For when val is negative and the form is (array - param). Use when called in loops.
#define neg_ovlimit_12_signed_int(val) INT_MAX + val

// For when val is positive and the form is (param - array). Use when called in loops.
#define pos_ovlimit_34_signed_int(val) val - INT_MAX
// For when val is negative and the form is (param - array). Use when called in loops.
#define neg_ovlimit_34_signed_int(val) val - INT_MIN;


// For use in loops when both parameters are arrays and are changing. 
#define loop_willoverflow_signed_int(lval, rval) \
							(((rval > 0) && (lval < (INT_MIN + rval))) \
							|| ((rval < 0) && (lval > (INT_MAX + rval))))


/*--------------------------------------------------------------------------- */
// For unsigned int.
// For unsigned only. Can use in loops and outside loops.
#define loop_willoverflow_unsigned_int(lval, rval) (lval < rval)


/*--------------------------------------------------------------------------- */
// For signed long.
// For when val is positive and the form is (array - param). Use when called in loops.
#define pos_ovlimit_12_signed_long(val) LONG_MIN + val
// For when val is negative and the form is (array - param). Use when called in loops.
#define neg_ovlimit_12_signed_long(val) LONG_MAX + val

// For when val is positive and the form is (param - array). Use when called in loops.
#define pos_ovlimit_34_signed_long(val) val - LONG_MAX
// For when val is negative and the form is (param - array). Use when called in loops.
#define neg_ovlimit_34_signed_long(val) val - LONG_MIN;


// For use in loops when both parameters are arrays and are changing. 
#define loop_willoverflow_signed_long(lval, rval) \
							(((rval > 0) && (lval < (LONG_MIN + rval))) \
							|| ((rval < 0) && (lval > (LONG_MAX + rval))))


/*--------------------------------------------------------------------------- */
// For unsigned long.
// For unsigned only. Can use in loops and outside loops.
#define loop_willoverflow_unsigned_long(lval, rval) (lval < rval)


/*--------------------------------------------------------------------------- */
// For signed long long.
// For when val is positive and the form is (array - param). Use when called in loops.
#define pos_ovlimit_12_signed_long_long(val) LLONG_MIN + val
// For when val is negative and the form is (array - param). Use when called in loops.
#define neg_ovlimit_12_signed_long_long(val) LLONG_MAX + val

// For when val is positive and the form is (param - array). Use when called in loops.
#define pos_ovlimit_34_signed_long_long(val) val - LLONG_MAX
// For when val is negative and the form is (param - array). Use when called in loops.
#define neg_ovlimit_34_signed_long_long(val) val - LLONG_MIN;


// For use in loops when both parameters are arrays and are changing. 
#define loop_willoverflow_signed_long_long(lval, rval) \
							(((rval > 0) && (lval < (LLONG_MIN + rval))) \
							|| ((rval < 0) && (lval > (LLONG_MAX + rval))))


/*--------------------------------------------------------------------------- */
// For unsigned long long.
// For unsigned only. Can use in loops and outside loops.
#define loop_willoverflow_unsigned_long_long(lval, rval) (lval < rval)


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



