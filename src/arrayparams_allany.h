//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_comp.c
// Purpose:  Functions for parsing parameters for aall and aany.
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

#include <stdbool.h>

#include "Python.h"

/*--------------------------------------------------------------------------- */

#define ARGSINIT_ALLANY {0, 0, 0, {NULL}, {NULL}, {0}}


// Provide a struct for returning data from parsing Python arguments.
struct args_params_allany {
	char error;
	char arraytype;
	Py_ssize_t arraylength;
	union dataarrays array1;
	Py_buffer pybuffer1;
	struct paramsvals param;
};

/*--------------------------------------------------------------------------- */

struct args_params_allany getparams_allany(PyObject *self, PyObject *args, PyObject *keywds, char *funcname);

void releasebuffers_allany(struct args_params_allany arraydata);

/*--------------------------------------------------------------------------- */
