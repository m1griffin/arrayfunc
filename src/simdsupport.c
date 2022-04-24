//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   simdsupport.c
// Purpose:  Return the SIMD support level.
// Language: C
// Date:     25-Jul-2016
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - 2022    Michael Griffin    <m12.griffin@gmail.com>
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

#define PY_SSIZE_T_CLEAN
#include "Python.h"

#include "simddefs.h"


#if defined(AF_HASSIMD_ARMv7_32BIT) || defined(AF_HASSIMD_ARM_AARCH64)
#include <sys/auxv.h>
#include <asm/hwcap.h>
#endif

/*--------------------------------------------------------------------------- */

static PyMethodDef simdsupport_methods[] = {
	{NULL, NULL}           /* sentinel */
};


PyDoc_STRVAR(module_doc,
"This provides information on the SIMD level compiled into this version \n\
of the library. There are two attributes, 'hassimd' and 'simdarch'.\n\
* 'hassimd' is TRUE if the CPU supports the required SIMD features.\n\
* 'simdarch' contains a string indicating the CPU architecture the library\n\
   was compiled for.\n\
Examples:\n\
>>> arrayfunc.simdsupport.hassimd\n\
True\n\
>>> arrayfunc.simdsupport.simdarch\n\
'x86_64'\n\
This was created primarily for unit testing and benchmarking and should\n\
not be considered to be a permanent or stable part of the library.\n\
");

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

// Determines the SIMS support compiled into the library based on the macros 
// defined elsewhere.

// For x86-64.
#ifdef AF_HASSIMD_X86

signed int hassimdlevel(void) {

	// Initialise the CPU test.
	__builtin_cpu_init();

	// Now check to see if SSE 4.1 is supported. 
	if (__builtin_cpu_supports("sse4.1")) {
		return 1;
	} else {
		return 0;
	}
}

#elif defined(AF_HASSIMD_ARMv7_32BIT)

// For ARMv7 32 bit with NEON.
signed int hassimdlevel(void) {
	if (getauxval(AT_HWCAP) & HWCAP_NEON) {
		return 2;
	} else {
		return 0;
	}
}

#elif defined(AF_HASSIMD_ARM_AARCH64)

// Apparently ARM aarch64 64 bit always has NEON.
signed int hassimdlevel(void) {
	return 3;
}

#else

// If none of the above, assume false. This should cover 32 bit x86.
signed int hassimdlevel(void) {
	return 0;
}

#endif



/*--------------------------------------------------------------------------- */


PyMODINIT_FUNC PyInit_simdsupport(void) {
	PyObject *m;

	signed int simdcode;

	m = PyModule_Create(&simdsupportmodule);
	if (m == NULL) { goto iserror; }

	// There are alternative hassimdlevel functions, only one of which
	// is defined at any one time.
	simdcode = hassimdlevel();

	switch (simdcode) {
		// No SIMD.
		case 0 : {
			if (PyModule_AddObject(m, "hassimd", PyBool_FromLong(0)) < 0) { goto iserror; }
			if (PyModule_AddObject(m, "simdarch", PyUnicode_FromString("none")) < 0) { goto iserror; }
			break;
		}
		// x86_64, also known as amd64.
		case 1 : {
			if (PyModule_AddObject(m, "hassimd", PyBool_FromLong(1)) < 0) { goto iserror; }
			if (PyModule_AddObject(m, "simdarch", PyUnicode_FromString("x86_64")) < 0) { goto iserror; }
			break;
		}
		// ARMv7 with 32 bit NEON. Also known as armv7l.
		case 2 : {
			if (PyModule_AddObject(m, "hassimd", PyBool_FromLong(1)) < 0) { goto iserror; }
			if (PyModule_AddObject(m, "simdarch", PyUnicode_FromString("armv7l")) < 0) { goto iserror; }
			break;
		}
		// ARMv8 with 64 bit NEON.  Also known as aarch64.
		case 3 : {
			if (PyModule_AddObject(m, "hassimd", PyBool_FromLong(1)) < 0) { goto iserror; }
			if (PyModule_AddObject(m, "simdarch", PyUnicode_FromString("aarch64")) < 0) { goto iserror; }
			break;
		}
		// We don't know this code.
		default: {
			if (PyModule_AddObject(m, "hassimd", PyBool_FromLong(0)) < 0) { goto iserror; }
			if (PyModule_AddObject(m, "simdarch", PyUnicode_FromString("none")) < 0) { goto iserror; }
			break;
		}
	}


	// This is the normal exit point.
	return m;

	// An error occurred.
	iserror:
	return NULL;

}

/*--------------------------------------------------------------------------- */


