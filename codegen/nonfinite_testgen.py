#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for math functions which use one input parameter.
# Language: Python 3.5
# Date:     08-Dec-2017
#
###############################################################################
#
#   Copyright 2014 - 2017    Michael Griffin    <m12.griffin@gmail.com>
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

import itertools
import codegen_common

# ==============================================================================


# This template is for functions which output a boolean result.
test_template_nonfinite = '''

##############################################################################
class %(funclabel)s_general_%(testlabel)s_%(typelabel)s(unittest.TestCase):
	"""Test for basic general function operation.
	test_template_nonfinite
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [%(test_op_x)s]

		datanan = [math.nan]
		datainf = [math.inf]
		dataninf = [-math.inf]

		self.data = array.array('%(typecode)s', xdata + data%(testlabel)s + xdata)

		self.expected = %(anyall)s([%(pyoperator)s(x) for x in self.data])

		self.limited = len(self.data) // 2

		limresults = [%(pyoperator)s(x) for x in self.data]
		self.expectedlim = %(anyall)s(limresults[:self.limited])


	########################################################
	def test_%(funclabel)s_a1(self):
		"""Test %(funclabel)s basic - Array code %(typelabel)s.
		"""
		result = arrayfunc.%(funcname)s(self.data)

		self.assertEqual(result, self.expected)


	########################################################
	def test_%(funclabel)s_a2(self):
		"""Test %(funclabel)s basic for return type - Array code %(typelabel)s.
		"""
		result = arrayfunc.%(funcname)s(self.data)

		self.assertIsInstance(result, bool)


	########################################################
	def test_%(funclabel)s_b1(self):
		"""Test %(funclabel)s with array maxlen  - Array code %(typelabel)s.
		"""
		result = arrayfunc.%(funcname)s(self.data, maxlen=self.limited)

		self.assertEqual(result, self.expectedlim)



##############################################################################

'''


# ==============================================================================

# This template is used to test for correct fuction for each of the non-finite
# data combiations - NaN, Inf, and -Inf.
nan_template = '''

##############################################################################
class %(funclabel)s_%(testlabel)s_%(typelabel)s(unittest.TestCase):
	"""Test for correct results for each of the non-finite data conditions.
	nan_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [%(test_op_x)s]

		datanan = [math.nan]
		datainf = [math.inf]
		dataninf = [-math.inf]


		self.cleandata = array.array('%(typecode)s', xdata + xdata)
		self.testdatacentre = array.array('%(typecode)s', xdata + data%(testlabel)s + xdata)
		self.testdatastart = array.array('%(typecode)s', data%(testlabel)s + xdata + xdata)
		self.testdataend = array.array('%(typecode)s', xdata + xdata + data%(testlabel)s)


	########################################################
	def test_%(funclabel)s_a1(self):
		"""Test %(funclabel)s no value to find - Array code %(typelabel)s.
		"""
		result = arrayfunc.%(funcname)s(self.cleandata)

		expected = %(anyall)s([%(pyoperator)s(x) for x in self.cleandata])

		# Should not find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_%(funclabel)s_a2(self):
		"""Test %(funclabel)s value to find in centre - Array code %(typelabel)s.
		"""
		result = arrayfunc.%(funcname)s(self.testdatacentre)

		expected = %(anyall)s([%(pyoperator)s(x) for x in self.testdatacentre])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_%(funclabel)s_a3(self):
		"""Test %(funclabel)s value to find at start - Array code %(typelabel)s.
		"""
		result = arrayfunc.%(funcname)s(self.testdatastart)

		expected = %(anyall)s([%(pyoperator)s(x) for x in self.testdatastart])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_%(funclabel)s_a4(self):
		"""Test %(funclabel)s value to find at end - Array code %(typelabel)s.
		"""
		result = arrayfunc.%(funcname)s(self.testdataend)

		expected = %(anyall)s([%(pyoperator)s(x) for x in self.testdataend])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_%(funclabel)s_b1(self):
		"""Test %(funclabel)s value to find beyond maxlen parameter - Array code %(typelabel)s.
		"""
		result = arrayfunc.%(funcname)s(self.testdataend, maxlen=len(self.testdataend) - 1)

		expected = %(anyall)s([%(pyoperator)s(x) for x in self.testdataend[:len(self.testdataend) - 1]])

		# Should find the value.
		self.assertEqual(result, expected)


##############################################################################

'''




