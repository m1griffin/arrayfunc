#!/usr/bin/env python3

import platform
from setuptools import setup, Extension


# This is a list of the files and all the dependencies.
extensions = [
('aall', ['src/aall.c', 'src/aall_simd_x86.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('aany', ['src/aany.c', 'src/aany_simd_x86.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('acalcvm', ['src/acalcvm.c', 'src/acalcvm_common.c', 'src/arrayfunc.c', 'src/arrayerrs.c', 'src/arithcalcs.c']),
('afilter', ['src/afilter.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('amapi', ['src/amapi.c', 'src/amap_common.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('amap', ['src/amap.c', 'src/amap_common.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('amax', ['src/amax.c', 'src/amax_simd_x86.c', 'src/arrayfunc.c', 'src/arrayerrs.c']),
('amin', ['src/amin.c', 'src/amin_simd_x86.c', 'src/arrayfunc.c', 'src/arrayerrs.c']),
('asum', ['src/asum.c', 'src/asum_simd_x86.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('compress', ['src/compress.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('convert', ['src/convert.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('count', ['src/count.c', 'src/arrayfunc.c', 'src/arrayerrs.c']),
('cycle', ['src/cycle.c', 'src/arrayfunc.c', 'src/arrayerrs.c']),
('dropwhile', ['src/dropwhile.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('findindex', ['src/findindex.c', 'src/findindex_simd_x86.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('findindices', ['src/findindices.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('repeat', ['src/repeat.c', 'src/arrayfunc.c', 'src/arrayerrs.c']),
('starmapi', ['src/starmapi.c', 'src/starmap_common.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('starmap', ['src/starmap.c', 'src/starmap_common.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('takewhile', ['src/takewhile.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('simdsupport', ['src/simdsupport.c']),
('arrayguardbands', ['src/arrayguardbands.c', 'src/arrayerrs.c']),
('arraylimits', ['src/arraylimits.c']),
]


# Detect the compiler used for Python. We will assume that this same compiler is
# being used to compile our own modules (since the two are supposed to match).
# We are looking specifically for GCC.
# The names used by MSVC for the SIMD instructions are not compatible with
# other compilers. LLVM Clang does not have full compiler intrinsics SIMD 
# support yet. Hence, we can only use SIMD with GCC at this time. We suppress
# the command line option for unsupported compilers to avoid compiler warnings.
# GCC is expected to return a string which looks something like the 
# following: 'GCC 5.4.0 20160609'
# LLVM Clang returned something like: 'GCC 4.2.1 Compatible Clang <etc.>'
# MSVC Returns something like 'MSC <version> <chip architecture>'
# Because LLVM Clang masquerades as GCC, we must take extra effort to ensure that
# we're actually dealing with GCC. If this changes in future, we can change the 
# following to enable the option. There are however also #define statements in
# the C source which must also be changed.
PyCompilerType = platform.python_compiler()
if ('GCC' in PyCompilerType) and ('Clang' not in PyCompilerType):
	Compile_Args = '-msse4.1'
else:
	Compile_Args = ''



with open('README.rst') as longdescdata:
    long_description = longdescdata.read()


setup(name = 'arrayfunc', 
	version = '3.0.0',
	description = 'Fast array processing functions',
	long_description = long_description,
	url = 'https://github.com/m1griffin/arrayfunc',
	author = 'M Griffin',
	author_email = 'm12.griffin@gmail.com',
	license = 'Apache License V2.0',
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Topic :: Scientific/Engineering :: Mathematics',
		'License :: OSI Approved :: Apache Software License',
		'Programming Language :: Python :: 3.5',
		],
	keywords = 'mathematical array functions',
	ext_package='arrayfunc',
	ext_modules = [Extension(x, y, extra_compile_args=[Compile_Args]) for x,y in extensions],
	packages=['arrayfunc']
	)

