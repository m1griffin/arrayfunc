#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_count.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     05-Jun-2014.
# Ver:      06-Mar-2016.
#
###############################################################################
#
#   Copyright 2014 - 2016    Michael Griffin    <m12.griffin@gmail.com>
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
"""This conducts unit tests for count.
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



##############################################################################
class count_b(unittest.TestCase):
	"""Test for basic count function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'b'

		self.data = array.array(self.TypeCode, itertools.repeat(0, 512))

		self.MaxVal = arrayfunc.arraylimits.b_max
		self.MinVal = arrayfunc.arraylimits.b_min

		self.zerodata = array.array(self.TypeCode, [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.b_max
		self.MaxStepData = array.array(self.TypeCode, itertools.repeat(0, 6))


		# For bytes types, we need a non-array data type.
		if 'b' == 'bytes':
			self.data = bytes(self.data)
			self.zerodata = bytes(self.zerodata)
			self.MaxStepData = bytes(self.MaxStepData)


	########################################################
	def PyCount(self, data, start, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []

		val = start

		for x in range(len(data)):
			seq.append(val)
			val = val + step
			if (step >= 0) and (val > self.MaxVal):
				val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				val = (val - (self.MinVal - 1)) + self.MaxVal

		return seq


	########################################################
	def test_count_01(self):
		"""Test count in array code  b - start from 0, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 1))


	########################################################
	def test_count_02(self):
		"""Test count in array code  b - start from 10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 1))


	########################################################
	def test_count_03(self):
		"""Test count in array code  b - start from 0, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 7))


	########################################################
	def test_count_04(self):
		"""Test count in array code  b - start from 10, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 7))


	########################################################
	def test_count_05(self):
		"""Test count in array code  b - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.zerodata, 0)


	########################################################
	def test_count_06(self):
		"""Test count in array code  b - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_07(self):
		"""Test count in array code  b - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_08(self):
		"""Test count in array code  b - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_09(self):
		"""Test count in array code  b - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_10(self):
		"""Test count in array code  b - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')


	########################################################
	def test_count_11(self):
		"""Test count in array code  b - Step is maximum size.
		"""
		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)
		# Float overflow behaviour seems to be unclear, so we test for it differently.
		if 'b' in ('f', 'd'):
			self.assertTrue(float('inf') in self.MaxStepData)
		else:
			self.assertEqual(list(self.MaxStepData), self.PyCount(self.MaxStepData, 0, self.MaxStep))


	########################################################
	def test_count_12(self):
		"""Test count in array code  b - start from 10, down by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, -1)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, -1))



	########################################################
	# Signed and float only.
	def test_count_13(self):
		"""Test count in array code  b - start from -10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, -10)
		self.assertEqual(list(self.data), self.PyCount(self.data, -10, 1))


##############################################################################



##############################################################################
class count_B(unittest.TestCase):
	"""Test for basic count function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'B'

		self.data = array.array(self.TypeCode, itertools.repeat(0, 512))

		self.MaxVal = arrayfunc.arraylimits.B_max
		self.MinVal = arrayfunc.arraylimits.B_min

		self.zerodata = array.array(self.TypeCode, [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.b_max
		self.MaxStepData = array.array(self.TypeCode, itertools.repeat(0, 6))


		# For bytes types, we need a non-array data type.
		if 'B' == 'bytes':
			self.data = bytes(self.data)
			self.zerodata = bytes(self.zerodata)
			self.MaxStepData = bytes(self.MaxStepData)


	########################################################
	def PyCount(self, data, start, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []

		val = start

		for x in range(len(data)):
			seq.append(val)
			val = val + step
			if (step >= 0) and (val > self.MaxVal):
				val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				val = (val - (self.MinVal - 1)) + self.MaxVal

		return seq


	########################################################
	def test_count_01(self):
		"""Test count in array code  B - start from 0, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 1))


	########################################################
	def test_count_02(self):
		"""Test count in array code  B - start from 10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 1))


	########################################################
	def test_count_03(self):
		"""Test count in array code  B - start from 0, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 7))


	########################################################
	def test_count_04(self):
		"""Test count in array code  B - start from 10, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 7))


	########################################################
	def test_count_05(self):
		"""Test count in array code  B - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.zerodata, 0)


	########################################################
	def test_count_06(self):
		"""Test count in array code  B - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_07(self):
		"""Test count in array code  B - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_08(self):
		"""Test count in array code  B - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_09(self):
		"""Test count in array code  B - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_10(self):
		"""Test count in array code  B - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')


	########################################################
	def test_count_11(self):
		"""Test count in array code  B - Step is maximum size.
		"""
		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)
		# Float overflow behaviour seems to be unclear, so we test for it differently.
		if 'B' in ('f', 'd'):
			self.assertTrue(float('inf') in self.MaxStepData)
		else:
			self.assertEqual(list(self.MaxStepData), self.PyCount(self.MaxStepData, 0, self.MaxStep))


	########################################################
	def test_count_12(self):
		"""Test count in array code  B - start from 10, down by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, -1)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, -1))



