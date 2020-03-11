#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_count.py
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
"""This conducts unit tests for count.
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
class count_params_b(unittest.TestCase):
	"""Test for count parameter function.
	count_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('b', [0] * self.ArrayLength)
		self.emptydata = array.array('b', [])


	########################################################
	def test_count_param_01(self):
		"""Test count in array code  b - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_count_param_02(self):
		"""Test count in array code  b - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_param_03(self):
		"""Test count in array code  b - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_param_04(self):
		"""Test count in array code  b - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_param_05(self):
		"""Test count in array code  b - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_param_06(self):
		"""Test count in array code  b - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')



##############################################################################



##############################################################################
class count_params_B(unittest.TestCase):
	"""Test for count parameter function.
	count_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('B', [0] * self.ArrayLength)
		self.emptydata = array.array('B', [])


	########################################################
	def test_count_param_01(self):
		"""Test count in array code  B - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_count_param_02(self):
		"""Test count in array code  B - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_param_03(self):
		"""Test count in array code  B - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_param_04(self):
		"""Test count in array code  B - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_param_05(self):
		"""Test count in array code  B - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_param_06(self):
		"""Test count in array code  B - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')



##############################################################################



##############################################################################
class count_params_h(unittest.TestCase):
	"""Test for count parameter function.
	count_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('h', [0] * self.ArrayLength)
		self.emptydata = array.array('h', [])


	########################################################
	def test_count_param_01(self):
		"""Test count in array code  h - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_count_param_02(self):
		"""Test count in array code  h - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_param_03(self):
		"""Test count in array code  h - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_param_04(self):
		"""Test count in array code  h - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_param_05(self):
		"""Test count in array code  h - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_param_06(self):
		"""Test count in array code  h - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')



##############################################################################



##############################################################################
class count_params_H(unittest.TestCase):
	"""Test for count parameter function.
	count_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('H', [0] * self.ArrayLength)
		self.emptydata = array.array('H', [])


	########################################################
	def test_count_param_01(self):
		"""Test count in array code  H - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_count_param_02(self):
		"""Test count in array code  H - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_param_03(self):
		"""Test count in array code  H - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_param_04(self):
		"""Test count in array code  H - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_param_05(self):
		"""Test count in array code  H - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_param_06(self):
		"""Test count in array code  H - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')



##############################################################################



##############################################################################
class count_params_i(unittest.TestCase):
	"""Test for count parameter function.
	count_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('i', [0] * self.ArrayLength)
		self.emptydata = array.array('i', [])


	########################################################
	def test_count_param_01(self):
		"""Test count in array code  i - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_count_param_02(self):
		"""Test count in array code  i - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_param_03(self):
		"""Test count in array code  i - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_param_04(self):
		"""Test count in array code  i - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_param_05(self):
		"""Test count in array code  i - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_param_06(self):
		"""Test count in array code  i - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')



##############################################################################



##############################################################################
class count_params_I(unittest.TestCase):
	"""Test for count parameter function.
	count_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('I', [0] * self.ArrayLength)
		self.emptydata = array.array('I', [])


	########################################################
	def test_count_param_01(self):
		"""Test count in array code  I - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_count_param_02(self):
		"""Test count in array code  I - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_param_03(self):
		"""Test count in array code  I - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_param_04(self):
		"""Test count in array code  I - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_param_05(self):
		"""Test count in array code  I - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_param_06(self):
		"""Test count in array code  I - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')



##############################################################################



##############################################################################
class count_params_l(unittest.TestCase):
	"""Test for count parameter function.
	count_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('l', [0] * self.ArrayLength)
		self.emptydata = array.array('l', [])


	########################################################
	def test_count_param_01(self):
		"""Test count in array code  l - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_count_param_02(self):
		"""Test count in array code  l - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_param_03(self):
		"""Test count in array code  l - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_param_04(self):
		"""Test count in array code  l - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_param_05(self):
		"""Test count in array code  l - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_param_06(self):
		"""Test count in array code  l - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')



##############################################################################



##############################################################################
class count_params_L(unittest.TestCase):
	"""Test for count parameter function.
	count_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('L', [0] * self.ArrayLength)
		self.emptydata = array.array('L', [])


	########################################################
	def test_count_param_01(self):
		"""Test count in array code  L - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_count_param_02(self):
		"""Test count in array code  L - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_param_03(self):
		"""Test count in array code  L - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_param_04(self):
		"""Test count in array code  L - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_param_05(self):
		"""Test count in array code  L - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_param_06(self):
		"""Test count in array code  L - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')



##############################################################################



##############################################################################
class count_params_q(unittest.TestCase):
	"""Test for count parameter function.
	count_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('q', [0] * self.ArrayLength)
		self.emptydata = array.array('q', [])


	########################################################
	def test_count_param_01(self):
		"""Test count in array code  q - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_count_param_02(self):
		"""Test count in array code  q - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_param_03(self):
		"""Test count in array code  q - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_param_04(self):
		"""Test count in array code  q - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_param_05(self):
		"""Test count in array code  q - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_param_06(self):
		"""Test count in array code  q - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')



