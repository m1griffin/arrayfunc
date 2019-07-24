#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_cycle.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     11-Jun-2014.
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
"""This conducts unit tests for cycle.
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
class cycle_param_b(unittest.TestCase):
	"""Test for basic cycle parameter tests.
	cycle_param_template
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



	########################################################
	def test_cycle_param_01(self):
		"""Test cycle in array code  b - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.cycle(self.zerodata, 0, 100, 100)


	########################################################
	def test_cycle_param_02(self):
		"""Test cycle in array code  b - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle()


	########################################################
	def test_cycle_param_03(self):
		"""Test cycle in array code  b - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data, 0, 100, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle([1, 2, 3, 4], [1, 2, 3, 4])


	########################################################
	def test_cycle_param_04(self):
		"""Test cycle in array code  b - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 0, 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)


	########################################################
	def test_cycle_param_05(self):
		"""Test cycle in array code  b - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 'a', 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)



##############################################################################



##############################################################################
class cycle_param_B(unittest.TestCase):
	"""Test for basic cycle parameter tests.
	cycle_param_template
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



	########################################################
	def test_cycle_param_01(self):
		"""Test cycle in array code  B - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.cycle(self.zerodata, 0, 100, 100)


	########################################################
	def test_cycle_param_02(self):
		"""Test cycle in array code  B - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle()


	########################################################
	def test_cycle_param_03(self):
		"""Test cycle in array code  B - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data, 0, 100, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle([1, 2, 3, 4], [1, 2, 3, 4])


	########################################################
	def test_cycle_param_04(self):
		"""Test cycle in array code  B - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 0, 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)


	########################################################
	def test_cycle_param_05(self):
		"""Test cycle in array code  B - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 'a', 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)



##############################################################################



##############################################################################
class cycle_param_h(unittest.TestCase):
	"""Test for basic cycle parameter tests.
	cycle_param_template
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



	########################################################
	def test_cycle_param_01(self):
		"""Test cycle in array code  h - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.cycle(self.zerodata, 0, 100, 100)


	########################################################
	def test_cycle_param_02(self):
		"""Test cycle in array code  h - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle()


	########################################################
	def test_cycle_param_03(self):
		"""Test cycle in array code  h - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data, 0, 100, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle([1, 2, 3, 4], [1, 2, 3, 4])


	########################################################
	def test_cycle_param_04(self):
		"""Test cycle in array code  h - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 0, 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)


	########################################################
	def test_cycle_param_05(self):
		"""Test cycle in array code  h - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 'a', 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)



##############################################################################



##############################################################################
class cycle_param_H(unittest.TestCase):
	"""Test for basic cycle parameter tests.
	cycle_param_template
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



	########################################################
	def test_cycle_param_01(self):
		"""Test cycle in array code  H - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.cycle(self.zerodata, 0, 100, 100)


	########################################################
	def test_cycle_param_02(self):
		"""Test cycle in array code  H - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle()


	########################################################
	def test_cycle_param_03(self):
		"""Test cycle in array code  H - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data, 0, 100, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle([1, 2, 3, 4], [1, 2, 3, 4])


	########################################################
	def test_cycle_param_04(self):
		"""Test cycle in array code  H - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 0, 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)


	########################################################
	def test_cycle_param_05(self):
		"""Test cycle in array code  H - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 'a', 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)



##############################################################################



##############################################################################
class cycle_param_i(unittest.TestCase):
	"""Test for basic cycle parameter tests.
	cycle_param_template
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



	########################################################
	def test_cycle_param_01(self):
		"""Test cycle in array code  i - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.cycle(self.zerodata, 0, 100, 100)


	########################################################
	def test_cycle_param_02(self):
		"""Test cycle in array code  i - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle()


	########################################################
	def test_cycle_param_03(self):
		"""Test cycle in array code  i - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data, 0, 100, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle([1, 2, 3, 4], [1, 2, 3, 4])


	########################################################
	def test_cycle_param_04(self):
		"""Test cycle in array code  i - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 0, 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)


	########################################################
	def test_cycle_param_05(self):
		"""Test cycle in array code  i - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 'a', 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)



##############################################################################



##############################################################################
class cycle_param_I(unittest.TestCase):
	"""Test for basic cycle parameter tests.
	cycle_param_template
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



	########################################################
	def test_cycle_param_01(self):
		"""Test cycle in array code  I - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.cycle(self.zerodata, 0, 100, 100)


	########################################################
	def test_cycle_param_02(self):
		"""Test cycle in array code  I - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle()


	########################################################
	def test_cycle_param_03(self):
		"""Test cycle in array code  I - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data, 0, 100, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle([1, 2, 3, 4], [1, 2, 3, 4])


	########################################################
	def test_cycle_param_04(self):
		"""Test cycle in array code  I - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 0, 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)


	########################################################
	def test_cycle_param_05(self):
		"""Test cycle in array code  I - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 'a', 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)



##############################################################################



##############################################################################
class cycle_param_l(unittest.TestCase):
	"""Test for basic cycle parameter tests.
	cycle_param_template
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



	########################################################
	def test_cycle_param_01(self):
		"""Test cycle in array code  l - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.cycle(self.zerodata, 0, 100, 100)


	########################################################
	def test_cycle_param_02(self):
		"""Test cycle in array code  l - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle()


	########################################################
	def test_cycle_param_03(self):
		"""Test cycle in array code  l - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data, 0, 100, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle([1, 2, 3, 4], [1, 2, 3, 4])


	########################################################
	def test_cycle_param_04(self):
		"""Test cycle in array code  l - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 0, 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)


	########################################################
	def test_cycle_param_05(self):
		"""Test cycle in array code  l - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 'a', 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)



##############################################################################



##############################################################################
class cycle_param_L(unittest.TestCase):
	"""Test for basic cycle parameter tests.
	cycle_param_template
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



	########################################################
	def test_cycle_param_01(self):
		"""Test cycle in array code  L - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.cycle(self.zerodata, 0, 100, 100)


	########################################################
	def test_cycle_param_02(self):
		"""Test cycle in array code  L - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle()


	########################################################
	def test_cycle_param_03(self):
		"""Test cycle in array code  L - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data, 0, 100, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle([1, 2, 3, 4], [1, 2, 3, 4])


	########################################################
	def test_cycle_param_04(self):
		"""Test cycle in array code  L - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 0, 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)


	########################################################
	def test_cycle_param_05(self):
		"""Test cycle in array code  L - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 'a', 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)



##############################################################################



##############################################################################
class cycle_param_q(unittest.TestCase):
	"""Test for basic cycle parameter tests.
	cycle_param_template
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



	########################################################
	def test_cycle_param_01(self):
		"""Test cycle in array code  q - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.cycle(self.zerodata, 0, 100, 100)


	########################################################
	def test_cycle_param_02(self):
		"""Test cycle in array code  q - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle()


	########################################################
	def test_cycle_param_03(self):
		"""Test cycle in array code  q - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data, 0, 100, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle([1, 2, 3, 4], [1, 2, 3, 4])


	########################################################
	def test_cycle_param_04(self):
		"""Test cycle in array code  q - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 0, 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)


	########################################################
	def test_cycle_param_05(self):
		"""Test cycle in array code  q - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 'a', 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)



##############################################################################



##############################################################################
class cycle_param_Q(unittest.TestCase):
	"""Test for basic cycle parameter tests.
	cycle_param_template
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



	########################################################
	def test_cycle_param_01(self):
		"""Test cycle in array code  Q - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.cycle(self.zerodata, 0, 100, 100)


	########################################################
	def test_cycle_param_02(self):
		"""Test cycle in array code  Q - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle()


	########################################################
	def test_cycle_param_03(self):
		"""Test cycle in array code  Q - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data, 0, 100, 1, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle([1, 2, 3, 4], [1, 2, 3, 4])


	########################################################
	def test_cycle_param_04(self):
		"""Test cycle in array code  Q - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 0, 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)


	########################################################
	def test_cycle_param_05(self):
		"""Test cycle in array code  Q - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 'a', 100, 1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)



##############################################################################



##############################################################################
class cycle_param_f(unittest.TestCase):
	"""Test for basic cycle parameter tests.
	cycle_param_template
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



	########################################################
	def test_cycle_param_01(self):
		"""Test cycle in array code  f - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.cycle(self.zerodata, 0.0, 100.0, 100.0)


	########################################################
	def test_cycle_param_02(self):
		"""Test cycle in array code  f - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle()


	########################################################
	def test_cycle_param_03(self):
		"""Test cycle in array code  f - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data, 0.0, 100.0, 1.0, 1.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle([1, 2, 3, 4], [1, 2, 3, 4])


	########################################################
	def test_cycle_param_04(self):
		"""Test cycle in array code  f - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 0.0, 100.0, 1.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)


	########################################################
	def test_cycle_param_05(self):
		"""Test cycle in array code  f - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 'a', 100.0, 1.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)



##############################################################################



##############################################################################
class cycle_param_d(unittest.TestCase):
	"""Test for basic cycle parameter tests.
	cycle_param_template
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



	########################################################
	def test_cycle_param_01(self):
		"""Test cycle in array code  d - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.cycle(self.zerodata, 0.0, 100.0, 100.0)


	########################################################
	def test_cycle_param_02(self):
		"""Test cycle in array code  d - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle()


	########################################################
	def test_cycle_param_03(self):
		"""Test cycle in array code  d - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data, 0.0, 100.0, 1.0, 1.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle([1, 2, 3, 4], [1, 2, 3, 4])


	########################################################
	def test_cycle_param_04(self):
		"""Test cycle in array code  d - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 0.0, 100.0, 1.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)


	########################################################
	def test_cycle_param_05(self):
		"""Test cycle in array code  d - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 'a', 100.0, 1.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)



##############################################################################



##############################################################################
class cycle_b(unittest.TestCase):
	"""Test for basic cycle operation function.
	cycle_op_template
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

		self.TypeCode = 'b'

		self.ArrayLength = 512

		self.data = array.array(self.TypeCode, itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.b_max
		self.MinVal = arrayfunc.arraylimits.b_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_01(self):
		"""Test cycle in array code  b - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 1)

		arrayfunc.cycle(self.data, 0, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_02(self):
		"""Test cycle in array code  b - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 1)

		arrayfunc.cycle(self.data, 10, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_03(self):
		"""Test cycle in array code  b - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 7)

		arrayfunc.cycle(self.data, 0, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_04(self):
		"""Test cycle in array code  b - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 7)

		arrayfunc.cycle(self.data, 10, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_05(self):
		"""Test cycle in array code  b - start from 10, count down by 1, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 125, 1)

		arrayfunc.cycle(self.data, 10, 125)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_06(self):
		"""Test cycle in array code  b - start from 10, count down by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125, 10, 7)

		arrayfunc.cycle(self.data, 125, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)