##############################################################################



##############################################################################
class count_h(unittest.TestCase):
	"""Test for basic count function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'h'

		self.data = array.array(self.TypeCode, itertools.repeat(0, 512))

		self.MaxVal = arrayfunc.arraylimits.h_max
		self.MinVal = arrayfunc.arraylimits.h_min

		self.zerodata = array.array(self.TypeCode, [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.h_max
		self.MaxStepData = array.array(self.TypeCode, itertools.repeat(0, 6))


		# For bytes types, we need a non-array data type.
		if 'h' == 'bytes':
			self.data = bytes(self.data)
			self.zerodata = bytes(self.zerodata)
			self.MaxStepData = bytes(self.MaxStepData)


	########################################################
	def PyCount(self, data, start, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []

		val = start

		for x in range(len(data)):
			seq.append(val)
			val = val + step
			if (step >= 0) and (val > self.MaxVal):
				val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				val = (val - (self.MinVal - 1)) + self.MaxVal

		return seq


	########################################################
	def test_count_01(self):
		"""Test count in array code  h - start from 0, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 1))


	########################################################
	def test_count_02(self):
		"""Test count in array code  h - start from 10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 1))


	########################################################
	def test_count_03(self):
		"""Test count in array code  h - start from 0, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 7))


	########################################################
	def test_count_04(self):
		"""Test count in array code  h - start from 10, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 7))


	########################################################
	def test_count_05(self):
		"""Test count in array code  h - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.zerodata, 0)


	########################################################
	def test_count_06(self):
		"""Test count in array code  h - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_07(self):
		"""Test count in array code  h - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_08(self):
		"""Test count in array code  h - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_09(self):
		"""Test count in array code  h - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_10(self):
		"""Test count in array code  h - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')


	########################################################
	def test_count_11(self):
		"""Test count in array code  h - Step is maximum size.
		"""
		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)
		# Float overflow behaviour seems to be unclear, so we test for it differently.
		if 'h' in ('f', 'd'):
			self.assertTrue(float('inf') in self.MaxStepData)
		else:
			self.assertEqual(list(self.MaxStepData), self.PyCount(self.MaxStepData, 0, self.MaxStep))


	########################################################
	def test_count_12(self):
		"""Test count in array code  h - start from 10, down by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, -1)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, -1))



	########################################################
	# Signed and float only.
	def test_count_13(self):
		"""Test count in array code  h - start from -10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, -10)
		self.assertEqual(list(self.data), self.PyCount(self.data, -10, 1))


##############################################################################



##############################################################################
class count_H(unittest.TestCase):
	"""Test for basic count function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'H'

		self.data = array.array(self.TypeCode, itertools.repeat(0, 512))

		self.MaxVal = arrayfunc.arraylimits.H_max
		self.MinVal = arrayfunc.arraylimits.H_min

		self.zerodata = array.array(self.TypeCode, [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.h_max
		self.MaxStepData = array.array(self.TypeCode, itertools.repeat(0, 6))


		# For bytes types, we need a non-array data type.
		if 'H' == 'bytes':
			self.data = bytes(self.data)
			self.zerodata = bytes(self.zerodata)
			self.MaxStepData = bytes(self.MaxStepData)


	########################################################
	def PyCount(self, data, start, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []

		val = start

		for x in range(len(data)):
			seq.append(val)
			val = val + step
			if (step >= 0) and (val > self.MaxVal):
				val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				val = (val - (self.MinVal - 1)) + self.MaxVal

		return seq


	########################################################
	def test_count_01(self):
		"""Test count in array code  H - start from 0, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 1))


	########################################################
	def test_count_02(self):
		"""Test count in array code  H - start from 10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 1))


	########################################################
	def test_count_03(self):
		"""Test count in array code  H - start from 0, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 7))


	########################################################
	def test_count_04(self):
		"""Test count in array code  H - start from 10, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 7))


	########################################################
	def test_count_05(self):
		"""Test count in array code  H - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.zerodata, 0)


	########################################################
	def test_count_06(self):
		"""Test count in array code  H - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_07(self):
		"""Test count in array code  H - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_08(self):
		"""Test count in array code  H - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_09(self):
		"""Test count in array code  H - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_10(self):
		"""Test count in array code  H - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')


	########################################################
	def test_count_11(self):
		"""Test count in array code  H - Step is maximum size.
		"""
		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)
		# Float overflow behaviour seems to be unclear, so we test for it differently.
		if 'H' in ('f', 'd'):
			self.assertTrue(float('inf') in self.MaxStepData)
		else:
			self.assertEqual(list(self.MaxStepData), self.PyCount(self.MaxStepData, 0, self.MaxStep))


	########################################################
	def test_count_12(self):
		"""Test count in array code  H - start from 10, down by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, -1)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, -1))



##############################################################################



##############################################################################
class count_i(unittest.TestCase):
	"""Test for basic count function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'i'

		self.data = array.array(self.TypeCode, itertools.repeat(0, 512))

		self.MaxVal = arrayfunc.arraylimits.i_max
		self.MinVal = arrayfunc.arraylimits.i_min

		self.zerodata = array.array(self.TypeCode, [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.i_max
		self.MaxStepData = array.array(self.TypeCode, itertools.repeat(0, 6))


		# For bytes types, we need a non-array data type.
		if 'i' == 'bytes':
			self.data = bytes(self.data)
			self.zerodata = bytes(self.zerodata)
			self.MaxStepData = bytes(self.MaxStepData)


	########################################################
	def PyCount(self, data, start, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []

		val = start

		for x in range(len(data)):
			seq.append(val)
			val = val + step
			if (step >= 0) and (val > self.MaxVal):
				val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				val = (val - (self.MinVal - 1)) + self.MaxVal

		return seq


	########################################################
	def test_count_01(self):
		"""Test count in array code  i - start from 0, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 1))


	########################################################
	def test_count_02(self):
		"""Test count in array code  i - start from 10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 1))


	########################################################
	def test_count_03(self):
		"""Test count in array code  i - start from 0, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 7))


	########################################################
	def test_count_04(self):
		"""Test count in array code  i - start from 10, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 7))


	########################################################
	def test_count_05(self):
		"""Test count in array code  i - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.zerodata, 0)


	########################################################
	def test_count_06(self):
		"""Test count in array code  i - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_07(self):
		"""Test count in array code  i - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_08(self):
		"""Test count in array code  i - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_09(self):
		"""Test count in array code  i - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_10(self):
		"""Test count in array code  i - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')


	########################################################
	def test_count_11(self):
		"""Test count in array code  i - Step is maximum size.
		"""
		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)
		# Float overflow behaviour seems to be unclear, so we test for it differently.
		if 'i' in ('f', 'd'):
			self.assertTrue(float('inf') in self.MaxStepData)
		else:
			self.assertEqual(list(self.MaxStepData), self.PyCount(self.MaxStepData, 0, self.MaxStep))


	########################################################
	def test_count_12(self):
		"""Test count in array code  i - start from 10, down by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, -1)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, -1))



	########################################################
	# Signed and float only.
	def test_count_13(self):
		"""Test count in array code  i - start from -10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, -10)
		self.assertEqual(list(self.data), self.PyCount(self.data, -10, 1))


