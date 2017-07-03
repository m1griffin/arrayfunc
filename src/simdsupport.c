//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   simdsupport.c
// Purpose:  Return the SIMD support level.
// Language: C
// Date:     25-Jul-2016
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2016    Michael Griffin    <m12.griffin@gmail.com>
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

#include "simddefs.h"

/*--------------------------------------------------------------------------- */

static PyMethodDef simdsupport_methods[] = {
	{NULL, NULL}           /* sentinel */
};


PyDoc_STRVAR(module_doc,
"The attribute 'hassimd' will be TRUE if the CPU supports the required SIMD features.\n");

static struct PyModuleDef simdsupportmodule = {
	PyModuleDef_HEAD_INIT,
	"simdsupport",
	module_doc,
	-1,
	simdsupport_methods,
	NULL,
	NULL,
	NULL,
	NULL
};

/*--------------------------------------------------------------------------- */

/* Return True if the SIMD level in the CPU is sufficient to support the library. */
signed int hassimdlevel(void) {
#ifdef AF_HASSIMD

	// Initialise the CPU test.
	__builtin_cpu_init();

	// Now check to see if SSE 4.1 is supported. 
	if (__builtin_cpu_supports("sse4.1")) {
		return 1;
	} else {
		return 0;
	}
#endif

	return 0;

}

/*--------------------------------------------------------------------------- */


PyMODINIT_FUNC PyInit_simdsupport(void) {
	PyObject *m;

	m = PyModule_Create(&simdsupportmodule);
	if (m == NULL) { goto iserror; }

	if (hassimdlevel()) {
		if (PyModule_AddObject(m, "hassimd", Py_True)) { goto iserror; }
	} else {
		if (PyModule_AddObject(m, "hassimd", Py_False)) { goto iserror; }
	}
		

	// This is the normal exit point.
	return m;

	// An error occurred.
	iserror:
	return NULL;

}

/*--------------------------------------------------------------------------- */


