#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for repeat.
# Language: Python 3.4
# Date:     11-Jun-2014
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

signedtestdata = {'initval' : 5, 'zeroparam' : 0, 
		'invalidtype1' : "'a'", 'invalidtype2' : 10.0, 
		'overflow' : 'self.MaxVal + 1', 'underflow' : 'self.MinVal - 1',
		'skipminoverflow' : '', 'skipmaxoverflow' : ''}


unsignedtestdata = {'initval' : 5, 'zeroparam' : 0, 
		'invalidtype1' : "'a'", 'invalidtype2' : 10.0, 
		'overflow' : 'self.MaxVal + 1', 'underflow' : 'self.MinVal - 1',
		'skipminoverflow' : '', 'skipmaxoverflow' : ''}


floattestdata = {'initval' : 5.0, 'zeroparam' : 0.0, 
		'invalidtype1' : "'a'", 'invalidtype2' : 10, 
		'overflow' : 'self.MaxVal * 1.1', 'underflow' : 'self.MinVal * 1.1',
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


# ==============================================================================

op_template = '''
##############################################################################
class repeat_%(typelabel)s(unittest.TestCase):
	"""Test for basic repeat function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = '%(typecode)s'

		self.data = array.array(self.TypeCode, itertools.repeat(%(initval)s, 512))

		self.MaxVal = arrayfunc.arraylimits.%(typecode)s_max
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min


		# For bytes types, we need a non-array data type.
		if '%(typelabel)s' == 'bytes':
			self.data = bytes(self.data)


	########################################################
	def test_repeat_01(self):
		"""Test repeat in array code  %(typelabel)s - Test for zero.
		"""
		arrayfunc.repeat(self.data, %(zeroparam)s)
		self.assertEqual(list(self.data), [%(zeroparam)s]*len(self.data))


	########################################################
	def test_repeat_02(self):
		"""Test repeat in array code  %(typelabel)s - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)
		self.assertEqual(list(self.data), [self.MaxVal]*len(self.data))


	########################################################
	def test_repeat_03(self):
		"""Test repeat in array code  %(typelabel)s - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)
		self.assertEqual(list(self.data), [self.MinVal]*len(self.data))


	########################################################
	def test_repeat_04(self):
		"""Test repeat in array code  %(typelabel)s - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, %(invalidtype1)s)


	########################################################
	def test_repeat_05(self):
		"""Test repeat in array code  %(typelabel)s - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, %(invalidtype2)s)


	########################################################
	def test_repeat_06(self):
		"""Test repeat in array code  %(typelabel)s - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(%(invalidtype1)s, %(zeroparam)s)


	########################################################
	def test_repeat_07(self):
		"""Test repeat in array code  %(typelabel)s - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_08(self):
		"""Test repeat in array code  %(typelabel)s - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_09(self):
		"""Test repeat in array code  %(typelabel)s - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, %(zeroparam)s, %(zeroparam)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)

'''

overflow_template = '''
	########################################################
%(skipmaxoverflow)s	def test_repeat_10(self):
		"""Test repeat in array code  %(typelabel)s - Test for parameter overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, %(overflow)s)


	########################################################
%(skipminoverflow)s	def test_repeat_11(self):
		"""Test repeat in array code  %(typelabel)s - Test for parameter underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, %(underflow)s)

'''


op_template_nan = '''
	########################################################
	# Floating point only.
	def test_repeat_12(self):
		"""Test repeat in array code  %(typelabel)s - Invalid param nan for value.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, float('nan'))


	########################################################
	# Floating point only.
	def test_repeat_13(self):
		"""Test repeat in array code  %(typelabel)s - Invalid param inf for value.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, float('inf'))


	########################################################
	# Floating point only.
	def test_repeat_14(self):
		"""Test repeat in array code  %(typelabel)s - Invalid param -inf for value.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, float('-inf'))


'''

endclass = """
##############################################################################


"""


# ==============================================================================

# Data for the copyright header files.
headerdate = codegen_common.FormatHeaderData('test_repeat', '11-Jun-2014', 'repeat')

with open('test_repeat.py', 'w') as f:
	# The copyright header.
	f.write(codegen_common.HeaderTemplate % headerdate)

	# Output the generated code for basic operator tests.
	for funtypes in codegen_common.arraycodes:

		testvalues = {'typecode' : funtypes}
		testvalues['typelabel'] = funtypes
		testvalues.update(testdata[funtypes])

		f.write(op_template % testvalues)

		# Not all array types can overflow.
		if funtypes not in 'LQ':
			f.write(overflow_template % testvalues)

		# Test for floating point nan, inf, -inf
		if funtypes in codegen_common.floatarrays:
			opfloat = op_template_nan % testvalues
			f.write(opfloat)

		f.write(endclass)


	# Do the tests for bytes.
	testvalues = testdata['B']
	testvalues['typecode'] = 'B'
	testvalues['typelabel'] = 'bytes'
	f.write(op_template % testvalues)


	f.write(codegen_common.testendtemplate % 'repeat')

