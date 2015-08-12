#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for cycle.
# Language: Python 3.4
# Date:     08-Jun-2014
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
			'negstart' : -10, 'startdown' : 125, 'stopval' : 100,
			'smallstep' : 1, 'oddstep' : 7, 'negstep' : -1,
			'fractionalstep' : 1, 'stepone' : 1, 'invalidtype' : "'a'", 'skiplonglong' : ''}

unsignedtestdata = {'initval' : 0, 'zeroparam' : 0, 'largestart' : 10,
			'negstart' : 10, 'startdown' : 125, 'stopval' : 100,
			'smallstep' : 1, 'oddstep' : 7, 'negstep' : 1,
			'fractionalstep' : 1, 'stepone' : 1, 'invalidtype' : "'a'", 'skiplonglong' : ''}


floattestdata = {'initval' : 0.0, 'zeroparam' : 0.0, 'largestart' : 10.0,
			'negstart' : -10.0, 'stopval' : 100.0, 'startdown' : 125.0,
			'smallstep' : 1.0, 'oddstep' : 7.0, 'negstep' : -1.0,
			'fractionalstep' : 0.1, 'stepone' : 1.0, 'invalidtype' : "'a'", 'skiplonglong' : ''}


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


# Patch in the cases for 'q' and 'Q' arrays.
testdata['q']['skiplonglong'] = codegen_common.LongLongTestSkipq
testdata['Q']['skiplonglong'] = codegen_common.LongLongTestSkipQ


# ==============================================================================

op_template = '''
##############################################################################
%(skiplonglong)sclass cycle_%(typelabel)s(unittest.TestCase):
	"""Test for basic cycle function.
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


		# For bytes types, we need a non-array data type.
		if '%(typelabel)s' == 'bytes':
			self.data = bytes(self.data)
			self.zerodata = bytes(self.zerodata)


	########################################################
	def PyCycle(self, data, start, stop, step):
		"""This should produce a Python equivalent to count for unit testing.
		"""
		seq = []
		maxval = self.MaxVal
		minval = self.MinVal
		val = start
		step = abs(step)

		if start <= stop:
			for x in range(len(data)):
				seq.append(val)
				val = val + step
				if (val > maxval) or (val > stop):
					val = start
		else:
			for x in range(len(data)):
				seq.append(val)
				val = val - step
				if (val < minval) or (val < stop):
					val = start

		return seq



	########################################################
	def test_cycle_01(self):
		"""Test cycle in array code  %(typelabel)s - start from 0, count up by one, and proceed to end without limit.
		"""
		arrayfunc.cycle(self.data, %(zeroparam)s, %(stopval)s)
		self.assertEqual(list(self.data), self.PyCycle(self.data, %(zeroparam)s, %(stopval)s, %(stepone)s))


	########################################################
	def test_cycle_02(self):
		"""Test cycle in array code  %(typelabel)s - start from 10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.cycle(self.data, %(largestart)s, %(stopval)s)
		self.assertEqual(list(self.data), self.PyCycle(self.data, %(largestart)s, %(stopval)s, %(stepone)s))


	########################################################
	def test_cycle_03(self):
		"""Test cycle in array code  %(typelabel)s - start from 0, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.cycle(self.data, %(zeroparam)s, %(stopval)s, %(oddstep)s)
		self.assertEqual(list(self.data), self.PyCycle(self.data, %(zeroparam)s, %(stopval)s, %(oddstep)s))


	########################################################
	def test_cycle_04(self):
		"""Test cycle in array code  %(typelabel)s - start from 10, count up by 7, and proceed to end without limit.
		"""
		arrayfunc.cycle(self.data, %(largestart)s, %(stopval)s, %(oddstep)s)
		self.assertEqual(list(self.data), self.PyCycle(self.data, %(largestart)s, %(stopval)s, %(oddstep)s))


	########################################################
	def test_cycle_05(self):
		"""Test cycle in array code  %(typelabel)s - start from 10, count down by 1, and proceed to end without limit.
		"""
		arrayfunc.cycle(self.data, %(largestart)s, %(startdown)s)
		self.assertEqual(list(self.data), self.PyCycle(self.data, %(largestart)s, %(startdown)s, %(stepone)s))


	########################################################
	def test_cycle_06(self):
		"""Test cycle in array code  %(typelabel)s - start from 10, count down by 7, and proceed to end without limit.
		"""
		arrayfunc.cycle(self.data, %(startdown)s, %(largestart)s, %(oddstep)s)
		self.assertEqual(list(self.data), self.PyCycle(self.data, %(startdown)s, %(largestart)s, %(oddstep)s))


	########################################################
	def test_cycle_07(self):
		"""Test cycle in array code  %(typelabel)s - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.cycle(self.zerodata, %(zeroparam)s, %(stopval)s, %(stopval)s)


	########################################################
	def test_cycle_08(self):
		"""Test cycle in array code  %(typelabel)s - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle()

	########################################################
	def test_cycle_09(self):
		"""Test cycle in array code  %(typelabel)s - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data, %(zeroparam)s, %(stopval)s, %(smallstep)s, %(smallstep)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle([1, 2, 3, 4], [1, 2, 3, 4])

	########################################################
	def test_cycle_10(self):
		"""Test cycle in array code  %(typelabel)s - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, %(zeroparam)s, %(stopval)s, %(smallstep)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)

	########################################################
	def test_cycle_11(self):
		"""Test cycle in array code  %(typelabel)s - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, %(invalidtype)s, %(stopval)s, %(smallstep)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)


'''

