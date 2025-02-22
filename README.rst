=========
ArrayFunc
=========

:Authors:
    Michael Griffin

:Version:  8.5.3 for 2025-01-13
:Copyright: 2014 - 2025
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

If you are installing on an ARM platform such as the Raspberry Pi, see the
installation notes at the end before attempting to install from PyPI using PIP.

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
       pow2 x * x or math.pow(x, 2)
       pow3 x * x * x or math.pow(x, 3)
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

======================= ======= ==== ======== =======
OS                       Arch   Bits Compiler Python 
======================= ======= ==== ======== =======
almalinux 9.5           x86_64   64  GCC      3.9.19   
alpine 3.20.3           i686     32  GCC      3.12.7  
Debian 12               i686     32  GCC      3.11.2   
Debian 12               x86_64   64  GCC      3.11.2   
FreeBSD 14.1            amd64    64  Clang    3.11.10
OpenBSD 7.6             amd64    64  Clang    3.11.10
Raspbian 12             armv7l   32  GCC      3.11.2 
Ubuntu 24.04            aarch64  64  GCC      3.12.3 
Debian 12               aarch64  64  GCC      3.11.2 
opensuse-leap 15.6      x86_64   64  GCC      3.6.15    
Ubuntu 24.04            x86_64   64  GCC      3.12.3 
Ubuntu 24.10            x86_64   64  GCC      3.12.7 
MS Windows 11           AMD64    64  MSC      3.13.1 
======================= ======= ==== ======== =======

amd64 and x86_64 are two names for the same thing.
armv7l is 32 bit ARM. aarch64 is 64 bit ARM.
The ARM test hardware consists of Raspberry PI
models 3, 4, and 5.



* The Rasberry Pi 3 tests were conducted on a Raspberry Pi 3 ARM CPU running
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
	# Force install from PyPI source instead of using a binary wheel.
	pip3 install --user --force-reinstall --no-binary=:all: arrayfunc
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


Recent versions of PyPI seem to be building their own binary wheels for some 
platforms using their own infrastruction. This may result in an invalid ARM 
binary on Raspberry Pi. 

If you have difficulties, then either download the tar.gz version and install 
it locally (see the above instructions for a local install). Alternatively,
see the above example for how to force a binary install instead of using a 
wheel. There is also a bash script called "setupuser.sh" which will call setup.
py directly with the appropriate parameters. 

The setup.py file has platform detection code which it uses to pass the 
correct flags to the C compiler. For ARM, this includes the CPU type. If you
are using an ARM CPU type which is not recognized then setup.py may not
compile in SIMD features. You can experiment with modifying setup.py to add
new ARM models, but be sure that anything you try is compatible with the 
existing ones.


Installing on Linux with PIP and PEP-668
----------------------------------------
PEP-668 (PEPs describe changes to Python) introduced a new feature which can
affect how packages are installed with PIP. If PIP is configured to be 
EXTERNALLY-MANAGED it will refuse to install a package outside of a virtual
environment.

The intention of this is to prevent conflicts between packages which are 
installed using the system package manager, and ones which are installed using
PIP.

Linux distros which are affeced by this include the latest versions of Debian
and Ubuntu.

As this package is a library which is intended to be used by other 
applications, there is no one right way to install it, whether inside or 
outside of a virtual environment. Review the options available with PIP to see
what is suitable for your application.

For testing purposes this package was installed by setting the environment
variable PIP_BREAK_SYSTEM_PACKAGES to "1", which effectively disables this
feature in PIP. 

example::

	export PIP_BREAK_SYSTEM_PACKAGES=1


---------------------------------------------------------------------

Release History
===============
* 8.5.3 - Update to testing and support. There were no code changes.
          Changes were made to unit testing and benchmark support
          scripts to support a new testing environment.
          Python support was updated to 3.13 on Windows OS.
* 8.5.2 - Update to testing and support. There were no code changes. 
          Python version on Windows 10 and 11 was updated to version 3.12.
