=========
ArrayFunc
=========

:Authors:
    Michael Griffin
    

:Version: 6.2.0 for 2021-06-05
:Copyright: 2014 - 2021
:License: This document may be distributed under the Apache License V2.0.
:Language: Python 3.6 or later


.. contents:: Table of Contents

---------------------------------------------------------------------

Introduction
============

The ArrayFunc module provides high speed array processing functions for use with
the standard Python array module. These functions are patterned after the
functions in the standard Python Itertools module together with some additional 
ones from other sources.

The purpose of these functions is to perform mathematical calculations on arrays
significantly faster than using native Python.


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
                criteria fails and proceeding to the end.
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

{summarytable}


Array Limit Attributes
----------------------

In addition to functions, a set of attributes are provided representing the 
platform specific maximum and minimum numerical values for each array type. 
These attributes are part of the "arraylimits" module.

---------------------------------------------------------------------


Searching and Summarising Arrays.
=================================

Comparison Operators
--------------------

Some functions use comparison operators. These are unicode strings containing
the Python compare operators and include following:

========= ============================
Operator   Description
========= ============================
 '<'       Less than.
 '<='      Less than or equal to.
 '>'       Greater than.
 '>='      Greater than or equal to.
 '=='      Equal to.
 '!='      Not equal to.
========= ============================

All comparison operators must contain only the above characters and may not
include any leading or trailing spaces or other characters.


Description
-----------

{extradocs}


arraylimits attributes
----------------------

A set of attributes are provided representing the platform specific maximum 
and minimum numerical values for each array type. These attributes are part of 
the "arraylimits" module.

Array integer sizes may differ on 32 versus 64 bit versions, plus other 
platform characteristics may also produce differences. 


================ =====================  =========== ============================
Array Type Code   Description            Min Value   Max Value
================ =====================  =========== ============================
b                 signed char            b_min       b_max
B                 unsigned char          B_min       B_max
h                 signed short           h_min       h_max
H                 unsigned short         H_min       H_max
i                 signed int             i_min       i_max
I                 unsigned int           I_min       I_max
l                 signed long            l_min       l_max
L                 unsigned long          L_min       L_max
q                 signed long long       q_min       q_max  
Q                 unsigned long long     Q_min       Q_max    
f                 float                  f_min       f_max 
d                 double                 d_min       d_max  
================ =====================  =========== ============================


example::

	import arrayfunc
	from arrayfunc import arraylimits

	arrayfunc.arraylimits.b_min
	==> -128
	arrayfunc.arraylimits.b_max
	==> 127
	arrayfunc.arraylimits.f_min
	==> -3.4028234663852886e+38
	arrayfunc.arraylimits.f_max
	==> 3.4028234663852886e+38

---------------------------------------------------------------------


Mathematical Functions
======================

Description
-----------

Mathematical functions provide similar functionality to the functions of the 
same name in the standard library "math" and "operator" modules, but operate 
over whole arrays instead of on a single value.

Mathematical functions can accept a variety of different combinations of array
and numerical parameters. Each function will automatically detect the category 
of parameter and adjust its behaviour accordingly. 

Output can be either into a separate output array, or in-place (into the 
original array) if no output array is provided.


Parameter Forms
_______________


This example will subtract 10 from each element of array 'x', replacing the 
original data.::

 x = array.array('b', [20,21,22,23,24,25])
 arrayfunc.sub(x, 10)


This example will do the same, but place the results into array 'z', leaving the
original array unchanged.::

 x = array.array('b', [20,21,22,23,24,25])
 z = array.array('b', [0] * len(x))
 arrayfunc.sub(x, 10, z)


This is similar to the first one, but performs the calculation of '10 - x' 
instead of 'x - 10'.::

 x = array.array('b', [20,21,22,23,24,25])
 arrayfunc.sub(10, x)


