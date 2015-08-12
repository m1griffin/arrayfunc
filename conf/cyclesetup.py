#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='cycle', version='0.0',
	ext_modules = [Extension('cycle', ['cycle.c', 'arrayfunc.c', 'arrayerrs.c'])])

