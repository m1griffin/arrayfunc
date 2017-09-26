#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='count', version='0.0',
	ext_modules = [Extension('count', ['count.c', 'count_common.c', 'arrayfunc.c', 'arrayerrs.c'])])

