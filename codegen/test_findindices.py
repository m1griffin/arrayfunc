#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_findindices.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     21-Jun-2014.
# Ver:      24-Sep-2017.
#
###############################################################################
#
#   Copyright 2014 - 2017    Michael Griffin    <m12.griffin@gmail.com>
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
"""This conducts unit tests for findindices.
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
class findindices_operator_b(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'b'
		self.TestData = [int(x) for x in [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.TestData2 = [int(x) for x in [103, 102, 101, 100, 97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.constfill = int(100)

		self.data = array.array(self.TypeCode, self.TestData)
		self.data2 = array.array(self.TypeCode, self.TestData2)
		self.data3 = array.array(self.TypeCode, itertools.repeat(self.constfill, len(self.TestData)))

		# Output arrays must be of a specific type.
		self.OutputTypeCode = 'q'
		self.dataout = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data)))
		self.dataout2 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data2)))
		self.dataout3 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data3)))

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, [int(x) for x in range(97, 107)])
		self.dataoutovfl = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.b_min
		self.Maxval = arrayfunc.arraylimits.b_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataoutempty = array.array(self.OutputTypeCode)

		# This duplicates the error code for no matches found.
		self.ARR_ERR_NOTFOUND = -5


		# For bytes types, we need a non-array data type.
		if 'b' == 'bytes':
			self.data = bytes(self.data)
			self.data2 = bytes(self.data2)
			self.data3 = bytes(self.data3)
			self.dataovfl = bytes(self.dataovfl)
			self.dataempty = bytes(self.dataempty)



	########################################################
	def FindIndices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		indices = []

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				padding = [0] * (len(data) - len(indices))
				return indices + padding, len(indices)
			if opval(j):
				indices.append(i)

		# No match was found.
		if not indices:
			return [0] * len(data), self.ARR_ERR_NOTFOUND

		padding = [0] * (len(data) - len(indices))
		return indices + padding, len(indices)


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code b. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code b. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code b. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code b. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code b. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code b. - Parameter at start.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code b. - Parameter at end.
		"""
		param = int(102)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code b. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code b. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code b. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code b. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code b. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code b. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code b. - Parameter at start.
		"""
		param = int(104)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code b. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code b. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code b. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code b. - Parameter at start.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code b. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code b. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code b. - Parameter in middle.
		"""
		param = int(100)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 101, 100, 100, 100, 100]])
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code b. - Parameter at start.
		"""
		param = int(103)
		data = array.array(self.TypeCode, [int(x) for x in [101, 100, 100, 100, 100, 100, 100, 100, 100, 100]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code b. - Parameter at end.
		"""
		param = int(98)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 100, 100, 100, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code b. - Parameter not found.
		"""
		param = int(100)
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, self.data3, self.dataout3, param)
		expected, expectedlength = self.FindIndices('!=', self.data3, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout3), expected)



	########################################################
	def test_operator_lim_01(self):
		"""Test arraly limits  - Array code b.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=len(self.data)//2)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test arraly limits  - Array code b.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=-1)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=-1)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code b.
		"""
		param = int(101)
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param, 3, maxlen=2)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code b.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices(-1, self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('a', self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, 99, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, 99, int(100))


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code b.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code b.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_input_and_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code b.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float(100.5))



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code b.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code b.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code b.
		"""
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval)


##############################################################################

