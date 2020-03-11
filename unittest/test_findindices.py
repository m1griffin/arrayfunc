#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_findindices.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     21-Jun-2014.
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
"""This conducts unit tests for findindices.
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
class findindices_operator_b(unittest.TestCase):
	"""Test for basic operator function.
	op_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'b'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 95, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)
		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		self.ARR_ERR_NOTFOUND = -1

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}


	########################################################
	def Findindices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# If the maxlen parameter is used, trim the source data accordingly.
		if maxlen > 0:
			testdata = data[:maxlen]
		else:
			testdata = data

		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]

		# Peform the operation.
		result = [x for x,y in enumerate(testdata) if opfunc(y, param)]
		copiedlength = len(result)
		
		# Pad out with the same fill used for the output array, and return
		# the number of items copied.
		trimmed = result + list(itertools.repeat(self.zerofill, len(data) - len(result)))

		return trimmed, copiedlength


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code b.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code b.
		"""
		param = 96
		result = arrayfunc.findindices('>', self.data, self.dataout, param)
		expected, explength = self.Findindices('>', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code b.
		"""
		param = 96
		result = arrayfunc.findindices('>=', self.data, self.dataout, param)
		expected, explength = self.Findindices('>=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code b.
		"""
		param = 98
		result = arrayfunc.findindices('<', self.data, self.dataout, param)
		expected, explength = self.Findindices('<', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code b.
		"""
		param = 98
		result = arrayfunc.findindices('<=', self.data, self.dataout, param)
		expected, explength = self.Findindices('<=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code b.
		"""
		param = 98
		result = arrayfunc.findindices('!=', self.data, self.dataout, param)
		expected, explength = self.Findindices('!=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)
		

	########################################################
	def test_operator_maxlen_01(self):
		"""Test array maxlen  - Array code b.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=len(self.data)//2)
		expected, explength = self.Findindices('==', self.data, param, maxlen=len(self.data)//2)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_maxlen_02(self):
		"""Test array maxlen  - Array code b.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=-1)
		expected, explength = self.Findindices('==', self.data, param, maxlen=-1)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class findindices_params_b(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'b'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)

		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataemptyout = array.array('q')


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code b.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, param, 3, maxlen=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [1, 2, 3, 4], 3)



	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code b.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices('!', self.data, self.dataout, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(62, self.data, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = list(filter('a', [0, 1, 2, 3, 4]))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter value  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', 99, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code b.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.dataempty, self.dataout, 100)


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty output array parameter type  - Array code b.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.data, self.dataemptyout, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 'e')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code b.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_outputarray_type_01(self):
		"""Test exception with invalid output array type  - Array code b.
		"""
		# The list of array types should have all supported types other than 'q'.
		for testval in ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'Q', 'f', 'd'):
			with self.subTest(msg='Failed with parameter', testval = testval):
		
				badarray = array.array(testval, itertools.repeat(0, len(self.data)))

				with self.assertRaises(TypeError):
					result = arrayfunc.findindices('==', self.data, badarray)


##############################################################################


##############################################################################
class findindices_paramovfl_b(unittest.TestCase):
	"""Test for testing parameter overflow.
	overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'b'
		self.zerofill = 0

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, range(97, 107))
		self.dataoutovfl = array.array('q', itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.b_min
		self.Maxval = arrayfunc.arraylimits.b_max


	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code b.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code b.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code b.
		"""
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval)



##############################################################################

 

##############################################################################
class findindices_operator_B(unittest.TestCase):
	"""Test for basic operator function.
	op_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'B'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 95, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)
		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		self.ARR_ERR_NOTFOUND = -1

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}


	########################################################
	def Findindices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# If the maxlen parameter is used, trim the source data accordingly.
		if maxlen > 0:
			testdata = data[:maxlen]
		else:
			testdata = data

		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]

		# Peform the operation.
		result = [x for x,y in enumerate(testdata) if opfunc(y, param)]
		copiedlength = len(result)
		
		# Pad out with the same fill used for the output array, and return
		# the number of items copied.
		trimmed = result + list(itertools.repeat(self.zerofill, len(data) - len(result)))

		return trimmed, copiedlength


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code B.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code B.
		"""
		param = 96
		result = arrayfunc.findindices('>', self.data, self.dataout, param)
		expected, explength = self.Findindices('>', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code B.
		"""
		param = 96
		result = arrayfunc.findindices('>=', self.data, self.dataout, param)
		expected, explength = self.Findindices('>=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code B.
		"""
		param = 98
		result = arrayfunc.findindices('<', self.data, self.dataout, param)
		expected, explength = self.Findindices('<', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code B.
		"""
		param = 98
		result = arrayfunc.findindices('<=', self.data, self.dataout, param)
		expected, explength = self.Findindices('<=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code B.
		"""
		param = 98
		result = arrayfunc.findindices('!=', self.data, self.dataout, param)
		expected, explength = self.Findindices('!=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)
		

	########################################################
	def test_operator_maxlen_01(self):
		"""Test array maxlen  - Array code B.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=len(self.data)//2)
		expected, explength = self.Findindices('==', self.data, param, maxlen=len(self.data)//2)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_maxlen_02(self):
		"""Test array maxlen  - Array code B.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=-1)
		expected, explength = self.Findindices('==', self.data, param, maxlen=-1)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class findindices_params_B(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'B'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)

		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataemptyout = array.array('q')


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code B.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, param, 3, maxlen=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [1, 2, 3, 4], 3)



	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code B.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices('!', self.data, self.dataout, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(62, self.data, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = list(filter('a', [0, 1, 2, 3, 4]))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter value  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', 99, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code B.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.dataempty, self.dataout, 100)


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty output array parameter type  - Array code B.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.data, self.dataemptyout, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 'e')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code B.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_outputarray_type_01(self):
		"""Test exception with invalid output array type  - Array code B.
		"""
		# The list of array types should have all supported types other than 'q'.
		for testval in ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'Q', 'f', 'd'):
			with self.subTest(msg='Failed with parameter', testval = testval):
		
				badarray = array.array(testval, itertools.repeat(0, len(self.data)))

				with self.assertRaises(TypeError):
					result = arrayfunc.findindices('==', self.data, badarray)


##############################################################################


##############################################################################
class findindices_paramovfl_B(unittest.TestCase):
	"""Test for testing parameter overflow.
	overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'B'
		self.zerofill = 0

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, range(97, 107))
		self.dataoutovfl = array.array('q', itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.B_min
		self.Maxval = arrayfunc.arraylimits.B_max


	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code B.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code B.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code B.
		"""
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval)



##############################################################################

 

##############################################################################
class findindices_operator_h(unittest.TestCase):
	"""Test for basic operator function.
	op_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'h'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 95, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)
		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		self.ARR_ERR_NOTFOUND = -1

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}


	########################################################
	def Findindices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# If the maxlen parameter is used, trim the source data accordingly.
		if maxlen > 0:
			testdata = data[:maxlen]
		else:
			testdata = data

		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]

		# Peform the operation.
		result = [x for x,y in enumerate(testdata) if opfunc(y, param)]
		copiedlength = len(result)
		
		# Pad out with the same fill used for the output array, and return
		# the number of items copied.
		trimmed = result + list(itertools.repeat(self.zerofill, len(data) - len(result)))

		return trimmed, copiedlength


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code h.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code h.
		"""
		param = 96
		result = arrayfunc.findindices('>', self.data, self.dataout, param)
		expected, explength = self.Findindices('>', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code h.
		"""
		param = 96
		result = arrayfunc.findindices('>=', self.data, self.dataout, param)
		expected, explength = self.Findindices('>=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code h.
		"""
		param = 98
		result = arrayfunc.findindices('<', self.data, self.dataout, param)
		expected, explength = self.Findindices('<', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code h.
		"""
		param = 98
		result = arrayfunc.findindices('<=', self.data, self.dataout, param)
		expected, explength = self.Findindices('<=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code h.
		"""
		param = 98
		result = arrayfunc.findindices('!=', self.data, self.dataout, param)
		expected, explength = self.Findindices('!=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)
		

	########################################################
	def test_operator_maxlen_01(self):
		"""Test array maxlen  - Array code h.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=len(self.data)//2)
		expected, explength = self.Findindices('==', self.data, param, maxlen=len(self.data)//2)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_maxlen_02(self):
		"""Test array maxlen  - Array code h.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=-1)
		expected, explength = self.Findindices('==', self.data, param, maxlen=-1)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class findindices_params_h(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'h'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)

		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataemptyout = array.array('q')


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code h.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, param, 3, maxlen=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [1, 2, 3, 4], 3)



	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code h.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices('!', self.data, self.dataout, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(62, self.data, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = list(filter('a', [0, 1, 2, 3, 4]))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter value  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', 99, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code h.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.dataempty, self.dataout, 100)


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty output array parameter type  - Array code h.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.data, self.dataemptyout, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 'e')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code h.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_outputarray_type_01(self):
		"""Test exception with invalid output array type  - Array code h.
		"""
		# The list of array types should have all supported types other than 'q'.
		for testval in ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'Q', 'f', 'd'):
			with self.subTest(msg='Failed with parameter', testval = testval):
		
				badarray = array.array(testval, itertools.repeat(0, len(self.data)))

				with self.assertRaises(TypeError):
					result = arrayfunc.findindices('==', self.data, badarray)


##############################################################################


##############################################################################
class findindices_paramovfl_h(unittest.TestCase):
	"""Test for testing parameter overflow.
	overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'h'
		self.zerofill = 0

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, range(97, 107))
		self.dataoutovfl = array.array('q', itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.h_min
		self.Maxval = arrayfunc.arraylimits.h_max


	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code h.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code h.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code h.
		"""
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval)



##############################################################################

 

##############################################################################
class findindices_operator_H(unittest.TestCase):
	"""Test for basic operator function.
	op_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'H'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 95, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)
		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		self.ARR_ERR_NOTFOUND = -1

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}


	########################################################
	def Findindices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# If the maxlen parameter is used, trim the source data accordingly.
		if maxlen > 0:
			testdata = data[:maxlen]
		else:
			testdata = data

		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]

		# Peform the operation.
		result = [x for x,y in enumerate(testdata) if opfunc(y, param)]
		copiedlength = len(result)
		
		# Pad out with the same fill used for the output array, and return
		# the number of items copied.
		trimmed = result + list(itertools.repeat(self.zerofill, len(data) - len(result)))

		return trimmed, copiedlength


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code H.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code H.
		"""
		param = 96
		result = arrayfunc.findindices('>', self.data, self.dataout, param)
		expected, explength = self.Findindices('>', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code H.
		"""
		param = 96
		result = arrayfunc.findindices('>=', self.data, self.dataout, param)
		expected, explength = self.Findindices('>=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code H.
		"""
		param = 98
		result = arrayfunc.findindices('<', self.data, self.dataout, param)
		expected, explength = self.Findindices('<', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code H.
		"""
		param = 98
		result = arrayfunc.findindices('<=', self.data, self.dataout, param)
		expected, explength = self.Findindices('<=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code H.
		"""
		param = 98
		result = arrayfunc.findindices('!=', self.data, self.dataout, param)
		expected, explength = self.Findindices('!=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)
		

	########################################################
	def test_operator_maxlen_01(self):
		"""Test array maxlen  - Array code H.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=len(self.data)//2)
		expected, explength = self.Findindices('==', self.data, param, maxlen=len(self.data)//2)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_maxlen_02(self):
		"""Test array maxlen  - Array code H.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=-1)
		expected, explength = self.Findindices('==', self.data, param, maxlen=-1)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class findindices_params_H(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'H'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)

		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataemptyout = array.array('q')


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code H.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, param, 3, maxlen=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [1, 2, 3, 4], 3)



	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code H.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices('!', self.data, self.dataout, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(62, self.data, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = list(filter('a', [0, 1, 2, 3, 4]))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter value  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', 99, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code H.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.dataempty, self.dataout, 100)


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty output array parameter type  - Array code H.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.data, self.dataemptyout, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 'e')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code H.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_outputarray_type_01(self):
		"""Test exception with invalid output array type  - Array code H.
		"""
		# The list of array types should have all supported types other than 'q'.
		for testval in ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'Q', 'f', 'd'):
			with self.subTest(msg='Failed with parameter', testval = testval):
		
				badarray = array.array(testval, itertools.repeat(0, len(self.data)))

				with self.assertRaises(TypeError):
					result = arrayfunc.findindices('==', self.data, badarray)


##############################################################################


##############################################################################
class findindices_paramovfl_H(unittest.TestCase):
	"""Test for testing parameter overflow.
	overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'H'
		self.zerofill = 0

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, range(97, 107))
		self.dataoutovfl = array.array('q', itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.H_min
		self.Maxval = arrayfunc.arraylimits.H_max


	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code H.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code H.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code H.
		"""
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval)



##############################################################################

 

##############################################################################
class findindices_operator_i(unittest.TestCase):
	"""Test for basic operator function.
	op_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'i'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 95, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)
		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		self.ARR_ERR_NOTFOUND = -1

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}


	########################################################
	def Findindices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# If the maxlen parameter is used, trim the source data accordingly.
		if maxlen > 0:
			testdata = data[:maxlen]
		else:
			testdata = data

		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]

		# Peform the operation.
		result = [x for x,y in enumerate(testdata) if opfunc(y, param)]
		copiedlength = len(result)
		
		# Pad out with the same fill used for the output array, and return
		# the number of items copied.
		trimmed = result + list(itertools.repeat(self.zerofill, len(data) - len(result)))

		return trimmed, copiedlength


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code i.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code i.
		"""
		param = 96
		result = arrayfunc.findindices('>', self.data, self.dataout, param)
		expected, explength = self.Findindices('>', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code i.
		"""
		param = 96
		result = arrayfunc.findindices('>=', self.data, self.dataout, param)
		expected, explength = self.Findindices('>=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code i.
		"""
		param = 98
		result = arrayfunc.findindices('<', self.data, self.dataout, param)
		expected, explength = self.Findindices('<', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code i.
		"""
		param = 98
		result = arrayfunc.findindices('<=', self.data, self.dataout, param)
		expected, explength = self.Findindices('<=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code i.
		"""
		param = 98
		result = arrayfunc.findindices('!=', self.data, self.dataout, param)
		expected, explength = self.Findindices('!=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)
		

	########################################################
	def test_operator_maxlen_01(self):
		"""Test array maxlen  - Array code i.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=len(self.data)//2)
		expected, explength = self.Findindices('==', self.data, param, maxlen=len(self.data)//2)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_maxlen_02(self):
		"""Test array maxlen  - Array code i.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=-1)
		expected, explength = self.Findindices('==', self.data, param, maxlen=-1)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class findindices_params_i(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'i'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)

		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataemptyout = array.array('q')


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code i.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, param, 3, maxlen=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [1, 2, 3, 4], 3)



	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code i.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices('!', self.data, self.dataout, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(62, self.data, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = list(filter('a', [0, 1, 2, 3, 4]))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter value  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', 99, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code i.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.dataempty, self.dataout, 100)


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty output array parameter type  - Array code i.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.data, self.dataemptyout, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 'e')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code i.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_outputarray_type_01(self):
		"""Test exception with invalid output array type  - Array code i.
		"""
		# The list of array types should have all supported types other than 'q'.
		for testval in ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'Q', 'f', 'd'):
			with self.subTest(msg='Failed with parameter', testval = testval):
		
				badarray = array.array(testval, itertools.repeat(0, len(self.data)))

				with self.assertRaises(TypeError):
					result = arrayfunc.findindices('==', self.data, badarray)


##############################################################################


##############################################################################
class findindices_paramovfl_i(unittest.TestCase):
	"""Test for testing parameter overflow.
	overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'i'
		self.zerofill = 0

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, range(97, 107))
		self.dataoutovfl = array.array('q', itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.i_min
		self.Maxval = arrayfunc.arraylimits.i_max


	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code i.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code i.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code i.
		"""
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval)



##############################################################################

 

##############################################################################
class findindices_operator_I(unittest.TestCase):
	"""Test for basic operator function.
	op_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'I'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 95, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)
		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		self.ARR_ERR_NOTFOUND = -1

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}


	########################################################
	def Findindices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# If the maxlen parameter is used, trim the source data accordingly.
		if maxlen > 0:
			testdata = data[:maxlen]
		else:
			testdata = data

		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]

		# Peform the operation.
		result = [x for x,y in enumerate(testdata) if opfunc(y, param)]
		copiedlength = len(result)
		
		# Pad out with the same fill used for the output array, and return
		# the number of items copied.
		trimmed = result + list(itertools.repeat(self.zerofill, len(data) - len(result)))

		return trimmed, copiedlength


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code I.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code I.
		"""
		param = 96
		result = arrayfunc.findindices('>', self.data, self.dataout, param)
		expected, explength = self.Findindices('>', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code I.
		"""
		param = 96
		result = arrayfunc.findindices('>=', self.data, self.dataout, param)
		expected, explength = self.Findindices('>=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code I.
		"""
		param = 98
		result = arrayfunc.findindices('<', self.data, self.dataout, param)
		expected, explength = self.Findindices('<', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code I.
		"""
		param = 98
		result = arrayfunc.findindices('<=', self.data, self.dataout, param)
		expected, explength = self.Findindices('<=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code I.
		"""
		param = 98
		result = arrayfunc.findindices('!=', self.data, self.dataout, param)
		expected, explength = self.Findindices('!=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)
		

	########################################################
	def test_operator_maxlen_01(self):
		"""Test array maxlen  - Array code I.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=len(self.data)//2)
		expected, explength = self.Findindices('==', self.data, param, maxlen=len(self.data)//2)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_maxlen_02(self):
		"""Test array maxlen  - Array code I.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=-1)
		expected, explength = self.Findindices('==', self.data, param, maxlen=-1)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class findindices_params_I(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'I'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)

		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataemptyout = array.array('q')


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code I.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, param, 3, maxlen=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [1, 2, 3, 4], 3)



	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code I.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices('!', self.data, self.dataout, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(62, self.data, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = list(filter('a', [0, 1, 2, 3, 4]))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter value  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', 99, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code I.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.dataempty, self.dataout, 100)


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty output array parameter type  - Array code I.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.data, self.dataemptyout, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 'e')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code I.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_outputarray_type_01(self):
		"""Test exception with invalid output array type  - Array code I.
		"""
		# The list of array types should have all supported types other than 'q'.
		for testval in ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'Q', 'f', 'd'):
			with self.subTest(msg='Failed with parameter', testval = testval):
		
				badarray = array.array(testval, itertools.repeat(0, len(self.data)))

				with self.assertRaises(TypeError):
					result = arrayfunc.findindices('==', self.data, badarray)


##############################################################################


##############################################################################
class findindices_paramovfl_I(unittest.TestCase):
	"""Test for testing parameter overflow.
	overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'I'
		self.zerofill = 0

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, range(97, 107))
		self.dataoutovfl = array.array('q', itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.I_min
		self.Maxval = arrayfunc.arraylimits.I_max


	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code I.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code I.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code I.
		"""
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval)



##############################################################################

 

##############################################################################
class findindices_operator_l(unittest.TestCase):
	"""Test for basic operator function.
	op_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'l'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 95, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)
		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		self.ARR_ERR_NOTFOUND = -1

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}


	########################################################
	def Findindices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# If the maxlen parameter is used, trim the source data accordingly.
		if maxlen > 0:
			testdata = data[:maxlen]
		else:
			testdata = data

		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]

		# Peform the operation.
		result = [x for x,y in enumerate(testdata) if opfunc(y, param)]
		copiedlength = len(result)
		
		# Pad out with the same fill used for the output array, and return
		# the number of items copied.
		trimmed = result + list(itertools.repeat(self.zerofill, len(data) - len(result)))

		return trimmed, copiedlength


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code l.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code l.
		"""
		param = 96
		result = arrayfunc.findindices('>', self.data, self.dataout, param)
		expected, explength = self.Findindices('>', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code l.
		"""
		param = 96
		result = arrayfunc.findindices('>=', self.data, self.dataout, param)
		expected, explength = self.Findindices('>=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code l.
		"""
		param = 98
		result = arrayfunc.findindices('<', self.data, self.dataout, param)
		expected, explength = self.Findindices('<', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code l.
		"""
		param = 98
		result = arrayfunc.findindices('<=', self.data, self.dataout, param)
		expected, explength = self.Findindices('<=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code l.
		"""
		param = 98
		result = arrayfunc.findindices('!=', self.data, self.dataout, param)
		expected, explength = self.Findindices('!=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)
		

	########################################################
	def test_operator_maxlen_01(self):
		"""Test array maxlen  - Array code l.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=len(self.data)//2)
		expected, explength = self.Findindices('==', self.data, param, maxlen=len(self.data)//2)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_maxlen_02(self):
		"""Test array maxlen  - Array code l.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=-1)
		expected, explength = self.Findindices('==', self.data, param, maxlen=-1)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class findindices_params_l(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'l'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)

		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataemptyout = array.array('q')


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code l.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, param, 3, maxlen=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [1, 2, 3, 4], 3)



	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code l.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices('!', self.data, self.dataout, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(62, self.data, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = list(filter('a', [0, 1, 2, 3, 4]))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter value  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', 99, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code l.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.dataempty, self.dataout, 100)


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty output array parameter type  - Array code l.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.data, self.dataemptyout, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 'e')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code l.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_outputarray_type_01(self):
		"""Test exception with invalid output array type  - Array code l.
		"""
		# The list of array types should have all supported types other than 'q'.
		for testval in ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'Q', 'f', 'd'):
			with self.subTest(msg='Failed with parameter', testval = testval):
		
				badarray = array.array(testval, itertools.repeat(0, len(self.data)))

				with self.assertRaises(TypeError):
					result = arrayfunc.findindices('==', self.data, badarray)


##############################################################################


##############################################################################
class findindices_paramovfl_l(unittest.TestCase):
	"""Test for testing parameter overflow.
	overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'l'
		self.zerofill = 0

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, range(97, 107))
		self.dataoutovfl = array.array('q', itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.l_min
		self.Maxval = arrayfunc.arraylimits.l_max


	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code l.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code l.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code l.
		"""
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval)



##############################################################################

 

##############################################################################
class findindices_operator_L(unittest.TestCase):
	"""Test for basic operator function.
	op_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'L'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 95, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)
		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		self.ARR_ERR_NOTFOUND = -1

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}


	########################################################
	def Findindices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# If the maxlen parameter is used, trim the source data accordingly.
		if maxlen > 0:
			testdata = data[:maxlen]
		else:
			testdata = data

		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]

		# Peform the operation.
		result = [x for x,y in enumerate(testdata) if opfunc(y, param)]
		copiedlength = len(result)
		
		# Pad out with the same fill used for the output array, and return
		# the number of items copied.
		trimmed = result + list(itertools.repeat(self.zerofill, len(data) - len(result)))

		return trimmed, copiedlength


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code L.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code L.
		"""
		param = 96
		result = arrayfunc.findindices('>', self.data, self.dataout, param)
		expected, explength = self.Findindices('>', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code L.
		"""
		param = 96
		result = arrayfunc.findindices('>=', self.data, self.dataout, param)
		expected, explength = self.Findindices('>=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code L.
		"""
		param = 98
		result = arrayfunc.findindices('<', self.data, self.dataout, param)
		expected, explength = self.Findindices('<', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code L.
		"""
		param = 98
		result = arrayfunc.findindices('<=', self.data, self.dataout, param)
		expected, explength = self.Findindices('<=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code L.
		"""
		param = 98
		result = arrayfunc.findindices('!=', self.data, self.dataout, param)
		expected, explength = self.Findindices('!=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)
		

	########################################################
	def test_operator_maxlen_01(self):
		"""Test array maxlen  - Array code L.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=len(self.data)//2)
		expected, explength = self.Findindices('==', self.data, param, maxlen=len(self.data)//2)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_maxlen_02(self):
		"""Test array maxlen  - Array code L.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=-1)
		expected, explength = self.Findindices('==', self.data, param, maxlen=-1)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class findindices_params_L(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'L'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)

		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataemptyout = array.array('q')


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code L.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, param, 3, maxlen=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [1, 2, 3, 4], 3)



	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code L.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices('!', self.data, self.dataout, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(62, self.data, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = list(filter('a', [0, 1, 2, 3, 4]))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter value  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', 99, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code L.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.dataempty, self.dataout, 100)


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty output array parameter type  - Array code L.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.data, self.dataemptyout, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 'e')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code L.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_outputarray_type_01(self):
		"""Test exception with invalid output array type  - Array code L.
		"""
		# The list of array types should have all supported types other than 'q'.
		for testval in ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'Q', 'f', 'd'):
			with self.subTest(msg='Failed with parameter', testval = testval):
		
				badarray = array.array(testval, itertools.repeat(0, len(self.data)))

				with self.assertRaises(TypeError):
					result = arrayfunc.findindices('==', self.data, badarray)


##############################################################################

 

##############################################################################
class findindices_operator_q(unittest.TestCase):
	"""Test for basic operator function.
	op_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'q'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 95, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)
		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		self.ARR_ERR_NOTFOUND = -1

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}


	########################################################
	def Findindices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# If the maxlen parameter is used, trim the source data accordingly.
		if maxlen > 0:
			testdata = data[:maxlen]
		else:
			testdata = data

		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]

		# Peform the operation.
		result = [x for x,y in enumerate(testdata) if opfunc(y, param)]
		copiedlength = len(result)
		
		# Pad out with the same fill used for the output array, and return
		# the number of items copied.
		trimmed = result + list(itertools.repeat(self.zerofill, len(data) - len(result)))

		return trimmed, copiedlength


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code q.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code q.
		"""
		param = 96
		result = arrayfunc.findindices('>', self.data, self.dataout, param)
		expected, explength = self.Findindices('>', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code q.
		"""
		param = 96
		result = arrayfunc.findindices('>=', self.data, self.dataout, param)
		expected, explength = self.Findindices('>=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code q.
		"""
		param = 98
		result = arrayfunc.findindices('<', self.data, self.dataout, param)
		expected, explength = self.Findindices('<', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code q.
		"""
		param = 98
		result = arrayfunc.findindices('<=', self.data, self.dataout, param)
		expected, explength = self.Findindices('<=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code q.
		"""
		param = 98
		result = arrayfunc.findindices('!=', self.data, self.dataout, param)
		expected, explength = self.Findindices('!=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)
		

	########################################################
	def test_operator_maxlen_01(self):
		"""Test array maxlen  - Array code q.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=len(self.data)//2)
		expected, explength = self.Findindices('==', self.data, param, maxlen=len(self.data)//2)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_maxlen_02(self):
		"""Test array maxlen  - Array code q.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=-1)
		expected, explength = self.Findindices('==', self.data, param, maxlen=-1)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class findindices_params_q(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'q'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)

		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataemptyout = array.array('q')


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code q.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, param, 3, maxlen=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [1, 2, 3, 4], 3)



	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code q.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices('!', self.data, self.dataout, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(62, self.data, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = list(filter('a', [0, 1, 2, 3, 4]))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter value  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', 99, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code q.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.dataempty, self.dataout, 100)


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty output array parameter type  - Array code q.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.data, self.dataemptyout, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 'e')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_outputarray_type_01(self):
		"""Test exception with invalid output array type  - Array code q.
		"""
		# The list of array types should have all supported types other than 'q'.
		for testval in ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'Q', 'f', 'd'):
			with self.subTest(msg='Failed with parameter', testval = testval):
		
				badarray = array.array(testval, itertools.repeat(0, len(self.data)))

				with self.assertRaises(TypeError):
					result = arrayfunc.findindices('==', self.data, badarray)


##############################################################################


##############################################################################
class findindices_paramovfl_q(unittest.TestCase):
	"""Test for testing parameter overflow.
	overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'q'
		self.zerofill = 0

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, range(97, 107))
		self.dataoutovfl = array.array('q', itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.q_min
		self.Maxval = arrayfunc.arraylimits.q_max


	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code q.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal - 1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code q.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval + 1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code q.
		"""
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval)



##############################################################################

 

##############################################################################
class findindices_operator_Q(unittest.TestCase):
	"""Test for basic operator function.
	op_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'Q'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 95, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)
		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		self.ARR_ERR_NOTFOUND = -1

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}


	########################################################
	def Findindices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# If the maxlen parameter is used, trim the source data accordingly.
		if maxlen > 0:
			testdata = data[:maxlen]
		else:
			testdata = data

		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]

		# Peform the operation.
		result = [x for x,y in enumerate(testdata) if opfunc(y, param)]
		copiedlength = len(result)
		
		# Pad out with the same fill used for the output array, and return
		# the number of items copied.
		trimmed = result + list(itertools.repeat(self.zerofill, len(data) - len(result)))

		return trimmed, copiedlength


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code Q.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code Q.
		"""
		param = 96
		result = arrayfunc.findindices('>', self.data, self.dataout, param)
		expected, explength = self.Findindices('>', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code Q.
		"""
		param = 96
		result = arrayfunc.findindices('>=', self.data, self.dataout, param)
		expected, explength = self.Findindices('>=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code Q.
		"""
		param = 98
		result = arrayfunc.findindices('<', self.data, self.dataout, param)
		expected, explength = self.Findindices('<', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code Q.
		"""
		param = 98
		result = arrayfunc.findindices('<=', self.data, self.dataout, param)
		expected, explength = self.Findindices('<=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code Q.
		"""
		param = 98
		result = arrayfunc.findindices('!=', self.data, self.dataout, param)
		expected, explength = self.Findindices('!=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)
		

	########################################################
	def test_operator_maxlen_01(self):
		"""Test array maxlen  - Array code Q.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=len(self.data)//2)
		expected, explength = self.Findindices('==', self.data, param, maxlen=len(self.data)//2)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_maxlen_02(self):
		"""Test array maxlen  - Array code Q.
		"""
		param = 97
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=-1)
		expected, explength = self.Findindices('==', self.data, param, maxlen=-1)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class findindices_params_Q(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'Q'
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]
		self.zerofill = 0

		self.data = array.array(self.TypeCode, self.TestData)

		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataemptyout = array.array('q')


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code Q.
		"""
		param = 101
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, param, 3, maxlen=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [1, 2, 3, 4], 3)



	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code Q.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices('!', self.data, self.dataout, 100)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(62, self.data, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = list(filter('a', [0, 1, 2, 3, 4]))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter value  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', 99, self.dataout, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, 99, 100)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code Q.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.dataempty, self.dataout, 100)


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty output array parameter type  - Array code Q.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.data, self.dataemptyout, 100)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 'e')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code Q.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.5)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_outputarray_type_01(self):
		"""Test exception with invalid output array type  - Array code Q.
		"""
		# The list of array types should have all supported types other than 'q'.
		for testval in ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'Q', 'f', 'd'):
			with self.subTest(msg='Failed with parameter', testval = testval):
		
				badarray = array.array(testval, itertools.repeat(0, len(self.data)))

				with self.assertRaises(TypeError):
					result = arrayfunc.findindices('==', self.data, badarray)


##############################################################################

 

##############################################################################
class findindices_operator_f(unittest.TestCase):
	"""Test for basic operator function.
	op_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'f'
		self.TestData = [97.0, 97.0, 97.0, 98.0, 99.0, 101.0, 101.0, 102.0, 95.0, 103.0]
		self.zerofill = 0.0

		self.data = array.array(self.TypeCode, self.TestData)
		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		self.ARR_ERR_NOTFOUND = -1

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}


	########################################################
	def Findindices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# If the maxlen parameter is used, trim the source data accordingly.
		if maxlen > 0:
			testdata = data[:maxlen]
		else:
			testdata = data

		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]

		# Peform the operation.
		result = [x for x,y in enumerate(testdata) if opfunc(y, param)]
		copiedlength = len(result)
		
		# Pad out with the same fill used for the output array, and return
		# the number of items copied.
		trimmed = result + list(itertools.repeat(self.zerofill, len(data) - len(result)))

		return trimmed, copiedlength


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code f.
		"""
		param = 97.0
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code f.
		"""
		param = 96.0
		result = arrayfunc.findindices('>', self.data, self.dataout, param)
		expected, explength = self.Findindices('>', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code f.
		"""
		param = 96.0
		result = arrayfunc.findindices('>=', self.data, self.dataout, param)
		expected, explength = self.Findindices('>=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code f.
		"""
		param = 98.0
		result = arrayfunc.findindices('<', self.data, self.dataout, param)
		expected, explength = self.Findindices('<', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code f.
		"""
		param = 98.0
		result = arrayfunc.findindices('<=', self.data, self.dataout, param)
		expected, explength = self.Findindices('<=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code f.
		"""
		param = 98.0
		result = arrayfunc.findindices('!=', self.data, self.dataout, param)
		expected, explength = self.Findindices('!=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)
		

	########################################################
	def test_operator_maxlen_01(self):
		"""Test array maxlen  - Array code f.
		"""
		param = 97.0
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=len(self.data)//2)
		expected, explength = self.Findindices('==', self.data, param, maxlen=len(self.data)//2)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_maxlen_02(self):
		"""Test array maxlen  - Array code f.
		"""
		param = 97.0
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=-1)
		expected, explength = self.Findindices('==', self.data, param, maxlen=-1)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class findindices_params_f(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'f'
		self.TestData = [97.0, 97.0, 97.0, 98.0, 99.0, 101.0, 101.0, 102.0, 102.0, 103.0]
		self.zerofill = 0.0

		self.data = array.array(self.TypeCode, self.TestData)

		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataemptyout = array.array('q')


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code f.
		"""
		param = 101.0
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, param, 3, maxlen=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [1, 2, 3, 4], 3)



	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.0, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.0, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code f.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices('!', self.data, self.dataout, 100.0)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(62, self.data, self.dataout, 100.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = list(filter('a', [0, 1, 2, 3, 4]))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter value  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', 99, self.dataout, 100.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, 99, 100.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code f.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.dataempty, self.dataout, 100.0)


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty output array parameter type  - Array code f.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.data, self.dataemptyout, 100.0)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 'e')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_outputarray_type_01(self):
		"""Test exception with invalid output array type  - Array code f.
		"""
		# The list of array types should have all supported types other than 'q'.
		for testval in ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'Q', 'f', 'd'):
			with self.subTest(msg='Failed with parameter', testval = testval):
		
				badarray = array.array(testval, itertools.repeat(0, len(self.data)))

				with self.assertRaises(TypeError):
					result = arrayfunc.findindices('==', self.data, badarray)


##############################################################################


##############################################################################
class findindices_paramovfl_f(unittest.TestCase):
	"""Test for testing parameter overflow.
	overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'f'
		self.zerofill = 0.0

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, range(97, 107))
		self.dataoutovfl = array.array('q', itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.f_min
		self.Maxval = arrayfunc.arraylimits.f_max


	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal * 1.1)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code f.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval * 1.1)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code f.
		"""
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval)



##############################################################################

 

##############################################################################
class findindices_operator_d(unittest.TestCase):
	"""Test for basic operator function.
	op_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'd'
		self.TestData = [97.0, 97.0, 97.0, 98.0, 99.0, 101.0, 101.0, 102.0, 95.0, 103.0]
		self.zerofill = 0.0

		self.data = array.array(self.TypeCode, self.TestData)
		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		self.ARR_ERR_NOTFOUND = -1

		# These are the compare operators to use when testing the findindices function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}


	########################################################
	def Findindices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# If the maxlen parameter is used, trim the source data accordingly.
		if maxlen > 0:
			testdata = data[:maxlen]
		else:
			testdata = data

		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]

		# Peform the operation.
		result = [x for x,y in enumerate(testdata) if opfunc(y, param)]
		copiedlength = len(result)
		
		# Pad out with the same fill used for the output array, and return
		# the number of items copied.
		trimmed = result + list(itertools.repeat(self.zerofill, len(data) - len(result)))

		return trimmed, copiedlength


	########################################################
	def test_operator_eq_01(self):
		"""Test eq  - Array code d.
		"""
		param = 97.0
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code d.
		"""
		param = 96.0
		result = arrayfunc.findindices('>', self.data, self.dataout, param)
		expected, explength = self.Findindices('>', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code d.
		"""
		param = 96.0
		result = arrayfunc.findindices('>=', self.data, self.dataout, param)
		expected, explength = self.Findindices('>=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code d.
		"""
		param = 98.0
		result = arrayfunc.findindices('<', self.data, self.dataout, param)
		expected, explength = self.Findindices('<', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code d.
		"""
		param = 98.0
		result = arrayfunc.findindices('<=', self.data, self.dataout, param)
		expected, explength = self.Findindices('<=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code d.
		"""
		param = 98.0
		result = arrayfunc.findindices('!=', self.data, self.dataout, param)
		expected, explength = self.Findindices('!=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)
		

	########################################################
	def test_operator_maxlen_01(self):
		"""Test array maxlen  - Array code d.
		"""
		param = 97.0
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=len(self.data)//2)
		expected, explength = self.Findindices('==', self.data, param, maxlen=len(self.data)//2)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_maxlen_02(self):
		"""Test array maxlen  - Array code d.
		"""
		param = 97.0
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=-1)
		expected, explength = self.Findindices('==', self.data, param, maxlen=-1)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################


##############################################################################
class findindices_params_d(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = 'd'
		self.TestData = [97.0, 97.0, 97.0, 98.0, 99.0, 101.0, 101.0, 102.0, 102.0, 103.0]
		self.zerofill = 0.0

		self.data = array.array(self.TypeCode, self.TestData)

		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataemptyout = array.array('q')


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code d.
		"""
		param = 101.0
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, param, 3, maxlen=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [1, 2, 3, 4], 3)



	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.0, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.0, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code d.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices('!', self.data, self.dataout, 100.0)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(62, self.data, self.dataout, 100.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = list(filter('a', [0, 1, 2, 3, 4]))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter value  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', 99, self.dataout, 100.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, 99, 100.0)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code d.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.dataempty, self.dataout, 100.0)


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty output array parameter type  - Array code d.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.data, self.dataemptyout, 100.0)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 'e')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_outputarray_type_01(self):
		"""Test exception with invalid output array type  - Array code d.
		"""
		# The list of array types should have all supported types other than 'q'.
		for testval in ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'Q', 'f', 'd'):
			with self.subTest(msg='Failed with parameter', testval = testval):
		
				badarray = array.array(testval, itertools.repeat(0, len(self.data)))

				with self.assertRaises(TypeError):
					result = arrayfunc.findindices('==', self.data, badarray)