This example takes each element of array 'x', adds the corresponding element of
array 'y', and puts the result in array 'z'.::

 x = array.array('b', [20,21,22,23,24,25])
 y = array.array('b', [10,5,55,42,42,0])
 z = array.array('b', [0] * len(x))
 arrayfunc.add(x, y, z)


Parameter Type Consistency
__________________________

Unless otherwise noted, all array and numeric parameters must be of the same
type when calling a mathematical function. That is, you may not mix integer
and floating point, or different integer sizes in the same calculation. Failing
to use consistent parameters will result in an exception being raised.



Using Less than the Entire Array
________________________________

If the size of the array is larger than the desired length of the calculation,
it may be limited to the first part of the array by using the 'maxlen' 
parameter. In the following example only the first 3 array elements will be
operated on, with the following ones left unchanged.::

 x = array.array('b', [20,21,22,23,24,25])
 arrayfunc.add(x, 10, maxlen=3)


Suppressing or Ignoring Math Errors
___________________________________

Functions can be made to ignore some mathematical errors (e.g. integer 
overflow) by setting the 'matherrors' keyword parameter to True.::

 x = array.array('b', [20,21,22,23,24,25])
 arrayfunc.add(x, 235, matherrors=True)


However, not all math errors can be suppressed, only those which would not 
otherwise cause a fatal error (e.g. division by zero). 

Ignoring errors may be desirable if the side effect (e.g. the result of an 
integer overflow) is the intended effect, or for reasons of a minor performance
improvement in some cases. Note that any such performance improvement will
vary greatly depending upon the specific function and array type. Benchmark
your calculation before deciding if this is worth while.


Differences with Native Python
______________________________


In many cases the Python 'math' module functions are thin wrappers around the
underlying C library, as is 'arrayfunc'.

However, in some cases 'arrayfunc' will not produce exactly the same result as
Python. There are several reasons for this, the primary one being that
arrayfunc operates on different underlying data types. Specifically, arrayfunc
uses the platform's native integer and floating point types as exposed by the
array module. For example, Python integers are of arbitrary size and can never
overflow (Python simply expands the word size indefinitely), while arrayfunc
integers will overflow the same as they would with programs written in C.

Think of arrayfunc as exposing C style semantics in a form convenient to use
in Python. Some convenience which Python provides (e.g. no limit to the size of 
integers) is traded off for large performance increases.

However, Arrayfunc does implement the mod or '%' operator in a manner which is
compatible with Python, not 'C'. The C method will produce mathematically
incorrect answers under some ranges of values (as will many other programming
languages as well as some popular spreadsheets which use the C compiler without 
correction). Python implements this in a mathematically correct manner in all 
cases, and Arrayfunc follows suit.


Arrayfunc diverges from Python in the following areas:

* The handling of non-finite floating point values such as 'NaN' (not-a-number) 
  and +/-Inf in calculations may not always be compatible.
* The 'floor' function will return a floating point value when floating point
  arrays are used, rather than an integer. This is necessary to maintain
  compatibility with the array parameters.
* Floordiv does not behave the same as '//' when working with infinity. When
  dividing positive or negative infinity by any number, the arrayfunc version 
  of floordiv will return +/- infinity, while the Python '//' operator will
  return 'NaN' (not-a-number) in each case.
* Binary operations such as shift and invert will operate according to their 
  native array data types, which may differ from Python's own integer 
  implementation. This is necessary because the array integer is of fixed size
  (Python integers can be infinitely large) and has both signed and unsigned
  types (Python integers are signed only).
* "Mod" does not behave exactly as "%" does for floating point. X % inf and
  x % -inf will return nan rather than +/- inf.
* The type of exception raised when an error is encountered in Python versus
  arrayfunc may not be the same in all cases.


Other Notes
___________


* Ldexp only accepts an integer number as the second parameter, not an array.
* Math.pow is not implemented because it duplicates the operator pow (and the 
  names would collide in arrayfunc).
* Fma is not part of the Python standard library, but has been offered here
  as an additional feature.



{opdocs}



