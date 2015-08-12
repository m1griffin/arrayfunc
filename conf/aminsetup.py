#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='amin', version='0.0',
	ext_modules = [Extension('amin', ['amin.c', 'arrayfunc.c', 'arrayerrs.c'])])