op_template_signed = '''
	########################################################
	def test_cycle_13(self):
		"""Test cycle in array code  %(typelabel)s - start from 10, count down by 1 using a negative step, and proceed to end without limit.
		"""
		arrayfunc.cycle(self.data, %(startdown)s, %(largestart)s, %(negstep)s)
		self.assertEqual(list(self.data), self.PyCycle(self.data, %(startdown)s, %(largestart)s, %(negstep)s))


	########################################################
	# Signed and float only.
	def test_cycle_14(self):
		"""Test cycle in array code  %(typelabel)s - start from -10, count up by one, and proceed to end without limit.
		"""
		arrayfunc.cycle(self.data, %(negstart)s, %(stopval)s, %(smallstep)s)
		self.assertEqual(list(self.data), self.PyCycle(self.data, %(negstart)s, %(stopval)s, %(smallstep)s))


	########################################################
	# Signed and float only.
	def test_cycle_15(self):
		"""Test cycle in array code  %(typelabel)s - start from 10, down up by one, and proceed to end without limit.
		"""
		arrayfunc.cycle(self.data, %(largestart)s, %(stopval)s, %(negstep)s)
		self.assertEqual(list(self.data), self.PyCycle(self.data, %(largestart)s, %(stopval)s, %(negstep)s))


'''


op_template_float = '''
	########################################################
	# Floating point only.
	def test_cycle_16(self):
		"""Test cycle in array code  %(typelabel)s - start from 0, count up by a small increment.
		"""
		arrayfunc.cycle(self.data, %(zeroparam)s, %(stopval)s, %(fractionalstep)s)
		for x,y in zip(self.data, self.PyCycle(self.data, %(zeroparam)s, %(stopval)s, %(fractionalstep)s)):
			self.assertAlmostEqual(x, y, delta=0.01)


	########################################################
	# Floating point only.
	def test_cycle_17(self):
		"""Test cycle in array code  %(typelabel)s - Invalid param nan for start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, float('nan'), 1000.0, 1.0)


	########################################################
	# Floating point only.
	def test_cycle_18(self):
		"""Test cycle in array code  %(typelabel)s - Invalid param inf for start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, float('inf'), 1000.0, 1.0)


	########################################################
	# Floating point only.
	def test_cycle_19(self):
		"""Test cycle in array code  %(typelabel)s - Invalid param -inf for start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, float('-inf'), 1000.0, 1.0)


	########################################################
	# Floating point only.
	def test_cycle_20(self):
		"""Test cycle in array code  %(typelabel)s - Invalid param nan for stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0.0, float('nan'), 1.0)


	########################################################
	# Floating point only.
	def test_cycle_21(self):
		"""Test cycle in array code  %(typelabel)s - Invalid param inf for stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0.0, float('inf'), 1.0)


	########################################################
	# Floating point only.
	def test_cycle_22(self):
		"""Test cycle in array code  %(typelabel)s - Invalid param -inf for stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0.0, float('-inf'), 1.0)


	########################################################
	# Floating point only.
	def test_cycle_23(self):
		"""Test cycle in array code  %(typelabel)s - Invalid param nan for step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0.0, 1000.0, float('nan'))


	########################################################
	# Floating point only.
	def test_cycle_24(self):
		"""Test cycle in array code  %(typelabel)s - Invalid param inf for step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0.0, 1000.0, float('inf'))


	########################################################
	# Floating point only.
	def test_cycle_25(self):
		"""Test cycle in array code  %(typelabel)s - Invalid param -inf for step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0.0, 1000.0, float('-inf'))


'''

endclass = """
##############################################################################


"""

# ==============================================================================

endtemplate = """
##############################################################################
if __name__ == '__main__':
    unittest.main()

##############################################################################
"""


# ==============================================================================

# Data for the copyright header files.
headerdate = codegen_common.FormatHeaderData('test_cycle', '10-Jun-2014', 'cycle')

with open('test_cycle.py', 'w') as f:
	# The copyright header.
	f.write(codegen_common.HeaderTemplate % headerdate)

	# Output the generated code for basic operator tests.
	for funtypes in codegen_common.arraycodes:

		testvalues = {'typecode' : funtypes}
		testvalues['typelabel'] = funtypes
		testvalues.update(testdata[funtypes])

		opdata = op_template % testvalues
		f.write(opdata)

		if funtypes in codegen_common.signedint or funtypes in codegen_common.floatarrays:
			opsigned = op_template_signed % testvalues
			f.write(opsigned)

		if funtypes in codegen_common.floatarrays:
			opfloat = op_template_float % testvalues
			f.write(opfloat)

		f.write(endclass)



	# Do the tests for bytes.
	testvalues = testdata['B']
	testvalues['typecode'] = 'B'
	testvalues['typelabel'] = 'bytes'
	f.write(op_template % testvalues)


	f.write(endtemplate)

