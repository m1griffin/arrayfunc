#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='amax', version='0.0',
	ext_modules = [Extension('amax', ['amax.c', 'amax_simd_x86.c', 'arrayfunc.c', 'arrayerrs.c'],
					extra_compile_args=['-msse4.1'])])