##############################################################################


##############################################################################
class findindices_nonfinite_f(unittest.TestCase):
	"""Test for nan, inf, -inf.
	nonfinite_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('f', [100.0] * 10)
		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))
		self.zerofill = 0.0

		# These are the compare operators to use when testing the function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}


	########################################################
	def Findindices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# If the maxlen parameter is used, trim the source data accordingly.
		if maxlen > 0:
			testdata = data[:maxlen]
		else:
			testdata = data

		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]

		# Peform the operation.
		result = [x for x,y in enumerate(testdata) if opfunc(y, param)]
		copiedlength = len(result)
		
		# Pad out with the same fill used for the output array, and return
		# the number of items copied.
		trimmed = result + list(itertools.repeat(self.zerofill, len(data) - len(result)))

		return trimmed, copiedlength


	########################################################
	def test_nonfinite_01(self):
		"""Test for param of nan  - Array code f.
		"""
		param = math.nan
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_nonfinite_02(self):
		"""Test for param of inf  - Array code f.
		"""
		param = math.inf
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_nonfinite_03(self):
		"""Test for param of -inf  - Array code f.
		"""
		param = -math.inf
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_nonfinite_04(self):
		"""Test for maxlen of nan  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.0, maxlen=math.nan)


	########################################################
	def test_nonfinite_05(self):
		"""Test for maxlen of inf  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.0, maxlen=math.inf)


	########################################################
	def test_nonfinite_06(self):
		"""Test for maxlen of -inf  - Array code f.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.0, maxlen=-math.inf)


