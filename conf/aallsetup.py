#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='aall', version='0.0',
	ext_modules = [Extension('aall', ['aall.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c'])])
