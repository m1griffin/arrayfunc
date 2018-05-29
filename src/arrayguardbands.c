//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arrayguardbands.c
// Purpose:  Provide the guard band values for unit testing.
// Language: C
// Date:     21-May-2014
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

#include <limits.h>
#include <float.h>

#include "convguardbands.h"


/*--------------------------------------------------------------------------- */

static PyMethodDef arrayguardbands_methods[] = {
	{NULL, NULL}           /* sentinel */
};


PyDoc_STRVAR(module_doc,
"Provide the guard band values used by 'convert' for unit testing. \n\
These values are provided by the compiler and exposed as module attributes \n\
This module exists only to assit in unit testing the 'convert' module, and \n\
must not not be relied upon to exist in future versions. \n");

static struct PyModuleDef arrayguardbandsmodule = {
	PyModuleDef_HEAD_INIT,
	"arrayguardbands",
	module_doc,
	-1,
	arrayguardbands_methods,
	NULL,
	NULL,
	NULL,
	NULL
};


PyMODINIT_FUNC PyInit_arrayguardbands(void) {
	PyObject *m;

	m = PyModule_Create(&arrayguardbandsmodule);
	if (m == NULL) { goto iserror; }


	if (PyModule_AddObject(m, "LONG_MAX_GUARD_D", PyLong_FromLong(LONG_MAX_GUARD_D)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "LONG_MIN_GUARD_D", PyLong_FromLong(LONG_MIN_GUARD_D)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "ULONG_MAX_GUARD_D", PyLong_FromUnsignedLong(ULONG_MAX_GUARD_D)) < 0) { goto iserror; }

	if (PyModule_AddObject(m, "LONG_MAX_GUARD_F", PyLong_FromLong(LONG_MAX_GUARD_F)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "LONG_MIN_GUARD_F", PyLong_FromLong(LONG_MIN_GUARD_F)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "ULONG_MAX_GUARD_F", PyLong_FromUnsignedLong(ULONG_MAX_GUARD_F)) < 0) { goto iserror; }

	if (PyModule_AddObject(m, "INT_MAX_GUARD_F", PyLong_FromLong(INT_MAX_GUARD_F)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "INT_MIN_GUARD_F", PyLong_FromLong(INT_MIN_GUARD_F)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "UINT_MAX_GUARD_F", PyLong_FromUnsignedLong(UINT_MAX_GUARD_F)) < 0) { goto iserror; }


	if (PyModule_AddObject(m, "LLONG_MAX_GUARD_F", PyLong_FromLongLong(LLONG_MAX_GUARD_F)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "LLONG_MIN_GUARD_F", PyLong_FromLongLong(LLONG_MIN_GUARD_F)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "ULLONG_MAX_GUARD_F", PyLong_FromUnsignedLongLong(ULLONG_MAX_GUARD_F)) < 0) { goto iserror; }

	if (PyModule_AddObject(m, "LLONG_MAX_GUARD_D", PyLong_FromLongLong(LLONG_MAX_GUARD_D)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "LLONG_MIN_GUARD_D", PyLong_FromLongLong(LLONG_MIN_GUARD_D)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "ULLONG_MAX_GUARD_D", PyLong_FromUnsignedLongLong(ULLONG_MAX_GUARD_D)) < 0) { goto iserror; }


	// This is the normal exit point.
	return m;

	// An error occurred.
	iserror:
	return NULL;

}

/*--------------------------------------------------------------------------- */

