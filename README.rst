=========
ArrayFunc
=========

:Authors:
    Michael Griffin

:Version: 7.0.0 for 2021-09-07
:Copyright: 2014 - 2021
:License: This document may be distributed under the Apache 2.0 License.
:Language: Python 3.6 or later

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

Average performance increase on x86_64 Ubuntu with GCC is 100 times faster 
than native Python. Performance will vary depending on the function, 
operation, array data type used, and whether overflow checking is enabled, 
with the performance increase ranging from 50% to 3000 times. 

Other platforms show similar improvements.

Detailed performance figures are listed in the full documentation.


---------------------------------------------------------------------

Platform support
================

Arrayfunc is written in 'C' and uses the standard C libraries to implement the 
underlying math functions. Arrayfunc has been tested on the following platforms.

===================== ========  =============== =========================
OS                      Bits      Compiler        Python Version Tested
===================== ========  =============== =========================
Ubuntu 20.04 LTS       64 bit    GCC               3.8
Ubuntu 21.04           64 bit    GCC               3.9
Debian 11              32 bit    GCC               3.9
Debian 11              64 bit    GCC               3.9
OpenSuse 15.3          64 bit    GCC               3.6
Centos 8.4             64 bit    GCC               3.6
FreeBSD 13             64 bit    LLVM              3.8
OpenBSD 6.9            64 bit    LLVM              3.8
MS Windows 10          64 bit    MS VS C 2015      3.9
Raspbian (RPi 3)       32 bit    GCC               3.7
Ubuntu 20.04 (RPi 4)   64 bit    GCC               3.8
===================== ========  =============== =========================

* The Raspbian (RPi 3) tests were conducted on a Raspberry Pi 3 ARM CPU running
  in 32 bit mode. 
* The Ubuntu ARM tests were conducted on a Raspberry Pi 4 ARM CPU running in
  64 bit mode.
* All others were conducted using VMs running on x86 hardware. 

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
	# Install a local package as a user package.
	pip3 install --user --no-index --find-links=. arrayfunc
	# Windows, FreeBSD, and OpenBSD seems to use "pip" instead 
	# of "pip3" for some reason.
	pip install arrayfunc


Newer versions of OpenBSD and FreeBSD will not install this package correctly 
when running setup.py directly. Use pip to install, even for local package
installs. Testing of this package has been changed to use only pip (or pip3)
in order to provide a common testing method for all platforms. Testing using
setup.py directly is no longer done.


---------------------------------------------------------------------

Release History
===============
* 7.0.0 - Major speed improvements to add, sub, mul, abs, neg using SIMD with 
          overflow checking on integer array types. SIMD is now active as the 
          default on integer arrays with smaller word sizes for these 
          functions. Major speed improvements on x86 for lshift and rshift by
          adding SIMD support to addition integer array types. This was already
          present on ARM. Added benchmark for "convert" (this was missing). 
          Debian test platforms were updated to latest versions (11). 
* 6.2.0 - Updated benchmarks to make each one a separate file. Centos and
          OpenSuse test platforms updated to latest versions.
* 6.1.1 - Documentation updated and version number bumped to reflect testing 
          with Ubuntu 21.04, FreeBSD 13.0, and OpenBSD 6.9. No code changes.
* 6.1.0 - Changed convguardbands to narrow -ve guard bands by 1 to handle 
          LLVM warning. Changed setup.py to detect Raspberry Pi 4 and set the 
          compiler args accordingly. Added support for Pi 4. Dropped testing 
          of 64 bit mode on Pi 3. 
* 6.0.1 - Documentation updated to reflect testing with the release version
          of Ubuntu 20.04 ARM (Rasberry Pi), Ubuntu 2010 (x86-64), OpenBSD 6.8,
          and Python 3.9 on Windows. No code changes and no change in version 
          number.
* 6.0.0 - Documentation updated to reflect testing with the release version
          of Ubuntu 20.04. No code changes and no change in version number.
* 6.0.0 - Added SIMD support for ARMv8 AARCH64. This is 64 bit ARM on a
          Raspberry Pi3 when running 64 bit Ubuntu. Raspbian is 32 bit only
          and has 64 bit SIMD vectors. 64 bit ARM has 128 bit SIMD vectors
          and so offers improved performance.
* 5.1.1 - Updated and improved help documentation. Also updated test
          platforms and retested.
* 5.1.0 - This is a bug fix release only, centred around SIMD issues on
          x86-64 with GCC. In a previous release some of the x86-64 SIMD 
          code had been changed to take advantage of a sort of assisted
          auto-vectorisation present in GCC. However, certain operations
          on certain integer sizes with certain array types will cause 
          GCC to generate incorrect x86 SIMD operations, producting 
          integer overflow. The functions known to be affected are aall, 
          aany, findindex (B, H, I arrays), eq, ge, gt, le, lt, ne (B, 
          H, I arrays), and rshift (h, i arrays). ARM was not affected. 
          All auto-vectorisation, where used, has been changed back to 
          manually generated SIMD operations for both x86 and ARM. 
          Rshift no longer uses SIMD  operations for b, B, h, or i 
          arrays on x86. Lshift no longer  supports SIMD operations on 
          b or B arrays on x86. Add and sub no longer use SIMD for B, H,
          and I arrays on x86. Mul no longer uses SIMD on x86 for any
          array types. Where SIMD functionality has been removed on x86, 
          it of course is still supported through normal portable CPU 
          instructions. ARM SIMD support was not affected by these
          changes. Lost SIMD acceleration will be returned to x86 in a
          later release where possible after the necessary research has
          been conducted. Unit tests have been updated to cover a 
          greater range of integer values to test for this problem. 
          Platforms using compilers other than GCC were not affected by 
          this, as they did not use SIMD anyway. The main effect of this
          present change is that some calculations may be slower for
          some array types. The problem with GCC generating incorrect
          SIMD instructions in some circumstances is apparently a known 
          (but obscure) issue. This will be avoided in future releases
          by sticking with manual SIMD built-ins. Some source code files 
          have updated date stamps in this release but no substantive 
          code changes due to the template system used to auto-generate 
          code.
* 5.0.0 - The main focus of this release has been adding SIMD 
          acceleration support to the ARMv7 platform  (e.g. Raspberry 
          Pi 3). Also added SIMD support to 'lshift' and 'rshift' on
          x86-64 and ARM. Changed arrayparamsbase to fix compiler 
          warning on newer versions of GCC, but no change in actual
          operation. Updated supported OS versions tested, and added
          OpenBSD to supported platform list.
* 4.3.1 - Numerous performance inprovements through the use of SIMD
          acceleration in many functions. See the documentation to
          see which functions are affected. Restrictions on the use of 
          non-finite data in parameters has been relaxed where possible. 
          Repeat now allows non-finite data as fill values. For 
          findindices, if no matches are found the result code is now 
          0 (zero) instead of -1.
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
