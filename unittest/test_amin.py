#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_amin.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     11-Jun-2014.
# Ver:      14-Aug-2015.
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
"""This conducts unit tests for amin.
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
class amin_operator_b(unittest.TestCase):
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
		"""Test amin  - Array code b. General test.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_02(self):
		"""Test amin  - Array code b. Test increasing values.
		"""
		data = array.array('b', range(1,100))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_03(self):
		"""Test amin  - Array code b. Test decreasing values.
		"""
		data = array.array('b', range(100,1,-1))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_04(self):
		"""Test amin  - Array code b. Test finding max for data type.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_05(self):
		"""Test amin  - Array code b. Test finding value from array that contains min for data type.
		"""
		data = array.array('b', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_06(self):
		"""Test amin  - Array code b. Test optional lim parameter.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		
		result = arrayfunc.amin(data, maxlen=5)
		self.assertEqual(result, min(data[:5]))


	########################################################
	def test_function_07(self):
		"""Test amin  - Array code b. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(1)


	########################################################
	def test_function_08(self):
		"""Test amin  - Array code b. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min()


	########################################################
	def test_function_09(self):
		"""Test amin  - Array code b. Test excess parameters.
		"""
		data = array.array('b', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(data, 5, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(data, 2)


##############################################################################



##############################################################################
class amin_operator_B(unittest.TestCase):
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
		"""Test amin  - Array code B. General test.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_02(self):
		"""Test amin  - Array code B. Test increasing values.
		"""
		data = array.array('B', range(1,100))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_03(self):
		"""Test amin  - Array code B. Test decreasing values.
		"""
		data = array.array('B', range(100,1,-1))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_04(self):
		"""Test amin  - Array code B. Test finding max for data type.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_05(self):
		"""Test amin  - Array code B. Test finding value from array that contains min for data type.
		"""
		data = array.array('B', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_06(self):
		"""Test amin  - Array code B. Test optional lim parameter.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		
		result = arrayfunc.amin(data, maxlen=5)
		self.assertEqual(result, min(data[:5]))


	########################################################
	def test_function_07(self):
		"""Test amin  - Array code B. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(1)


	########################################################
	def test_function_08(self):
		"""Test amin  - Array code B. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min()


	########################################################
	def test_function_09(self):
		"""Test amin  - Array code B. Test excess parameters.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(data, 5, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(data, 2)


##############################################################################



##############################################################################
class amin_operator_h(unittest.TestCase):
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
		"""Test amin  - Array code h. General test.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_02(self):
		"""Test amin  - Array code h. Test increasing values.
		"""
		data = array.array('h', range(1,100))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_03(self):
		"""Test amin  - Array code h. Test decreasing values.
		"""
		data = array.array('h', range(100,1,-1))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_04(self):
		"""Test amin  - Array code h. Test finding max for data type.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_05(self):
		"""Test amin  - Array code h. Test finding value from array that contains min for data type.
		"""
		data = array.array('h', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_06(self):
		"""Test amin  - Array code h. Test optional lim parameter.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		
		result = arrayfunc.amin(data, maxlen=5)
		self.assertEqual(result, min(data[:5]))


	########################################################
	def test_function_07(self):
		"""Test amin  - Array code h. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(1)


	########################################################
	def test_function_08(self):
		"""Test amin  - Array code h. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min()


	########################################################
	def test_function_09(self):
		"""Test amin  - Array code h. Test excess parameters.
		"""
		data = array.array('h', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(data, 5, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(data, 2)


##############################################################################



##############################################################################
class amin_operator_H(unittest.TestCase):
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
		"""Test amin  - Array code H. General test.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_02(self):
		"""Test amin  - Array code H. Test increasing values.
		"""
		data = array.array('H', range(1,100))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_03(self):
		"""Test amin  - Array code H. Test decreasing values.
		"""
		data = array.array('H', range(100,1,-1))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_04(self):
		"""Test amin  - Array code H. Test finding max for data type.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_05(self):
		"""Test amin  - Array code H. Test finding value from array that contains min for data type.
		"""
		data = array.array('H', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_06(self):
		"""Test amin  - Array code H. Test optional lim parameter.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		
		result = arrayfunc.amin(data, maxlen=5)
		self.assertEqual(result, min(data[:5]))


	########################################################
	def test_function_07(self):
		"""Test amin  - Array code H. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(1)


	########################################################
	def test_function_08(self):
		"""Test amin  - Array code H. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min()


	########################################################
	def test_function_09(self):
		"""Test amin  - Array code H. Test excess parameters.
		"""
		data = array.array('H', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(data, 5, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(data, 2)


##############################################################################



##############################################################################
class amin_operator_i(unittest.TestCase):
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
		"""Test amin  - Array code i. General test.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_02(self):
		"""Test amin  - Array code i. Test increasing values.
		"""
		data = array.array('i', range(1,100))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_03(self):
		"""Test amin  - Array code i. Test decreasing values.
		"""
		data = array.array('i', range(100,1,-1))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_04(self):
		"""Test amin  - Array code i. Test finding max for data type.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_05(self):
		"""Test amin  - Array code i. Test finding value from array that contains min for data type.
		"""
		data = array.array('i', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_06(self):
		"""Test amin  - Array code i. Test optional lim parameter.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		
		result = arrayfunc.amin(data, maxlen=5)
		self.assertEqual(result, min(data[:5]))


	########################################################
	def test_function_07(self):
		"""Test amin  - Array code i. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(1)


	########################################################
	def test_function_08(self):
		"""Test amin  - Array code i. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min()


	########################################################
	def test_function_09(self):
		"""Test amin  - Array code i. Test excess parameters.
		"""
		data = array.array('i', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(data, 5, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(data, 2)


##############################################################################



##############################################################################
class amin_operator_I(unittest.TestCase):
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
		"""Test amin  - Array code I. General test.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_02(self):
		"""Test amin  - Array code I. Test increasing values.
		"""
		data = array.array('I', range(1,100))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_03(self):
		"""Test amin  - Array code I. Test decreasing values.
		"""
		data = array.array('I', range(100,1,-1))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_04(self):
		"""Test amin  - Array code I. Test finding max for data type.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_05(self):
		"""Test amin  - Array code I. Test finding value from array that contains min for data type.
		"""
		data = array.array('I', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_06(self):
		"""Test amin  - Array code I. Test optional lim parameter.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		
		result = arrayfunc.amin(data, maxlen=5)
		self.assertEqual(result, min(data[:5]))


	########################################################
	def test_function_07(self):
		"""Test amin  - Array code I. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(1)


	########################################################
	def test_function_08(self):
		"""Test amin  - Array code I. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min()


	########################################################
	def test_function_09(self):
		"""Test amin  - Array code I. Test excess parameters.
		"""
		data = array.array('I', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(data, 5, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(data, 2)


##############################################################################



##############################################################################
class amin_operator_l(unittest.TestCase):
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
		"""Test amin  - Array code l. General test.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_02(self):
		"""Test amin  - Array code l. Test increasing values.
		"""
		data = array.array('l', range(1,100))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_03(self):
		"""Test amin  - Array code l. Test decreasing values.
		"""
		data = array.array('l', range(100,1,-1))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_04(self):
		"""Test amin  - Array code l. Test finding max for data type.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_05(self):
		"""Test amin  - Array code l. Test finding value from array that contains min for data type.
		"""
		data = array.array('l', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_06(self):
		"""Test amin  - Array code l. Test optional lim parameter.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		
		result = arrayfunc.amin(data, maxlen=5)
		self.assertEqual(result, min(data[:5]))


	########################################################
	def test_function_07(self):
		"""Test amin  - Array code l. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(1)


	########################################################
	def test_function_08(self):
		"""Test amin  - Array code l. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min()


	########################################################
	def test_function_09(self):
		"""Test amin  - Array code l. Test excess parameters.
		"""
		data = array.array('l', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(data, 5, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(data, 2)


##############################################################################



##############################################################################
class amin_operator_L(unittest.TestCase):
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
		"""Test amin  - Array code L. General test.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_02(self):
		"""Test amin  - Array code L. Test increasing values.
		"""
		data = array.array('L', range(1,100))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_03(self):
		"""Test amin  - Array code L. Test decreasing values.
		"""
		data = array.array('L', range(100,1,-1))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_04(self):
		"""Test amin  - Array code L. Test finding max for data type.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_05(self):
		"""Test amin  - Array code L. Test finding value from array that contains min for data type.
		"""
		data = array.array('L', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_06(self):
		"""Test amin  - Array code L. Test optional lim parameter.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		
		result = arrayfunc.amin(data, maxlen=5)
		self.assertEqual(result, min(data[:5]))


	########################################################
	def test_function_07(self):
		"""Test amin  - Array code L. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(1)


	########################################################
	def test_function_08(self):
		"""Test amin  - Array code L. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min()


	########################################################
	def test_function_09(self):
		"""Test amin  - Array code L. Test excess parameters.
		"""
		data = array.array('L', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(data, 5, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(data, 2)


##############################################################################



##############################################################################
# Cannot test if 'q' or 'Q' arrays are not supported in this architecture.
@unittest.skipIf('q' not in array.typecodes, 'Skip test if array type not supported on this platform.')
class amin_operator_q(unittest.TestCase):
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
		"""Test amin  - Array code q. General test.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_02(self):
		"""Test amin  - Array code q. Test increasing values.
		"""
		data = array.array('q', range(1,100))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_03(self):
		"""Test amin  - Array code q. Test decreasing values.
		"""
		data = array.array('q', range(100,1,-1))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_04(self):
		"""Test amin  - Array code q. Test finding max for data type.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_05(self):
		"""Test amin  - Array code q. Test finding value from array that contains min for data type.
		"""
		data = array.array('q', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_06(self):
		"""Test amin  - Array code q. Test optional lim parameter.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3)))
		
		result = arrayfunc.amin(data, maxlen=5)
		self.assertEqual(result, min(data[:5]))


	########################################################
	def test_function_07(self):
		"""Test amin  - Array code q. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(1)


	########################################################
	def test_function_08(self):
		"""Test amin  - Array code q. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min()


	########################################################
	def test_function_09(self):
		"""Test amin  - Array code q. Test excess parameters.
		"""
		data = array.array('q', itertools.chain(range(1,10,2), range(11,-88,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(data, 5, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(data, 2)


##############################################################################



##############################################################################
# Cannot test if 'q' or 'Q' arrays are not supported in this architecture.
@unittest.skipIf('Q' not in array.typecodes, 'Skip test if array type not supported on this platform.')
class amin_operator_Q(unittest.TestCase):
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
		"""Test amin  - Array code Q. General test.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_02(self):
		"""Test amin  - Array code Q. Test increasing values.
		"""
		data = array.array('Q', range(1,100))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_03(self):
		"""Test amin  - Array code Q. Test decreasing values.
		"""
		data = array.array('Q', range(100,1,-1))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_04(self):
		"""Test amin  - Array code Q. Test finding max for data type.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_05(self):
		"""Test amin  - Array code Q. Test finding value from array that contains min for data type.
		"""
		data = array.array('Q', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_06(self):
		"""Test amin  - Array code Q. Test optional lim parameter.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		
		result = arrayfunc.amin(data, maxlen=5)
		self.assertEqual(result, min(data[:5]))


	########################################################
	def test_function_07(self):
		"""Test amin  - Array code Q. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(1)


	########################################################
	def test_function_08(self):
		"""Test amin  - Array code Q. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min()


	########################################################
	def test_function_09(self):
		"""Test amin  - Array code Q. Test excess parameters.
		"""
		data = array.array('Q', itertools.chain(range(1,10,2), range(88,12,-3)))
		
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(data, 5, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(data, 2)


##############################################################################



##############################################################################
class amin_operator_f(unittest.TestCase):
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
		"""Test amin  - Array code f. General test.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_02(self):
		"""Test amin  - Array code f. Test increasing values.
		"""
		data = array.array('f', [float(x) for x in range(1,100)])
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_03(self):
		"""Test amin  - Array code f. Test decreasing values.
		"""
		data = array.array('f', [float(x) for x in range(100,1,-1)])
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_04(self):
		"""Test amin  - Array code f. Test finding max for data type.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3))])
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_05(self):
		"""Test amin  - Array code f. Test finding value from array that contains min for data type.
		"""
		data = array.array('f', [float(x) for x in itertools.chain([self.MinVal] * 10, range(1,10,2), [self.MinVal] * 10)])
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_06(self):
		"""Test amin  - Array code f. Test optional lim parameter.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3))])
		
		result = arrayfunc.amin(data, maxlen=5)
		self.assertEqual(result, min(data[:5]))


	########################################################
	def test_function_07(self):
		"""Test amin  - Array code f. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(1)


	########################################################
	def test_function_08(self):
		"""Test amin  - Array code f. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min()


	########################################################
	def test_function_09(self):
		"""Test amin  - Array code f. Test excess parameters.
		"""
		data = array.array('f', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(data, 5, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(data, 2)


##############################################################################



##############################################################################
class amin_operator_d(unittest.TestCase):
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
		"""Test amin  - Array code d. General test.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_02(self):
		"""Test amin  - Array code d. Test increasing values.
		"""
		data = array.array('d', [float(x) for x in range(1,100)])
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_03(self):
		"""Test amin  - Array code d. Test decreasing values.
		"""
		data = array.array('d', [float(x) for x in range(100,1,-1)])
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_04(self):
		"""Test amin  - Array code d. Test finding max for data type.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3))])
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_05(self):
		"""Test amin  - Array code d. Test finding value from array that contains min for data type.
		"""
		data = array.array('d', [float(x) for x in itertools.chain([self.MinVal] * 10, range(1,10,2), [self.MinVal] * 10)])
		
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_06(self):
		"""Test amin  - Array code d. Test optional lim parameter.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3))])
		
		result = arrayfunc.amin(data, maxlen=5)
		self.assertEqual(result, min(data[:5]))


	########################################################
	def test_function_07(self):
		"""Test amin  - Array code d. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(1)


	########################################################
	def test_function_08(self):
		"""Test amin  - Array code d. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min()


	########################################################
	def test_function_09(self):
		"""Test amin  - Array code d. Test excess parameters.
		"""
		data = array.array('d', [float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))])
		
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(data, 5, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(data, 2)


##############################################################################



##############################################################################
class amin_operator_bytes(unittest.TestCase):
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
		"""Test amin  - Array code bytes. General test.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		data = bytes(data)
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_02(self):
		"""Test amin  - Array code bytes. Test increasing values.
		"""
		data = array.array('B', range(1,100))
		data = bytes(data)
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_03(self):
		"""Test amin  - Array code bytes. Test decreasing values.
		"""
		data = array.array('B', range(100,1,-1))
		data = bytes(data)
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_04(self):
		"""Test amin  - Array code bytes. Test finding max for data type.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		data = bytes(data)
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_05(self):
		"""Test amin  - Array code bytes. Test finding value from array that contains min for data type.
		"""
		data = array.array('B', itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10))
		data = bytes(data)
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_06(self):
		"""Test amin  - Array code bytes. Test optional lim parameter.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3)))
		data = bytes(data)
		result = arrayfunc.amin(data, maxlen=5)
		self.assertEqual(result, min(data[:5]))


	########################################################
	def test_function_07(self):
		"""Test amin  - Array code bytes. Test invalid parameter type.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(1)


	########################################################
	def test_function_08(self):
		"""Test amin  - Array code bytes. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min()


	########################################################
	def test_function_09(self):
		"""Test amin  - Array code bytes. Test excess parameters.
		"""
		data = array.array('B', itertools.chain(range(1,10,2), range(88,12,-3)))
		data = bytes(data)
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(data, 5, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(data, 2)


##############################################################################


##############################################################################
class amin_nan_f(unittest.TestCase):
	"""Test with floating point nan, inf -inf.
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
		self.data_mixed = array.array('f', [float('inf'), 0.0, float('-inf'), float('nan'), self.MaxVal, self.MinVal, 100.5])


	########################################################
	def rottest(self, x, rotplaces):
		"""Modify the test data by shifting the data in the array.
		"""
		return x[rotplaces:] + x[:rotplaces]


##############################################################################
class amin_nan_d(unittest.TestCase):
	"""Test with floating point nan, inf -inf.
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
		self.data_mixed = array.array('d', [float('inf'), 0.0, float('-inf'), float('nan'), self.MaxVal, self.MinVal, 100.5])


	########################################################
	def rottest(self, x, rotplaces):
		"""Modify the test data by shifting the data in the array.
		"""
		return x[rotplaces:] + x[:rotplaces]


##############################################################################
class amin_nan_f(unittest.TestCase):
	"""Test with floating point nan, inf -inf.
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
		self.data_mixed = array.array('f', [float('inf'), 0.0, float('-inf'), float('nan'), self.MaxVal, self.MinVal, 100.5])


	########################################################
	def rottest(self, x, rotplaces):
		"""Modify the test data by shifting the data in the array.
		"""
		return x[rotplaces:] + x[:rotplaces]


	########################################################
	def test_nan_0(self):
		"""Test array with nan - Array code f.
		"""
		data = self.rottest(self.data_nan, 0)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_nan_1(self):
		"""Test array with nan - Array code f.
		"""
		data = self.rottest(self.data_nan, 1)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_nan_2(self):
		"""Test array with nan - Array code f.
		"""
		data = self.rottest(self.data_nan, 2)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_nan_3(self):
		"""Test array with nan - Array code f.
		"""
		data = self.rottest(self.data_nan, 3)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_nan_4(self):
		"""Test array with nan - Array code f.
		"""
		data = self.rottest(self.data_nan, 4)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_nan_5(self):
		"""Test array with nan - Array code f.
		"""
		data = self.rottest(self.data_nan, 5)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_nan_6(self):
		"""Test array with nan - Array code f.
		"""
		data = self.rottest(self.data_nan, 6)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_inf_0(self):
		"""Test array with inf - Array code f.
		"""
		data = self.rottest(self.data_inf, 0)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_inf_1(self):
		"""Test array with inf - Array code f.
		"""
		data = self.rottest(self.data_inf, 1)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_inf_2(self):
		"""Test array with inf - Array code f.
		"""
		data = self.rottest(self.data_inf, 2)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_inf_3(self):
		"""Test array with inf - Array code f.
		"""
		data = self.rottest(self.data_inf, 3)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_inf_4(self):
		"""Test array with inf - Array code f.
		"""
		data = self.rottest(self.data_inf, 4)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_inf_5(self):
		"""Test array with inf - Array code f.
		"""
		data = self.rottest(self.data_inf, 5)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_inf_6(self):
		"""Test array with inf - Array code f.
		"""
		data = self.rottest(self.data_inf, 6)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_ninf_0(self):
		"""Test array with ninf - Array code f.
		"""
		data = self.rottest(self.data_ninf, 0)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_ninf_1(self):
		"""Test array with ninf - Array code f.
		"""
		data = self.rottest(self.data_ninf, 1)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_ninf_2(self):
		"""Test array with ninf - Array code f.
		"""
		data = self.rottest(self.data_ninf, 2)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_ninf_3(self):
		"""Test array with ninf - Array code f.
		"""
		data = self.rottest(self.data_ninf, 3)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_ninf_4(self):
		"""Test array with ninf - Array code f.
		"""
		data = self.rottest(self.data_ninf, 4)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_ninf_5(self):
		"""Test array with ninf - Array code f.
		"""
		data = self.rottest(self.data_ninf, 5)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_ninf_6(self):
		"""Test array with ninf - Array code f.
		"""
		data = self.rottest(self.data_ninf, 6)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_mixed_0(self):
		"""Test array with mixed - Array code f.
		"""
		data = self.rottest(self.data_mixed, 0)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_mixed_1(self):
		"""Test array with mixed - Array code f.
		"""
		data = self.rottest(self.data_mixed, 1)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_mixed_2(self):
		"""Test array with mixed - Array code f.
		"""
		data = self.rottest(self.data_mixed, 2)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_mixed_3(self):
		"""Test array with mixed - Array code f.
		"""
		data = self.rottest(self.data_mixed, 3)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_mixed_4(self):
		"""Test array with mixed - Array code f.
		"""
		data = self.rottest(self.data_mixed, 4)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_mixed_5(self):
		"""Test array with mixed - Array code f.
		"""
		data = self.rottest(self.data_mixed, 5)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_mixed_6(self):
		"""Test array with mixed - Array code f.
		"""
		data = self.rottest(self.data_mixed, 6)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


##############################################################################

##############################################################################
class amin_nan_d(unittest.TestCase):
	"""Test with floating point nan, inf -inf.
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
		self.data_mixed = array.array('d', [float('inf'), 0.0, float('-inf'), float('nan'), self.MaxVal, self.MinVal, 100.5])


	########################################################
	def rottest(self, x, rotplaces):
		"""Modify the test data by shifting the data in the array.
		"""
		return x[rotplaces:] + x[:rotplaces]


	########################################################
	def test_nan_0(self):
		"""Test array with nan - Array code d.
		"""
		data = self.rottest(self.data_nan, 0)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_nan_1(self):
		"""Test array with nan - Array code d.
		"""
		data = self.rottest(self.data_nan, 1)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_nan_2(self):
		"""Test array with nan - Array code d.
		"""
		data = self.rottest(self.data_nan, 2)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_nan_3(self):
		"""Test array with nan - Array code d.
		"""
		data = self.rottest(self.data_nan, 3)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_nan_4(self):
		"""Test array with nan - Array code d.
		"""
		data = self.rottest(self.data_nan, 4)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_nan_5(self):
		"""Test array with nan - Array code d.
		"""
		data = self.rottest(self.data_nan, 5)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_nan_6(self):
		"""Test array with nan - Array code d.
		"""
		data = self.rottest(self.data_nan, 6)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_inf_0(self):
		"""Test array with inf - Array code d.
		"""
		data = self.rottest(self.data_inf, 0)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_inf_1(self):
		"""Test array with inf - Array code d.
		"""
		data = self.rottest(self.data_inf, 1)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_inf_2(self):
		"""Test array with inf - Array code d.
		"""
		data = self.rottest(self.data_inf, 2)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_inf_3(self):
		"""Test array with inf - Array code d.
		"""
		data = self.rottest(self.data_inf, 3)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_inf_4(self):
		"""Test array with inf - Array code d.
		"""
		data = self.rottest(self.data_inf, 4)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_inf_5(self):
		"""Test array with inf - Array code d.
		"""
		data = self.rottest(self.data_inf, 5)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_inf_6(self):
		"""Test array with inf - Array code d.
		"""
		data = self.rottest(self.data_inf, 6)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_ninf_0(self):
		"""Test array with ninf - Array code d.
		"""
		data = self.rottest(self.data_ninf, 0)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_ninf_1(self):
		"""Test array with ninf - Array code d.
		"""
		data = self.rottest(self.data_ninf, 1)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_ninf_2(self):
		"""Test array with ninf - Array code d.
		"""
		data = self.rottest(self.data_ninf, 2)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_ninf_3(self):
		"""Test array with ninf - Array code d.
		"""
		data = self.rottest(self.data_ninf, 3)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_ninf_4(self):
		"""Test array with ninf - Array code d.
		"""
		data = self.rottest(self.data_ninf, 4)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_ninf_5(self):
		"""Test array with ninf - Array code d.
		"""
		data = self.rottest(self.data_ninf, 5)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_ninf_6(self):
		"""Test array with ninf - Array code d.
		"""
		data = self.rottest(self.data_ninf, 6)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_mixed_0(self):
		"""Test array with mixed - Array code d.
		"""
		data = self.rottest(self.data_mixed, 0)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_mixed_1(self):
		"""Test array with mixed - Array code d.
		"""
		data = self.rottest(self.data_mixed, 1)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_mixed_2(self):
		"""Test array with mixed - Array code d.
		"""
		data = self.rottest(self.data_mixed, 2)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_mixed_3(self):
		"""Test array with mixed - Array code d.
		"""
		data = self.rottest(self.data_mixed, 3)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_mixed_4(self):
		"""Test array with mixed - Array code d.
		"""
		data = self.rottest(self.data_mixed, 4)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_mixed_5(self):
		"""Test array with mixed - Array code d.
		"""
		data = self.rottest(self.data_mixed, 5)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


	########################################################
	def test_mixed_6(self):
		"""Test array with mixed - Array code d.
		"""
		data = self.rottest(self.data_mixed, 6)
		result = arrayfunc.amin(data)
		# nan does not equal nan.
		if math.isnan(result):
			self.assertEqual(math.isnan(result), math.isnan(min(data)))
		else:
			self.assertEqual(result, min(data))


##############################################################################

##############################################################################
if __name__ == '__main__':
    unittest.main()

##############################################################################