##############################################################################
class findindices_operator_B(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'B'
		self.TestData = [int(x) for x in [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.TestData2 = [int(x) for x in [103, 102, 101, 100, 97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.constfill = int(100)

		self.data = array.array(self.TypeCode, self.TestData)
		self.data2 = array.array(self.TypeCode, self.TestData2)
		self.data3 = array.array(self.TypeCode, itertools.repeat(self.constfill, len(self.TestData)))

		# Output arrays must be of a specific type.
		self.OutputTypeCode = 'q'
		self.dataout = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data)))
		self.dataout2 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data2)))
		self.dataout3 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data3)))

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, [int(x) for x in range(97, 107)])
		self.dataoutovfl = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.B_min
		self.Maxval = arrayfunc.arraylimits.B_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataoutempty = array.array(self.OutputTypeCode)

		# This duplicates the error code for no matches found.
		self.ARR_ERR_NOTFOUND = -5


		# For bytes types, we need a non-array data type.
		if 'B' == 'bytes':
			self.data = bytes(self.data)
			self.data2 = bytes(self.data2)
			self.data3 = bytes(self.data3)
			self.dataovfl = bytes(self.dataovfl)
			self.dataempty = bytes(self.dataempty)



	########################################################
	def FindIndices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		indices = []

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				padding = [0] * (len(data) - len(indices))
				return indices + padding, len(indices)
			if opval(j):
				indices.append(i)

		# No match was found.
		if not indices:
			return [0] * len(data), self.ARR_ERR_NOTFOUND

		padding = [0] * (len(data) - len(indices))
		return indices + padding, len(indices)


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code B. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code B. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code B. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code B. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code B. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code B. - Parameter at start.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code B. - Parameter at end.
		"""
		param = int(102)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code B. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code B. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code B. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code B. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code B. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code B. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code B. - Parameter at start.
		"""
		param = int(104)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code B. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code B. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code B. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code B. - Parameter at start.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code B. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code B. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code B. - Parameter in middle.
		"""
		param = int(100)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 101, 100, 100, 100, 100]])
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code B. - Parameter at start.
		"""
		param = int(103)
		data = array.array(self.TypeCode, [int(x) for x in [101, 100, 100, 100, 100, 100, 100, 100, 100, 100]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code B. - Parameter at end.
		"""
		param = int(98)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 100, 100, 100, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code B. - Parameter not found.
		"""
		param = int(100)
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, self.data3, self.dataout3, param)
		expected, expectedlength = self.FindIndices('!=', self.data3, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout3), expected)



	########################################################
	def test_operator_lim_01(self):
		"""Test arraly limits  - Array code B.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=len(self.data)//2)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test arraly limits  - Array code B.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=-1)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=-1)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code B.
		"""
		param = int(101)
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param, 3, maxlen=2)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code B.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices(-1, self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('a', self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, 99, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, 99, int(100))


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code B.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code B.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_input_and_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code B.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float(100.5))



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code B.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code B.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code B.
		"""
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval)


##############################################################################

##############################################################################
class findindices_operator_h(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'h'
		self.TestData = [int(x) for x in [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.TestData2 = [int(x) for x in [103, 102, 101, 100, 97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.constfill = int(100)

		self.data = array.array(self.TypeCode, self.TestData)
		self.data2 = array.array(self.TypeCode, self.TestData2)
		self.data3 = array.array(self.TypeCode, itertools.repeat(self.constfill, len(self.TestData)))

		# Output arrays must be of a specific type.
		self.OutputTypeCode = 'q'
		self.dataout = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data)))
		self.dataout2 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data2)))
		self.dataout3 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data3)))

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, [int(x) for x in range(97, 107)])
		self.dataoutovfl = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.h_min
		self.Maxval = arrayfunc.arraylimits.h_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataoutempty = array.array(self.OutputTypeCode)

		# This duplicates the error code for no matches found.
		self.ARR_ERR_NOTFOUND = -5


		# For bytes types, we need a non-array data type.
		if 'h' == 'bytes':
			self.data = bytes(self.data)
			self.data2 = bytes(self.data2)
			self.data3 = bytes(self.data3)
			self.dataovfl = bytes(self.dataovfl)
			self.dataempty = bytes(self.dataempty)



	########################################################
	def FindIndices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		indices = []

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				padding = [0] * (len(data) - len(indices))
				return indices + padding, len(indices)
			if opval(j):
				indices.append(i)

		# No match was found.
		if not indices:
			return [0] * len(data), self.ARR_ERR_NOTFOUND

		padding = [0] * (len(data) - len(indices))
		return indices + padding, len(indices)


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code h. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code h. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code h. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code h. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code h. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code h. - Parameter at start.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code h. - Parameter at end.
		"""
		param = int(102)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code h. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code h. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code h. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code h. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code h. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code h. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code h. - Parameter at start.
		"""
		param = int(104)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code h. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code h. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code h. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code h. - Parameter at start.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code h. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code h. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code h. - Parameter in middle.
		"""
		param = int(100)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 101, 100, 100, 100, 100]])
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code h. - Parameter at start.
		"""
		param = int(103)
		data = array.array(self.TypeCode, [int(x) for x in [101, 100, 100, 100, 100, 100, 100, 100, 100, 100]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code h. - Parameter at end.
		"""
		param = int(98)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 100, 100, 100, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code h. - Parameter not found.
		"""
		param = int(100)
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, self.data3, self.dataout3, param)
		expected, expectedlength = self.FindIndices('!=', self.data3, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout3), expected)



	########################################################
	def test_operator_lim_01(self):
		"""Test arraly limits  - Array code h.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=len(self.data)//2)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test arraly limits  - Array code h.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=-1)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=-1)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code h.
		"""
		param = int(101)
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param, 3, maxlen=2)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code h.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices(-1, self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('a', self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, 99, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, 99, int(100))


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code h.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code h.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_input_and_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code h.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float(100.5))



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code h.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code h.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code h.
		"""
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval)


##############################################################################

