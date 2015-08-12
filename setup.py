#!/usr/bin/env python3
from distutils.core import setup, Extension

extensions = [
('aall', ['aall.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c']),
('aany', ['aany.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c']),
('afilter', ['afilter.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c']),
('amapi', ['amapi.c', 'amap_common.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c']),
('amap', ['amap.c', 'amap_common.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c']),
('amax', ['amax.c', 'arrayfunc.c', 'arrayerrs.c']),
('amin', ['amin.c', 'arrayfunc.c', 'arrayerrs.c']),
('arrayguardbands', ['arrayguardbands.c', 'arrayerrs.c']),
('arraylimits', ['arraylimits.c']),
('asum', ['asum.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c']),
('compress', ['compress.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c']),
('convert', ['convert.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c']),
('count', ['count.c', 'arrayfunc.c', 'arrayerrs.c']),
('cycle', ['cycle.c', 'arrayfunc.c', 'arrayerrs.c']),
('dropwhile', ['dropwhile.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c']),
('findindex', ['findindex.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c']),
('findindices', ['findindices.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c']),
('repeat', ['repeat.c', 'arrayfunc.c', 'arrayerrs.c']),
('starmapi', ['starmapi.c', 'starmap_common.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c']),
('starmap', ['starmap.c', 'starmap_common.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c']),
('takewhile', ['takewhile.c', 'arrayfunc.c', 'arithcalcs.c', 'arrayerrs.c']),
]

for modname, modext in extensions:
	setup(name = modname, version='0.0', ext_modules = [Extension(modname, ['src/%s' % x for x in modext])])


with open('README.rst') as longdescdata:
    long_description = longdescdata.read()

setup(name = 'ArrayFunc',
      version = '0.9.1rc1',
      description = 'Fast array processing functions',
      long_description = long_description,
      url = 'https://github.com/arrayfunc/arrayfunc',
      author = 'M Griffin',
      author_email = 'm12.griffin@gmail.com',
      license = 'Apache License V2.0',
      classifiers = [
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Topic :: Scientific/Engineering :: Mathematics',
          'License :: OSI Approved :: Apache License V2.0',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          ],
      keywords = 'mathematical array functions',
      packages=find_packages(exclude=['benchmarks', 'codegen', 'unittests']
      ),






