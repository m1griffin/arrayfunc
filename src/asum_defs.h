//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   asum_defs.h
// Purpose:  Additional macros for asum
//           
// Language: C
// Date:     21-Jun-2022
// Ver:      04-Jul-2022.
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

// Integer overflow checks.

// Unsigned integer - new value will cause an integer overflow.
#define loop_willoverflow_unsigned(val, partialsum) (val > (ULLONG_MAX - partialsum))

// Signed integer - new value will cause an integer overflow.
#define loop_willoverflow_signed(val, partialsum) (((partialsum > 0) && (val > (LLONG_MAX - partialsum))) ||                                                    ((partialsum < 0) && (val < (LLONG_MIN - partialsum))))

/*--------------------------------------------------------------------------- */