---------------------------------------------------------------------

Option Flags and Parameters
===========================

Arithmetic Overflow Control
---------------------------

Many functions allow integer overflow detection to be turned off if desired. 
See the list of operators for which operators this applies to. 

Integer overflow is when a number becomes too large to fit within the specified
word size for that array data type. For example, an unsigned char has a range
of 0 to 255. When a calculation overflows, it "wraps around" one or more times
and produces an arithmetically invalid result.

If it is known in advance that overflow cannot occur (due to the size of the
numbers), or if overflow is a desired side effect, then overflow checking may
be disabled via the "matherrors" parameter. Setting "matherrors" to true will 
*disable* overflow checking, while setting it to false will *enable* overflow 
checking. Checking is enabled by default, including when the "matherrors" 
parameter is not specified.

Disabling overflow checking can significantly increase the speed of calculation,
with the amount of improvement depending on the type of calculation being 
performed and the data type used.


Using Only Part of an Array
---------------------------

The array math functions only use existing arrays that the user provides and do 
not create new arrays or resize existing ones. The reason for this is that when
very large arrays are being used, continually allocating and de-allocating 
arrays can take too much time, plus this may result in problems controlling how
much memory is used.

Since the filter functions (or other data sources) may not use all of an output 
array, and the result may vary depending on the data, most functions provide an 
optional keyword parameter which limits the functions to part of the array. The
"maxlen" parameter specifies the maximum number of array elements to use, 
starting from the beginning of the array. 

For example, specifying a "maxlen" of 10 for a 20 element array will limit a 
function to using only the first 10 array elements and ignoring the rest of the
array.

If the array length limit value is zero, negative, or greater than the actual 
size of the array, the length limit will be ignored and the entire array used. 
The default is to use the entire array.


SIMD Control
------------

SIMD (Single Instruction Multiple Data) is a set of CPU features which allow
multiple operations to take place in parallel. Some, but not all, functions will
make use of these instructions to speed up execution. 

Those functions which do support SIMD features will automatically make use of 
them by default unless this feature is disabled. There is normally no reason
to disable SIMD, but should there be hardware related problems the function can
be forced to fall back to conventional execution mode. 

If the optional parameter "nosimd" is set to true ("nosimd=True"), SIMD 
execution will be disabled. The default is "False". 

To repeat, there is normally no reason to wish to disable SIMD. 

See the documentation section on SIMD support has more detail.


---------------------------------------------------------------------

Data Types
==========

Array Types
-----------

The following array types from the Python standard library are supported.

================ ===============================================================
Array Type Code   Description
================ ===============================================================
b                 signed char
B                 unsigned char
h                 signed short
H                 unsigned short
i                 signed int
I                 unsigned int
l                 signed long
L                 unsigned long
q                 signed long long
Q                 unsigned long long
f                 float
d                 double
================ ===============================================================


Numeric Parameter Types
-----------------------

================ ===============================================================
Python Type       Description
================ ===============================================================
integer           Integral values such as 0, 1, 100, -99, etc.
floating point    Real numbers such as 0.0, 1.93, 3.1417, -5693.0, etc.
================ ===============================================================

The numeric type must be compatible with the array type code. 

The 'L' and 'Q' type parameters cannot be checked for integer overflow due to a 
mismatch between Python and 'C' language numeric limits. 


Maximum Array Size
------------------

Arrays are limited to no more than the number of elements defined by the Python
C API constant Py_ssize_t. The size of this will depend on your platform 
characteristics. However, it will normally allow for arrays larger than can be
contained in memory for most computers. 

When creating very large arrays, it is recommended to consider using 
itertools.repeat as an initializer or to use array.extend or array.append
to add to an array rather than using a list as an initializer. Lists use much
more memory than arrays (even for the same data type), and it is easy to
run out of memory if you are not careful when creating very large arrays from
lists.




Platform Compiler Support
-------------------------