# ==============================================================================


# The template used to generate the tests for testing invalid parameter types.
param_invalid_template = '''

##############################################################################
class %(funclabel)s_param_errors_%(testlabel)s_%(typelabel)s(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [%(test_op_x)s]

		datanan = [math.nan] * len(xdata)
		datainf = [math.inf] * len(xdata)
		dataninf = [-math.inf] * len(xdata)

		self.floatarray = array.array('%(typecode)s', xdata + data%(testlabel)s)
		self.floatarray2 = copy.copy(self.floatarray)

		self.testmaxlen = len(self.floatarray) // 2

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in xdata + xdata])


	########################################################
	def test_%(funclabel)s_a1(self):
		"""Test %(funclabel)s for integer array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		result = arrayfunc.%(funcname)s(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s(self.intarray)


	########################################################
	def test_%(funclabel)s_b1(self):
		"""Test %(funclabel)s for maxlen='a' - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		result = arrayfunc.%(funcname)s(self.floatarray, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s(self.floatarray2, maxlen='a')


	########################################################
	def test_%(funclabel)s_c1(self):
		"""Test %(funclabel)s for matherrors=True (unsupported option) - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		result = arrayfunc.%(funcname)s(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s(self.floatarray2, matherrors=True)


	########################################################
	def test_%(funclabel)s_d1(self):
		"""Test %(funclabel)s for missing array - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s()


	########################################################
	def test_%(funclabel)s_d2(self):
		"""Test %(funclabel)s for missing array with maxlen - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s(maxlen=self.testmaxlen)


	########################################################
	def test_%(funclabel)s_no_params_d3(self):
		"""Test %(funclabel)s with no parameters - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.%(funcname)s()


##############################################################################

'''

# ==============================================================================

# These are all the test code templates. 
test_templates = {'test_template_nonfinite' : test_template_nonfinite}


# ==============================================================================


# Select what non-finite value to use when testing how a function works.
nftestvals = {'isinf' : ['inf', 'ninf'],
			'isnan' : ['nan'],
			'isfinite' : ['inf', 'ninf', 'nan']
}


# Determines whether to use 'any' or 'all' when testing.
anyall = {'isinf' : 'any',
			'isnan' : 'any',
			'isfinite' : 'all'
}

# ==============================================================================

# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.

funclist = [x for x in oplist if x['test_op_templ'] == 'test_template_nonfinite']


# ==============================================================================


for func in funclist:

	funcname = func['funcname']
	filenamebase = 'test_' + funcname
	filename = filenamebase + '.py'
	headerdate = codegen_common.FormatHeaderData(filenamebase, '09-Dec-2017', funcname)

	with open(filename, 'w') as f:
		# The copyright header.
		f.write(codegen_common.HeaderTemplate % headerdate)

		testtemplate = test_templates[func['test_op_templ']]

		for functype in codegen_common.floatarrays:
			for testlabel in nftestvals[funcname]:
				funcdata = {'funclabel' : funcname, 'funcname' : funcname, 
					'pyoperator' : func['pyoperator'],
					'typelabel' : functype, 'typecode' : functype, 
					'test_op_x' : func['test_op_x'],
					'testlabel' : testlabel,
					'anyall' : anyall[funcname]}
				f.write(testtemplate % funcdata)

				# Test for invalid parameters. One template should work for all 
				# functions of this style.
				f.write(param_invalid_template % funcdata)

				# Tests involving NaN, inf, and -inf.
				f.write(nan_template % funcdata)


		f.write(codegen_common.testendtemplate % funcname)

# ==============================================================================