##############################################################################
class findindices_operator_H(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'H'
		self.TestData = [int(x) for x in [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.TestData2 = [int(x) for x in [103, 102, 101, 100, 97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.constfill = int(100)

		self.data = array.array(self.TypeCode, self.TestData)
		self.data2 = array.array(self.TypeCode, self.TestData2)
		self.data3 = array.array(self.TypeCode, itertools.repeat(self.constfill, len(self.TestData)))

		# Output arrays must be of a specific type.
		self.OutputTypeCode = 'q'
		self.dataout = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data)))
		self.dataout2 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data2)))
		self.dataout3 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data3)))

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, [int(x) for x in range(97, 107)])
		self.dataoutovfl = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.H_min
		self.Maxval = arrayfunc.arraylimits.H_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataoutempty = array.array(self.OutputTypeCode)

		# This duplicates the error code for no matches found.
		self.ARR_ERR_NOTFOUND = -5


		# For bytes types, we need a non-array data type.
		if 'H' == 'bytes':
			self.data = bytes(self.data)
			self.data2 = bytes(self.data2)
			self.data3 = bytes(self.data3)
			self.dataovfl = bytes(self.dataovfl)
			self.dataempty = bytes(self.dataempty)



	########################################################
	def FindIndices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		indices = []

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				padding = [0] * (len(data) - len(indices))
				return indices + padding, len(indices)
			if opval(j):
				indices.append(i)

		# No match was found.
		if not indices:
			return [0] * len(data), self.ARR_ERR_NOTFOUND

		padding = [0] * (len(data) - len(indices))
		return indices + padding, len(indices)


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code H. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code H. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code H. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code H. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code H. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code H. - Parameter at start.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code H. - Parameter at end.
		"""
		param = int(102)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code H. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code H. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code H. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code H. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code H. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code H. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code H. - Parameter at start.
		"""
		param = int(104)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code H. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code H. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code H. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code H. - Parameter at start.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code H. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code H. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code H. - Parameter in middle.
		"""
		param = int(100)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 101, 100, 100, 100, 100]])
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code H. - Parameter at start.
		"""
		param = int(103)
		data = array.array(self.TypeCode, [int(x) for x in [101, 100, 100, 100, 100, 100, 100, 100, 100, 100]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code H. - Parameter at end.
		"""
		param = int(98)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 100, 100, 100, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code H. - Parameter not found.
		"""
		param = int(100)
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, self.data3, self.dataout3, param)
		expected, expectedlength = self.FindIndices('!=', self.data3, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout3), expected)



	########################################################
	def test_operator_lim_01(self):
		"""Test arraly limits  - Array code H.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=len(self.data)//2)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test arraly limits  - Array code H.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=-1)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=-1)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code H.
		"""
		param = int(101)
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param, 3, maxlen=2)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code H.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices(-1, self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('a', self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, 99, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, 99, int(100))


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code H.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code H.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_input_and_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code H.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float(100.5))



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code H.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code H.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code H.
		"""
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval)


##############################################################################

##############################################################################
class findindices_operator_i(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'i'
		self.TestData = [int(x) for x in [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.TestData2 = [int(x) for x in [103, 102, 101, 100, 97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.constfill = int(100)

		self.data = array.array(self.TypeCode, self.TestData)
		self.data2 = array.array(self.TypeCode, self.TestData2)
		self.data3 = array.array(self.TypeCode, itertools.repeat(self.constfill, len(self.TestData)))

		# Output arrays must be of a specific type.
		self.OutputTypeCode = 'q'
		self.dataout = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data)))
		self.dataout2 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data2)))
		self.dataout3 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data3)))

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, [int(x) for x in range(97, 107)])
		self.dataoutovfl = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.i_min
		self.Maxval = arrayfunc.arraylimits.i_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataoutempty = array.array(self.OutputTypeCode)

		# This duplicates the error code for no matches found.
		self.ARR_ERR_NOTFOUND = -5


		# For bytes types, we need a non-array data type.
		if 'i' == 'bytes':
			self.data = bytes(self.data)
			self.data2 = bytes(self.data2)
			self.data3 = bytes(self.data3)
			self.dataovfl = bytes(self.dataovfl)
			self.dataempty = bytes(self.dataempty)



	########################################################
	def FindIndices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		indices = []

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				padding = [0] * (len(data) - len(indices))
				return indices + padding, len(indices)
			if opval(j):
				indices.append(i)

		# No match was found.
		if not indices:
			return [0] * len(data), self.ARR_ERR_NOTFOUND

		padding = [0] * (len(data) - len(indices))
		return indices + padding, len(indices)


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code i. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code i. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code i. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code i. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code i. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code i. - Parameter at start.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code i. - Parameter at end.
		"""
		param = int(102)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code i. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code i. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code i. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code i. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code i. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code i. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code i. - Parameter at start.
		"""
		param = int(104)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code i. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code i. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code i. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code i. - Parameter at start.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code i. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code i. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code i. - Parameter in middle.
		"""
		param = int(100)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 101, 100, 100, 100, 100]])
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code i. - Parameter at start.
		"""
		param = int(103)
		data = array.array(self.TypeCode, [int(x) for x in [101, 100, 100, 100, 100, 100, 100, 100, 100, 100]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code i. - Parameter at end.
		"""
		param = int(98)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 100, 100, 100, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code i. - Parameter not found.
		"""
		param = int(100)
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, self.data3, self.dataout3, param)
		expected, expectedlength = self.FindIndices('!=', self.data3, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout3), expected)



	########################################################
	def test_operator_lim_01(self):
		"""Test arraly limits  - Array code i.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=len(self.data)//2)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test arraly limits  - Array code i.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=-1)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=-1)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code i.
		"""
		param = int(101)
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param, 3, maxlen=2)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code i.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices(-1, self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('a', self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, 99, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, 99, int(100))


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code i.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code i.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_input_and_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code i.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float(100.5))



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code i.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code i.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code i.
		"""
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval)


##############################################################################