Beginning with version 2.0 of ArrayFunc, versions compiled with the Microsoft 
MSVS compiler now has feature parity with the GCC version. This change is due 
to the Microsoft C compiler now supporting a new enough version of the 'C' 
standard.


Integer Error Checking
----------------------

Error checking in integer operators is conducted as follows:

Error Categories
___________________


====================  ============ =========== ============= ===================
Operation              Result out   Divide by   Negate max.   Parameter is
                       of range     zero        negative      negative
                                                signed int 
====================  ============ =========== ============= ===================
Addition (+)              X
Subtraction (-)           X
Modulus (%)                             X            X
Multiplication (*)        X
Division (/, //)                        X            X
Negation (-)                                         X
Absolute Value                                       X
Factorial                 X                                    X
Power (**)                X                                    X
====================  ============ =========== ============= ===================

* Negation of the maximum negative signed in (the most negative integer for that
  array type) can be caused by negation, absolute value, division, and modulus 
  operations. Since signed integers do not have a symmetrical range (e.g. -128 
  to 127 for 8 bit sizes) anything which attempts to convert (in this example) 
  -128 to +128 would cause an overflow back to -128.
* The factorial of negative numbers is undefined. 
* Powers are not calculated for integers raised to negative powers, as integer
  arrays cannot contain fractional results.


Disabling Integer Division by Zero Checks
_________________________________________

Division by zero cannot be disabled for integer division or modulus operations.
Division by zero could cause seg faults (crashes), so this option is ignored for
these functions.


Floating Point NaN and Infinity
_______________________________

Floating point numbers include three special values, NaN (Not a Number), and
negative and positive infinity. Arrayfunc uses the platform C compiler to create
executable code. Some compilers may produce different results than other 
compilers under certain conditions when operating on NaN and infinity values. In
addition, the Arrayfunc results may differ from those in native Python on some
platforms when using NaN and infinity as inputs.


However, since using NaN and infinity as numeric inputs is not a common
operation, this is unlikely to be a serious problem when writing cross platform
code in most cases. 

---------------------------------------------------------------------

Exceptions
==========

Exceptions - General
--------------------

The following exceptions apply to most functions.

==================  ===========================================  ======================================================
Exception type      Text                                           Description
==================  ===========================================  ======================================================
ArithmeticError     arithmetic error in calculation.             An arithmetic error occurred in a calculation.
ZeroDivisionError   zero division error in calculation.          A calculation attempted to divide by zero.
IndexError          array length error.                          One or more arrays has an invalid length (e.g a 
                                                                 length of zero).
IndexError          input array length error.                    The input array has an invalid length.
IndexError          output length error.                         The output array has an invalid length.
IndexError          array length mismatch.                       Two or more arrays which are expected to be of equal 
                                                                 length are not.
OverflowError       arithmetic overflow in calculation.          An arithmetic integer overflow occurred in a 
                                                                 calculation. 
OverflowError       arithmetic overflow in parameter.            The size or range of a non-array parameter was not
                                                                 compatible with the array parameters.
TypeError           array and parameter type mismatch.           A non-array parameter data type was not compatible 
                                                                 with the array parameters.
TypeError           array type mismatch.                         An array parameter is not compatible with another
                                                                 array parameter. For most functions, both arrays 
                                                                 must be of the same type.
TypeError           unknown array type.                          The array type is unknown.
TypeError           array.array expected.                        A non-array parameter was found where an array 
                                                                 parameter was expected. 
ValueError          operator not valid for this function.        An operator parameter used was not valid for this
                                                                 function. 
ValueError          operator not valid for this platform.        The operator used is not supported on this platform.
TypeError           parameter error.                             An unspecified error occurred when parsing the 
                                                                 parameters.
TypeError           parameter missing.                           An expected parameter was missing. 
ValueError          parameter not valid for this operation.      A value is not valid for this operation. E.g.
                                                                 attempting to perform a factorial on a negative 
                                                                 number.
IndexError          selector length error.                       The selector array length is incorrect.
ValueError          conversion not valid for this type.          The conversion attempted was invalid.
ValueError          cannot convert float NaN to integer.         Cannot convert NaN (Not A Number) floating point
                                                                 value in the input array to integer.
TypeError           output array type invalid.                   The output array type is invalid.
==================  ===========================================  ======================================================


---------------------------------------------------------------------


Platform Oddities
=================

As most operators are implemented using native behaviour, details of some 
operations may depend on the CPU architecture.

Lshift and rshift will exhibit a behaviour that depends on the CPU type 
whether it is 32 or 64 bit, and array size. 

For 32 bit x86 systems, if the array word size is 32 bits or less, the shift 
is masked to 5 bits. That is, shift amounts greater than 32 will "roll over",
repeating smaller shifts.

On 64 bit systems, this behaviour will vary depending on whether SIMD is used
or not. This, arrays which are not even multiples of SIMD register sizes may
exibit different behaviour at different array indexes (depending on whether 
SIMD or non-SIMD instructions were used for those parts of the array).

ARM does not display this roll-over behaviour, and so may give different
results than x86. However, negative shift values may result in the shift
operation being conducted in the opposite direction (e.g. right shift instead
of left shift).

The conclusion is that bit shift operations which use a shift amount which is
not in the range of 0 to "maximum number" may produce undefined results.
So valid bit shift amounts should be 0 to 7, 0 to 15, 0 to 31 and 0 to 63,
depending on the array type.


---------------------------------------------------------------------

SIMD Support
============

General
-------

SIMD (Single Instruction Multiple Data) is a set of CPU features which allow
multiple operations to take place in parallel. Some, but not all, functions will
make use of these instructions to speed up execution. 

Those functions which do support SIMD features will automatically make use of 
them by default unless this feature is disabled. There is normally no reason
to disable SIMD, but should there be hardware related problems the function can
be forced to fall back to conventional execution mode. 


Platform Support
----------------

SIMD instructions are presently supported only on the following:

* 64 bit x86 (i.e. AMD64) using GCC.
* 32 bit ARMv7 using GCC (tested on Raspberry Pi 3).
* 64 bit ARMv8 AARCH64 using GCC (tested on Raspberry Pi 4).

Other compilers or platforms will still run the same functions and should 
produce the same results, but they will not benefit from SIMD acceleration. 

However, non-SIMD functions will still be much faster standard Python code. See
the performance benchmarks to see what the relative speed differences are. With
wider data types (e.g. double precision floating point) SIMD provides only
marginal speed ups anyway. 



Raspberry Pi 32 versus 64 bit
-----------------------------

The Raspberry Pi uses an ARM CPU. This can operate in 32 or 64 bit mode. When
in 32 bit mode, the Raspberry Pi 3 operates in ARMv7 mode. This has 64 bit ARM
NEON SIMD vectors.

When in 64 bit mode, it acts as an ARMv8, with AARCH64 128 bit ARM NEON SIMD
vectors.

The Raspbian Linux OS is 32 bit mode only. Other distros such as Ubuntu offer
64 bit versions. 

The "setup.py" file uses platform detection code to determine which ARM CPU
and mode it is running on. Due to the availability of hardware for testing,
this code is tailored to the Raspberry Pi 3 and Raspberry Pi 4 and the 
operating systems listed. This code then selects the appropriate compiler 
arguments to pass to the setup routines to tell the compiler what mode to 
compile for.

If other ARM platforms are used which have different platform signatures or
which require different compiler arguments, the "setup.py" file may need to be
modified in order to use SIMD acceleration.

However, the straight 'C' code should still compile and run, and still provide 
performance many times faster than when using native Python.


Data Type Support
-----------------

x86-64
______

The following table shows which array data types are supported by x86-64 
SIMD instructions.

{simddata_x86}


ARMv7
_____

The following table shows which array data types are supported by ARMv7 
SIMD instructions.

{simddata_armv7}


ARMv8 AARCH64
_____________

The following table shows which array data types are supported by ARMv8 
SIMD instructions.

{simddata_armv8}


SIMD Support Attributes
-----------------------

There is an attribute which can be tested to detect if ArrayFunc is compiled 
with SIMD support and if the current hardware supports the required SIMD level.

arrayfunc.simdsupport.hassimd

The attribute "hassimd" will be True if the module supports SIMD.

example::

	import arrayfunc
	arrayfunc.simdsupport.hassimd
	==> True


---------------------------------------------------------------------

Performance
===========

Variables affecting Performance
-------------------------------

The purpose of the Arrayfunc module is to execute common operations faster than
native Python. The relative speed will depend upon a number of factors:

* The function.
* The data type of the array.
* Function options. Turning checking off will result in faster performance.
* The data in the arrays and the parameters. 
* The size of the array.
* The platform, including CPU type (e.g. x86 or ARM), operating system, 
  and compiler.

The speeds listed below should be used as rough guidelines only. More exact
results will require application specific testing. The numbers shown are the
execution time of each function relative to native Python. For example, a value 
of '50' means that the corresponding Arrayfunc operation ran 50 times faster 
than the closest native Python equivalent. 

Both relative performance (the speed-up as compared to Python) and absolute
performance (the actual execution speed of Python and ArrayFunc) will vary
significantly depending upon the compiler (which is OS platform dependent) and 
whether compiled to 32 or 64 bit. If your precise actual benchmark performance 
results matter, be sure to conduct your testing using the actual OS and compiler 
your final program will be deployed on. The values listed below were measured on 
x86-64 Linux compiled with GCC. 


Note: Some more complex Arrayfunc functions do not work exactly the same way as 
the built-in or "itertools" Python equivalents. This means that the benchmark 
results should be taken as general guidelines rather than precise comparisons. 


Typical Performance Readings
----------------------------

Default Performance
___________________


In this set of tests, all error checking was turned on and SIMD 
acceleration was enabled where this did not conflict with the preceding
(the defaults in each case). 

{pybench}


Optimised Performance (with SIMD)
_________________________________

In this set of tests, all arithmetic error checking was disabled (not the 
default state) and SIMD acceleration was enabled (the normal default).
Note that there may be unexpected slight differences as compared to the 
previous data table due to variations in test timing.

This data may be of some use when estimating if any useful performance
gains can be made in your specific application by disabling error 
checking in order to enable SIMD operations. It is not recommended
to disable math error checking without good reason.

{simdbench}


SIMD Optimisation Effects
_________________________

This set of tests shows what the effect of SIMD optimisations are for those
functions which support it. SIMD optimisations are enabled by default except in
a few cases where they conflict with math error checking (in which case error 
checking must be disabled to use them). This information may be useful in 
deciding which platform you wish to use to run your application. This
data is primarily of interest in judging expected benchmark performance
on different platforms. 

{simdrelbench}


Array Size Versus Performance
_____________________________


The following shoes the effects of array size on a selected arrayfunc function 
benchmark.

As array size increases, function call overhead decreases as a proportion of
total run time. 

Declines in performance when the array exceeds a certain size may be related to
hardware cache effects. Arrayfunc functions together with their data may be
able to reside entirely in cache, but larger arrays may require repeated cache
reloads. This threshold will depend upon the particular hardware being used.

{arraysizebench}



Platform Effects
----------------

The platform, including CPU, OS, compiler, and compiler version can 
affect performance, and this influence can change significantly for 
different functions. 

If your application requires exact performance data, then benchmark
your application in the specific platform (hardware, OS, and compiler) 
that you will be using.


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
Debian 10              32 bit    GCC               3.7
Debian 10              64 bit    GCC               3.7
OpenSuse 15.3          64 bit    GCC               3.6
Centos 8.4             64 bit    GCC               3.6
FreeBSD 13             64 bit    LLVM              3.7
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

