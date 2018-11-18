#!/usr/bin/env python3

# Setup file for arrayfunc. As part of the setup process this script will
# attempt to detect if the current system is x86-64 with GCC and if so will 
# enable SIMD extensions. If the current system is any other architecture or 
# compiler they will be disabled.


import platform
from setuptools import setup, Extension


# This is a list of the files and all the dependencies.
extensions = [
	('aall', ['src/aall.c', 'src/aall_common.c', 'src/aall_simd_x86.c', 'src/arrayparams_base.c', 'src/arrayops.c', 'src/arrayerrs.c']),
	('aany', ['src/aany.c', 'src/aany_common.c', 'src/aany_simd_x86.c', 'src/arrayparams_base.c', 'src/arrayops.c', 'src/arrayerrs.c']),

	('afilter', ['src/afilter.c', 'src/afilter_common.c', 'src/arrayparams_base.c', 'src/arrayops.c', 'src/arrayerrs.c']),

	('amax', ['src/amax.c', 'src/amax_common.c', 'src/amax_simd_x86.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('amin', ['src/amin.c', 'src/amin_common.c', 'src/amin_simd_x86.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),

	('asum', ['src/asum.c', 'src/asum_common.c', 'src/asum_simd_x86.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),

	('compress', ['src/compress.c', 'src/compress_common.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('convert', ['src/convert.c', 'src/convert_common.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),

	('count', ['src/count.c', 'src/count_common.c', 'src/arrayparams_base.c', 'src/arrayops.c', 'src/arrayerrs.c']),
	('cycle', ['src/cycle.c', 'src/cycle_common.c', 'src/arrayparams_base.c', 'src/arrayops.c', 'src/arrayerrs.c']),
	('repeat', ['src/repeat.c', 'src/repeat_common.c', 'src/arrayparams_base.c', 'src/arrayops.c', 'src/arrayerrs.c']),

	('dropwhile', ['src/dropwhile.c', 'src/dropwhile_common.c', 'src/arrayparams_base.c', 'src/arrayops.c', 'src/arrayerrs.c']),
	('takewhile', ['src/takewhile.c', 'src/takewhile_common.c', 'src/arrayparams_base.c', 'src/arrayops.c', 'src/arrayerrs.c']),

	('findindex', ['src/findindex.c', 'src/findindex_common.c', 'src/findindex_simd_x86.c', 'src/arrayparams_base.c', 'src/arrayops.c', 'src/arrayerrs.c']),
	('findindices', ['src/findindices.c', 'src/findindices_common.c', 'src/arrayparams_base.c', 'src/arrayops.c', 'src/arrayerrs.c']),


	('simdsupport', ['src/simdsupport.c']),
	('arrayguardbands', ['src/arrayguardbands.c', 'src/arrayerrs.c']),
	('arraylimits', ['src/arraylimits.c']),


	('add', ['src/add.c', 'src/arrayparams_two.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('sub', ['src/sub.c', 'src/arrayparams_two.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('mul', ['src/mul.c', 'src/arrayparams_two.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('truediv', ['src/truediv.c', 'src/arrayparams_two.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('floordiv', ['src/floordiv.c', 'src/arrayparams_two.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('mod', ['src/mod.c', 'src/arrayparams_two.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('pow', ['src/pow.c', 'src/arrayparams_two.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),

	('eq', ['src/eq.c', 'src/arrayparams_comp.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('ne', ['src/ne.c', 'src/arrayparams_comp.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('gt', ['src/gt.c', 'src/arrayparams_comp.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('ge', ['src/ge.c', 'src/arrayparams_comp.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('lt', ['src/lt.c', 'src/arrayparams_comp.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('le', ['src/le.c', 'src/arrayparams_comp.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),

	('and_', ['src/and_.c', 'src/arrayparams_two.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('or_', ['src/or_.c', 'src/arrayparams_two.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('xor', ['src/xor.c', 'src/arrayparams_two.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('lshift', ['src/lshift.c', 'src/arrayparams_two.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('rshift', ['src/rshift.c', 'src/arrayparams_two.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),

	('neg', ['src/neg.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('abs_', ['src/abs_.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('factorial', ['src/factorial.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('invert', ['src/invert.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),

	('acos', ['src/acos.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('acosh', ['src/acosh.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('asin', ['src/asin.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('asinh', ['src/asinh.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('atan', ['src/atan.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('atanh', ['src/atanh.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('ceil', ['src/ceil.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('cos', ['src/cos.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('cosh', ['src/cosh.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('erf', ['src/erf.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('erfc', ['src/erfc.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('exp', ['src/exp.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('expm1', ['src/expm1.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('fabs', ['src/fabs.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('floor', ['src/floor.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('gamma', ['src/gamma.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('lgamma', ['src/lgamma.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('log10', ['src/log10.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('log1p', ['src/log1p.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('log2', ['src/log2.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('log', ['src/log.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('sin', ['src/sin.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('sinh', ['src/sinh.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('sqrt', ['src/sqrt.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('tan', ['src/tan.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('tanh', ['src/tanh.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('trunc', ['src/trunc.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),

	('degrees', ['src/degrees.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('radians', ['src/radians.c', 'src/arrayparams_one.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),

	('isfinite', ['src/isfinite.c', 'src/arrayparams_boolout.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('isinf', ['src/isinf.c', 'src/arrayparams_boolout.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('isnan', ['src/isnan.c', 'src/arrayparams_boolout.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),

	('atan2', ['src/atan2.c', 'src/arrayparams_two.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('copysign', ['src/copysign.c', 'src/arrayparams_two.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('fmod', ['src/fmod.c', 'src/arrayparams_two.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('hypot', ['src/hypot.c', 'src/arrayparams_two.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),
	('ldexp', ['src/ldexp.c', 'src/arrayparams_special.c', 'src/arrayparams_base.c', 'src/arrayerrs.c']),

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
# First however, we must check to make sure this is an x86 CPU, otherwise the
# SIMD flags are completely different.
PyCompilerType = platform.python_compiler()
if ('x86' in platform.machine()) and ('GCC' in PyCompilerType) and ('Clang' not in PyCompilerType):
	Compile_Args = ['-msse4.1']
else:
	Compile_Args = []



with open('README.rst') as longdescdata:
    long_description = longdescdata.read()


setup(name = 'arrayfunc', 
	version = '4.1.0',
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
	ext_modules = [Extension(x, y, extra_compile_args=Compile_Args) for x,y in extensions],
	packages=['arrayfunc']
	)

