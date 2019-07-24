#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_compress.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     11-Jun-2014.
# Ver:      27-Jun-2019.
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
class compress_finite_finite_b(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'b'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  b finite finite - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  b finite finite - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  b finite finite - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  b finite finite - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  b finite finite - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  b finite finite - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_params_b(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'b'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  b - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  b - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  b - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  b - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  b - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  b - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  b - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_08(self):
		"""Test compress in array code  b - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))



##############################################################################


##############################################################################
class compress_finite_finite_B(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'B'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  B finite finite - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  B finite finite - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  B finite finite - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  B finite finite - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  B finite finite - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  B finite finite - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_params_B(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'B'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  B - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  B - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  B - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  B - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  B - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  B - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  B - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_08(self):
		"""Test compress in array code  B - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))



##############################################################################


##############################################################################
class compress_finite_finite_h(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'h'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  h finite finite - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  h finite finite - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  h finite finite - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  h finite finite - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  h finite finite - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  h finite finite - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_params_h(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'h'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  h - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  h - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  h - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  h - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  h - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  h - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  h - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_08(self):
		"""Test compress in array code  h - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))



##############################################################################


##############################################################################
class compress_finite_finite_H(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'H'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  H finite finite - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  H finite finite - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  H finite finite - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  H finite finite - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  H finite finite - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  H finite finite - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_params_H(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'H'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  H - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  H - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  H - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  H - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  H - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  H - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  H - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_08(self):
		"""Test compress in array code  H - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))



##############################################################################


##############################################################################
class compress_finite_finite_i(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'i'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  i finite finite - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  i finite finite - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  i finite finite - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  i finite finite - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  i finite finite - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  i finite finite - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_params_i(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'i'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  i - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  i - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  i - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  i - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  i - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  i - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  i - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_08(self):
		"""Test compress in array code  i - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))



##############################################################################


##############################################################################
class compress_finite_finite_I(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'I'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  I finite finite - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  I finite finite - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  I finite finite - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  I finite finite - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  I finite finite - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  I finite finite - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_params_I(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'I'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  I - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  I - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  I - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  I - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  I - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  I - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  I - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_08(self):
		"""Test compress in array code  I - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))



##############################################################################


##############################################################################
class compress_finite_finite_l(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'l'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  l finite finite - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  l finite finite - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  l finite finite - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  l finite finite - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  l finite finite - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  l finite finite - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_params_l(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'l'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  l - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  l - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  l - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  l - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  l - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  l - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  l - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_08(self):
		"""Test compress in array code  l - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))



##############################################################################


##############################################################################
class compress_finite_finite_L(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'L'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  L finite finite - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  L finite finite - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  L finite finite - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  L finite finite - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  L finite finite - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  L finite finite - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_params_L(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'L'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  L - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  L - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  L - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  L - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  L - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  L - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  L - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_08(self):
		"""Test compress in array code  L - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))



##############################################################################


##############################################################################
class compress_finite_finite_q(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'q'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  q finite finite - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  q finite finite - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  q finite finite - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  q finite finite - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  q finite finite - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  q finite finite - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_params_q(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'q'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  q - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  q - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  q - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  q - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  q - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  q - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  q - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_08(self):
		"""Test compress in array code  q - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))



##############################################################################


##############################################################################
class compress_finite_finite_Q(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'Q'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  Q finite finite - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  Q finite finite - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  Q finite finite - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  Q finite finite - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  Q finite finite - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  Q finite finite - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_params_Q(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'Q'

		self.initvalin = 5
		self.initvalout = 6
		self.selector = [0, 1]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  Q - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  Q - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  Q - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  Q - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  Q - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  Q - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  Q - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_08(self):
		"""Test compress in array code  Q - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))



##############################################################################


