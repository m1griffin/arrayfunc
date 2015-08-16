##############################################################################
# Project:  arrayfunc
# Purpose:  Common code for library C code and unit test generation.
# Language: Python 3.4
# Date:     23-May-2014
#
###############################################################################
#
#   Copyright 2014 - 2015    Michael Griffin    <m12.griffin@gmail.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
##############################################################################


# ==============================================================================

import datetime
import csv
import itertools

# ==============================================================================


# This gives us the order in which to create the code blocks.
arraycodes = ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']
intarrays = ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q')
floatarrays = ('f', 'd')
unsignedint = ('B', 'H', 'I', 'L', 'Q')
signedint = ('b', 'h', 'i', 'l', 'q')


# This defines how python array codes translate to C data types.
arraytypes = {'b' : 'signed char', 'B' : 'unsigned char', 
	'h' : 'signed short', 'H' : 'unsigned short', 
	'i' : 'signed int', 'I' : 'unsigned int', 
	'l' : 'signed long', 'L' : 'unsigned long', 
	'q' : 'signed long long', 'Q' : 'unsigned long long', 
	'f' : 'float', 'd' : 'double'}



# ==============================================================================

# Some architectures do not support 'q' or 'Q' array types. 
LongLongTestSkip = """# Cannot test if 'q' or 'Q' arrays are not supported in this architecture.
@unittest.skipIf('%(typecode)s' not in array.typecodes, 'Skip test if array type not supported on this platform.')
"""
# For 'q' arrays.
LongLongTestSkipq = LongLongTestSkip % {'typecode' : 'q'}
# For 'Q' arrays.
LongLongTestSkipQ = LongLongTestSkip % {'typecode' : 'Q'}

# This adds an indent to skip specific tests rather than classes.
# For 'q' and 'Q' arrays.
FuncLongLongTestSkip = "@unittest.skipIf('q' not in array.typecodes, 'Skip test if array type not supported on this platform.')"

# ==============================================================================

# Overflow tests for array type 'I'. With some architectures, we cannot check
# the parameters for overflow because there is no larger integer size.
OvflTestSkip = """	# Whether this test can be peformed depends on the integer word sizes in for this architecture.
	@unittest.skipIf(arrayfunc.arraylimits.I_max == arrayfunc.arraylimits.L_max, 
		'Skip test if I integer does not have overflow checks.')
"""

# ==============================================================================

# MSVC 2010 appears to have bugs when converting float or double to unsigned long long.
MSVCQTestSkip = """	# MSVC 2010 appears to have bugs when converting float or double to unsigned long long.
	@unittest.skipIf(platform.python_compiler().startswith('MSC'), 'Skip test due to bugs in the platform C compiler.')
"""

# This version is used to skip entire classes rather than just individual functions.
MSVCQTestSkipFunc = """# MSVC 2010 appears to have bugs when converting float or double to unsigned long long.
@unittest.skipIf(platform.python_compiler().startswith('MSC'), 'Skip test due to bugs in the platform C compiler.')
"""

# ==============================================================================

# This defines the minimum value for each type.
minvalue = {
	'b' : 'SCHAR_MIN',	# signed char
	'B' : '0',			# unsigned char
	'h' : 'SHRT_MIN',	# signed short
	'H' : '0',			# unsigned short
	'i' : 'INT_MIN',	# signed int
	'I' : '0',			# unsigned int
	'l' : 'LONG_MIN',	# signed long
	'L' : '0',			# unsigned long
	'q' : 'LLONG_MIN',	# signed long long
	'Q' : '0',			# unsigned long long
	'f' : '-FLT_MAX',	# float
	'd' : '-DBL_MAX'	# double
}

# This defines the maximum value for each type.
maxvalue = {
	'b' : 'SCHAR_MAX',	# signed char
	'B' : 'UCHAR_MAX',	# unsigned char
	'h' : 'SHRT_MAX',	# signed short
	'H' : 'USHRT_MAX',	# unsigned short
	'i' : 'INT_MAX',	# signed int
	'I' : 'UINT_MAX',	# unsigned int
	'l' : 'LONG_MAX',	# signed long
	'L' : 'ULONG_MAX',	# unsigned long
	'q' : 'LLONG_MAX',	# signed long long
	'Q' : 'ULLONG_MAX',	# unsigned long long
	'f' : 'FLT_MAX',	# float
	'd' : 'DBL_MAX'		# double
}

# ==============================================================================

