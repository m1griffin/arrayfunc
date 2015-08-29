#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_asum.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     11-Jun-2014.
# Ver:      29-Aug-2015.
#
###############################################################################
#
#   Copyright 2014 - 2015    Michael Griffin    <m12.griffin@gmail.com>
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
"""This conducts unit tests for asum.
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
class asum_operator_b(unittest.TestCase):
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
		"""Test asum  - Array code b. General test.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_02(self):
		"""Test asum  - Array code b. General test with overflow checking on.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=False)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_03(self):
		"""Test asum  - Array code b. General test with overflow checking off.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=True)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_04(self):
		"""Test asum  - Array code b. General test with array limit applied.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_05(self):
		"""Test asum  - Array code b. General test with array limit applied and overflow checking on.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=False, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_06(self):
		"""Test asum  - Array code b. General test with array limit applied and overflow checking off.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=True, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_07(self):
		"""Test asum  - Array code b. Test invalid parameter type for array data.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)

	########################################################
	def test_function_08(self):
		"""Test asum  - Array code b. Test invalid parameter type for overflow flag.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, disovfl='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')

	########################################################
	def test_function_09(self):
		"""Test asum  - Array code b. Test invalid parameter type for limit.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')


	########################################################
	def test_function_10(self):
		"""Test asum  - Array code b. Test no parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_function_11(self):
		"""Test asum  - Array code b. Test too many (four) parameters.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, False, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(data, 0, 2)



##############################################################################

##############################################################################
class asum_operator_B(unittest.TestCase):
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
		"""Test asum  - Array code B. General test.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_02(self):
		"""Test asum  - Array code B. General test with overflow checking on.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=False)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_03(self):
		"""Test asum  - Array code B. General test with overflow checking off.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=True)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_04(self):
		"""Test asum  - Array code B. General test with array limit applied.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_05(self):
		"""Test asum  - Array code B. General test with array limit applied and overflow checking on.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=False, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_06(self):
		"""Test asum  - Array code B. General test with array limit applied and overflow checking off.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=True, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_07(self):
		"""Test asum  - Array code B. Test invalid parameter type for array data.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)

	########################################################
	def test_function_08(self):
		"""Test asum  - Array code B. Test invalid parameter type for overflow flag.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, disovfl='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')

	########################################################
	def test_function_09(self):
		"""Test asum  - Array code B. Test invalid parameter type for limit.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')


	########################################################
	def test_function_10(self):
		"""Test asum  - Array code B. Test no parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_function_11(self):
		"""Test asum  - Array code B. Test too many (four) parameters.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, False, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(data, 0, 2)



##############################################################################

##############################################################################
class asum_operator_h(unittest.TestCase):
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
		"""Test asum  - Array code h. General test.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_02(self):
		"""Test asum  - Array code h. General test with overflow checking on.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=False)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_03(self):
		"""Test asum  - Array code h. General test with overflow checking off.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=True)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_04(self):
		"""Test asum  - Array code h. General test with array limit applied.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_05(self):
		"""Test asum  - Array code h. General test with array limit applied and overflow checking on.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=False, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_06(self):
		"""Test asum  - Array code h. General test with array limit applied and overflow checking off.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=True, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_07(self):
		"""Test asum  - Array code h. Test invalid parameter type for array data.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)

	########################################################
	def test_function_08(self):
		"""Test asum  - Array code h. Test invalid parameter type for overflow flag.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, disovfl='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')

	########################################################
	def test_function_09(self):
		"""Test asum  - Array code h. Test invalid parameter type for limit.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')


	########################################################
	def test_function_10(self):
		"""Test asum  - Array code h. Test no parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_function_11(self):
		"""Test asum  - Array code h. Test too many (four) parameters.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, False, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(data, 0, 2)



##############################################################################

