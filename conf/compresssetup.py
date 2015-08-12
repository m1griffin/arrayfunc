#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='compress', version='0.0',
	ext_modules = [Extension('compress', ['compress.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c'])])