arraytypeclass = {
	'b' : {'typecode' : 'b', 'typelabel' : 'b', 'typeconvert' : 'int', 'skiplonglong' : ''},
	'B' : {'typecode' : 'B', 'typelabel' : 'B', 'typeconvert' : 'int', 'skiplonglong' : ''}, 
	'h' : {'typecode' : 'h', 'typelabel' : 'h', 'typeconvert' : 'int', 'skiplonglong' : ''}, 
	'H' : {'typecode' : 'H', 'typelabel' : 'H', 'typeconvert' : 'int', 'skiplonglong' : ''}, 
	'i' : {'typecode' : 'i', 'typelabel' : 'i', 'typeconvert' : 'int', 'skiplonglong' : ''}, 
	'I' : {'typecode' : 'I', 'typelabel' : 'I', 'typeconvert' : 'int', 'skiplonglong' : ''}, 
	'l' : {'typecode' : 'l', 'typelabel' : 'l', 'typeconvert' : 'int', 'skiplonglong' : ''}, 
	'L' : {'typecode' : 'L', 'typelabel' : 'L', 'typeconvert' : 'int', 'skiplonglong' : ''}, 
	'q' : {'typecode' : 'q', 'typelabel' : 'q', 'typeconvert' : 'int', 'skiplonglong' : LongLongTestSkipq}, 
	'Q' : {'typecode' : 'Q', 'typelabel' : 'Q', 'typeconvert' : 'int', 'skiplonglong' : LongLongTestSkipQ}, 
	'f' : {'typecode' : 'f', 'typelabel' : 'f', 'typeconvert' : 'float', 'skiplonglong' : ''}, 
	'd' : {'typecode' : 'd', 'typelabel' : 'd', 'typeconvert' : 'float', 'skiplonglong' : ''},
	'bytes' : {'typecode' : 'B', 'typelabel' : 'bytes', 'typeconvert' : 'int', 'skiplonglong' : ''}, 
}

# ==============================================================================

# When converting from floating point to integer, resolution is lost if the integer
# word size is larger than the resolution (precision) of the floating point
# value. This means there is a grey area near the limits of the integer values
# where conversion from floating point to integer may cause an unexpected integer
# roll-over. The solution adopted is to use guard band limits which are slightly
# smaller than the actual maximum integer value.
maxguardvalue = {
	'd' : {'l' : 'LONG_MAX_GUARD_D', 'L' : 'ULONG_MAX_GUARD_D', 
			'q' : 'LLONG_MAX_GUARD_D', 'Q' : 'ULLONG_MAX_GUARD_D'},
	'f' : {'i' : 'INT_MAX_GUARD_F', 'I' : 'UINT_MAX_GUARD_F',
			'l' : 'LONG_MAX_GUARD_F', 'L' : 'ULONG_MAX_GUARD_F',
			'q' : 'LLONG_MAX_GUARD_F', 'Q' : 'ULLONG_MAX_GUARD_F'},
}

minguardvalue = {
	'd' : {'l' : 'LONG_MIN_GUARD_D', 'L' : '0', 
			'q' : 'LLONG_MIN_GUARD_D', 'Q' : '0'},
	'f' : {'i' : 'INT_MIN_GUARD_F',  'I' : '0',
			'l' : 'LONG_MIN_GUARD_F', 'L' : '0', 
			'q' : 'LLONG_MIN_GUARD_F', 'Q' : '0'},
}

# ==============================================================================


def ReadCSVData():
	"""Read the operator and function definition data from a CSV file. All of
	the data to create the C code is stored in a spreadsheet and then saved to
	a CSV file. This function reads in the file, and saves it in a list of
	dictionaries. While doing this, sanatize the data to take out "'" characters
	which were added to prevent conflicts with spreadsheet codes. 

	The first row of the spreadsheet is used as the expected key names.

	"""
	csvreaddata = []
	with open('arrayfunc.csv', 'r') as csvfile:
		opreader = csv.reader(csvfile, delimiter='\t')
		# The first row is the descriptive headers, which we use as key names.
		dataformat = next(opreader)
		# Read in all the data at once so we can work on it more easily. 
		for rec in opreader:
			csvreaddata.append(dict([(x,y.replace("'", '')) for x,y in zip(dataformat, rec)]))

		# Sanitise the data to remove quote characters which were added to the
		# spreadsheet to prevent conflicts with spreadsheet formatting codes.
		csvdata = []
		for rec in csvreaddata:
			rec['pyoperator'] = rec['pyoperator'].replace("'", '')
			csvdata.append(rec)


	return csvdata

# ==============================================================================


# This is used to auto-generate the copyright header for the unit test.

HeaderTemplate = '''#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   %(testfilename)s.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     %(startdate)s.
# Ver:      %(verdate)s.
#
###############################################################################
#
#   Copyright 2014 - %(cpyear)s    Michael Griffin    <m12.griffin@gmail.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
##############################################################################
"""This conducts unit tests for %(funcname)s.
"""

##############################################################################
import array
import itertools
import math
import operator
import platform

import unittest

import arrayfunc

##############################################################################

##############################################################################

# The following code is all auto-generated.


'''


# ==============================================================================

# Format and return the data for the copyright header files.
def FormatHeaderData(testfilename, startdate, funcname):
	"""Format and return the dictionary data used in the copyright header. 
	Parameters: testfilename = The file name to go in the header.
		startdate = The date the file was started on.
		funcname = The function name(s) to use in the doc string for the module.
	Returns: <dict>
	"""
	testdate = datetime.date.today()
	testdatestamp = testdate.strftime('%d-%b-%Y')
	testyear = testdate.year

	return {'testfilename' : testfilename, 
		'startdate' : startdate, 
		'verdate' : testdatestamp, 
		'cpyear' : testyear, 
		'funcname' : funcname}


# ==============================================================================

