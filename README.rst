=========
ArrayFunc
=========

:Authors:
    Michael Griffin

:Copyright: 2014 - 2015
:License: This document may be distributed under the Apache 2.0 License.
:Language: Python 3.x

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
============== =================================================================

Amap and amapi support more than 70 different operations. Starmap and starmapi
support more than two dozen different operations.


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

Average performance increase for amap is 95 times faster than native Python.
For functions other than amap, amapi, starmap, and starmapi is 63 times faster 
than native Python. However, some functions and operations may be more than 350
times faster than native Python.

Detailed performance figures are listed in the documentation.


---------------------------------------------------------------------

Platform support
================

Arrayfunc is written in 'C' and uses the standard C libraries to implement the 
underlying math functions. Arrayfunc has been tested on the following platforms.

================= ========  ========================== =========================
OS                   Bits      Compiler                  Python Version Tested
================= ========  ========================== =========================
Ubuntu 14.04 LTS   64 bit    GCC                         3.4
Debian 8           32 bit    GCC                         3.4
FreeBSD 10         64 bit    LLVM                        3.4
MS Windows 8.1     32 bit    MS Visual Studio C 2010     3.4
================= ========  ========================== =========================

Some amap and amapi operations are not supported on MS Windows due to lack of 
compiler support. See the documentation for details.

