#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_amax.py
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
"""This conducts unit tests for amax.
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
class amax_operator_b(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'b'

		self.MaxVal = arrayfunc.arraylimits.b_max
		self.MinVal = arrayfunc.arraylimits.b_min


	########################################################
	def test_function_01(self):
		"""Test amax  - Array code b. General test with SIMD.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), range(11,-88,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_02(self):
		"""Test amax  - Array code b. General test without SIMD.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), range(11,-88,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_03(self):
		"""Test amax  - Array code b. Test increasing values with SIMD.
		"""
		data = array.array('b', range(1,100))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_04(self):
		"""Test amax  - Array code b. Test increasing values without SIMD.
		"""
		data = array.array('b', range(1,100))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_05(self):
		"""Test amax  - Array code b. Test decreasing values with SIMD.
		"""
		data = array.array('b', range(100,1,-1))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_06(self):
		"""Test amax  - Array code b. Test decreasing values without SIMD.
		"""
		data = array.array('b', range(100,1,-1))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_07(self):
		"""Test amax  - Array code b. Test finding max for data type with SIMD.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_08(self):
		"""Test amax  - Array code b. Test finding max for data type without SIMD.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_09(self):
		"""Test amax  - Array code b. Test finding value from array that contains min for data type with SIMD.
		"""
		data = array.array('b', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_10(self):
		"""Test amax  - Array code b. Test finding value from array that contains min for data type without SIMD.
		"""
		data = array.array('b', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_11(self):
		"""Test amax  - Array code b. Test optional lim parameter with SIMD.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data, maxlen=5)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_12(self):
		"""Test amax  - Array code b. Test optional lim parameter without SIMD.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data, maxlen=5, nosimd=True)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_13(self):
		"""Test amax  - Array code b. Test invalid parameter type with SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_14(self):
		"""Test amax  - Array code b. Test invalid parameter type without SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1, nosimd=True)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_15(self):
		"""Test amax  - Array code b. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max()


	########################################################
	def test_function_16(self):
		"""Test amax  - Array code b. Test excess parameters.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), range(11,-88,-3)))
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(data, 5, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(data, 2)


##############################################################################



##############################################################################
class amax_operator_B(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'B'

		self.MaxVal = arrayfunc.arraylimits.B_max
		self.MinVal = arrayfunc.arraylimits.B_min


	########################################################
	def test_function_01(self):
		"""Test amax  - Array code B. General test with SIMD.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_02(self):
		"""Test amax  - Array code B. General test without SIMD.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_03(self):
		"""Test amax  - Array code B. Test increasing values with SIMD.
		"""
		data = array.array('B', range(1,100))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_04(self):
		"""Test amax  - Array code B. Test increasing values without SIMD.
		"""
		data = array.array('B', range(1,100))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_05(self):
		"""Test amax  - Array code B. Test decreasing values with SIMD.
		"""
		data = array.array('B', range(100,1,-1))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_06(self):
		"""Test amax  - Array code B. Test decreasing values without SIMD.
		"""
		data = array.array('B', range(100,1,-1))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_07(self):
		"""Test amax  - Array code B. Test finding max for data type with SIMD.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_08(self):
		"""Test amax  - Array code B. Test finding max for data type without SIMD.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_09(self):
		"""Test amax  - Array code B. Test finding value from array that contains min for data type with SIMD.
		"""
		data = array.array('B', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_10(self):
		"""Test amax  - Array code B. Test finding value from array that contains min for data type without SIMD.
		"""
		data = array.array('B', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_11(self):
		"""Test amax  - Array code B. Test optional lim parameter with SIMD.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data, maxlen=5)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_12(self):
		"""Test amax  - Array code B. Test optional lim parameter without SIMD.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data, maxlen=5, nosimd=True)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_13(self):
		"""Test amax  - Array code B. Test invalid parameter type with SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_14(self):
		"""Test amax  - Array code B. Test invalid parameter type without SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1, nosimd=True)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_15(self):
		"""Test amax  - Array code B. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max()


	########################################################
	def test_function_16(self):
		"""Test amax  - Array code B. Test excess parameters.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(data, 5, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(data, 2)


##############################################################################



##############################################################################
class amax_operator_h(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'h'

		self.MaxVal = arrayfunc.arraylimits.h_max
		self.MinVal = arrayfunc.arraylimits.h_min


	########################################################
	def test_function_01(self):
		"""Test amax  - Array code h. General test with SIMD.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), range(11,-88,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_02(self):
		"""Test amax  - Array code h. General test without SIMD.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), range(11,-88,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_03(self):
		"""Test amax  - Array code h. Test increasing values with SIMD.
		"""
		data = array.array('h', range(1,100))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_04(self):
		"""Test amax  - Array code h. Test increasing values without SIMD.
		"""
		data = array.array('h', range(1,100))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_05(self):
		"""Test amax  - Array code h. Test decreasing values with SIMD.
		"""
		data = array.array('h', range(100,1,-1))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_06(self):
		"""Test amax  - Array code h. Test decreasing values without SIMD.
		"""
		data = array.array('h', range(100,1,-1))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_07(self):
		"""Test amax  - Array code h. Test finding max for data type with SIMD.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_08(self):
		"""Test amax  - Array code h. Test finding max for data type without SIMD.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_09(self):
		"""Test amax  - Array code h. Test finding value from array that contains min for data type with SIMD.
		"""
		data = array.array('h', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_10(self):
		"""Test amax  - Array code h. Test finding value from array that contains min for data type without SIMD.
		"""
		data = array.array('h', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_11(self):
		"""Test amax  - Array code h. Test optional lim parameter with SIMD.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data, maxlen=5)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_12(self):
		"""Test amax  - Array code h. Test optional lim parameter without SIMD.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data, maxlen=5, nosimd=True)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_13(self):
		"""Test amax  - Array code h. Test invalid parameter type with SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_14(self):
		"""Test amax  - Array code h. Test invalid parameter type without SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1, nosimd=True)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_15(self):
		"""Test amax  - Array code h. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max()


	########################################################
	def test_function_16(self):
		"""Test amax  - Array code h. Test excess parameters.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), range(11,-88,-3)))
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(data, 5, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(data, 2)


##############################################################################



##############################################################################
class amax_operator_H(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'H'

		self.MaxVal = arrayfunc.arraylimits.H_max
		self.MinVal = arrayfunc.arraylimits.H_min


	########################################################
	def test_function_01(self):
		"""Test amax  - Array code H. General test with SIMD.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), range(88,12,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_02(self):
		"""Test amax  - Array code H. General test without SIMD.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), range(88,12,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_03(self):
		"""Test amax  - Array code H. Test increasing values with SIMD.
		"""
		data = array.array('H', range(1,100))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_04(self):
		"""Test amax  - Array code H. Test increasing values without SIMD.
		"""
		data = array.array('H', range(1,100))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_05(self):
		"""Test amax  - Array code H. Test decreasing values with SIMD.
		"""
		data = array.array('H', range(100,1,-1))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_06(self):
		"""Test amax  - Array code H. Test decreasing values without SIMD.
		"""
		data = array.array('H', range(100,1,-1))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_07(self):
		"""Test amax  - Array code H. Test finding max for data type with SIMD.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_08(self):
		"""Test amax  - Array code H. Test finding max for data type without SIMD.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_09(self):
		"""Test amax  - Array code H. Test finding value from array that contains min for data type with SIMD.
		"""
		data = array.array('H', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_10(self):
		"""Test amax  - Array code H. Test finding value from array that contains min for data type without SIMD.
		"""
		data = array.array('H', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_11(self):
		"""Test amax  - Array code H. Test optional lim parameter with SIMD.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data, maxlen=5)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_12(self):
		"""Test amax  - Array code H. Test optional lim parameter without SIMD.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data, maxlen=5, nosimd=True)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_13(self):
		"""Test amax  - Array code H. Test invalid parameter type with SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_14(self):
		"""Test amax  - Array code H. Test invalid parameter type without SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1, nosimd=True)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_15(self):
		"""Test amax  - Array code H. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max()


	########################################################
	def test_function_16(self):
		"""Test amax  - Array code H. Test excess parameters.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), range(88,12,-3)))
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(data, 5, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(data, 2)


##############################################################################



##############################################################################
class amax_operator_i(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'i'

		self.MaxVal = arrayfunc.arraylimits.i_max
		self.MinVal = arrayfunc.arraylimits.i_min


	########################################################
	def test_function_01(self):
		"""Test amax  - Array code i. General test with SIMD.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), range(11,-88,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_02(self):
		"""Test amax  - Array code i. General test without SIMD.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), range(11,-88,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_03(self):
		"""Test amax  - Array code i. Test increasing values with SIMD.
		"""
		data = array.array('i', range(1,100))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_04(self):
		"""Test amax  - Array code i. Test increasing values without SIMD.
		"""
		data = array.array('i', range(1,100))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_05(self):
		"""Test amax  - Array code i. Test decreasing values with SIMD.
		"""
		data = array.array('i', range(100,1,-1))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_06(self):
		"""Test amax  - Array code i. Test decreasing values without SIMD.
		"""
		data = array.array('i', range(100,1,-1))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_07(self):
		"""Test amax  - Array code i. Test finding max for data type with SIMD.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_08(self):
		"""Test amax  - Array code i. Test finding max for data type without SIMD.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_09(self):
		"""Test amax  - Array code i. Test finding value from array that contains min for data type with SIMD.
		"""
		data = array.array('i', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_10(self):
		"""Test amax  - Array code i. Test finding value from array that contains min for data type without SIMD.
		"""
		data = array.array('i', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_11(self):
		"""Test amax  - Array code i. Test optional lim parameter with SIMD.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data, maxlen=5)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_12(self):
		"""Test amax  - Array code i. Test optional lim parameter without SIMD.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data, maxlen=5, nosimd=True)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_13(self):
		"""Test amax  - Array code i. Test invalid parameter type with SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_14(self):
		"""Test amax  - Array code i. Test invalid parameter type without SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1, nosimd=True)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_15(self):
		"""Test amax  - Array code i. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max()


	########################################################
	def test_function_16(self):
		"""Test amax  - Array code i. Test excess parameters.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), range(11,-88,-3)))
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(data, 5, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(data, 2)


##############################################################################



##############################################################################
class amax_operator_I(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'I'

		self.MaxVal = arrayfunc.arraylimits.I_max
		self.MinVal = arrayfunc.arraylimits.I_min


	########################################################
	def test_function_01(self):
		"""Test amax  - Array code I. General test with SIMD.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), range(88,12,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_02(self):
		"""Test amax  - Array code I. General test without SIMD.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), range(88,12,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_03(self):
		"""Test amax  - Array code I. Test increasing values with SIMD.
		"""
		data = array.array('I', range(1,100))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_04(self):
		"""Test amax  - Array code I. Test increasing values without SIMD.
		"""
		data = array.array('I', range(1,100))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_05(self):
		"""Test amax  - Array code I. Test decreasing values with SIMD.
		"""
		data = array.array('I', range(100,1,-1))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_06(self):
		"""Test amax  - Array code I. Test decreasing values without SIMD.
		"""
		data = array.array('I', range(100,1,-1))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_07(self):
		"""Test amax  - Array code I. Test finding max for data type with SIMD.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_08(self):
		"""Test amax  - Array code I. Test finding max for data type without SIMD.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_09(self):
		"""Test amax  - Array code I. Test finding value from array that contains min for data type with SIMD.
		"""
		data = array.array('I', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_10(self):
		"""Test amax  - Array code I. Test finding value from array that contains min for data type without SIMD.
		"""
		data = array.array('I', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_11(self):
		"""Test amax  - Array code I. Test optional lim parameter with SIMD.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data, maxlen=5)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_12(self):
		"""Test amax  - Array code I. Test optional lim parameter without SIMD.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data, maxlen=5, nosimd=True)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_13(self):
		"""Test amax  - Array code I. Test invalid parameter type with SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_14(self):
		"""Test amax  - Array code I. Test invalid parameter type without SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1, nosimd=True)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_15(self):
		"""Test amax  - Array code I. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max()


	########################################################
	def test_function_16(self):
		"""Test amax  - Array code I. Test excess parameters.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), range(88,12,-3)))
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(data, 5, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(data, 2)


##############################################################################



##############################################################################
class amax_operator_l(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'l'

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min


	########################################################
	def test_function_01(self):
		"""Test amax  - Array code l. General test with SIMD.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), range(11,-88,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_02(self):
		"""Test amax  - Array code l. General test without SIMD.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), range(11,-88,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_03(self):
		"""Test amax  - Array code l. Test increasing values with SIMD.
		"""
		data = array.array('l', range(1,100))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_04(self):
		"""Test amax  - Array code l. Test increasing values without SIMD.
		"""
		data = array.array('l', range(1,100))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_05(self):
		"""Test amax  - Array code l. Test decreasing values with SIMD.
		"""
		data = array.array('l', range(100,1,-1))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_06(self):
		"""Test amax  - Array code l. Test decreasing values without SIMD.
		"""
		data = array.array('l', range(100,1,-1))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_07(self):
		"""Test amax  - Array code l. Test finding max for data type with SIMD.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_08(self):
		"""Test amax  - Array code l. Test finding max for data type without SIMD.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_09(self):
		"""Test amax  - Array code l. Test finding value from array that contains min for data type with SIMD.
		"""
		data = array.array('l', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_10(self):
		"""Test amax  - Array code l. Test finding value from array that contains min for data type without SIMD.
		"""
		data = array.array('l', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_11(self):
		"""Test amax  - Array code l. Test optional lim parameter with SIMD.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data, maxlen=5)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_12(self):
		"""Test amax  - Array code l. Test optional lim parameter without SIMD.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data, maxlen=5, nosimd=True)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_13(self):
		"""Test amax  - Array code l. Test invalid parameter type with SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_14(self):
		"""Test amax  - Array code l. Test invalid parameter type without SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1, nosimd=True)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_15(self):
		"""Test amax  - Array code l. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max()


	########################################################
	def test_function_16(self):
		"""Test amax  - Array code l. Test excess parameters.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), range(11,-88,-3)))
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(data, 5, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(data, 2)


##############################################################################



##############################################################################
class amax_operator_L(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'L'

		self.MaxVal = arrayfunc.arraylimits.L_max
		self.MinVal = arrayfunc.arraylimits.L_min


	########################################################
	def test_function_01(self):
		"""Test amax  - Array code L. General test with SIMD.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), range(88,12,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_02(self):
		"""Test amax  - Array code L. General test without SIMD.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), range(88,12,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_03(self):
		"""Test amax  - Array code L. Test increasing values with SIMD.
		"""
		data = array.array('L', range(1,100))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_04(self):
		"""Test amax  - Array code L. Test increasing values without SIMD.
		"""
		data = array.array('L', range(1,100))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_05(self):
		"""Test amax  - Array code L. Test decreasing values with SIMD.
		"""
		data = array.array('L', range(100,1,-1))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_06(self):
		"""Test amax  - Array code L. Test decreasing values without SIMD.
		"""
		data = array.array('L', range(100,1,-1))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_07(self):
		"""Test amax  - Array code L. Test finding max for data type with SIMD.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_08(self):
		"""Test amax  - Array code L. Test finding max for data type without SIMD.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_09(self):
		"""Test amax  - Array code L. Test finding value from array that contains min for data type with SIMD.
		"""
		data = array.array('L', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_10(self):
		"""Test amax  - Array code L. Test finding value from array that contains min for data type without SIMD.
		"""
		data = array.array('L', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_11(self):
		"""Test amax  - Array code L. Test optional lim parameter with SIMD.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data, maxlen=5)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_12(self):
		"""Test amax  - Array code L. Test optional lim parameter without SIMD.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data, maxlen=5, nosimd=True)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_13(self):
		"""Test amax  - Array code L. Test invalid parameter type with SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_14(self):
		"""Test amax  - Array code L. Test invalid parameter type without SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1, nosimd=True)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_15(self):
		"""Test amax  - Array code L. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max()


	########################################################
	def test_function_16(self):
		"""Test amax  - Array code L. Test excess parameters.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), range(88,12,-3)))
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(data, 5, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(data, 2)


##############################################################################



##############################################################################
class amax_operator_q(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'q'

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min


	########################################################
	def test_function_01(self):
		"""Test amax  - Array code q. General test with SIMD.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), range(11,-88,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_02(self):
		"""Test amax  - Array code q. General test without SIMD.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), range(11,-88,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_03(self):
		"""Test amax  - Array code q. Test increasing values with SIMD.
		"""
		data = array.array('q', range(1,100))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_04(self):
		"""Test amax  - Array code q. Test increasing values without SIMD.
		"""
		data = array.array('q', range(1,100))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_05(self):
		"""Test amax  - Array code q. Test decreasing values with SIMD.
		"""
		data = array.array('q', range(100,1,-1))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_06(self):
		"""Test amax  - Array code q. Test decreasing values without SIMD.
		"""
		data = array.array('q', range(100,1,-1))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_07(self):
		"""Test amax  - Array code q. Test finding max for data type with SIMD.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_08(self):
		"""Test amax  - Array code q. Test finding max for data type without SIMD.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_09(self):
		"""Test amax  - Array code q. Test finding value from array that contains min for data type with SIMD.
		"""
		data = array.array('q', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_10(self):
		"""Test amax  - Array code q. Test finding value from array that contains min for data type without SIMD.
		"""
		data = array.array('q', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_11(self):
		"""Test amax  - Array code q. Test optional lim parameter with SIMD.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data, maxlen=5)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_12(self):
		"""Test amax  - Array code q. Test optional lim parameter without SIMD.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		result = arrayfunc.amax(data, maxlen=5, nosimd=True)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_13(self):
		"""Test amax  - Array code q. Test invalid parameter type with SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_14(self):
		"""Test amax  - Array code q. Test invalid parameter type without SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1, nosimd=True)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_15(self):
		"""Test amax  - Array code q. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max()


	########################################################
	def test_function_16(self):
		"""Test amax  - Array code q. Test excess parameters.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), range(11,-88,-3)))
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(data, 5, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(data, 2)


##############################################################################



##############################################################################
class amax_operator_Q(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'Q'

		self.MaxVal = arrayfunc.arraylimits.Q_max
		self.MinVal = arrayfunc.arraylimits.Q_min


	########################################################
	def test_function_01(self):
		"""Test amax  - Array code Q. General test with SIMD.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), range(88,12,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_02(self):
		"""Test amax  - Array code Q. General test without SIMD.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), range(88,12,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_03(self):
		"""Test amax  - Array code Q. Test increasing values with SIMD.
		"""
		data = array.array('Q', range(1,100))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_04(self):
		"""Test amax  - Array code Q. Test increasing values without SIMD.
		"""
		data = array.array('Q', range(1,100))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_05(self):
		"""Test amax  - Array code Q. Test decreasing values with SIMD.
		"""
		data = array.array('Q', range(100,1,-1))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_06(self):
		"""Test amax  - Array code Q. Test decreasing values without SIMD.
		"""
		data = array.array('Q', range(100,1,-1))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_07(self):
		"""Test amax  - Array code Q. Test finding max for data type with SIMD.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_08(self):
		"""Test amax  - Array code Q. Test finding max for data type without SIMD.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_09(self):
		"""Test amax  - Array code Q. Test finding value from array that contains min for data type with SIMD.
		"""
		data = array.array('Q', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_10(self):
		"""Test amax  - Array code Q. Test finding value from array that contains min for data type without SIMD.
		"""
		data = array.array('Q', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_11(self):
		"""Test amax  - Array code Q. Test optional lim parameter with SIMD.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data, maxlen=5)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_12(self):
		"""Test amax  - Array code Q. Test optional lim parameter without SIMD.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		result = arrayfunc.amax(data, maxlen=5, nosimd=True)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_13(self):
		"""Test amax  - Array code Q. Test invalid parameter type with SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_14(self):
		"""Test amax  - Array code Q. Test invalid parameter type without SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1, nosimd=True)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_15(self):
		"""Test amax  - Array code Q. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max()


	########################################################
	def test_function_16(self):
		"""Test amax  - Array code Q. Test excess parameters.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), range(88,12,-3)))
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(data, 5, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(data, 2)


##############################################################################



##############################################################################
class amax_operator_f(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'f'

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min


	########################################################
	def test_function_01(self):
		"""Test amax  - Array code f. General test with SIMD.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_02(self):
		"""Test amax  - Array code f. General test without SIMD.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_03(self):
		"""Test amax  - Array code f. Test increasing values with SIMD.
		"""
		data = array.array('f', [float(x) for x in range(1,100)])
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_04(self):
		"""Test amax  - Array code f. Test increasing values without SIMD.
		"""
		data = array.array('f', [float(x) for x in range(1,100)])
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_05(self):
		"""Test amax  - Array code f. Test decreasing values with SIMD.
		"""
		data = array.array('f', [float(x) for x in range(100,1,-1)])
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_06(self):
		"""Test amax  - Array code f. Test decreasing values without SIMD.
		"""
		data = array.array('f', [float(x) for x in range(100,1,-1)])
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_07(self):
		"""Test amax  - Array code f. Test finding max for data type with SIMD.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3))])
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_08(self):
		"""Test amax  - Array code f. Test finding max for data type without SIMD.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3))])
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_09(self):
		"""Test amax  - Array code f. Test finding value from array that contains min for data type with SIMD.
		"""
		data = array.array('f', [float(x) for x in itertools.chain([self.MinVal] * 10, range(1,10,2), [self.MinVal] * 10)])
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_10(self):
		"""Test amax  - Array code f. Test finding value from array that contains min for data type without SIMD.
		"""
		data = array.array('f', [float(x) for x in itertools.chain([self.MinVal] * 10, range(1,10,2), [self.MinVal] * 10)])
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_11(self):
		"""Test amax  - Array code f. Test optional lim parameter with SIMD.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3))])
		result = arrayfunc.amax(data, maxlen=5)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_12(self):
		"""Test amax  - Array code f. Test optional lim parameter without SIMD.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3))])
		result = arrayfunc.amax(data, maxlen=5, nosimd=True)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_13(self):
		"""Test amax  - Array code f. Test invalid parameter type with SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_14(self):
		"""Test amax  - Array code f. Test invalid parameter type without SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1, nosimd=True)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_15(self):
		"""Test amax  - Array code f. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max()


	########################################################
	def test_function_16(self):
		"""Test amax  - Array code f. Test excess parameters.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(data, 5, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(data, 2)


##############################################################################



##############################################################################
class amax_operator_d(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'd'

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min


	########################################################
	def test_function_01(self):
		"""Test amax  - Array code d. General test with SIMD.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_02(self):
		"""Test amax  - Array code d. General test without SIMD.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_03(self):
		"""Test amax  - Array code d. Test increasing values with SIMD.
		"""
		data = array.array('d', [float(x) for x in range(1,100)])
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_04(self):
		"""Test amax  - Array code d. Test increasing values without SIMD.
		"""
		data = array.array('d', [float(x) for x in range(1,100)])
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_05(self):
		"""Test amax  - Array code d. Test decreasing values with SIMD.
		"""
		data = array.array('d', [float(x) for x in range(100,1,-1)])
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_06(self):
		"""Test amax  - Array code d. Test decreasing values without SIMD.
		"""
		data = array.array('d', [float(x) for x in range(100,1,-1)])
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_07(self):
		"""Test amax  - Array code d. Test finding max for data type with SIMD.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3))])
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_08(self):
		"""Test amax  - Array code d. Test finding max for data type without SIMD.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3))])
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_09(self):
		"""Test amax  - Array code d. Test finding value from array that contains min for data type with SIMD.
		"""
		data = array.array('d', [float(x) for x in itertools.chain([self.MinVal] * 10, range(1,10,2), [self.MinVal] * 10)])
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_10(self):
		"""Test amax  - Array code d. Test finding value from array that contains min for data type without SIMD.
		"""
		data = array.array('d', [float(x) for x in itertools.chain([self.MinVal] * 10, range(1,10,2), [self.MinVal] * 10)])
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_function_11(self):
		"""Test amax  - Array code d. Test optional lim parameter with SIMD.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3))])
		result = arrayfunc.amax(data, maxlen=5)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_12(self):
		"""Test amax  - Array code d. Test optional lim parameter without SIMD.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3))])
		result = arrayfunc.amax(data, maxlen=5, nosimd=True)
		self.assertEqual(result, max(data[:5]))


	########################################################
	def test_function_13(self):
		"""Test amax  - Array code d. Test invalid parameter type with SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_14(self):
		"""Test amax  - Array code d. Test invalid parameter type without SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(1, nosimd=True)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(1)


	########################################################
	def test_function_15(self):
		"""Test amax  - Array code d. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amax()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max()


	########################################################
	def test_function_16(self):
		"""Test amax  - Array code d. Test excess parameters.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		with self.assertRaises(TypeError):
			result = arrayfunc.amax(data, 5, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = max(data, 2)


##############################################################################


##############################################################################
class amax_nan_f(unittest.TestCase):
	"""Test with floating point nan, inf -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min

		self.data_nan = array.array('f', [-10.0, -1000.0, -1.0, 0.0, 1.0, float('nan'), self.MaxVal, self.MinVal, 100.5, 100.1, 100.1])
		self.data_inf = array.array('f', [-10.0, -1000.0, -1.0, 0.0, 1.0, float('inf'), self.MaxVal, self.MinVal, 100.5, 100.1, 100.1])
		self.data_ninf = array.array('f', [-10.0, -1000.0, -1.0, 0.0, 1.0, float('-inf'), self.MaxVal, self.MinVal, 100.5, 100.1, 100.1])
		self.data_mixed = array.array('f', [-10.0, -1000.0, float('inf'), 0.0, float('-inf'), float('nan'), self.MaxVal, self.MinVal, 100.5, 100.1, 100.1])


	########################################################
	def rottest(self, x, rotplaces):
		"""Modify the test data by shifting the data in the array.
		"""
		return x[rotplaces:] + x[:rotplaces]


	########################################################
	def test_inf_SIMD_0(self):
		"""Test array with inf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_inf, 0)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_0(self):
		"""Test array with inf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_inf, 0)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_1(self):
		"""Test array with inf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_inf, 1)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_1(self):
		"""Test array with inf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_inf, 1)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_2(self):
		"""Test array with inf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_inf, 2)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_2(self):
		"""Test array with inf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_inf, 2)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_3(self):
		"""Test array with inf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_inf, 3)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_3(self):
		"""Test array with inf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_inf, 3)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_4(self):
		"""Test array with inf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_inf, 4)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_4(self):
		"""Test array with inf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_inf, 4)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_5(self):
		"""Test array with inf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_inf, 5)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_5(self):
		"""Test array with inf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_inf, 5)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_6(self):
		"""Test array with inf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_inf, 6)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_6(self):
		"""Test array with inf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_inf, 6)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_7(self):
		"""Test array with inf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_inf, 7)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_7(self):
		"""Test array with inf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_inf, 7)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_8(self):
		"""Test array with inf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_inf, 8)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_8(self):
		"""Test array with inf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_inf, 8)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_9(self):
		"""Test array with inf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_inf, 9)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_9(self):
		"""Test array with inf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_inf, 9)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_10(self):
		"""Test array with inf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_inf, 10)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_10(self):
		"""Test array with inf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_inf, 10)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_0(self):
		"""Test array with ninf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_ninf, 0)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_0(self):
		"""Test array with ninf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_ninf, 0)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_1(self):
		"""Test array with ninf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_ninf, 1)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_1(self):
		"""Test array with ninf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_ninf, 1)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_2(self):
		"""Test array with ninf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_ninf, 2)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_2(self):
		"""Test array with ninf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_ninf, 2)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_3(self):
		"""Test array with ninf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_ninf, 3)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_3(self):
		"""Test array with ninf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_ninf, 3)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_4(self):
		"""Test array with ninf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_ninf, 4)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_4(self):
		"""Test array with ninf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_ninf, 4)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_5(self):
		"""Test array with ninf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_ninf, 5)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_5(self):
		"""Test array with ninf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_ninf, 5)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_6(self):
		"""Test array with ninf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_ninf, 6)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_6(self):
		"""Test array with ninf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_ninf, 6)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_7(self):
		"""Test array with ninf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_ninf, 7)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_7(self):
		"""Test array with ninf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_ninf, 7)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_8(self):
		"""Test array with ninf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_ninf, 8)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_8(self):
		"""Test array with ninf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_ninf, 8)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_9(self):
		"""Test array with ninf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_ninf, 9)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_9(self):
		"""Test array with ninf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_ninf, 9)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_10(self):
		"""Test array with ninf - Array code f with SIMD.
		"""
		data = self.rottest(self.data_ninf, 10)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_10(self):
		"""Test array with ninf - Array code f without SIMD.
		"""
		data = self.rottest(self.data_ninf, 10)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_nan_SIMD_0(self):
		"""Test array with nan - Array code f with SIMD.
		"""
		data = self.rottest(self.data_nan, 0)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_0(self):
		"""Test array with nan - Array code f without SIMD.
		"""
		data = self.rottest(self.data_nan, 0)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_1(self):
		"""Test array with nan - Array code f with SIMD.
		"""
		data = self.rottest(self.data_nan, 1)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_1(self):
		"""Test array with nan - Array code f without SIMD.
		"""
		data = self.rottest(self.data_nan, 1)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_2(self):
		"""Test array with nan - Array code f with SIMD.
		"""
		data = self.rottest(self.data_nan, 2)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_2(self):
		"""Test array with nan - Array code f without SIMD.
		"""
		data = self.rottest(self.data_nan, 2)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_3(self):
		"""Test array with nan - Array code f with SIMD.
		"""
		data = self.rottest(self.data_nan, 3)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_3(self):
		"""Test array with nan - Array code f without SIMD.
		"""
		data = self.rottest(self.data_nan, 3)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_4(self):
		"""Test array with nan - Array code f with SIMD.
		"""
		data = self.rottest(self.data_nan, 4)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_4(self):
		"""Test array with nan - Array code f without SIMD.
		"""
		data = self.rottest(self.data_nan, 4)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_5(self):
		"""Test array with nan - Array code f with SIMD.
		"""
		data = self.rottest(self.data_nan, 5)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_5(self):
		"""Test array with nan - Array code f without SIMD.
		"""
		data = self.rottest(self.data_nan, 5)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_6(self):
		"""Test array with nan - Array code f with SIMD.
		"""
		data = self.rottest(self.data_nan, 6)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_6(self):
		"""Test array with nan - Array code f without SIMD.
		"""
		data = self.rottest(self.data_nan, 6)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_7(self):
		"""Test array with nan - Array code f with SIMD.
		"""
		data = self.rottest(self.data_nan, 7)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_7(self):
		"""Test array with nan - Array code f without SIMD.
		"""
		data = self.rottest(self.data_nan, 7)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_8(self):
		"""Test array with nan - Array code f with SIMD.
		"""
		data = self.rottest(self.data_nan, 8)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_8(self):
		"""Test array with nan - Array code f without SIMD.
		"""
		data = self.rottest(self.data_nan, 8)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_9(self):
		"""Test array with nan - Array code f with SIMD.
		"""
		data = self.rottest(self.data_nan, 9)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_9(self):
		"""Test array with nan - Array code f without SIMD.
		"""
		data = self.rottest(self.data_nan, 9)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_10(self):
		"""Test array with nan - Array code f with SIMD.
		"""
		data = self.rottest(self.data_nan, 10)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_10(self):
		"""Test array with nan - Array code f without SIMD.
		"""
		data = self.rottest(self.data_nan, 10)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_0(self):
		"""Test array with mixed - Array code f with SIMD.
		"""
		data = self.rottest(self.data_mixed, 0)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_0(self):
		"""Test array with mixed - Array code f without SIMD.
		"""
		data = self.rottest(self.data_mixed, 0)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_1(self):
		"""Test array with mixed - Array code f with SIMD.
		"""
		data = self.rottest(self.data_mixed, 1)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_1(self):
		"""Test array with mixed - Array code f without SIMD.
		"""
		data = self.rottest(self.data_mixed, 1)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_2(self):
		"""Test array with mixed - Array code f with SIMD.
		"""
		data = self.rottest(self.data_mixed, 2)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_2(self):
		"""Test array with mixed - Array code f without SIMD.
		"""
		data = self.rottest(self.data_mixed, 2)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_3(self):
		"""Test array with mixed - Array code f with SIMD.
		"""
		data = self.rottest(self.data_mixed, 3)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_3(self):
		"""Test array with mixed - Array code f without SIMD.
		"""
		data = self.rottest(self.data_mixed, 3)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_4(self):
		"""Test array with mixed - Array code f with SIMD.
		"""
		data = self.rottest(self.data_mixed, 4)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_4(self):
		"""Test array with mixed - Array code f without SIMD.
		"""
		data = self.rottest(self.data_mixed, 4)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_5(self):
		"""Test array with mixed - Array code f with SIMD.
		"""
		data = self.rottest(self.data_mixed, 5)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_5(self):
		"""Test array with mixed - Array code f without SIMD.
		"""
		data = self.rottest(self.data_mixed, 5)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_6(self):
		"""Test array with mixed - Array code f with SIMD.
		"""
		data = self.rottest(self.data_mixed, 6)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_6(self):
		"""Test array with mixed - Array code f without SIMD.
		"""
		data = self.rottest(self.data_mixed, 6)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_7(self):
		"""Test array with mixed - Array code f with SIMD.
		"""
		data = self.rottest(self.data_mixed, 7)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_7(self):
		"""Test array with mixed - Array code f without SIMD.
		"""
		data = self.rottest(self.data_mixed, 7)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_8(self):
		"""Test array with mixed - Array code f with SIMD.
		"""
		data = self.rottest(self.data_mixed, 8)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_8(self):
		"""Test array with mixed - Array code f without SIMD.
		"""
		data = self.rottest(self.data_mixed, 8)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_9(self):
		"""Test array with mixed - Array code f with SIMD.
		"""
		data = self.rottest(self.data_mixed, 9)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_9(self):
		"""Test array with mixed - Array code f without SIMD.
		"""
		data = self.rottest(self.data_mixed, 9)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_10(self):
		"""Test array with mixed - Array code f with SIMD.
		"""
		data = self.rottest(self.data_mixed, 10)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_10(self):
		"""Test array with mixed - Array code f without SIMD.
		"""
		data = self.rottest(self.data_mixed, 10)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


