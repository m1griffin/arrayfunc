//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   arraylimits.c
// Purpose:  Return the platform limits for each array type.
// Language: C
// Date:     21-May-2014
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

/*--------------------------------------------------------------------------- */

#include "Python.h"

#include <limits.h>
#include <float.h>


/*--------------------------------------------------------------------------- */

static PyMethodDef arraylimits_methods[] = {
	{NULL, NULL}           /* sentinel */
};


PyDoc_STRVAR(module_doc,
"Provide the maximum and minimum platform specific array data value limits. \n\
These values are provided by the compiler and exposed as module attributes \n\
The following lists the Python array codes together with the corresponding \n\
'C' data types. Integer sizes may vary depending upon the compiler  \n\
implementation. \n\
-----------  ---------------------- \n\
Array Code    C Type \n\
-----------  ---------------------- \n\
  b            signed char \n\
  B            unsigned char \n\
  h            signed short \n\
  H            unsigned short \n\
  i            signed int \n\
  I            unsigned int \n\
  l            signed long \n\
  L            unsigned long \n\
  q            signed long long \n\
  Q            unsigned long long \n\
  f            float \n\
  d            double \n\
-----------  ---------------------- \n\
");

static struct PyModuleDef arraylimitsmodule = {
	PyModuleDef_HEAD_INIT,
	"arraylimits",
	module_doc,
	-1,
	arraylimits_methods,
	NULL,
	NULL,
	NULL,
	NULL
};


PyMODINIT_FUNC PyInit_arraylimits(void) {
	PyObject *m;

	m = PyModule_Create(&arraylimitsmodule);
	if (m == NULL) { goto iserror; }


	// b - signed char
	if (PyModule_AddObject(m, "b_min", PyLong_FromLong(SCHAR_MIN)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "b_max", PyLong_FromLong(SCHAR_MAX)) < 0) { goto iserror; }

	// B - unsigned char
	if (PyModule_AddObject(m, "B_min", PyLong_FromUnsignedLong(0)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "B_max", PyLong_FromUnsignedLong(UCHAR_MAX)) < 0) { goto iserror; }

	// h - signed short
	if (PyModule_AddObject(m, "h_min", PyLong_FromLong(SHRT_MIN)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "h_max", PyLong_FromLong(SHRT_MAX)) < 0) { goto iserror; }

	// H - unsigned short
	if (PyModule_AddObject(m, "H_min", PyLong_FromUnsignedLong(0)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "H_max", PyLong_FromUnsignedLong(USHRT_MAX)) < 0) { goto iserror; }

	// i - signed int
	if (PyModule_AddObject(m, "i_min", PyLong_FromLong(INT_MIN)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "i_max", PyLong_FromLong(INT_MAX)) < 0) { goto iserror; }

	// I - unsigned int
	if (PyModule_AddObject(m, "I_min", PyLong_FromUnsignedLong(0)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "I_max", PyLong_FromUnsignedLong(UINT_MAX)) < 0) { goto iserror; }

	// l - signed long
	if (PyModule_AddObject(m, "l_min", PyLong_FromLong(LONG_MIN)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "l_max", PyLong_FromLong(LONG_MAX)) < 0) { goto iserror; }

	// L - unsigned long
	if (PyModule_AddObject(m, "L_min", PyLong_FromUnsignedLong(0)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "L_max", PyLong_FromUnsignedLong(ULONG_MAX)) < 0) { goto iserror; }

	// q - signed long long
	if (PyModule_AddObject(m, "q_min", PyLong_FromLongLong(LLONG_MIN)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "q_max", PyLong_FromLongLong(LLONG_MAX)) < 0) { goto iserror; }

	// Q - unsigned long long
	if (PyModule_AddObject(m, "Q_min", PyLong_FromUnsignedLongLong(0)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "Q_max", PyLong_FromUnsignedLongLong(ULLONG_MAX)) < 0) { goto iserror; }

	// f - float
	if (PyModule_AddObject(m, "f_min", PyFloat_FromDouble(-FLT_MAX)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "f_max", PyFloat_FromDouble(FLT_MAX)) < 0) { goto iserror; }

	// d - double
	if (PyModule_AddObject(m, "d_min", PyFloat_FromDouble(-DBL_MAX)) < 0) { goto iserror; }
	if (PyModule_AddObject(m, "d_max", PyFloat_FromDouble(DBL_MAX)) < 0) { goto iserror; }


	// This is the normal exit point.
	return m;

	// An error occurred.
	iserror:
	return NULL;

}

/*--------------------------------------------------------------------------- */

