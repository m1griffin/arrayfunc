#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='convert', version='0.0',
	ext_modules = [Extension('convert', ['convert.c', 'convert_common.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c'])])

