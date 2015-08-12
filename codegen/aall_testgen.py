#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for aall.
# Language: Python 3.4
# Date:     21-May-2014
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
	'eq_true1' : 100, 'eq_false1' : 99,
	'gt_true1' : 99, 'gt_false1' : 100, 
	'gte_true1' : 99, 'gte_true2' : 100, 'gte_false1' : 101, 
	'lt_true1' : 101, 'lt_false1' : 100, 
	'lte_true1' : 101, 'lte_true2' : 100, 'lte_false1' : 99, 
	'ne_true1' : 99, 'ne_false1' : 100,
	'skipminoverflow' : '', 'skipmaxoverflow' : '', 
	'skiplonglong' : ''}


unsignedtestdata = {'testdata' : 100, 'paramdata1' : "'e'", 'paramdata2' : 100.5,
	'overflowinc' : '+ 1', 'overflowdec' : '- 1', 
	'eq_true1' : 100, 'eq_false1' : 99,
	'gt_true1' : 99, 'gt_false1' : 100, 
	'gte_true1' : 99, 'gte_true2' : 100, 'gte_false1' : 101, 
	'lt_true1' : 101, 'lt_false1' : 100, 
	'lte_true1' : 101, 'lte_true2' : 100, 'lte_false1' : 99, 
	'ne_true1' : 99, 'ne_false1' : 100,
	'skipminoverflow' : '', 'skipmaxoverflow' : '', 
	'skiplonglong' : ''}

floattestdata = {'testdata' : 100.0, 'paramdata1' : "'e'", 'paramdata2' : 100,
	'overflowinc' : '* 1.1', 'overflowdec' : '* 1.1', 
	'eq_true1' : 100.0, 'eq_false1' : 99.0,
	'gt_true1' : 99.0, 'gt_false1' : 100.0, 
	'gte_true1' : 99.0, 'gte_true2' : 100.0, 'gte_false1' : 101.0, 
	'lt_true1' : 101.0, 'lt_false1' : 100.0, 
	'lte_true1' : 101.0, 'lte_true2' : 100.0, 'lte_false1' : 99.0, 
	'ne_true1' : 99.0, 'ne_false1' : 100.0,
	'skipminoverflow' : '', 'skipmaxoverflow' : '', 
	'skiplonglong' : ''}



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


# Patch in the cases for 'q' and 'Q' arrays.
testdata['q']['skiplonglong'] = codegen_common.LongLongTestSkipq
testdata['Q']['skiplonglong'] = codegen_common.LongLongTestSkipQ



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
%(skiplonglong)sclass aall_operator_%(typelabel)s(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('%(typecode)s', [%(testdata)s]*10)

		# For bytes types, we need a non-array data type.
		if '%(typelabel)s' == 'bytes':
			self.data = bytes(self.data)


	########################################################
	def test_operator_01_eq(self):
		"""Test eq  - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_eq, self.data, %(eq_true1)s)
		self.assertTrue(result)
		result = arrayfunc.aall(arrayfunc.aops.af_eq, self.data, %(eq_false1)s)
		self.assertFalse(result)

	########################################################
	def test_operator_02_gt(self):
		"""Test gt  - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_gt, self.data, %(gt_true1)s)
		self.assertTrue(result)
		result = arrayfunc.aall(arrayfunc.aops.af_gt, self.data, %(gt_false1)s)
		self.assertFalse(result)

	########################################################
	def test_operator_03_gte(self):
		"""Test gte  - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_gte, self.data, %(gte_true1)s)
		self.assertTrue(result)
		result = arrayfunc.aall(arrayfunc.aops.af_gte, self.data, %(gte_true2)s)
		self.assertTrue(result)
		result = arrayfunc.aall(arrayfunc.aops.af_gte, self.data, %(gte_false1)s)
		self.assertFalse(result)

	########################################################
	def test_operator_04_lt(self):
		"""Test lt  - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_lt, self.data, %(lt_true1)s)
		self.assertTrue(result)
		result = arrayfunc.aall(arrayfunc.aops.af_lt, self.data, %(lt_false1)s)
		self.assertFalse(result)

	########################################################
	def test_operator_05_lte(self):
		"""Test lte  - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_lte, self.data, %(lte_true1)s)
		self.assertTrue(result)
		result = arrayfunc.aall(arrayfunc.aops.af_lte, self.data, %(lte_true2)s)
		self.assertTrue(result)
		result = arrayfunc.aall(arrayfunc.aops.af_lte, self.data, %(lte_false1)s)
		self.assertFalse(result)

	########################################################
	def test_operator_06_ne(self):
		"""Test ne  - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_ne, self.data, %(ne_true1)s)
		self.assertTrue(result)
		result = arrayfunc.aall(arrayfunc.aops.af_ne, self.data, %(ne_false1)s)
		self.assertFalse(result)