##############################################################################


##############################################################################
class cycle_B(unittest.TestCase):
	"""Test for basic cycle operation function.
	cycle_op_template
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

		self.TypeCode = 'B'

		self.ArrayLength = 512

		self.data = array.array(self.TypeCode, itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.B_max
		self.MinVal = arrayfunc.arraylimits.B_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_01(self):
		"""Test cycle in array code  B - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 1)

		arrayfunc.cycle(self.data, 0, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_02(self):
		"""Test cycle in array code  B - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 1)

		arrayfunc.cycle(self.data, 10, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_03(self):
		"""Test cycle in array code  B - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 7)

		arrayfunc.cycle(self.data, 0, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_04(self):
		"""Test cycle in array code  B - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 7)

		arrayfunc.cycle(self.data, 10, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_05(self):
		"""Test cycle in array code  B - start from 10, count down by 1, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 125, 1)

		arrayfunc.cycle(self.data, 10, 125)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_06(self):
		"""Test cycle in array code  B - start from 10, count down by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125, 10, 7)

		arrayfunc.cycle(self.data, 125, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)




##############################################################################


##############################################################################
class cycle_h(unittest.TestCase):
	"""Test for basic cycle operation function.
	cycle_op_template
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

		self.TypeCode = 'h'

		self.ArrayLength = 512

		self.data = array.array(self.TypeCode, itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.h_max
		self.MinVal = arrayfunc.arraylimits.h_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_01(self):
		"""Test cycle in array code  h - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 1)

		arrayfunc.cycle(self.data, 0, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_02(self):
		"""Test cycle in array code  h - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 1)

		arrayfunc.cycle(self.data, 10, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_03(self):
		"""Test cycle in array code  h - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 7)

		arrayfunc.cycle(self.data, 0, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_04(self):
		"""Test cycle in array code  h - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 7)

		arrayfunc.cycle(self.data, 10, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_05(self):
		"""Test cycle in array code  h - start from 10, count down by 1, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 125, 1)

		arrayfunc.cycle(self.data, 10, 125)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_06(self):
		"""Test cycle in array code  h - start from 10, count down by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125, 10, 7)

		arrayfunc.cycle(self.data, 125, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)




