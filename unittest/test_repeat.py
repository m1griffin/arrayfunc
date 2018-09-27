#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_repeat.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     11-Jun-2014.
# Ver:      19-Jun-2018.
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
"""This conducts unit tests for repeat.
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
class repeat_b(unittest.TestCase):
	"""Test for basic repeat function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'b'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))

		self.MaxVal = arrayfunc.arraylimits.b_max
		self.MinVal = arrayfunc.arraylimits.b_min


	########################################################
	def test_repeat_01(self):
		"""Test repeat in array code  b - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)
		self.assertEqual(list(self.data), [0]*len(self.data))


	########################################################
	def test_repeat_02(self):
		"""Test repeat in array code  b - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)
		self.assertEqual(list(self.data), [self.MaxVal]*len(self.data))


	########################################################
	def test_repeat_03(self):
		"""Test repeat in array code  b - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)
		self.assertEqual(list(self.data), [self.MinVal]*len(self.data))


	########################################################
	def test_repeat_04(self):
		"""Test repeat in array code  b - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_05(self):
		"""Test repeat in array code  b - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_06(self):
		"""Test repeat in array code  b - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_07(self):
		"""Test repeat in array code  b - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_08(self):
		"""Test repeat in array code  b - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_09(self):
		"""Test repeat in array code  b - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)


	########################################################
	def test_repeat_10(self):
		"""Test repeat in array code  b - Test for parameter overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MaxVal + 1)


	########################################################
	def test_repeat_11(self):
		"""Test repeat in array code  b - Test for parameter underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MinVal - 1)


##############################################################################



##############################################################################
class repeat_B(unittest.TestCase):
	"""Test for basic repeat function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'B'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))

		self.MaxVal = arrayfunc.arraylimits.B_max
		self.MinVal = arrayfunc.arraylimits.B_min


	########################################################
	def test_repeat_01(self):
		"""Test repeat in array code  B - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)
		self.assertEqual(list(self.data), [0]*len(self.data))


	########################################################
	def test_repeat_02(self):
		"""Test repeat in array code  B - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)
		self.assertEqual(list(self.data), [self.MaxVal]*len(self.data))


	########################################################
	def test_repeat_03(self):
		"""Test repeat in array code  B - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)
		self.assertEqual(list(self.data), [self.MinVal]*len(self.data))


	########################################################
	def test_repeat_04(self):
		"""Test repeat in array code  B - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_05(self):
		"""Test repeat in array code  B - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_06(self):
		"""Test repeat in array code  B - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_07(self):
		"""Test repeat in array code  B - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_08(self):
		"""Test repeat in array code  B - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_09(self):
		"""Test repeat in array code  B - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)


	########################################################
	def test_repeat_10(self):
		"""Test repeat in array code  B - Test for parameter overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MaxVal + 1)


	########################################################
	def test_repeat_11(self):
		"""Test repeat in array code  B - Test for parameter underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MinVal - 1)


##############################################################################



##############################################################################
class repeat_h(unittest.TestCase):
	"""Test for basic repeat function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'h'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))

		self.MaxVal = arrayfunc.arraylimits.h_max
		self.MinVal = arrayfunc.arraylimits.h_min


	########################################################
	def test_repeat_01(self):
		"""Test repeat in array code  h - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)
		self.assertEqual(list(self.data), [0]*len(self.data))


	########################################################
	def test_repeat_02(self):
		"""Test repeat in array code  h - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)
		self.assertEqual(list(self.data), [self.MaxVal]*len(self.data))


	########################################################
	def test_repeat_03(self):
		"""Test repeat in array code  h - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)
		self.assertEqual(list(self.data), [self.MinVal]*len(self.data))


	########################################################
	def test_repeat_04(self):
		"""Test repeat in array code  h - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_05(self):
		"""Test repeat in array code  h - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_06(self):
		"""Test repeat in array code  h - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_07(self):
		"""Test repeat in array code  h - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_08(self):
		"""Test repeat in array code  h - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_09(self):
		"""Test repeat in array code  h - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)


	########################################################
	def test_repeat_10(self):
		"""Test repeat in array code  h - Test for parameter overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MaxVal + 1)


	########################################################
	def test_repeat_11(self):
		"""Test repeat in array code  h - Test for parameter underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MinVal - 1)


##############################################################################



##############################################################################
class repeat_H(unittest.TestCase):
	"""Test for basic repeat function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'H'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))

		self.MaxVal = arrayfunc.arraylimits.H_max
		self.MinVal = arrayfunc.arraylimits.H_min


	########################################################
	def test_repeat_01(self):
		"""Test repeat in array code  H - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)
		self.assertEqual(list(self.data), [0]*len(self.data))


	########################################################
	def test_repeat_02(self):
		"""Test repeat in array code  H - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)
		self.assertEqual(list(self.data), [self.MaxVal]*len(self.data))


	########################################################
	def test_repeat_03(self):
		"""Test repeat in array code  H - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)
		self.assertEqual(list(self.data), [self.MinVal]*len(self.data))


	########################################################
	def test_repeat_04(self):
		"""Test repeat in array code  H - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_05(self):
		"""Test repeat in array code  H - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_06(self):
		"""Test repeat in array code  H - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_07(self):
		"""Test repeat in array code  H - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_08(self):
		"""Test repeat in array code  H - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_09(self):
		"""Test repeat in array code  H - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)


	########################################################
	def test_repeat_10(self):
		"""Test repeat in array code  H - Test for parameter overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MaxVal + 1)


	########################################################
	def test_repeat_11(self):
		"""Test repeat in array code  H - Test for parameter underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MinVal - 1)


##############################################################################



##############################################################################
class repeat_i(unittest.TestCase):
	"""Test for basic repeat function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'i'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))

		self.MaxVal = arrayfunc.arraylimits.i_max
		self.MinVal = arrayfunc.arraylimits.i_min


	########################################################
	def test_repeat_01(self):
		"""Test repeat in array code  i - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)
		self.assertEqual(list(self.data), [0]*len(self.data))


	########################################################
	def test_repeat_02(self):
		"""Test repeat in array code  i - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)
		self.assertEqual(list(self.data), [self.MaxVal]*len(self.data))


	########################################################
	def test_repeat_03(self):
		"""Test repeat in array code  i - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)
		self.assertEqual(list(self.data), [self.MinVal]*len(self.data))


	########################################################
	def test_repeat_04(self):
		"""Test repeat in array code  i - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_05(self):
		"""Test repeat in array code  i - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_06(self):
		"""Test repeat in array code  i - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_07(self):
		"""Test repeat in array code  i - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_08(self):
		"""Test repeat in array code  i - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_09(self):
		"""Test repeat in array code  i - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)


	########################################################
	def test_repeat_10(self):
		"""Test repeat in array code  i - Test for parameter overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MaxVal + 1)


	########################################################
	def test_repeat_11(self):
		"""Test repeat in array code  i - Test for parameter underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MinVal - 1)


##############################################################################



##############################################################################
class repeat_I(unittest.TestCase):
	"""Test for basic repeat function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'I'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))

		self.MaxVal = arrayfunc.arraylimits.I_max
		self.MinVal = arrayfunc.arraylimits.I_min


	########################################################
	def test_repeat_01(self):
		"""Test repeat in array code  I - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)
		self.assertEqual(list(self.data), [0]*len(self.data))


	########################################################
	def test_repeat_02(self):
		"""Test repeat in array code  I - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)
		self.assertEqual(list(self.data), [self.MaxVal]*len(self.data))


	########################################################
	def test_repeat_03(self):
		"""Test repeat in array code  I - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)
		self.assertEqual(list(self.data), [self.MinVal]*len(self.data))


	########################################################
	def test_repeat_04(self):
		"""Test repeat in array code  I - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_05(self):
		"""Test repeat in array code  I - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_06(self):
		"""Test repeat in array code  I - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_07(self):
		"""Test repeat in array code  I - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_08(self):
		"""Test repeat in array code  I - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_09(self):
		"""Test repeat in array code  I - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)


	########################################################
	# Whether this test can be peformed depends on the integer word sizes in for this architecture.
	@unittest.skipIf(arrayfunc.arraylimits.I_max == arrayfunc.arraylimits.L_max, 
		'Skip test if I integer does not have overflow checks.')
	def test_repeat_10(self):
		"""Test repeat in array code  I - Test for parameter overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MaxVal + 1)


	########################################################
	# Whether this test can be peformed depends on the integer word sizes in for this architecture.
	@unittest.skipIf(arrayfunc.arraylimits.I_max == arrayfunc.arraylimits.L_max, 
		'Skip test if I integer does not have overflow checks.')
	def test_repeat_11(self):
		"""Test repeat in array code  I - Test for parameter underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MinVal - 1)


##############################################################################



##############################################################################
class repeat_l(unittest.TestCase):
	"""Test for basic repeat function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'l'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min


	########################################################
	def test_repeat_01(self):
		"""Test repeat in array code  l - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)
		self.assertEqual(list(self.data), [0]*len(self.data))


	########################################################
	def test_repeat_02(self):
		"""Test repeat in array code  l - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)
		self.assertEqual(list(self.data), [self.MaxVal]*len(self.data))


	########################################################
	def test_repeat_03(self):
		"""Test repeat in array code  l - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)
		self.assertEqual(list(self.data), [self.MinVal]*len(self.data))


	########################################################
	def test_repeat_04(self):
		"""Test repeat in array code  l - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_05(self):
		"""Test repeat in array code  l - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_06(self):
		"""Test repeat in array code  l - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_07(self):
		"""Test repeat in array code  l - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_08(self):
		"""Test repeat in array code  l - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_09(self):
		"""Test repeat in array code  l - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)


	########################################################
	def test_repeat_10(self):
		"""Test repeat in array code  l - Test for parameter overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MaxVal + 1)


	########################################################
	def test_repeat_11(self):
		"""Test repeat in array code  l - Test for parameter underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MinVal - 1)


##############################################################################



##############################################################################
class repeat_L(unittest.TestCase):
	"""Test for basic repeat function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'L'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))

		self.MaxVal = arrayfunc.arraylimits.L_max
		self.MinVal = arrayfunc.arraylimits.L_min


	########################################################
	def test_repeat_01(self):
		"""Test repeat in array code  L - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)
		self.assertEqual(list(self.data), [0]*len(self.data))


	########################################################
	def test_repeat_02(self):
		"""Test repeat in array code  L - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)
		self.assertEqual(list(self.data), [self.MaxVal]*len(self.data))


	########################################################
	def test_repeat_03(self):
		"""Test repeat in array code  L - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)
		self.assertEqual(list(self.data), [self.MinVal]*len(self.data))


	########################################################
	def test_repeat_04(self):
		"""Test repeat in array code  L - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_05(self):
		"""Test repeat in array code  L - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_06(self):
		"""Test repeat in array code  L - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_07(self):
		"""Test repeat in array code  L - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_08(self):
		"""Test repeat in array code  L - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_09(self):
		"""Test repeat in array code  L - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)


##############################################################################



##############################################################################
class repeat_q(unittest.TestCase):
	"""Test for basic repeat function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'q'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min


	########################################################
	def test_repeat_01(self):
		"""Test repeat in array code  q - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)
		self.assertEqual(list(self.data), [0]*len(self.data))


	########################################################
	def test_repeat_02(self):
		"""Test repeat in array code  q - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)
		self.assertEqual(list(self.data), [self.MaxVal]*len(self.data))


	########################################################
	def test_repeat_03(self):
		"""Test repeat in array code  q - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)
		self.assertEqual(list(self.data), [self.MinVal]*len(self.data))


	########################################################
	def test_repeat_04(self):
		"""Test repeat in array code  q - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_05(self):
		"""Test repeat in array code  q - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_06(self):
		"""Test repeat in array code  q - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_07(self):
		"""Test repeat in array code  q - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_08(self):
		"""Test repeat in array code  q - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_09(self):
		"""Test repeat in array code  q - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)


	########################################################
	def test_repeat_10(self):
		"""Test repeat in array code  q - Test for parameter overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MaxVal + 1)


	########################################################
	def test_repeat_11(self):
		"""Test repeat in array code  q - Test for parameter underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MinVal - 1)


##############################################################################



##############################################################################
class repeat_Q(unittest.TestCase):
	"""Test for basic repeat function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'Q'

		self.data = array.array(self.TypeCode, itertools.repeat(5, 512))

		self.MaxVal = arrayfunc.arraylimits.Q_max
		self.MinVal = arrayfunc.arraylimits.Q_min


	########################################################
	def test_repeat_01(self):
		"""Test repeat in array code  Q - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)
		self.assertEqual(list(self.data), [0]*len(self.data))


	########################################################
	def test_repeat_02(self):
		"""Test repeat in array code  Q - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)
		self.assertEqual(list(self.data), [self.MaxVal]*len(self.data))


	########################################################
	def test_repeat_03(self):
		"""Test repeat in array code  Q - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)
		self.assertEqual(list(self.data), [self.MinVal]*len(self.data))


	########################################################
	def test_repeat_04(self):
		"""Test repeat in array code  Q - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_05(self):
		"""Test repeat in array code  Q - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_06(self):
		"""Test repeat in array code  Q - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_07(self):
		"""Test repeat in array code  Q - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_08(self):
		"""Test repeat in array code  Q - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_09(self):
		"""Test repeat in array code  Q - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)


##############################################################################



##############################################################################
class repeat_f(unittest.TestCase):
	"""Test for basic repeat function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'f'

		self.data = array.array(self.TypeCode, itertools.repeat(5.0, 512))

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min


	########################################################
	def test_repeat_01(self):
		"""Test repeat in array code  f - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0.0)
		self.assertEqual(list(self.data), [0.0]*len(self.data))


	########################################################
	def test_repeat_02(self):
		"""Test repeat in array code  f - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)
		self.assertEqual(list(self.data), [self.MaxVal]*len(self.data))


	########################################################
	def test_repeat_03(self):
		"""Test repeat in array code  f - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)
		self.assertEqual(list(self.data), [self.MinVal]*len(self.data))


	########################################################
	def test_repeat_04(self):
		"""Test repeat in array code  f - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_05(self):
		"""Test repeat in array code  f - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10)


	########################################################
	def test_repeat_06(self):
		"""Test repeat in array code  f - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0.0)


	########################################################
	def test_repeat_07(self):
		"""Test repeat in array code  f - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_08(self):
		"""Test repeat in array code  f - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_09(self):
		"""Test repeat in array code  f - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0.0, 0.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)


	########################################################
	def test_repeat_10(self):
		"""Test repeat in array code  f - Test for parameter overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MaxVal * 1.1)


	########################################################
	def test_repeat_11(self):
		"""Test repeat in array code  f - Test for parameter underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MinVal * 1.1)


	########################################################
	# Floating point only.
	def test_repeat_12(self):
		"""Test repeat in array code  f - Invalid param nan for value.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, float('nan'))


	########################################################
	# Floating point only.
	def test_repeat_13(self):
		"""Test repeat in array code  f - Invalid param inf for value.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, float('inf'))


	########################################################
	# Floating point only.
	def test_repeat_14(self):
		"""Test repeat in array code  f - Invalid param -inf for value.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, float('-inf'))



