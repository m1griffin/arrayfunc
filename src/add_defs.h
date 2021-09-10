//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   add_defs.h
// Purpose:  Additional macros for add
//           
// Language: C
// Date:     08-Aug-2021
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
// For when ovlimit was calculated on a positive value (pos_ovlimit_).
#define pos_willoverflow(val, ovlimit) ( val > ovlimit )
// For when ovlimit was calculated on a negative value (neg_ovlimit_).
#define neg_willoverflow(val, ovlimit) ( val < ovlimit )


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
// For when val is positive or negative. Do not use in loops.
#define ovlimit_signed_char(val) (val >= 0) ? ( SCHAR_MAX - val ) : ( SCHAR_MIN - val )
// For when val is positive. Use when called in loops.
#define pos_ovlimit_signed_char(val) SCHAR_MAX - val
// For when val is negative. Use when called in loops.
#define neg_ovlimit_signed_char(val) SCHAR_MIN - val

// For use in loops when both parameters are arrays and are changing. 
#define loop_willoverflow_signed_char(lval, rval) \
							(((rval > 0) && (lval > (SCHAR_MAX - rval))) \
							|| ((rval < 0) && (lval < (SCHAR_MIN - rval))))


/*--------------------------------------------------------------------------- */
// For unsigned char.
// For unsigned. Can use in loops and outside loops.
#define ovlimit_unsigned_char(val) ( UCHAR_MAX - val )

#define loop_willoverflow_unsigned_char(lval, rval) (lval > (UCHAR_MAX - rval))


/*--------------------------------------------------------------------------- */
// For signed short.
// For when val is positive or negative. Do not use in loops.
#define ovlimit_signed_short(val) (val >= 0) ? ( SHRT_MAX - val ) : ( SHRT_MIN - val )
// For when val is positive. Use when called in loops.
#define pos_ovlimit_signed_short(val) SHRT_MAX - val
// For when val is negative. Use when called in loops.
#define neg_ovlimit_signed_short(val) SHRT_MIN - val

// For use in loops when both parameters are arrays and are changing. 
#define loop_willoverflow_signed_short(lval, rval) \
							(((rval > 0) && (lval > (SHRT_MAX - rval))) \
							|| ((rval < 0) && (lval < (SHRT_MIN - rval))))


/*--------------------------------------------------------------------------- */
// For unsigned short.
// For unsigned. Can use in loops and outside loops.
#define ovlimit_unsigned_short(val) ( USHRT_MAX - val )

#define loop_willoverflow_unsigned_short(lval, rval) (lval > (USHRT_MAX - rval))


/*--------------------------------------------------------------------------- */
// For signed int.
// For when val is positive or negative. Do not use in loops.
#define ovlimit_signed_int(val) (val >= 0) ? ( INT_MAX - val ) : ( INT_MIN - val )
// For when val is positive. Use when called in loops.
#define pos_ovlimit_signed_int(val) INT_MAX - val
// For when val is negative. Use when called in loops.
#define neg_ovlimit_signed_int(val) INT_MIN - val

// For use in loops when both parameters are arrays and are changing. 
#define loop_willoverflow_signed_int(lval, rval) \
							(((rval > 0) && (lval > (INT_MAX - rval))) \
							|| ((rval < 0) && (lval < (INT_MIN - rval))))


/*--------------------------------------------------------------------------- */
// For unsigned int.
// For unsigned. Can use in loops and outside loops.
#define ovlimit_unsigned_int(val) ( UINT_MAX - val )

#define loop_willoverflow_unsigned_int(lval, rval) (lval > (UINT_MAX - rval))


/*--------------------------------------------------------------------------- */
// For signed long.
// For when val is positive or negative. Do not use in loops.
#define ovlimit_signed_long(val) (val >= 0) ? ( LONG_MAX - val ) : ( LONG_MIN - val )
// For when val is positive. Use when called in loops.
#define pos_ovlimit_signed_long(val) LONG_MAX - val
// For when val is negative. Use when called in loops.
#define neg_ovlimit_signed_long(val) LONG_MIN - val

// For use in loops when both parameters are arrays and are changing. 
#define loop_willoverflow_signed_long(lval, rval) \
							(((rval > 0) && (lval > (LONG_MAX - rval))) \
							|| ((rval < 0) && (lval < (LONG_MIN - rval))))


/*--------------------------------------------------------------------------- */
// For unsigned long.
// For unsigned. Can use in loops and outside loops.
#define ovlimit_unsigned_long(val) ( ULONG_MAX - val )

#define loop_willoverflow_unsigned_long(lval, rval) (lval > (ULONG_MAX - rval))


/*--------------------------------------------------------------------------- */
// For signed long long.
// For when val is positive or negative. Do not use in loops.
#define ovlimit_signed_long_long(val) (val >= 0) ? ( LLONG_MAX - val ) : ( LLONG_MIN - val )
// For when val is positive. Use when called in loops.
#define pos_ovlimit_signed_long_long(val) LLONG_MAX - val
// For when val is negative. Use when called in loops.
#define neg_ovlimit_signed_long_long(val) LLONG_MIN - val

// For use in loops when both parameters are arrays and are changing. 
#define loop_willoverflow_signed_long_long(lval, rval) \
							(((rval > 0) && (lval > (LLONG_MAX - rval))) \
							|| ((rval < 0) && (lval < (LLONG_MIN - rval))))


/*--------------------------------------------------------------------------- */
// For unsigned long long.
// For unsigned. Can use in loops and outside loops.
#define ovlimit_unsigned_long_long(val) ( ULLONG_MAX - val )

#define loop_willoverflow_unsigned_long_long(lval, rval) (lval > (ULLONG_MAX - rval))


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



