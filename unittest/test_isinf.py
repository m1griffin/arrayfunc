#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_isinf.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     09-Dec-2017.
# Ver:      06-Jul-2019.
#
###############################################################################
#
#   Copyright 2014 - 2019    Michael Griffin    <m12.griffin@gmail.com>
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
"""This conducts unit tests for isinf.
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
class isinf_general_inf_f(unittest.TestCase):
	"""Test for basic general function operation.
	test_template_nonfinite
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]

		datanan = [math.nan]
		datainf = [math.inf]
		dataninf = [-math.inf]

		self.data = array.array('f', xdata + datainf + xdata)

		self.expected = any([math.isinf(x) for x in self.data])

		self.limited = len(self.data) // 2

		limresults = [math.isinf(x) for x in self.data]
		self.expectedlim = any(limresults[:self.limited])


	########################################################
	def test_isinf_a1(self):
		"""Test isinf basic - Array code f.
		"""
		result = arrayfunc.isinf(self.data)

		self.assertEqual(result, self.expected)


	########################################################
	def test_isinf_a2(self):
		"""Test isinf basic for return type - Array code f.
		"""
		result = arrayfunc.isinf(self.data)

		self.assertIsInstance(result, bool)


	########################################################
	def test_isinf_b1(self):
		"""Test isinf with array maxlen  - Array code f.
		"""
		result = arrayfunc.isinf(self.data, maxlen=self.limited)

		self.assertEqual(result, self.expectedlim)



##############################################################################



##############################################################################
class isinf_param_errors_inf_f(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]

		datanan = [math.nan] * len(xdata)
		datainf = [math.inf] * len(xdata)
		dataninf = [-math.inf] * len(xdata)

		self.floatarray = array.array('f', xdata + datainf)
		self.floatarray2 = copy.copy(self.floatarray)

		self.testmaxlen = len(self.floatarray) // 2

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in xdata + xdata])


	########################################################
	def test_isinf_a1(self):
		"""Test isinf for integer array - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.isinf(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf(self.intarray)


	########################################################
	def test_isinf_b1(self):
		"""Test isinf for maxlen='a' - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.isinf(self.floatarray, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf(self.floatarray2, maxlen='a')


	########################################################
	def test_isinf_c1(self):
		"""Test isinf for matherrors=True (unsupported option) - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.isinf(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf(self.floatarray2, matherrors=True)


	########################################################
	def test_isinf_d1(self):
		"""Test isinf for missing array - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf()


	########################################################
	def test_isinf_d2(self):
		"""Test isinf for missing array with maxlen - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf(maxlen=self.testmaxlen)


	########################################################
	def test_isinf_no_params_d3(self):
		"""Test isinf with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf()


##############################################################################



##############################################################################
class isinf_inf_f(unittest.TestCase):
	"""Test for correct results for each of the non-finite data conditions.
	nan_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]

		datanan = [math.nan]
		datainf = [math.inf]
		dataninf = [-math.inf]


		self.cleandata = array.array('f', xdata + xdata)
		self.testdatacentre = array.array('f', xdata + datainf + xdata)
		self.testdatastart = array.array('f', datainf + xdata + xdata)
		self.testdataend = array.array('f', xdata + xdata + datainf)


	########################################################
	def test_isinf_a1(self):
		"""Test isinf no value to find - Array code f.
		"""
		result = arrayfunc.isinf(self.cleandata)

		expected = any([math.isinf(x) for x in self.cleandata])

		# Should not find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isinf_a2(self):
		"""Test isinf value to find in centre - Array code f.
		"""
		result = arrayfunc.isinf(self.testdatacentre)

		expected = any([math.isinf(x) for x in self.testdatacentre])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isinf_a3(self):
		"""Test isinf value to find at start - Array code f.
		"""
		result = arrayfunc.isinf(self.testdatastart)

		expected = any([math.isinf(x) for x in self.testdatastart])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isinf_a4(self):
		"""Test isinf value to find at end - Array code f.
		"""
		result = arrayfunc.isinf(self.testdataend)

		expected = any([math.isinf(x) for x in self.testdataend])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isinf_b1(self):
		"""Test isinf value to find beyond maxlen parameter - Array code f.
		"""
		result = arrayfunc.isinf(self.testdataend, maxlen=len(self.testdataend) - 1)

		expected = any([math.isinf(x) for x in self.testdataend[:len(self.testdataend) - 1]])

		# Should find the value.
		self.assertEqual(result, expected)


##############################################################################



##############################################################################
class isinf_general_ninf_f(unittest.TestCase):
	"""Test for basic general function operation.
	test_template_nonfinite
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]

		datanan = [math.nan]
		datainf = [math.inf]
		dataninf = [-math.inf]

		self.data = array.array('f', xdata + dataninf + xdata)

		self.expected = any([math.isinf(x) for x in self.data])

		self.limited = len(self.data) // 2

		limresults = [math.isinf(x) for x in self.data]
		self.expectedlim = any(limresults[:self.limited])


	########################################################
	def test_isinf_a1(self):
		"""Test isinf basic - Array code f.
		"""
		result = arrayfunc.isinf(self.data)

		self.assertEqual(result, self.expected)


	########################################################
	def test_isinf_a2(self):
		"""Test isinf basic for return type - Array code f.
		"""
		result = arrayfunc.isinf(self.data)

		self.assertIsInstance(result, bool)


	########################################################
	def test_isinf_b1(self):
		"""Test isinf with array maxlen  - Array code f.
		"""
		result = arrayfunc.isinf(self.data, maxlen=self.limited)

		self.assertEqual(result, self.expectedlim)



