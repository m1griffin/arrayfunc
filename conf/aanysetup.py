#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='aany', version='0.0',
	ext_modules = [Extension('aany', ['aany.c', 'aany_simd_x86.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c'],
					extra_compile_args=['-msse4.1'])])

