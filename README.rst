=========
ArrayFunc
=========

:Authors:
    Michael Griffin

:Version: 4.2.0 for 2018-12-22
:Copyright: 2014 - 2018
:License: This document may be distributed under the Apache 2.0 License.
:Language: Python 3.5 or later

---------------------------------------------------------------------

Introduction
============

The arrayfunc module provides high speed array processing functions for use with
the standard Python array module. These functions are patterned after the
functions in the standard Python Itertools and math module together with some 
additional ones from other sources.

The purpose of these functions is to perform mathematical calculations on arrays
faster than using native Python.

See full documentation at: http://arrayfunc.readthedocs.io/en/latest/

---------------------------------------------------------------------

Function Summary
================


The functions fall into several categories.

Filling Arrays
--------------

========= ======================================================================
Function    Description
========= ======================================================================
count      Fill an array with evenly spaced values using a start and step 
           values.
cycle      Fill an array with evenly spaced values using a start, stop, and step 
           values, and repeat until the array is filled.
repeat     Fill an array with a specified value.
========= ======================================================================


Filtering Arrays
----------------

============== =================================================================
Function         Description
============== =================================================================
afilter         Select values from an array based on a boolean criteria.
compress        Select values from an array based on another array of boolean
                values.
dropwhile       Select values from an array starting from where a selected 
                criteria fails and proceding to the end.
takewhile       Like dropwhile, but starts from the beginning and stops when the
                criteria fails.
============== =================================================================


Examining and Searching Arrays
------------------------------

============== =================================================================
Function         Description
============== =================================================================
findindex       Returns the index of the first value in an array to meet the
                specified criteria.
findindices     Searches an array for the array indices which meet the specified 
                criteria and writes the results to a second array. Also returns
                the number of matches found.
============== =================================================================


Summarising Arrays
------------------

============== =================================================================
Function         Description
============== =================================================================
aany            Returns True if any element in an array meets the selected
                criteria.
aall            Returns True if all element in an array meet the selected
                criteria.
amax            Returns the maximum value in the array.
amin            Returns the minimum value in the array.
asum            Calculate the arithmetic sum of an array.
============== =================================================================


Data Conversion
---------------

========= ======================================================================
Function   Description
========= ======================================================================
convert    Convert arrays between data types. The data will be converted into
           the form required by the output array.
========= ======================================================================


Mathematical operator functions
-------------------------------


=========== ===============================================
  Function              Equivalent to
=========== ===============================================
        add x + y
    truediv x / y
   floordiv x // y
        mod x % y
        mul x * y
        neg -x
        pow x**y or math.pow(x, y)
        sub x - y
      abs\_ abs(x)
=========== ===============================================

Comparison operator functions
-----------------------------


=========== ===============================================
  Function              Equivalent to
=========== ===============================================
         eq x == y
         gt x > y
         ge x >= y
         lt x < y
         le x <= y
         ne x != y
=========== ===============================================

Bitwise operator functions
--------------------------


=========== ===============================================
  Function              Equivalent to
=========== ===============================================
      and\_ x & y
       or\_ x | y
        xor x ^ y
     invert ~x
     lshift x << y
     rshift x >> y
=========== ===============================================

Power and logarithmic functions
-------------------------------


=========== ===============================================
  Function              Equivalent to
=========== ===============================================
        exp math.exp(x)
      expm1 math.expm1(x)
        log math.log(x)
      log10 math.log10(x)
      log1p math.log1p(x)
       log2 math.log2(x)
       sqrt math.sqrt(x)
=========== ===============================================

Hyperbolic functions
--------------------


=========== ===============================================
  Function              Equivalent to
=========== ===============================================
      acosh math.acosh(x)
      asinh math.asinh(x)
      atanh math.atanh(x)
       cosh math.cosh(x)
       sinh math.sinh(x)
       tanh math.tanh(x)
=========== ===============================================

Trigonometric functions
-----------------------


=========== ===============================================
  Function              Equivalent to
=========== ===============================================
       acos math.acos(x)
       asin math.asin(x)
       atan math.atan(x)
      atan2 math.atan2(x, y)
        cos math.cos(x)
      hypot math.hypot(x, y)
        sin math.sin(x)
        tan math.tan(x)
=========== ===============================================

Angular conversion
------------------


=========== ===============================================
  Function              Equivalent to
=========== ===============================================
    degrees math.degrees(x)
    radians math.radians(x)
=========== ===============================================

Number-theoretic and representation functions
---------------------------------------------


=========== ===============================================
  Function              Equivalent to