##############################################################################


##############################################################################
class cycle_H(unittest.TestCase):
	"""Test for basic cycle operation function.
	cycle_op_template
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

		self.TypeCode = 'H'

		self.ArrayLength = 512

		self.data = array.array(self.TypeCode, itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.H_max
		self.MinVal = arrayfunc.arraylimits.H_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_01(self):
		"""Test cycle in array code  H - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 1)

		arrayfunc.cycle(self.data, 0, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_02(self):
		"""Test cycle in array code  H - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 1)

		arrayfunc.cycle(self.data, 10, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_03(self):
		"""Test cycle in array code  H - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 7)

		arrayfunc.cycle(self.data, 0, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_04(self):
		"""Test cycle in array code  H - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 7)

		arrayfunc.cycle(self.data, 10, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_05(self):
		"""Test cycle in array code  H - start from 10, count down by 1, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 125, 1)

		arrayfunc.cycle(self.data, 10, 125)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_06(self):
		"""Test cycle in array code  H - start from 10, count down by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125, 10, 7)

		arrayfunc.cycle(self.data, 125, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)




##############################################################################


##############################################################################
class cycle_i(unittest.TestCase):
	"""Test for basic cycle operation function.
	cycle_op_template
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

		self.TypeCode = 'i'

		self.ArrayLength = 512

		self.data = array.array(self.TypeCode, itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.i_max
		self.MinVal = arrayfunc.arraylimits.i_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_01(self):
		"""Test cycle in array code  i - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 1)

		arrayfunc.cycle(self.data, 0, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_02(self):
		"""Test cycle in array code  i - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 1)

		arrayfunc.cycle(self.data, 10, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_03(self):
		"""Test cycle in array code  i - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 7)

		arrayfunc.cycle(self.data, 0, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_04(self):
		"""Test cycle in array code  i - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 7)

		arrayfunc.cycle(self.data, 10, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_05(self):
		"""Test cycle in array code  i - start from 10, count down by 1, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 125, 1)

		arrayfunc.cycle(self.data, 10, 125)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_06(self):
		"""Test cycle in array code  i - start from 10, count down by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125, 10, 7)

		arrayfunc.cycle(self.data, 125, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)




##############################################################################


##############################################################################
class cycle_I(unittest.TestCase):
	"""Test for basic cycle operation function.
	cycle_op_template
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

		self.TypeCode = 'I'

		self.ArrayLength = 512

		self.data = array.array(self.TypeCode, itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.I_max
		self.MinVal = arrayfunc.arraylimits.I_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_01(self):
		"""Test cycle in array code  I - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 1)

		arrayfunc.cycle(self.data, 0, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_02(self):
		"""Test cycle in array code  I - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 1)

		arrayfunc.cycle(self.data, 10, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_03(self):
		"""Test cycle in array code  I - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 7)

		arrayfunc.cycle(self.data, 0, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_04(self):
		"""Test cycle in array code  I - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 7)

		arrayfunc.cycle(self.data, 10, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_05(self):
		"""Test cycle in array code  I - start from 10, count down by 1, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 125, 1)

		arrayfunc.cycle(self.data, 10, 125)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_06(self):
		"""Test cycle in array code  I - start from 10, count down by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125, 10, 7)

		arrayfunc.cycle(self.data, 125, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)




##############################################################################


##############################################################################
class cycle_l(unittest.TestCase):
	"""Test for basic cycle operation function.
	cycle_op_template
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

		self.TypeCode = 'l'

		self.ArrayLength = 512

		self.data = array.array(self.TypeCode, itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_01(self):
		"""Test cycle in array code  l - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 1)

		arrayfunc.cycle(self.data, 0, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_02(self):
		"""Test cycle in array code  l - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 1)

		arrayfunc.cycle(self.data, 10, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_03(self):
		"""Test cycle in array code  l - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 7)

		arrayfunc.cycle(self.data, 0, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_04(self):
		"""Test cycle in array code  l - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 7)

		arrayfunc.cycle(self.data, 10, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_05(self):
		"""Test cycle in array code  l - start from 10, count down by 1, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 125, 1)

		arrayfunc.cycle(self.data, 10, 125)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_06(self):
		"""Test cycle in array code  l - start from 10, count down by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125, 10, 7)

		arrayfunc.cycle(self.data, 125, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)