##############################################################################
class compress_finite_finite_f(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'f'

		self.initvalin = 5.5
		self.initvalout = 6.6
		self.selector = [0.0, 1.0]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  f finite finite - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  f finite finite - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  f finite finite - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  f finite finite - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  f finite finite - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  f finite finite - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_params_f(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'f'

		self.initvalin = 5.5
		self.initvalout = 6.6
		self.selector = [0.0, 1.0]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  f - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  f - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  f - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  f - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  f - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  f - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  f - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_08(self):
		"""Test compress in array code  f - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))



##############################################################################


##############################################################################
class compress_finite_finite_d(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'd'

		self.initvalin = 5.5
		self.initvalout = 6.6
		self.selector = [0.0, 1.0]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  d finite finite - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  d finite finite - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  d finite finite - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  d finite finite - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  d finite finite - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  d finite finite - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_params_d(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'd'

		self.initvalin = 5.5
		self.initvalout = 6.6
		self.selector = [0.0, 1.0]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def test_compress_01(self):
		"""Test compress in array code  d - Test for invalid input array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(1, self.dataout, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress(1, [1,0,1,0]))


	########################################################
	def test_compress_02(self):
		"""Test compress in array code  d - Test for invalid output array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, 1, self.selector)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_03(self):
		"""Test compress in array code  d - Test for invalid selector array parameter type.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1,0,1,0], 1))


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  d - Test invalid parameter type for limit.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], maxlen='a'))


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  d - Test for missing all array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress())


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  d - Test for missing two array parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_07(self):
		"""Test compress in array code  d - Test for missing one array parameter.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4]))


	########################################################
	def test_compress_08(self):
		"""Test compress in array code  d - Test too many (5) parameters.
		"""
		with self.assertRaises(TypeError):
			x = arrayfunc.compress(self.data, self.dataout, self.selector, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			x = list(itertools.compress([1, 2, 3, 4], [1,0,1,0], 2))



##############################################################################


##############################################################################
class compress_nan_inp_f(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'f'

		self.initvalin = math.nan
		self.initvalout = 6.6
		self.selector = [0.0, 1.0]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  f nan inp - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  f nan inp - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  f nan inp - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  f nan inp - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  f nan inp - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  f nan inp - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_inf_inp_f(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'f'

		self.initvalin = math.inf
		self.initvalout = 6.6
		self.selector = [0.0, 1.0]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  f inf inp - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  f inf inp - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  f inf inp - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  f inf inp - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  f inf inp - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  f inf inp - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_ninf_inp_f(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'f'

		self.initvalin = -math.inf
		self.initvalout = 6.6
		self.selector = [0.0, 1.0]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  f ninf inp - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  f ninf inp - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  f ninf inp - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  f ninf inp - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  f ninf inp - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  f ninf inp - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_nan_inp_d(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'd'

		self.initvalin = math.nan
		self.initvalout = 6.6
		self.selector = [0.0, 1.0]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  d nan inp - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  d nan inp - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  d nan inp - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  d nan inp - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  d nan inp - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  d nan inp - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_inf_inp_d(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'd'

		self.initvalin = math.inf
		self.initvalout = 6.6
		self.selector = [0.0, 1.0]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  d inf inp - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  d inf inp - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  d inf inp - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  d inf inp - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  d inf inp - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  d inf inp - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_ninf_inp_d(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'd'

		self.initvalin = -math.inf
		self.initvalout = 6.6
		self.selector = [0.0, 1.0]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  d ninf inp - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  d ninf inp - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  d ninf inp - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  d ninf inp - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  d ninf inp - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  d ninf inp - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_nan_sel_f(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'f'

		self.initvalin = 5.5
		self.initvalout = 6.6
		self.selector = [0.0, math.nan]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  f nan sel - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  f nan sel - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  f nan sel - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  f nan sel - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  f nan sel - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  f nan sel - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_inf_sel_f(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'f'

		self.initvalin = 5.5
		self.initvalout = 6.6
		self.selector = [0.0, math.inf]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  f inf sel - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  f inf sel - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  f inf sel - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  f inf sel - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  f inf sel - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  f inf sel - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_ninf_sel_f(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'f'

		self.initvalin = 5.5
		self.initvalout = 6.6
		self.selector = [0.0, -math.inf]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  f ninf sel - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  f ninf sel - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  f ninf sel - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  f ninf sel - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  f ninf sel - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  f ninf sel - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_nan_sel_d(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'd'

		self.initvalin = 5.5
		self.initvalout = 6.6
		self.selector = [0.0, math.nan]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  d nan sel - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  d nan sel - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  d nan sel - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  d nan sel - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  d nan sel - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  d nan sel - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_inf_sel_d(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'd'

		self.initvalin = 5.5
		self.initvalout = 6.6
		self.selector = [0.0, math.inf]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  d inf sel - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  d inf sel - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  d inf sel - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  d inf sel - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  d inf sel - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  d inf sel - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class compress_ninf_sel_d(unittest.TestCase):
	"""Test for basic compress function.
	op_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
		"""This function is patched into assertEqual to allow testing for 
		the floating point special values NaN, Inf, and -Inf.
		"""
		# NaN cannot be compared using normal means.
		if math.isnan(dataoutitem) and math.isnan(expecteditem):
			pass
		# Anything else can be compared normally.
		else:
			if not math.isclose(expecteditem, dataoutitem, rel_tol=0.01, abs_tol=0.0):
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = 'd'

		self.initvalin = 5.5
		self.initvalout = 6.6
		self.selector = [0.0, -math.inf]

		self.data = array.array(self.TypeCode, itertools.repeat(self.initvalin, 512))
		self.dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, 512))
		self.selector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat(self.selector, 24)))


	########################################################
	def PyCompress(self, data, dataout, selector, maxlen=0):
		"""This returns the compressed list and the number of elements copied.
		"""
		if (maxlen > 0) and (len(data) > maxlen):
			tmpdata = data[:maxlen]
		else:
			tmpdata = data

		# The selector must be at least as long as the input data, but can
		# be longer.
		if len(tmpdata) > len(selector):
			tmpselector = selector * len(tmpdata)
		else:
			tmpselector = selector

		# Compress from the standard library.
		result = list(itertools.compress(tmpdata, tmpselector))

		# We can't use the dataout in the parameter, as it may be altered.
		tmpdataout = [self.initvalout] * len(dataout)

		paddedresult = result

		# Account for result is longer than the output.
		if len(result) > len(tmpdataout):
			paddedresult = result[:len(tmpdataout)]

		# Account for the result is shorter than the output.
		if len(result) < len(tmpdataout):
			paddedresult = result + tmpdataout[len(result):]

		# Account for when the input array is longer than the output array.
		if len(result) > len(paddedresult):
			actuallen = len(paddedresult)
		else:
			actuallen = len(result)

		return (paddedresult, actuallen)





	########################################################
	def test_compress_01(self):
		"""Test compress in array code  d ninf sel - Test for basic function.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_02(self):
		"""Test compress in array code  d ninf sel - General test with array limit applied.
		"""
		result = arrayfunc.compress(self.data, self.dataout, self.selector, maxlen=256)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, self.selector, maxlen=256)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_compress_03(self):
		"""Test compress in array code  d ninf sel - Test for zero filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([0.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == 0)
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_04(self):
		"""Test compress in array code  d ninf sel - Test for one filled selector.
		"""
		localselector = array.array(self.TypeCode, itertools.chain.from_iterable(itertools.repeat([1.0], 24)))

		result = arrayfunc.compress(self.data, self.dataout, localselector)

		expected, expectedlen = self.PyCompress(self.data, self.dataout, localselector)

		# Check the test to make sure it is working as intended.
		self.assertTrue(result == len(self.data))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_05(self):
		"""Test compress in array code  d ninf sel - Test for destination array is shorter than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) // 4))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_compress_06(self):
		"""Test compress in array code  d ninf sel - Test for destination array is longer than source array.
		"""
		dataout = array.array(self.TypeCode, itertools.repeat(self.initvalout, len(self.data) * 2))

		result = arrayfunc.compress(self.data, dataout, self.selector)

		# Floating point needs special handling to account for floating point imprecision.
		expected, expectedlen = self.PyCompress(self.data, dataout, self.selector)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, expectedlen)
		for dataoutitem, expecteditem in zip(list(dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)



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
