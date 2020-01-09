#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_ne.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     14-Feb-2018.
# Ver:      02-Jan-2020.
#
###############################################################################
#
#   Copyright 2014 - 2020    Michael Griffin    <m12.griffin@gmail.com>
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
"""This conducts unit tests for ne.
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
class ne_general_even_arraysize_nosimd_simd_b_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'b' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'b' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.b_min
			maxval = arrayfunc.arraylimits.b_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'b' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('b', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('b', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('b', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('b', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('b', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code b.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code b.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_b_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'b' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'b' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.b_min
			maxval = arrayfunc.arraylimits.b_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'b' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('b', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('b', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('b', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('b', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('b', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code b.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code b.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_b_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'b' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'b' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.b_min
			maxval = arrayfunc.arraylimits.b_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'b' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('b', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('b', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('b', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('b', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('b', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code b.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code b.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_b_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'b' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'b' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.b_min
			maxval = arrayfunc.arraylimits.b_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'b' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('b', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('b', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('b', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('b', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('b', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code b.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code b.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_b_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'b' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'b' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.b_min
			maxval = arrayfunc.arraylimits.b_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'b' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('b', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('b', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('b', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('b', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('b', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code b.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code b.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_b_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'b' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'b' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.b_min
			maxval = arrayfunc.arraylimits.b_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'b' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('b', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('b', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('b', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('b', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('b', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code b.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code b.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_b_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'b' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'b' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.b_min
			maxval = arrayfunc.arraylimits.b_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'b' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('b', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('b', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('b', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('b', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('b', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code b.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code b.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_b_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'b' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'b' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.b_min
			maxval = arrayfunc.arraylimits.b_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'b' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('b', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('b', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('b', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('b', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('b', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code b.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code b.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_B_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'B' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'B' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.B_min
			maxval = arrayfunc.arraylimits.B_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'B' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('B', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('B', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('B', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('B', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('B', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code B.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code B.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_B_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'B' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'B' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.B_min
			maxval = arrayfunc.arraylimits.B_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'B' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('B', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('B', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('B', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('B', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('B', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code B.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code B.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_B_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'B' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'B' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.B_min
			maxval = arrayfunc.arraylimits.B_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'B' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('B', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('B', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('B', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('B', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('B', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code B.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code B.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_B_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'B' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'B' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.B_min
			maxval = arrayfunc.arraylimits.B_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'B' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('B', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('B', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('B', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('B', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('B', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code B.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code B.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_B_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'B' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'B' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.B_min
			maxval = arrayfunc.arraylimits.B_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'B' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('B', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('B', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('B', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('B', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('B', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code B.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code B.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_B_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'B' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'B' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.B_min
			maxval = arrayfunc.arraylimits.B_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'B' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('B', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('B', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('B', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('B', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('B', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code B.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code B.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_B_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'B' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'B' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.B_min
			maxval = arrayfunc.arraylimits.B_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'B' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('B', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('B', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('B', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('B', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('B', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code B.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code B.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_B_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'B' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'B' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.B_min
			maxval = arrayfunc.arraylimits.B_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'B' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('B', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('B', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('B', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('B', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('B', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code B.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code B.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_h_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'h' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'h' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'h' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('h', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('h', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('h', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('h', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('h', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code h.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code h.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_h_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'h' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'h' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'h' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('h', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('h', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('h', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('h', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('h', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code h.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code h.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_h_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'h' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'h' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'h' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('h', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('h', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('h', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('h', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('h', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code h.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code h.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_h_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'h' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'h' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'h' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('h', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('h', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('h', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('h', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('h', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code h.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code h.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_h_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'h' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'h' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'h' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('h', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('h', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('h', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('h', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('h', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code h.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code h.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_h_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'h' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'h' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'h' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('h', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('h', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('h', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('h', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('h', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code h.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code h.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_h_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'h' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'h' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'h' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('h', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('h', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('h', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('h', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('h', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code h.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code h.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_h_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'h' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'h' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'h' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('h', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('h', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('h', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('h', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('h', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code h.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code h.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_H_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'H' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'H' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.H_min
			maxval = arrayfunc.arraylimits.H_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'H' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('H', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('H', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('H', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('H', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('H', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code H.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code H.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_H_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'H' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'H' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.H_min
			maxval = arrayfunc.arraylimits.H_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'H' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('H', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('H', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('H', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('H', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('H', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code H.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code H.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_H_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'H' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'H' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.H_min
			maxval = arrayfunc.arraylimits.H_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'H' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('H', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('H', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('H', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('H', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('H', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code H.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code H.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_H_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'H' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'H' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.H_min
			maxval = arrayfunc.arraylimits.H_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'H' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('H', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('H', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('H', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('H', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('H', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code H.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code H.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_H_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'H' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'H' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.H_min
			maxval = arrayfunc.arraylimits.H_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'H' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('H', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('H', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('H', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('H', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('H', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code H.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code H.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_H_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'H' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'H' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.H_min
			maxval = arrayfunc.arraylimits.H_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'H' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('H', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('H', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('H', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('H', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('H', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code H.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code H.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_H_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'H' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'H' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.H_min
			maxval = arrayfunc.arraylimits.H_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'H' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('H', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('H', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('H', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('H', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('H', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code H.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code H.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_H_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'H' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'H' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.H_min
			maxval = arrayfunc.arraylimits.H_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'H' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('H', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('H', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('H', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('H', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('H', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code H.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code H.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_i_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'i' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'i' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'i' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('i', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('i', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('i', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('i', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('i', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code i.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code i.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_i_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'i' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'i' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'i' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('i', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('i', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('i', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('i', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('i', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code i.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code i.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_i_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'i' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'i' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'i' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('i', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('i', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('i', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('i', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('i', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code i.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code i.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_i_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'i' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'i' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'i' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('i', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('i', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('i', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('i', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('i', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code i.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code i.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_i_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'i' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'i' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'i' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('i', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('i', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('i', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('i', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('i', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code i.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code i.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_i_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'i' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'i' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'i' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('i', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('i', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('i', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('i', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('i', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code i.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code i.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_i_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'i' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'i' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'i' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('i', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('i', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('i', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('i', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('i', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code i.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code i.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_i_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'i' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'i' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'i' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('i', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('i', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('i', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('i', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('i', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code i.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code i.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_I_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'I' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'I' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.I_min
			maxval = arrayfunc.arraylimits.I_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'I' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('I', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('I', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('I', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('I', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('I', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code I.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code I.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_I_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'I' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'I' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.I_min
			maxval = arrayfunc.arraylimits.I_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'I' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('I', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('I', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('I', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('I', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('I', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code I.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code I.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_I_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'I' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'I' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.I_min
			maxval = arrayfunc.arraylimits.I_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'I' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('I', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('I', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('I', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('I', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('I', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code I.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code I.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_I_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'I' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'I' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.I_min
			maxval = arrayfunc.arraylimits.I_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'I' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('I', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('I', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('I', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('I', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('I', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code I.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code I.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_I_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'I' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'I' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.I_min
			maxval = arrayfunc.arraylimits.I_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'I' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('I', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('I', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('I', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('I', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('I', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code I.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code I.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_I_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'I' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'I' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.I_min
			maxval = arrayfunc.arraylimits.I_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'I' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('I', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('I', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('I', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('I', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('I', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code I.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code I.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_I_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'I' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'I' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.I_min
			maxval = arrayfunc.arraylimits.I_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'I' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('I', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('I', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('I', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('I', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('I', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code I.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code I.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_I_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'I' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'I' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.I_min
			maxval = arrayfunc.arraylimits.I_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'I' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('I', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('I', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('I', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('I', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('I', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code I.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code I.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_l_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'l' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'l' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.l_min
			maxval = arrayfunc.arraylimits.l_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'l' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('l', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('l', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('l', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('l', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('l', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code l.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code l.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_l_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'l' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'l' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.l_min
			maxval = arrayfunc.arraylimits.l_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'l' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('l', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('l', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('l', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('l', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('l', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code l.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code l.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_l_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'l' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'l' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.l_min
			maxval = arrayfunc.arraylimits.l_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'l' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('l', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('l', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('l', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('l', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('l', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code l.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code l.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_l_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'l' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'l' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.l_min
			maxval = arrayfunc.arraylimits.l_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'l' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('l', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('l', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('l', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('l', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('l', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code l.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code l.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_l_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'l' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'l' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.l_min
			maxval = arrayfunc.arraylimits.l_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'l' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('l', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('l', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('l', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('l', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('l', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code l.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code l.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_l_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'l' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'l' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.l_min
			maxval = arrayfunc.arraylimits.l_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'l' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('l', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('l', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('l', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('l', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('l', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code l.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code l.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_l_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'l' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'l' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.l_min
			maxval = arrayfunc.arraylimits.l_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'l' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('l', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('l', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('l', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('l', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('l', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code l.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code l.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_l_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'l' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'l' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.l_min
			maxval = arrayfunc.arraylimits.l_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'l' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('l', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('l', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('l', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('l', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('l', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code l.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code l.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_L_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'L' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'L' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.L_min
			maxval = arrayfunc.arraylimits.L_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'L' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('L', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('L', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('L', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('L', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('L', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code L.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code L.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_L_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'L' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'L' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.L_min
			maxval = arrayfunc.arraylimits.L_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'L' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('L', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('L', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('L', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('L', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('L', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code L.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code L.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_L_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'L' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'L' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.L_min
			maxval = arrayfunc.arraylimits.L_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'L' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('L', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('L', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('L', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('L', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('L', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code L.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code L.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_L_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'L' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'L' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.L_min
			maxval = arrayfunc.arraylimits.L_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'L' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('L', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('L', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('L', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('L', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('L', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code L.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code L.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_L_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'L' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'L' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.L_min
			maxval = arrayfunc.arraylimits.L_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'L' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('L', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('L', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('L', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('L', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('L', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code L.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code L.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_L_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'L' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'L' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.L_min
			maxval = arrayfunc.arraylimits.L_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'L' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('L', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('L', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('L', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('L', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('L', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code L.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code L.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_L_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'L' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'L' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.L_min
			maxval = arrayfunc.arraylimits.L_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'L' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('L', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('L', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('L', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('L', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('L', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code L.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code L.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_L_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'L' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'L' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.L_min
			maxval = arrayfunc.arraylimits.L_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'L' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('L', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('L', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('L', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('L', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('L', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code L.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code L.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_q_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.q_min
			maxval = arrayfunc.arraylimits.q_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'q' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('q', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code q.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_q_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.q_min
			maxval = arrayfunc.arraylimits.q_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'q' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('q', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code q.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_q_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.q_min
			maxval = arrayfunc.arraylimits.q_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'q' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('q', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code q.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_q_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.q_min
			maxval = arrayfunc.arraylimits.q_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'q' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('q', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code q.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_q_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.q_min
			maxval = arrayfunc.arraylimits.q_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'q' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('q', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code q.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_q_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.q_min
			maxval = arrayfunc.arraylimits.q_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'q' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('q', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code q.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_q_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.q_min
			maxval = arrayfunc.arraylimits.q_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'q' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('q', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code q.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_q_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.q_min
			maxval = arrayfunc.arraylimits.q_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'q' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('q', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code q.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_Q_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'Q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'Q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.Q_min
			maxval = arrayfunc.arraylimits.Q_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'Q' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('Q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('Q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('Q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('Q', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('Q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code Q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code Q.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_Q_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'Q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'Q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.Q_min
			maxval = arrayfunc.arraylimits.Q_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'Q' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('Q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('Q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('Q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('Q', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('Q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code Q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code Q.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_Q_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'Q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'Q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.Q_min
			maxval = arrayfunc.arraylimits.Q_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'Q' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('Q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('Q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('Q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('Q', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('Q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code Q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code Q.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_Q_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'Q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'Q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.Q_min
			maxval = arrayfunc.arraylimits.Q_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'Q' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('Q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('Q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('Q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('Q', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('Q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code Q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code Q.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_Q_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'Q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'Q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.Q_min
			maxval = arrayfunc.arraylimits.Q_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'Q' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('Q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('Q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('Q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('Q', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('Q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code Q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code Q.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_Q_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'Q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'Q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.Q_min
			maxval = arrayfunc.arraylimits.Q_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'Q' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('Q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('Q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('Q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('Q', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('Q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code Q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code Q.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_Q_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'Q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'Q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.Q_min
			maxval = arrayfunc.arraylimits.Q_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'Q' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('Q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('Q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('Q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('Q', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('Q', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code Q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code Q.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_Q_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'Q' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'Q' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.Q_min
			maxval = arrayfunc.arraylimits.Q_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'Q' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('Q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('Q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('Q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('Q', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('Q', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code Q.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code Q.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_f_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'f' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'f' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.f_min
			maxval = arrayfunc.arraylimits.f_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'f' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('f', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('f', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('f', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('f', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('f', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code f.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code f.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code f.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_f_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'f' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'f' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.f_min
			maxval = arrayfunc.arraylimits.f_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'f' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('f', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('f', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('f', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('f', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('f', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code f.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code f.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code f.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_f_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'f' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'f' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.f_min
			maxval = arrayfunc.arraylimits.f_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'f' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('f', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('f', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('f', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('f', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('f', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code f.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code f.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code f.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_f_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'f' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'f' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.f_min
			maxval = arrayfunc.arraylimits.f_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'f' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('f', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('f', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('f', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('f', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('f', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code f.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code f.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code f.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_f_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'f' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'f' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.f_min
			maxval = arrayfunc.arraylimits.f_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'f' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('f', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('f', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('f', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('f', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('f', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code f.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code f.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code f.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_f_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'f' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'f' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.f_min
			maxval = arrayfunc.arraylimits.f_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'f' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('f', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('f', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('f', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('f', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('f', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code f.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code f.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code f.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_f_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'f' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'f' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.f_min
			maxval = arrayfunc.arraylimits.f_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'f' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('f', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('f', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('f', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('f', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('f', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code f.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code f.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code f.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_f_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'f' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'f' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.f_min
			maxval = arrayfunc.arraylimits.f_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'f' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('f', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('f', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('f', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('f', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('f', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code f.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code f.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code f.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_d_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'd' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'd' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.d_min
			maxval = arrayfunc.arraylimits.d_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'd' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('d', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('d', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('d', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('d', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('d', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code d.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code d.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code d.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_nosimd_simd_d_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'd' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'd' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.d_min
			maxval = arrayfunc.arraylimits.d_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'd' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('d', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('d', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('d', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('d', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('d', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code d.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code d.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code d.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_d_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'd' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'd' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.d_min
			maxval = arrayfunc.arraylimits.d_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'd' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('d', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('d', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('d', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('d', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('d', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code d.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code d.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code d.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_withsimd_simd_d_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 512
		if 'even' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'd' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'd' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.d_min
			maxval = arrayfunc.arraylimits.d_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'd' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('d', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('d', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('d', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('d', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('d', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code d.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code d.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code d.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_d_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'd' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'd' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.d_min
			maxval = arrayfunc.arraylimits.d_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'd' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('d', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('d', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('d', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('d', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('d', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code d.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code d.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code d.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_nosimd_simd_d_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'd' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'd' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.d_min
			maxval = arrayfunc.arraylimits.d_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'd' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('d', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('d', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('d', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('d', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('d', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code d.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array , nosimd=True)

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code d.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited , nosimd=True)

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail , nosimd=True)

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code d.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited , nosimd=True)

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_d_0(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'd' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'd' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.d_min
			maxval = arrayfunc.arraylimits.d_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'd' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval1, 0, midval3]]
			vals_param_array_num_fail = [float(x) for x in [baseval, baseval, baseval]]
			vals_param_num_array_pass = [float(x) for x in [midval1, midval3, 0]]
			vals_param_num_array_fail = [float(x) for x in [baseval, baseval, baseval]]
		else:
			vals_param_array_num_pass = [midval1, 0, midval3]
			vals_param_array_num_fail = [baseval, baseval, baseval]
			vals_param_num_array_pass = [midval1, midval3, 0]
			vals_param_num_array_fail = [baseval, baseval, baseval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('d', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('d', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('d', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))
		self.data_array_array_pass = array.array('d', list(itertools.islice(itertools.cycle([midval2, midval3, midval1]), testdatasize)))
		self.data_array_array_fail = array.array('d', list(itertools.islice(itertools.cycle([baseval, baseval, baseval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code d.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code d.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code d.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_withsimd_simd_d_1(unittest.TestCase):
	"""Test for basic general function operation using numeric data.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 512
		if 'odd' == 'odd':
			testdatasize = 511

		# The maximum and minimum values used for 'f' and 'd' arrays are 
		# limited here to within their precision so that small changes
		# can be made to the test data when comparing values. 
		# 'f' numbers have only 23 bits of precision and 'd' numbers have only 52 
		# bits of precision, so they are limited here to the next lowest integer value. 
		if 'd' == 'f':
			minval = arrayfunc.arraylimits.h_min
			maxval = arrayfunc.arraylimits.h_max
		elif 'd' == 'd':
			minval = arrayfunc.arraylimits.i_min
			maxval = arrayfunc.arraylimits.i_max
		else:
			minval = arrayfunc.arraylimits.d_min
			maxval = arrayfunc.arraylimits.d_max

		# We create numbers algorithmically in order to spread the 
		# test values over the ranges of different integers.
		# Create values near the bottom and top of the integer range.
		baseval = minval + 10
		topval = maxval - 10
		maxint = maxval

		# Pick something near the middle of the range, but with a bit of
		# an aribitrary offset.
		midval1 = ((maxval + minval) // 2) + 3
		midval2 = ((maxval + minval) // 2) + 5
		midval3 = ((maxval + minval) // 2) + 25


		# The template has to conver integer to floating point parameters. 
		if 'd' in ('f', 'd'):
			vals_param_array_num_pass = [float(x) for x in [midval3, midval2, 0]]
			vals_param_array_num_fail = [float(x) for x in [topval, topval, topval]]
			vals_param_num_array_pass = [float(x) for x in [midval3, midval1, 0]]
			vals_param_num_array_fail = [float(x) for x in [topval, topval, topval]]
		else:
			vals_param_array_num_pass = [midval3, midval2, 0]
			vals_param_array_num_fail = [topval, topval, topval]
			vals_param_num_array_pass = [midval3, midval1, 0]
			vals_param_num_array_fail = [topval, topval, topval]


		# Now create the arrays and lists.
		self.data_array_num = array.array('d', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_array_num_pass = vals_param_array_num_pass
		self.param_array_num_fail = vals_param_array_num_fail

		self.data_num_array = array.array('d', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.param_num_array_pass = vals_param_num_array_pass
		self.param_num_array_fail = vals_param_num_array_fail

		self.data_array_array = array.array('d', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))
		self.data_array_array_pass = array.array('d', list(itertools.islice(itertools.cycle([midval1, 0, midval3]), testdatasize)))
		self.data_array_array_fail = array.array('d', list(itertools.islice(itertools.cycle([topval, topval, topval]), testdatasize)))


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.param_array_num_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data_array_num])

				result = arrayfunc.ne(self.data_array_num, testval )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code d.
		"""
		for testval in self.param_array_num_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_array_num) // 2

				expected = all([x != testval for x in self.data_array_num[0:limited]])

				result = arrayfunc.ne(self.data_array_num, testval, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.param_num_array_fail:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data_num_array])

				result = arrayfunc.ne(testval, self.data_num_array )

				self.assertFalse(expected)
				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code d.
		"""
		for testval in self.param_num_array_pass:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data_num_array) // 2

				expected = all([testval != x for x in self.data_num_array[0:limited]])

				result = arrayfunc.ne(testval, self.data_num_array, maxlen=limited )

				self.assertTrue(expected)
				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_pass)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data_array_array, self.data_array_array_fail)])
		result = arrayfunc.ne(self.data_array_array, self.data_array_array_fail )

		self.assertFalse(expected)
		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code d.
		"""
		limited = len(self.data_array_array) // 2

		expected = all([x != y for (x, y) in zip(self.data_array_array[0:limited], self.data_array_array_pass[0:limited])])

		result = arrayfunc.ne(self.data_array_array, self.data_array_array_pass, maxlen=limited )

		self.assertTrue(expected)
		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 


##############################################################################
class ne_numpos_b(unittest.TestCase):
	"""Test with a single fail value in different array positions.
	test_template_numpos
	"""


	########################################################
	def setUp(self):
		"""Initialise. The test data is generated from the script itself.
		"""
		self.testarraylen = 159

		self.data1 = array.array('b', [5] * self.testarraylen)
		self.testval1 = self.data1[0]
		self.data1fail = array.array('b', list(self.data1))
		self.data1fail[-1] = 6

		self.data2 = array.array('b', [6] * self.testarraylen)
		self.testval2 = self.data2[0]
		self.data2fail = array.array('b', list(self.data2))
		self.data2fail[-1] = 5



	########################################################
	def test_ne_numpos_array_num_a1(self):
		"""Test ne as *array-num* for failing with different data positions in array - Array code b.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != self.testval2 for x in self.data1fail])

				result = arrayfunc.ne(self.data1fail, self.testval2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_num_array_b1(self):
		"""Test ne as *num-array* for failing with different data positions in array - Array code b.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([self.testval1 != x for x in self.data2fail])

				result = arrayfunc.ne(self.testval1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


	########################################################
	def test_ne_numpos_array_array_c1(self):
		"""Test ne as *array-array* for failing with different data positions in array 1 - Array code b.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1fail, self.data2)])

				result = arrayfunc.ne(self.data1fail, self.data2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_array_array_c2(self):
		"""Test ne as *array-array* for failing with different data positions in array 2 - Array code b.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1, self.data2fail)])

				result = arrayfunc.ne(self.data1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


##############################################################################



##############################################################################
class ne_param_errors_b(unittest.TestCase):
	"""Test for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.data1 = array.array('b', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.data2 = array.array('b', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])

		# Create some array equivalents which are different than the correct ones.
		self.badarray1 = array.array('d', [5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0])
		self.badarray2 = array.array('d', [6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0])


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for incompatible array - Array code b.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badarray1, testval)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for incompatible number - Array code b.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(data1, badval)


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for incompatible array - Array code b.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(testval, badarray1)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for incompatible number - Array code b.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badval, data1)


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for incompatible second array - Array code b.
		"""
		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This version is expected to pass.
		result = arrayfunc.ne(data1, self.data2)

		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(data1, self.badarray2)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for incompatible first array - Array code b.
		"""
		# This version is expected to pass.
		result = arrayfunc.ne(self.data1, self.data2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.badarray1, self.data2)


	########################################################
	def test_ne_no_params_f1(self):
		"""Test ne with no parameters - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.ne()



##############################################################################



##############################################################################
class ne_param_errors_opt_b(unittest.TestCase):
	"""Test for invalid errors and maxlen parameters. The errors does not
	exist with these functions.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('b', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('b', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])
		self.inparray2b = copy.copy(self.inparray2a)

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for matherrors=True - Array code b.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, matherrors=True)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for maxlen='a' - Array code b.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen='a')


	########################################################
	def test_ne_array_num_a3(self):
		"""Test ne as *array-num* for nosimd='a' - Array code b.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd='a')


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for matherrors=True - Array code b.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, matherrors=True)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for maxlen='a' - Array code b.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen='a')


	########################################################
	def test_ne_num_array_c3(self):
		"""Test ne as *num-array* for nosimd='a' - Array code b.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd='a')


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for matherrors=True - Array code b.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, matherrors=True)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for maxlen='a' - Array code b.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen='a')


	########################################################
	def test_ne_array_array_e3(self):
		"""Test ne as *array-array* for nosimd='a' - Array code b.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd='a')


##############################################################################

 


##############################################################################
class ne_numpos_B(unittest.TestCase):
	"""Test with a single fail value in different array positions.
	test_template_numpos
	"""


	########################################################
	def setUp(self):
		"""Initialise. The test data is generated from the script itself.
		"""
		self.testarraylen = 159

		self.data1 = array.array('B', [5] * self.testarraylen)
		self.testval1 = self.data1[0]
		self.data1fail = array.array('B', list(self.data1))
		self.data1fail[-1] = 6

		self.data2 = array.array('B', [6] * self.testarraylen)
		self.testval2 = self.data2[0]
		self.data2fail = array.array('B', list(self.data2))
		self.data2fail[-1] = 5



	########################################################
	def test_ne_numpos_array_num_a1(self):
		"""Test ne as *array-num* for failing with different data positions in array - Array code B.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != self.testval2 for x in self.data1fail])

				result = arrayfunc.ne(self.data1fail, self.testval2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_num_array_b1(self):
		"""Test ne as *num-array* for failing with different data positions in array - Array code B.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([self.testval1 != x for x in self.data2fail])

				result = arrayfunc.ne(self.testval1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


	########################################################
	def test_ne_numpos_array_array_c1(self):
		"""Test ne as *array-array* for failing with different data positions in array 1 - Array code B.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1fail, self.data2)])

				result = arrayfunc.ne(self.data1fail, self.data2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_array_array_c2(self):
		"""Test ne as *array-array* for failing with different data positions in array 2 - Array code B.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1, self.data2fail)])

				result = arrayfunc.ne(self.data1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


##############################################################################



##############################################################################
class ne_param_errors_B(unittest.TestCase):
	"""Test for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.data1 = array.array('B', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.data2 = array.array('B', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])

		# Create some array equivalents which are different than the correct ones.
		self.badarray1 = array.array('d', [5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0])
		self.badarray2 = array.array('d', [6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0])


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for incompatible array - Array code B.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badarray1, testval)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for incompatible number - Array code B.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(data1, badval)


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for incompatible array - Array code B.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(testval, badarray1)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for incompatible number - Array code B.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badval, data1)


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for incompatible second array - Array code B.
		"""
		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This version is expected to pass.
		result = arrayfunc.ne(data1, self.data2)

		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(data1, self.badarray2)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for incompatible first array - Array code B.
		"""
		# This version is expected to pass.
		result = arrayfunc.ne(self.data1, self.data2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.badarray1, self.data2)


	########################################################
	def test_ne_no_params_f1(self):
		"""Test ne with no parameters - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.ne()



##############################################################################



##############################################################################
class ne_param_errors_opt_B(unittest.TestCase):
	"""Test for invalid errors and maxlen parameters. The errors does not
	exist with these functions.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('B', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('B', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])
		self.inparray2b = copy.copy(self.inparray2a)

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for matherrors=True - Array code B.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, matherrors=True)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for maxlen='a' - Array code B.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen='a')


	########################################################
	def test_ne_array_num_a3(self):
		"""Test ne as *array-num* for nosimd='a' - Array code B.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd='a')


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for matherrors=True - Array code B.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, matherrors=True)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for maxlen='a' - Array code B.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen='a')


	########################################################
	def test_ne_num_array_c3(self):
		"""Test ne as *num-array* for nosimd='a' - Array code B.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd='a')


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for matherrors=True - Array code B.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, matherrors=True)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for maxlen='a' - Array code B.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen='a')


	########################################################
	def test_ne_array_array_e3(self):
		"""Test ne as *array-array* for nosimd='a' - Array code B.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd='a')


##############################################################################

 


##############################################################################
class ne_numpos_h(unittest.TestCase):
	"""Test with a single fail value in different array positions.
	test_template_numpos
	"""


	########################################################
	def setUp(self):
		"""Initialise. The test data is generated from the script itself.
		"""
		self.testarraylen = 159

		self.data1 = array.array('h', [5] * self.testarraylen)
		self.testval1 = self.data1[0]
		self.data1fail = array.array('h', list(self.data1))
		self.data1fail[-1] = 6

		self.data2 = array.array('h', [6] * self.testarraylen)
		self.testval2 = self.data2[0]
		self.data2fail = array.array('h', list(self.data2))
		self.data2fail[-1] = 5



	########################################################
	def test_ne_numpos_array_num_a1(self):
		"""Test ne as *array-num* for failing with different data positions in array - Array code h.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != self.testval2 for x in self.data1fail])

				result = arrayfunc.ne(self.data1fail, self.testval2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_num_array_b1(self):
		"""Test ne as *num-array* for failing with different data positions in array - Array code h.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([self.testval1 != x for x in self.data2fail])

				result = arrayfunc.ne(self.testval1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


	########################################################
	def test_ne_numpos_array_array_c1(self):
		"""Test ne as *array-array* for failing with different data positions in array 1 - Array code h.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1fail, self.data2)])

				result = arrayfunc.ne(self.data1fail, self.data2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_array_array_c2(self):
		"""Test ne as *array-array* for failing with different data positions in array 2 - Array code h.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1, self.data2fail)])

				result = arrayfunc.ne(self.data1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


##############################################################################



##############################################################################
class ne_param_errors_h(unittest.TestCase):
	"""Test for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.data1 = array.array('h', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.data2 = array.array('h', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])

		# Create some array equivalents which are different than the correct ones.
		self.badarray1 = array.array('d', [5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0])
		self.badarray2 = array.array('d', [6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0])


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for incompatible array - Array code h.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badarray1, testval)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for incompatible number - Array code h.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(data1, badval)


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for incompatible array - Array code h.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(testval, badarray1)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for incompatible number - Array code h.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badval, data1)


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for incompatible second array - Array code h.
		"""
		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This version is expected to pass.
		result = arrayfunc.ne(data1, self.data2)

		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(data1, self.badarray2)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for incompatible first array - Array code h.
		"""
		# This version is expected to pass.
		result = arrayfunc.ne(self.data1, self.data2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.badarray1, self.data2)


	########################################################
	def test_ne_no_params_f1(self):
		"""Test ne with no parameters - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.ne()



##############################################################################



##############################################################################
class ne_param_errors_opt_h(unittest.TestCase):
	"""Test for invalid errors and maxlen parameters. The errors does not
	exist with these functions.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('h', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('h', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])
		self.inparray2b = copy.copy(self.inparray2a)

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for matherrors=True - Array code h.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, matherrors=True)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for maxlen='a' - Array code h.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen='a')


	########################################################
	def test_ne_array_num_a3(self):
		"""Test ne as *array-num* for nosimd='a' - Array code h.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd='a')


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for matherrors=True - Array code h.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, matherrors=True)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for maxlen='a' - Array code h.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen='a')


	########################################################
	def test_ne_num_array_c3(self):
		"""Test ne as *num-array* for nosimd='a' - Array code h.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd='a')


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for matherrors=True - Array code h.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, matherrors=True)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for maxlen='a' - Array code h.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen='a')


	########################################################
	def test_ne_array_array_e3(self):
		"""Test ne as *array-array* for nosimd='a' - Array code h.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd='a')


##############################################################################

 


##############################################################################
class ne_numpos_H(unittest.TestCase):
	"""Test with a single fail value in different array positions.
	test_template_numpos
	"""


	########################################################
	def setUp(self):
		"""Initialise. The test data is generated from the script itself.
		"""
		self.testarraylen = 159

		self.data1 = array.array('H', [5] * self.testarraylen)
		self.testval1 = self.data1[0]
		self.data1fail = array.array('H', list(self.data1))
		self.data1fail[-1] = 6

		self.data2 = array.array('H', [6] * self.testarraylen)
		self.testval2 = self.data2[0]
		self.data2fail = array.array('H', list(self.data2))
		self.data2fail[-1] = 5



	########################################################
	def test_ne_numpos_array_num_a1(self):
		"""Test ne as *array-num* for failing with different data positions in array - Array code H.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != self.testval2 for x in self.data1fail])

				result = arrayfunc.ne(self.data1fail, self.testval2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_num_array_b1(self):
		"""Test ne as *num-array* for failing with different data positions in array - Array code H.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([self.testval1 != x for x in self.data2fail])

				result = arrayfunc.ne(self.testval1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


	########################################################
	def test_ne_numpos_array_array_c1(self):
		"""Test ne as *array-array* for failing with different data positions in array 1 - Array code H.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1fail, self.data2)])

				result = arrayfunc.ne(self.data1fail, self.data2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_array_array_c2(self):
		"""Test ne as *array-array* for failing with different data positions in array 2 - Array code H.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1, self.data2fail)])

				result = arrayfunc.ne(self.data1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


##############################################################################



##############################################################################
class ne_param_errors_H(unittest.TestCase):
	"""Test for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.data1 = array.array('H', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.data2 = array.array('H', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])

		# Create some array equivalents which are different than the correct ones.
		self.badarray1 = array.array('d', [5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0])
		self.badarray2 = array.array('d', [6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0])


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for incompatible array - Array code H.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badarray1, testval)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for incompatible number - Array code H.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(data1, badval)


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for incompatible array - Array code H.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(testval, badarray1)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for incompatible number - Array code H.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badval, data1)


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for incompatible second array - Array code H.
		"""
		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This version is expected to pass.
		result = arrayfunc.ne(data1, self.data2)

		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(data1, self.badarray2)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for incompatible first array - Array code H.
		"""
		# This version is expected to pass.
		result = arrayfunc.ne(self.data1, self.data2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.badarray1, self.data2)


	########################################################
	def test_ne_no_params_f1(self):
		"""Test ne with no parameters - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.ne()



##############################################################################



##############################################################################
class ne_param_errors_opt_H(unittest.TestCase):
	"""Test for invalid errors and maxlen parameters. The errors does not
	exist with these functions.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('H', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('H', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])
		self.inparray2b = copy.copy(self.inparray2a)

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for matherrors=True - Array code H.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, matherrors=True)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for maxlen='a' - Array code H.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen='a')


	########################################################
	def test_ne_array_num_a3(self):
		"""Test ne as *array-num* for nosimd='a' - Array code H.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd='a')


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for matherrors=True - Array code H.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, matherrors=True)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for maxlen='a' - Array code H.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen='a')


	########################################################
	def test_ne_num_array_c3(self):
		"""Test ne as *num-array* for nosimd='a' - Array code H.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd='a')


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for matherrors=True - Array code H.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, matherrors=True)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for maxlen='a' - Array code H.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen='a')


	########################################################
	def test_ne_array_array_e3(self):
		"""Test ne as *array-array* for nosimd='a' - Array code H.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd='a')


##############################################################################

 


##############################################################################
class ne_numpos_i(unittest.TestCase):
	"""Test with a single fail value in different array positions.
	test_template_numpos
	"""


	########################################################
	def setUp(self):
		"""Initialise. The test data is generated from the script itself.
		"""
		self.testarraylen = 159

		self.data1 = array.array('i', [5] * self.testarraylen)
		self.testval1 = self.data1[0]
		self.data1fail = array.array('i', list(self.data1))
		self.data1fail[-1] = 6

		self.data2 = array.array('i', [6] * self.testarraylen)
		self.testval2 = self.data2[0]
		self.data2fail = array.array('i', list(self.data2))
		self.data2fail[-1] = 5



	########################################################
	def test_ne_numpos_array_num_a1(self):
		"""Test ne as *array-num* for failing with different data positions in array - Array code i.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != self.testval2 for x in self.data1fail])

				result = arrayfunc.ne(self.data1fail, self.testval2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_num_array_b1(self):
		"""Test ne as *num-array* for failing with different data positions in array - Array code i.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([self.testval1 != x for x in self.data2fail])

				result = arrayfunc.ne(self.testval1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


	########################################################
	def test_ne_numpos_array_array_c1(self):
		"""Test ne as *array-array* for failing with different data positions in array 1 - Array code i.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1fail, self.data2)])

				result = arrayfunc.ne(self.data1fail, self.data2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_array_array_c2(self):
		"""Test ne as *array-array* for failing with different data positions in array 2 - Array code i.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1, self.data2fail)])

				result = arrayfunc.ne(self.data1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


##############################################################################



##############################################################################
class ne_param_errors_i(unittest.TestCase):
	"""Test for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.data1 = array.array('i', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.data2 = array.array('i', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])

		# Create some array equivalents which are different than the correct ones.
		self.badarray1 = array.array('d', [5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0])
		self.badarray2 = array.array('d', [6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0])


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for incompatible array - Array code i.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badarray1, testval)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for incompatible number - Array code i.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(data1, badval)


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for incompatible array - Array code i.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(testval, badarray1)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for incompatible number - Array code i.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badval, data1)


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for incompatible second array - Array code i.
		"""
		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This version is expected to pass.
		result = arrayfunc.ne(data1, self.data2)

		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(data1, self.badarray2)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for incompatible first array - Array code i.
		"""
		# This version is expected to pass.
		result = arrayfunc.ne(self.data1, self.data2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.badarray1, self.data2)


	########################################################
	def test_ne_no_params_f1(self):
		"""Test ne with no parameters - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.ne()



##############################################################################



##############################################################################
class ne_param_errors_opt_i(unittest.TestCase):
	"""Test for invalid errors and maxlen parameters. The errors does not
	exist with these functions.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('i', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('i', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])
		self.inparray2b = copy.copy(self.inparray2a)

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for matherrors=True - Array code i.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, matherrors=True)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for maxlen='a' - Array code i.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen='a')


	########################################################
	def test_ne_array_num_a3(self):
		"""Test ne as *array-num* for nosimd='a' - Array code i.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd='a')


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for matherrors=True - Array code i.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, matherrors=True)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for maxlen='a' - Array code i.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen='a')


	########################################################
	def test_ne_num_array_c3(self):
		"""Test ne as *num-array* for nosimd='a' - Array code i.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd='a')


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for matherrors=True - Array code i.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, matherrors=True)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for maxlen='a' - Array code i.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen='a')


	########################################################
	def test_ne_array_array_e3(self):
		"""Test ne as *array-array* for nosimd='a' - Array code i.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd='a')


##############################################################################

 


##############################################################################
class ne_numpos_I(unittest.TestCase):
	"""Test with a single fail value in different array positions.
	test_template_numpos
	"""


	########################################################
	def setUp(self):
		"""Initialise. The test data is generated from the script itself.
		"""
		self.testarraylen = 159

		self.data1 = array.array('I', [5] * self.testarraylen)
		self.testval1 = self.data1[0]
		self.data1fail = array.array('I', list(self.data1))
		self.data1fail[-1] = 6

		self.data2 = array.array('I', [6] * self.testarraylen)
		self.testval2 = self.data2[0]
		self.data2fail = array.array('I', list(self.data2))
		self.data2fail[-1] = 5



	########################################################
	def test_ne_numpos_array_num_a1(self):
		"""Test ne as *array-num* for failing with different data positions in array - Array code I.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != self.testval2 for x in self.data1fail])

				result = arrayfunc.ne(self.data1fail, self.testval2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_num_array_b1(self):
		"""Test ne as *num-array* for failing with different data positions in array - Array code I.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([self.testval1 != x for x in self.data2fail])

				result = arrayfunc.ne(self.testval1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


	########################################################
	def test_ne_numpos_array_array_c1(self):
		"""Test ne as *array-array* for failing with different data positions in array 1 - Array code I.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1fail, self.data2)])

				result = arrayfunc.ne(self.data1fail, self.data2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_array_array_c2(self):
		"""Test ne as *array-array* for failing with different data positions in array 2 - Array code I.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1, self.data2fail)])

				result = arrayfunc.ne(self.data1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


##############################################################################



##############################################################################
class ne_param_errors_I(unittest.TestCase):
	"""Test for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.data1 = array.array('I', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.data2 = array.array('I', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])

		# Create some array equivalents which are different than the correct ones.
		self.badarray1 = array.array('d', [5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0])
		self.badarray2 = array.array('d', [6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0])


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for incompatible array - Array code I.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badarray1, testval)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for incompatible number - Array code I.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(data1, badval)


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for incompatible array - Array code I.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(testval, badarray1)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for incompatible number - Array code I.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badval, data1)


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for incompatible second array - Array code I.
		"""
		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This version is expected to pass.
		result = arrayfunc.ne(data1, self.data2)

		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(data1, self.badarray2)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for incompatible first array - Array code I.
		"""
		# This version is expected to pass.
		result = arrayfunc.ne(self.data1, self.data2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.badarray1, self.data2)


	########################################################
	def test_ne_no_params_f1(self):
		"""Test ne with no parameters - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.ne()



##############################################################################



##############################################################################
class ne_param_errors_opt_I(unittest.TestCase):
	"""Test for invalid errors and maxlen parameters. The errors does not
	exist with these functions.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('I', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('I', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])
		self.inparray2b = copy.copy(self.inparray2a)

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for matherrors=True - Array code I.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, matherrors=True)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for maxlen='a' - Array code I.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen='a')


	########################################################
	def test_ne_array_num_a3(self):
		"""Test ne as *array-num* for nosimd='a' - Array code I.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd='a')


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for matherrors=True - Array code I.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, matherrors=True)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for maxlen='a' - Array code I.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen='a')


	########################################################
	def test_ne_num_array_c3(self):
		"""Test ne as *num-array* for nosimd='a' - Array code I.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd='a')


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for matherrors=True - Array code I.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, matherrors=True)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for maxlen='a' - Array code I.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen='a')


	########################################################
	def test_ne_array_array_e3(self):
		"""Test ne as *array-array* for nosimd='a' - Array code I.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd='a')


##############################################################################

 


##############################################################################
class ne_numpos_l(unittest.TestCase):
	"""Test with a single fail value in different array positions.
	test_template_numpos
	"""


	########################################################
	def setUp(self):
		"""Initialise. The test data is generated from the script itself.
		"""
		self.testarraylen = 159

		self.data1 = array.array('l', [5] * self.testarraylen)
		self.testval1 = self.data1[0]
		self.data1fail = array.array('l', list(self.data1))
		self.data1fail[-1] = 6

		self.data2 = array.array('l', [6] * self.testarraylen)
		self.testval2 = self.data2[0]
		self.data2fail = array.array('l', list(self.data2))
		self.data2fail[-1] = 5



	########################################################
	def test_ne_numpos_array_num_a1(self):
		"""Test ne as *array-num* for failing with different data positions in array - Array code l.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != self.testval2 for x in self.data1fail])

				result = arrayfunc.ne(self.data1fail, self.testval2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_num_array_b1(self):
		"""Test ne as *num-array* for failing with different data positions in array - Array code l.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([self.testval1 != x for x in self.data2fail])

				result = arrayfunc.ne(self.testval1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


	########################################################
	def test_ne_numpos_array_array_c1(self):
		"""Test ne as *array-array* for failing with different data positions in array 1 - Array code l.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1fail, self.data2)])

				result = arrayfunc.ne(self.data1fail, self.data2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_array_array_c2(self):
		"""Test ne as *array-array* for failing with different data positions in array 2 - Array code l.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1, self.data2fail)])

				result = arrayfunc.ne(self.data1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


##############################################################################



##############################################################################
class ne_param_errors_l(unittest.TestCase):
	"""Test for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.data1 = array.array('l', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.data2 = array.array('l', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])

		# Create some array equivalents which are different than the correct ones.
		self.badarray1 = array.array('d', [5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0])
		self.badarray2 = array.array('d', [6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0])


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for incompatible array - Array code l.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badarray1, testval)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for incompatible number - Array code l.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(data1, badval)


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for incompatible array - Array code l.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(testval, badarray1)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for incompatible number - Array code l.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badval, data1)


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for incompatible second array - Array code l.
		"""
		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This version is expected to pass.
		result = arrayfunc.ne(data1, self.data2)

		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(data1, self.badarray2)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for incompatible first array - Array code l.
		"""
		# This version is expected to pass.
		result = arrayfunc.ne(self.data1, self.data2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.badarray1, self.data2)


	########################################################
	def test_ne_no_params_f1(self):
		"""Test ne with no parameters - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.ne()



##############################################################################



##############################################################################
class ne_param_errors_opt_l(unittest.TestCase):
	"""Test for invalid errors and maxlen parameters. The errors does not
	exist with these functions.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('l', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('l', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])
		self.inparray2b = copy.copy(self.inparray2a)

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for matherrors=True - Array code l.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, matherrors=True)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for maxlen='a' - Array code l.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen='a')


	########################################################
	def test_ne_array_num_a3(self):
		"""Test ne as *array-num* for nosimd='a' - Array code l.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd='a')


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for matherrors=True - Array code l.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, matherrors=True)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for maxlen='a' - Array code l.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen='a')


	########################################################
	def test_ne_num_array_c3(self):
		"""Test ne as *num-array* for nosimd='a' - Array code l.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd='a')


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for matherrors=True - Array code l.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, matherrors=True)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for maxlen='a' - Array code l.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen='a')


	########################################################
	def test_ne_array_array_e3(self):
		"""Test ne as *array-array* for nosimd='a' - Array code l.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd='a')


##############################################################################

 


##############################################################################
class ne_numpos_L(unittest.TestCase):
	"""Test with a single fail value in different array positions.
	test_template_numpos
	"""


	########################################################
	def setUp(self):
		"""Initialise. The test data is generated from the script itself.
		"""
		self.testarraylen = 159

		self.data1 = array.array('L', [5] * self.testarraylen)
		self.testval1 = self.data1[0]
		self.data1fail = array.array('L', list(self.data1))
		self.data1fail[-1] = 6

		self.data2 = array.array('L', [6] * self.testarraylen)
		self.testval2 = self.data2[0]
		self.data2fail = array.array('L', list(self.data2))
		self.data2fail[-1] = 5



	########################################################
	def test_ne_numpos_array_num_a1(self):
		"""Test ne as *array-num* for failing with different data positions in array - Array code L.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != self.testval2 for x in self.data1fail])

				result = arrayfunc.ne(self.data1fail, self.testval2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_num_array_b1(self):
		"""Test ne as *num-array* for failing with different data positions in array - Array code L.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([self.testval1 != x for x in self.data2fail])

				result = arrayfunc.ne(self.testval1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


	########################################################
	def test_ne_numpos_array_array_c1(self):
		"""Test ne as *array-array* for failing with different data positions in array 1 - Array code L.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1fail, self.data2)])

				result = arrayfunc.ne(self.data1fail, self.data2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_array_array_c2(self):
		"""Test ne as *array-array* for failing with different data positions in array 2 - Array code L.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1, self.data2fail)])

				result = arrayfunc.ne(self.data1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


##############################################################################



##############################################################################
class ne_param_errors_L(unittest.TestCase):
	"""Test for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.data1 = array.array('L', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.data2 = array.array('L', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])

		# Create some array equivalents which are different than the correct ones.
		self.badarray1 = array.array('d', [5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0])
		self.badarray2 = array.array('d', [6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0])


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for incompatible array - Array code L.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badarray1, testval)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for incompatible number - Array code L.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(data1, badval)


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for incompatible array - Array code L.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(testval, badarray1)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for incompatible number - Array code L.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badval, data1)


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for incompatible second array - Array code L.
		"""
		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This version is expected to pass.
		result = arrayfunc.ne(data1, self.data2)

		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(data1, self.badarray2)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for incompatible first array - Array code L.
		"""
		# This version is expected to pass.
		result = arrayfunc.ne(self.data1, self.data2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.badarray1, self.data2)


	########################################################
	def test_ne_no_params_f1(self):
		"""Test ne with no parameters - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.ne()



##############################################################################



##############################################################################
class ne_param_errors_opt_L(unittest.TestCase):
	"""Test for invalid errors and maxlen parameters. The errors does not
	exist with these functions.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('L', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('L', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])
		self.inparray2b = copy.copy(self.inparray2a)

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for matherrors=True - Array code L.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, matherrors=True)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for maxlen='a' - Array code L.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen='a')


	########################################################
	def test_ne_array_num_a3(self):
		"""Test ne as *array-num* for nosimd='a' - Array code L.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd='a')


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for matherrors=True - Array code L.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, matherrors=True)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for maxlen='a' - Array code L.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen='a')


	########################################################
	def test_ne_num_array_c3(self):
		"""Test ne as *num-array* for nosimd='a' - Array code L.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd='a')


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for matherrors=True - Array code L.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, matherrors=True)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for maxlen='a' - Array code L.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen='a')


	########################################################
	def test_ne_array_array_e3(self):
		"""Test ne as *array-array* for nosimd='a' - Array code L.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd='a')


##############################################################################

 


##############################################################################
class ne_numpos_q(unittest.TestCase):
	"""Test with a single fail value in different array positions.
	test_template_numpos
	"""


	########################################################
	def setUp(self):
		"""Initialise. The test data is generated from the script itself.
		"""
		self.testarraylen = 159

		self.data1 = array.array('q', [5] * self.testarraylen)
		self.testval1 = self.data1[0]
		self.data1fail = array.array('q', list(self.data1))
		self.data1fail[-1] = 6

		self.data2 = array.array('q', [6] * self.testarraylen)
		self.testval2 = self.data2[0]
		self.data2fail = array.array('q', list(self.data2))
		self.data2fail[-1] = 5



	########################################################
	def test_ne_numpos_array_num_a1(self):
		"""Test ne as *array-num* for failing with different data positions in array - Array code q.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != self.testval2 for x in self.data1fail])

				result = arrayfunc.ne(self.data1fail, self.testval2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_num_array_b1(self):
		"""Test ne as *num-array* for failing with different data positions in array - Array code q.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([self.testval1 != x for x in self.data2fail])

				result = arrayfunc.ne(self.testval1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


	########################################################
	def test_ne_numpos_array_array_c1(self):
		"""Test ne as *array-array* for failing with different data positions in array 1 - Array code q.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1fail, self.data2)])

				result = arrayfunc.ne(self.data1fail, self.data2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_array_array_c2(self):
		"""Test ne as *array-array* for failing with different data positions in array 2 - Array code q.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1, self.data2fail)])

				result = arrayfunc.ne(self.data1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


##############################################################################



##############################################################################
class ne_param_errors_q(unittest.TestCase):
	"""Test for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.data1 = array.array('q', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.data2 = array.array('q', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])

		# Create some array equivalents which are different than the correct ones.
		self.badarray1 = array.array('d', [5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0])
		self.badarray2 = array.array('d', [6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0])


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for incompatible array - Array code q.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badarray1, testval)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for incompatible number - Array code q.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(data1, badval)


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for incompatible array - Array code q.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(testval, badarray1)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for incompatible number - Array code q.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badval, data1)


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for incompatible second array - Array code q.
		"""
		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This version is expected to pass.
		result = arrayfunc.ne(data1, self.data2)

		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(data1, self.badarray2)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for incompatible first array - Array code q.
		"""
		# This version is expected to pass.
		result = arrayfunc.ne(self.data1, self.data2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.badarray1, self.data2)


	########################################################
	def test_ne_no_params_f1(self):
		"""Test ne with no parameters - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.ne()



##############################################################################



##############################################################################
class ne_param_errors_opt_q(unittest.TestCase):
	"""Test for invalid errors and maxlen parameters. The errors does not
	exist with these functions.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('q', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('q', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])
		self.inparray2b = copy.copy(self.inparray2a)

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for matherrors=True - Array code q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, matherrors=True)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for maxlen='a' - Array code q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen='a')


	########################################################
	def test_ne_array_num_a3(self):
		"""Test ne as *array-num* for nosimd='a' - Array code q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd='a')


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for matherrors=True - Array code q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, matherrors=True)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for maxlen='a' - Array code q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen='a')


	########################################################
	def test_ne_num_array_c3(self):
		"""Test ne as *num-array* for nosimd='a' - Array code q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd='a')


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for matherrors=True - Array code q.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, matherrors=True)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for maxlen='a' - Array code q.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen='a')


	########################################################
	def test_ne_array_array_e3(self):
		"""Test ne as *array-array* for nosimd='a' - Array code q.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd='a')


##############################################################################

 


##############################################################################
class ne_numpos_Q(unittest.TestCase):
	"""Test with a single fail value in different array positions.
	test_template_numpos
	"""


	########################################################
	def setUp(self):
		"""Initialise. The test data is generated from the script itself.
		"""
		self.testarraylen = 159

		self.data1 = array.array('Q', [5] * self.testarraylen)
		self.testval1 = self.data1[0]
		self.data1fail = array.array('Q', list(self.data1))
		self.data1fail[-1] = 6

		self.data2 = array.array('Q', [6] * self.testarraylen)
		self.testval2 = self.data2[0]
		self.data2fail = array.array('Q', list(self.data2))
		self.data2fail[-1] = 5



	########################################################
	def test_ne_numpos_array_num_a1(self):
		"""Test ne as *array-num* for failing with different data positions in array - Array code Q.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != self.testval2 for x in self.data1fail])

				result = arrayfunc.ne(self.data1fail, self.testval2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_num_array_b1(self):
		"""Test ne as *num-array* for failing with different data positions in array - Array code Q.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([self.testval1 != x for x in self.data2fail])

				result = arrayfunc.ne(self.testval1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


	########################################################
	def test_ne_numpos_array_array_c1(self):
		"""Test ne as *array-array* for failing with different data positions in array 1 - Array code Q.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1fail, self.data2)])

				result = arrayfunc.ne(self.data1fail, self.data2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_array_array_c2(self):
		"""Test ne as *array-array* for failing with different data positions in array 2 - Array code Q.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1, self.data2fail)])

				result = arrayfunc.ne(self.data1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


##############################################################################



##############################################################################
class ne_param_errors_Q(unittest.TestCase):
	"""Test for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.data1 = array.array('Q', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.data2 = array.array('Q', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])

		# Create some array equivalents which are different than the correct ones.
		self.badarray1 = array.array('d', [5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0])
		self.badarray2 = array.array('d', [6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0])


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for incompatible array - Array code Q.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badarray1, testval)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for incompatible number - Array code Q.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(data1, badval)


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for incompatible array - Array code Q.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(testval, badarray1)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for incompatible number - Array code Q.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badval, data1)


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for incompatible second array - Array code Q.
		"""
		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This version is expected to pass.
		result = arrayfunc.ne(data1, self.data2)

		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(data1, self.badarray2)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for incompatible first array - Array code Q.
		"""
		# This version is expected to pass.
		result = arrayfunc.ne(self.data1, self.data2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.badarray1, self.data2)


	########################################################
	def test_ne_no_params_f1(self):
		"""Test ne with no parameters - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.ne()



##############################################################################



##############################################################################
class ne_param_errors_opt_Q(unittest.TestCase):
	"""Test for invalid errors and maxlen parameters. The errors does not
	exist with these functions.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('Q', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('Q', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])
		self.inparray2b = copy.copy(self.inparray2a)

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for matherrors=True - Array code Q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, matherrors=True)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for maxlen='a' - Array code Q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen='a')


	########################################################
	def test_ne_array_num_a3(self):
		"""Test ne as *array-num* for nosimd='a' - Array code Q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd='a')


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for matherrors=True - Array code Q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, matherrors=True)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for maxlen='a' - Array code Q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen='a')


	########################################################
	def test_ne_num_array_c3(self):
		"""Test ne as *num-array* for nosimd='a' - Array code Q.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd='a')


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for matherrors=True - Array code Q.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, matherrors=True)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for maxlen='a' - Array code Q.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen='a')


	########################################################
	def test_ne_array_array_e3(self):
		"""Test ne as *array-array* for nosimd='a' - Array code Q.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd='a')


##############################################################################

 


##############################################################################
class ne_numpos_f(unittest.TestCase):
	"""Test with a single fail value in different array positions.
	test_template_numpos
	"""


	########################################################
	def setUp(self):
		"""Initialise. The test data is generated from the script itself.
		"""
		self.testarraylen = 159

		self.data1 = array.array('f', [5] * self.testarraylen)
		self.testval1 = self.data1[0]
		self.data1fail = array.array('f', list(self.data1))
		self.data1fail[-1] = 6

		self.data2 = array.array('f', [6] * self.testarraylen)
		self.testval2 = self.data2[0]
		self.data2fail = array.array('f', list(self.data2))
		self.data2fail[-1] = 5



	########################################################
	def test_ne_numpos_array_num_a1(self):
		"""Test ne as *array-num* for failing with different data positions in array - Array code f.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != self.testval2 for x in self.data1fail])

				result = arrayfunc.ne(self.data1fail, self.testval2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_num_array_b1(self):
		"""Test ne as *num-array* for failing with different data positions in array - Array code f.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([self.testval1 != x for x in self.data2fail])

				result = arrayfunc.ne(self.testval1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


	########################################################
	def test_ne_numpos_array_array_c1(self):
		"""Test ne as *array-array* for failing with different data positions in array 1 - Array code f.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1fail, self.data2)])

				result = arrayfunc.ne(self.data1fail, self.data2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_array_array_c2(self):
		"""Test ne as *array-array* for failing with different data positions in array 2 - Array code f.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1, self.data2fail)])

				result = arrayfunc.ne(self.data1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


##############################################################################



##############################################################################
class ne_param_errors_f(unittest.TestCase):
	"""Test for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.data1 = array.array('f', [5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0])
		self.data2 = array.array('f', [6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0])

		# Create some array equivalents which are different than the correct ones.
		self.badarray1 = array.array('i', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.badarray2 = array.array('i', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for incompatible array - Array code f.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badarray1, testval)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for incompatible number - Array code f.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(data1, badval)


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for incompatible array - Array code f.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(testval, badarray1)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for incompatible number - Array code f.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badval, data1)


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for incompatible second array - Array code f.
		"""
		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This version is expected to pass.
		result = arrayfunc.ne(data1, self.data2)

		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(data1, self.badarray2)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for incompatible first array - Array code f.
		"""
		# This version is expected to pass.
		result = arrayfunc.ne(self.data1, self.data2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.badarray1, self.data2)


	########################################################
	def test_ne_no_params_f1(self):
		"""Test ne with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.ne()



##############################################################################



##############################################################################
class ne_param_errors_opt_f(unittest.TestCase):
	"""Test for invalid errors and maxlen parameters. The errors does not
	exist with these functions.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('f', [5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('f', [6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0])
		self.inparray2b = copy.copy(self.inparray2a)

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for matherrors=True - Array code f.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, matherrors=True)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for maxlen='a' - Array code f.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen='a')


	########################################################
	def test_ne_array_num_a3(self):
		"""Test ne as *array-num* for nosimd='a' - Array code f.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd='a')


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for matherrors=True - Array code f.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, matherrors=True)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for maxlen='a' - Array code f.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen='a')


	########################################################
	def test_ne_num_array_c3(self):
		"""Test ne as *num-array* for nosimd='a' - Array code f.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd='a')


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for matherrors=True - Array code f.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, matherrors=True)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for maxlen='a' - Array code f.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen='a')


	########################################################
	def test_ne_array_array_e3(self):
		"""Test ne as *array-array* for nosimd='a' - Array code f.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd='a')


##############################################################################



##############################################################################
class ne_errors_nf_f(unittest.TestCase):
	"""Test for basic general function operation using parameter NaN, inf, and -inf.
	nan_data_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testvalue = 10.5
		self.testdata = array.array('f', [self.testvalue] * 20)

		self.nanvalue = math.nan
		self.infvalue = math.inf
		self.ninfvalue = -math.inf

		self.nandata = array.array('f', [float(self.nanvalue)] * len(self.testdata))
		self.infdata = array.array('f', [float(self.infvalue)] * len(self.testdata))
		self.ninfdata = array.array('f', [float(self.ninfvalue)] * len(self.testdata))


	########################################################
	def test_ne_nan_data_array_num_a1(self):
		"""Test ne as *array-num* for NaN value - Array code f.
		"""
		expected = all([x != self.nanvalue for x in self.testdata])

		result = arrayfunc.ne(self.testdata, self.nanvalue)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_num_a2(self):
		"""Test ne as *array-num* for NaN array - Array code f.
		"""
		expected = all([x != self.testvalue for x in self.nandata])

		result = arrayfunc.ne(self.nandata, self.testvalue)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_num_array_a3(self):
		"""Test ne as *num-array* for NaN value - Array code f.
		"""
		expected = all([self.nanvalue != x for x in self.testdata])

		result = arrayfunc.ne(self.nanvalue, self.testdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_num_array_a4(self):
		"""Test ne as *num-array* for NaN array - Array code f.
		"""
		expected = all([self.testvalue != x for x in self.nandata])

		result = arrayfunc.ne(self.testvalue, self.nandata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_array_a5(self):
		"""Test ne as *array-array* for NaN array 1 - Array code f.
		"""
		expected = all([x != y for (x,y) in zip(self.nandata, self.testdata)])

		result = arrayfunc.ne(self.nandata, self.testdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_array_a6(self):
		"""Test ne as *array-array* for NaN array 2 - Array code f.
		"""
		expected = all([x != y for (x,y) in zip(self.testdata, self.nandata)])

		result = arrayfunc.ne(self.testdata, self.nandata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_num_b1(self):
		"""Test ne as *array-num* for inf value - Array code f.
		"""
		expected = all([x != self.infvalue for x in self.testdata])

		result = arrayfunc.ne(self.testdata, self.infvalue)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_num_b2(self):
		"""Test ne as *array-num* for inf array - Array code f.
		"""
		expected = all([x != self.testvalue for x in self.infdata])

		result = arrayfunc.ne(self.infdata, self.testvalue)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_num_array_b3(self):
		"""Test ne as *num-array* for inf value - Array code f.
		"""
		expected = all([self.infvalue != x for x in self.testdata])

		result = arrayfunc.ne(self.infvalue, self.testdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_num_array_b4(self):
		"""Test ne as *num-array* for inf array - Array code f.
		"""
		expected = all([self.testvalue != x for x in self.infdata])

		result = arrayfunc.ne(self.testvalue, self.infdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_array_b5(self):
		"""Test ne as *array-array* for inf array 1 - Array code f.
		"""
		expected = all([x != y for (x,y) in zip(self.infdata, self.testdata)])

		result = arrayfunc.ne(self.infdata, self.testdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_array_b6(self):
		"""Test ne as *array-array* for inf array 2 - Array code f.
		"""
		expected = all([x != y for (x,y) in zip(self.testdata, self.infdata)])

		result = arrayfunc.ne(self.testdata, self.infdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_num_c1(self):
		"""Test ne as *array-num* for -inf value - Array code f.
		"""
		expected = all([x != self.ninfvalue for x in self.testdata])

		result = arrayfunc.ne(self.testdata, self.ninfvalue)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_num_c2(self):
		"""Test ne as *array-num* for -inf array - Array code f.
		"""
		expected = all([x != self.testvalue for x in self.ninfdata])

		result = arrayfunc.ne(self.ninfdata, self.testvalue)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_num_array_c3(self):
		"""Test ne as *num-array* for -inf value - Array code f.
		"""
		expected = all([self.ninfvalue != x for x in self.testdata])

		result = arrayfunc.ne(self.ninfvalue, self.testdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_num_array_c4(self):
		"""Test ne as *num-array* for -inf array - Array code f.
		"""
		expected = all([self.testvalue != x for x in self.ninfdata])

		result = arrayfunc.ne(self.testvalue, self.ninfdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_array_c5(self):
		"""Test ne as *array-array* for -inf array 1 - Array code f.
		"""
		expected = all([x != y for (x,y) in zip(self.ninfdata, self.testdata)])

		result = arrayfunc.ne(self.ninfdata, self.testdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_array_c6(self):
		"""Test ne as *array-array* for -inf array 2 - Array code f.
		"""
		expected = all([x != y for (x,y) in zip(self.testdata, self.ninfdata)])

		result = arrayfunc.ne(self.testdata, self.ninfdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 


##############################################################################
class ne_numpos_d(unittest.TestCase):
	"""Test with a single fail value in different array positions.
	test_template_numpos
	"""


	########################################################
	def setUp(self):
		"""Initialise. The test data is generated from the script itself.
		"""
		self.testarraylen = 159

		self.data1 = array.array('d', [5] * self.testarraylen)
		self.testval1 = self.data1[0]
		self.data1fail = array.array('d', list(self.data1))
		self.data1fail[-1] = 6

		self.data2 = array.array('d', [6] * self.testarraylen)
		self.testval2 = self.data2[0]
		self.data2fail = array.array('d', list(self.data2))
		self.data2fail[-1] = 5



	########################################################
	def test_ne_numpos_array_num_a1(self):
		"""Test ne as *array-num* for failing with different data positions in array - Array code d.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != self.testval2 for x in self.data1fail])

				result = arrayfunc.ne(self.data1fail, self.testval2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_num_array_b1(self):
		"""Test ne as *num-array* for failing with different data positions in array - Array code d.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([self.testval1 != x for x in self.data2fail])

				result = arrayfunc.ne(self.testval1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


	########################################################
	def test_ne_numpos_array_array_c1(self):
		"""Test ne as *array-array* for failing with different data positions in array 1 - Array code d.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1fail, self.data2)])

				result = arrayfunc.ne(self.data1fail, self.data2)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data1.append(self.data1.pop(0))


	########################################################
	def test_ne_numpos_array_array_c2(self):
		"""Test ne as *array-array* for failing with different data positions in array 2 - Array code d.
		"""
		for testpos in range(self.testarraylen):
			with self.subTest(msg='Failed with posistion', testpos = testpos):

				expected = all([x != y for x,y in zip(self.data1, self.data2fail)])

				result = arrayfunc.ne(self.data1, self.data2fail)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)

			
			# Shift the data one position.
			self.data2.append(self.data2.pop(0))


##############################################################################



##############################################################################
class ne_param_errors_d(unittest.TestCase):
	"""Test for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.data1 = array.array('d', [5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0])
		self.data2 = array.array('d', [6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0])

		# Create some array equivalents which are different than the correct ones.
		self.badarray1 = array.array('i', [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5])
		self.badarray2 = array.array('i', [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6])


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for incompatible array - Array code d.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badarray1, testval)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for incompatible number - Array code d.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(data1, testval)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(data1, badval)


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for incompatible array - Array code d.
		"""
		for testval in self.data2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(testval, badarray1)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for incompatible number - Array code d.
		"""
		for testval, badval in zip(self.data2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				data1 = copy.copy(self.data1)

				# This version is expected to pass.
				result = arrayfunc.ne(testval, data1)

				data1 = copy.copy(self.data1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					result = arrayfunc.ne(badval, data1)


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for incompatible second array - Array code d.
		"""
		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This version is expected to pass.
		result = arrayfunc.ne(data1, self.data2)

		# Copy the array so we don't change the original data.
		data1 = copy.copy(self.data1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(data1, self.badarray2)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for incompatible first array - Array code d.
		"""
		# This version is expected to pass.
		result = arrayfunc.ne(self.data1, self.data2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.badarray1, self.data2)


	########################################################
	def test_ne_no_params_f1(self):
		"""Test ne with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.ne()



##############################################################################



##############################################################################
class ne_param_errors_opt_d(unittest.TestCase):
	"""Test for invalid errors and maxlen parameters. The errors does not
	exist with these functions.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.inparray1a = array.array('d', [5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0])
		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2a = array.array('d', [6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0])
		self.inparray2b = copy.copy(self.inparray2a)

		self.testmaxlen = len(self.inparray1a) // 2


	########################################################
	def test_ne_array_num_a1(self):
		"""Test ne as *array-num* for matherrors=True - Array code d.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, matherrors=True)


	########################################################
	def test_ne_array_num_a2(self):
		"""Test ne as *array-num* for maxlen='a' - Array code d.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, maxlen='a')


	########################################################
	def test_ne_array_num_a3(self):
		"""Test ne as *array-num* for nosimd='a' - Array code d.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, inpvalue, nosimd='a')


	########################################################
	def test_ne_num_array_c1(self):
		"""Test ne as *num-array* for matherrors=True - Array code d.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, matherrors=True)


	########################################################
	def test_ne_num_array_c2(self):
		"""Test ne as *num-array* for maxlen='a' - Array code d.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, maxlen='a')


	########################################################
	def test_ne_num_array_c3(self):
		"""Test ne as *num-array* for nosimd='a' - Array code d.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(inpvalue, self.inparray1a, nosimd='a')


	########################################################
	def test_ne_array_array_e1(self):
		"""Test ne as *array-array* for matherrors=True - Array code d.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, matherrors=True)


	########################################################
	def test_ne_array_array_e2(self):
		"""Test ne as *array-array* for maxlen='a' - Array code d.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, maxlen='a')


	########################################################
	def test_ne_array_array_e3(self):
		"""Test ne as *array-array* for nosimd='a' - Array code d.
		"""

		# This version is expected to pass.
		result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			result = arrayfunc.ne(self.inparray1a, self.inparray2a, nosimd='a')


##############################################################################



##############################################################################
class ne_errors_nf_d(unittest.TestCase):
	"""Test for basic general function operation using parameter NaN, inf, and -inf.
	nan_data_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.testvalue = 10.5
		self.testdata = array.array('d', [self.testvalue] * 20)

		self.nanvalue = math.nan
		self.infvalue = math.inf
		self.ninfvalue = -math.inf

		self.nandata = array.array('d', [float(self.nanvalue)] * len(self.testdata))
		self.infdata = array.array('d', [float(self.infvalue)] * len(self.testdata))
		self.ninfdata = array.array('d', [float(self.ninfvalue)] * len(self.testdata))


	########################################################
	def test_ne_nan_data_array_num_a1(self):
		"""Test ne as *array-num* for NaN value - Array code d.
		"""
		expected = all([x != self.nanvalue for x in self.testdata])

		result = arrayfunc.ne(self.testdata, self.nanvalue)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_num_a2(self):
		"""Test ne as *array-num* for NaN array - Array code d.
		"""
		expected = all([x != self.testvalue for x in self.nandata])

		result = arrayfunc.ne(self.nandata, self.testvalue)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_num_array_a3(self):
		"""Test ne as *num-array* for NaN value - Array code d.
		"""
		expected = all([self.nanvalue != x for x in self.testdata])

		result = arrayfunc.ne(self.nanvalue, self.testdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_num_array_a4(self):
		"""Test ne as *num-array* for NaN array - Array code d.
		"""
		expected = all([self.testvalue != x for x in self.nandata])

		result = arrayfunc.ne(self.testvalue, self.nandata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_array_a5(self):
		"""Test ne as *array-array* for NaN array 1 - Array code d.
		"""
		expected = all([x != y for (x,y) in zip(self.nandata, self.testdata)])

		result = arrayfunc.ne(self.nandata, self.testdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_array_a6(self):
		"""Test ne as *array-array* for NaN array 2 - Array code d.
		"""
		expected = all([x != y for (x,y) in zip(self.testdata, self.nandata)])

		result = arrayfunc.ne(self.testdata, self.nandata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_num_b1(self):
		"""Test ne as *array-num* for inf value - Array code d.
		"""
		expected = all([x != self.infvalue for x in self.testdata])

		result = arrayfunc.ne(self.testdata, self.infvalue)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_num_b2(self):
		"""Test ne as *array-num* for inf array - Array code d.
		"""
		expected = all([x != self.testvalue for x in self.infdata])

		result = arrayfunc.ne(self.infdata, self.testvalue)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_num_array_b3(self):
		"""Test ne as *num-array* for inf value - Array code d.
		"""
		expected = all([self.infvalue != x for x in self.testdata])

		result = arrayfunc.ne(self.infvalue, self.testdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_num_array_b4(self):
		"""Test ne as *num-array* for inf array - Array code d.
		"""
		expected = all([self.testvalue != x for x in self.infdata])

		result = arrayfunc.ne(self.testvalue, self.infdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_array_b5(self):
		"""Test ne as *array-array* for inf array 1 - Array code d.
		"""
		expected = all([x != y for (x,y) in zip(self.infdata, self.testdata)])

		result = arrayfunc.ne(self.infdata, self.testdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_array_b6(self):
		"""Test ne as *array-array* for inf array 2 - Array code d.
		"""
		expected = all([x != y for (x,y) in zip(self.testdata, self.infdata)])

		result = arrayfunc.ne(self.testdata, self.infdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_num_c1(self):
		"""Test ne as *array-num* for -inf value - Array code d.
		"""
		expected = all([x != self.ninfvalue for x in self.testdata])

		result = arrayfunc.ne(self.testdata, self.ninfvalue)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_num_c2(self):
		"""Test ne as *array-num* for -inf array - Array code d.
		"""
		expected = all([x != self.testvalue for x in self.ninfdata])

		result = arrayfunc.ne(self.ninfdata, self.testvalue)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_num_array_c3(self):
		"""Test ne as *num-array* for -inf value - Array code d.
		"""
		expected = all([self.ninfvalue != x for x in self.testdata])

		result = arrayfunc.ne(self.ninfvalue, self.testdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_num_array_c4(self):
		"""Test ne as *num-array* for -inf array - Array code d.
		"""
		expected = all([self.testvalue != x for x in self.ninfdata])

		result = arrayfunc.ne(self.testvalue, self.ninfdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_array_c5(self):
		"""Test ne as *array-array* for -inf array 1 - Array code d.
		"""
		expected = all([x != y for (x,y) in zip(self.ninfdata, self.testdata)])

		result = arrayfunc.ne(self.ninfdata, self.testdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_nan_data_array_array_c6(self):
		"""Test ne as *array-array* for -inf array 2 - Array code d.
		"""
		expected = all([x != y for (x,y) in zip(self.testdata, self.ninfdata)])

		result = arrayfunc.ne(self.testdata, self.ninfdata)

		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


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
			f.write('ne\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