##############################################################################
class asum_operator_H(unittest.TestCase):
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
		"""Test asum  - Array code H. General test.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_02(self):
		"""Test asum  - Array code H. General test with overflow checking on.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=False)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_03(self):
		"""Test asum  - Array code H. General test with overflow checking off.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=True)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_04(self):
		"""Test asum  - Array code H. General test with array limit applied.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_05(self):
		"""Test asum  - Array code H. General test with array limit applied and overflow checking on.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=False, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_06(self):
		"""Test asum  - Array code H. General test with array limit applied and overflow checking off.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=True, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_07(self):
		"""Test asum  - Array code H. Test invalid parameter type for array data.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)

	########################################################
	def test_function_08(self):
		"""Test asum  - Array code H. Test invalid parameter type for overflow flag.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, disovfl='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')

	########################################################
	def test_function_09(self):
		"""Test asum  - Array code H. Test invalid parameter type for limit.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')


	########################################################
	def test_function_10(self):
		"""Test asum  - Array code H. Test no parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_function_11(self):
		"""Test asum  - Array code H. Test too many (four) parameters.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, False, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(data, 0, 2)



##############################################################################

##############################################################################
class asum_operator_i(unittest.TestCase):
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
		"""Test asum  - Array code i. General test.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_02(self):
		"""Test asum  - Array code i. General test with overflow checking on.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=False)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_03(self):
		"""Test asum  - Array code i. General test with overflow checking off.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=True)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_04(self):
		"""Test asum  - Array code i. General test with array limit applied.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_05(self):
		"""Test asum  - Array code i. General test with array limit applied and overflow checking on.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=False, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_06(self):
		"""Test asum  - Array code i. General test with array limit applied and overflow checking off.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=True, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_07(self):
		"""Test asum  - Array code i. Test invalid parameter type for array data.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)

	########################################################
	def test_function_08(self):
		"""Test asum  - Array code i. Test invalid parameter type for overflow flag.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, disovfl='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')

	########################################################
	def test_function_09(self):
		"""Test asum  - Array code i. Test invalid parameter type for limit.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')


	########################################################
	def test_function_10(self):
		"""Test asum  - Array code i. Test no parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_function_11(self):
		"""Test asum  - Array code i. Test too many (four) parameters.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, False, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(data, 0, 2)



##############################################################################