##############################################################################



##############################################################################
class isinf_param_errors_ninf_f(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]

		datanan = [math.nan] * len(xdata)
		datainf = [math.inf] * len(xdata)
		dataninf = [-math.inf] * len(xdata)

		self.floatarray = array.array('f', xdata + dataninf)
		self.floatarray2 = copy.copy(self.floatarray)

		self.testmaxlen = len(self.floatarray) // 2

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in xdata + xdata])


	########################################################
	def test_isinf_a1(self):
		"""Test isinf for integer array - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.isinf(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf(self.intarray)


	########################################################
	def test_isinf_b1(self):
		"""Test isinf for maxlen='a' - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.isinf(self.floatarray, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf(self.floatarray2, maxlen='a')


	########################################################
	def test_isinf_c1(self):
		"""Test isinf for matherrors=True (unsupported option) - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.isinf(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf(self.floatarray2, matherrors=True)


	########################################################
	def test_isinf_d1(self):
		"""Test isinf for missing array - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf()


	########################################################
	def test_isinf_d2(self):
		"""Test isinf for missing array with maxlen - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf(maxlen=self.testmaxlen)


	########################################################
	def test_isinf_no_params_d3(self):
		"""Test isinf with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf()


##############################################################################



##############################################################################
class isinf_ninf_f(unittest.TestCase):
	"""Test for correct results for each of the non-finite data conditions.
	nan_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]

		datanan = [math.nan]
		datainf = [math.inf]
		dataninf = [-math.inf]


		self.cleandata = array.array('f', xdata + xdata)
		self.testdatacentre = array.array('f', xdata + dataninf + xdata)
		self.testdatastart = array.array('f', dataninf + xdata + xdata)
		self.testdataend = array.array('f', xdata + xdata + dataninf)


	########################################################
	def test_isinf_a1(self):
		"""Test isinf no value to find - Array code f.
		"""
		result = arrayfunc.isinf(self.cleandata)

		expected = any([math.isinf(x) for x in self.cleandata])

		# Should not find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isinf_a2(self):
		"""Test isinf value to find in centre - Array code f.
		"""
		result = arrayfunc.isinf(self.testdatacentre)

		expected = any([math.isinf(x) for x in self.testdatacentre])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isinf_a3(self):
		"""Test isinf value to find at start - Array code f.
		"""
		result = arrayfunc.isinf(self.testdatastart)

		expected = any([math.isinf(x) for x in self.testdatastart])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isinf_a4(self):
		"""Test isinf value to find at end - Array code f.
		"""
		result = arrayfunc.isinf(self.testdataend)

		expected = any([math.isinf(x) for x in self.testdataend])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isinf_b1(self):
		"""Test isinf value to find beyond maxlen parameter - Array code f.
		"""
		result = arrayfunc.isinf(self.testdataend, maxlen=len(self.testdataend) - 1)

		expected = any([math.isinf(x) for x in self.testdataend[:len(self.testdataend) - 1]])

		# Should find the value.
		self.assertEqual(result, expected)


##############################################################################



##############################################################################
class isinf_general_inf_d(unittest.TestCase):
	"""Test for basic general function operation.
	test_template_nonfinite
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]

		datanan = [math.nan]
		datainf = [math.inf]
		dataninf = [-math.inf]

		self.data = array.array('d', xdata + datainf + xdata)

		self.expected = any([math.isinf(x) for x in self.data])

		self.limited = len(self.data) // 2

		limresults = [math.isinf(x) for x in self.data]
		self.expectedlim = any(limresults[:self.limited])


	########################################################
	def test_isinf_a1(self):
		"""Test isinf basic - Array code d.
		"""
		result = arrayfunc.isinf(self.data)

		self.assertEqual(result, self.expected)


	########################################################
	def test_isinf_a2(self):
		"""Test isinf basic for return type - Array code d.
		"""
		result = arrayfunc.isinf(self.data)

		self.assertIsInstance(result, bool)


	########################################################
	def test_isinf_b1(self):
		"""Test isinf with array maxlen  - Array code d.
		"""
		result = arrayfunc.isinf(self.data, maxlen=self.limited)

		self.assertEqual(result, self.expectedlim)



