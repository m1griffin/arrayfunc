#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='findindex', version='0.0',
	ext_modules = [Extension('findindex', ['findindex.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c'])])

