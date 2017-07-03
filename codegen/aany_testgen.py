#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for aany.
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

signedtestdata = {'testdata' : 100, 'paramdata1' : "'e'", 'paramdata2' : 100.5,
	'overflowinc' : '+ 1', 'overflowdec' : '- 1', 
	'eq_true1' : 100, 'eq_false1' : 127,
	'gt_true1' : 90, 'gt_false1' : 127, 
	'gte_true1' : 100, 'gte_true2' : 105, 'gte_false1' : 127, 
	'lt_true1' : 127, 'lt_false1' : 90, 
	'lte_true1' : 100, 'lte_true2' : 106, 'lte_false1' : 90, 
	'ne_true1' : 127, 'ne_false1' : 100,
	'skipminoverflow' : '', 'skipmaxoverflow' : ''}

unsignedtestdata = {'testdata' : 100, 'paramdata1' : "'e'", 'paramdata2' : 100.5,
	'overflowinc' : '+ 1', 'overflowdec' : '- 1', 
	'eq_true1' : 100, 'eq_false1' : 127,
	'gt_true1' : 90, 'gt_false1' : 127, 
	'gte_true1' : 100, 'gte_true2' : 105, 'gte_false1' : 127, 
	'lt_true1' : 127, 'lt_false1' : 90,  
	'lte_true1' : 100, 'lte_true2' : 106, 'lte_false1' : 90, 
	'ne_true1' : 127, 'ne_false1' : 100,
	'skipminoverflow' : '', 'skipmaxoverflow' : ''}

floattestdata = {'testdata' : 100.0, 'paramdata1' : "'e'", 'paramdata2' : 100,
	'overflowinc' : '* 1.1', 'overflowdec' : '* 1.1', 
	'eq_true1' : 100.0, 'eq_false1' : 127.0,
	'gt_true1' : 90.0, 'gt_false1' : 127.0, 
	'gte_true1' : 100.0, 'gte_true2' : 105.0, 'gte_false1' : 127.0, 
	'lt_true1' : 127.0, 'lt_false1' : 90.0, 
	'lte_true1' : 100.0, 'lte_true2' : 106.0, 'lte_false1' : 90.0, 
	'ne_true1' : 127.0, 'ne_false1' : 100.0,
	'skipminoverflow' : '', 'skipmaxoverflow' : ''}


testdata = {'b' : copy.copy(signedtestdata),
	'B' : copy.copy(unsignedtestdata),
	'h' : copy.copy(signedtestdata),
	'H' : copy.copy(unsignedtestdata),
	'i' : copy.copy(signedtestdata),
	'I' : copy.copy(unsignedtestdata),
	'l' : copy.copy(signedtestdata),
	'L' : copy.copy(unsignedtestdata),
	'q' : copy.copy(signedtestdata),
	'Q' : copy.copy(unsignedtestdata),
	'f' : copy.copy(floattestdata),
	'd' : copy.copy(floattestdata),
}