##############################################################################



##############################################################################
class isinf_param_errors_inf_d(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]

		datanan = [math.nan] * len(xdata)
		datainf = [math.inf] * len(xdata)
		dataninf = [-math.inf] * len(xdata)

		self.floatarray = array.array('d', xdata + datainf)
		self.floatarray2 = copy.copy(self.floatarray)

		self.testmaxlen = len(self.floatarray) // 2

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in xdata + xdata])


	########################################################
	def test_isinf_a1(self):
		"""Test isinf for integer array - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.isinf(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf(self.intarray)


	########################################################
	def test_isinf_b1(self):
		"""Test isinf for maxlen='a' - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.isinf(self.floatarray, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf(self.floatarray2, maxlen='a')


	########################################################
	def test_isinf_c1(self):
		"""Test isinf for matherrors=True (unsupported option) - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.isinf(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf(self.floatarray2, matherrors=True)


	########################################################
	def test_isinf_d1(self):
		"""Test isinf for missing array - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf()


	########################################################
	def test_isinf_d2(self):
		"""Test isinf for missing array with maxlen - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf(maxlen=self.testmaxlen)


	########################################################
	def test_isinf_no_params_d3(self):
		"""Test isinf with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf()


##############################################################################



##############################################################################
class isinf_inf_d(unittest.TestCase):
	"""Test for correct results for each of the non-finite data conditions.
	nan_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]

		datanan = [math.nan]
		datainf = [math.inf]
		dataninf = [-math.inf]


		self.cleandata = array.array('d', xdata + xdata)
		self.testdatacentre = array.array('d', xdata + datainf + xdata)
		self.testdatastart = array.array('d', datainf + xdata + xdata)
		self.testdataend = array.array('d', xdata + xdata + datainf)


	########################################################
	def test_isinf_a1(self):
		"""Test isinf no value to find - Array code d.
		"""
		result = arrayfunc.isinf(self.cleandata)

		expected = any([math.isinf(x) for x in self.cleandata])

		# Should not find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isinf_a2(self):
		"""Test isinf value to find in centre - Array code d.
		"""
		result = arrayfunc.isinf(self.testdatacentre)

		expected = any([math.isinf(x) for x in self.testdatacentre])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isinf_a3(self):
		"""Test isinf value to find at start - Array code d.
		"""
		result = arrayfunc.isinf(self.testdatastart)

		expected = any([math.isinf(x) for x in self.testdatastart])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isinf_a4(self):
		"""Test isinf value to find at end - Array code d.
		"""
		result = arrayfunc.isinf(self.testdataend)

		expected = any([math.isinf(x) for x in self.testdataend])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isinf_b1(self):
		"""Test isinf value to find beyond maxlen parameter - Array code d.
		"""
		result = arrayfunc.isinf(self.testdataend, maxlen=len(self.testdataend) - 1)

		expected = any([math.isinf(x) for x in self.testdataend[:len(self.testdataend) - 1]])

		# Should find the value.
		self.assertEqual(result, expected)


##############################################################################



##############################################################################
class isinf_general_ninf_d(unittest.TestCase):
	"""Test for basic general function operation.
	test_template_nonfinite
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]

		datanan = [math.nan]
		datainf = [math.inf]
		dataninf = [-math.inf]

		self.data = array.array('d', xdata + dataninf + xdata)

		self.expected = any([math.isinf(x) for x in self.data])

		self.limited = len(self.data) // 2

		limresults = [math.isinf(x) for x in self.data]
		self.expectedlim = any(limresults[:self.limited])


	########################################################
	def test_isinf_a1(self):
		"""Test isinf basic - Array code d.
		"""
		result = arrayfunc.isinf(self.data)

		self.assertEqual(result, self.expected)


	########################################################
	def test_isinf_a2(self):
		"""Test isinf basic for return type - Array code d.
		"""
		result = arrayfunc.isinf(self.data)

		self.assertIsInstance(result, bool)


	########################################################
	def test_isinf_b1(self):
		"""Test isinf with array maxlen  - Array code d.
		"""
		result = arrayfunc.isinf(self.data, maxlen=self.limited)

		self.assertEqual(result, self.expectedlim)