##############################################################################

'''

# ==============================================================================

# The basic template for testing parameters.
param_template = '''
##############################################################################
%(skiplonglong)sclass aall_parameter_%(typelabel)s(unittest.TestCase):
	"""Test for correct parameters.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('%(typecode)s', [%(testdata)s]*10)
		self.dataempty = array.array('%(typecode)s')

		# For bytes types, we need a non-array data type.
		if '%(typelabel)s' == 'bytes':
			self.data = bytes(self.data)
			self.dataempty = bytes(self.dataempty)


	########################################################
	def test_param_01_no_params_01(self):
		"""Test exception when no parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()

	########################################################
	def test_param_02_one_params(self):
		"""Test exception when one parameter passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(arrayfunc.aops.af_eq)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()

	########################################################
	def test_param_03_two_params(self):
		"""Test exception when two parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(arrayfunc.aops.af_eq, self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all()

	########################################################
	def test_param_04_five_params(self):
		"""Test exception when five parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(arrayfunc.aops.af_eq, self.data, %(testdata)s, 99, 99)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1, 2, 3, 4], 99)


	########################################################
	def test_param_05_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(arrayfunc.aops.af_eq, self.data, %(testdata)s, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all([1,2,3], xx=2)

	########################################################
	def test_param_06_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(arrayfunc.aops.af_eq, self.data, %(testdata)s, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)

	########################################################
	def test_param_07_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.aall(-1, self.data, %(testdata)s)


	########################################################
	def test_param_08_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall('a', self.data, %(testdata)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)

	########################################################
	def test_param_09_invalid_array_param_value(self):
		"""Test exception with invalid array parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(arrayfunc.aops.af_eq, 99, %(testdata)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)

	########################################################
	def test_param_10_invalid_array_param_length(self):
		"""Test exception with invalid array parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.aall(arrayfunc.aops.af_eq, self.dataempty, %(testdata)s)


	########################################################
	def test_param_11_invalid_array_param_type(self):
		"""Test exception with invalid compare parameter type  - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(arrayfunc.aops.af_eq, self.data, %(paramdata1)s)
		with self.assertRaises(TypeError):
			result = arrayfunc.aall(arrayfunc.aops.af_eq, self.data, %(paramdata2)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = all(1)


##############################################################################

'''
# ==============================================================================


# The basic template for testing parameter overflow.
overflow_template = '''
##############################################################################
%(skiplonglong)sclass aall_overflow_%(typelabel)s(unittest.TestCase):
	"""Test for parameter overflow.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('%(typecode)s', [%(testdata)s]*10)
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
			result = arrayfunc.aall(arrayfunc.aops.af_eq, self.data, self.MinVal %(overflowdec)s)

	########################################################
%(skipmaxoverflow)s	def test_overflow_02_max(self):
		"""Test parameter overflow max  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall(arrayfunc.aops.af_eq, self.data, self.Maxval %(overflowinc)s)

	########################################################
	def test_overflow_03_ok(self):
		"""Test no overflow. These should not overflow  - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_eq, self.data, self.MinVal)
		result = arrayfunc.aall(arrayfunc.aops.af_eq, self.data, self.Maxval)

##############################################################################

'''

# ==============================================================================

# The template for testing floating point nan, inf, -inf.
nan_template = '''
##############################################################################
class aall_nan_test%(seq)s_%(typelabel)s(unittest.TestCase):
	"""Test for operator function with floating point nan inf, and -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data_nan = array.array('%(typecode)s', [float('nan')]*10)
		self.data_inf = array.array('%(typecode)s', [float('inf')]*10)
		self.data_ninf = array.array('%(typecode)s', [float('-inf')]*10)

		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min
		self.Maxval = arrayfunc.arraylimits.%(typecode)s_max

	########################################################
	def test_nan_val%(seq)s_01_eq(self):
		"""Test eq with nan and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_eq, self.data_nan, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('nan') == %(testval)s)

	########################################################
	def test_nan_val%(seq)s_02_eq(self):
		"""Test eq with inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_eq, self.data_inf, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('inf') == %(testval)s)

	########################################################
	def test_nan_val%(seq)s_03_eq(self):
		"""Test eq with -inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_eq, self.data_ninf, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(%(testval)s == float('-inf'))


	########################################################
	def test_nan_val%(seq)s_04_gt(self):
		"""Test gt with nan and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_gt, self.data_nan, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('nan') > %(testval)s)

	########################################################
	def test_nan_val%(seq)s_05_gt(self):
		"""Test gt with inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_gt, self.data_inf, %(testval)s)
		self.assertTrue(result)
		self.assertTrue(float('inf') > %(testval)s)

	########################################################
	def test_nan_val%(seq)s_06_gt(self):
		"""Test gt with -inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_gt, self.data_ninf, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('-inf') > %(testval)s)


	########################################################
	def test_nan_val%(seq)s_07_gte(self):
		"""Test gte with nan and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_gte, self.data_nan, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('nan') >= %(testval)s)

	########################################################
	def test_nan_val%(seq)s_08_gte(self):
		"""Test gte with inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_gte, self.data_inf, %(testval)s)
		self.assertTrue(result)
		self.assertTrue(float('inf') >= %(testval)s)

	########################################################
	def test_nan_val%(seq)s_09_gte(self):
		"""Test gte with -inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_gte, self.data_ninf, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('-inf') >= %(testval)s)


	########################################################
	def test_nan_val%(seq)s_10_lt(self):
		"""Test lt with nan and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_lt, self.data_nan, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('nan') < %(testval)s)

	########################################################
	def test_nan_val%(seq)s_11_lt(self):
		"""Test lt with inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_lt, self.data_inf, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('inf') < %(testval)s)

	########################################################
	def test_nan_val%(seq)s_12_lt(self):
		"""Test lt with -inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_lt, self.data_ninf, %(testval)s)
		self.assertTrue(result)
		self.assertTrue(float('-inf') < %(testval)s)


	########################################################
	def test_nan_val%(seq)s_13_lte(self):
		"""Test lte with nan and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_lte, self.data_nan, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('nan') <= %(testval)s)

	########################################################
	def test_nan_val%(seq)s_14_lte(self):
		"""Test lte with inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_lte, self.data_inf, %(testval)s)
		self.assertFalse(result)
		self.assertFalse(float('inf') <= %(testval)s)

	########################################################
	def test_nan_val%(seq)s_15_lte(self):
		"""Test lte with -inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_lte, self.data_ninf, %(testval)s)
		self.assertTrue(result)
		self.assertTrue(float('-inf') <= %(testval)s)


	########################################################
	def test_nan_val%(seq)s_16_ne(self):
		"""Test ne with nan and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_ne, self.data_nan, %(testval)s)
		self.assertTrue(result)
		self.assertTrue(float('nan') != %(testval)s)

	########################################################
	def test_nan_val%(seq)s_17_ne(self):
		"""Test ne with inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_ne, self.data_inf, %(testval)s)
		self.assertTrue(result)
		self.assertTrue(float('inf') != %(testval)s)

	########################################################
	def test_nan_val%(seq)s_18_ne(self):
		"""Test ne with -inf and data %(testval)s - Array code %(typelabel)s.
		"""
		result = arrayfunc.aall(arrayfunc.aops.af_ne, self.data_ninf, %(testval)s)
		self.assertTrue(result)
		self.assertTrue(float('-inf') != %(testval)s)

##############################################################################

'''

# ==============================================================================


# The basic template for testing floating point parameters with nan, inf, -inf.
nanparam_template = '''
##############################################################################
class aall_nanparam_%(typelabel)s(unittest.TestCase):
	"""Test for float parameter errors with nan, inf, -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('%(typecode)s', [100.0]*10)


	########################################################
	def test_nanparam_01_nan(self):
		"""Test parameter nan  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall(arrayfunc.aops.af_eq, self.data, float('nan'))

	########################################################
	def test_nanparam_02_inf(self):
		"""Test parameter inf  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall(arrayfunc.aops.af_eq, self.data, float('inf'))

	########################################################
	def test_nanparam_03_ninf(self):
		"""Test parameter negative inf  - Array code %(typelabel)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.aall(arrayfunc.aops.af_eq, self.data, float('-inf'))


##############################################################################

'''

# ==============================================================================


endtemplate = """
##############################################################################
if __name__ == '__main__':
    unittest.main()

##############################################################################
"""

# ==============================================================================


# Data for the copyright header files.
headerdate = codegen_common.FormatHeaderData('test_aall', '20-May-2014', 'aall')

with open('test_aall.py', 'w') as f:
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

	f.write(endtemplate)