=========== ===============================================
       ceil math.ceil(x)
   copysign math.copysign(x, y)
       fabs math.fabs(x)
  factorial math.factorial(x)
      floor math.floor(x)
       fmod math.fmod(x, y)
   isfinite math.isfinite(x)
      isinf math.isinf(x)
      isnan math.isnan(x)
      ldexp math.ldexp(x, y)
      trunc math.trunc(x)
=========== ===============================================

Special functions
-----------------


=========== ===============================================
  Function              Equivalent to
=========== ===============================================
        erf math.erf(x)
       erfc math.erfc(x)
      gamma math.gamma(x)
     lgamma math.lgamma(x)
=========== ===============================================

Additional functions
--------------------


=========== ===============================================
  Function              Equivalent to
=========== ===============================================
        fma fma(x, y, z) or x * y + z
=========== ===============================================


Attributes
__________

In addition to functions, a set of attributes are provided representing the 
platform specific maximum and minimum numerical values for each array type. 
These attributes are part of the "arraylimits" module.

---------------------------------------------------------------------

Supported Array Types
=====================

Arrayfunc supports all standard Python 3.x array types.


---------------------------------------------------------------------

Performance
===========

Average performance increase on x86_64 Ubuntu with GCC is 100 times faster than 
native Python. Performance will vary depending on the function, operation, array 
data type used, and whether overflow checking is enabled, with the performance 
increase ranging from 50% to 500 times. 

Other platforms show similar improvements.

Detailed performance figures are listed in the full documentation.


---------------------------------------------------------------------

Platform support
================

Arrayfunc is written in 'C' and uses the standard C libraries to implement the 
underlying math functions. Arrayfunc has been tested on the following platforms.

================= ========  ========================== =========================
OS                   Bits      Compiler                  Python Version Tested
================= ========  ========================== =========================
Ubuntu 18.04 LTS   64 bit    GCC                         3.6
Ubuntu 18.10       64 bit    GCC                         3.6
Debian 9           32 bit    GCC                         3.5
Debian 9           64 bit    GCC                         3.5
OpenSuse 15        64 bit    GCC                         3.6
Centos 7           64 bit    GCC                         3.6
FreeBSD 12         64 bit    LLVM                        3.6
MS Windows 10      64 bit    MS Visual Studio C 2015     3.7
Raspbian (RPi 3)   32 bit    GCC                         3.5
================= ========  ========================== =========================

The Raspbian (RPi 3) tests were conducted on a Raspberry Pi ARM CPU. All others
were conducted using VMs running on x86 hardware. 

---------------------------------------------------------------------

Installation
============

Please note that this is a Python 3 package. To install using Pip, you will 
need (with Debian package in brackets):

* The appropriate C compiler and header files (gcc and build-essential).
* The Python3 development headers (python3-dev).
* Pip3 together with the corresponding Setuptools (python3-pip).

example::

	# Install from PyPI.
	pip3 install arrayfunc
	# Install from a local copy of the source package (Linux).
	pip3 install --no-index --find-links=. arrayfunc
	# Windows seems to use "pip" instead of "pip3" for some reason.
	pip install arrayfunc

---------------------------------------------------------------------

Release History
===============

* 4.2.0 - Added fma function. This has no equivalent in the Python 
          standard library but is equivalent to x * y + z. Also changed
          list of supported platforms to update FreeBSD to version 12
          and added Centos 7.
* 4.1.0 - Added isfinite function.
* 4.0.1 - Repeat upload to synchronise source and Windows binary "wheel"
          version. PyPI was not happy with the previous attempt. 
* 4.0.0 - Major revision with many changes. Amap, starmap, and acalc were 
          replaced with new individual functions. This change was made to 
          provides a simpler and more consistent interface which is tailored to
          the individual function rather than attempting to make one parameter 
          format fit all. The "disovfl" parameter has been named to "matherrors" 
          in order to better reflect that it encompasses more than just integer
          overflow. Support for the "bytes" type has been removed. The Raspberry
          Pi has been added as a supported platform.
* 3.1.0 - Added log2 to amap, amapi, and acalc.
* 3.0.0 - Changed package format to "Wheel" files. No functional changes.
* 2.1.1 - Fixed missing header files in PyPI package. No functional changes.
* 2.0.0 - Many changes. Updated MS Windows support to 3.6 and latest compiler.
          This in turn brought the Windows version up to feature parity with
          the other versions. Changed supported MS Windows version from 32 bit
          to 64 bit. Added SIMD support for some functions which provided a 
          significant performance for those affected. Updated supported versions
          of Debian and FreeBSD to current releases.
* 1.1.0 - Added support for math constants math.pi and math.e.
* 1.0.0 - First release.
