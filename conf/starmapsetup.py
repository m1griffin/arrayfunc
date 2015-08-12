#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='starmap', version='0.0',
	ext_modules = [Extension('starmap', ['starmap.c', 'starmap_common.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c'])])

