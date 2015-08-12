#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='amapi', version='0.0',
	ext_modules = [Extension('amapi', ['amapi.c', 'amap_common.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c'])])

