//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_two.c
// Purpose:  Functions for parsing parameters for functions which take two params.
// Language: C
// Date:     28-Nov-2017
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2017    Michael Griffin    <m12.griffin@gmail.com>
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

#define ARGSINIT_TWO {0, 0, 0, 0, 0, 0, 0, 0, 0, {NULL}, {NULL}, {NULL}, {NULL}, {NULL}, {NULL}, {0}}


enum paramcats
{
	param_arr_num_none,
	param_arr_num_arr,
	param_num_arr_none,
	param_num_arr_arr,
	param_arr_arr_none,
	param_arr_arr_arr
};


// Provide a struct for returning data from parsing Python arguments.
struct args_params_2 {
	char error;
	char arraytype;
	bool hasoutputarray;
	char hasbuffer1;
	char hasbuffer2;
	char hasbuffer3;
	unsigned int ignoreerrors;
	int nosimd;
	Py_ssize_t arraylength;
	union dataarrays array1;
	union dataarrays array2;
	union dataarrays array3;
	Py_buffer pybuffer1;
	Py_buffer pybuffer2;
	Py_buffer pybuffer3;
	struct paramsvals param;
	enum paramcats paramcat;
};


/*--------------------------------------------------------------------------- */

struct args_params_2 getparams_two(PyObject *self, PyObject *args, PyObject *keywds, char matherrors, char hasnosimd, char *funcname);

void releasebuffers_two(struct args_params_2 arraydata);


/*--------------------------------------------------------------------------- */
