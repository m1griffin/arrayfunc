#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for count.
# Language: Python 3.4
# Date:     06-Jun-2014
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

signedtestdata = {'initval' : 0, 'zeroparam' : 0, 'largestart' : 10,
			'negstart' : -10, 'smallstep' : 1, 'oddstep' : 7, 'negstep' : -1,
			'fractionalstep' : 1, 'stepone' : 1, 'invalidstep' : "'a'",
			'invalidtype' : "'a'", 'maxsteptypecode' : ''}

unsignedtestdata = {'initval' : 0, 'zeroparam' : 0, 'largestart' : 10,
			'negstart' : 10, 'smallstep' : 1, 'oddstep' : 7, 'negstep' : -1,
			'fractionalstep' : 1, 'stepone' : 1, 'invalidstep' : "'a'",
			'invalidtype' : "'a'", 'maxsteptypecode' : ''}

floattestdata = {'initval' : 0.0, 'zeroparam' : 0.0, 'largestart' : 10.0,
			'negstart' : -10.0, 'smallstep' : 1.0, 'oddstep' : 7.0, 'negstep' : -1.0,
			'fractionalstep' : 0.1, 'stepone' : 1.0, 'invalidstep' : "'a'",
			'invalidtype' : "'a'", 'maxsteptypecode' : ''}

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

testdata['b']['maxsteptypecode'] = 'b'
testdata['B']['maxsteptypecode'] = 'b'
testdata['h']['maxsteptypecode'] = 'h'
testdata['H']['maxsteptypecode'] = 'h'
testdata['i']['maxsteptypecode'] = 'i'
testdata['I']['maxsteptypecode'] = 'i'
testdata['l']['maxsteptypecode'] = 'l'
testdata['L']['maxsteptypecode'] = 'l'
testdata['q']['maxsteptypecode'] = 'q'
testdata['Q']['maxsteptypecode'] = 'q'
testdata['f']['maxsteptypecode'] = 'f'
testdata['d']['maxsteptypecode'] = 'd'


# ==============================================================================

op_template = '''
##############################################################################
class count_%(typelabel)s(unittest.TestCase):
	"""Test for basic count function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = '%(typecode)s'

		self.data = array.array(self.TypeCode, itertools.repeat(%(initval)s, 512))

		self.MaxVal = arrayfunc.arraylimits.%(typecode)s_max
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min

		self.zerodata = array.array(self.TypeCode, [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.%(maxsteptypecode)s_max
		self.MaxStepData = array.array(self.TypeCode, itertools.repeat(%(initval)s, 6))


		# For bytes types, we need a non-array data type.
		if '%(typelabel)s' == 'bytes':
			self.data = bytes(self.data)
			self.zerodata = bytes(self.zerodata)
			self.MaxStepData = bytes(self.MaxStepData)


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
				val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				val = (val - (self.MinVal - 1)) + self.MaxVal

		return seq


	########################################################
	def test_count_01(self):
		"""Test count in array code  %(typelabel)s - start from 0, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, %(zeroparam)s)
		self.assertEqual(list(self.data), self.PyCount(self.data, %(zeroparam)s, %(smallstep)s))


	########################################################
	def test_count_02(self):
		"""Test count in array code  %(typelabel)s - start from 10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, %(largestart)s)
		self.assertEqual(list(self.data), self.PyCount(self.data, %(largestart)s, %(smallstep)s))


	########################################################
	def test_count_03(self):
		"""Test count in array code  %(typelabel)s - start from 0, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, %(zeroparam)s, %(oddstep)s)
		self.assertEqual(list(self.data), self.PyCount(self.data, %(zeroparam)s, %(oddstep)s))


	########################################################
	def test_count_04(self):
		"""Test count in array code  %(typelabel)s - start from 10, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, %(largestart)s, %(oddstep)s)
		self.assertEqual(list(self.data), self.PyCount(self.data, %(largestart)s, %(oddstep)s))


	########################################################
	def test_count_05(self):
		"""Test count in array code  %(typelabel)s - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.zerodata, %(zeroparam)s)


	########################################################
	def test_count_06(self):
		"""Test count in array code  %(typelabel)s - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_07(self):
		"""Test count in array code  %(typelabel)s - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, %(zeroparam)s, %(smallstep)s, %(smallstep)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_08(self):
		"""Test count in array code  %(typelabel)s - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, %(zeroparam)s, %(smallstep)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_09(self):
		"""Test count in array code  %(typelabel)s - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, %(invalidtype)s, %(smallstep)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_10(self):
		"""Test count in array code  %(typelabel)s - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, %(zeroparam)s, %(invalidstep)s)


	########################################################
	def test_count_11(self):
		"""Test count in array code  %(typelabel)s - Step is maximum size.
		"""
		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, %(zeroparam)s, self.MaxStep)
		# Float overflow behaviour seems to be unclear, so we test for it differently.
		if '%(typecode)s' in ('f', 'd'):
			self.assertTrue(float('inf') in self.MaxStepData)
		else:
			self.assertEqual(list(self.MaxStepData), self.PyCount(self.MaxStepData, %(zeroparam)s, self.MaxStep))


	########################################################
	def test_count_12(self):
		"""Test count in array code  %(typelabel)s - start from 10, down by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, %(largestart)s, %(negstep)s)
		self.assertEqual(list(self.data), self.PyCount(self.data, %(largestart)s, %(negstep)s))


'''