##############################################################################

##############################################################################
class amax_nan_d(unittest.TestCase):
	"""Test with floating point nan, inf -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min

		self.data_nan = array.array('d', [-10.0, -1000.0, -1.0, 0.0, 1.0, float('nan'), self.MaxVal, self.MinVal, 100.5, 100.1, 100.1])
		self.data_inf = array.array('d', [-10.0, -1000.0, -1.0, 0.0, 1.0, float('inf'), self.MaxVal, self.MinVal, 100.5, 100.1, 100.1])
		self.data_ninf = array.array('d', [-10.0, -1000.0, -1.0, 0.0, 1.0, float('-inf'), self.MaxVal, self.MinVal, 100.5, 100.1, 100.1])
		self.data_mixed = array.array('d', [-10.0, -1000.0, float('inf'), 0.0, float('-inf'), float('nan'), self.MaxVal, self.MinVal, 100.5, 100.1, 100.1])


	########################################################
	def rottest(self, x, rotplaces):
		"""Modify the test data by shifting the data in the array.
		"""
		return x[rotplaces:] + x[:rotplaces]


	########################################################
	def test_inf_SIMD_0(self):
		"""Test array with inf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_inf, 0)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_0(self):
		"""Test array with inf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_inf, 0)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_1(self):
		"""Test array with inf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_inf, 1)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_1(self):
		"""Test array with inf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_inf, 1)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_2(self):
		"""Test array with inf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_inf, 2)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_2(self):
		"""Test array with inf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_inf, 2)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_3(self):
		"""Test array with inf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_inf, 3)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_3(self):
		"""Test array with inf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_inf, 3)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_4(self):
		"""Test array with inf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_inf, 4)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_4(self):
		"""Test array with inf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_inf, 4)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_5(self):
		"""Test array with inf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_inf, 5)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_5(self):
		"""Test array with inf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_inf, 5)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_6(self):
		"""Test array with inf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_inf, 6)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_6(self):
		"""Test array with inf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_inf, 6)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_7(self):
		"""Test array with inf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_inf, 7)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_7(self):
		"""Test array with inf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_inf, 7)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_8(self):
		"""Test array with inf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_inf, 8)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_8(self):
		"""Test array with inf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_inf, 8)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_9(self):
		"""Test array with inf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_inf, 9)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_9(self):
		"""Test array with inf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_inf, 9)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_SIMD_10(self):
		"""Test array with inf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_inf, 10)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_inf_NOSIMD_10(self):
		"""Test array with inf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_inf, 10)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_0(self):
		"""Test array with ninf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_ninf, 0)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_0(self):
		"""Test array with ninf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_ninf, 0)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_1(self):
		"""Test array with ninf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_ninf, 1)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_1(self):
		"""Test array with ninf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_ninf, 1)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_2(self):
		"""Test array with ninf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_ninf, 2)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_2(self):
		"""Test array with ninf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_ninf, 2)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_3(self):
		"""Test array with ninf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_ninf, 3)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_3(self):
		"""Test array with ninf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_ninf, 3)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_4(self):
		"""Test array with ninf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_ninf, 4)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_4(self):
		"""Test array with ninf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_ninf, 4)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_5(self):
		"""Test array with ninf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_ninf, 5)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_5(self):
		"""Test array with ninf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_ninf, 5)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_6(self):
		"""Test array with ninf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_ninf, 6)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_6(self):
		"""Test array with ninf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_ninf, 6)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_7(self):
		"""Test array with ninf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_ninf, 7)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_7(self):
		"""Test array with ninf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_ninf, 7)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_8(self):
		"""Test array with ninf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_ninf, 8)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_8(self):
		"""Test array with ninf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_ninf, 8)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_9(self):
		"""Test array with ninf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_ninf, 9)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_9(self):
		"""Test array with ninf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_ninf, 9)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_SIMD_10(self):
		"""Test array with ninf - Array code d with SIMD.
		"""
		data = self.rottest(self.data_ninf, 10)
		result = arrayfunc.amax(data)
		self.assertEqual(result, max(data))


	########################################################
	def test_ninf_NOSIMD_10(self):
		"""Test array with ninf - Array code d without SIMD.
		"""
		data = self.rottest(self.data_ninf, 10)
		result = arrayfunc.amax(data, nosimd=True)
		self.assertEqual(result, max(data))


	########################################################
	def test_nan_SIMD_0(self):
		"""Test array with nan - Array code d with SIMD.
		"""
		data = self.rottest(self.data_nan, 0)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_0(self):
		"""Test array with nan - Array code d without SIMD.
		"""
		data = self.rottest(self.data_nan, 0)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_1(self):
		"""Test array with nan - Array code d with SIMD.
		"""
		data = self.rottest(self.data_nan, 1)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_1(self):
		"""Test array with nan - Array code d without SIMD.
		"""
		data = self.rottest(self.data_nan, 1)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_2(self):
		"""Test array with nan - Array code d with SIMD.
		"""
		data = self.rottest(self.data_nan, 2)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_2(self):
		"""Test array with nan - Array code d without SIMD.
		"""
		data = self.rottest(self.data_nan, 2)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_3(self):
		"""Test array with nan - Array code d with SIMD.
		"""
		data = self.rottest(self.data_nan, 3)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_3(self):
		"""Test array with nan - Array code d without SIMD.
		"""
		data = self.rottest(self.data_nan, 3)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_4(self):
		"""Test array with nan - Array code d with SIMD.
		"""
		data = self.rottest(self.data_nan, 4)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_4(self):
		"""Test array with nan - Array code d without SIMD.
		"""
		data = self.rottest(self.data_nan, 4)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_5(self):
		"""Test array with nan - Array code d with SIMD.
		"""
		data = self.rottest(self.data_nan, 5)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_5(self):
		"""Test array with nan - Array code d without SIMD.
		"""
		data = self.rottest(self.data_nan, 5)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_6(self):
		"""Test array with nan - Array code d with SIMD.
		"""
		data = self.rottest(self.data_nan, 6)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_6(self):
		"""Test array with nan - Array code d without SIMD.
		"""
		data = self.rottest(self.data_nan, 6)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_7(self):
		"""Test array with nan - Array code d with SIMD.
		"""
		data = self.rottest(self.data_nan, 7)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_7(self):
		"""Test array with nan - Array code d without SIMD.
		"""
		data = self.rottest(self.data_nan, 7)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_8(self):
		"""Test array with nan - Array code d with SIMD.
		"""
		data = self.rottest(self.data_nan, 8)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_8(self):
		"""Test array with nan - Array code d without SIMD.
		"""
		data = self.rottest(self.data_nan, 8)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_9(self):
		"""Test array with nan - Array code d with SIMD.
		"""
		data = self.rottest(self.data_nan, 9)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_9(self):
		"""Test array with nan - Array code d without SIMD.
		"""
		data = self.rottest(self.data_nan, 9)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_SIMD_10(self):
		"""Test array with nan - Array code d with SIMD.
		"""
		data = self.rottest(self.data_nan, 10)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_nan_NOSIMD_10(self):
		"""Test array with nan - Array code d without SIMD.
		"""
		data = self.rottest(self.data_nan, 10)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_0(self):
		"""Test array with mixed - Array code d with SIMD.
		"""
		data = self.rottest(self.data_mixed, 0)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_0(self):
		"""Test array with mixed - Array code d without SIMD.
		"""
		data = self.rottest(self.data_mixed, 0)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_1(self):
		"""Test array with mixed - Array code d with SIMD.
		"""
		data = self.rottest(self.data_mixed, 1)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_1(self):
		"""Test array with mixed - Array code d without SIMD.
		"""
		data = self.rottest(self.data_mixed, 1)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_2(self):
		"""Test array with mixed - Array code d with SIMD.
		"""
		data = self.rottest(self.data_mixed, 2)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_2(self):
		"""Test array with mixed - Array code d without SIMD.
		"""
		data = self.rottest(self.data_mixed, 2)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_3(self):
		"""Test array with mixed - Array code d with SIMD.
		"""
		data = self.rottest(self.data_mixed, 3)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_3(self):
		"""Test array with mixed - Array code d without SIMD.
		"""
		data = self.rottest(self.data_mixed, 3)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_4(self):
		"""Test array with mixed - Array code d with SIMD.
		"""
		data = self.rottest(self.data_mixed, 4)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_4(self):
		"""Test array with mixed - Array code d without SIMD.
		"""
		data = self.rottest(self.data_mixed, 4)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_5(self):
		"""Test array with mixed - Array code d with SIMD.
		"""
		data = self.rottest(self.data_mixed, 5)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_5(self):
		"""Test array with mixed - Array code d without SIMD.
		"""
		data = self.rottest(self.data_mixed, 5)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_6(self):
		"""Test array with mixed - Array code d with SIMD.
		"""
		data = self.rottest(self.data_mixed, 6)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_6(self):
		"""Test array with mixed - Array code d without SIMD.
		"""
		data = self.rottest(self.data_mixed, 6)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_7(self):
		"""Test array with mixed - Array code d with SIMD.
		"""
		data = self.rottest(self.data_mixed, 7)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_7(self):
		"""Test array with mixed - Array code d without SIMD.
		"""
		data = self.rottest(self.data_mixed, 7)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_8(self):
		"""Test array with mixed - Array code d with SIMD.
		"""
		data = self.rottest(self.data_mixed, 8)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_8(self):
		"""Test array with mixed - Array code d without SIMD.
		"""
		data = self.rottest(self.data_mixed, 8)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_9(self):
		"""Test array with mixed - Array code d with SIMD.
		"""
		data = self.rottest(self.data_mixed, 9)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_9(self):
		"""Test array with mixed - Array code d without SIMD.
		"""
		data = self.rottest(self.data_mixed, 9)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_SIMD_10(self):
		"""Test array with mixed - Array code d with SIMD.
		"""
		data = self.rottest(self.data_mixed, 10)
		result = arrayfunc.amax(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_mixed_NOSIMD_10(self):
		"""Test array with mixed - Array code d without SIMD.
		"""
		data = self.rottest(self.data_mixed, 10)
		result = arrayfunc.amax(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


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
			f.write('amax\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