##############################################################################


##############################################################################
class findindices_nonfinite_d(unittest.TestCase):
	"""Test for nan, inf, -inf.
	nonfinite_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('d', [100.0] * 10)
		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))
		self.zerofill = 0.0

		# These are the compare operators to use when testing the function.
		self.opvals = {
			'<' : operator.lt,
			'<=' : operator.le,
			'==' : operator.eq,
			'!=' : operator.ne,
			'>=' : operator.ge,
			'>' : operator.gt
			}


	########################################################
	def Findindices(self, op, data, param, maxlen=0):
		"""Emulate the test function.
		"""
		# If the maxlen parameter is used, trim the source data accordingly.
		if maxlen > 0:
			testdata = data[:maxlen]
		else:
			testdata = data

		# Get the type of compare operation we want, and convert it into a
		# function we can use as a predicate.
		opfunc = self.opvals[op]

		# Peform the operation.
		result = [x for x,y in enumerate(testdata) if opfunc(y, param)]
		copiedlength = len(result)
		
		# Pad out with the same fill used for the output array, and return
		# the number of items copied.
		trimmed = result + list(itertools.repeat(self.zerofill, len(data) - len(result)))

		return trimmed, copiedlength


	########################################################
	def test_nonfinite_01(self):
		"""Test for param of nan  - Array code d.
		"""
		param = math.nan
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_nonfinite_02(self):
		"""Test for param of inf  - Array code d.
		"""
		param = math.inf
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_nonfinite_03(self):
		"""Test for param of -inf  - Array code d.
		"""
		param = -math.inf
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_nonfinite_04(self):
		"""Test for maxlen of nan  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.0, maxlen=math.nan)


	########################################################
	def test_nonfinite_05(self):
		"""Test for maxlen of inf  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.0, maxlen=math.inf)


	########################################################
	def test_nonfinite_06(self):
		"""Test for maxlen of -inf  - Array code d.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.0, maxlen=-math.inf)


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
			f.write('findindices\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
