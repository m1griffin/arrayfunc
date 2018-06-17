//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_bool.c
// Purpose:  Common functions for arrayfunc.
// Language: C
// Date:     10-Apr-2018
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

#include <stdbool.h>

#include "Python.h"

/*--------------------------------------------------------------------------- */

#define ARGSINIT_BOOLOUT {0, 0, 0, 0, {NULL}, {NULL}}


// Provide a struct for returning data from parsing Python arguments.
struct args_params_boolout {
	char error;
	char arraytype;
	char hasbuffer1;
	Py_ssize_t arraylength;
	union dataarrays array1;
	Py_buffer pybuffer1;
};

/*--------------------------------------------------------------------------- */

struct args_params_boolout getparams_boolout(PyObject *self, PyObject *args, PyObject *keywds, char *funcname);

void releasebuffers_boolout(struct args_params_boolout arraydata);

/*--------------------------------------------------------------------------- */
