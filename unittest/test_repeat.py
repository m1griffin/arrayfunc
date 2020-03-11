#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_repeat.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     11-Jun-2014.
# Ver:      06-Mar-2020.
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
class repeat_params_b(unittest.TestCase):
	"""Test for repeat parameter function.
	repeat_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('b', [0] * self.ArrayLength)
		self.emptydata = array.array('b', [])



	########################################################
	def test_repeat_param_01(self):
		"""Test repeat in array code  b - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_repeat_param_02(self):
		"""Test repeat in array code  b - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_param_03(self):
		"""Test repeat in array code  b - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_param_04(self):
		"""Test repeat in array code  b - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_param_05(self):
		"""Test repeat in array code  b - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_06(self):
		"""Test repeat in array code  b - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_07(self):
		"""Test repeat in array code  b - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)



##############################################################################


##############################################################################
class repeat_params_B(unittest.TestCase):
	"""Test for repeat parameter function.
	repeat_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('B', [0] * self.ArrayLength)
		self.emptydata = array.array('B', [])



	########################################################
	def test_repeat_param_01(self):
		"""Test repeat in array code  B - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_repeat_param_02(self):
		"""Test repeat in array code  B - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_param_03(self):
		"""Test repeat in array code  B - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_param_04(self):
		"""Test repeat in array code  B - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_param_05(self):
		"""Test repeat in array code  B - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_06(self):
		"""Test repeat in array code  B - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_07(self):
		"""Test repeat in array code  B - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)



##############################################################################


##############################################################################
class repeat_params_h(unittest.TestCase):
	"""Test for repeat parameter function.
	repeat_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('h', [0] * self.ArrayLength)
		self.emptydata = array.array('h', [])



	########################################################
	def test_repeat_param_01(self):
		"""Test repeat in array code  h - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_repeat_param_02(self):
		"""Test repeat in array code  h - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_param_03(self):
		"""Test repeat in array code  h - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_param_04(self):
		"""Test repeat in array code  h - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_param_05(self):
		"""Test repeat in array code  h - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_06(self):
		"""Test repeat in array code  h - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_07(self):
		"""Test repeat in array code  h - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)



##############################################################################


##############################################################################
class repeat_params_H(unittest.TestCase):
	"""Test for repeat parameter function.
	repeat_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('H', [0] * self.ArrayLength)
		self.emptydata = array.array('H', [])



	########################################################
	def test_repeat_param_01(self):
		"""Test repeat in array code  H - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_repeat_param_02(self):
		"""Test repeat in array code  H - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_param_03(self):
		"""Test repeat in array code  H - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_param_04(self):
		"""Test repeat in array code  H - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_param_05(self):
		"""Test repeat in array code  H - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_06(self):
		"""Test repeat in array code  H - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_07(self):
		"""Test repeat in array code  H - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)



##############################################################################


##############################################################################
class repeat_params_i(unittest.TestCase):
	"""Test for repeat parameter function.
	repeat_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('i', [0] * self.ArrayLength)
		self.emptydata = array.array('i', [])



	########################################################
	def test_repeat_param_01(self):
		"""Test repeat in array code  i - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_repeat_param_02(self):
		"""Test repeat in array code  i - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_param_03(self):
		"""Test repeat in array code  i - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_param_04(self):
		"""Test repeat in array code  i - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_param_05(self):
		"""Test repeat in array code  i - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_06(self):
		"""Test repeat in array code  i - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_07(self):
		"""Test repeat in array code  i - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)



##############################################################################


##############################################################################
class repeat_params_I(unittest.TestCase):
	"""Test for repeat parameter function.
	repeat_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('I', [0] * self.ArrayLength)
		self.emptydata = array.array('I', [])



	########################################################
	def test_repeat_param_01(self):
		"""Test repeat in array code  I - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_repeat_param_02(self):
		"""Test repeat in array code  I - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_param_03(self):
		"""Test repeat in array code  I - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_param_04(self):
		"""Test repeat in array code  I - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_param_05(self):
		"""Test repeat in array code  I - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_06(self):
		"""Test repeat in array code  I - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_07(self):
		"""Test repeat in array code  I - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)