op_template_signed = '''
	########################################################
	# Signed and float only.
	def test_count_13(self):
		"""Test count in array code  %(typelabel)s - start from -10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.count(self.data, %(negstart)s)
		self.assertEqual(list(self.data), self.PyCount(self.data, %(negstart)s, %(smallstep)s))

'''


op_template_float = '''
	########################################################
	# Floating point only.
	def test_count_14(self):
		"""Test count in array code  %(typelabel)s - start from 0, count up by a small increment.
		"""
		arrayfunc.count(self.data, %(zeroparam)s, %(fractionalstep)s)
		for x,y in zip(self.data, self.PyCount(self.data, %(zeroparam)s, %(fractionalstep)s)):
			self.assertAlmostEqual(x, y, delta=0.01)


	########################################################
	# Floating point only.
	def test_count_15(self):
		"""Test count in array code  %(typelabel)s - Invalid param nan for start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, float('nan'), 1.0)


	########################################################
	# Floating point only.
	def test_count_16(self):
		"""Test count in array code  %(typelabel)s - Invalid param inf for start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, float('inf'), 1.0)


	########################################################
	# Floating point only.
	def test_count_17(self):
		"""Test count in array code  %(typelabel)s - Invalid param -inf for start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, float('-inf'), 1.0)


	########################################################
	# Floating point only.
	def test_count_18(self):
		"""Test count in array code  %(typelabel)s - Invalid param nan for step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0.0, float('nan'))


	########################################################
	# Floating point only.
	def test_count_19(self):
		"""Test count in array code  %(typelabel)s - Invalid param inf for step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0.0, float('inf'))


	########################################################
	# Floating point only.
	def test_count_20(self):
		"""Test count in array code  %(typelabel)s - Invalid param -inf for step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0.0, float('-inf'))

'''

endclass = """
##############################################################################


"""


# ==============================================================================

# Data for the copyright header files.
headerdate = codegen_common.FormatHeaderData('test_count', '05-Jun-2014', 'count')

with open('test_count.py', 'w') as f:
	# The copyright header.
	f.write(codegen_common.HeaderTemplate % headerdate)

	# Output the generated code for basic operator tests.
	for funtypes in codegen_common.arraycodes:

		testvalues = {'typecode' : funtypes}
		testvalues['typelabel'] = funtypes
		testvalues.update(testdata[funtypes])

		f.write(op_template % testvalues)
		if funtypes in codegen_common.signedint or funtypes in codegen_common.floatarrays:
			f.write(op_template_signed % testvalues)
		if funtypes in codegen_common.floatarrays:
			f.write(op_template_float % testvalues)
		f.write(endclass)


	# Do the tests for bytes.
	testvalues = {'typecode' : 'B'}
	testvalues['typelabel'] = 'bytes'
	testvalues.update(testdata['B'])
	f.write(op_template % testvalues)


	f.write(codegen_common.testendtemplate % 'count')

