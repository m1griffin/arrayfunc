#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='dropwhile', version='0.0',
	ext_modules = [Extension('dropwhile', ['dropwhile.c', 'dropwhile_common.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c'])])