##############################################################################



##############################################################################
class count_I(unittest.TestCase):
	"""Test for basic count function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'I'

		self.data = array.array(self.TypeCode, itertools.repeat(0, 512))

		self.MaxVal = arrayfunc.arraylimits.I_max
		self.MinVal = arrayfunc.arraylimits.I_min

		self.zerodata = array.array(self.TypeCode, [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.i_max
		self.MaxStepData = array.array(self.TypeCode, itertools.repeat(0, 6))


		# For bytes types, we need a non-array data type.
		if 'I' == 'bytes':
			self.data = bytes(self.data)
			self.zerodata = bytes(self.zerodata)
			self.MaxStepData = bytes(self.MaxStepData)


	########################################################
	def PyCount(self, data, start, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []

		val = start

		for x in range(len(data)):
			seq.append(val)
			val = val + step
			if (step >= 0) and (val > self.MaxVal):
				val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				val = (val - (self.MinVal - 1)) + self.MaxVal

		return seq


	########################################################
	def test_count_01(self):
		"""Test count in array code  I - start from 0, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 1))


	########################################################
	def test_count_02(self):
		"""Test count in array code  I - start from 10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 1))


	########################################################
	def test_count_03(self):
		"""Test count in array code  I - start from 0, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 7))


	########################################################
	def test_count_04(self):
		"""Test count in array code  I - start from 10, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 7))


	########################################################
	def test_count_05(self):
		"""Test count in array code  I - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.zerodata, 0)


	########################################################
	def test_count_06(self):
		"""Test count in array code  I - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_07(self):
		"""Test count in array code  I - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_08(self):
		"""Test count in array code  I - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_09(self):
		"""Test count in array code  I - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_10(self):
		"""Test count in array code  I - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')


	########################################################
	def test_count_11(self):
		"""Test count in array code  I - Step is maximum size.
		"""
		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)
		# Float overflow behaviour seems to be unclear, so we test for it differently.
		if 'I' in ('f', 'd'):
			self.assertTrue(float('inf') in self.MaxStepData)
		else:
			self.assertEqual(list(self.MaxStepData), self.PyCount(self.MaxStepData, 0, self.MaxStep))


	########################################################
	def test_count_12(self):
		"""Test count in array code  I - start from 10, down by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, -1)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, -1))



