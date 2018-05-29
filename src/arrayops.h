//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayops.c
// Purpose:  Functions for parsing parameters for functions which use compare
//            compare operations.
// Language: C
// Date:     28-May-2018
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


#define OP_AF_EQ 1
#define OP_AF_GT 2
#define OP_AF_GTE 3
#define OP_AF_LT 4
#define OP_AF_LTE 5
#define OP_AF_NE 6

//------------------------------------------------------------------------------

signed int opstrdecode(PyObject *opstr);

char paramtypecode(PyObject *paramobj);
char paramcompatok(char arraytype, char paramtype);


//------------------------------------------------------------------------------