##############################################################################



##############################################################################
class repeat_d(unittest.TestCase):
	"""Test for basic repeat function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'd'

		self.data = array.array(self.TypeCode, itertools.repeat(5.0, 512))

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min


	########################################################
	def test_repeat_01(self):
		"""Test repeat in array code  d - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0.0)
		self.assertEqual(list(self.data), [0.0]*len(self.data))


	########################################################
	def test_repeat_02(self):
		"""Test repeat in array code  d - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)
		self.assertEqual(list(self.data), [self.MaxVal]*len(self.data))


	########################################################
	def test_repeat_03(self):
		"""Test repeat in array code  d - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)
		self.assertEqual(list(self.data), [self.MinVal]*len(self.data))


	########################################################
	def test_repeat_04(self):
		"""Test repeat in array code  d - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_05(self):
		"""Test repeat in array code  d - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10)


	########################################################
	def test_repeat_06(self):
		"""Test repeat in array code  d - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0.0)


	########################################################
	def test_repeat_07(self):
		"""Test repeat in array code  d - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_08(self):
		"""Test repeat in array code  d - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_09(self):
		"""Test repeat in array code  d - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0.0, 0.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)


	########################################################
	def test_repeat_10(self):
		"""Test repeat in array code  d - Test for parameter overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MaxVal * 1.1)


	########################################################
	def test_repeat_11(self):
		"""Test repeat in array code  d - Test for parameter underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.MinVal * 1.1)


	########################################################
	# Floating point only.
	def test_repeat_12(self):
		"""Test repeat in array code  d - Invalid param nan for value.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, float('nan'))


	########################################################
	# Floating point only.
	def test_repeat_13(self):
		"""Test repeat in array code  d - Invalid param inf for value.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, float('inf'))


	########################################################
	# Floating point only.
	def test_repeat_14(self):
		"""Test repeat in array code  d - Invalid param -inf for value.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, float('-inf'))



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
			f.write('repeat\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
