#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for findindices.
# Language: Python 3.4
# Date:     21-Jun-2014
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

# ==============================================================================

import copy

import codegen_common

# ==============================================================================


intparams = {'overflowinc' : '+ 1', 'overflowdec' : '- 1', 
	'typeconvert' : 'int', 'invalidtypeconvert' : 'float',
	'skipminoverflow' : '', 'skipmaxoverflow' : ''}

floatparams = {'overflowinc' : '* 1.1', 'overflowdec' : '* 1.1', 
	'typeconvert' : 'float', 'invalidtypeconvert' : 'int',
	'skipminoverflow' : '', 'skipmaxoverflow' : ''}

testdata = {
	'b' : intparams,
	'B' : intparams,
	'h' : intparams,
	'H' : intparams,
	'i' : intparams,
	'I' : copy.copy(intparams),
	'l' : intparams,
	'L' : intparams,
	'q' : copy.copy(intparams),
	'Q' : copy.copy(intparams),
	'f' : floatparams,
	'd' : floatparams,
	}

# Patch in the case for 'I' arrays.
testdata['I']['skipminoverflow'] = codegen_common.OvflTestSkip
testdata['I']['skipmaxoverflow'] = codegen_common.OvflTestSkip


# This is used to insert code to convert the test data to bytes type. 
bytesconverter = 'data = bytes(data)'


# ==============================================================================

# The template used to generate the tests.
template = '''
##############################################################################
class findindices_operator_%(typelabel)s(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = '%(typecode)s'
		self.TestData = [%(typeconvert)s(x) for x in [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.TestData2 = [%(typeconvert)s(x) for x in [103, 102, 101, 100, 97, 97, 97, 98, 99, 101, 101, 102, 102, 103]]
		self.constfill = %(typeconvert)s(100)

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

		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min
		self.Maxval = arrayfunc.arraylimits.%(typecode)s_max


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataoutempty = array.array(self.OutputTypeCode)

		# This duplicates the error code for no matches found.
		self.ARR_ERR_NOTFOUND = -5


		# For bytes types, we need a non-array data type.
		if '%(typelabel)s' == 'bytes':
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
		"""Test eq  - Array code %(typelabel)s. - Parameter in middle.
		"""
		param = %(typeconvert)s(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_02(self):
		"""Test eq  - Array code %(typelabel)s. - Parameter at start.
		"""
		param = %(typeconvert)s(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_03(self):
		"""Test eq  - Array code %(typelabel)s. - Parameter at end.
		"""
		param = %(typeconvert)s(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_eq_04(self):
		"""Test eq  - Array code %(typelabel)s. - Parameter not found.
		"""
		param = %(typeconvert)s(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('==', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code %(typelabel)s. - Parameter in middle.
		"""
		param = %(typeconvert)s(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_02(self):
		"""Test gt  - Array code %(typelabel)s. - Parameter at start.
		"""
		param = %(typeconvert)s(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_03(self):
		"""Test gt  - Array code %(typelabel)s. - Parameter at end.
		"""
		param = %(typeconvert)s(102)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gt_04(self):
		"""Test gt  - Array code %(typelabel)s. - Parameter not found.
		"""
		param = %(typeconvert)s(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gt, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code %(typelabel)s. - Parameter in middle.
		"""
		param = %(typeconvert)s(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_02(self):
		"""Test gte  - Array code %(typelabel)s. - Parameter at start.
		"""
		param = %(typeconvert)s(97)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_03(self):
		"""Test gte  - Array code %(typelabel)s. - Parameter at end.
		"""
		param = %(typeconvert)s(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_gte_04(self):
		"""Test gte  - Array code %(typelabel)s. - Parameter not found.
		"""
		param = %(typeconvert)s(110)
		result = arrayfunc.findindices(arrayfunc.aops.af_gte, self.data, self.dataout, param)
		expected, expectedlength = self.FindIndices('>=', self.data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)



	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code %(typelabel)s. - Parameter in middle.
		"""
		param = %(typeconvert)s(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_02(self):
		"""Test lt  - Array code %(typelabel)s. - Parameter at start.
		"""
		param = %(typeconvert)s(104)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_03(self):
		"""Test lt  - Array code %(typelabel)s. - Parameter at end.
		"""
		param = %(typeconvert)s(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lt_04(self):
		"""Test lt  - Array code %(typelabel)s. - Parameter not found.
		"""
		param = %(typeconvert)s(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lt, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code %(typelabel)s. - Parameter in middle.
		"""
		param = %(typeconvert)s(101)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_02(self):
		"""Test lte  - Array code %(typelabel)s. - Parameter at start.
		"""
		param = %(typeconvert)s(103)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_03(self):
		"""Test lte  - Array code %(typelabel)s. - Parameter at end.
		"""
		param = %(typeconvert)s(98)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)


	########################################################
	def test_operator_lte_04(self):
		"""Test lte  - Array code %(typelabel)s. - Parameter not found.
		"""
		param = %(typeconvert)s(96)
		result = arrayfunc.findindices(arrayfunc.aops.af_lte, self.data2, self.dataout2, param)
		expected, expectedlength = self.FindIndices('<=', self.data2, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout2), expected)



	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code %(typelabel)s. - Parameter in middle.
		"""
		param = %(typeconvert)s(100)
		data = array.array(self.TypeCode, [%(typeconvert)s(x) for x in [100, 100, 100, 100, 100, 101, 100, 100, 100, 100]])
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_02(self):
		"""Test ne  - Array code %(typelabel)s. - Parameter at start.
		"""
		param = %(typeconvert)s(103)
		data = array.array(self.TypeCode, [%(typeconvert)s(x) for x in [101, 100, 100, 100, 100, 100, 100, 100, 100, 100]])
		%(bytesconverter)s
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_03(self):
		"""Test ne  - Array code %(typelabel)s. - Parameter at end.
		"""
		param = %(typeconvert)s(98)
		data = array.array(self.TypeCode, [%(typeconvert)s(x) for x in [100, 100, 100, 100, 100, 100, 100, 100, 100, 101]])
		%(bytesconverter)s
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, data, self.dataout, param)
		expected, expectedlength = self.FindIndices('!=', data, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_ne_04(self):
		"""Test ne  - Array code %(typelabel)s. - Parameter not found.
		"""
		param = %(typeconvert)s(100)
		result = arrayfunc.findindices(arrayfunc.aops.af_ne, self.data3, self.dataout3, param)
		expected, expectedlength = self.FindIndices('!=', self.data3, param)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout3), expected)



	########################################################
	def test_operator_lim_01(self):
		"""Test arraly limits  - Array code %(typelabel)s.
		"""
		param = %(typeconvert)s(101)
		data = array.array(self.TypeCode, [%(typeconvert)s(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		%(bytesconverter)s
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=len(self.data)//2)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=len(self.data)//2)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_operator_lim_02(self):
		"""Test arraly limits  - Array code %(typelabel)s.
		"""
		param = %(typeconvert)s(101)
		data = array.array(self.TypeCode, [%(typeconvert)s(x) for x in [100, 100, 100, 101, 101, 101, 100, 101, 100, 101]])
		%(bytesconverter)s
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, data, self.dataout, param, maxlen=-1)
		expected, expectedlength = self.FindIndices('==', data, param, maxlen=-1)
		self.assertEqual(result, expectedlength)
		self.assertEqual(list(self.dataout), expected)


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code %(typelabel)s.
		"""
		param = %(typeconvert)s(101)
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, param, 3, maxlen=2)


	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, %(typeconvert)s(100), xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, %(typeconvert)s(100), maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code %(typelabel)s.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices(-1, self.data, self.dataout, %(typeconvert)s(100))


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('a', self.data, self.dataout, %(typeconvert)s(100))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, 99, self.dataout, %(typeconvert)s(100))


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, 99, %(typeconvert)s(100))


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataout, %(typeconvert)s(100))


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataoutempty, %(typeconvert)s(100))


	########################################################
	def test_param_invalid_input_and_output_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataempty, self.dataoutempty, %(typeconvert)s(100))


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 'e')


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, %(invalidtypeconvert)s(100.5))


'''

