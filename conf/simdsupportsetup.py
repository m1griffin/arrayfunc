#!/usr/bin/env python3
from distutils.core import setup, Extension

setup(name='simdsupport', version='0.0',
	ext_modules = [Extension('simdsupport', ['simdsupport.c'])])