##############################################################################


##############################################################################
class cycle_L(unittest.TestCase):
	"""Test for basic cycle operation function.
	cycle_op_template
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

		self.TypeCode = 'L'

		self.ArrayLength = 512

		self.data = array.array(self.TypeCode, itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.L_max
		self.MinVal = arrayfunc.arraylimits.L_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_01(self):
		"""Test cycle in array code  L - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 1)

		arrayfunc.cycle(self.data, 0, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_02(self):
		"""Test cycle in array code  L - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 1)

		arrayfunc.cycle(self.data, 10, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_03(self):
		"""Test cycle in array code  L - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 7)

		arrayfunc.cycle(self.data, 0, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_04(self):
		"""Test cycle in array code  L - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 7)

		arrayfunc.cycle(self.data, 10, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_05(self):
		"""Test cycle in array code  L - start from 10, count down by 1, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 125, 1)

		arrayfunc.cycle(self.data, 10, 125)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_06(self):
		"""Test cycle in array code  L - start from 10, count down by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125, 10, 7)

		arrayfunc.cycle(self.data, 125, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)




##############################################################################


##############################################################################
class cycle_q(unittest.TestCase):
	"""Test for basic cycle operation function.
	cycle_op_template
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

		self.TypeCode = 'q'

		self.ArrayLength = 512

		self.data = array.array(self.TypeCode, itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_01(self):
		"""Test cycle in array code  q - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 1)

		arrayfunc.cycle(self.data, 0, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_02(self):
		"""Test cycle in array code  q - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 1)

		arrayfunc.cycle(self.data, 10, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_03(self):
		"""Test cycle in array code  q - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 7)

		arrayfunc.cycle(self.data, 0, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_04(self):
		"""Test cycle in array code  q - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 7)

		arrayfunc.cycle(self.data, 10, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_05(self):
		"""Test cycle in array code  q - start from 10, count down by 1, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 125, 1)

		arrayfunc.cycle(self.data, 10, 125)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_06(self):
		"""Test cycle in array code  q - start from 10, count down by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125, 10, 7)

		arrayfunc.cycle(self.data, 125, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)




##############################################################################