##############################################################################


##############################################################################
class repeat_params_l(unittest.TestCase):
	"""Test for repeat parameter function.
	repeat_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('l', [0] * self.ArrayLength)
		self.emptydata = array.array('l', [])



	########################################################
	def test_repeat_param_01(self):
		"""Test repeat in array code  l - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_repeat_param_02(self):
		"""Test repeat in array code  l - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_param_03(self):
		"""Test repeat in array code  l - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_param_04(self):
		"""Test repeat in array code  l - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_param_05(self):
		"""Test repeat in array code  l - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_06(self):
		"""Test repeat in array code  l - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_07(self):
		"""Test repeat in array code  l - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)



##############################################################################


##############################################################################
class repeat_params_L(unittest.TestCase):
	"""Test for repeat parameter function.
	repeat_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('L', [0] * self.ArrayLength)
		self.emptydata = array.array('L', [])



	########################################################
	def test_repeat_param_01(self):
		"""Test repeat in array code  L - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_repeat_param_02(self):
		"""Test repeat in array code  L - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_param_03(self):
		"""Test repeat in array code  L - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_param_04(self):
		"""Test repeat in array code  L - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_param_05(self):
		"""Test repeat in array code  L - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_06(self):
		"""Test repeat in array code  L - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_07(self):
		"""Test repeat in array code  L - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)



##############################################################################


##############################################################################
class repeat_params_q(unittest.TestCase):
	"""Test for repeat parameter function.
	repeat_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('q', [0] * self.ArrayLength)
		self.emptydata = array.array('q', [])



	########################################################
	def test_repeat_param_01(self):
		"""Test repeat in array code  q - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_repeat_param_02(self):
		"""Test repeat in array code  q - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_param_03(self):
		"""Test repeat in array code  q - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_param_04(self):
		"""Test repeat in array code  q - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_param_05(self):
		"""Test repeat in array code  q - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_06(self):
		"""Test repeat in array code  q - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_07(self):
		"""Test repeat in array code  q - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)



##############################################################################


##############################################################################
class repeat_params_Q(unittest.TestCase):
	"""Test for repeat parameter function.
	repeat_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('Q', [0] * self.ArrayLength)
		self.emptydata = array.array('Q', [])



	########################################################
	def test_repeat_param_01(self):
		"""Test repeat in array code  Q - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_repeat_param_02(self):
		"""Test repeat in array code  Q - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_param_03(self):
		"""Test repeat in array code  Q - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10.0)


	########################################################
	def test_repeat_param_04(self):
		"""Test repeat in array code  Q - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0)


	########################################################
	def test_repeat_param_05(self):
		"""Test repeat in array code  Q - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_06(self):
		"""Test repeat in array code  Q - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_07(self):
		"""Test repeat in array code  Q - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0, 0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)



##############################################################################


##############################################################################
class repeat_params_f(unittest.TestCase):
	"""Test for repeat parameter function.
	repeat_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('f', [0] * self.ArrayLength)
		self.emptydata = array.array('f', [])



	########################################################
	def test_repeat_param_01(self):
		"""Test repeat in array code  f - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0.0)


	########################################################
	def test_repeat_param_02(self):
		"""Test repeat in array code  f - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_param_03(self):
		"""Test repeat in array code  f - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10)


	########################################################
	def test_repeat_param_04(self):
		"""Test repeat in array code  f - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0.0)


	########################################################
	def test_repeat_param_05(self):
		"""Test repeat in array code  f - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_06(self):
		"""Test repeat in array code  f - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_07(self):
		"""Test repeat in array code  f - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0.0, 0.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)



##############################################################################


