#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='arrayguardbands', version='0.0',
	ext_modules = [Extension('arrayguardbands', ['arrayguardbands.c', 'arrayerrs.c'])])

