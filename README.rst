=========
ArrayFunc
=========

:Authors:
    Michael Griffin

:Version: 3.0.0 for 2017-08-27
:Copyright: 2014 - 2017
:License: This document may be distributed under the Apache 2.0 License.
:Language: Python 3.5 or later

---------------------------------------------------------------------

Introduction
============

The arrayfunc module provides high speed array processing functions for use with
the standard Python array module. These functions are patterned after the
functions in the standard Python Itertools module together with some additional 
ones from other sources.

The purpose of these functions is to perform mathematical calculations on arrays
faster than using native Python.

---------------------------------------------------------------------

Functions
=========

Summary
-------

The functions fall into several categories.

Filling Arrays
______________

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
________________

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
______________________________

============== =================================================================
Function         Description
============== =================================================================
aany            Returns True if any element in an array meets the selected
                criteria.
aall            Returns True if all element in an array meet the selected
                criteria.
amax            Returns the maximum value in the array.
amin            Returns the minimum value in the array.
findindex       Returns the index of the first value in an array to meet the
                specified criteria.
findindices     Searches an array for the array indices which meet the specified 
                criteria and writes the results to a second array. Also returns
                the number of matches found.
============== =================================================================


Operating on Arrays
___________________

============== =================================================================
Function         Description
============== =================================================================
amap            Apply an operator to each element of an array, together with an 
                optional second parameter (for operators taking two parameters).
                The results are written to a second array.
amapi           Like amap, but the results are written in place to the input
                array.
starmap         Like amap, but where a second array acts as the second 
                parameter. The results are written to an output array.
starmapi        Like starmap, but the results are written in place to the first 
                input array.
asum            Calculate the arithmetic sum of an array.
acalc           Calculate arbitrary equations over an array. 
============== =================================================================

Amap and amapi support more than 70 different operations. Starmap and starmapi
support more than two dozen different operations. ACalc supports more than 50
operations.


Data Conversion
_______________

========= ======================================================================
Function   Description
========= ======================================================================
convert    Convert arrays between data types. The data will be converted into
           the form required by the output array.
========= ======================================================================

Attributes
__________

In addition to functions, a set of attributes are provided representing the 
platform specific maximum and minimum numerical values for each array type. 
These attributes are part of the "arraylimits" module.

---------------------------------------------------------------------

Supported Array Types
=====================

Arrayfunc supports all standard Python 3.x array types, as well as the 'bytes' 
type.


---------------------------------------------------------------------

Performance
===========

Performance will vary depending on the function, operation, array data type 
used, and whether overflow checking is enabled. 

Average performance increase for amap is 80 times faster than native Python.
Functions other than amap, starmap, and acalc average is 50 times faster  than
native Python. However, some functions and operations may be more than 200 to 
300 times faster than native Python.

Detailed performance figures are listed in the documentation.


---------------------------------------------------------------------

Platform support
================

Arrayfunc is written in 'C' and uses the standard C libraries to implement the 
underlying math functions. Arrayfunc has been tested on the following platforms.

================= ========  ========================== =========================
OS                   Bits      Compiler                  Python Version Tested
================= ========  ========================== =========================
Ubuntu 16.04 LTS   64 bit    GCC                         3.5
Debian 9           32 bit    GCC                         3.5
Debian 9           64 bit    GCC                         3.5
FreeBSD 11         64 bit    LLVM                        3.5
MS Windows 10      64 bit    MS Visual Studio C 2015     3.6
================= ========  ========================== =========================


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

* 1.0.0 - First release.
* 1.1.0 - Added support for math constants math.pi and math.e.
* 2.0.0 - Many changes. Updated MS Windows support to 3.6 and latest compiler.
          This in turn brought the Windows version up to feature parity with
          the other versions. Changed supported MS Windows version from 32 bit
          to 64 bit. Added SIMD support for some functions which provided a 
          significant performance for those affected. Updated supported versions
          of Debian and FreeBSD to current releases.
* 2.1.1 - Fixed missing header files in PyPI package. No functional changes.
* 3.0.0 - Changed package format to "Wheel" files. No functional changes.