##############################################################################
class repeat_params_d(unittest.TestCase):
	"""Test for repeat parameter function.
	repeat_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('d', [0] * self.ArrayLength)
		self.emptydata = array.array('d', [])



	########################################################
	def test_repeat_param_01(self):
		"""Test repeat in array code  d - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0.0)


	########################################################
	def test_repeat_param_02(self):
		"""Test repeat in array code  d - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_param_03(self):
		"""Test repeat in array code  d - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10)


	########################################################
	def test_repeat_param_04(self):
		"""Test repeat in array code  d - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0.0)


	########################################################
	def test_repeat_param_05(self):
		"""Test repeat in array code  d - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_06(self):
		"""Test repeat in array code  d - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_07(self):
		"""Test repeat in array code  d - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0.0, 0.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)



##############################################################################


##############################################################################
class repeat_op_b(unittest.TestCase):
	"""Test for basic repeat function.
	repeat_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('b', [10] * self.ArrayLength)

		self.MaxVal = arrayfunc.arraylimits.b_max
		self.MinVal = arrayfunc.arraylimits.b_min


	########################################################
	def test_repeat_op_01(self):
		"""Test repeat operation in array code  b - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)

		expected = [0] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_02(self):
		"""Test repeat operation in array code  b - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)

		expected = [self.MaxVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_03(self):
		"""Test repeat operation in array code  b - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)

		expected = [self.MinVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class repeat_op_B(unittest.TestCase):
	"""Test for basic repeat function.
	repeat_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('B', [10] * self.ArrayLength)

		self.MaxVal = arrayfunc.arraylimits.B_max
		self.MinVal = arrayfunc.arraylimits.B_min


	########################################################
	def test_repeat_op_01(self):
		"""Test repeat operation in array code  B - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)

		expected = [0] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_02(self):
		"""Test repeat operation in array code  B - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)

		expected = [self.MaxVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_03(self):
		"""Test repeat operation in array code  B - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)

		expected = [self.MinVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class repeat_op_h(unittest.TestCase):
	"""Test for basic repeat function.
	repeat_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('h', [10] * self.ArrayLength)

		self.MaxVal = arrayfunc.arraylimits.h_max
		self.MinVal = arrayfunc.arraylimits.h_min


	########################################################
	def test_repeat_op_01(self):
		"""Test repeat operation in array code  h - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)

		expected = [0] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_02(self):
		"""Test repeat operation in array code  h - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)

		expected = [self.MaxVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_03(self):
		"""Test repeat operation in array code  h - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)

		expected = [self.MinVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class repeat_op_H(unittest.TestCase):
	"""Test for basic repeat function.
	repeat_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('H', [10] * self.ArrayLength)

		self.MaxVal = arrayfunc.arraylimits.H_max
		self.MinVal = arrayfunc.arraylimits.H_min


	########################################################
	def test_repeat_op_01(self):
		"""Test repeat operation in array code  H - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)

		expected = [0] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_02(self):
		"""Test repeat operation in array code  H - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)

		expected = [self.MaxVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_03(self):
		"""Test repeat operation in array code  H - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)

		expected = [self.MinVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class repeat_op_i(unittest.TestCase):
	"""Test for basic repeat function.
	repeat_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('i', [10] * self.ArrayLength)

		self.MaxVal = arrayfunc.arraylimits.i_max
		self.MinVal = arrayfunc.arraylimits.i_min


	########################################################
	def test_repeat_op_01(self):
		"""Test repeat operation in array code  i - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)

		expected = [0] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_02(self):
		"""Test repeat operation in array code  i - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)

		expected = [self.MaxVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_03(self):
		"""Test repeat operation in array code  i - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)

		expected = [self.MinVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class repeat_op_I(unittest.TestCase):
	"""Test for basic repeat function.
	repeat_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('I', [10] * self.ArrayLength)

		self.MaxVal = arrayfunc.arraylimits.I_max
		self.MinVal = arrayfunc.arraylimits.I_min


	########################################################
	def test_repeat_op_01(self):
		"""Test repeat operation in array code  I - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)

		expected = [0] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_02(self):
		"""Test repeat operation in array code  I - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)

		expected = [self.MaxVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_03(self):
		"""Test repeat operation in array code  I - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)

		expected = [self.MinVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class repeat_op_l(unittest.TestCase):
	"""Test for basic repeat function.
	repeat_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('l', [10] * self.ArrayLength)

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min


	########################################################
	def test_repeat_op_01(self):
		"""Test repeat operation in array code  l - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)

		expected = [0] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_02(self):
		"""Test repeat operation in array code  l - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)

		expected = [self.MaxVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_03(self):
		"""Test repeat operation in array code  l - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)

		expected = [self.MinVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class repeat_op_L(unittest.TestCase):
	"""Test for basic repeat function.
	repeat_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('L', [10] * self.ArrayLength)

		self.MaxVal = arrayfunc.arraylimits.L_max
		self.MinVal = arrayfunc.arraylimits.L_min


	########################################################
	def test_repeat_op_01(self):
		"""Test repeat operation in array code  L - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)

		expected = [0] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_02(self):
		"""Test repeat operation in array code  L - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)

		expected = [self.MaxVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_03(self):
		"""Test repeat operation in array code  L - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)

		expected = [self.MinVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class repeat_op_q(unittest.TestCase):
	"""Test for basic repeat function.
	repeat_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('q', [10] * self.ArrayLength)

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min


	########################################################
	def test_repeat_op_01(self):
		"""Test repeat operation in array code  q - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)

		expected = [0] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_02(self):
		"""Test repeat operation in array code  q - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)

		expected = [self.MaxVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_03(self):
		"""Test repeat operation in array code  q - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)

		expected = [self.MinVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class repeat_op_Q(unittest.TestCase):
	"""Test for basic repeat function.
	repeat_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('Q', [10] * self.ArrayLength)

		self.MaxVal = arrayfunc.arraylimits.Q_max
		self.MinVal = arrayfunc.arraylimits.Q_min


	########################################################
	def test_repeat_op_01(self):
		"""Test repeat operation in array code  Q - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0)

		expected = [0] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_02(self):
		"""Test repeat operation in array code  Q - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)

		expected = [self.MaxVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_03(self):
		"""Test repeat operation in array code  Q - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)

		expected = [self.MinVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class repeat_op_f(unittest.TestCase):
	"""Test for basic repeat function.
	repeat_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('f', [10] * self.ArrayLength)

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min


	########################################################
	def test_repeat_op_01(self):
		"""Test repeat operation in array code  f - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0.0)

		expected = [0.0] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_02(self):
		"""Test repeat operation in array code  f - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)

		expected = [self.MaxVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_03(self):
		"""Test repeat operation in array code  f - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)

		expected = [self.MinVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class repeat_op_d(unittest.TestCase):
	"""Test for basic repeat function.
	repeat_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('d', [10] * self.ArrayLength)

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min


	########################################################
	def test_repeat_op_01(self):
		"""Test repeat operation in array code  d - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0.0)

		expected = [0.0] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_02(self):
		"""Test repeat operation in array code  d - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)

		expected = [self.MaxVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_03(self):
		"""Test repeat operation in array code  d - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)

		expected = [self.MinVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class repeat_nonfinite_f(unittest.TestCase):
	"""Test for nonfinite repeat function.
	repeat_nonfinite_template
	"""

	##############################################################################
	def FloatassertEqual(self, dataoutitem, expecteditem, msg=None):
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
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.ArrayLength = 512

		self.data = array.array('f', [10] * self.ArrayLength)


	########################################################
	def test_repeat_nan_01(self):
		"""Test repeat non-finite operation in array code  f - Test for NaN.
		"""
		arrayfunc.repeat(self.data, math.nan)

		expected = [math.nan] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_inf_02(self):
		"""Test repeat non-finite operation in array code  f - Test for Inf value.
		"""
		arrayfunc.repeat(self.data, math.inf)

		expected = [math.inf] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_ninf_03(self):
		"""Test repeat non-finite operation in array code  f - Test for Neg Inf value.
		"""
		arrayfunc.repeat(self.data, -math.inf)

		expected = [-math.inf] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class repeat_nonfinite_d(unittest.TestCase):
	"""Test for nonfinite repeat function.
	repeat_nonfinite_template
	"""

	##############################################################################
	def FloatassertEqual(self, dataoutitem, expecteditem, msg=None):
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
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.ArrayLength = 512

		self.data = array.array('d', [10] * self.ArrayLength)


	########################################################
	def test_repeat_nan_01(self):
		"""Test repeat non-finite operation in array code  d - Test for NaN.
		"""
		arrayfunc.repeat(self.data, math.nan)

		expected = [math.nan] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_inf_02(self):
		"""Test repeat non-finite operation in array code  d - Test for Inf value.
		"""
		arrayfunc.repeat(self.data, math.inf)

		expected = [math.inf] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_ninf_03(self):
		"""Test repeat non-finite operation in array code  d - Test for Neg Inf value.
		"""
		arrayfunc.repeat(self.data, -math.inf)

		expected = [-math.inf] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class repeat_overflow_b(unittest.TestCase):
	"""Test for overflow repeat function.
	repeat_overflow_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.b_max
		self.MinVal = arrayfunc.arraylimits.b_min


		# Create the overflow value for this data type.
		if 'b' in ('f', 'd'):
			self.Overflow = self.MaxVal * 1.1
			self.Underflow = self.MinVal * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1

		self.data = array.array('b', [0] * self.ArrayLength)


	########################################################
	def test_repeat_ovfl_01(self):
		"""Test repeat overflow operation in array code  b - Test for overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Overflow)


	########################################################
	def test_repeat_ovfl_02(self):
		"""Test repeat overflow operation in array code  b - Test for underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Underflow)



##############################################################################


##############################################################################
class repeat_overflow_B(unittest.TestCase):
	"""Test for overflow repeat function.
	repeat_overflow_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.B_max
		self.MinVal = arrayfunc.arraylimits.B_min


		# Create the overflow value for this data type.
		if 'B' in ('f', 'd'):
			self.Overflow = self.MaxVal * 1.1
			self.Underflow = self.MinVal * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1

		self.data = array.array('B', [0] * self.ArrayLength)


	########################################################
	def test_repeat_ovfl_01(self):
		"""Test repeat overflow operation in array code  B - Test for overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Overflow)


	########################################################
	def test_repeat_ovfl_02(self):
		"""Test repeat overflow operation in array code  B - Test for underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Underflow)



