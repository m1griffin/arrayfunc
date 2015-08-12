#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='aany', version='0.0',
	ext_modules = [Extension('aany', ['aany.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c'])])

