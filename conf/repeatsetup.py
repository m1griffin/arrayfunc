#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='repeat', version='0.0',
	ext_modules = [Extension('repeat', ['repeat.c', 'repeat_common.c', 'arrayfunc.c', 'arrayerrs.c'])])