##############################################################################
class asum_operator_I(unittest.TestCase):
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
		"""Test asum  - Array code I. General test.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_02(self):
		"""Test asum  - Array code I. General test with overflow checking on.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=False)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_03(self):
		"""Test asum  - Array code I. General test with overflow checking off.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=True)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_04(self):
		"""Test asum  - Array code I. General test with array limit applied.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_05(self):
		"""Test asum  - Array code I. General test with array limit applied and overflow checking on.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=False, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_06(self):
		"""Test asum  - Array code I. General test with array limit applied and overflow checking off.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=True, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_07(self):
		"""Test asum  - Array code I. Test invalid parameter type for array data.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)

	########################################################
	def test_function_08(self):
		"""Test asum  - Array code I. Test invalid parameter type for overflow flag.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, disovfl='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')

	########################################################
	def test_function_09(self):
		"""Test asum  - Array code I. Test invalid parameter type for limit.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')


	########################################################
	def test_function_10(self):
		"""Test asum  - Array code I. Test no parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_function_11(self):
		"""Test asum  - Array code I. Test too many (four) parameters.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, False, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(data, 0, 2)



##############################################################################

##############################################################################
class asum_operator_l(unittest.TestCase):
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
		"""Test asum  - Array code l. General test.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_02(self):
		"""Test asum  - Array code l. General test with overflow checking on.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=False)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_03(self):
		"""Test asum  - Array code l. General test with overflow checking off.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=True)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_04(self):
		"""Test asum  - Array code l. General test with array limit applied.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_05(self):
		"""Test asum  - Array code l. General test with array limit applied and overflow checking on.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=False, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_06(self):
		"""Test asum  - Array code l. General test with array limit applied and overflow checking off.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=True, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_07(self):
		"""Test asum  - Array code l. Test invalid parameter type for array data.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)

	########################################################
	def test_function_08(self):
		"""Test asum  - Array code l. Test invalid parameter type for overflow flag.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, disovfl='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')

	########################################################
	def test_function_09(self):
		"""Test asum  - Array code l. Test invalid parameter type for limit.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')


	########################################################
	def test_function_10(self):
		"""Test asum  - Array code l. Test no parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_function_11(self):
		"""Test asum  - Array code l. Test too many (four) parameters.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, False, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(data, 0, 2)



	########################################################
	def test_function_12(self):
		"""Test asum  - Array code l. Arithmetic positive overflow expected.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), [self.MaxVal] * 10, range(11,-88,-3)))
		
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(data)


	########################################################
	def test_function_13(self):
		"""Test asum  - Array code l. Arithmetic overflow expected for negative numbers.
		"""
		data = array.array('l', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(data)


##############################################################################

##############################################################################
class asum_operator_L(unittest.TestCase):
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
		"""Test asum  - Array code L. General test.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_02(self):
		"""Test asum  - Array code L. General test with overflow checking on.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=False)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_03(self):
		"""Test asum  - Array code L. General test with overflow checking off.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=True)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_04(self):
		"""Test asum  - Array code L. General test with array limit applied.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_05(self):
		"""Test asum  - Array code L. General test with array limit applied and overflow checking on.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=False, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_06(self):
		"""Test asum  - Array code L. General test with array limit applied and overflow checking off.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=True, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_07(self):
		"""Test asum  - Array code L. Test invalid parameter type for array data.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)

	########################################################
	def test_function_08(self):
		"""Test asum  - Array code L. Test invalid parameter type for overflow flag.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, disovfl='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')

	########################################################
	def test_function_09(self):
		"""Test asum  - Array code L. Test invalid parameter type for limit.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')


	########################################################
	def test_function_10(self):
		"""Test asum  - Array code L. Test no parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_function_11(self):
		"""Test asum  - Array code L. Test too many (four) parameters.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, False, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(data, 0, 2)



	########################################################
	def test_function_12(self):
		"""Test asum  - Array code L. Arithmetic positive overflow expected.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), [self.MaxVal] * 10, range(88,12,-3)))
		
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(data)


##############################################################################

##############################################################################
# Cannot test if 'q' or 'Q' arrays are not supported in this architecture.
@unittest.skipIf('q' not in array.typecodes, 'Skip test if array type not supported on this platform.')
class asum_operator_q(unittest.TestCase):
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
		"""Test asum  - Array code q. General test.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_02(self):
		"""Test asum  - Array code q. General test with overflow checking on.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=False)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_03(self):
		"""Test asum  - Array code q. General test with overflow checking off.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=True)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_04(self):
		"""Test asum  - Array code q. General test with array limit applied.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_05(self):
		"""Test asum  - Array code q. General test with array limit applied and overflow checking on.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=False, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_06(self):
		"""Test asum  - Array code q. General test with array limit applied and overflow checking off.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.asum(data, disovfl=True, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_07(self):
		"""Test asum  - Array code q. Test invalid parameter type for array data.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)

	########################################################
	def test_function_08(self):
		"""Test asum  - Array code q. Test invalid parameter type for overflow flag.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, disovfl='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')

	########################################################
	def test_function_09(self):
		"""Test asum  - Array code q. Test invalid parameter type for limit.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')


	########################################################
	def test_function_10(self):
		"""Test asum  - Array code q. Test no parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_function_11(self):
		"""Test asum  - Array code q. Test too many (four) parameters.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, False, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(data, 0, 2)



	########################################################
	def test_function_12(self):
		"""Test asum  - Array code q. Arithmetic positive overflow expected.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), [self.MaxVal] * 10, range(11,-88,-3)))
		
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(data)


	########################################################
	def test_function_13(self):
		"""Test asum  - Array code q. Arithmetic overflow expected for negative numbers.
		"""
		data = array.array('q', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(data)


##############################################################################

##############################################################################
# Cannot test if 'q' or 'Q' arrays are not supported in this architecture.
@unittest.skipIf('Q' not in array.typecodes, 'Skip test if array type not supported on this platform.')
class asum_operator_Q(unittest.TestCase):
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
		"""Test asum  - Array code Q. General test.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_02(self):
		"""Test asum  - Array code Q. General test with overflow checking on.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=False)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_03(self):
		"""Test asum  - Array code Q. General test with overflow checking off.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=True)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_04(self):
		"""Test asum  - Array code Q. General test with array limit applied.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_05(self):
		"""Test asum  - Array code Q. General test with array limit applied and overflow checking on.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=False, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_06(self):
		"""Test asum  - Array code Q. General test with array limit applied and overflow checking off.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.asum(data, disovfl=True, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_07(self):
		"""Test asum  - Array code Q. Test invalid parameter type for array data.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)

	########################################################
	def test_function_08(self):
		"""Test asum  - Array code Q. Test invalid parameter type for overflow flag.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, disovfl='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')

	########################################################
	def test_function_09(self):
		"""Test asum  - Array code Q. Test invalid parameter type for limit.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')


	########################################################
	def test_function_10(self):
		"""Test asum  - Array code Q. Test no parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_function_11(self):
		"""Test asum  - Array code Q. Test too many (four) parameters.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, False, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(data, 0, 2)



	########################################################
	def test_function_12(self):
		"""Test asum  - Array code Q. Arithmetic positive overflow expected.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), [self.MaxVal] * 10, range(88,12,-3)))
		
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(data)


##############################################################################

##############################################################################
class asum_operator_f(unittest.TestCase):
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
		"""Test asum  - Array code f. General test.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		result = arrayfunc.asum(data)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_02(self):
		"""Test asum  - Array code f. General test with overflow checking on.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		result = arrayfunc.asum(data, disovfl=False)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_03(self):
		"""Test asum  - Array code f. General test with overflow checking off.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		result = arrayfunc.asum(data, disovfl=True)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_04(self):
		"""Test asum  - Array code f. General test with array limit applied.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		result = arrayfunc.asum(data, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_05(self):
		"""Test asum  - Array code f. General test with array limit applied and overflow checking on.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		result = arrayfunc.asum(data, disovfl=False, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_06(self):
		"""Test asum  - Array code f. General test with array limit applied and overflow checking off.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		result = arrayfunc.asum(data, disovfl=True, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_07(self):
		"""Test asum  - Array code f. Test invalid parameter type for array data.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)

	########################################################
	def test_function_08(self):
		"""Test asum  - Array code f. Test invalid parameter type for overflow flag.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, disovfl='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')

	########################################################
	def test_function_09(self):
		"""Test asum  - Array code f. Test invalid parameter type for limit.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')


	########################################################
	def test_function_10(self):
		"""Test asum  - Array code f. Test no parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_function_11(self):
		"""Test asum  - Array code f. Test too many (four) parameters.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, False, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(data, 0, 2)



	########################################################
	def test_function_12(self):
		"""Test asum  - Array code f. Arithmetic positive overflow expected.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), [self.MaxVal] * 10, range(11,-88,-3))])
		
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(data)


	########################################################
	def test_function_13(self):
		"""Test asum  - Array code f. Arithmetic overflow expected for negative numbers.
		"""
		data = array.array('f', [float(x) for x in itertools.chain([self.MinVal] * 10, range(1,10,2), [self.MinVal] * 10)])
		
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(data)


##############################################################################

##############################################################################
class asum_operator_d(unittest.TestCase):
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
		"""Test asum  - Array code d. General test.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		result = arrayfunc.asum(data)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_02(self):
		"""Test asum  - Array code d. General test with overflow checking on.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		result = arrayfunc.asum(data, disovfl=False)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_03(self):
		"""Test asum  - Array code d. General test with overflow checking off.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		result = arrayfunc.asum(data, disovfl=True)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_04(self):
		"""Test asum  - Array code d. General test with array limit applied.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		result = arrayfunc.asum(data, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_05(self):
		"""Test asum  - Array code d. General test with array limit applied and overflow checking on.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		result = arrayfunc.asum(data, disovfl=False, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_06(self):
		"""Test asum  - Array code d. General test with array limit applied and overflow checking off.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		result = arrayfunc.asum(data, disovfl=True, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_07(self):
		"""Test asum  - Array code d. Test invalid parameter type for array data.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)

	########################################################
	def test_function_08(self):
		"""Test asum  - Array code d. Test invalid parameter type for overflow flag.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, disovfl='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')

	########################################################
	def test_function_09(self):
		"""Test asum  - Array code d. Test invalid parameter type for limit.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')


	########################################################
	def test_function_10(self):
		"""Test asum  - Array code d. Test no parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_function_11(self):
		"""Test asum  - Array code d. Test too many (four) parameters.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, False, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(data, 0, 2)



	########################################################
	def test_function_12(self):
		"""Test asum  - Array code d. Arithmetic positive overflow expected.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), [self.MaxVal] * 10, range(11,-88,-3))])
		
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(data)


	########################################################
	def test_function_13(self):
		"""Test asum  - Array code d. Arithmetic overflow expected for negative numbers.
		"""
		data = array.array('d', [float(x) for x in itertools.chain([self.MinVal] * 10, range(1,10,2), [self.MinVal] * 10)])
		
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(data)


##############################################################################

##############################################################################
class asum_operator_bytes(unittest.TestCase):
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
		"""Test asum  - Array code bytes. General test.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		data = bytes(data)
		result = arrayfunc.asum(data)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_02(self):
		"""Test asum  - Array code bytes. General test with overflow checking on.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		data = bytes(data)
		result = arrayfunc.asum(data, disovfl=False)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_03(self):
		"""Test asum  - Array code bytes. General test with overflow checking off.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		data = bytes(data)
		result = arrayfunc.asum(data, disovfl=True)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_04(self):
		"""Test asum  - Array code bytes. General test with array limit applied.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		data = bytes(data)
		result = arrayfunc.asum(data, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_05(self):
		"""Test asum  - Array code bytes. General test with array limit applied and overflow checking on.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		data = bytes(data)
		result = arrayfunc.asum(data, disovfl=False, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_06(self):
		"""Test asum  - Array code bytes. General test with array limit applied and overflow checking off.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		data = bytes(data)
		result = arrayfunc.asum(data, disovfl=True, maxlen=10)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_07(self):
		"""Test asum  - Array code bytes. Test invalid parameter type for array data.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)

	########################################################
	def test_function_08(self):
		"""Test asum  - Array code bytes. Test invalid parameter type for overflow flag.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		data = bytes(data)
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, disovfl='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')

	########################################################
	def test_function_09(self):
		"""Test asum  - Array code bytes. Test invalid parameter type for limit.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		data = bytes(data)
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, maxlen='a')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')


	########################################################
	def test_function_10(self):
		"""Test asum  - Array code bytes. Test no parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_function_11(self):
		"""Test asum  - Array code bytes. Test too many (four) parameters.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		data = bytes(data)
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, False, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(data, 0, 2)



