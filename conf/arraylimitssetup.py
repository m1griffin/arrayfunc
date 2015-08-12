#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='arraylimits', version='0.0',
	ext_modules = [Extension('arraylimits', ['arraylimits.c'])])