##############################################################################



##############################################################################
class count_l(unittest.TestCase):
	"""Test for basic count function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'l'

		self.data = array.array(self.TypeCode, itertools.repeat(0, 512))

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min

		self.zerodata = array.array(self.TypeCode, [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.l_max
		self.MaxStepData = array.array(self.TypeCode, itertools.repeat(0, 6))


		# For bytes types, we need a non-array data type.
		if 'l' == 'bytes':
			self.data = bytes(self.data)
			self.zerodata = bytes(self.zerodata)
			self.MaxStepData = bytes(self.MaxStepData)


	########################################################
	def PyCount(self, data, start, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []

		val = start

		for x in range(len(data)):
			seq.append(val)
			val = val + step
			if (step >= 0) and (val > self.MaxVal):
				val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				val = (val - (self.MinVal - 1)) + self.MaxVal

		return seq


	########################################################
	def test_count_01(self):
		"""Test count in array code  l - start from 0, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 1))


	########################################################
	def test_count_02(self):
		"""Test count in array code  l - start from 10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 1))


	########################################################
	def test_count_03(self):
		"""Test count in array code  l - start from 0, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 7))


	########################################################
	def test_count_04(self):
		"""Test count in array code  l - start from 10, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 7))


	########################################################
	def test_count_05(self):
		"""Test count in array code  l - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.zerodata, 0)


	########################################################
	def test_count_06(self):
		"""Test count in array code  l - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_07(self):
		"""Test count in array code  l - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_08(self):
		"""Test count in array code  l - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_09(self):
		"""Test count in array code  l - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_10(self):
		"""Test count in array code  l - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')


	########################################################
	def test_count_11(self):
		"""Test count in array code  l - Step is maximum size.
		"""
		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)
		# Float overflow behaviour seems to be unclear, so we test for it differently.
		if 'l' in ('f', 'd'):
			self.assertTrue(float('inf') in self.MaxStepData)
		else:
			self.assertEqual(list(self.MaxStepData), self.PyCount(self.MaxStepData, 0, self.MaxStep))


	########################################################
	def test_count_12(self):
		"""Test count in array code  l - start from 10, down by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, -1)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, -1))



	########################################################
	# Signed and float only.
	def test_count_13(self):
		"""Test count in array code  l - start from -10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, -10)
		self.assertEqual(list(self.data), self.PyCount(self.data, -10, 1))


##############################################################################



##############################################################################
class count_L(unittest.TestCase):
	"""Test for basic count function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'L'

		self.data = array.array(self.TypeCode, itertools.repeat(0, 512))

		self.MaxVal = arrayfunc.arraylimits.L_max
		self.MinVal = arrayfunc.arraylimits.L_min

		self.zerodata = array.array(self.TypeCode, [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.l_max
		self.MaxStepData = array.array(self.TypeCode, itertools.repeat(0, 6))


		# For bytes types, we need a non-array data type.
		if 'L' == 'bytes':
			self.data = bytes(self.data)
			self.zerodata = bytes(self.zerodata)
			self.MaxStepData = bytes(self.MaxStepData)


	########################################################
	def PyCount(self, data, start, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []

		val = start

		for x in range(len(data)):
			seq.append(val)
			val = val + step
			if (step >= 0) and (val > self.MaxVal):
				val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				val = (val - (self.MinVal - 1)) + self.MaxVal

		return seq


	########################################################
	def test_count_01(self):
		"""Test count in array code  L - start from 0, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 1))


	########################################################
	def test_count_02(self):
		"""Test count in array code  L - start from 10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 1))


	########################################################
	def test_count_03(self):
		"""Test count in array code  L - start from 0, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 7))


	########################################################
	def test_count_04(self):
		"""Test count in array code  L - start from 10, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 7))


	########################################################
	def test_count_05(self):
		"""Test count in array code  L - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.zerodata, 0)


	########################################################
	def test_count_06(self):
		"""Test count in array code  L - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_07(self):
		"""Test count in array code  L - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_08(self):
		"""Test count in array code  L - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_09(self):
		"""Test count in array code  L - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_10(self):
		"""Test count in array code  L - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')


	########################################################
	def test_count_11(self):
		"""Test count in array code  L - Step is maximum size.
		"""
		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)
		# Float overflow behaviour seems to be unclear, so we test for it differently.
		if 'L' in ('f', 'd'):
			self.assertTrue(float('inf') in self.MaxStepData)
		else:
			self.assertEqual(list(self.MaxStepData), self.PyCount(self.MaxStepData, 0, self.MaxStep))


	########################################################
	def test_count_12(self):
		"""Test count in array code  L - start from 10, down by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, -1)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, -1))



##############################################################################



##############################################################################
# Cannot test if 'q' or 'Q' arrays are not supported in this architecture.
@unittest.skipIf('q' not in array.typecodes, 'Skip test if array type not supported on this platform.')
class count_q(unittest.TestCase):
	"""Test for basic count function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'q'

		self.data = array.array(self.TypeCode, itertools.repeat(0, 512))

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min

		self.zerodata = array.array(self.TypeCode, [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.q_max
		self.MaxStepData = array.array(self.TypeCode, itertools.repeat(0, 6))


		# For bytes types, we need a non-array data type.
		if 'q' == 'bytes':
			self.data = bytes(self.data)
			self.zerodata = bytes(self.zerodata)
			self.MaxStepData = bytes(self.MaxStepData)


	########################################################
	def PyCount(self, data, start, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []

		val = start

		for x in range(len(data)):
			seq.append(val)
			val = val + step
			if (step >= 0) and (val > self.MaxVal):
				val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				val = (val - (self.MinVal - 1)) + self.MaxVal

		return seq


	########################################################
	def test_count_01(self):
		"""Test count in array code  q - start from 0, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 1))


	########################################################
	def test_count_02(self):
		"""Test count in array code  q - start from 10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 1))


	########################################################
	def test_count_03(self):
		"""Test count in array code  q - start from 0, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 7))


	########################################################
	def test_count_04(self):
		"""Test count in array code  q - start from 10, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 7))


	########################################################
	def test_count_05(self):
		"""Test count in array code  q - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.zerodata, 0)


	########################################################
	def test_count_06(self):
		"""Test count in array code  q - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_07(self):
		"""Test count in array code  q - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_08(self):
		"""Test count in array code  q - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_09(self):
		"""Test count in array code  q - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_10(self):
		"""Test count in array code  q - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')


	########################################################
	def test_count_11(self):
		"""Test count in array code  q - Step is maximum size.
		"""
		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)
		# Float overflow behaviour seems to be unclear, so we test for it differently.
		if 'q' in ('f', 'd'):
			self.assertTrue(float('inf') in self.MaxStepData)
		else:
			self.assertEqual(list(self.MaxStepData), self.PyCount(self.MaxStepData, 0, self.MaxStep))


	########################################################
	def test_count_12(self):
		"""Test count in array code  q - start from 10, down by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, -1)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, -1))



	########################################################
	# Signed and float only.
	def test_count_13(self):
		"""Test count in array code  q - start from -10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, -10)
		self.assertEqual(list(self.data), self.PyCount(self.data, -10, 1))


