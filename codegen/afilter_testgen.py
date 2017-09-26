#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for afilter.
# Language: Python 3.4
# Date:     22-May-2014
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


intparams = {'testdata' : 100, 'paramdata1' : "'e'", 'paramdata2' : 100.5,
	'overflowinc' : '+ 1', 'overflowdec' : '- 1', 'typeconvert' : 'int', 
	'eq_true1' : 101, 'eq_false1' : 107,
	'gt_true1' : 100, 'gt_false1' : 107, 
	'gte_true1' : 100, 'gte_true2' : 101, 'gte_false1' : 107, 
	'lt_true1' : 102, 'lt_false1' : 95, 
	'lte_true1' : 102, 'lte_true2' : 101, 'lte_false1' : 95, 
	'ne_true1' : 99, 'ne_false1' : 100,
	'skipminoverflow' : '', 'skipmaxoverflow' : ''}

floatparams = {'testdata' : 100.0, 'paramdata1' : "'e'", 'paramdata2' : 100,
	'overflowinc' : '* 1.1', 'overflowdec' : '* 1.1', 'typeconvert' : 'float', 
	'eq_true1' : 101.0, 'eq_false1' : 107.0,
	'gt_true1' : 100.0, 'gt_false1' : 107.0, 
	'gte_true1' : 100.0, 'gte_true2' : 101.0, 'gte_false1' : 107.0, 
	'lt_true1' : 102.0, 'lt_false1' : 95.0, 
	'lte_true1' : 102.0, 'lte_true2' : 101.0, 'lte_false1' : 95.0, 
	'ne_true1' : 99.0, 'ne_false1' : 100.0,
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



# This is used to test floating point data with nan, inf, and -inf.
nantestdata = [{'seq' : '01', 'testval' : 0.0},
	{'seq' : '02', 'testval' : 100.0},
	{'seq' : '03', 'testval' : -100.0},
	{'seq' : '04', 'testval' : 'self.MinVal'},
	{'seq' : '05', 'testval' : 'self.Maxval'}
	]

# ==============================================================================

# The basic template for testing each array type for operator function.
op_template = '''
##############################################################################
class afilter_operator_%(typelabel)s(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.ArrayLength = 10
		self.TestData = [97, 97, 97, 98, 99, 101, 101, 102, 102, 103]
		# As characters - ['a', 'a', 'a', 'b', 'c', 'e', 'e', 'f', 'f', 'g']

		self.data = array.array('%(typecode)s', [%(typeconvert)s(x) for x in self.TestData])
		self.data2 = array.array('%(typecode)s', [%(typeconvert)s(100)]*self.ArrayLength)
		self.dataout = array.array('%(typecode)s', [%(typeconvert)s(0)]*self.ArrayLength)


		# For bytes types, we need a non-array data type.
		if '%(typelabel)s' == 'bytes':
			self.data = bytes(self.data)
			self.data2 = bytes(self.data2)
			self.dataout = bytes(self.dataout)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data, self.dataout, %(eq_true1)s)
		expected = [x for x in self.data if x == %(eq_true1)s]
		self.assertEqual(result, len(expected))
		self.assertEqual(list(self.dataout)[0:2], expected)

		result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data, self.dataout, %(eq_false1)s)
		self.assertEqual(result, 0)

	########################################################
	def test_operator_02_gt(self):
		"""Test gt  - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_gt, self.data, self.dataout, %(gt_true1)s)
		expected = [x for x in self.data if x > %(gt_true1)s]
		self.assertEqual(result, len(expected))
		self.assertEqual(list(self.dataout)[0:5], expected)

		result = arrayfunc.afilter(arrayfunc.aops.af_gt, self.data, self.dataout, %(gt_false1)s)
		self.assertEqual(result, 0)

	########################################################
	def test_operator_03_gte(self):
		"""Test gte  - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_gte, self.data, self.dataout, %(gt_true1)s)
		expected = [x for x in self.data if x >= %(gt_true1)s]
		self.assertEqual(result, len(expected))
		self.assertEqual(list(self.dataout)[0:5], expected)

		result = arrayfunc.afilter(arrayfunc.aops.af_gte, self.data, self.dataout, %(gte_true2)s)
		expected = [x for x in self.data if x >= %(gte_true2)s]
		self.assertEqual(result, len(expected))
		self.assertEqual(list(self.dataout)[0:5], expected)

		result = arrayfunc.afilter(arrayfunc.aops.af_gte, self.data, self.dataout, %(gte_false1)s)
		self.assertEqual(result, 0)

	########################################################
	def test_operator_04_lt(self):
		"""Test lt  - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_lt, self.data, self.dataout, %(lt_true1)s)
		expected = [x for x in self.data if x < %(lt_true1)s]
		self.assertEqual(result, len(expected))
		self.assertEqual(list(self.dataout)[0:7], expected)

		result = arrayfunc.afilter(arrayfunc.aops.af_lt, self.data, self.dataout, %(lt_false1)s)
		self.assertEqual(result, 0)

	########################################################
	def test_operator_05_lte(self):
		"""Test lte  - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_lte, self.data, self.dataout, %(lte_true1)s)
		expected = [x for x in self.data if x <= %(lte_true1)s]
		self.assertEqual(result, len(expected))
		self.assertEqual(list(self.dataout)[0:9], expected)

		result = arrayfunc.afilter(arrayfunc.aops.af_lte, self.data, self.dataout, %(gte_true2)s)
		expected = [x for x in self.data if x <= %(lte_true2)s]
		self.assertEqual(result, len(expected))
		self.assertEqual(list(self.dataout)[0:7], expected)

		result = arrayfunc.afilter(arrayfunc.aops.af_lte, self.data, self.dataout, %(lte_false1)s)
		self.assertEqual(result, 0)

	########################################################
	def test_operator_06_ne(self):
		"""Test ne  - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_ne, self.data, self.dataout, %(ne_true1)s)
		expected = [x for x in self.data if x != %(ne_true1)s]
		self.assertEqual(result, len(expected))
		self.assertEqual(list(self.dataout)[0:9], expected)
		
		result = arrayfunc.afilter(arrayfunc.aops.af_ne, self.data2, self.dataout, %(ne_false1)s)
		self.assertEqual(result, 0)

##############################################################################

'''

# ==============================================================================

# The basic template for testing parameters.
param_template = '''
##############################################################################
class afilter_parameter_%(typelabel)s(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('%(typecode)s', [%(typeconvert)s(x) for x in range(97, 107)])
		self.dataout = array.array('%(typecode)s', [%(typeconvert)s(0)]*10)
		self.dataempty = array.array('%(typecode)s')


		# For bytes types, we need a non-array data type.
		if '%(typelabel)s' == 'bytes':
			self.data = bytes(self.data)
			self.dataout = bytes(self.dataout)
			self.dataempty = bytes(self.dataempty)


	########################################################
	def test_param_01_no_params(self):
		"""Test exception when no parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.afilter()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter()

	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.afilter(arrayfunc.aops.af_eq)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x)

	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x)

	########################################################
	def test_param_04_three_params(self):
		"""Test exception when three parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x)

	########################################################
	def test_param_05_six_params(self):
		"""Test exception when six parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data, self.dataout, %(testdata)s, 5, 5)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x, [1,2,3], 99)

	########################################################
	def test_param_06_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data, self.dataout, %(testdata)s, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x, [1,2,3], xx=2)

	########################################################
	def test_param_07_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data, self.dataout, %(testdata)s, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x, [1,2,3], maxlen='x')

	########################################################
	def test_param_08_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.afilter(-1, self.data, self.dataout, %(testdata)s)


	########################################################
	def test_param_09_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.afilter('a', self.data, self.dataout, %(testdata)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = list(filter('a', [1,2,3]))

	########################################################
	def test_param_10_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.afilter(arrayfunc.aops.af_eq, 99, self.dataout, %(testdata)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x, 99)

	########################################################
	def test_param_11_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data, 99, %(testdata)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x, 99)

	########################################################
	def test_param_12_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.dataempty, self.dataout, %(testdata)s)


	########################################################
	def test_param_13_invalid_output_array_param_length(self):
		"""Test exception with empty output array parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data, self.dataempty, %(testdata)s)

	########################################################
	def test_param_14_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data, self.dataout, %(paramdata1)s)
		with self.assertRaises(TypeError):
			result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data, self.dataout, %(paramdata2)s)


##############################################################################

'''
# ==============================================================================


# The basic template for testing parameter overflow.
overflow_template = '''
##############################################################################
class afilter_overflow_%(typelabel)s(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('%(typecode)s', [%(typeconvert)s(x) for x in range(97, 107)])
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min
		self.Maxval = arrayfunc.arraylimits.%(typecode)s_max


		# For bytes types, we need a non-array data type.
		if '%(typelabel)s' == 'bytes':
			self.data = bytes(self.data)


	########################################################
%(skipminoverflow)s	def test_overflow_01_min(self):
		"""Test parameter overflow min  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data, self.data, self.MinVal %(overflowdec)s)

	########################################################
%(skipmaxoverflow)s	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data, self.data, self.Maxval %(overflowinc)s)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data, self.data, self.MinVal)
		result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data, self.data, self.Maxval)

##############################################################################

'''

# ==============================================================================

# The template for testing floating point nan, inf, -inf.
nan_template = '''
##############################################################################
class afilter_nan_test%(seq)s_%(typelabel)s(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data_nan = array.array('%(typecode)s', [float('nan')]*10)
		self.data_inf = array.array('%(typecode)s', [float('inf')]*10)
		self.data_ninf = array.array('%(typecode)s', [float('-inf')]*10)
		self.dataout = array.array('%(typecode)s', [0.0]*10)

		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min
		self.Maxval = arrayfunc.arraylimits.%(typecode)s_max


	########################################################
	def test_nan_val%(seq)s_01_eq(self):
		"""Test eq with nan and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data_nan, self.dataout, %(testval)s)
		self.assertEqual(result, 0)
		self.assertFalse(float('nan') == %(testval)s)

	########################################################
	def test_nan_val%(seq)s_02_eq(self):
		"""Test eq with inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data_inf, self.dataout, %(testval)s)
		self.assertEqual(result, 0)
		self.assertFalse(float('inf') == %(testval)s)

	########################################################
	def test_nan_val%(seq)s_03_eq(self):
		"""Test eq with -inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data_ninf, self.dataout, %(testval)s)
		self.assertEqual(result, 0)
		self.assertFalse(float('-inf') == %(testval)s)


	########################################################
	def test_nan_val%(seq)s_04_gt(self):
		"""Test gt with nan and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_gt, self.data_nan, self.dataout, %(testval)s)
		self.assertEqual(result, 0)
		self.assertFalse(float('nan') > %(testval)s)

	########################################################
	def test_nan_val%(seq)s_05_gt(self):
		"""Test gt with inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_gt, self.data_inf, self.dataout, %(testval)s)
		self.assertEqual(result, len(self.data_inf))
		self.assertTrue(float('inf') > %(testval)s)

	########################################################
	def test_nan_val%(seq)s_06_gt(self):
		"""Test gt with -inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_gt, self.data_ninf, self.dataout, %(testval)s)
		self.assertEqual(result, 0)
		self.assertFalse(float('-inf') > %(testval)s)


	########################################################
	def test_nan_val%(seq)s_07_gte(self):
		"""Test gte with nan and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_gte, self.data_nan, self.dataout, %(testval)s)
		self.assertEqual(result, 0)
		self.assertFalse(float('nan') >= %(testval)s)

	########################################################
	def test_nan_val%(seq)s_08_gte(self):
		"""Test gte with inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_gte, self.data_inf, self.dataout, %(testval)s)
		self.assertEqual(result, len(self.data_inf))
		self.assertTrue(float('inf') >= %(testval)s)

	########################################################
	def test_nan_val%(seq)s_09_gte(self):
		"""Test gte with -inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_gte, self.data_ninf, self.dataout, %(testval)s)
		self.assertEqual(result, 0)
		self.assertFalse(float('-inf') >= %(testval)s)


	########################################################
	def test_nan_val%(seq)s_10_lt(self):
		"""Test lt with nan and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_lt, self.data_nan, self.dataout, %(testval)s)
		self.assertEqual(result, 0)
		self.assertFalse(float('nan') < %(testval)s)

	########################################################
	def test_nan_val%(seq)s_11_lt(self):
		"""Test lt with inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_lt, self.data_inf, self.dataout, %(testval)s)
		self.assertEqual(result, 0)
		self.assertFalse(float('inf') < %(testval)s)

	########################################################
	def test_nan_val%(seq)s_12_lt(self):
		"""Test lt with -inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_lt, self.data_ninf, self.dataout, %(testval)s)
		self.assertEqual(result, len(self.data_ninf))
		self.assertTrue(float('-inf') < %(testval)s)


	########################################################
	def test_nan_val%(seq)s_13_lte(self):
		"""Test lte with nan and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_lte, self.data_nan, self.dataout, %(testval)s)
		self.assertEqual(result, 0)
		self.assertFalse(float('nan') <= %(testval)s)

	########################################################
	def test_nan_val%(seq)s_14_lte(self):
		"""Test lte with inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_lte, self.data_inf, self.dataout, %(testval)s)
		self.assertEqual(result, 0)
		self.assertFalse(float('inf') <= %(testval)s)

	########################################################
	def test_nan_val%(seq)s_15_lte(self):
		"""Test lte with -inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_lte, self.data_ninf, self.dataout, %(testval)s)
		self.assertEqual(result, len(self.data_ninf))
		self.assertTrue(float('-inf') <= %(testval)s)


	########################################################
	def test_nan_val%(seq)s_16_ne(self):
		"""Test ne with nan and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_ne, self.data_nan, self.dataout, %(testval)s)
		self.assertEqual(result, len(self.data_nan))
		self.assertTrue(float('nan') != %(testval)s)

	########################################################
	def test_nan_val%(seq)s_17_ne(self):
		"""Test ne with inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_ne, self.data_inf, self.dataout, %(testval)s)
		self.assertEqual(result, len(self.data_inf))
		self.assertTrue(float('inf') != %(testval)s)

	########################################################
	def test_nan_val%(seq)s_18_ne(self):
		"""Test ne with -inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.afilter(arrayfunc.aops.af_ne, self.data_ninf, self.dataout, %(testval)s)
		self.assertEqual(result, len(self.data_ninf))
		self.assertTrue(float('-inf') != %(testval)s)

##############################################################################

'''

# ==============================================================================


# The basic template for testing floating point parameters with nan, inf, -inf.
nanparam_template = '''
##############################################################################
class afilter_nanparam_%(typelabel)s(unittest.TestCase):
	"""Test for float parameter errors with nan, inf, -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('%(typecode)s', [100.0]*10)
		self.dataout = array.array('%(typecode)s', [0.0]*10)


	########################################################
	def test_nanparam_01_nan(self):
		"""Test parameter nan  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data, self.dataout, float('nan'))

	########################################################
	def test_nanparam_02_inf(self):
		"""Test parameter inf  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data, self.dataout, float('inf'))

	########################################################
	def test_nanparam_03_ninf(self):
		"""Test parameter negative inf  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.afilter(arrayfunc.aops.af_eq, self.data, self.dataout, float('-inf'))


##############################################################################

'''

# ==============================================================================

# Data for the copyright header files.
headerdate = codegen_common.FormatHeaderData('test_afilter', '23-May-2014', 'afilter')


with open('test_afilter.py', 'w') as f:
	# The copyright header.
	f.write(codegen_common.HeaderTemplate % headerdate)

	# Output the generated code for basic operator tests.
	for funtypes in codegen_common.arraycodes:
		datarec = testdata[funtypes]
		datarec['typecode'] = funtypes
		datarec['typelabel'] = funtypes
		f.write(op_template % datarec)

	# Output the generated code for parameter tests.
	for funtypes in codegen_common.arraycodes:
		datarec = testdata[funtypes]
		datarec['typecode'] = funtypes
		datarec['typelabel'] = funtypes
		f.write(param_template % datarec)


	# Output the generated code for parameter overflow tests.
	for funtypes in codegen_common.arraycodes:
		# There are some array types we can't test for overflow.
		if funtypes not in 'LQ':
			datarec = testdata[funtypes]
			datarec['typecode'] = funtypes
			datarec['typelabel'] = funtypes
			f.write(overflow_template % datarec)


	# Do the tests for bytes.
	datarec = testdata['B']
	datarec['typecode'] = 'B'
	datarec['typelabel'] = 'bytes'
	f.write(op_template % datarec)
	f.write(param_template % datarec)
	f.write(overflow_template % datarec)


	# Output the generated code for nan and inf data in array tests.
	datarec = {}
	for funtypes in codegen_common.floatarrays:
		for testseq in nantestdata:
			datarec.update(testseq)
			datarec['typecode'] = funtypes
			datarec['typelabel'] = funtypes
			f.write(nan_template % datarec)


	# Output the generated code for nan and inf in parameter tests.
	datarec = {}
	for funtypes in codegen_common.floatarrays:
		datarec['typecode'] = funtypes
		datarec['typelabel'] = funtypes
		f.write(nanparam_template % datarec)


	f.write(codegen_common.testendtemplate % 'afilter')


