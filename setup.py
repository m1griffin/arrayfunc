#!/usr/bin/env python3

from distutils.core import setup, Extension

extensions = [
('aall', ['src/aall.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('aany', ['src/aany.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('acalcvm', ['src/acalcvm.c', 'src/acalcvm_common.c', 'src/arrayfunc.c', 'src/arrayerrs.c', 'src/arithcalcs.c']),
('afilter', ['src/afilter.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('amapi', ['src/amapi.c', 'src/amap_common.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('amap', ['src/amap.c', 'src/amap_common.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('amax', ['src/amax.c', 'src/arrayfunc.c', 'src/arrayerrs.c']),
('amin', ['src/amin.c', 'src/arrayfunc.c', 'src/arrayerrs.c']),
('arrayguardbands', ['src/arrayguardbands.c', 'src/arrayerrs.c']),
('arraylimits', ['src/arraylimits.c']),
('asum', ['src/asum.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('compress', ['src/compress.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('convert', ['src/convert.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('count', ['src/count.c', 'src/arrayfunc.c', 'src/arrayerrs.c']),
('cycle', ['src/cycle.c', 'src/arrayfunc.c', 'src/arrayerrs.c']),
('dropwhile', ['src/dropwhile.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('findindex', ['src/findindex.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('findindices', ['src/findindices.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('repeat', ['src/repeat.c', 'src/arrayfunc.c', 'src/arrayerrs.c']),
('starmapi', ['src/starmapi.c', 'src/starmap_common.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('starmap', ['src/starmap.c', 'src/starmap_common.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
('takewhile', ['src/takewhile.c', 'src/arrayfunc.c', 'src/arithcalcs.c', 'src/arrayerrs.c']),
]


with open('README.rst') as longdescdata:
    long_description = longdescdata.read()


setup(name = 'arrayfunc', 
	version = '1.1.0',
	description = 'Fast array processing functions',
	long_description = long_description,
	url = 'https://github.com/arrayfunc/arrayfunc',
	author = 'M Griffin',
	author_email = 'm12.griffin@gmail.com',
	license = 'Apache License V2.0',
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Topic :: Scientific/Engineering :: Mathematics',
		'License :: OSI Approved :: Apache Software License',
		'Programming Language :: Python :: 3.4',
		],
	keywords = 'mathematical array functions',
	ext_package='arrayfunc',
	ext_modules = [Extension(x, y) for x,y in extensions],
	packages=['arrayfunc']
	)