# It is not possible to check parameter overflow for this array type.
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
class aany_operator_%(simdpresent)s_simd_%(typelabel)s(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# Data with one element different. This is evenly divisible by the SIMD
		# register size and should be caught by the SIMD code.
		# For gt, gte
		datalisteven = [100] * 160
		datalisteven[-1] = 101

		# For lt, lte
		datalisteven2 = [100] * 160
		datalisteven2[-1] = 99

		# For ne
		datalisteven3 = [100] * 160

		# Data with one element different. This is not evenly divisible by the 
		# SIMD register size and should be handled by the non-SIMD code which 
		# catches the odd array data after the SIMD operation.
		# For gt, gte
		datalistodd = [100] * 160
		datalistodd.append(101)

		# For lt, lte
		datalistodd2 = [100] * 160
		datalistodd2.append(99)

		# For ne
		datalistodd3 = [100] * 160
		datalistodd3.append(100)


		self.dataeven = array.array('%(typecode)s', datalisteven)
		self.dataodd = array.array('%(typecode)s', datalistodd)
		self.dataeven2 = array.array('%(typecode)s', datalisteven2)
		self.dataodd2 = array.array('%(typecode)s', datalistodd2)
		self.dataeven3 = array.array('%(typecode)s', datalisteven3)
		self.dataodd3 = array.array('%(typecode)s', datalistodd3)


		# For bytes types, we need a non-array data type.
		if '%(typelabel)s' == 'bytes':
			self.dataeven = bytes(self.dataeven)
			self.dataodd = bytes(self.dataodd)
			self.dataeven2 = bytes(self.dataeven2)
			self.dataodd2 = bytes(self.dataodd2)
			self.dataeven3 = bytes(self.dataeven3)
			self.dataodd3 = bytes(self.dataodd3)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code %(typelabel)s. General test even length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 101%(decimal)s %(nosimd)s)
		self.assertTrue(result)


	########################################################
	def test_operator_02_eq(self):
		"""Test eq  - Array code %(typelabel)s. General test even length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataeven, 102%(decimal)s %(nosimd)s)
		self.assertFalse(result)


	########################################################
	def test_operator_03_eq(self):
		"""Test eq  - Array code %(typelabel)s. General test odd length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 101%(decimal)s %(nosimd)s)
		self.assertTrue(result)


	########################################################
	def test_operator_04_eq(self):
		"""Test eq  - Array code %(typelabel)s. General test odd length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataodd, 102%(decimal)s %(nosimd)s)
		self.assertFalse(result)



	########################################################
	def test_operator_05_gt(self):
		"""Test gt  - Array code %(typelabel)s. General test even length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 100%(decimal)s %(nosimd)s)
		self.assertTrue(result)


	########################################################
	def test_operator_06_gt(self):
		"""Test gt  - Array code %(typelabel)s. General test even length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataeven, 102%(decimal)s %(nosimd)s)
		self.assertFalse(result)


	########################################################
	def test_operator_07_gt(self):
		"""Test gt  - Array code %(typelabel)s. General test odd length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 100%(decimal)s %(nosimd)s)
		self.assertTrue(result)


	########################################################
	def test_operator_08_gt(self):
		"""Test gt  - Array code %(typelabel)s. General test odd length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.dataodd, 102%(decimal)s %(nosimd)s)
		self.assertFalse(result)



	########################################################
	def test_operator_09_gte(self):
		"""Test gte  - Array code %(typelabel)s. General test even length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 100%(decimal)s %(nosimd)s)
		self.assertTrue(result)


	########################################################
	def test_operator_10_gte(self):
		"""Test gte  - Array code %(typelabel)s. General test even length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 101%(decimal)s %(nosimd)s)
		self.assertTrue(result)


	########################################################
	def test_operator_11_gte(self):
		"""Test gte  - Array code %(typelabel)s. General test even length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataeven, 102%(decimal)s %(nosimd)s)
		self.assertFalse(result)


	########################################################
	def test_operator_12_gte(self):
		"""Test gte  - Array code %(typelabel)s. General test odd length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 100%(decimal)s %(nosimd)s)
		self.assertTrue(result)


	########################################################
	def test_operator_13_gte(self):
		"""Test gte  - Array code %(typelabel)s. General test odd length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 101%(decimal)s %(nosimd)s)
		self.assertTrue(result)


	########################################################
	def test_operator_14_gte(self):
		"""Test gte  - Array code %(typelabel)s. General test odd length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.dataodd, 102%(decimal)s %(nosimd)s)
		self.assertFalse(result)



	########################################################
	def test_operator_15_lt(self):
		"""Test lt  - Array code %(typelabel)s. General test even length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 100%(decimal)s %(nosimd)s)
		self.assertTrue(result)


	########################################################
	def test_operator_16_lt(self):
		"""Test lt  - Array code %(typelabel)s. General test even length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataeven2, 98%(decimal)s %(nosimd)s)
		self.assertFalse(result)


	########################################################
	def test_operator_17_lt(self):
		"""Test lt  - Array code %(typelabel)s. General test odd length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 100%(decimal)s %(nosimd)s)
		self.assertTrue(result)


	########################################################
	def test_operator_18_lt(self):
		"""Test lt  - Array code %(typelabel)s. General test odd length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.dataodd2, 98%(decimal)s %(nosimd)s)
		self.assertFalse(result)



	########################################################
	def test_operator_19_lte(self):
		"""Test lte  - Array code %(typelabel)s. General test even length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 100%(decimal)s %(nosimd)s)
		self.assertTrue(result)


	########################################################
	def test_operator_20_lte(self):
		"""Test lte  - Array code %(typelabel)s. General test even length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 99%(decimal)s %(nosimd)s)
		self.assertTrue(result)


	########################################################
	def test_operator_21_lte(self):
		"""Test lte  - Array code %(typelabel)s. General test even length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataeven2, 98%(decimal)s %(nosimd)s)
		self.assertFalse(result)


	########################################################
	def test_operator_22_lte(self):
		"""Test lte  - Array code %(typelabel)s. General test odd length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 100%(decimal)s %(nosimd)s)
		self.assertTrue(result)


	########################################################
	def test_operator_23_lte(self):
		"""Test lte  - Array code %(typelabel)s. General test odd length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 99%(decimal)s %(nosimd)s)
		self.assertTrue(result)


	########################################################
	def test_operator_24_lte(self):
		"""Test lte  - Array code %(typelabel)s. General test odd length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.dataodd2, 98%(decimal)s %(nosimd)s)
		self.assertFalse(result)



	########################################################
	def test_operator_25_ne(self):
		"""Test ne  - Array code %(typelabel)s. General test even length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven2, 100%(decimal)s %(nosimd)s)
		self.assertTrue(result)


	########################################################
	def test_operator_26_ne(self):
		"""Test ne  - Array code %(typelabel)s. General test even length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataeven3, 100%(decimal)s %(nosimd)s)
		self.assertFalse(result)


	########################################################
	def test_operator_27_ne(self):
		"""Test ne  - Array code %(typelabel)s. General test odd length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd2, 100%(decimal)s %(nosimd)s)
		self.assertTrue(result)


	########################################################
	def test_operator_28_ne(self):
		"""Test ne  - Array code %(typelabel)s. General test odd length array %(simdpresent)s SIMD.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.dataodd3, 100%(decimal)s %(nosimd)s)
		self.assertFalse(result)




##############################################################################

'''

# ==============================================================================

# The basic template for testing parameters.
param_template = '''
##############################################################################
class aany_parameter_%(typelabel)s(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('%(typecode)s', list(range(97, 107)) * 10)
		self.dataempty = array.array('%(typecode)s')


		# For bytes types, we need a non-array data type.
		if '%(typelabel)s' == 'bytes':
			self.data = bytes(self.data)
			self.dataempty = bytes(self.dataempty)


	########################################################
	def test_param_01_no_params(self):
		"""Test exception when no parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any()


	########################################################
	def test_param_04_six_params(self):
		"""Test exception when six parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, %(testdata)s, 99, 0, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, %(testdata)s, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any([1, 2, 3], xx=2)


	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid maxlen keyword parameter type passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, %(testdata)s, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code %(typelabel)s.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aany(-1, self.data, %(testdata)s)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany('a', self.data, %(testdata)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, 99, %(testdata)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.dataempty, %(testdata)s)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, %(paramdata1)s)
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, %(paramdata2)s)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)



	########################################################
	def test_param_12_invalid_keyword_param_type(self):
		"""Test exception with invalid nosimd keyword parameter type passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, %(testdata)s, nosimd='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = any(1)


