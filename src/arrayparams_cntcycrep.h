//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_cntcycrep.h
// Purpose:  Common functions for arrayfunc.
// Language: C
// Date:     28-Nov-2017
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2019    Michael Griffin    <m12.griffin@gmail.com>
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

#include "Python.h"

/*--------------------------------------------------------------------------- */

#define ARGSINIT_CNTCYCREP {0, 0, 0, 0, 0, 0, {0}, {0}, {0}, {NULL}, {NULL}}


// Provide a struct for returning data from parsing Python arguments.
struct args_params_cntcycrep {
	char error;
	char arraytype;
	char hasbuffer1;
	char hasparam2;
	char hasparam3;
	Py_ssize_t arraylength;
	struct paramsvals param1;
	struct paramsvals param2;
	struct paramsvals param3;
	union dataarrays array1;
	Py_buffer pybuffer1;
};

/*--------------------------------------------------------------------------- */

// Each function has its own parameter parsing code.
struct args_params_cntcycrep getparams_repeat(PyObject *self, PyObject *args, PyObject *keywds, char *funcname);
struct args_params_cntcycrep getparams_count(PyObject *self, PyObject *args, PyObject *keywds, char *funcname);
struct args_params_cntcycrep getparams_cycle(PyObject *self, PyObject *args, PyObject *keywds, char *funcname);


void releasebuffers_cntcycrep(struct args_params_cntcycrep arraydata);

/*--------------------------------------------------------------------------- */
