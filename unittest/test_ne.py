#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_ne.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     14-Feb-2018.
# Ver:      01-Jul-2019.
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
class ne_general_even_arraysize_with_simd_b(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('b', xdata)
		self.data2 = array.array('b', ydata)
		self.data2fail = array.array('b', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code b.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code b.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_with_simd_b(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('b', xdata)
		self.data2 = array.array('b', ydata)
		self.data2fail = array.array('b', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code b.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code b.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_without_simd_b(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('b', xdata)
		self.data2 = array.array('b', ydata)
		self.data2fail = array.array('b', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code b.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code b.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code b.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code b.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail , nosimd=True)

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code b.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited , nosimd=True)

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
class ne_general_even_arraysize_with_simd_B(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('B', xdata)
		self.data2 = array.array('B', ydata)
		self.data2fail = array.array('B', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code B.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code B.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_with_simd_B(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('B', xdata)
		self.data2 = array.array('B', ydata)
		self.data2fail = array.array('B', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code B.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code B.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_without_simd_B(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('B', xdata)
		self.data2 = array.array('B', ydata)
		self.data2fail = array.array('B', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code B.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code B.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code B.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code B.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail , nosimd=True)

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code B.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


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
class ne_general_even_arraysize_with_simd_h(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('h', xdata)
		self.data2 = array.array('h', ydata)
		self.data2fail = array.array('h', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code h.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code h.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_with_simd_h(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('h', xdata)
		self.data2 = array.array('h', ydata)
		self.data2fail = array.array('h', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code h.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code h.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_without_simd_h(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('h', xdata)
		self.data2 = array.array('h', ydata)
		self.data2fail = array.array('h', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code h.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code h.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code h.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code h.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail , nosimd=True)

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code h.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


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
class ne_general_even_arraysize_with_simd_H(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('H', xdata)
		self.data2 = array.array('H', ydata)
		self.data2fail = array.array('H', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code H.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code H.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_with_simd_H(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('H', xdata)
		self.data2 = array.array('H', ydata)
		self.data2fail = array.array('H', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code H.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code H.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_without_simd_H(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('H', xdata)
		self.data2 = array.array('H', ydata)
		self.data2fail = array.array('H', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code H.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code H.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code H.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code H.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail , nosimd=True)

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code H.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


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
class ne_general_even_arraysize_with_simd_i(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('i', xdata)
		self.data2 = array.array('i', ydata)
		self.data2fail = array.array('i', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code i.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code i.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_with_simd_i(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('i', xdata)
		self.data2 = array.array('i', ydata)
		self.data2fail = array.array('i', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code i.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code i.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_without_simd_i(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('i', xdata)
		self.data2 = array.array('i', ydata)
		self.data2fail = array.array('i', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code i.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code i.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code i.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code i.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail , nosimd=True)

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code i.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


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
class ne_general_even_arraysize_with_simd_I(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('I', xdata)
		self.data2 = array.array('I', ydata)
		self.data2fail = array.array('I', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code I.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code I.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_with_simd_I(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('I', xdata)
		self.data2 = array.array('I', ydata)
		self.data2fail = array.array('I', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code I.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code I.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_without_simd_I(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('I', xdata)
		self.data2 = array.array('I', ydata)
		self.data2fail = array.array('I', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code I.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code I.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code I.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code I.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail , nosimd=True)

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code I.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


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
class ne_general_even_arraysize_with_simd_l(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('l', xdata)
		self.data2 = array.array('l', ydata)
		self.data2fail = array.array('l', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code l.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code l.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_with_simd_l(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('l', xdata)
		self.data2 = array.array('l', ydata)
		self.data2fail = array.array('l', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code l.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code l.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_without_simd_l(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('l', xdata)
		self.data2 = array.array('l', ydata)
		self.data2fail = array.array('l', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code l.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code l.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code l.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code l.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail , nosimd=True)

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code l.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


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
class ne_general_even_arraysize_with_simd_L(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('L', xdata)
		self.data2 = array.array('L', ydata)
		self.data2fail = array.array('L', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code L.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code L.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_with_simd_L(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('L', xdata)
		self.data2 = array.array('L', ydata)
		self.data2fail = array.array('L', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code L.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code L.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_without_simd_L(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('L', xdata)
		self.data2 = array.array('L', ydata)
		self.data2fail = array.array('L', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code L.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code L.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code L.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code L.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail , nosimd=True)

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code L.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


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
class ne_general_even_arraysize_with_simd_q(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('q', xdata)
		self.data2 = array.array('q', ydata)
		self.data2fail = array.array('q', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code q.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_with_simd_q(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('q', xdata)
		self.data2 = array.array('q', ydata)
		self.data2fail = array.array('q', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code q.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_without_simd_q(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('q', xdata)
		self.data2 = array.array('q', ydata)
		self.data2fail = array.array('q', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code q.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code q.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail , nosimd=True)

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code q.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


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
class ne_general_even_arraysize_with_simd_Q(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('Q', xdata)
		self.data2 = array.array('Q', ydata)
		self.data2fail = array.array('Q', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code Q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code Q.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_with_simd_Q(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('Q', xdata)
		self.data2 = array.array('Q', ydata)
		self.data2fail = array.array('Q', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code Q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code Q.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_without_simd_Q(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]), range(testdatasize))]

		self.data1 = array.array('Q', xdata)
		self.data2 = array.array('Q', ydata)
		self.data2fail = array.array('Q', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code Q.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code Q.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code Q.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code Q.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail , nosimd=True)

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code Q.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


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
class ne_general_even_arraysize_with_simd_f(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0]), range(testdatasize))]

		self.data1 = array.array('f', xdata)
		self.data2 = array.array('f', ydata)
		self.data2fail = array.array('f', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code f.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code f.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code f.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_with_simd_f(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0]), range(testdatasize))]

		self.data1 = array.array('f', xdata)
		self.data2 = array.array('f', ydata)
		self.data2fail = array.array('f', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code f.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code f.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code f.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_without_simd_f(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0]), range(testdatasize))]

		self.data1 = array.array('f', xdata)
		self.data2 = array.array('f', ydata)
		self.data2fail = array.array('f', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code f.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code f.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code f.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code f.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code f.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail , nosimd=True)

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code f.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


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
class ne_general_even_arraysize_with_simd_d(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0]), range(testdatasize))]

		self.data1 = array.array('d', xdata)
		self.data2 = array.array('d', ydata)
		self.data2fail = array.array('d', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code d.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code d.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code d.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_odd_arraysize_with_simd_d(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'odd' == 'even':
			testdatasize = 160
		if 'odd' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0]), range(testdatasize))]

		self.data1 = array.array('d', xdata)
		self.data2 = array.array('d', ydata)
		self.data2fail = array.array('d', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code d.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail )

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code d.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited )

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail )

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code d.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited )

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


##############################################################################

 

##############################################################################
class ne_general_even_arraysize_without_simd_d(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data 6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0.
	test_template_comp
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if 'even' == 'even':
			testdatasize = 160
		if 'even' == 'odd':
			testdatasize = 159
		paramitersize = 5

		xdata = [x for x,y in zip(itertools.cycle([5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0,6.0]), range(testdatasize))]
		ydatafail = [x for x,y in zip(itertools.cycle([5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0]), range(testdatasize))]

		self.data1 = array.array('d', xdata)
		self.data2 = array.array('d', ydata)
		self.data2fail = array.array('d', ydatafail)

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]
		self.data2failparam = self.data2fail[:paramitersize]


	########################################################
	def test_ne_basic_array_num_a1(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a2(self):
		"""Test ne as *array-num* for basic function - Array code d.
		"""
		for testval in self.data2failparam:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([x != testval for x in self.data1])

				result = arrayfunc.ne(self.data1, testval , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_num_a3(self):
		"""Test ne as *array-num* for basic function with array limit - Array code d.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([x != testval for x in self.data1[0:limited]])

				result = arrayfunc.ne(self.data1, testval, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b1(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2])

				result = arrayfunc.ne(testval, self.data2 , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b2(self):
		"""Test ne as *num-array* for basic function - Array code d.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = all([testval != x for x in self.data2fail])

				result = arrayfunc.ne(testval, self.data2fail , nosimd=True)

				self.assertFalse(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_num_array_b3(self):
		"""Test ne as *num-array* for basic function with array limit - Array code d.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				limited = len(self.data1) // 2

				expected = all([testval != x for x in self.data2[0:limited]])

				result = arrayfunc.ne(testval, self.data2, maxlen=limited , nosimd=True)

				self.assertTrue(result)
				self.assertIsInstance(result, bool)
				self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c1(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2)])
		result = arrayfunc.ne(self.data1, self.data2 , nosimd=True)

		self.assertTrue(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c2(self):
		"""Test ne as *array-array* for basic function - Array code d.
		"""
		expected = all([x != y for (x, y) in zip(self.data1, self.data2fail)])
		result = arrayfunc.ne(self.data1, self.data2fail , nosimd=True)

		self.assertFalse(result)
		self.assertIsInstance(result, bool)
		self.assertEqual(expected, result)


	########################################################
	def test_ne_basic_array_array_c3(self):
		"""Test ne as *array-array* for basic function with array limit - Array code d.
		"""
		limited = len(self.data1) // 2

		expected = all([x != y for (x, y) in zip(self.data1[0:limited], self.data2[0:limited])])

		result = arrayfunc.ne(self.data1, self.data2, maxlen=limited , nosimd=True)

		self.assertTrue(result)
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
