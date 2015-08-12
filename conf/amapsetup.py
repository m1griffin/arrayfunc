#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='amap', version='0.0',
	ext_modules = [Extension('amap', ['amap.c', 'amap_common.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c'])])