##############################################################################
class cycle_Q(unittest.TestCase):
	"""Test for basic cycle operation function.
	cycle_op_template
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

		self.TypeCode = 'Q'

		self.ArrayLength = 512

		self.data = array.array(self.TypeCode, itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.Q_max
		self.MinVal = arrayfunc.arraylimits.Q_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_01(self):
		"""Test cycle in array code  Q - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 1)

		arrayfunc.cycle(self.data, 0, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_02(self):
		"""Test cycle in array code  Q - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 1)

		arrayfunc.cycle(self.data, 10, 100)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_03(self):
		"""Test cycle in array code  Q - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0, 100, 7)

		arrayfunc.cycle(self.data, 0, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_04(self):
		"""Test cycle in array code  Q - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, 7)

		arrayfunc.cycle(self.data, 10, 100, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_05(self):
		"""Test cycle in array code  Q - start from 10, count down by 1, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 125, 1)

		arrayfunc.cycle(self.data, 10, 125)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_06(self):
		"""Test cycle in array code  Q - start from 10, count down by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125, 10, 7)

		arrayfunc.cycle(self.data, 125, 10, 7)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)




##############################################################################


##############################################################################
class cycle_f(unittest.TestCase):
	"""Test for basic cycle operation function.
	cycle_op_template
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

		self.data = array.array(self.TypeCode, itertools.repeat(0.0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_01(self):
		"""Test cycle in array code  f - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0.0, 100.0, 1.0)

		arrayfunc.cycle(self.data, 0.0, 100.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_02(self):
		"""Test cycle in array code  f - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10.0, 100.0, 1.0)

		arrayfunc.cycle(self.data, 10.0, 100.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_03(self):
		"""Test cycle in array code  f - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0.0, 100.0, 7.0)

		arrayfunc.cycle(self.data, 0.0, 100.0, 7.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_04(self):
		"""Test cycle in array code  f - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10.0, 100.0, 7.0)

		arrayfunc.cycle(self.data, 10.0, 100.0, 7.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_05(self):
		"""Test cycle in array code  f - start from 10, count down by 1, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10.0, 125.0, 1.0)

		arrayfunc.cycle(self.data, 10.0, 125.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_06(self):
		"""Test cycle in array code  f - start from 10, count down by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125.0, 10.0, 7.0)

		arrayfunc.cycle(self.data, 125.0, 10.0, 7.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)




##############################################################################


##############################################################################
class cycle_d(unittest.TestCase):
	"""Test for basic cycle operation function.
	cycle_op_template
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

		self.data = array.array(self.TypeCode, itertools.repeat(0.0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_01(self):
		"""Test cycle in array code  d - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0.0, 100.0, 1.0)

		arrayfunc.cycle(self.data, 0.0, 100.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_02(self):
		"""Test cycle in array code  d - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10.0, 100.0, 1.0)

		arrayfunc.cycle(self.data, 10.0, 100.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_03(self):
		"""Test cycle in array code  d - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0.0, 100.0, 7.0)

		arrayfunc.cycle(self.data, 0.0, 100.0, 7.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_04(self):
		"""Test cycle in array code  d - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10.0, 100.0, 7.0)

		arrayfunc.cycle(self.data, 10.0, 100.0, 7.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_05(self):
		"""Test cycle in array code  d - start from 10, count down by 1, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10.0, 125.0, 1.0)

		arrayfunc.cycle(self.data, 10.0, 125.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_06(self):
		"""Test cycle in array code  d - start from 10, count down by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125.0, 10.0, 7.0)

		arrayfunc.cycle(self.data, 125.0, 10.0, 7.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)




##############################################################################


##############################################################################
class cycle_op_signed_b(unittest.TestCase):
	"""Test for basic cycle operation function for signed arrays only.
	cycle_op_signed_template
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

		self.TypeCode = 'b'

		self.ArrayLength = 512

		self.data = array.array(self.TypeCode, itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.b_max
		self.MinVal = arrayfunc.arraylimits.b_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_op_signed_01(self):
		"""Test cycle in array code  b - start from 10, count down by 1 using a negative step, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125, 10, -1)

		arrayfunc.cycle(self.data, 125, 10, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_op_signed_02(self):
		"""Test cycle in array code  b - start from -10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, -10, 100, 1)

		arrayfunc.cycle(self.data, -10, 100, 1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_op_signed_03(self):
		"""Test cycle in array code  b - start from 10, down up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, -1)

		arrayfunc.cycle(self.data, 10, 100, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class cycle_op_signed_h(unittest.TestCase):
	"""Test for basic cycle operation function for signed arrays only.
	cycle_op_signed_template
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

		self.TypeCode = 'h'

		self.ArrayLength = 512

		self.data = array.array(self.TypeCode, itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.h_max
		self.MinVal = arrayfunc.arraylimits.h_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_op_signed_01(self):
		"""Test cycle in array code  h - start from 10, count down by 1 using a negative step, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125, 10, -1)

		arrayfunc.cycle(self.data, 125, 10, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_op_signed_02(self):
		"""Test cycle in array code  h - start from -10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, -10, 100, 1)

		arrayfunc.cycle(self.data, -10, 100, 1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_op_signed_03(self):
		"""Test cycle in array code  h - start from 10, down up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, -1)

		arrayfunc.cycle(self.data, 10, 100, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class cycle_op_signed_i(unittest.TestCase):
	"""Test for basic cycle operation function for signed arrays only.
	cycle_op_signed_template
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

		self.TypeCode = 'i'

		self.ArrayLength = 512

		self.data = array.array(self.TypeCode, itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.i_max
		self.MinVal = arrayfunc.arraylimits.i_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_op_signed_01(self):
		"""Test cycle in array code  i - start from 10, count down by 1 using a negative step, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125, 10, -1)

		arrayfunc.cycle(self.data, 125, 10, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_op_signed_02(self):
		"""Test cycle in array code  i - start from -10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, -10, 100, 1)

		arrayfunc.cycle(self.data, -10, 100, 1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_op_signed_03(self):
		"""Test cycle in array code  i - start from 10, down up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, -1)

		arrayfunc.cycle(self.data, 10, 100, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class cycle_op_signed_l(unittest.TestCase):
	"""Test for basic cycle operation function for signed arrays only.
	cycle_op_signed_template
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

		self.TypeCode = 'l'

		self.ArrayLength = 512

		self.data = array.array(self.TypeCode, itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.l_max
		self.MinVal = arrayfunc.arraylimits.l_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_op_signed_01(self):
		"""Test cycle in array code  l - start from 10, count down by 1 using a negative step, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125, 10, -1)

		arrayfunc.cycle(self.data, 125, 10, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_op_signed_02(self):
		"""Test cycle in array code  l - start from -10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, -10, 100, 1)

		arrayfunc.cycle(self.data, -10, 100, 1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_op_signed_03(self):
		"""Test cycle in array code  l - start from 10, down up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, -1)

		arrayfunc.cycle(self.data, 10, 100, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class cycle_op_signed_q(unittest.TestCase):
	"""Test for basic cycle operation function for signed arrays only.
	cycle_op_signed_template
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

		self.TypeCode = 'q'

		self.ArrayLength = 512

		self.data = array.array(self.TypeCode, itertools.repeat(0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.q_max
		self.MinVal = arrayfunc.arraylimits.q_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_op_signed_01(self):
		"""Test cycle in array code  q - start from 10, count down by 1 using a negative step, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125, 10, -1)

		arrayfunc.cycle(self.data, 125, 10, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_op_signed_02(self):
		"""Test cycle in array code  q - start from -10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, -10, 100, 1)

		arrayfunc.cycle(self.data, -10, 100, 1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_op_signed_03(self):
		"""Test cycle in array code  q - start from 10, down up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10, 100, -1)

		arrayfunc.cycle(self.data, 10, 100, -1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class cycle_op_signed_f(unittest.TestCase):
	"""Test for basic cycle operation function for signed arrays only.
	cycle_op_signed_template
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

		self.data = array.array(self.TypeCode, itertools.repeat(0.0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_op_signed_01(self):
		"""Test cycle in array code  f - start from 10, count down by 1 using a negative step, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125.0, 10.0, -1.0)

		arrayfunc.cycle(self.data, 125.0, 10.0, -1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_op_signed_02(self):
		"""Test cycle in array code  f - start from -10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, -10.0, 100.0, 1.0)

		arrayfunc.cycle(self.data, -10.0, 100.0, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_op_signed_03(self):
		"""Test cycle in array code  f - start from 10, down up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10.0, 100.0, -1.0)

		arrayfunc.cycle(self.data, 10.0, 100.0, -1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class cycle_op_signed_d(unittest.TestCase):
	"""Test for basic cycle operation function for signed arrays only.
	cycle_op_signed_template
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

		self.data = array.array(self.TypeCode, itertools.repeat(0.0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq



	########################################################
	def test_cycle_op_signed_01(self):
		"""Test cycle in array code  d - start from 10, count down by 1 using a negative step, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125.0, 10.0, -1.0)

		arrayfunc.cycle(self.data, 125.0, 10.0, -1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_op_signed_02(self):
		"""Test cycle in array code  d - start from -10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, -10.0, 100.0, 1.0)

		arrayfunc.cycle(self.data, -10.0, 100.0, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_op_signed_03(self):
		"""Test cycle in array code  d - start from 10, down up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10.0, 100.0, -1.0)

		arrayfunc.cycle(self.data, 10.0, 100.0, -1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
class cycle_nonfinite_f(unittest.TestCase):
	"""Test for nonfinite cycle function.
	cycle_nonfinite_template
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

		self.TypeCode = 'f'

		self.data = array.array(self.TypeCode, itertools.repeat(0.0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.f_max
		self.MinVal = arrayfunc.arraylimits.f_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq




	########################################################
	def test_cycle_nonfinite_01(self):
		"""Test cycle in array code  f - Invalid param nan for start.
		"""
		expected = self.PyCycle(self.data, math.nan, 1000.0, 1.0)

		arrayfunc.cycle(self.data, math.nan, 1000.0, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_02(self):
		"""Test cycle in array code  f - Invalid param inf for start.
		"""
		expected = self.PyCycle(self.data, math.inf, 1000.0, 1.0)

		arrayfunc.cycle(self.data, math.inf, 1000.0, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_03(self):
		"""Test cycle in array code  f - Invalid param -inf for start.
		"""
		expected = self.PyCycle(self.data, -math.inf, 1000.0, 1.0)

		arrayfunc.cycle(self.data, -math.inf, 1000.0, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_04(self):
		"""Test cycle in array code  f - Invalid param nan for stop.
		"""
		expected = self.PyCycle(self.data, 0.0, math.nan, 1.0)

		arrayfunc.cycle(self.data, 0.0, math.nan, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_05(self):
		"""Test cycle in array code  f - Invalid param inf for stop.
		"""
		expected = self.PyCycle(self.data, 0.0, math.inf, 1.0)

		arrayfunc.cycle(self.data, 0.0, math.inf, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_06(self):
		"""Test cycle in array code  f - Invalid param -inf for stop.
		"""
		expected = self.PyCycle(self.data, 0.0, -math.inf, 1.0)

		arrayfunc.cycle(self.data, 0.0, -math.inf, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_07(self):
		"""Test cycle in array code  f - Invalid param nan for step.
		"""
		expected = self.PyCycle(self.data, 0.0, 1000.0, math.nan)

		arrayfunc.cycle(self.data, 0.0, 1000.0, math.nan)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_08(self):
		"""Test cycle in array code  f - Invalid param inf for step.
		"""
		expected = self.PyCycle(self.data, 0.0, 1000.0, math.inf)

		arrayfunc.cycle(self.data, 0.0, 1000.0, math.inf)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_09(self):
		"""Test cycle in array code  f - Invalid param -inf for step.
		"""
		expected = self.PyCycle(self.data, 0.0, 1000.0, -math.inf)

		arrayfunc.cycle(self.data, 0.0, 1000.0, -math.inf)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	# This is not really a non-finite test, but it is convenient to put
	# it here as it is for floating point only.
	def test_cycle_nonfinite_10(self):
		"""Test cycle in array code  f - start from 0, count up by a small increment.
		"""
		expected = self.PyCycle(self.data, 0.0, 100.0, 0.1)

		arrayfunc.cycle(self.data, 0.0, 100.0, 0.1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class cycle_nonfinite_d(unittest.TestCase):
	"""Test for nonfinite cycle function.
	cycle_nonfinite_template
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

		self.TypeCode = 'd'

		self.data = array.array(self.TypeCode, itertools.repeat(0.0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.d_max
		self.MinVal = arrayfunc.arraylimits.d_min


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		val = start
		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val > stop:
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if not self.TypeCode in ('f', 'd'):
					if val > self.MaxVal:
						val = (val - (self.MaxVal + 1)) + self.MinVal
					if val < self.MinVal:
						val = (val - (self.MinVal - 1)) + self.MaxVal
				if val < stop:
					val = start
		return seq




	########################################################
	def test_cycle_nonfinite_01(self):
		"""Test cycle in array code  d - Invalid param nan for start.
		"""
		expected = self.PyCycle(self.data, math.nan, 1000.0, 1.0)

		arrayfunc.cycle(self.data, math.nan, 1000.0, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_02(self):
		"""Test cycle in array code  d - Invalid param inf for start.
		"""
		expected = self.PyCycle(self.data, math.inf, 1000.0, 1.0)

		arrayfunc.cycle(self.data, math.inf, 1000.0, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_03(self):
		"""Test cycle in array code  d - Invalid param -inf for start.
		"""
		expected = self.PyCycle(self.data, -math.inf, 1000.0, 1.0)

		arrayfunc.cycle(self.data, -math.inf, 1000.0, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_04(self):
		"""Test cycle in array code  d - Invalid param nan for stop.
		"""
		expected = self.PyCycle(self.data, 0.0, math.nan, 1.0)

		arrayfunc.cycle(self.data, 0.0, math.nan, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_05(self):
		"""Test cycle in array code  d - Invalid param inf for stop.
		"""
		expected = self.PyCycle(self.data, 0.0, math.inf, 1.0)

		arrayfunc.cycle(self.data, 0.0, math.inf, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_06(self):
		"""Test cycle in array code  d - Invalid param -inf for stop.
		"""
		expected = self.PyCycle(self.data, 0.0, -math.inf, 1.0)

		arrayfunc.cycle(self.data, 0.0, -math.inf, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_07(self):
		"""Test cycle in array code  d - Invalid param nan for step.
		"""
		expected = self.PyCycle(self.data, 0.0, 1000.0, math.nan)

		arrayfunc.cycle(self.data, 0.0, 1000.0, math.nan)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_08(self):
		"""Test cycle in array code  d - Invalid param inf for step.
		"""
		expected = self.PyCycle(self.data, 0.0, 1000.0, math.inf)

		arrayfunc.cycle(self.data, 0.0, 1000.0, math.inf)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_09(self):
		"""Test cycle in array code  d - Invalid param -inf for step.
		"""
		expected = self.PyCycle(self.data, 0.0, 1000.0, -math.inf)

		arrayfunc.cycle(self.data, 0.0, 1000.0, -math.inf)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	# This is not really a non-finite test, but it is convenient to put
	# it here as it is for floating point only.
	def test_cycle_nonfinite_10(self):
		"""Test cycle in array code  d - start from 0, count up by a small increment.
		"""
		expected = self.PyCycle(self.data, 0.0, 100.0, 0.1)

		arrayfunc.cycle(self.data, 0.0, 100.0, 0.1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class cycle_overflow_b(unittest.TestCase):
	"""Test for overflow cycle function.
	cycle_overflow_template
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
	def test_cycle_ovfl_01(self):
		"""Test cycle overflow operation in array code  b - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Overflow, 100, 1)


	########################################################
	def test_cycle_ovfl_02(self):
		"""Test cycle overflow operation in array code  b - Test for overflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100, self.Overflow, 1)


	########################################################
	def test_cycle_ovfl_03(self):
		"""Test cycle overflow operation in array code  b - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0, 100, self.StepOverflow)


	########################################################
	def test_cycle_ovfl_04(self):
		"""Test cycle overflow operation in array code  b - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Underflow, 100, 1)


	########################################################
	def test_cycle_ovfl_05(self):
		"""Test cycle overflow operation in array code  b - Test for underflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100, self.Underflow, 1)


	########################################################
	def test_cycle_ovfl_06(self):
		"""Test cycle overflow operation in array code  b - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0, 100, self.StepUnderflow)


##############################################################################


##############################################################################
class cycle_overflow_B(unittest.TestCase):
	"""Test for overflow cycle function.
	cycle_overflow_template
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
			self.StepOverflow = arrayfunc.arraylimits.B_max * 1.1
			self.StepUnderflow = arrayfunc.arraylimits.B_min * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1
			self.StepOverflow = arrayfunc.arraylimits.B_max + 1
			self.StepUnderflow = arrayfunc.arraylimits.B_min - 1


		self.data = array.array('B', [0] * self.ArrayLength)


	########################################################
	def test_cycle_ovfl_01(self):
		"""Test cycle overflow operation in array code  B - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Overflow, 100, 1)


	########################################################
	def test_cycle_ovfl_02(self):
		"""Test cycle overflow operation in array code  B - Test for overflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100, self.Overflow, 1)


	########################################################
	def test_cycle_ovfl_03(self):
		"""Test cycle overflow operation in array code  B - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0, 100, self.StepOverflow)


	########################################################
	def test_cycle_ovfl_04(self):
		"""Test cycle overflow operation in array code  B - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Underflow, 100, 1)


	########################################################
	def test_cycle_ovfl_05(self):
		"""Test cycle overflow operation in array code  B - Test for underflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100, self.Underflow, 1)


	########################################################
	def test_cycle_ovfl_06(self):
		"""Test cycle overflow operation in array code  B - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0, 100, self.StepUnderflow)


##############################################################################


##############################################################################
class cycle_overflow_h(unittest.TestCase):
	"""Test for overflow cycle function.
	cycle_overflow_template
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
	def test_cycle_ovfl_01(self):
		"""Test cycle overflow operation in array code  h - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Overflow, 100, 1)


	########################################################
	def test_cycle_ovfl_02(self):
		"""Test cycle overflow operation in array code  h - Test for overflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100, self.Overflow, 1)


	########################################################
	def test_cycle_ovfl_03(self):
		"""Test cycle overflow operation in array code  h - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0, 100, self.StepOverflow)


	########################################################
	def test_cycle_ovfl_04(self):
		"""Test cycle overflow operation in array code  h - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Underflow, 100, 1)


	########################################################
	def test_cycle_ovfl_05(self):
		"""Test cycle overflow operation in array code  h - Test for underflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100, self.Underflow, 1)


	########################################################
	def test_cycle_ovfl_06(self):
		"""Test cycle overflow operation in array code  h - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0, 100, self.StepUnderflow)


##############################################################################


##############################################################################
class cycle_overflow_H(unittest.TestCase):
	"""Test for overflow cycle function.
	cycle_overflow_template
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
			self.StepOverflow = arrayfunc.arraylimits.H_max * 1.1
			self.StepUnderflow = arrayfunc.arraylimits.H_min * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1
			self.StepOverflow = arrayfunc.arraylimits.H_max + 1
			self.StepUnderflow = arrayfunc.arraylimits.H_min - 1


		self.data = array.array('H', [0] * self.ArrayLength)


	########################################################
	def test_cycle_ovfl_01(self):
		"""Test cycle overflow operation in array code  H - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Overflow, 100, 1)


	########################################################
	def test_cycle_ovfl_02(self):
		"""Test cycle overflow operation in array code  H - Test for overflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100, self.Overflow, 1)


	########################################################
	def test_cycle_ovfl_03(self):
		"""Test cycle overflow operation in array code  H - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0, 100, self.StepOverflow)


	########################################################
	def test_cycle_ovfl_04(self):
		"""Test cycle overflow operation in array code  H - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Underflow, 100, 1)


	########################################################
	def test_cycle_ovfl_05(self):
		"""Test cycle overflow operation in array code  H - Test for underflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100, self.Underflow, 1)


	########################################################
	def test_cycle_ovfl_06(self):
		"""Test cycle overflow operation in array code  H - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0, 100, self.StepUnderflow)


##############################################################################


##############################################################################
class cycle_overflow_i(unittest.TestCase):
	"""Test for overflow cycle function.
	cycle_overflow_template
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
	def test_cycle_ovfl_01(self):
		"""Test cycle overflow operation in array code  i - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Overflow, 100, 1)


	########################################################
	def test_cycle_ovfl_02(self):
		"""Test cycle overflow operation in array code  i - Test for overflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100, self.Overflow, 1)


	########################################################
	def test_cycle_ovfl_03(self):
		"""Test cycle overflow operation in array code  i - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0, 100, self.StepOverflow)


	########################################################
	def test_cycle_ovfl_04(self):
		"""Test cycle overflow operation in array code  i - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Underflow, 100, 1)


	########################################################
	def test_cycle_ovfl_05(self):
		"""Test cycle overflow operation in array code  i - Test for underflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100, self.Underflow, 1)


	########################################################
	def test_cycle_ovfl_06(self):
		"""Test cycle overflow operation in array code  i - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0, 100, self.StepUnderflow)


##############################################################################


##############################################################################
class cycle_overflow_I(unittest.TestCase):
	"""Test for overflow cycle function.
	cycle_overflow_template
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
			self.StepOverflow = arrayfunc.arraylimits.I_max * 1.1
			self.StepUnderflow = arrayfunc.arraylimits.I_min * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1
			self.StepOverflow = arrayfunc.arraylimits.I_max + 1
			self.StepUnderflow = arrayfunc.arraylimits.I_min - 1


		self.data = array.array('I', [0] * self.ArrayLength)


	########################################################
	def test_cycle_ovfl_01(self):
		"""Test cycle overflow operation in array code  I - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Overflow, 100, 1)


	########################################################
	def test_cycle_ovfl_02(self):
		"""Test cycle overflow operation in array code  I - Test for overflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100, self.Overflow, 1)


	########################################################
	def test_cycle_ovfl_03(self):
		"""Test cycle overflow operation in array code  I - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0, 100, self.StepOverflow)


	########################################################
	def test_cycle_ovfl_04(self):
		"""Test cycle overflow operation in array code  I - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Underflow, 100, 1)


	########################################################
	def test_cycle_ovfl_05(self):
		"""Test cycle overflow operation in array code  I - Test for underflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100, self.Underflow, 1)


	########################################################
	def test_cycle_ovfl_06(self):
		"""Test cycle overflow operation in array code  I - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0, 100, self.StepUnderflow)


##############################################################################


##############################################################################
class cycle_overflow_l(unittest.TestCase):
	"""Test for overflow cycle function.
	cycle_overflow_template
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
	def test_cycle_ovfl_01(self):
		"""Test cycle overflow operation in array code  l - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Overflow, 100, 1)


	########################################################
	def test_cycle_ovfl_02(self):
		"""Test cycle overflow operation in array code  l - Test for overflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100, self.Overflow, 1)


	########################################################
	def test_cycle_ovfl_03(self):
		"""Test cycle overflow operation in array code  l - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0, 100, self.StepOverflow)


	########################################################
	def test_cycle_ovfl_04(self):
		"""Test cycle overflow operation in array code  l - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Underflow, 100, 1)


	########################################################
	def test_cycle_ovfl_05(self):
		"""Test cycle overflow operation in array code  l - Test for underflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100, self.Underflow, 1)


	########################################################
	def test_cycle_ovfl_06(self):
		"""Test cycle overflow operation in array code  l - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0, 100, self.StepUnderflow)