##############################################################################



##############################################################################
class count_params_Q(unittest.TestCase):
	"""Test for count parameter function.
	count_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('Q', [0] * self.ArrayLength)
		self.emptydata = array.array('Q', [])


	########################################################
	def test_count_param_01(self):
		"""Test count in array code  Q - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0)


	########################################################
	def test_count_param_02(self):
		"""Test count in array code  Q - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_param_03(self):
		"""Test count in array code  Q - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_param_04(self):
		"""Test count in array code  Q - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_param_05(self):
		"""Test count in array code  Q - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_param_06(self):
		"""Test count in array code  Q - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0, 'a')



##############################################################################



##############################################################################
class count_params_f(unittest.TestCase):
	"""Test for count parameter function.
	count_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('f', [0] * self.ArrayLength)
		self.emptydata = array.array('f', [])


	########################################################
	def test_count_param_01(self):
		"""Test count in array code  f - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0.0)


	########################################################
	def test_count_param_02(self):
		"""Test count in array code  f - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_param_03(self):
		"""Test count in array code  f - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0.0, 1.0, 1.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_param_04(self):
		"""Test count in array code  f - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0.0, 1.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_param_05(self):
		"""Test count in array code  f - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_param_06(self):
		"""Test count in array code  f - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0.0, 'a')



##############################################################################



