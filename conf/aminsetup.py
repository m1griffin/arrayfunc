#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='amin', version='0.0',
	ext_modules = [Extension('amin', ['amin.c', 'amin_common.c', 'amin_simd_x86.c', 'arrayfunc.c', 'arrayerrs.c'],
					extra_compile_args=['-msse4.1'])])