##############################################################################
class findindices_operator_I(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'I'
		self.TestData = [int(x) for x in [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.TestData2 = [int(x) for x in [103, 102, 101, 100, 97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.constfill = int(100)

		self.data = array.array(self.TypeCode, self.TestData)
		self.data2 = array.array(self.TypeCode, self.TestData2)
		self.data3 = array.array(self.TypeCode, itertools.repeat(self.constfill, len(self.TestData)))

		# Output arrays must be of a specific type.
		self.OutputTypeCode = 'q'
		self.dataout = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data)))
		self.dataout2 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data2)))
		self.dataout3 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data3)))

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, [int(x) for x in range(97, 107)])
		self.dataoutovfl = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.I_min
		self.Maxval = arrayfunc.arraylimits.I_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataoutempty = array.array(self.OutputTypeCode)

		# This duplicates the error code for no matches found.
		self.ARR_ERR_NOTFOUND = -5


		# For bytes types, we need a non-array data type.
		if 'I' == 'bytes':
			self.data = bytes(self.data)
			self.data2 = bytes(self.data2)
			self.data3 = bytes(self.data3)
			self.dataovfl = bytes(self.dataovfl)
			self.dataempty = bytes(self.dataempty)



	########################################################
	def FindIndices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		indices = []

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				padding = [0] * (len(data) - len(indices))
				return indices + padding, len(indices)
			if opval(j):
				indices.append(i)

		# No match was found.
		if not indices:
			return [0] * len(data), self.ARR_ERR_NOTFOUND

		padding = [0] * (len(data) - len(indices))
		return indices + padding, len(indices)


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code I. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code I. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code I. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code I. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code I. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code I. - Parameter at start.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code I. - Parameter at end.
		"""
		param = int(102)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code I. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code I. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code I. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code I. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code I. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code I. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code I. - Parameter at start.
		"""
		param = int(104)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code I. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code I. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code I. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code I. - Parameter at start.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code I. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code I. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code I. - Parameter in middle.
		"""
		param = int(100)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 101, 100, 100, 100, 100]])
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code I. - Parameter at start.
		"""
		param = int(103)
		data = array.array(self.TypeCode, [int(x) for x in [101, 100, 100, 100, 100, 100, 100, 100, 100, 100]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code I. - Parameter at end.
		"""
		param = int(98)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 100, 100, 100, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code I. - Parameter not found.
		"""
		param = int(100)
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, self.data3, self.dataout3, param)
		expected, expectedlength = self.FindIndices('!=', self.data3, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout3), expected)



	########################################################
	def test_operator_lim_01(self):
		"""Test arraly limits  - Array code I.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=len(self.data)//2)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test arraly limits  - Array code I.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=-1)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=-1)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code I.
		"""
		param = int(101)
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param, 3, maxlen=2)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code I.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices(-1, self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('a', self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, 99, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, 99, int(100))


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code I.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code I.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_input_and_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code I.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float(100.5))



	########################################################
	# Whether this test can be peformed depends on the integer word sizes in for this architecture.
	@unittest.skipIf(arrayfunc.arraylimits.I_max == arrayfunc.arraylimits.L_max, 
		'Skip test if I integer does not have overflow checks.')
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code I.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal - 1)


	########################################################
	# Whether this test can be peformed depends on the integer word sizes in for this architecture.
	@unittest.skipIf(arrayfunc.arraylimits.I_max == arrayfunc.arraylimits.L_max, 
		'Skip test if I integer does not have overflow checks.')
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code I.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code I.
		"""
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval)


##############################################################################

##############################################################################
class findindices_operator_l(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'l'
		self.TestData = [int(x) for x in [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.TestData2 = [int(x) for x in [103, 102, 101, 100, 97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.constfill = int(100)

		self.data = array.array(self.TypeCode, self.TestData)
		self.data2 = array.array(self.TypeCode, self.TestData2)
		self.data3 = array.array(self.TypeCode, itertools.repeat(self.constfill, len(self.TestData)))

		# Output arrays must be of a specific type.
		self.OutputTypeCode = 'q'
		self.dataout = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data)))
		self.dataout2 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data2)))
		self.dataout3 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data3)))

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, [int(x) for x in range(97, 107)])
		self.dataoutovfl = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.l_min
		self.Maxval = arrayfunc.arraylimits.l_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataoutempty = array.array(self.OutputTypeCode)

		# This duplicates the error code for no matches found.
		self.ARR_ERR_NOTFOUND = -5


		# For bytes types, we need a non-array data type.
		if 'l' == 'bytes':
			self.data = bytes(self.data)
			self.data2 = bytes(self.data2)
			self.data3 = bytes(self.data3)
			self.dataovfl = bytes(self.dataovfl)
			self.dataempty = bytes(self.dataempty)



	########################################################
	def FindIndices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		indices = []

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				padding = [0] * (len(data) - len(indices))
				return indices + padding, len(indices)
			if opval(j):
				indices.append(i)

		# No match was found.
		if not indices:
			return [0] * len(data), self.ARR_ERR_NOTFOUND

		padding = [0] * (len(data) - len(indices))
		return indices + padding, len(indices)


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code l. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code l. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code l. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code l. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code l. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code l. - Parameter at start.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code l. - Parameter at end.
		"""
		param = int(102)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code l. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code l. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code l. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code l. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code l. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code l. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code l. - Parameter at start.
		"""
		param = int(104)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code l. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code l. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code l. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code l. - Parameter at start.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code l. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code l. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code l. - Parameter in middle.
		"""
		param = int(100)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 101, 100, 100, 100, 100]])
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code l. - Parameter at start.
		"""
		param = int(103)
		data = array.array(self.TypeCode, [int(x) for x in [101, 100, 100, 100, 100, 100, 100, 100, 100, 100]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code l. - Parameter at end.
		"""
		param = int(98)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 100, 100, 100, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code l. - Parameter not found.
		"""
		param = int(100)
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, self.data3, self.dataout3, param)
		expected, expectedlength = self.FindIndices('!=', self.data3, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout3), expected)



	########################################################
	def test_operator_lim_01(self):
		"""Test arraly limits  - Array code l.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=len(self.data)//2)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test arraly limits  - Array code l.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=-1)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=-1)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code l.
		"""
		param = int(101)
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param, 3, maxlen=2)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code l.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices(-1, self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('a', self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, 99, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, 99, int(100))


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code l.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code l.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_input_and_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code l.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float(100.5))



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code l.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code l.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code l.
		"""
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval)


##############################################################################

