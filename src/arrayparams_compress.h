//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_compress.h
// Purpose:  Parameter parsing for compress.
// Language: C
// Date:     10-May-2014
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

#define ARGSINIT_COMPRESS {0, 0, 0, 0, 0, 0, 0, 0, {NULL}, {NULL}, {NULL}, {NULL}, {NULL}, {NULL}}



// Provide a struct for returning data from parsing Python arguments.
struct args_params_compress {
	char error;
	char arraytype;
	Py_ssize_t arraylength1;
	Py_ssize_t arraylength2;
	Py_ssize_t arraylength3;
	char hasbuffer1;
	char hasbuffer2;
	char hasbuffer3;
	union dataarrays array1;
	union dataarrays array2;
	union dataarrays array3;
	Py_buffer pybuffer1;
	Py_buffer pybuffer2;
	Py_buffer pybuffer3;
};

/*--------------------------------------------------------------------------- */

struct args_params_compress getparams_compress(PyObject *self, PyObject *args, PyObject *keywds, char *funcname);

void releasebuffers_compress(struct args_params_compress arraydata);

/*--------------------------------------------------------------------------- */