##############################################################################



##############################################################################
# Cannot test if 'q' or 'Q' arrays are not supported in this architecture.
@unittest.skipIf('Q' not in array.typecodes, 'Skip test if array type not supported on this platform.')
class count_Q(unittest.TestCase):
	"""Test for basic count function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'Q'

		self.data = array.array(self.TypeCode, itertools.repeat(0, 512))

		self.MaxVal = arrayfunc.arraylimits.Q_max
		self.MinVal = arrayfunc.arraylimits.Q_min

		self.zerodata = array.array(self.TypeCode, [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.q_max
		self.MaxStepData = array.array(self.TypeCode, itertools.repeat(0, 6))


		# For bytes types, we need a non-array data type.
		if 'Q' == 'bytes':
			self.data = bytes(self.data)
			self.zerodata = bytes(self.zerodata)
			self.MaxStepData = bytes(self.MaxStepData)


	########################################################
	def PyCount(self, data, start, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []

		val = start

		for x in range(len(data)):
			seq.append(val)
			val = val + step
			if (step >= 0) and (val > self.MaxVal):
				val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				val = (val - (self.MinVal - 1)) + self.MaxVal

		return seq


	########################################################
	def test_count_01(self):
		"""Test count in array code  Q - start from 0, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 1))


	########################################################
	def test_count_02(self):
		"""Test count in array code  Q - start from 10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 1))


	########################################################
	def test_count_03(self):
		"""Test count in array code  Q - start from 0, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 7))


	########################################################
	def test_count_04(self):
		"""Test count in array code  Q - start from 10, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 7))


	########################################################
	def test_count_05(self):
		"""Test count in array code  Q - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.zerodata, 0)


	########################################################
	def test_count_06(self):
		"""Test count in array code  Q - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_07(self):
		"""Test count in array code  Q - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_08(self):
		"""Test count in array code  Q - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_09(self):
		"""Test count in array code  Q - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_10(self):
		"""Test count in array code  Q - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')


	########################################################
	def test_count_11(self):
		"""Test count in array code  Q - Step is maximum size.
		"""
		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)
		# Float overflow behaviour seems to be unclear, so we test for it differently.
		if 'Q' in ('f', 'd'):
			self.assertTrue(float('inf') in self.MaxStepData)
		else:
			self.assertEqual(list(self.MaxStepData), self.PyCount(self.MaxStepData, 0, self.MaxStep))


	########################################################
	def test_count_12(self):
		"""Test count in array code  Q - start from 10, down by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, -1)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, -1))



