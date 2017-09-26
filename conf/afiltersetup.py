#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='afilter', version='0.0',
	ext_modules = [Extension('afilter', ['afilter.c', 'afilter_common.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c'])])