##############################################################################



##############################################################################
class isinf_param_errors_ninf_d(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]

		datanan = [math.nan] * len(xdata)
		datainf = [math.inf] * len(xdata)
		dataninf = [-math.inf] * len(xdata)

		self.floatarray = array.array('d', xdata + dataninf)
		self.floatarray2 = copy.copy(self.floatarray)

		self.testmaxlen = len(self.floatarray) // 2

		# Create some integer array equivalents.
		self.intarray = array.array('i', [int(x) for x in xdata + xdata])


	########################################################
	def test_isinf_a1(self):
		"""Test isinf for integer array - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.isinf(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf(self.intarray)


	########################################################
	def test_isinf_b1(self):
		"""Test isinf for maxlen='a' - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.isinf(self.floatarray, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf(self.floatarray2, maxlen='a')


	########################################################
	def test_isinf_c1(self):
		"""Test isinf for matherrors=True (unsupported option) - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.isinf(self.floatarray)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf(self.floatarray2, matherrors=True)


	########################################################
	def test_isinf_d1(self):
		"""Test isinf for missing array - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf()


	########################################################
	def test_isinf_d2(self):
		"""Test isinf for missing array with maxlen - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf(maxlen=self.testmaxlen)


	########################################################
	def test_isinf_no_params_d3(self):
		"""Test isinf with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.isinf()


##############################################################################



##############################################################################
class isinf_ninf_d(unittest.TestCase):
	"""Test for correct results for each of the non-finite data conditions.
	nan_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		xdata = [-5.0,-1.0,0.0,0.4,0.8,1.2,1.6,2.0,2.4,2.8,3.2,3.6]

		datanan = [math.nan]
		datainf = [math.inf]
		dataninf = [-math.inf]


		self.cleandata = array.array('d', xdata + xdata)
		self.testdatacentre = array.array('d', xdata + dataninf + xdata)
		self.testdatastart = array.array('d', dataninf + xdata + xdata)
		self.testdataend = array.array('d', xdata + xdata + dataninf)


	########################################################
	def test_isinf_a1(self):
		"""Test isinf no value to find - Array code d.
		"""
		result = arrayfunc.isinf(self.cleandata)

		expected = any([math.isinf(x) for x in self.cleandata])

		# Should not find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isinf_a2(self):
		"""Test isinf value to find in centre - Array code d.
		"""
		result = arrayfunc.isinf(self.testdatacentre)

		expected = any([math.isinf(x) for x in self.testdatacentre])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isinf_a3(self):
		"""Test isinf value to find at start - Array code d.
		"""
		result = arrayfunc.isinf(self.testdatastart)

		expected = any([math.isinf(x) for x in self.testdatastart])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isinf_a4(self):
		"""Test isinf value to find at end - Array code d.
		"""
		result = arrayfunc.isinf(self.testdataend)

		expected = any([math.isinf(x) for x in self.testdataend])

		# Should find the value.
		self.assertEqual(result, expected)


	########################################################
	def test_isinf_b1(self):
		"""Test isinf value to find beyond maxlen parameter - Array code d.
		"""
		result = arrayfunc.isinf(self.testdataend, maxlen=len(self.testdataend) - 1)

		expected = any([math.isinf(x) for x in self.testdataend[:len(self.testdataend) - 1]])

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
			f.write('isinf\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