##############################################################################


##############################################################################
class repeat_overflow_h(unittest.TestCase):
	"""Test for overflow repeat function.
	repeat_overflow_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.h_max
		self.MinVal = arrayfunc.arraylimits.h_min


		# Create the overflow value for this data type.
		if 'h' in ('f', 'd'):
			self.Overflow = self.MaxVal * 1.1
			self.Underflow = self.MinVal * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1

		self.data = array.array('h', [0] * self.ArrayLength)


	########################################################
	def test_repeat_ovfl_01(self):
		"""Test repeat overflow operation in array code  h - Test for overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Overflow)


	########################################################
	def test_repeat_ovfl_02(self):
		"""Test repeat overflow operation in array code  h - Test for underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Underflow)



##############################################################################


##############################################################################
class repeat_overflow_H(unittest.TestCase):
	"""Test for overflow repeat function.
	repeat_overflow_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.H_max
		self.MinVal = arrayfunc.arraylimits.H_min


		# Create the overflow value for this data type.
		if 'H' in ('f', 'd'):
			self.Overflow = self.MaxVal * 1.1
			self.Underflow = self.MinVal * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1

		self.data = array.array('H', [0] * self.ArrayLength)


	########################################################
	def test_repeat_ovfl_01(self):
		"""Test repeat overflow operation in array code  H - Test for overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Overflow)


	########################################################
	def test_repeat_ovfl_02(self):
		"""Test repeat overflow operation in array code  H - Test for underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Underflow)