##############################################################################
class findindices_operator_L(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'L'
		self.TestData = [int(x) for x in [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.TestData2 = [int(x) for x in [103, 102, 101, 100, 97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.constfill = int(100)

		self.data = array.array(self.TypeCode, self.TestData)
		self.data2 = array.array(self.TypeCode, self.TestData2)
		self.data3 = array.array(self.TypeCode, itertools.repeat(self.constfill, len(self.TestData)))

		# Output arrays must be of a specific type.
		self.OutputTypeCode = 'q'
		self.dataout = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data)))
		self.dataout2 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data2)))
		self.dataout3 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data3)))

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, [int(x) for x in range(97, 107)])
		self.dataoutovfl = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.L_min
		self.Maxval = arrayfunc.arraylimits.L_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataoutempty = array.array(self.OutputTypeCode)

		# This duplicates the error code for no matches found.
		self.ARR_ERR_NOTFOUND = -5


		# For bytes types, we need a non-array data type.
		if 'L' == 'bytes':
			self.data = bytes(self.data)
			self.data2 = bytes(self.data2)
			self.data3 = bytes(self.data3)
			self.dataovfl = bytes(self.dataovfl)
			self.dataempty = bytes(self.dataempty)



	########################################################
	def FindIndices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		indices = []

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				padding = [0] * (len(data) - len(indices))
				return indices + padding, len(indices)
			if opval(j):
				indices.append(i)

		# No match was found.
		if not indices:
			return [0] * len(data), self.ARR_ERR_NOTFOUND

		padding = [0] * (len(data) - len(indices))
		return indices + padding, len(indices)


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code L. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code L. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code L. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code L. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code L. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code L. - Parameter at start.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code L. - Parameter at end.
		"""
		param = int(102)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code L. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code L. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code L. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code L. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code L. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code L. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code L. - Parameter at start.
		"""
		param = int(104)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code L. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code L. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code L. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code L. - Parameter at start.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code L. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code L. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code L. - Parameter in middle.
		"""
		param = int(100)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 101, 100, 100, 100, 100]])
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code L. - Parameter at start.
		"""
		param = int(103)
		data = array.array(self.TypeCode, [int(x) for x in [101, 100, 100, 100, 100, 100, 100, 100, 100, 100]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code L. - Parameter at end.
		"""
		param = int(98)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 100, 100, 100, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code L. - Parameter not found.
		"""
		param = int(100)
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, self.data3, self.dataout3, param)
		expected, expectedlength = self.FindIndices('!=', self.data3, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout3), expected)



	########################################################
	def test_operator_lim_01(self):
		"""Test arraly limits  - Array code L.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=len(self.data)//2)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test arraly limits  - Array code L.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=-1)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=-1)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code L.
		"""
		param = int(101)
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param, 3, maxlen=2)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code L.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices(-1, self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('a', self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, 99, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, 99, int(100))


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code L.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code L.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_input_and_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code L.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float(100.5))



##############################################################################