##############################################################################
class count_params_d(unittest.TestCase):
	"""Test for count parameter function.
	count_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('d', [0] * self.ArrayLength)
		self.emptydata = array.array('d', [])


	########################################################
	def test_count_param_01(self):
		"""Test count in array code  d - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0.0)


	########################################################
	def test_count_param_02(self):
		"""Test count in array code  d - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_param_03(self):
		"""Test count in array code  d - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0.0, 1.0, 1.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_param_04(self):
		"""Test count in array code  d - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0.0, 1.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_param_05(self):
		"""Test count in array code  d - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_param_06(self):
		"""Test count in array code  d - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0.0, 'a')



##############################################################################



##############################################################################
class count_op_b(unittest.TestCase):
	"""Test for basic count function.
	count_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'b'

		self.ArrayLength = 512

		self.data = array.array('b', itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.b_max
		self.MinVal = arrayfunc.arraylimits.b_min

		self.zerodata = array.array('b', [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.b_max
		self.MaxStepData = array.array('b', itertools.repeat(0, 6))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	def test_count_op_01(self):
		"""Test count in array code  b - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 1)

		arrayfunc.count(self.data, 0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_02(self):
		"""Test count in array code  b - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 1)

		arrayfunc.count(self.data, 10)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_03(self):
		"""Test count in array code  b - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 7)

		arrayfunc.count(self.data, 0, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_04(self):
		"""Test count in array code  b - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 7)

		arrayfunc.count(self.data, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_count_op_05(self):
		"""Test count in array code  b - Step is maximum size.
		"""
		expected = self.PyCount(self.MaxStepData, 0, self.MaxStep)

		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)


		for dataoutitem, expecteditem in zip(list(self.MaxStepData), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_06(self):
		"""Test count in array code  b - start from 10, down by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, -1)

		arrayfunc.count(self.data, 10, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class count_op_B(unittest.TestCase):
	"""Test for basic count function.
	count_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'B'

		self.ArrayLength = 512

		self.data = array.array('B', itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.B_max
		self.MinVal = arrayfunc.arraylimits.B_min

		self.zerodata = array.array('B', [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.b_max
		self.MaxStepData = array.array('B', itertools.repeat(0, 6))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	def test_count_op_01(self):
		"""Test count in array code  B - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 1)

		arrayfunc.count(self.data, 0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_02(self):
		"""Test count in array code  B - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 1)

		arrayfunc.count(self.data, 10)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_03(self):
		"""Test count in array code  B - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 7)

		arrayfunc.count(self.data, 0, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_04(self):
		"""Test count in array code  B - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 7)

		arrayfunc.count(self.data, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_count_op_05(self):
		"""Test count in array code  B - Step is maximum size.
		"""
		expected = self.PyCount(self.MaxStepData, 0, self.MaxStep)

		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)


		for dataoutitem, expecteditem in zip(list(self.MaxStepData), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_06(self):
		"""Test count in array code  B - start from 10, down by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, -1)

		arrayfunc.count(self.data, 10, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class count_op_h(unittest.TestCase):
	"""Test for basic count function.
	count_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'h'

		self.ArrayLength = 512

		self.data = array.array('h', itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.h_max
		self.MinVal = arrayfunc.arraylimits.h_min

		self.zerodata = array.array('h', [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.h_max
		self.MaxStepData = array.array('h', itertools.repeat(0, 6))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	def test_count_op_01(self):
		"""Test count in array code  h - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 1)

		arrayfunc.count(self.data, 0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_02(self):
		"""Test count in array code  h - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 1)

		arrayfunc.count(self.data, 10)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_03(self):
		"""Test count in array code  h - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 7)

		arrayfunc.count(self.data, 0, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_04(self):
		"""Test count in array code  h - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 7)

		arrayfunc.count(self.data, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_count_op_05(self):
		"""Test count in array code  h - Step is maximum size.
		"""
		expected = self.PyCount(self.MaxStepData, 0, self.MaxStep)

		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)


		for dataoutitem, expecteditem in zip(list(self.MaxStepData), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_06(self):
		"""Test count in array code  h - start from 10, down by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, -1)

		arrayfunc.count(self.data, 10, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class count_op_H(unittest.TestCase):
	"""Test for basic count function.
	count_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'H'

		self.ArrayLength = 512

		self.data = array.array('H', itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.H_max
		self.MinVal = arrayfunc.arraylimits.H_min

		self.zerodata = array.array('H', [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.h_max
		self.MaxStepData = array.array('H', itertools.repeat(0, 6))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	def test_count_op_01(self):
		"""Test count in array code  H - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 1)

		arrayfunc.count(self.data, 0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_02(self):
		"""Test count in array code  H - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 1)

		arrayfunc.count(self.data, 10)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_03(self):
		"""Test count in array code  H - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 7)

		arrayfunc.count(self.data, 0, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_04(self):
		"""Test count in array code  H - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 7)

		arrayfunc.count(self.data, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_count_op_05(self):
		"""Test count in array code  H - Step is maximum size.
		"""
		expected = self.PyCount(self.MaxStepData, 0, self.MaxStep)

		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)


		for dataoutitem, expecteditem in zip(list(self.MaxStepData), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_06(self):
		"""Test count in array code  H - start from 10, down by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, -1)

		arrayfunc.count(self.data, 10, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class count_op_i(unittest.TestCase):
	"""Test for basic count function.
	count_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'i'

		self.ArrayLength = 512

		self.data = array.array('i', itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.i_max
		self.MinVal = arrayfunc.arraylimits.i_min

		self.zerodata = array.array('i', [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.i_max
		self.MaxStepData = array.array('i', itertools.repeat(0, 6))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	def test_count_op_01(self):
		"""Test count in array code  i - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 1)

		arrayfunc.count(self.data, 0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_02(self):
		"""Test count in array code  i - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 1)

		arrayfunc.count(self.data, 10)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_03(self):
		"""Test count in array code  i - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 7)

		arrayfunc.count(self.data, 0, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_04(self):
		"""Test count in array code  i - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 7)

		arrayfunc.count(self.data, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_count_op_05(self):
		"""Test count in array code  i - Step is maximum size.
		"""
		expected = self.PyCount(self.MaxStepData, 0, self.MaxStep)

		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)


		for dataoutitem, expecteditem in zip(list(self.MaxStepData), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_06(self):
		"""Test count in array code  i - start from 10, down by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, -1)

		arrayfunc.count(self.data, 10, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class count_op_I(unittest.TestCase):
	"""Test for basic count function.
	count_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'I'

		self.ArrayLength = 512

		self.data = array.array('I', itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.I_max
		self.MinVal = arrayfunc.arraylimits.I_min

		self.zerodata = array.array('I', [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.i_max
		self.MaxStepData = array.array('I', itertools.repeat(0, 6))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	def test_count_op_01(self):
		"""Test count in array code  I - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 1)

		arrayfunc.count(self.data, 0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_02(self):
		"""Test count in array code  I - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 1)

		arrayfunc.count(self.data, 10)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_03(self):
		"""Test count in array code  I - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 7)

		arrayfunc.count(self.data, 0, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_04(self):
		"""Test count in array code  I - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 7)

		arrayfunc.count(self.data, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_count_op_05(self):
		"""Test count in array code  I - Step is maximum size.
		"""
		expected = self.PyCount(self.MaxStepData, 0, self.MaxStep)

		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)


		for dataoutitem, expecteditem in zip(list(self.MaxStepData), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_06(self):
		"""Test count in array code  I - start from 10, down by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, -1)

		arrayfunc.count(self.data, 10, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class count_op_l(unittest.TestCase):
	"""Test for basic count function.
	count_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'l'

		self.ArrayLength = 512

		self.data = array.array('l', itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min

		self.zerodata = array.array('l', [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.l_max
		self.MaxStepData = array.array('l', itertools.repeat(0, 6))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	def test_count_op_01(self):
		"""Test count in array code  l - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 1)

		arrayfunc.count(self.data, 0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_02(self):
		"""Test count in array code  l - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 1)

		arrayfunc.count(self.data, 10)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_03(self):
		"""Test count in array code  l - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 7)

		arrayfunc.count(self.data, 0, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_04(self):
		"""Test count in array code  l - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 7)

		arrayfunc.count(self.data, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_count_op_05(self):
		"""Test count in array code  l - Step is maximum size.
		"""
		expected = self.PyCount(self.MaxStepData, 0, self.MaxStep)

		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)


		for dataoutitem, expecteditem in zip(list(self.MaxStepData), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_06(self):
		"""Test count in array code  l - start from 10, down by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, -1)

		arrayfunc.count(self.data, 10, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class count_op_L(unittest.TestCase):
	"""Test for basic count function.
	count_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'L'

		self.ArrayLength = 512

		self.data = array.array('L', itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.L_max
		self.MinVal = arrayfunc.arraylimits.L_min

		self.zerodata = array.array('L', [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.l_max
		self.MaxStepData = array.array('L', itertools.repeat(0, 6))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	def test_count_op_01(self):
		"""Test count in array code  L - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 1)

		arrayfunc.count(self.data, 0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_02(self):
		"""Test count in array code  L - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 1)

		arrayfunc.count(self.data, 10)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_03(self):
		"""Test count in array code  L - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 7)

		arrayfunc.count(self.data, 0, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_04(self):
		"""Test count in array code  L - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 7)

		arrayfunc.count(self.data, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_count_op_05(self):
		"""Test count in array code  L - Step is maximum size.
		"""
		expected = self.PyCount(self.MaxStepData, 0, self.MaxStep)

		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)


		for dataoutitem, expecteditem in zip(list(self.MaxStepData), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_06(self):
		"""Test count in array code  L - start from 10, down by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, -1)

		arrayfunc.count(self.data, 10, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class count_op_q(unittest.TestCase):
	"""Test for basic count function.
	count_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'q'

		self.ArrayLength = 512

		self.data = array.array('q', itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min

		self.zerodata = array.array('q', [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.q_max
		self.MaxStepData = array.array('q', itertools.repeat(0, 6))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	def test_count_op_01(self):
		"""Test count in array code  q - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 1)

		arrayfunc.count(self.data, 0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_02(self):
		"""Test count in array code  q - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 1)

		arrayfunc.count(self.data, 10)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_03(self):
		"""Test count in array code  q - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 7)

		arrayfunc.count(self.data, 0, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_04(self):
		"""Test count in array code  q - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 7)

		arrayfunc.count(self.data, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_count_op_05(self):
		"""Test count in array code  q - Step is maximum size.
		"""
		expected = self.PyCount(self.MaxStepData, 0, self.MaxStep)

		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)


		for dataoutitem, expecteditem in zip(list(self.MaxStepData), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_06(self):
		"""Test count in array code  q - start from 10, down by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, -1)

		arrayfunc.count(self.data, 10, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class count_op_Q(unittest.TestCase):
	"""Test for basic count function.
	count_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'Q'

		self.ArrayLength = 512

		self.data = array.array('Q', itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.Q_max
		self.MinVal = arrayfunc.arraylimits.Q_min

		self.zerodata = array.array('Q', [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.q_max
		self.MaxStepData = array.array('Q', itertools.repeat(0, 6))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	def test_count_op_01(self):
		"""Test count in array code  Q - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 1)

		arrayfunc.count(self.data, 0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_02(self):
		"""Test count in array code  Q - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 1)

		arrayfunc.count(self.data, 10)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_03(self):
		"""Test count in array code  Q - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0, 7)

		arrayfunc.count(self.data, 0, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_04(self):
		"""Test count in array code  Q - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, 7)

		arrayfunc.count(self.data, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_count_op_05(self):
		"""Test count in array code  Q - Step is maximum size.
		"""
		expected = self.PyCount(self.MaxStepData, 0, self.MaxStep)

		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0, self.MaxStep)


		for dataoutitem, expecteditem in zip(list(self.MaxStepData), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_06(self):
		"""Test count in array code  Q - start from 10, down by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10, -1)

		arrayfunc.count(self.data, 10, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class count_op_f(unittest.TestCase):
	"""Test for basic count function.
	count_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'f'

		self.ArrayLength = 512

		self.data = array.array('f', itertools.repeat(0.0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min

		self.zerodata = array.array('f', [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.f_max
		self.MaxStepData = array.array('f', itertools.repeat(0.0, 6))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	def test_count_op_01(self):
		"""Test count in array code  f - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0.0, 1.0)

		arrayfunc.count(self.data, 0.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_02(self):
		"""Test count in array code  f - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10.0, 1.0)

		arrayfunc.count(self.data, 10.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_03(self):
		"""Test count in array code  f - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0.0, 7.0)

		arrayfunc.count(self.data, 0.0, 7.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_04(self):
		"""Test count in array code  f - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10.0, 7.0)

		arrayfunc.count(self.data, 10.0, 7.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_count_op_05(self):
		"""Test count in array code  f - Step is maximum size.
		"""
		expected = self.PyCount(self.MaxStepData, 0.0, self.MaxStep)

		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0.0, self.MaxStep)


		for dataoutitem, expecteditem in zip(list(self.MaxStepData), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_06(self):
		"""Test count in array code  f - start from 10, down by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10.0, -1.0)

		arrayfunc.count(self.data, 10.0, -1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class count_op_d(unittest.TestCase):
	"""Test for basic count function.
	count_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'd'

		self.ArrayLength = 512

		self.data = array.array('d', itertools.repeat(0.0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min

		self.zerodata = array.array('d', [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.d_max
		self.MaxStepData = array.array('d', itertools.repeat(0.0, 6))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	def test_count_op_01(self):
		"""Test count in array code  d - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0.0, 1.0)

		arrayfunc.count(self.data, 0.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_02(self):
		"""Test count in array code  d - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10.0, 1.0)

		arrayfunc.count(self.data, 10.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_03(self):
		"""Test count in array code  d - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0.0, 7.0)

		arrayfunc.count(self.data, 0.0, 7.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_04(self):
		"""Test count in array code  d - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10.0, 7.0)

		arrayfunc.count(self.data, 10.0, 7.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_count_op_05(self):
		"""Test count in array code  d - Step is maximum size.
		"""
		expected = self.PyCount(self.MaxStepData, 0.0, self.MaxStep)

		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0.0, self.MaxStep)


		for dataoutitem, expecteditem in zip(list(self.MaxStepData), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_06(self):
		"""Test count in array code  d - start from 10, down by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10.0, -1.0)

		arrayfunc.count(self.data, 10.0, -1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class count_op_signed_b(unittest.TestCase):
	"""Test for basic count function for signed data.
	count_op_signed_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'b'

		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.b_max
		self.MinVal = arrayfunc.arraylimits.b_min

		self.data = array.array('b', itertools.repeat(0, self.ArrayLength))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	# Signed and float only.
	def test_count_op_signed_01(self):
		"""Test count in array code  b - start from -10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, -10, 1)

		arrayfunc.count(self.data, -10)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class count_op_signed_h(unittest.TestCase):
	"""Test for basic count function for signed data.
	count_op_signed_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'h'

		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.h_max
		self.MinVal = arrayfunc.arraylimits.h_min

		self.data = array.array('h', itertools.repeat(0, self.ArrayLength))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	# Signed and float only.
	def test_count_op_signed_01(self):
		"""Test count in array code  h - start from -10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, -10, 1)

		arrayfunc.count(self.data, -10)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class count_op_signed_i(unittest.TestCase):
	"""Test for basic count function for signed data.
	count_op_signed_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'i'

		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.i_max
		self.MinVal = arrayfunc.arraylimits.i_min

		self.data = array.array('i', itertools.repeat(0, self.ArrayLength))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	# Signed and float only.
	def test_count_op_signed_01(self):
		"""Test count in array code  i - start from -10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, -10, 1)

		arrayfunc.count(self.data, -10)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class count_op_signed_l(unittest.TestCase):
	"""Test for basic count function for signed data.
	count_op_signed_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'l'

		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min

		self.data = array.array('l', itertools.repeat(0, self.ArrayLength))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	# Signed and float only.
	def test_count_op_signed_01(self):
		"""Test count in array code  l - start from -10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, -10, 1)

		arrayfunc.count(self.data, -10)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class count_op_signed_q(unittest.TestCase):
	"""Test for basic count function for signed data.
	count_op_signed_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'q'

		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min

		self.data = array.array('q', itertools.repeat(0, self.ArrayLength))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	# Signed and float only.
	def test_count_op_signed_01(self):
		"""Test count in array code  q - start from -10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, -10, 1)

		arrayfunc.count(self.data, -10)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class count_op_signed_f(unittest.TestCase):
	"""Test for basic count function for signed data.
	count_op_signed_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'f'

		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min

		self.data = array.array('f', itertools.repeat(0.0, self.ArrayLength))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	# Signed and float only.
	def test_count_op_signed_01(self):
		"""Test count in array code  f - start from -10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, -10.0, 1.0)

		arrayfunc.count(self.data, -10.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class count_op_signed_d(unittest.TestCase):
	"""Test for basic count function for signed data.
	count_op_signed_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'd'

		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min

		self.data = array.array('d', itertools.repeat(0.0, self.ArrayLength))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	# Signed and float only.
	def test_count_op_signed_01(self):
		"""Test count in array code  d - start from -10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, -10.0, 1.0)

		arrayfunc.count(self.data, -10.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class count_nonfinite_f(unittest.TestCase):
	"""Test for nonfinite count function.
	count_nonfinite_template
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

		self.TypeCode = 'f'

		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min

		self.data = array.array('f', [10] * self.ArrayLength)


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq


	########################################################
	def test_count_nonfinite_01(self):
		"""Test count in array code  f - Test for NaN for start.
		"""
		expected = self.PyCount(self.data, math.nan, 1.0)

		arrayfunc.count(self.data, math.nan, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_nonfinite_02(self):
		"""Test count in array code  f - Test for inf for start.
		"""
		expected = self.PyCount(self.data, math.inf, 1.0)

		arrayfunc.count(self.data, math.inf, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_nonfinite_03(self):
		"""Test count in array code  f - Test for -inf for start.
		"""
		expected = self.PyCount(self.data, -math.inf, 1.0)

		arrayfunc.count(self.data, -math.inf, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_nonfinite_04(self):
		"""Test count in array code  f - Test for nan for step.
		"""
		expected = self.PyCount(self.data, 0.0, math.nan)

		arrayfunc.count(self.data, 0.0, math.nan)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_nonfinite_05(self):
		"""Test count in array code  f - Test for inf for step.
		"""
		expected = self.PyCount(self.data, 0.0, math.inf)

		arrayfunc.count(self.data, 0.0, math.inf)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_nonfinite_06(self):
		"""Test count in array code  f - Test for -inf for step.
		"""
		expected = self.PyCount(self.data, 0.0, -math.inf)

		arrayfunc.count(self.data, 0.0, -math.inf)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	# This is not really a non-finite test, but it is convenient to put
	# it here as it is for floating point only.
	def test_count_nonfinite_07(self):
		"""Test count in array code  f - start from 0, count up by a small increment.
		"""
		expected = self.PyCount(self.data, 0.0, 0.1)

		arrayfunc.count(self.data, 0.0, 0.1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class count_nonfinite_d(unittest.TestCase):
	"""Test for nonfinite count function.
	count_nonfinite_template
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

		self.TypeCode = 'd'

		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min

		self.data = array.array('d', [10] * self.ArrayLength)


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq


	########################################################
	def test_count_nonfinite_01(self):
		"""Test count in array code  d - Test for NaN for start.
		"""
		expected = self.PyCount(self.data, math.nan, 1.0)

		arrayfunc.count(self.data, math.nan, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_nonfinite_02(self):
		"""Test count in array code  d - Test for inf for start.
		"""
		expected = self.PyCount(self.data, math.inf, 1.0)

		arrayfunc.count(self.data, math.inf, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_nonfinite_03(self):
		"""Test count in array code  d - Test for -inf for start.
		"""
		expected = self.PyCount(self.data, -math.inf, 1.0)

		arrayfunc.count(self.data, -math.inf, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_nonfinite_04(self):
		"""Test count in array code  d - Test for nan for step.
		"""
		expected = self.PyCount(self.data, 0.0, math.nan)

		arrayfunc.count(self.data, 0.0, math.nan)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_nonfinite_05(self):
		"""Test count in array code  d - Test for inf for step.
		"""
		expected = self.PyCount(self.data, 0.0, math.inf)

		arrayfunc.count(self.data, 0.0, math.inf)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_nonfinite_06(self):
		"""Test count in array code  d - Test for -inf for step.
		"""
		expected = self.PyCount(self.data, 0.0, -math.inf)

		arrayfunc.count(self.data, 0.0, -math.inf)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	# This is not really a non-finite test, but it is convenient to put
	# it here as it is for floating point only.
	def test_count_nonfinite_07(self):
		"""Test count in array code  d - start from 0, count up by a small increment.
		"""
		expected = self.PyCount(self.data, 0.0, 0.1)

		arrayfunc.count(self.data, 0.0, 0.1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class count_overflow_b(unittest.TestCase):
	"""Test for overflow count function.
	count_overflow_template
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
			self.StepOverflow = arrayfunc.arraylimits.b_max * 1.1
			self.StepUnderflow = arrayfunc.arraylimits.b_min * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1
			self.StepOverflow = arrayfunc.arraylimits.b_max + 1
			self.StepUnderflow = arrayfunc.arraylimits.b_min - 1


		self.data = array.array('b', [0] * self.ArrayLength)


	########################################################
	def test_count_ovfl_01(self):
		"""Test count overflow operation in array code  b - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Overflow, 1)


	########################################################
	def test_count_ovfl_02(self):
		"""Test count overflow operation in array code  b - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0, self.StepOverflow)


	########################################################
	def test_count_ovfl_03(self):
		"""Test count overflow operation in array code  b - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Underflow, -1)


	########################################################
	def test_count_ovfl_04(self):
		"""Test count overflow operation in array code  b - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0, self.StepUnderflow)


##############################################################################


##############################################################################
class count_overflow_B(unittest.TestCase):
	"""Test for overflow count function.
	count_overflow_template
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
			self.StepOverflow = arrayfunc.arraylimits.b_max * 1.1
			self.StepUnderflow = arrayfunc.arraylimits.b_min * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1
			self.StepOverflow = arrayfunc.arraylimits.b_max + 1
			self.StepUnderflow = arrayfunc.arraylimits.b_min - 1


		self.data = array.array('B', [0] * self.ArrayLength)


	########################################################
	def test_count_ovfl_01(self):
		"""Test count overflow operation in array code  B - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Overflow, 1)


	########################################################
	def test_count_ovfl_02(self):
		"""Test count overflow operation in array code  B - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0, self.StepOverflow)


	########################################################
	def test_count_ovfl_03(self):
		"""Test count overflow operation in array code  B - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Underflow, -1)


	########################################################
	def test_count_ovfl_04(self):
		"""Test count overflow operation in array code  B - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0, self.StepUnderflow)


##############################################################################


##############################################################################
class count_overflow_h(unittest.TestCase):
	"""Test for overflow count function.
	count_overflow_template
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
			self.StepOverflow = arrayfunc.arraylimits.h_max * 1.1
			self.StepUnderflow = arrayfunc.arraylimits.h_min * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1
			self.StepOverflow = arrayfunc.arraylimits.h_max + 1
			self.StepUnderflow = arrayfunc.arraylimits.h_min - 1


		self.data = array.array('h', [0] * self.ArrayLength)


	########################################################
	def test_count_ovfl_01(self):
		"""Test count overflow operation in array code  h - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Overflow, 1)


	########################################################
	def test_count_ovfl_02(self):
		"""Test count overflow operation in array code  h - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0, self.StepOverflow)


	########################################################
	def test_count_ovfl_03(self):
		"""Test count overflow operation in array code  h - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Underflow, -1)


	########################################################
	def test_count_ovfl_04(self):
		"""Test count overflow operation in array code  h - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0, self.StepUnderflow)


##############################################################################


##############################################################################
class count_overflow_H(unittest.TestCase):
	"""Test for overflow count function.
	count_overflow_template
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
			self.StepOverflow = arrayfunc.arraylimits.h_max * 1.1
			self.StepUnderflow = arrayfunc.arraylimits.h_min * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1
			self.StepOverflow = arrayfunc.arraylimits.h_max + 1
			self.StepUnderflow = arrayfunc.arraylimits.h_min - 1


		self.data = array.array('H', [0] * self.ArrayLength)


	########################################################
	def test_count_ovfl_01(self):
		"""Test count overflow operation in array code  H - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Overflow, 1)


	########################################################
	def test_count_ovfl_02(self):
		"""Test count overflow operation in array code  H - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0, self.StepOverflow)


	########################################################
	def test_count_ovfl_03(self):
		"""Test count overflow operation in array code  H - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Underflow, -1)


	########################################################
	def test_count_ovfl_04(self):
		"""Test count overflow operation in array code  H - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0, self.StepUnderflow)


##############################################################################


##############################################################################
class count_overflow_i(unittest.TestCase):
	"""Test for overflow count function.
	count_overflow_template
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
			self.StepOverflow = arrayfunc.arraylimits.i_max * 1.1
			self.StepUnderflow = arrayfunc.arraylimits.i_min * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1
			self.StepOverflow = arrayfunc.arraylimits.i_max + 1
			self.StepUnderflow = arrayfunc.arraylimits.i_min - 1


		self.data = array.array('i', [0] * self.ArrayLength)


	########################################################
	def test_count_ovfl_01(self):
		"""Test count overflow operation in array code  i - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Overflow, 1)


	########################################################
	def test_count_ovfl_02(self):
		"""Test count overflow operation in array code  i - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0, self.StepOverflow)


	########################################################
	def test_count_ovfl_03(self):
		"""Test count overflow operation in array code  i - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Underflow, -1)


	########################################################
	def test_count_ovfl_04(self):
		"""Test count overflow operation in array code  i - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0, self.StepUnderflow)


##############################################################################


##############################################################################
class count_overflow_I(unittest.TestCase):
	"""Test for overflow count function.
	count_overflow_template
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
			self.StepOverflow = arrayfunc.arraylimits.i_max * 1.1
			self.StepUnderflow = arrayfunc.arraylimits.i_min * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1
			self.StepOverflow = arrayfunc.arraylimits.i_max + 1
			self.StepUnderflow = arrayfunc.arraylimits.i_min - 1


		self.data = array.array('I', [0] * self.ArrayLength)


	########################################################
	def test_count_ovfl_01(self):
		"""Test count overflow operation in array code  I - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Overflow, 1)


	########################################################
	def test_count_ovfl_02(self):
		"""Test count overflow operation in array code  I - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0, self.StepOverflow)


	########################################################
	def test_count_ovfl_03(self):
		"""Test count overflow operation in array code  I - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Underflow, -1)


	########################################################
	def test_count_ovfl_04(self):
		"""Test count overflow operation in array code  I - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0, self.StepUnderflow)


##############################################################################


##############################################################################
class count_overflow_l(unittest.TestCase):
	"""Test for overflow count function.
	count_overflow_template
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
			self.StepOverflow = arrayfunc.arraylimits.l_max * 1.1
			self.StepUnderflow = arrayfunc.arraylimits.l_min * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1
			self.StepOverflow = arrayfunc.arraylimits.l_max + 1
			self.StepUnderflow = arrayfunc.arraylimits.l_min - 1


		self.data = array.array('l', [0] * self.ArrayLength)


	########################################################
	def test_count_ovfl_01(self):
		"""Test count overflow operation in array code  l - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Overflow, 1)


	########################################################
	def test_count_ovfl_02(self):
		"""Test count overflow operation in array code  l - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0, self.StepOverflow)


	########################################################
	def test_count_ovfl_03(self):
		"""Test count overflow operation in array code  l - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Underflow, -1)


	########################################################
	def test_count_ovfl_04(self):
		"""Test count overflow operation in array code  l - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0, self.StepUnderflow)


##############################################################################


##############################################################################
class count_overflow_q(unittest.TestCase):
	"""Test for overflow count function.
	count_overflow_template
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
			self.StepOverflow = arrayfunc.arraylimits.q_max * 1.1
			self.StepUnderflow = arrayfunc.arraylimits.q_min * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1
			self.StepOverflow = arrayfunc.arraylimits.q_max + 1
			self.StepUnderflow = arrayfunc.arraylimits.q_min - 1


		self.data = array.array('q', [0] * self.ArrayLength)


	########################################################
	def test_count_ovfl_01(self):
		"""Test count overflow operation in array code  q - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Overflow, 1)


	########################################################
	def test_count_ovfl_02(self):
		"""Test count overflow operation in array code  q - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0, self.StepOverflow)


	########################################################
	def test_count_ovfl_03(self):
		"""Test count overflow operation in array code  q - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Underflow, -1)


	########################################################
	def test_count_ovfl_04(self):
		"""Test count overflow operation in array code  q - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0, self.StepUnderflow)


##############################################################################


##############################################################################
class count_overflow_f(unittest.TestCase):
	"""Test for overflow count function.
	count_overflow_template
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
			self.StepOverflow = arrayfunc.arraylimits.f_max * 1.1
			self.StepUnderflow = arrayfunc.arraylimits.f_min * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1
			self.StepOverflow = arrayfunc.arraylimits.f_max + 1
			self.StepUnderflow = arrayfunc.arraylimits.f_min - 1


		self.data = array.array('f', [0] * self.ArrayLength)


	########################################################
	def test_count_ovfl_01(self):
		"""Test count overflow operation in array code  f - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Overflow, 1.0)


	########################################################
	def test_count_ovfl_02(self):
		"""Test count overflow operation in array code  f - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0.0, self.StepOverflow)


	########################################################
	def test_count_ovfl_03(self):
		"""Test count overflow operation in array code  f - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Underflow, -1.0)


	########################################################
	def test_count_ovfl_04(self):
		"""Test count overflow operation in array code  f - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0.0, self.StepUnderflow)


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
			f.write('count\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
