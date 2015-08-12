#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='starmapi', version='0.0',
	ext_modules = [Extension('starmapi', ['starmapi.c', 'starmap_common.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c'])])