##############################################################################
class findindices_operator_q(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'q'
		self.TestData = [int(x) for x in [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.TestData2 = [int(x) for x in [103, 102, 101, 100, 97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.constfill = int(100)

		self.data = array.array(self.TypeCode, self.TestData)
		self.data2 = array.array(self.TypeCode, self.TestData2)
		self.data3 = array.array(self.TypeCode, itertools.repeat(self.constfill, len(self.TestData)))

		# Output arrays must be of a specific type.
		self.OutputTypeCode = 'q'
		self.dataout = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data)))
		self.dataout2 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data2)))
		self.dataout3 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data3)))

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, [int(x) for x in range(97, 107)])
		self.dataoutovfl = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.q_min
		self.Maxval = arrayfunc.arraylimits.q_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataoutempty = array.array(self.OutputTypeCode)

		# This duplicates the error code for no matches found.
		self.ARR_ERR_NOTFOUND = -5


		# For bytes types, we need a non-array data type.
		if 'q' == 'bytes':
			self.data = bytes(self.data)
			self.data2 = bytes(self.data2)
			self.data3 = bytes(self.data3)
			self.dataovfl = bytes(self.dataovfl)
			self.dataempty = bytes(self.dataempty)



	########################################################
	def FindIndices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		indices = []

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				padding = [0] * (len(data) - len(indices))
				return indices + padding, len(indices)
			if opval(j):
				indices.append(i)

		# No match was found.
		if not indices:
			return [0] * len(data), self.ARR_ERR_NOTFOUND

		padding = [0] * (len(data) - len(indices))
		return indices + padding, len(indices)


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code q. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code q. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code q. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code q. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code q. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code q. - Parameter at start.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code q. - Parameter at end.
		"""
		param = int(102)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code q. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code q. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code q. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code q. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code q. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code q. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code q. - Parameter at start.
		"""
		param = int(104)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code q. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code q. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code q. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code q. - Parameter at start.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code q. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code q. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code q. - Parameter in middle.
		"""
		param = int(100)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 101, 100, 100, 100, 100]])
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code q. - Parameter at start.
		"""
		param = int(103)
		data = array.array(self.TypeCode, [int(x) for x in [101, 100, 100, 100, 100, 100, 100, 100, 100, 100]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code q. - Parameter at end.
		"""
		param = int(98)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 100, 100, 100, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code q. - Parameter not found.
		"""
		param = int(100)
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, self.data3, self.dataout3, param)
		expected, expectedlength = self.FindIndices('!=', self.data3, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout3), expected)



	########################################################
	def test_operator_lim_01(self):
		"""Test arraly limits  - Array code q.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=len(self.data)//2)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test arraly limits  - Array code q.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=-1)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=-1)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code q.
		"""
		param = int(101)
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param, 3, maxlen=2)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code q.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices(-1, self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('a', self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, 99, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, 99, int(100))


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code q.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code q.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_input_and_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code q.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float(100.5))



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code q.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code q.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code q.
		"""
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval)


##############################################################################

##############################################################################
class findindices_operator_Q(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'Q'
		self.TestData = [int(x) for x in [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.TestData2 = [int(x) for x in [103, 102, 101, 100, 97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.constfill = int(100)

		self.data = array.array(self.TypeCode, self.TestData)
		self.data2 = array.array(self.TypeCode, self.TestData2)
		self.data3 = array.array(self.TypeCode, itertools.repeat(self.constfill, len(self.TestData)))

		# Output arrays must be of a specific type.
		self.OutputTypeCode = 'q'
		self.dataout = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data)))
		self.dataout2 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data2)))
		self.dataout3 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data3)))

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, [int(x) for x in range(97, 107)])
		self.dataoutovfl = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.Q_min
		self.Maxval = arrayfunc.arraylimits.Q_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataoutempty = array.array(self.OutputTypeCode)

		# This duplicates the error code for no matches found.
		self.ARR_ERR_NOTFOUND = -5


		# For bytes types, we need a non-array data type.
		if 'Q' == 'bytes':
			self.data = bytes(self.data)
			self.data2 = bytes(self.data2)
			self.data3 = bytes(self.data3)
			self.dataovfl = bytes(self.dataovfl)
			self.dataempty = bytes(self.dataempty)



	########################################################
	def FindIndices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		indices = []

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				padding = [0] * (len(data) - len(indices))
				return indices + padding, len(indices)
			if opval(j):
				indices.append(i)

		# No match was found.
		if not indices:
			return [0] * len(data), self.ARR_ERR_NOTFOUND

		padding = [0] * (len(data) - len(indices))
		return indices + padding, len(indices)


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code Q. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code Q. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code Q. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code Q. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code Q. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code Q. - Parameter at start.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code Q. - Parameter at end.
		"""
		param = int(102)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code Q. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code Q. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code Q. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code Q. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code Q. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code Q. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code Q. - Parameter at start.
		"""
		param = int(104)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code Q. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code Q. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code Q. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code Q. - Parameter at start.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code Q. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code Q. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code Q. - Parameter in middle.
		"""
		param = int(100)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 101, 100, 100, 100, 100]])
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code Q. - Parameter at start.
		"""
		param = int(103)
		data = array.array(self.TypeCode, [int(x) for x in [101, 100, 100, 100, 100, 100, 100, 100, 100, 100]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code Q. - Parameter at end.
		"""
		param = int(98)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 100, 100, 100, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code Q. - Parameter not found.
		"""
		param = int(100)
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, self.data3, self.dataout3, param)
		expected, expectedlength = self.FindIndices('!=', self.data3, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout3), expected)



	########################################################
	def test_operator_lim_01(self):
		"""Test arraly limits  - Array code Q.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=len(self.data)//2)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test arraly limits  - Array code Q.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=-1)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=-1)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code Q.
		"""
		param = int(101)
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param, 3, maxlen=2)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code Q.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices(-1, self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('a', self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, 99, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, 99, int(100))


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code Q.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code Q.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_input_and_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code Q.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float(100.5))



##############################################################################

##############################################################################
class findindices_operator_f(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'f'
		self.TestData = [float(x) for x in [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.TestData2 = [float(x) for x in [103, 102, 101, 100, 97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.constfill = float(100)

		self.data = array.array(self.TypeCode, self.TestData)
		self.data2 = array.array(self.TypeCode, self.TestData2)
		self.data3 = array.array(self.TypeCode, itertools.repeat(self.constfill, len(self.TestData)))

		# Output arrays must be of a specific type.
		self.OutputTypeCode = 'q'
		self.dataout = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data)))
		self.dataout2 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data2)))
		self.dataout3 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data3)))

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, [int(x) for x in range(97, 107)])
		self.dataoutovfl = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.f_min
		self.Maxval = arrayfunc.arraylimits.f_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataoutempty = array.array(self.OutputTypeCode)

		# This duplicates the error code for no matches found.
		self.ARR_ERR_NOTFOUND = -5


		# For bytes types, we need a non-array data type.
		if 'f' == 'bytes':
			self.data = bytes(self.data)
			self.data2 = bytes(self.data2)
			self.data3 = bytes(self.data3)
			self.dataovfl = bytes(self.dataovfl)
			self.dataempty = bytes(self.dataempty)



	########################################################
	def FindIndices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		indices = []

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				padding = [0] * (len(data) - len(indices))
				return indices + padding, len(indices)
			if opval(j):
				indices.append(i)

		# No match was found.
		if not indices:
			return [0] * len(data), self.ARR_ERR_NOTFOUND

		padding = [0] * (len(data) - len(indices))
		return indices + padding, len(indices)


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code f. - Parameter in middle.
		"""
		param = float(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code f. - Parameter at start.
		"""
		param = float(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code f. - Parameter at end.
		"""
		param = float(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code f. - Parameter not found.
		"""
		param = float(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code f. - Parameter in middle.
		"""
		param = float(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code f. - Parameter at start.
		"""
		param = float(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code f. - Parameter at end.
		"""
		param = float(102)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code f. - Parameter not found.
		"""
		param = float(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code f. - Parameter in middle.
		"""
		param = float(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code f. - Parameter at start.
		"""
		param = float(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code f. - Parameter at end.
		"""
		param = float(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code f. - Parameter not found.
		"""
		param = float(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code f. - Parameter in middle.
		"""
		param = float(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code f. - Parameter at start.
		"""
		param = float(104)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code f. - Parameter at end.
		"""
		param = float(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code f. - Parameter not found.
		"""
		param = float(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code f. - Parameter in middle.
		"""
		param = float(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code f. - Parameter at start.
		"""
		param = float(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code f. - Parameter at end.
		"""
		param = float(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code f. - Parameter not found.
		"""
		param = float(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code f. - Parameter in middle.
		"""
		param = float(100)
		data = array.array(self.TypeCode, [float(x) for x in [100, 100, 100, 100, 100, 101, 100, 100, 100, 100]])
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code f. - Parameter at start.
		"""
		param = float(103)
		data = array.array(self.TypeCode, [float(x) for x in [101, 100, 100, 100, 100, 100, 100, 100, 100, 100]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code f. - Parameter at end.
		"""
		param = float(98)
		data = array.array(self.TypeCode, [float(x) for x in [100, 100, 100, 100, 100, 100, 100, 100, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code f. - Parameter not found.
		"""
		param = float(100)
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, self.data3, self.dataout3, param)
		expected, expectedlength = self.FindIndices('!=', self.data3, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout3), expected)



	########################################################
	def test_operator_lim_01(self):
		"""Test arraly limits  - Array code f.
		"""
		param = float(101)
		data = array.array(self.TypeCode, [float(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=len(self.data)//2)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test arraly limits  - Array code f.
		"""
		param = float(101)
		data = array.array(self.TypeCode, [float(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=-1)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=-1)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code f.
		"""
		param = float(101)
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param, 3, maxlen=2)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float(100), xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float(100), maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code f.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices(-1, self.data, self.dataout, float(100))


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('a', self.data, self.dataout, float(100))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, 99, self.dataout, float(100))


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, 99, float(100))


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code f.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataout, float(100))


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code f.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataoutempty, float(100))


	########################################################
	def test_param_invalid_input_and_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code f.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataoutempty, float(100))


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100.5))



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal * 1.1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval * 1.1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code f.
		"""
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval)


##############################################################################

##############################################################################
class findindices_operator_d(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'd'
		self.TestData = [float(x) for x in [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.TestData2 = [float(x) for x in [103, 102, 101, 100, 97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.constfill = float(100)

		self.data = array.array(self.TypeCode, self.TestData)
		self.data2 = array.array(self.TypeCode, self.TestData2)
		self.data3 = array.array(self.TypeCode, itertools.repeat(self.constfill, len(self.TestData)))

		# Output arrays must be of a specific type.
		self.OutputTypeCode = 'q'
		self.dataout = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data)))
		self.dataout2 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data2)))
		self.dataout3 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data3)))

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, [int(x) for x in range(97, 107)])
		self.dataoutovfl = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.d_min
		self.Maxval = arrayfunc.arraylimits.d_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataoutempty = array.array(self.OutputTypeCode)

		# This duplicates the error code for no matches found.
		self.ARR_ERR_NOTFOUND = -5


		# For bytes types, we need a non-array data type.
		if 'd' == 'bytes':
			self.data = bytes(self.data)
			self.data2 = bytes(self.data2)
			self.data3 = bytes(self.data3)
			self.dataovfl = bytes(self.dataovfl)
			self.dataempty = bytes(self.dataempty)



	########################################################
	def FindIndices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		indices = []

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				padding = [0] * (len(data) - len(indices))
				return indices + padding, len(indices)
			if opval(j):
				indices.append(i)

		# No match was found.
		if not indices:
			return [0] * len(data), self.ARR_ERR_NOTFOUND

		padding = [0] * (len(data) - len(indices))
		return indices + padding, len(indices)


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code d. - Parameter in middle.
		"""
		param = float(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code d. - Parameter at start.
		"""
		param = float(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code d. - Parameter at end.
		"""
		param = float(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code d. - Parameter not found.
		"""
		param = float(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code d. - Parameter in middle.
		"""
		param = float(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code d. - Parameter at start.
		"""
		param = float(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code d. - Parameter at end.
		"""
		param = float(102)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code d. - Parameter not found.
		"""
		param = float(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code d. - Parameter in middle.
		"""
		param = float(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code d. - Parameter at start.
		"""
		param = float(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code d. - Parameter at end.
		"""
		param = float(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code d. - Parameter not found.
		"""
		param = float(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code d. - Parameter in middle.
		"""
		param = float(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code d. - Parameter at start.
		"""
		param = float(104)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code d. - Parameter at end.
		"""
		param = float(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code d. - Parameter not found.
		"""
		param = float(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code d. - Parameter in middle.
		"""
		param = float(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code d. - Parameter at start.
		"""
		param = float(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code d. - Parameter at end.
		"""
		param = float(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code d. - Parameter not found.
		"""
		param = float(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code d. - Parameter in middle.
		"""
		param = float(100)
		data = array.array(self.TypeCode, [float(x) for x in [100, 100, 100, 100, 100, 101, 100, 100, 100, 100]])
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code d. - Parameter at start.
		"""
		param = float(103)
		data = array.array(self.TypeCode, [float(x) for x in [101, 100, 100, 100, 100, 100, 100, 100, 100, 100]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code d. - Parameter at end.
		"""
		param = float(98)
		data = array.array(self.TypeCode, [float(x) for x in [100, 100, 100, 100, 100, 100, 100, 100, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code d. - Parameter not found.
		"""
		param = float(100)
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, self.data3, self.dataout3, param)
		expected, expectedlength = self.FindIndices('!=', self.data3, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout3), expected)



	########################################################
	def test_operator_lim_01(self):
		"""Test arraly limits  - Array code d.
		"""
		param = float(101)
		data = array.array(self.TypeCode, [float(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=len(self.data)//2)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test arraly limits  - Array code d.
		"""
		param = float(101)
		data = array.array(self.TypeCode, [float(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=-1)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=-1)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code d.
		"""
		param = float(101)
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param, 3, maxlen=2)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float(100), xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float(100), maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code d.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices(-1, self.data, self.dataout, float(100))


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('a', self.data, self.dataout, float(100))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, 99, self.dataout, float(100))


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, 99, float(100))


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code d.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataout, float(100))


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code d.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataoutempty, float(100))


	########################################################
	def test_param_invalid_input_and_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code d.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataoutempty, float(100))


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100.5))



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal * 1.1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval * 1.1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code d.
		"""
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval)


##############################################################################

##############################################################################
class findindices_operator_bytes(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'B'
		self.TestData = [int(x) for x in [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.TestData2 = [int(x) for x in [103, 102, 101, 100, 97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.constfill = int(100)

		self.data = array.array(self.TypeCode, self.TestData)
		self.data2 = array.array(self.TypeCode, self.TestData2)
		self.data3 = array.array(self.TypeCode, itertools.repeat(self.constfill, len(self.TestData)))

		# Output arrays must be of a specific type.
		self.OutputTypeCode = 'q'
		self.dataout = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data)))
		self.dataout2 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data2)))
		self.dataout3 = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.data3)))

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, [int(x) for x in range(97, 107)])
		self.dataoutovfl = array.array(self.OutputTypeCode, itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.B_min
		self.Maxval = arrayfunc.arraylimits.B_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataoutempty = array.array(self.OutputTypeCode)

		# This duplicates the error code for no matches found.
		self.ARR_ERR_NOTFOUND = -5


		# For bytes types, we need a non-array data type.
		if 'bytes' == 'bytes':
			self.data = bytes(self.data)
			self.data2 = bytes(self.data2)
			self.data3 = bytes(self.data3)
			self.dataovfl = bytes(self.dataovfl)
			self.dataempty = bytes(self.dataempty)



	########################################################
	def FindIndices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]
		opval = lambda x: opfunc(x, param)

		indices = []

		for i,j in enumerate(data):
			if (maxlen > 0) and (i >= maxlen):
				padding = [0] * (len(data) - len(indices))
				return indices + padding, len(indices)
			if opval(j):
				indices.append(i)

		# No match was found.
		if not indices:
			return [0] * len(data), self.ARR_ERR_NOTFOUND

		padding = [0] * (len(data) - len(indices))
		return indices + padding, len(indices)


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code bytes. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code bytes. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code bytes. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code bytes. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code bytes. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code bytes. - Parameter at start.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code bytes. - Parameter at end.
		"""
		param = int(102)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code bytes. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code bytes. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code bytes. - Parameter at start.
		"""
		param = int(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code bytes. - Parameter at end.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code bytes. - Parameter not found.
		"""
		param = int(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code bytes. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code bytes. - Parameter at start.
		"""
		param = int(104)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code bytes. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code bytes. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code bytes. - Parameter in middle.
		"""
		param = int(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code bytes. - Parameter at start.
		"""
		param = int(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code bytes. - Parameter at end.
		"""
		param = int(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code bytes. - Parameter not found.
		"""
		param = int(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code bytes. - Parameter in middle.
		"""
		param = int(100)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 101, 100, 100, 100, 100]])
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code bytes. - Parameter at start.
		"""
		param = int(103)
		data = array.array(self.TypeCode, [int(x) for x in [101, 100, 100, 100, 100, 100, 100, 100, 100, 100]])
		data = bytes(data)
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code bytes. - Parameter at end.
		"""
		param = int(98)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 100, 100, 100, 100, 100, 100, 101]])
		data = bytes(data)
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code bytes. - Parameter not found.
		"""
		param = int(100)
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, self.data3, self.dataout3, param)
		expected, expectedlength = self.FindIndices('!=', self.data3, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout3), expected)



	########################################################
	def test_operator_lim_01(self):
		"""Test arraly limits  - Array code bytes.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		data = bytes(data)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=len(self.data)//2)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test arraly limits  - Array code bytes.
		"""
		param = int(101)
		data = array.array(self.TypeCode, [int(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		data = bytes(data)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=-1)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=-1)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code bytes.
		"""
		param = int(101)
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param, 3, maxlen=2)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, int(100), maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code bytes.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices(-1, self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('a', self.data, self.dataout, int(100))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, 99, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, 99, int(100))


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code bytes.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataout, int(100))


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code bytes.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_input_and_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code bytes.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataoutempty, int(100))


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code bytes.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float(100.5))



	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code bytes.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code bytes.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code bytes.
		"""
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval)


##############################################################################
class findindices_nan_f(unittest.TestCase):
	"""Test for nan, inf, -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('f', [100.0] * 10)
		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


	########################################################
	def test_nan_01(self):
		"""Test for param of nan  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float('nan'))


	########################################################
	def test_nan_02(self):
		"""Test for param of inf  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float('inf'))


	########################################################
	def test_nan_03(self):
		"""Test for param of -inf  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float('-inf'))


	########################################################
	def test_nan_04(self):
		"""Test for lim of nan  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 100.0, maxlen=float('nan'))


	########################################################
	def test_nan_05(self):
		"""Test for lim of inf  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 100.0, maxlen=float('inf'))


	########################################################
	def test_nan_06(self):
		"""Test for lim of -inf  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 100.0, maxlen=float('-inf'))


##############################################################################

##############################################################################
class findindices_nan_d(unittest.TestCase):
	"""Test for nan, inf, -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('d', [100.0] * 10)
		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


	########################################################
	def test_nan_01(self):
		"""Test for param of nan  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float('nan'))


	########################################################
	def test_nan_02(self):
		"""Test for param of inf  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float('inf'))


	########################################################
	def test_nan_03(self):
		"""Test for param of -inf  - Array code d.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float('-inf'))


	########################################################
	def test_nan_04(self):
		"""Test for lim of nan  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 100.0, maxlen=float('nan'))


	########################################################
	def test_nan_05(self):
		"""Test for lim of inf  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 100.0, maxlen=float('inf'))


	########################################################
	def test_nan_06(self):
		"""Test for lim of -inf  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 100.0, maxlen=float('-inf'))


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
			f.write('

')
			f.write('findindices

')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################