##############################################################################

'''
# ==============================================================================


# The basic template for testing parameter overflow.
overflow_template = '''
##############################################################################
class aany_overflow_%(typelabel)s(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('%(typecode)s', list(range(97, 107)) * 10)
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
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal %(overflowdec)s)

	########################################################
%(skipmaxoverflow)s	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval %(overflowinc)s)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.MinVal)
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, self.Maxval)

##############################################################################

'''


# ==============================================================================

# The template for testing floating point nan, inf, -inf.
nan_template = '''
##############################################################################
class aany_nan_test%(seq)s_%(typelabel)s(unittest.TestCase):
	"""Test for operator function with floating point nan inf, and -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data_nan = array.array('%(typecode)s', [float('nan')]*100)
		self.data_inf = array.array('%(typecode)s', [float('inf')]*100)
		self.data_ninf = array.array('%(typecode)s', [float('-inf')]*100)

		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min
		self.Maxval = arrayfunc.arraylimits.%(typecode)s_max

	########################################################
	def test_nan_val%(seq)s_01_eq(self):
		"""Test eq with nan and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_nan, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('nan') == %(testval)s)

	########################################################
	def test_nan_val%(seq)s_02_eq(self):
		"""Test eq with inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_inf, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('inf') == %(testval)s)

	########################################################
	def test_nan_val%(seq)s_03_eq(self):
		"""Test eq with -inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data_ninf, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(%(testval)s == float('-inf'))


	########################################################
	def test_nan_val%(seq)s_04_gt(self):
		"""Test gt with nan and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_nan, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('nan') > %(testval)s)

	########################################################
	def test_nan_val%(seq)s_05_gt(self):
		"""Test gt with inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_inf, %(testval)s)
		self.assertTrue(result)
		self.assertTrue(float('inf') > %(testval)s)

	########################################################
	def test_nan_val%(seq)s_06_gt(self):
		"""Test gt with -inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gt, self.data_ninf, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > %(testval)s)


	########################################################
	def test_nan_val%(seq)s_07_gte(self):
		"""Test gte with nan and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_nan, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= %(testval)s)

	########################################################
	def test_nan_val%(seq)s_08_gte(self):
		"""Test gte with inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_inf, %(testval)s)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= %(testval)s)

	########################################################
	def test_nan_val%(seq)s_09_gte(self):
		"""Test gte with -inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_gte, self.data_ninf, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= %(testval)s)


	########################################################
	def test_nan_val%(seq)s_10_lt(self):
		"""Test lt with nan and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_nan, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('nan') < %(testval)s)

	########################################################
	def test_nan_val%(seq)s_11_lt(self):
		"""Test lt with inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_inf, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('inf') < %(testval)s)

	########################################################
	def test_nan_val%(seq)s_12_lt(self):
		"""Test lt with -inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lt, self.data_ninf, %(testval)s)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < %(testval)s)


	########################################################
	def test_nan_val%(seq)s_13_lte(self):
		"""Test lte with nan and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_nan, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= %(testval)s)

	########################################################
	def test_nan_val%(seq)s_14_lte(self):
		"""Test lte with inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_inf, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= %(testval)s)

	########################################################
	def test_nan_val%(seq)s_15_lte(self):
		"""Test lte with -inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_lte, self.data_ninf, %(testval)s)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= %(testval)s)


	########################################################
	def test_nan_val%(seq)s_16_ne(self):
		"""Test ne with nan and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_nan, %(testval)s)
		self.assertTrue(result)
		self.assertTrue(float('nan') != %(testval)s)

	########################################################
	def test_nan_val%(seq)s_17_ne(self):
		"""Test ne with inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_inf, %(testval)s)
		self.assertTrue(result)
		self.assertTrue(float('inf') != %(testval)s)

	########################################################
	def test_nan_val%(seq)s_18_ne(self):
		"""Test ne with -inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aany(arrayfunc.aops.af_ne, self.data_ninf, %(testval)s)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != %(testval)s)

##############################################################################

'''


# ==============================================================================


# The basic template for testing floating point parameters with nan, inf, -inf.
nanparam_template = '''
##############################################################################
class aany_nanparam_%(typelabel)s(unittest.TestCase):
	"""Test for float parameter errors with nan, inf, -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('%(typecode)s', [100.0]*100)


	########################################################
	def test_nanparam_01_nan(self):
		"""Test parameter nan  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, float('nan'))

	########################################################
	def test_nanparam_02_inf(self):
		"""Test parameter inf  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, float('inf'))

	########################################################
	def test_nanparam_03_ninf(self):
		"""Test parameter negative inf  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aany(arrayfunc.aops.af_eq, self.data, float('-inf'))


##############################################################################

'''

# ==============================================================================

endtemplate = """
##############################################################################
if __name__ == '__main__':
	with open('arrayfunc_unittest.txt', 'a') as f:
		f.write('\\n\\n')
		f.write('aany\\n\\n')
		trun = unittest.TextTestRunner(f)
		unittest.main(testRunner=trun)

