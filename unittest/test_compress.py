#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_compress.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     11-Jun-2014.
# Ver:      28-May-2018.
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
"""This conducts unit tests for compress.
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
class compress_int_b(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'b'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(6, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0, 1], 24)))



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [5] * (len(tmpdata) - len(result))
		else:
			pad = [6] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  b - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  b - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  b - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  b - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  b - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) // 4))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  b - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) * 2))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  b - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  b - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  b - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  b - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  b - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  b - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  b - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  b - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))


##############################################################################



##############################################################################
class compress_int_B(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'B'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(6, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0, 1], 24)))



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [5] * (len(tmpdata) - len(result))
		else:
			pad = [6] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  B - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  B - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  B - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  B - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  B - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) // 4))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  B - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) * 2))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  B - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  B - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  B - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  B - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  B - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  B - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  B - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  B - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))


##############################################################################



##############################################################################
class compress_int_h(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'h'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(6, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0, 1], 24)))



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [5] * (len(tmpdata) - len(result))
		else:
			pad = [6] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  h - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  h - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  h - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  h - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  h - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) // 4))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  h - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) * 2))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  h - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  h - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  h - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  h - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  h - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  h - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  h - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  h - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))


##############################################################################



##############################################################################
class compress_int_H(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'H'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(6, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0, 1], 24)))



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [5] * (len(tmpdata) - len(result))
		else:
			pad = [6] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  H - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  H - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  H - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  H - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  H - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) // 4))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  H - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) * 2))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  H - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  H - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  H - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  H - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  H - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  H - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  H - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  H - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))


##############################################################################



##############################################################################
class compress_int_i(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'i'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(6, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0, 1], 24)))



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [5] * (len(tmpdata) - len(result))
		else:
			pad = [6] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  i - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  i - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  i - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  i - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  i - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) // 4))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  i - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) * 2))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  i - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  i - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  i - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  i - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  i - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  i - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  i - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  i - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))


##############################################################################



##############################################################################
class compress_int_I(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'I'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(6, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0, 1], 24)))



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [5] * (len(tmpdata) - len(result))
		else:
			pad = [6] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  I - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  I - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  I - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  I - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  I - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) // 4))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  I - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) * 2))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  I - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  I - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  I - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  I - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  I - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  I - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  I - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  I - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))


##############################################################################



##############################################################################
class compress_int_l(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'l'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(6, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0, 1], 24)))



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [5] * (len(tmpdata) - len(result))
		else:
			pad = [6] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  l - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  l - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  l - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  l - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  l - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) // 4))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  l - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) * 2))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  l - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  l - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  l - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  l - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  l - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  l - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  l - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  l - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))


##############################################################################



##############################################################################
class compress_int_L(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'L'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(6, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0, 1], 24)))



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [5] * (len(tmpdata) - len(result))
		else:
			pad = [6] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  L - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  L - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  L - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  L - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  L - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) // 4))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  L - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) * 2))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  L - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  L - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  L - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  L - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  L - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  L - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  L - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  L - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))


##############################################################################



##############################################################################
class compress_int_q(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'q'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(6, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0, 1], 24)))



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [5] * (len(tmpdata) - len(result))
		else:
			pad = [6] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  q - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  q - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  q - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  q - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  q - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) // 4))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  q - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) * 2))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  q - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  q - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  q - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  q - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  q - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  q - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  q - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  q - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))


##############################################################################



##############################################################################
class compress_int_Q(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'Q'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(6, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0, 1], 24)))



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [5] * (len(tmpdata) - len(result))
		else:
			pad = [6] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  Q - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  Q - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  Q - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  Q - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  Q - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) // 4))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  Q - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6, len(self.data) * 2))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  Q - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  Q - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  Q - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  Q - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  Q - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  Q - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  Q - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  Q - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))


##############################################################################



##############################################################################
class compress_float_f(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'f'

		self.data = array.array(self.TypeCode, itertools.repeat(5.5, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(6.6, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0, 1.1], 24)))



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [5.5] * (len(tmpdata) - len(result))
		else:
			pad = [6.6] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  f - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  f - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  f - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  f - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.1], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  f - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6.6, len(self.data) // 4))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  f - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6.6, len(self.data) * 2))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  f - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  f - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  f - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  f - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  f - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  f - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  f - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  f - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))


##############################################################################



##############################################################################
class compress_float_d(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'd'

		self.data = array.array(self.TypeCode, itertools.repeat(5.5, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(6.6, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0, 1.1], 24)))



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [5.5] * (len(tmpdata) - len(result))
		else:
			pad = [6.6] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  d - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  d - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  d - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  d - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.1], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  d - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6.6, len(self.data) // 4))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  d - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6.6, len(self.data) * 2))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  d - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  d - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  d - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  d - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  d - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  d - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  d - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  d - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))


##############################################################################



##############################################################################



##############################################################################
class compress_nan_f(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'f'

		self.data = array.array(self.TypeCode, itertools.repeat(float('nan'), 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(6.6, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0, 1.1], 24)))



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [float('nan')] * (len(tmpdata) - len(result))
		else:
			pad = [6.6] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  f - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  f - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  f - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  f - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.1], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  f - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6.6, len(self.data) // 4))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  f - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6.6, len(self.data) * 2))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  f - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  f - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  f - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  f - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  f - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  f - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  f - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  f - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))


##############################################################################



##############################################################################
class compress_inf_f(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'f'

		self.data = array.array(self.TypeCode, itertools.repeat(float('inf'), 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(6.6, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0, 1.1], 24)))



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [float('inf')] * (len(tmpdata) - len(result))
		else:
			pad = [6.6] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  f - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  f - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  f - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  f - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.1], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  f - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6.6, len(self.data) // 4))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  f - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6.6, len(self.data) * 2))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  f - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  f - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  f - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  f - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  f - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  f - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  f - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  f - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))


##############################################################################



##############################################################################
class compress_ninf_f(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'f'

		self.data = array.array(self.TypeCode, itertools.repeat(float('-inf'), 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(6.6, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0, 1.1], 24)))



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [float('-inf')] * (len(tmpdata) - len(result))
		else:
			pad = [6.6] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  f - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  f - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  f - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  f - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.1], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  f - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6.6, len(self.data) // 4))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  f - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6.6, len(self.data) * 2))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  f - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  f - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  f - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  f - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  f - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  f - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  f - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  f - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))


##############################################################################



##############################################################################
class compress_nan_d(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'd'

		self.data = array.array(self.TypeCode, itertools.repeat(float('nan'), 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(6.6, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0, 1.1], 24)))



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [float('nan')] * (len(tmpdata) - len(result))
		else:
			pad = [6.6] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  d - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  d - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  d - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  d - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.1], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  d - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6.6, len(self.data) // 4))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  d - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6.6, len(self.data) * 2))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  d - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  d - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  d - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  d - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  d - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  d - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  d - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  d - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))


##############################################################################



##############################################################################
class compress_inf_d(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'd'

		self.data = array.array(self.TypeCode, itertools.repeat(float('inf'), 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(6.6, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0, 1.1], 24)))



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [float('inf')] * (len(tmpdata) - len(result))
		else:
			pad = [6.6] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  d - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  d - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  d - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  d - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.1], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  d - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6.6, len(self.data) // 4))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  d - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6.6, len(self.data) * 2))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  d - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  d - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  d - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  d - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  d - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  d - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  d - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  d - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))


##############################################################################



##############################################################################
class compress_ninf_d(unittest.TestCase):
	"""Test for basic compress function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'd'

		self.data = array.array(self.TypeCode, itertools.repeat(float('-inf'), 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(6.6, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0, 1.1], 24)))



	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		result = []
		selindex = 0

		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		for x in tmpdata:
			if selector[selindex]:
				result.append(x)
			selindex += 1
			if selindex >= len(selector):
				selindex = 0
			if len(result) >= len(dataout):
				return result, len(result)
		if len(tmpdata) > len(dataout):
			pad = [float('-inf')] * (len(tmpdata) - len(result))
		else:
			pad = [6.6] * (len(dataout) - len(result))

		paddedresult = result + pad
		return (paddedresult, len(result))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  d - Test for basic function.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  d - General test with array limit applied.
		"""
		ccount = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Floating point needs special handling to account for floating point imprecision.
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  d - Test for zero filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  d - Test for one filled selector.
		"""
		selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.1], 24)))

		ccount = arrayfunc.compress(self.data, self.dataout, selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(self.dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(self.dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  d - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6.6, len(self.data) // 4))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  d - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(6.6, len(self.data) * 2))

		ccount = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)
		if self.TypeCode in ('f', 'd'):
			for dataoutitem, expecteditem in zip(list(dataout), expected):
				if math.isnan(dataoutitem) or math.isnan(expecteditem):
					self.assertEqual(math.isnan(dataoutitem), math.isnan(expecteditem))
				else:
					deltaval = min((abs(dataoutitem), abs(expecteditem))) / 100.0
					self.assertAlmostEqual(dataoutitem, expecteditem, delta=deltaval)
		else:
			self.assertEqual(list(dataout), expected)
		self.assertEqual(ccount, expectedlen)


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  d - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))

	########################################################
	def test_compress_08(self):
		"""Test compress in array code  d - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_09(self):
		"""Test compress in array code  d - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_10(self):
		"""Test compress in array code  d - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_11(self):
		"""Test compress in array code  d - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_12(self):
		"""Test compress in array code  d - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_13(self):
		"""Test compress in array code  d - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_14(self):
		"""Test compress in array code  d - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))


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
			f.write('compress\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
