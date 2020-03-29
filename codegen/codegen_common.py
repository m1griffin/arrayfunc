##############################################################################
# Project:  arrayfunc
# Purpose:  Common code for library C code and unit test generation.
# Language: Python 3.4
# Date:     23-May-2014
#
###############################################################################
#
#   Copyright 2014 - 2018    Michael Griffin    <m12.griffin@gmail.com>
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
import re
import glob
import os.path

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




# Used to look up documentation of array types.
def FormatDocsArrayTypes(docarraytypes):
	"""Take the string from the 'arraytypes' column of the math spreadsheet, 
	and use it to look up a properly formatted version which lists the 
	actual array type codes.
	Parameters: docarraytypes (string) - The string from the spreadsheet which
		contains a combination of 'si', 'ui', and 'f'.
	Returns: (string) - A string which converts the above to a comma separated
		series of array code letters.
	"""
	# Array types to test.
	docsplit = set(docarraytypes.split(','))


	# All array types supported.
	if docsplit == {'si', 'ui', 'f'}:
		return ', '.join(arraycodes)
	# Only signed array types.
	elif docsplit == {'si', 'f'}:
		return ', '.join(signedint + floatarrays)
	# Only integer arrays.
	elif docsplit == {'si', 'ui'}:
		return ', '.join(intarrays)
	# Only floating point arrays.
	elif docsplit == {'f'}:
		return ', '.join(floatarrays)
	else:
	# No matching value.
		raise ValueError



# ==============================================================================