##############################################################################
"""

# ==============================================================================

# Data for the copyright header files.
headerdate = codegen_common.FormatHeaderData('test_aany', '20-May-2014', 'aany')

with open('test_aany.py', 'w') as f:
	# The copyright header.
	f.write(codegen_common.HeaderTemplate % headerdate)

	############################################################################

	# Output the generated code for basic operator tests with SIMD.
	for funtypes in codegen_common.arraycodes:
		datarec = testdata[funtypes]
		datarec['typecode'] = funtypes
		datarec['typelabel'] = funtypes
		if funtypes in codegen_common.floatarrays:
			datarec['decimal'] = '.0'
		else:
			datarec['decimal'] = ''

		# With SIMD.
		datarec['simdpresent'] = 'with'
		datarec['nosimd'] = ''
		f.write(op_template % datarec)

		# Without SIMD.
		datarec['simdpresent'] = 'without'
		datarec['nosimd'] = ', nosimd=True'
		f.write(op_template % datarec)


	# Do the tests for bytes.
	datarec = testdata['B']
	datarec['typecode'] = 'B'
	datarec['typelabel'] = 'bytes'
	datarec['decimal'] = ''
	# With SIMD.
	datarec['simdpresent'] = 'with'
	datarec['nosimd'] = ''
	f.write(op_template % datarec)
	# Without SIMD.
	datarec['simdpresent'] = 'without'
	datarec['nosimd'] = ', nosimd=True'
	f.write(op_template % datarec)

	############################################################################


	# Output the generated code for parameter tests.
	for funtypes in codegen_common.arraycodes:
		datarec = testdata[funtypes]
		datarec['typecode'] = funtypes
		datarec['typelabel'] = funtypes
		f.write(param_template % datarec)

	############################################################################

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
	f.write(param_template % datarec)
	f.write(overflow_template % datarec)

	############################################################################


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

	f.write(endtemplate)


