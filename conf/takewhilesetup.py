#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='takewhile', version='0.0',
	ext_modules = [Extension('takewhile', ['takewhile.c', 'takewhile_common.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c'])])

