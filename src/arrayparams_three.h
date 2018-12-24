//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayparams_three.h
// Purpose:  Functions for parsing parameters for functions which take three params.
// Language: C
// Date:     29-Nov-2018
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

#define ARGSINIT_THREE {0, 0, 0, 0, 0, 0, 0, 0, 0, {NULL}, {NULL}, {NULL}, {NULL}, {NULL}, {NULL}, {NULL}, {NULL}, {0}}


enum paramcats
{
	param_arr_num_num_none,
	param_arr_num_num_arr,
	param_arr_arr_num_none,
	param_arr_arr_num_arr,
	param_arr_num_arr_none,
	param_arr_num_arr_arr,
	param_arr_arr_arr_none,
	param_arr_arr_arr_arr
};


// Provide a struct for returning data from parsing Python arguments.
struct args_params_3 {
	char error;
	char arraytype;
	bool hasoutputarray;
	char hasbuffer1;
	char hasbuffer2;
	char hasbuffer3;
	char hasbuffer4;
	unsigned int ignoreerrors;
	Py_ssize_t arraylength;
	union dataarrays array1;
	union dataarrays array2;
	union dataarrays array3;
	union dataarrays array4;
	Py_buffer pybuffer1;
	Py_buffer pybuffer2;
	Py_buffer pybuffer3;
	Py_buffer pybuffer4;
	struct paramsvals param2;
	struct paramsvals param3;
	enum paramcats paramcat;
};


/*--------------------------------------------------------------------------- */

struct args_params_3 getparams_three(PyObject *self, PyObject *args, PyObject *keywds, char *funcname);

void releasebuffers_three(struct args_params_3 arraydata);


/*--------------------------------------------------------------------------- */