##############################################################################



##############################################################################
class count_f(unittest.TestCase):
	"""Test for basic count function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'f'

		self.data = array.array(self.TypeCode, itertools.repeat(0.0, 512))

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min

		self.zerodata = array.array(self.TypeCode, [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.f_max
		self.MaxStepData = array.array(self.TypeCode, itertools.repeat(0.0, 6))


		# For bytes types, we need a non-array data type.
		if 'f' == 'bytes':
			self.data = bytes(self.data)
			self.zerodata = bytes(self.zerodata)
			self.MaxStepData = bytes(self.MaxStepData)


	########################################################
	def PyCount(self, data, start, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []

		val = start

		for x in range(len(data)):
			seq.append(val)
			val = val + step
			if (step >= 0) and (val > self.MaxVal):
				val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				val = (val - (self.MinVal - 1)) + self.MaxVal

		return seq


	########################################################
	def test_count_01(self):
		"""Test count in array code  f - start from 0, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0.0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0.0, 1.0))


	########################################################
	def test_count_02(self):
		"""Test count in array code  f - start from 10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10.0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10.0, 1.0))


	########################################################
	def test_count_03(self):
		"""Test count in array code  f - start from 0, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0.0, 7.0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0.0, 7.0))


	########################################################
	def test_count_04(self):
		"""Test count in array code  f - start from 10, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10.0, 7.0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10.0, 7.0))


	########################################################
	def test_count_05(self):
		"""Test count in array code  f - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.zerodata, 0.0)


	########################################################
	def test_count_06(self):
		"""Test count in array code  f - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_07(self):
		"""Test count in array code  f - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0.0, 1.0, 1.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_08(self):
		"""Test count in array code  f - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0.0, 1.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_09(self):
		"""Test count in array code  f - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_10(self):
		"""Test count in array code  f - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0.0, 'a')


	########################################################
	def test_count_11(self):
		"""Test count in array code  f - Step is maximum size.
		"""
		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0.0, self.MaxStep)
		# Float overflow behaviour seems to be unclear, so we test for it differently.
		if 'f' in ('f', 'd'):
			self.assertTrue(float('inf') in self.MaxStepData)
		else:
			self.assertEqual(list(self.MaxStepData), self.PyCount(self.MaxStepData, 0.0, self.MaxStep))


	########################################################
	def test_count_12(self):
		"""Test count in array code  f - start from 10, down by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10.0, -1.0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10.0, -1.0))



	########################################################
	# Signed and float only.
	def test_count_13(self):
		"""Test count in array code  f - start from -10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, -10.0)
		self.assertEqual(list(self.data), self.PyCount(self.data, -10.0, 1.0))


	########################################################
	# Floating point only.
	def test_count_14(self):
		"""Test count in array code  f - start from 0, count up by a small increment.
		"""
		arrayfunc.count(self.data, 0.0, 0.1)
		for x,y in zip(self.data, self.PyCount(self.data, 0.0, 0.1)):
			self.assertAlmostEqual(x, y, delta=0.01)


	########################################################
	# Floating point only.
	def test_count_15(self):
		"""Test count in array code  f - Invalid param nan for start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, float('nan'), 1.0)


	########################################################
	# Floating point only.
	def test_count_16(self):
		"""Test count in array code  f - Invalid param inf for start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, float('inf'), 1.0)


	########################################################
	# Floating point only.
	def test_count_17(self):
		"""Test count in array code  f - Invalid param -inf for start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, float('-inf'), 1.0)


	########################################################
	# Floating point only.
	def test_count_18(self):
		"""Test count in array code  f - Invalid param nan for step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0.0, float('nan'))


	########################################################
	# Floating point only.
	def test_count_19(self):
		"""Test count in array code  f - Invalid param inf for step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0.0, float('inf'))


	########################################################
	# Floating point only.
	def test_count_20(self):
		"""Test count in array code  f - Invalid param -inf for step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0.0, float('-inf'))


##############################################################################



##############################################################################
class count_d(unittest.TestCase):
	"""Test for basic count function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'd'

		self.data = array.array(self.TypeCode, itertools.repeat(0.0, 512))

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min

		self.zerodata = array.array(self.TypeCode, [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.d_max
		self.MaxStepData = array.array(self.TypeCode, itertools.repeat(0.0, 6))


		# For bytes types, we need a non-array data type.
		if 'd' == 'bytes':
			self.data = bytes(self.data)
			self.zerodata = bytes(self.zerodata)
			self.MaxStepData = bytes(self.MaxStepData)


	########################################################
	def PyCount(self, data, start, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []

		val = start

		for x in range(len(data)):
			seq.append(val)
			val = val + step
			if (step >= 0) and (val > self.MaxVal):
				val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				val = (val - (self.MinVal - 1)) + self.MaxVal

		return seq


	########################################################
	def test_count_01(self):
		"""Test count in array code  d - start from 0, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0.0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0.0, 1.0))


	########################################################
	def test_count_02(self):
		"""Test count in array code  d - start from 10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10.0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10.0, 1.0))


	########################################################
	def test_count_03(self):
		"""Test count in array code  d - start from 0, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0.0, 7.0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0.0, 7.0))


	########################################################
	def test_count_04(self):
		"""Test count in array code  d - start from 10, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10.0, 7.0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10.0, 7.0))


	########################################################
	def test_count_05(self):
		"""Test count in array code  d - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.zerodata, 0.0)


	########################################################
	def test_count_06(self):
		"""Test count in array code  d - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_07(self):
		"""Test count in array code  d - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0.0, 1.0, 1.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_08(self):
		"""Test count in array code  d - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0.0, 1.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_09(self):
		"""Test count in array code  d - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_10(self):
		"""Test count in array code  d - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0.0, 'a')


	########################################################
	def test_count_11(self):
		"""Test count in array code  d - Step is maximum size.
		"""
		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0.0, self.MaxStep)
		# Float overflow behaviour seems to be unclear, so we test for it differently.
		if 'd' in ('f', 'd'):
			self.assertTrue(float('inf') in self.MaxStepData)
		else:
			self.assertEqual(list(self.MaxStepData), self.PyCount(self.MaxStepData, 0.0, self.MaxStep))


	########################################################
	def test_count_12(self):
		"""Test count in array code  d - start from 10, down by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10.0, -1.0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10.0, -1.0))



	########################################################
	# Signed and float only.
	def test_count_13(self):
		"""Test count in array code  d - start from -10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, -10.0)
		self.assertEqual(list(self.data), self.PyCount(self.data, -10.0, 1.0))


	########################################################
	# Floating point only.
	def test_count_14(self):
		"""Test count in array code  d - start from 0, count up by a small increment.
		"""
		arrayfunc.count(self.data, 0.0, 0.1)
		for x,y in zip(self.data, self.PyCount(self.data, 0.0, 0.1)):
			self.assertAlmostEqual(x, y, delta=0.01)


	########################################################
	# Floating point only.
	def test_count_15(self):
		"""Test count in array code  d - Invalid param nan for start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, float('nan'), 1.0)


	########################################################
	# Floating point only.
	def test_count_16(self):
		"""Test count in array code  d - Invalid param inf for start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, float('inf'), 1.0)


	########################################################
	# Floating point only.
	def test_count_17(self):
		"""Test count in array code  d - Invalid param -inf for start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, float('-inf'), 1.0)


	########################################################
	# Floating point only.
	def test_count_18(self):
		"""Test count in array code  d - Invalid param nan for step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0.0, float('nan'))


	########################################################
	# Floating point only.
	def test_count_19(self):
		"""Test count in array code  d - Invalid param inf for step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0.0, float('inf'))


	########################################################
	# Floating point only.
	def test_count_20(self):
		"""Test count in array code  d - Invalid param -inf for step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0.0, float('-inf'))