# Overflow testing. This can't be used with all types.
overflow_template = '''
	########################################################
%(skipminoverflow)s	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal %(overflowdec)s)


	########################################################
%(skipmaxoverflow)s	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval %(overflowinc)s)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code %(typelabel)s.
		"""
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.dataovfl, self.dataoutovfl, self.Maxval)

'''


# The template used to generate the tests for nan, inf, -inf.
nan_template = '''
##############################################################################
class findindices_nan_%(typelabel)s(unittest.TestCase):
	"""Test for nan, inf, -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('%(typecode)s', [100.0] * 10)
		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


	########################################################
	def test_nan_01(self):
		"""Test for param of nan  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float('nan'))


	########################################################
	def test_nan_02(self):
		"""Test for param of inf  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float('inf'))


	########################################################
	def test_nan_03(self):
		"""Test for param of -inf  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, float('-inf'))


	########################################################
	def test_nan_04(self):
		"""Test for lim of nan  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 100.0, maxlen=float('nan'))


	########################################################
	def test_nan_05(self):
		"""Test for lim of inf  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 100.0, maxlen=float('inf'))


	########################################################
	def test_nan_06(self):
		"""Test for lim of -inf  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(arrayfunc.aops.af_eq, self.data, self.dataout, 100.0, maxlen=float('-inf'))


##############################################################################
'''


classend = """
##############################################################################
"""

# ==============================================================================

endtemplate = """
##############################################################################
if __name__ == '__main__':
	with open('arrayfunc_unittest.txt', 'a') as f:
		f.write('\\n\\n')
		f.write('findindices\\n\\n')
		trun = unittest.TextTestRunner(f)
		unittest.main(testRunner=trun)

##############################################################################
"""

# ==============================================================================

# Data for the copyright header files.
headerdate = codegen_common.FormatHeaderData('test_findindices', '21-Jun-2014', 'findindices')

with open('test_findindices.py', 'w') as f:
	# The copyright header.
	f.write(codegen_common.HeaderTemplate % headerdate)

	# Output the generated code for all tests.
	for funtypes in codegen_common.arraycodes:
		datarec = testdata[funtypes]
		datarec['typecode'] = funtypes
		datarec['typelabel'] = funtypes
		datarec['bytesconverter'] = ''
		f.write(template % datarec)

		# There are some array types we can't test for overflow.
		if funtypes not in 'LQ':
			datarec = testdata[funtypes]
			datarec['typecode'] = funtypes
			datarec['typelabel'] = funtypes
			datarec['bytesconverter'] = ''
			f.write(overflow_template % datarec)

		# This is just a comment to close off the class.
		f.write(classend)


	# Do the tests for bytes.
	datarec = testdata['B']
	datarec['typecode'] = 'B'
	datarec['typelabel'] = 'bytes'
	datarec['bytesconverter'] = bytesconverter
	f.write(template % datarec)
	f.write(overflow_template % datarec)


	# Test for nan, inf, -inf.
	for funtypes in codegen_common.floatarrays:
		f.write(nan_template % {'typelabel' : funtypes, 'typecode' : funtypes})


	f.write(endtemplate)


