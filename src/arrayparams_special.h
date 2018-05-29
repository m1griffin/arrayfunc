//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_special.h
// Purpose:  Common functions for arrayfunc.
// Language: C
// Date:     25-Jan-2018
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

#define ARGSINIT_SPECIAL {0, 0, 0, 0, 0, 0, {NULL}, {NULL}, {NULL}, {NULL}}


// Provide a struct for returning data from parsing Python arguments.
struct args_params_ldexp {
	char error;
	char arraytype;
	bool hassecondarray;
	unsigned int ignoreerrors;
	signed long long exp;
	Py_ssize_t arraylength;
	union dataarrays array1;
	union dataarrays array2;
	Py_buffer pybuffer1;
	Py_buffer pybuffer2;
};

/*--------------------------------------------------------------------------- */

struct args_params_ldexp getparams_ldexp(PyObject *self, PyObject *args, PyObject *keywds);

void releasebuffers_twobuff(Py_buffer pybuffer1, Py_buffer pybuffer2, char hasoutputarray);

/*--------------------------------------------------------------------------- */