##############################################################################


##############################################################################
class repeat_overflow_i(unittest.TestCase):
	"""Test for overflow repeat function.
	repeat_overflow_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.i_max
		self.MinVal = arrayfunc.arraylimits.i_min


		# Create the overflow value for this data type.
		if 'i' in ('f', 'd'):
			self.Overflow = self.MaxVal * 1.1
			self.Underflow = self.MinVal * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1

		self.data = array.array('i', [0] * self.ArrayLength)


	########################################################
	def test_repeat_ovfl_01(self):
		"""Test repeat overflow operation in array code  i - Test for overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Overflow)


	########################################################
	def test_repeat_ovfl_02(self):
		"""Test repeat overflow operation in array code  i - Test for underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Underflow)



##############################################################################


##############################################################################
class repeat_overflow_I(unittest.TestCase):
	"""Test for overflow repeat function.
	repeat_overflow_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.I_max
		self.MinVal = arrayfunc.arraylimits.I_min


		# Create the overflow value for this data type.
		if 'I' in ('f', 'd'):
			self.Overflow = self.MaxVal * 1.1
			self.Underflow = self.MinVal * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1

		self.data = array.array('I', [0] * self.ArrayLength)


	########################################################
	def test_repeat_ovfl_01(self):
		"""Test repeat overflow operation in array code  I - Test for overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Overflow)


	########################################################
	def test_repeat_ovfl_02(self):
		"""Test repeat overflow operation in array code  I - Test for underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Underflow)



