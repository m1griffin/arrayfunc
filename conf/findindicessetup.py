#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='findindices', version='0.0',
	ext_modules = [Extension('findindices', ['findindices.c', 'findindices_common.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c'])])