##############################################################################



##############################################################################
class count_bytes(unittest.TestCase):
	"""Test for basic count function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'B'

		self.data = array.array(self.TypeCode, itertools.repeat(0, 512))

		self.MaxVal = arrayfunc.arraylimits.B_max
		self.MinVal = arrayfunc.arraylimits.B_min

		self.zerodata = array.array(self.TypeCode, [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.b_max
		self.MaxStepData = array.array(self.TypeCode, itertools.repeat(0, 6))


		# For bytes types, we need a non-array data type.
		if 'bytes' == 'bytes':
			self.data = bytes(self.data)
			self.zerodata = bytes(self.zerodata)
			self.MaxStepData = bytes(self.MaxStepData)


	########################################################
	def PyCount(self, data, start, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []

		val = start

		for x in range(len(data)):
			seq.append(val)
			val = val + step
			if (step >= 0) and (val > self.MaxVal):
				val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				val = (val - (self.MinVal - 1)) + self.MaxVal

		return seq


	########################################################
	def test_count_01(self):
		"""Test count in array code  bytes - start from 0, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 1))


	########################################################
	def test_count_02(self):
		"""Test count in array code  bytes - start from 10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 1))


	########################################################
	def test_count_03(self):
		"""Test count in array code  bytes - start from 0, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 0, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 0, 7))


	########################################################
	def test_count_04(self):
		"""Test count in array code  bytes - start from 10, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, 7)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, 7))


	########################################################
	def test_count_05(self):
		"""Test count in array code  bytes - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.zerodata, 0)


	########################################################
	def test_count_06(self):
		"""Test count in array code  bytes - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_07(self):
		"""Test count in array code  bytes - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_08(self):
		"""Test count in array code  bytes - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_09(self):
		"""Test count in array code  bytes - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_10(self):
		"""Test count in array code  bytes - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')


	########################################################
	def test_count_11(self):
		"""Test count in array code  bytes - Step is maximum size.
		"""
		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)
		# Float overflow behaviour seems to be unclear, so we test for it differently.
		if 'B' in ('f', 'd'):
			self.assertTrue(float('inf') in self.MaxStepData)
		else:
			self.assertEqual(list(self.MaxStepData), self.PyCount(self.MaxStepData, 0, self.MaxStep))


	########################################################
	def test_count_12(self):
		"""Test count in array code  bytes - start from 10, down by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, 10, -1)
		self.assertEqual(list(self.data), self.PyCount(self.data, 10, -1))



##############################################################################
if __name__ == '__main__':
    unittest.main()

##############################################################################