##############################################################################


##############################################################################
class repeat_overflow_l(unittest.TestCase):
	"""Test for overflow repeat function.
	repeat_overflow_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min


		# Create the overflow value for this data type.
		if 'l' in ('f', 'd'):
			self.Overflow = self.MaxVal * 1.1
			self.Underflow = self.MinVal * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1

		self.data = array.array('l', [0] * self.ArrayLength)


	########################################################
	def test_repeat_ovfl_01(self):
		"""Test repeat overflow operation in array code  l - Test for overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Overflow)


	########################################################
	def test_repeat_ovfl_02(self):
		"""Test repeat overflow operation in array code  l - Test for underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Underflow)



##############################################################################


##############################################################################
class repeat_overflow_q(unittest.TestCase):
	"""Test for overflow repeat function.
	repeat_overflow_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min


		# Create the overflow value for this data type.
		if 'q' in ('f', 'd'):
			self.Overflow = self.MaxVal * 1.1
			self.Underflow = self.MinVal * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1

		self.data = array.array('q', [0] * self.ArrayLength)


	########################################################
	def test_repeat_ovfl_01(self):
		"""Test repeat overflow operation in array code  q - Test for overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Overflow)


	########################################################
	def test_repeat_ovfl_02(self):
		"""Test repeat overflow operation in array code  q - Test for underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Underflow)



##############################################################################


##############################################################################
class repeat_overflow_f(unittest.TestCase):
	"""Test for overflow repeat function.
	repeat_overflow_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min


		# Create the overflow value for this data type.
		if 'f' in ('f', 'd'):
			self.Overflow = self.MaxVal * 1.1
			self.Underflow = self.MinVal * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1

		self.data = array.array('f', [0] * self.ArrayLength)


	########################################################
	def test_repeat_ovfl_01(self):
		"""Test repeat overflow operation in array code  f - Test for overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Overflow)


	########################################################
	def test_repeat_ovfl_02(self):
		"""Test repeat overflow operation in array code  f - Test for underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Underflow)



##############################################################################


##############################################################################
if __name__ == '__main__':

	# Check to see if the log file option has been selected. This is an option
	# which we have added in order to decide where to output the results.
	if '-l' in sys.argv:
		# Remove the option from the argument list so that "unittest" does 
		# not complain about unknown options.
		sys.argv.remove('-l')

		with open('af_unittest.txt', 'a') as f:
			f.write('\n\n')
			f.write('repeat\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
