//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayplatform.h
// Purpose:  Platform support definitions.
// Language: C
// Date:     07-Dec-2014
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

/*--------------------------------------------------------------------------- */

// The following is used for platform support for 32 versus 64 bit support.
// Array types 'q' and 'Q' are not present in some 32 bit systems. Unfortunately
// there is no standard way of detecting this, so we have to determine it 
// indirectly. Additional tests may have to be added as the need is discovered.

// Determine if this is gcc.
#ifdef __GNUC__

// We've only tested x86 for 64 bit. Other architectures could be added to this.
#if __x86_64__
// The standard Python HAVE_LONG_LONG doesn't seem to work for some reason, we
// we create our own.
#define AF_HAVE_LONG_LONG
#endif

#else

// We assume that every other compiler uses 64 bit integers. 
#define AF_HAVE_LONG_LONG

#endif // __GNUC__

/*--------------------------------------------------------------------------- */

