#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_isfinite.py
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
"""This conducts unit tests for isfinite.
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
class isfinite_general_inf_f(unittest.TestCase):
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

		self.data = array.array('f', xdata + datainf + xdata)

		self.expected = all([math.isfinite(x) for x in self.data])

		self.limited = len(self.data) // 2

		limresults = [math.isfinite(x) for x in self.data]
		self.expectedlim = all(limresults[:self.limited])


	########################################################
	def test_isfinite_a1(self):
		"""Test isfinite basic - Array code f.
		"""
		result = arrayfunc.isfinite(self.data)

		self.assertEqual(result, self.expected)


	########################################################
	def test_isfinite_a2(self):
		"""Test isfinite basic for return type - Array code f.
		"""
		result = arrayfunc.isfinite(self.data)

		self.assertIsInstance(result, bool)


	########################################################
	def test_isfinite_b1(self):
		"""Test isfinite with array limit  - Array code f.
		"""
		result = arrayfunc.isfinite(self.data, maxlen=self.limited)

		self.assertEqual(result, self.expectedlim)



##############################################################################



##############################################################################
class isfinite_param_errors_inf_f(unittest.TestCase):
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

		self.floatarray = array.array('f', xdata + datainf)
		self.floatarray2 = copy.copy(self.floatarray)

		self.testmaxlen = len(self.floatarray) // 2

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in xdata + xdata])


	########################################################
	def test_isfinite_a1(self):
		"""Test isfinite for integer array - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.isfinite(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(self.intarray)


	########################################################
	def test_isfinite_b1(self):
		"""Test isfinite for maxlen='a' - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.isfinite(self.floatarray, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(self.floatarray2, maxlen='a')


	########################################################
	def test_isfinite_c1(self):
		"""Test isfinite for matherrors=True (unsupported option) - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.isfinite(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(self.floatarray2, matherrors=True)


	########################################################
	def test_isfinite_d1(self):
		"""Test isfinite for missing array - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite()


	########################################################
	def test_isfinite_d2(self):
		"""Test isfinite for missing array with maxlen - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(maxlen=self.testmaxlen)


	########################################################
	def test_isfinite_no_params_d3(self):
		"""Test isfinite with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite()


##############################################################################



##############################################################################
class isfinite_inf_f(unittest.TestCase):
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
		self.testdatacentre = array.array('f', xdata + datainf + xdata)
		self.testdatastart = array.array('f', datainf + xdata + xdata)
		self.testdataend = array.array('f', xdata + xdata + datainf)


	########################################################
	def test_isfinite_a1(self):
		"""Test isfinite no value to find - Array code f.
		"""
		result = arrayfunc.isfinite(self.cleandata)

		expected = all([math.isfinite(x) for x in self.cleandata])

		# Should not find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_a2(self):
		"""Test isfinite value to find in centre - Array code f.
		"""
		result = arrayfunc.isfinite(self.testdatacentre)

		expected = all([math.isfinite(x) for x in self.testdatacentre])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_a3(self):
		"""Test isfinite value to find at start - Array code f.
		"""
		result = arrayfunc.isfinite(self.testdatastart)

		expected = all([math.isfinite(x) for x in self.testdatastart])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_a4(self):
		"""Test isfinite value to find at end - Array code f.
		"""
		result = arrayfunc.isfinite(self.testdataend)

		expected = all([math.isfinite(x) for x in self.testdataend])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_b1(self):
		"""Test isfinite value to find beyond limit parameter - Array code f.
		"""
		result = arrayfunc.isfinite(self.testdataend, maxlen=len(self.testdataend) - 1)

		expected = all([math.isfinite(x) for x in self.testdataend[:len(self.testdataend) - 1]])

		# Should find the value.
		self.assertEqual(result, expected)


##############################################################################



##############################################################################
class isfinite_general_ninf_f(unittest.TestCase):
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

		self.data = array.array('f', xdata + dataninf + xdata)

		self.expected = all([math.isfinite(x) for x in self.data])

		self.limited = len(self.data) // 2

		limresults = [math.isfinite(x) for x in self.data]
		self.expectedlim = all(limresults[:self.limited])


	########################################################
	def test_isfinite_a1(self):
		"""Test isfinite basic - Array code f.
		"""
		result = arrayfunc.isfinite(self.data)

		self.assertEqual(result, self.expected)


	########################################################
	def test_isfinite_a2(self):
		"""Test isfinite basic for return type - Array code f.
		"""
		result = arrayfunc.isfinite(self.data)

		self.assertIsInstance(result, bool)


	########################################################
	def test_isfinite_b1(self):
		"""Test isfinite with array limit  - Array code f.
		"""
		result = arrayfunc.isfinite(self.data, maxlen=self.limited)

		self.assertEqual(result, self.expectedlim)



##############################################################################



##############################################################################
class isfinite_param_errors_ninf_f(unittest.TestCase):
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

		self.floatarray = array.array('f', xdata + dataninf)
		self.floatarray2 = copy.copy(self.floatarray)

		self.testmaxlen = len(self.floatarray) // 2

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in xdata + xdata])


	########################################################
	def test_isfinite_a1(self):
		"""Test isfinite for integer array - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.isfinite(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(self.intarray)


	########################################################
	def test_isfinite_b1(self):
		"""Test isfinite for maxlen='a' - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.isfinite(self.floatarray, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(self.floatarray2, maxlen='a')


	########################################################
	def test_isfinite_c1(self):
		"""Test isfinite for matherrors=True (unsupported option) - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.isfinite(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(self.floatarray2, matherrors=True)


	########################################################
	def test_isfinite_d1(self):
		"""Test isfinite for missing array - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite()


	########################################################
	def test_isfinite_d2(self):
		"""Test isfinite for missing array with maxlen - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(maxlen=self.testmaxlen)


	########################################################
	def test_isfinite_no_params_d3(self):
		"""Test isfinite with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite()


##############################################################################



##############################################################################
class isfinite_ninf_f(unittest.TestCase):
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
		self.testdatacentre = array.array('f', xdata + dataninf + xdata)
		self.testdatastart = array.array('f', dataninf + xdata + xdata)
		self.testdataend = array.array('f', xdata + xdata + dataninf)


	########################################################
	def test_isfinite_a1(self):
		"""Test isfinite no value to find - Array code f.
		"""
		result = arrayfunc.isfinite(self.cleandata)

		expected = all([math.isfinite(x) for x in self.cleandata])

		# Should not find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_a2(self):
		"""Test isfinite value to find in centre - Array code f.
		"""
		result = arrayfunc.isfinite(self.testdatacentre)

		expected = all([math.isfinite(x) for x in self.testdatacentre])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_a3(self):
		"""Test isfinite value to find at start - Array code f.
		"""
		result = arrayfunc.isfinite(self.testdatastart)

		expected = all([math.isfinite(x) for x in self.testdatastart])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_a4(self):
		"""Test isfinite value to find at end - Array code f.
		"""
		result = arrayfunc.isfinite(self.testdataend)

		expected = all([math.isfinite(x) for x in self.testdataend])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_b1(self):
		"""Test isfinite value to find beyond limit parameter - Array code f.
		"""
		result = arrayfunc.isfinite(self.testdataend, maxlen=len(self.testdataend) - 1)

		expected = all([math.isfinite(x) for x in self.testdataend[:len(self.testdataend) - 1]])

		# Should find the value.
		self.assertEqual(result, expected)


##############################################################################



##############################################################################
class isfinite_general_nan_f(unittest.TestCase):
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

		self.expected = all([math.isfinite(x) for x in self.data])

		self.limited = len(self.data) // 2

		limresults = [math.isfinite(x) for x in self.data]
		self.expectedlim = all(limresults[:self.limited])


	########################################################
	def test_isfinite_a1(self):
		"""Test isfinite basic - Array code f.
		"""
		result = arrayfunc.isfinite(self.data)

		self.assertEqual(result, self.expected)


	########################################################
	def test_isfinite_a2(self):
		"""Test isfinite basic for return type - Array code f.
		"""
		result = arrayfunc.isfinite(self.data)

		self.assertIsInstance(result, bool)


	########################################################
	def test_isfinite_b1(self):
		"""Test isfinite with array limit  - Array code f.
		"""
		result = arrayfunc.isfinite(self.data, maxlen=self.limited)

		self.assertEqual(result, self.expectedlim)



##############################################################################



##############################################################################
class isfinite_param_errors_nan_f(unittest.TestCase):
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
	def test_isfinite_a1(self):
		"""Test isfinite for integer array - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.isfinite(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(self.intarray)


	########################################################
	def test_isfinite_b1(self):
		"""Test isfinite for maxlen='a' - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.isfinite(self.floatarray, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(self.floatarray2, maxlen='a')


	########################################################
	def test_isfinite_c1(self):
		"""Test isfinite for matherrors=True (unsupported option) - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.isfinite(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(self.floatarray2, matherrors=True)


	########################################################
	def test_isfinite_d1(self):
		"""Test isfinite for missing array - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite()


	########################################################
	def test_isfinite_d2(self):
		"""Test isfinite for missing array with maxlen - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(maxlen=self.testmaxlen)


	########################################################
	def test_isfinite_no_params_d3(self):
		"""Test isfinite with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite()


##############################################################################



##############################################################################
class isfinite_nan_f(unittest.TestCase):
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
	def test_isfinite_a1(self):
		"""Test isfinite no value to find - Array code f.
		"""
		result = arrayfunc.isfinite(self.cleandata)

		expected = all([math.isfinite(x) for x in self.cleandata])

		# Should not find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_a2(self):
		"""Test isfinite value to find in centre - Array code f.
		"""
		result = arrayfunc.isfinite(self.testdatacentre)

		expected = all([math.isfinite(x) for x in self.testdatacentre])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_a3(self):
		"""Test isfinite value to find at start - Array code f.
		"""
		result = arrayfunc.isfinite(self.testdatastart)

		expected = all([math.isfinite(x) for x in self.testdatastart])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_a4(self):
		"""Test isfinite value to find at end - Array code f.
		"""
		result = arrayfunc.isfinite(self.testdataend)

		expected = all([math.isfinite(x) for x in self.testdataend])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_b1(self):
		"""Test isfinite value to find beyond limit parameter - Array code f.
		"""
		result = arrayfunc.isfinite(self.testdataend, maxlen=len(self.testdataend) - 1)

		expected = all([math.isfinite(x) for x in self.testdataend[:len(self.testdataend) - 1]])

		# Should find the value.
		self.assertEqual(result, expected)


##############################################################################



##############################################################################
class isfinite_general_inf_d(unittest.TestCase):
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

		self.data = array.array('d', xdata + datainf + xdata)

		self.expected = all([math.isfinite(x) for x in self.data])

		self.limited = len(self.data) // 2

		limresults = [math.isfinite(x) for x in self.data]
		self.expectedlim = all(limresults[:self.limited])


	########################################################
	def test_isfinite_a1(self):
		"""Test isfinite basic - Array code d.
		"""
		result = arrayfunc.isfinite(self.data)

		self.assertEqual(result, self.expected)


	########################################################
	def test_isfinite_a2(self):
		"""Test isfinite basic for return type - Array code d.
		"""
		result = arrayfunc.isfinite(self.data)

		self.assertIsInstance(result, bool)


	########################################################
	def test_isfinite_b1(self):
		"""Test isfinite with array limit  - Array code d.
		"""
		result = arrayfunc.isfinite(self.data, maxlen=self.limited)

		self.assertEqual(result, self.expectedlim)



##############################################################################



##############################################################################
class isfinite_param_errors_inf_d(unittest.TestCase):
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

		self.floatarray = array.array('d', xdata + datainf)
		self.floatarray2 = copy.copy(self.floatarray)

		self.testmaxlen = len(self.floatarray) // 2

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in xdata + xdata])


	########################################################
	def test_isfinite_a1(self):
		"""Test isfinite for integer array - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.isfinite(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(self.intarray)


	########################################################
	def test_isfinite_b1(self):
		"""Test isfinite for maxlen='a' - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.isfinite(self.floatarray, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(self.floatarray2, maxlen='a')


	########################################################
	def test_isfinite_c1(self):
		"""Test isfinite for matherrors=True (unsupported option) - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.isfinite(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(self.floatarray2, matherrors=True)


	########################################################
	def test_isfinite_d1(self):
		"""Test isfinite for missing array - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite()


	########################################################
	def test_isfinite_d2(self):
		"""Test isfinite for missing array with maxlen - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(maxlen=self.testmaxlen)


	########################################################
	def test_isfinite_no_params_d3(self):
		"""Test isfinite with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite()


##############################################################################



##############################################################################
class isfinite_inf_d(unittest.TestCase):
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
		self.testdatacentre = array.array('d', xdata + datainf + xdata)
		self.testdatastart = array.array('d', datainf + xdata + xdata)
		self.testdataend = array.array('d', xdata + xdata + datainf)


	########################################################
	def test_isfinite_a1(self):
		"""Test isfinite no value to find - Array code d.
		"""
		result = arrayfunc.isfinite(self.cleandata)

		expected = all([math.isfinite(x) for x in self.cleandata])

		# Should not find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_a2(self):
		"""Test isfinite value to find in centre - Array code d.
		"""
		result = arrayfunc.isfinite(self.testdatacentre)

		expected = all([math.isfinite(x) for x in self.testdatacentre])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_a3(self):
		"""Test isfinite value to find at start - Array code d.
		"""
		result = arrayfunc.isfinite(self.testdatastart)

		expected = all([math.isfinite(x) for x in self.testdatastart])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_a4(self):
		"""Test isfinite value to find at end - Array code d.
		"""
		result = arrayfunc.isfinite(self.testdataend)

		expected = all([math.isfinite(x) for x in self.testdataend])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_b1(self):
		"""Test isfinite value to find beyond limit parameter - Array code d.
		"""
		result = arrayfunc.isfinite(self.testdataend, maxlen=len(self.testdataend) - 1)

		expected = all([math.isfinite(x) for x in self.testdataend[:len(self.testdataend) - 1]])

		# Should find the value.
		self.assertEqual(result, expected)


##############################################################################



##############################################################################
class isfinite_general_ninf_d(unittest.TestCase):
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

		self.data = array.array('d', xdata + dataninf + xdata)

		self.expected = all([math.isfinite(x) for x in self.data])

		self.limited = len(self.data) // 2

		limresults = [math.isfinite(x) for x in self.data]
		self.expectedlim = all(limresults[:self.limited])


	########################################################
	def test_isfinite_a1(self):
		"""Test isfinite basic - Array code d.
		"""
		result = arrayfunc.isfinite(self.data)

		self.assertEqual(result, self.expected)


	########################################################
	def test_isfinite_a2(self):
		"""Test isfinite basic for return type - Array code d.
		"""
		result = arrayfunc.isfinite(self.data)

		self.assertIsInstance(result, bool)


	########################################################
	def test_isfinite_b1(self):
		"""Test isfinite with array limit  - Array code d.
		"""
		result = arrayfunc.isfinite(self.data, maxlen=self.limited)

		self.assertEqual(result, self.expectedlim)



##############################################################################



##############################################################################
class isfinite_param_errors_ninf_d(unittest.TestCase):
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

		self.floatarray = array.array('d', xdata + dataninf)
		self.floatarray2 = copy.copy(self.floatarray)

		self.testmaxlen = len(self.floatarray) // 2

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in xdata + xdata])


	########################################################
	def test_isfinite_a1(self):
		"""Test isfinite for integer array - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.isfinite(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(self.intarray)


	########################################################
	def test_isfinite_b1(self):
		"""Test isfinite for maxlen='a' - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.isfinite(self.floatarray, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(self.floatarray2, maxlen='a')


	########################################################
	def test_isfinite_c1(self):
		"""Test isfinite for matherrors=True (unsupported option) - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.isfinite(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(self.floatarray2, matherrors=True)


	########################################################
	def test_isfinite_d1(self):
		"""Test isfinite for missing array - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite()


	########################################################
	def test_isfinite_d2(self):
		"""Test isfinite for missing array with maxlen - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(maxlen=self.testmaxlen)


	########################################################
	def test_isfinite_no_params_d3(self):
		"""Test isfinite with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite()


##############################################################################



##############################################################################
class isfinite_ninf_d(unittest.TestCase):
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
		self.testdatacentre = array.array('d', xdata + dataninf + xdata)
		self.testdatastart = array.array('d', dataninf + xdata + xdata)
		self.testdataend = array.array('d', xdata + xdata + dataninf)


	########################################################
	def test_isfinite_a1(self):
		"""Test isfinite no value to find - Array code d.
		"""
		result = arrayfunc.isfinite(self.cleandata)

		expected = all([math.isfinite(x) for x in self.cleandata])

		# Should not find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_a2(self):
		"""Test isfinite value to find in centre - Array code d.
		"""
		result = arrayfunc.isfinite(self.testdatacentre)

		expected = all([math.isfinite(x) for x in self.testdatacentre])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_a3(self):
		"""Test isfinite value to find at start - Array code d.
		"""
		result = arrayfunc.isfinite(self.testdatastart)

		expected = all([math.isfinite(x) for x in self.testdatastart])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_a4(self):
		"""Test isfinite value to find at end - Array code d.
		"""
		result = arrayfunc.isfinite(self.testdataend)

		expected = all([math.isfinite(x) for x in self.testdataend])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_b1(self):
		"""Test isfinite value to find beyond limit parameter - Array code d.
		"""
		result = arrayfunc.isfinite(self.testdataend, maxlen=len(self.testdataend) - 1)

		expected = all([math.isfinite(x) for x in self.testdataend[:len(self.testdataend) - 1]])

		# Should find the value.
		self.assertEqual(result, expected)


##############################################################################



##############################################################################
class isfinite_general_nan_d(unittest.TestCase):
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

		self.expected = all([math.isfinite(x) for x in self.data])

		self.limited = len(self.data) // 2

		limresults = [math.isfinite(x) for x in self.data]
		self.expectedlim = all(limresults[:self.limited])


	########################################################
	def test_isfinite_a1(self):
		"""Test isfinite basic - Array code d.
		"""
		result = arrayfunc.isfinite(self.data)

		self.assertEqual(result, self.expected)


	########################################################
	def test_isfinite_a2(self):
		"""Test isfinite basic for return type - Array code d.
		"""
		result = arrayfunc.isfinite(self.data)

		self.assertIsInstance(result, bool)


	########################################################
	def test_isfinite_b1(self):
		"""Test isfinite with array limit  - Array code d.
		"""
		result = arrayfunc.isfinite(self.data, maxlen=self.limited)

		self.assertEqual(result, self.expectedlim)



##############################################################################



##############################################################################
class isfinite_param_errors_nan_d(unittest.TestCase):
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
	def test_isfinite_a1(self):
		"""Test isfinite for integer array - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.isfinite(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(self.intarray)


	########################################################
	def test_isfinite_b1(self):
		"""Test isfinite for maxlen='a' - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.isfinite(self.floatarray, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(self.floatarray2, maxlen='a')


	########################################################
	def test_isfinite_c1(self):
		"""Test isfinite for matherrors=True (unsupported option) - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.isfinite(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(self.floatarray2, matherrors=True)


	########################################################
	def test_isfinite_d1(self):
		"""Test isfinite for missing array - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite()


	########################################################
	def test_isfinite_d2(self):
		"""Test isfinite for missing array with maxlen - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite(maxlen=self.testmaxlen)


	########################################################
	def test_isfinite_no_params_d3(self):
		"""Test isfinite with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isfinite()


##############################################################################



##############################################################################
class isfinite_nan_d(unittest.TestCase):
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
	def test_isfinite_a1(self):
		"""Test isfinite no value to find - Array code d.
		"""
		result = arrayfunc.isfinite(self.cleandata)

		expected = all([math.isfinite(x) for x in self.cleandata])

		# Should not find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_a2(self):
		"""Test isfinite value to find in centre - Array code d.
		"""
		result = arrayfunc.isfinite(self.testdatacentre)

		expected = all([math.isfinite(x) for x in self.testdatacentre])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_a3(self):
		"""Test isfinite value to find at start - Array code d.
		"""
		result = arrayfunc.isfinite(self.testdatastart)

		expected = all([math.isfinite(x) for x in self.testdatastart])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_a4(self):
		"""Test isfinite value to find at end - Array code d.
		"""
		result = arrayfunc.isfinite(self.testdataend)

		expected = all([math.isfinite(x) for x in self.testdataend])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isfinite_b1(self):
		"""Test isfinite value to find beyond limit parameter - Array code d.
		"""
		result = arrayfunc.isfinite(self.testdataend, maxlen=len(self.testdataend) - 1)

		expected = all([math.isfinite(x) for x in self.testdataend[:len(self.testdataend) - 1]])

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
			f.write('isfinite\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