##############################################################################
class asum_nan_f(unittest.TestCase):
	"""Test with floating point nan inf, and -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min

		self.data_nan = array.array('f', [-1.0, 0.0, 1.0, float('nan'), self.MaxVal, self.MinVal, 100.5])
		self.data_inf = array.array('f', [-1.0, 0.0, 1.0, float('inf'), self.MaxVal, self.MinVal, 100.5])
		self.data_ninf = array.array('f', [-1.0, 0.0, 1.0, float('-inf'), self.MaxVal, self.MinVal, 100.5])


	########################################################
	def test_nan_01(self):
		"""Test array with nan - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)

	########################################################
	def test_nan_02(self):
		"""Test array with infinity - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)

	########################################################
	def test_nan_03(self):
		"""Test array with negative infinity - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


##############################################################################


##############################################################################
class asum_nan_d(unittest.TestCase):
	"""Test with floating point nan inf, and -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min

		self.data_nan = array.array('d', [-1.0, 0.0, 1.0, float('nan'), self.MaxVal, self.MinVal, 100.5])
		self.data_inf = array.array('d', [-1.0, 0.0, 1.0, float('inf'), self.MaxVal, self.MinVal, 100.5])
		self.data_ninf = array.array('d', [-1.0, 0.0, 1.0, float('-inf'), self.MaxVal, self.MinVal, 100.5])


	########################################################
	def test_nan_01(self):
		"""Test array with nan - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)

	########################################################
	def test_nan_02(self):
		"""Test array with infinity - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)

	########################################################
	def test_nan_03(self):
		"""Test array with negative infinity - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)


##############################################################################


##############################################################################
if __name__ == '__main__':
    unittest.main()

##############################################################################