# Overflow tests for array type 'I'. With some architectures, we cannot check
# the parameters for overflow because there is no larger integer size.
OvflTestSkip = """	# Whether this test can be peformed depends on the integer word sizes in for this architecture.
	@unittest.skipIf(arrayfunc.arraylimits.I_max == arrayfunc.arraylimits.L_max, 
		'Skip test if I integer does not have overflow checks.')
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
	'b' : {'typecode' : 'b', 'typelabel' : 'b', 'typeconvert' : 'int'},
	'B' : {'typecode' : 'B', 'typelabel' : 'B', 'typeconvert' : 'int'}, 
	'h' : {'typecode' : 'h', 'typelabel' : 'h', 'typeconvert' : 'int'}, 
	'H' : {'typecode' : 'H', 'typelabel' : 'H', 'typeconvert' : 'int'}, 
	'i' : {'typecode' : 'i', 'typelabel' : 'i', 'typeconvert' : 'int'}, 
	'I' : {'typecode' : 'I', 'typelabel' : 'I', 'typeconvert' : 'int'}, 
	'l' : {'typecode' : 'l', 'typelabel' : 'l', 'typeconvert' : 'int'}, 
	'L' : {'typecode' : 'L', 'typelabel' : 'L', 'typeconvert' : 'int'}, 
	'q' : {'typecode' : 'q', 'typelabel' : 'q', 'typeconvert' : 'int'}, 
	'Q' : {'typecode' : 'Q', 'typelabel' : 'Q', 'typeconvert' : 'int'}, 
	'f' : {'typecode' : 'f', 'typelabel' : 'f', 'typeconvert' : 'float'}, 
	'd' : {'typecode' : 'd', 'typelabel' : 'd', 'typeconvert' : 'float'},
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

# These are the compare operations used in some functions.
CompOps = [
{'opcodename' : 'AF_EQ', 'compare_ops' : '=='},
{'opcodename' : 'AF_GT', 'compare_ops' : '>'},
{'opcodename' : 'AF_GTE', 'compare_ops' : '>='},
{'opcodename' : 'AF_LT', 'compare_ops' : '<'},
{'opcodename' : 'AF_LTE', 'compare_ops' : '<='},
{'opcodename' : 'AF_NE', 'compare_ops' : '!='}
]


def ReadCSVData(filename):
	"""Read the operator and function definition data from a CSV file. All of
	the data to create the C code is stored in a spreadsheet and then saved to
	a CSV file. This function reads in the file, and saves it in a list of
	dictionaries. While doing this, sanatize the data to take out "'" characters
	which were added to prevent conflicts with spreadsheet codes. 

	The first row of the spreadsheet is used as the expected key names.

	"""
	csvreaddata = []
	with open(filename, 'r') as csvfile:
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
# Project:  %(modulename)s
# Module:   %(testfilename)s.py
# Purpose:  %(modulename)s unit test.
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
import sys

%(arrayimport)s
import itertools
import math
import operator
import platform
import copy

import unittest

import %(modulename)s

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

# This is added to the end of each unit test.
testendtemplate = """
##############################################################################
if __name__ == '__main__':

	# Check to see if the log file option has been selected. This is an option
	# which we have added in order to decide where to output the results.
	if '-l' in sys.argv:
		# Remove the option from the argument list so that "unittest" does 
		# not complain about unknown options.
		sys.argv.remove('-l')

		with open('%(testprefix)s_unittest.txt', 'a') as f:
			f.write('\\n\\n')
			f.write('%(funcname)s\\n\\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
"""

# ==============================================================================

# This is used to auto-generate the copyright header for the C source code.
CHeaderTemplate = '''\
//------------------------------------------------------------------------------
// Project:  arrayfunc
// Module:   %(cfilename)s
// Purpose:  %(purpose1)s
//           %(purpose2)s
// Language: C
// Date:     %(startdate)s
// Ver:      %(verdate)s.
//
//------------------------------------------------------------------------------
//
//   Copyright 2014 - %(cpyear)s    Michael Griffin    <m12.griffin@gmail.com>
//
//   Licensed under the Apache License, Version 2.0 (the "License");
//   you may not use this file except in compliance with the License.
//   You may obtain a copy of the License at
//
//       http://www.apache.org/licenses/LICENSE-2.0
//
//   Unless required by applicable law or agreed to in writing, software
//   distributed under the License is distributed on an "AS IS" BASIS,
//   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//   See the License for the specific language governing permissions and
//   limitations under the License.
//
//------------------------------------------------------------------------------
'''

# These are the standard includes. There is one string substitution format
# String to allow extra dependencies to be included.
CIncludes = '''
/*--------------------------------------------------------------------------- */
// This must be defined before "Python.h" in order for the pointers in the
// argument parsing functions to work properly. 
#define PY_SSIZE_T_CLEAN

#include "Python.h"
%s
#include "arrayerrs.h"
'''

# This must be added if the function has an SIMD implementation.
CSIMDdefMsg = '''
#include "simddefs.h"
'''

# This is required to actually include the SIMD implementation. Note the 
# string substitution required.
CSIMDMacroMsg = '''
#ifdef AF_HASSIMD
#include "%(funcname)s_simd_x86.h"
#endif
'''

# This closes off the header and adds a message that everything after is auto
# generated code.
CHeaderEnd = '''
/*--------------------------------------------------------------------------- */

/*--------------------------------------------------------------------------- */

// Auto generated code goes below.
'''


# ==============================================================================

# Format and return the data for the copyright header files.
def FormatCCodeHeaderData(cfilename, purpose1, purpose2, startdate):
	"""Format and return the dictionary data used in the C source copyright header. 
	Parameters: cfilename = The file name to go in the header.
		purpose1 = First line of description.
		purpose2 = Second line of description.
		startdate = The date the file was started on.
	Returns: <dict>
	"""
	codedate = datetime.date.today()
	codedatestamp = codedate.strftime('%d-%b-%Y')
	codeyear = codedate.year

	return {'cfilename' : cfilename, 
		'purpose1' : purpose1,
		'purpose2' : purpose2,
		'startdate' : startdate, 
		'verdate' : codedatestamp, 
		'cpyear' : codeyear}


# ==============================================================================

# These are the possible extra C headers to be added to the source code.
_COutputHeaderOptions = {
	'limits' : '#include <limits.h>', 
	'float' : '#include <float.h>', 
	'math' : '#include <math.h>', 
	'arithcalcs' : '#include "arithcalcs.h"', 
	'simddefs' : '#include "simddefs.h"', 
	'simdmacromsg' : '#ifdef AF_HASSIMD_X86\n#include "%(funcname)s_simd_x86.h"\n#endif',
	'simdmacromsg_armv7' : '#ifdef AF_HASSIMD_ARMv7_32BIT\n#include "arm_neon.h"\n#endif',
	'simdmacromsg_armv8' : '#ifdef AF_HASSIMD_ARM_AARCH64\n#include "arm_neon.h"\n#endif',
	'acalcvm_ops' : '#include "acalcvm_ops.h"',
	'guardbands' : '#include "convguardbands.h"',
	'arrayfunc' : '#include "arrayfunc.h"',
	'arrayparams_base' : '#include "arrayparams_base.h"',
	'arrayops' : '#include "arrayops.h"',
	}


# This can be added as a description to the platform independent source files.
PlatformIndependentDescr = 'Common platform independent code.'

# This can be added as a description to SIMD source files.
SIMDDescription = 'This file provides an SIMD version of the functions.'


def OutputSourceCode(filename, outputlist, purpose1, purpose2, startdate, funcname, 
			extraheaders): 
	"""Write out the C source code to a file, including copyright header and other info.
	Parameters: filename = The name to use for the file. 
		outputlist = The list of text strings which makes up the source code.
		purpose1 = The first line of the copyright header 'purpose' description.
		purpose2 = The second line of the 'purpose' description.
		startdate = The date the original file was started.
		funcname = The name of the function to be used in CSIMDMacroMsg. This is
			may be left blank for SIMD source. 
		extraheaders = A list of strings defining which extra C headers 
			(e.g. #include <float.h>) to include in the source code.
	"""
	with open(filename, 'w') as f:
		# Output the copyright header.
		f.write(CHeaderTemplate % FormatCCodeHeaderData(filename, 
				purpose1, purpose2, startdate))

		if extraheaders:
			extrincl = '\n' + '\n'.join([_COutputHeaderOptions[x] for x in extraheaders]) + '\n'
			cincludextra = extrincl % {'funcname' : funcname}
		else:
			cincludextra = ''

		f.write(CIncludes % cincludextra)

		f.write(CHeaderEnd)

		# Output the C source code.
		for x in outputlist:
			f.write(x)


# ==============================================================================


def OutputCHeader(filename, headedefs, purpose1, purpose2, startdate): 
	"""Write out the C source code to a file for .h files, including copyright 
		header and other info.
	Parameters: filename = The name to use for the file. 
		headedefs = The list of text strings which makes up the source code.
		purpose1 = The first line of the copyright header 'purpose' description.
		purpose2 = The second line of the 'purpose' description.
		startdate = The date the original file was started.
	"""
	with open(filename, 'w') as f:
		f.write(CHeaderTemplate % FormatCCodeHeaderData(filename, 
			purpose1, purpose2, startdate))
		f.write('\n\n')
		for x in headedefs:
			f.write(x)
		f.write('\n\n')

# ==============================================================================

def GenCHeaderText(outputlist, funcname):
	"""Output the .h header file for the platform independent C source code. 
		This works by searching through the C code looking for anything that 
		looks like an appropriate C function.
	Parameters: outputlist = The list of blocks of text containing the C 
			function source code. 
		funcname = The name of the function (e.g. amax, or aany). This is used
			to search for the source code function name.
		Returns: A list of strings containing the C header definitions.
	"""
	textblock = '\n'.join(outputlist)

	# Create the regex pattren by combining the basic pattern with all possible
	# C data types as return types. We're basically looking for somethinge
	# like 'Py_ssize_t compress_.*?{' and all possible variations.
	ctnames = ['Py_ssize_t', 'void'] + list(arraytypes.values())
	pattern = '|'.join([x +  (' %s_.*?{' % funcname) for x in ctnames])

	# Perform the regex match. The flags=re.DOTALL causes the match to ignore
	# newline characters.
	headertext = re.findall(pattern, textblock, flags=re.DOTALL)
	headerblock = '\n'.join(headertext)
	# Replace the '{' character at the end of all the matches with a ';'.
	return re.sub(' {', ';', headerblock, flags=re.DOTALL)



# ==============================================================================


def GenSIMDCHeaderText(outputlist, funcname):
	"""Output the .h header file for the SIMD C source code. 
		This works by searching through the C code looking for anything that 
		looks like an appropriate C function.
	Parameters: outputlist = The list of blocks of text containing the C 
			function source code. 
		funcname = The name of the function (e.g. amax, or aany). This is used
			to search for the source code function name.
		Returns: A list of strings containing the C header definitions.
	"""
	# Split the blocks of text into separate list elements so we can search them.
	# We need to flatten the list, otherwise we will have lists of lists.
	splitoutput = itertools.chain.from_iterable([x.splitlines() for x in outputlist])

	# Find the list elements which include the function defintions. While we're
	# at it, strip off the trailing ' {' and replace it with a ';'.
	return [x.rstrip(' {') + ';\n' for x in splitoutput if (' ' + funcname + '_' in x)]


# ==============================================================================


# ==============================================================================

# Read the C function names from the SIMD header files.
def GetHeaderFileDataSIMD(filepath):
	"""Get the names of functions which have SIMD acceleration. This
		works by reading the C source code header file names and 
		extracting the name of the function from the file names. This 
		assumes that the file name follows a specific convention.
		It also searches through the file to find C function names
		and extracts the data types from it. 
		The C source code files must be in a specific position relative
		to this script.
	Parameters: filepath (string): Get the path defining the SIMD files.
		Returns: (list) a list of arrayfunc function names and the data
			types used by that arrayfunc function.
	"""
	# Get a list of the SIMD related header files.
	filelist=glob.glob(filepath)
	filelist.sort()

	filedata = []


	for fname in filelist:
		# This gets the function name from the file, assuming the function
		# name is the first part of the file name (e.g. aall_simd_x86.h ).
		simdfile = os.path.basename(fname)
		funcname = re.split('_simd', simdfile)[0]

		with open(fname, 'r') as f:
			typemaps = dict(zip(arraytypes.values(), itertools.repeat(False)))
			cfuncs = [x for x in f if '_simd(' in x]

			for line in cfuncs:
				# Trim off everything from _simd and to the right.
				funcstart = line.partition('_simd(')[0]
				# Split off the return value.
				cfuncname = funcstart.rpartition(' ')[2]
				# Get the type the function handles.
				afunctype = cfuncname.split('_')[1:]
				# Some functions have a trailing underscore that results in
				# an extra space that needs to be filtered out. E.g. and_, or_
				if afunctype[0] == '':
					afunctype = afunctype[1:]
				# Take care of instances where there are multiple numbered versions.
				if afunctype[-1].isdigit():
					afunctype = afunctype[:-1]
				# Take care of cass where there is an extra descriptive element in the
				# first part of the list. This happens in cases where a comparison
				# character is passed as a parameter (e.g. with aall, aany, etc.).
				if afunctype[0] in ('eq', 'lt', 'le', 'gt', 'ge', 'ne'):
					afunctype = afunctype[1:]
				# Put the type label back together if there is more than one word.
				afunclabel = ' '.join(afunctype)

				typemaps[afunclabel] = True
				

			filedata.append((funcname, typemaps))

	return filedata


# ==============================================================================

