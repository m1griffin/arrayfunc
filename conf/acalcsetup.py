#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='acalc', version='0.0',
	ext_modules = [Extension('acalcvm', ['acalcvm.c', 'acalcvm_common.c', 'arrayfunc.c', 'arrayerrs.c', 'arithcalcs.c'])])