* 8.5.1 - Update to testing and support. There were no code. changes. 
          Ubuntu version updated to 23.04. AlmaLinux updated to 9.1. 
          Alpine Linux updated to 3.17.3. FreeBSD updated to 13.2. 
          OpenBSD updated to 7.3. 
          On Ubuntu 23.04, the installation method has changed due to how 
          PEP-668 was implemented by Debian and how this affects "pip". 
          Some other distros may experience the same problems if they made 
          the same changes. See the README.TxT for details. 
* 8.5.0 - Added pyproject.toml file to satisfy Python 3.11 requirements.
          Updated build scripts to use python3 -m build instead of calling
          setup.py directly. Test targets were updated, Ubuntu 20.04 was 
          dropped, Ubuntu 22.10 was added, FreeBSD python version upgraded 
          to 3.9, OpenBSD upgraded to 7.2, Windows 10 Python upgraded to 3.11,
          Windows 11 Python upgraded to 3.11. Removed duplicate assignment in
          parameter parsing return data in arrayparams_asum.c. 
          Added __version__ attribute to allow checking package version 
          number at run time. Added version unit test. Updated setup.py 
          and other files to allow the version number to be automatically 
          updated from a single source at build time.
* 8.4.1 - Minor bug fix for asum for unsigned integer SIMD on ARM. This 
          corrects the function return type for SIMD operations on ARM.
          No incorrect behaviour was found in the original, but this change
          was made to ensure correctness. 
* 8.4.0 - Major performance improvements for asum through the use of SIMD and
          other optimizations. 
* 8.3.0 - Fixed the effects of an apparent compiler bug affecting 32 bit 
          x86 only for function asum. Tested and verified on 32 bit Debian 
          and 32 bit Alpine. This would in a few very specific circumstances 
          result in the sum of a float array (array code 'f') exceeding 
          the valid range for a float instead of returning infinity. The
          fix forces the result to infinity in these cases. Also tested
          with new releases of Alma 9 and Alpine 3.16. 
* 8.2.0 - Update to testing and support. Tested with new releases of Ubuntu 
          22.04 and OpenBSD 7.1. Changed "simdsupport" to also report the 
          architecture the binary was compiled for. "Simdsupport" is only
          used for testing and benchmarking and is not a stable part of
          the release.
* 8.1.2 - Bump to correct minor documentation error in README.rst. 
* 8.1.1 - Update to testing and support. Raspberry Pi 32 bit OS updated to
          version 2022-04-04. Update to setup.py to improve ARM version 
          detection.
* 8.1.0 - Update to testing and support. Centos has been replaced by 
          AlmaLinux due to Red Hat ending long term support for Centos.
          No actual code changes.
* 8.0.1 - Technical bump to version number to include update information.
* 8.0.0 - Performance improvements in add, sub, mul, neg, abs, ceil, floor, 
          trunc, sqrt, degrees, radians. Asum will now use error checking 
          with floating point SIMD by default where available. Benchmarks
          and unit tests have been updated accordingly.
* 7.2.0 - Performance improvements in asum and pow. Asum will now use error
          checking with floating point SIMD on x86_64 by default. Pow has
          special cases for powers of 2 and 3 on integer arrays which allow
          for much greater performance. Pow will now raise a value error
          exception if an attempt to raise to a negative number. This makes it
          it more compatible with Python. New functions pow2 and pow3 added
          which raise array values to powers of 2 and 3 respectively. These
          have additional optimisations beyond pow, particularly with floating
          point arrays. Benchmarks for add, floordiv, mod, mul, pow, sub, and
          truediv have been changed to make them run the expanded range of
          tests much faster. 
* 7.1.0 - This is a bugfix release to correct mod, mul, and pow. This affects
          integer overflow checking at extremes, particularly with the greatest
          magnitude negative number on signed arrays. Certain combinations of
          numbers may have produced an overflow error when the result was at 
          the negative margin of the numeric range (e.g. -128 for array type
          'b' when -2 is raised to the power of 7). The errors have been fixed,
          including adding special cases. Also, when 1 or -1 was raised to a
          very large power this would cause the algorithm to work for a very
          long time to produce an answer (e.g. 1 to the power of 4 billion).
          This is now detected and a special case added to short circuit the
          calculation to produce the answer. The unit tests for these and 
          related functions have been updated to include a much wider range 
          of test data.
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


