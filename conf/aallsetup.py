#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='aall', version='0.0',
	ext_modules = [Extension('aall', ['aall.c', 'aall_common.c', 'aall_simd_x86.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c'],
					extra_compile_args=['-msse4.1'])])