##############################################################################


##############################################################################
class cycle_overflow_q(unittest.TestCase):
	"""Test for overflow cycle function.
	cycle_overflow_template
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
	def test_cycle_ovfl_01(self):
		"""Test cycle overflow operation in array code  q - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Overflow, 100, 1)


	########################################################
	def test_cycle_ovfl_02(self):
		"""Test cycle overflow operation in array code  q - Test for overflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100, self.Overflow, 1)


	########################################################
	def test_cycle_ovfl_03(self):
		"""Test cycle overflow operation in array code  q - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0, 100, self.StepOverflow)


	########################################################
	def test_cycle_ovfl_04(self):
		"""Test cycle overflow operation in array code  q - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Underflow, 100, 1)


	########################################################
	def test_cycle_ovfl_05(self):
		"""Test cycle overflow operation in array code  q - Test for underflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100, self.Underflow, 1)


	########################################################
	def test_cycle_ovfl_06(self):
		"""Test cycle overflow operation in array code  q - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0, 100, self.StepUnderflow)


##############################################################################


##############################################################################
class cycle_overflow_f(unittest.TestCase):
	"""Test for overflow cycle function.
	cycle_overflow_template
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
	def test_cycle_ovfl_01(self):
		"""Test cycle overflow operation in array code  f - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Overflow, 100.0, 1.0)


	########################################################
	def test_cycle_ovfl_02(self):
		"""Test cycle overflow operation in array code  f - Test for overflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100.0, self.Overflow, 1.0)


	########################################################
	def test_cycle_ovfl_03(self):
		"""Test cycle overflow operation in array code  f - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0.0, 100.0, self.StepOverflow)


	########################################################
	def test_cycle_ovfl_04(self):
		"""Test cycle overflow operation in array code  f - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Underflow, 100.0, 1.0)


	########################################################
	def test_cycle_ovfl_05(self):
		"""Test cycle overflow operation in array code  f - Test for underflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100.0, self.Underflow, 1.0)


	########################################################
	def test_cycle_ovfl_06(self):
		"""Test cycle overflow operation in array code  f - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0.0, 100.0, self.StepUnderflow)


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
			f.write('cycle\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
