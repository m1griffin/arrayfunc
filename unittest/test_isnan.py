#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_isnan.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     09-Dec-2017.
# Ver:      16-Nov-2018.
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
"""This conducts unit tests for isnan.
"""

##############################################################################
import sys

import array
import itertools
import math
import operator
import platform
import copy

import unittest

import arrayfunc

##############################################################################

##############################################################################

# The following code is all auto-generated.




##############################################################################
class isnan_general_nan_f(unittest.TestCase):
	"""Test for basic general function operation.
	test_template_nonfinite
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]

		datanan = [float('nan')]
		datainf = [float('inf')]
		dataninf = [float('-inf')]

		self.data = array.array('f', xdata + datanan + xdata)

		self.expected = any([math.isnan(x) for x in self.data])

		self.limited = len(self.data) // 2

		limresults = [math.isnan(x) for x in self.data]
		self.expectedlim = any(limresults[:self.limited])


	########################################################
	def test_isnan_a1(self):
		"""Test isnan basic - Array code f.
		"""
		result = arrayfunc.isnan(self.data)

		self.assertEqual(result, self.expected)


	########################################################
	def test_isnan_a2(self):
		"""Test isnan basic for return type - Array code f.
		"""
		result = arrayfunc.isnan(self.data)

		self.assertIsInstance(result, bool)


	########################################################
	def test_isnan_b1(self):
		"""Test isnan with array limit  - Array code f.
		"""
		result = arrayfunc.isnan(self.data, maxlen=self.limited)

		self.assertEqual(result, self.expectedlim)



##############################################################################



##############################################################################
class isnan_param_errors_nan_f(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]

		datanan = [float('nan')] * len(xdata)
		datainf = [float('inf')] * len(xdata)
		dataninf = [float('-inf')] * len(xdata)

		self.floatarray = array.array('f', xdata + datanan)
		self.floatarray2 = copy.copy(self.floatarray)

		self.testmaxlen = len(self.floatarray) // 2

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in xdata + xdata])


	########################################################
	def test_isnan_a1(self):
		"""Test isnan for integer array - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.isnan(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isnan(self.intarray)


	########################################################
	def test_isnan_b1(self):
		"""Test isnan for maxlen='a' - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.isnan(self.floatarray, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isnan(self.floatarray2, maxlen='a')


	########################################################
	def test_isnan_c1(self):
		"""Test isnan for matherrors=True (unsupported option) - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.isnan(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isnan(self.floatarray2, matherrors=True)


	########################################################
	def test_isnan_d1(self):
		"""Test isnan for missing array - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isnan()


	########################################################
	def test_isnan_d2(self):
		"""Test isnan for missing array with maxlen - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isnan(maxlen=self.testmaxlen)


	########################################################
	def test_isnan_no_params_d3(self):
		"""Test isnan with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isnan()


##############################################################################



##############################################################################
class isnan_nan_f(unittest.TestCase):
	"""Test for correct results for each of the non-finite data conditions.
	nan_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]

		datanan = [float('nan')]
		datainf = [float('inf')]
		dataninf = [float('-inf')]


		self.cleandata = array.array('f', xdata + xdata)
		self.testdatacentre = array.array('f', xdata + datanan + xdata)
		self.testdatastart = array.array('f', datanan + xdata + xdata)
		self.testdataend = array.array('f', xdata + xdata + datanan)


	########################################################
	def test_isnan_a1(self):
		"""Test isnan no value to find - Array code f.
		"""
		result = arrayfunc.isnan(self.cleandata)

		expected = any([math.isnan(x) for x in self.cleandata])

		# Should not find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isnan_a2(self):
		"""Test isnan value to find in centre - Array code f.
		"""
		result = arrayfunc.isnan(self.testdatacentre)

		expected = any([math.isnan(x) for x in self.testdatacentre])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isnan_a3(self):
		"""Test isnan value to find at start - Array code f.
		"""
		result = arrayfunc.isnan(self.testdatastart)

		expected = any([math.isnan(x) for x in self.testdatastart])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isnan_a4(self):
		"""Test isnan value to find at end - Array code f.
		"""
		result = arrayfunc.isnan(self.testdataend)

		expected = any([math.isnan(x) for x in self.testdataend])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isnan_b1(self):
		"""Test isnan value to find beyond limit parameter - Array code f.
		"""
		result = arrayfunc.isnan(self.testdataend, maxlen=len(self.testdataend) - 1)

		expected = any([math.isnan(x) for x in self.testdataend[:len(self.testdataend) - 1]])

		# Should find the value.
		self.assertEqual(result, expected)


##############################################################################



##############################################################################
class isnan_general_nan_d(unittest.TestCase):
	"""Test for basic general function operation.
	test_template_nonfinite
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]

		datanan = [float('nan')]
		datainf = [float('inf')]
		dataninf = [float('-inf')]

		self.data = array.array('d', xdata + datanan + xdata)

		self.expected = any([math.isnan(x) for x in self.data])

		self.limited = len(self.data) // 2

		limresults = [math.isnan(x) for x in self.data]
		self.expectedlim = any(limresults[:self.limited])


	########################################################
	def test_isnan_a1(self):
		"""Test isnan basic - Array code d.
		"""
		result = arrayfunc.isnan(self.data)

		self.assertEqual(result, self.expected)


	########################################################
	def test_isnan_a2(self):
		"""Test isnan basic for return type - Array code d.
		"""
		result = arrayfunc.isnan(self.data)

		self.assertIsInstance(result, bool)


	########################################################
	def test_isnan_b1(self):
		"""Test isnan with array limit  - Array code d.
		"""
		result = arrayfunc.isnan(self.data, maxlen=self.limited)

		self.assertEqual(result, self.expectedlim)



##############################################################################



##############################################################################
class isnan_param_errors_nan_d(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]

		datanan = [float('nan')] * len(xdata)
		datainf = [float('inf')] * len(xdata)
		dataninf = [float('-inf')] * len(xdata)

		self.floatarray = array.array('d', xdata + datanan)
		self.floatarray2 = copy.copy(self.floatarray)

		self.testmaxlen = len(self.floatarray) // 2

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in xdata + xdata])


	########################################################
	def test_isnan_a1(self):
		"""Test isnan for integer array - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.isnan(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isnan(self.intarray)


	########################################################
	def test_isnan_b1(self):
		"""Test isnan for maxlen='a' - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.isnan(self.floatarray, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isnan(self.floatarray2, maxlen='a')


	########################################################
	def test_isnan_c1(self):
		"""Test isnan for matherrors=True (unsupported option) - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.isnan(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isnan(self.floatarray2, matherrors=True)


	########################################################
	def test_isnan_d1(self):
		"""Test isnan for missing array - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isnan()


	########################################################
	def test_isnan_d2(self):
		"""Test isnan for missing array with maxlen - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isnan(maxlen=self.testmaxlen)


	########################################################
	def test_isnan_no_params_d3(self):
		"""Test isnan with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isnan()


##############################################################################



##############################################################################
class isnan_nan_d(unittest.TestCase):
	"""Test for correct results for each of the non-finite data conditions.
	nan_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]

		datanan = [float('nan')]
		datainf = [float('inf')]
		dataninf = [float('-inf')]


		self.cleandata = array.array('d', xdata + xdata)
		self.testdatacentre = array.array('d', xdata + datanan + xdata)
		self.testdatastart = array.array('d', datanan + xdata + xdata)
		self.testdataend = array.array('d', xdata + xdata + datanan)


	########################################################
	def test_isnan_a1(self):
		"""Test isnan no value to find - Array code d.
		"""
		result = arrayfunc.isnan(self.cleandata)

		expected = any([math.isnan(x) for x in self.cleandata])

		# Should not find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isnan_a2(self):
		"""Test isnan value to find in centre - Array code d.
		"""
		result = arrayfunc.isnan(self.testdatacentre)

		expected = any([math.isnan(x) for x in self.testdatacentre])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isnan_a3(self):
		"""Test isnan value to find at start - Array code d.
		"""
		result = arrayfunc.isnan(self.testdatastart)

		expected = any([math.isnan(x) for x in self.testdatastart])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isnan_a4(self):
		"""Test isnan value to find at end - Array code d.
		"""
		result = arrayfunc.isnan(self.testdataend)

		expected = any([math.isnan(x) for x in self.testdataend])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isnan_b1(self):
		"""Test isnan value to find beyond limit parameter - Array code d.
		"""
		result = arrayfunc.isnan(self.testdataend, maxlen=len(self.testdataend) - 1)

		expected = any([math.isnan(x) for x in self.testdataend[:len(self.testdataend) - 1]])

		# Should find the value.
		self.assertEqual(result, expected)


##############################################################################


##############################################################################
if __name__ == '__main__':

	# Check to see if the log file option has been selected. This is an option
	# which we have added in order to decide where to output the results.
	if '-l' in sys.argv:
		# Remove the option from the argument list so that "unittest" does 
		# not complain about unknown options.
		sys.argv.remove('-l')

		with open('arrayfunc_unittest.txt', 'a') as f:
			f.write('\n\n')
			f.write('isnan\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
