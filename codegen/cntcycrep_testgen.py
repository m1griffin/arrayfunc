#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for count, cycle, repeat.
# Language: Python 3.6
# Date:     21-May-2014
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

# ==============================================================================

import itertools
import codegen_common

# ==============================================================================


# ==============================================================================

count_param_template = '''
##############################################################################
class count_params_%(typecode)s(unittest.TestCase):
	"""Test for count parameter function.
	count_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('%(typecode)s', [0] * self.ArrayLength)
		self.emptydata = array.array('%(typecode)s', [])


	########################################################
	def test_count_param_01(self):
		"""Test count in array code  %(typecode)s - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0%(zeropad)s)


	########################################################
	def test_count_param_02(self):
		"""Test count in array code  %(typecode)s - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data)


	########################################################
	def test_count_param_03(self):
		"""Test count in array code  %(typecode)s - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0%(zeropad)s, 1%(zeropad)s, 1%(zeropad)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count(10, 12, 20)


	########################################################
	def test_count_param_04(self):
		"""Test count in array code  %(typecode)s - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(1, 0%(zeropad)s, 1%(zeropad)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')

	########################################################
	def test_count_param_05(self):
		"""Test count in array code  %(typecode)s - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 'a', 1%(zeropad)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.count('a')


	########################################################
	def test_count_param_06(self):
		"""Test count in array code  %(typecode)s - Invalid param type for step.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.count(self.data, 0%(zeropad)s, 'a')



##############################################################################


'''

# ==============================================================================

count_op_template = '''
##############################################################################
class count_op_%(typecode)s(unittest.TestCase):
	"""Test for basic count function.
	count_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = '%(typecode)s'

		self.ArrayLength = 512

		self.data = array.array('%(typecode)s', itertools.repeat(0%(zeropad)s, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.%(typecode)s_max
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min

		self.zerodata = array.array('%(typecode)s', [])

		# This is the largest step allowed for this array type.
		self.MaxStep = arrayfunc.arraylimits.%(maxsteptypecode)s_max
		self.MaxStepData = array.array('%(typecode)s', itertools.repeat(0%(zeropad)s, 6))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	def test_count_op_01(self):
		"""Test count in array code  %(typecode)s - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0%(zeropad)s, 1%(zeropad)s)

		arrayfunc.count(self.data, 0%(zeropad)s)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_02(self):
		"""Test count in array code  %(typecode)s - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10%(zeropad)s, 1%(zeropad)s)

		arrayfunc.count(self.data, 10%(zeropad)s)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_03(self):
		"""Test count in array code  %(typecode)s - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 0%(zeropad)s, 7%(zeropad)s)

		arrayfunc.count(self.data, 0%(zeropad)s, 7%(zeropad)s)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_04(self):
		"""Test count in array code  %(typecode)s - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10%(zeropad)s, 7%(zeropad)s)

		arrayfunc.count(self.data, 10%(zeropad)s, 7%(zeropad)s)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_count_op_05(self):
		"""Test count in array code  %(typecode)s - Step is maximum size.
		"""
		expected = self.PyCount(self.MaxStepData, 0%(zeropad)s, self.MaxStep)

		# We use a smaller array because we expect an overflow near the beginning.
		arrayfunc.count(self.MaxStepData, 0%(zeropad)s, self.MaxStep)


		for dataoutitem, expecteditem in zip(list(self.MaxStepData), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_op_06(self):
		"""Test count in array code  %(typecode)s - start from 10, down by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, 10%(zeropad)s, -1%(zeropad)s)

		arrayfunc.count(self.data, 10%(zeropad)s, -1%(zeropad)s)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

'''


# ==============================================================================

count_op_signed_template = '''
##############################################################################
class count_op_signed_%(typecode)s(unittest.TestCase):
	"""Test for basic count function for signed data.
	count_op_signed_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = '%(typecode)s'

		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.%(typecode)s_max
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min

		self.data = array.array('%(typecode)s', itertools.repeat(0%(zeropad)s, self.ArrayLength))


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq



	########################################################
	# Signed and float only.
	def test_count_op_signed_01(self):
		"""Test count in array code  %(typecode)s - start from -10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCount(self.data, -10%(zeropad)s, 1%(zeropad)s)

		arrayfunc.count(self.data, -10%(zeropad)s)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

'''


# ==============================================================================

count_nonfinite_template = '''
##############################################################################
class count_nonfinite_%(typecode)s(unittest.TestCase):
	"""Test for nonfinite count function.
	count_nonfinite_template
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = '%(typecode)s'

		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.%(typecode)s_max
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min

		self.data = array.array('%(typecode)s', [10] * self.ArrayLength)


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
				if (self.TypeCode == 'f') and val > self.MaxVal:
					val = math.inf
				elif (self.TypeCode == 'd') and val > self.MaxVal:
					pass
				else:
					val = (val - (self.MaxVal + 1)) + self.MinVal
			elif (step < 0) and (val < self.MinVal):
				if (self.TypeCode == 'f') and val < self.MinVal:
					val = -math.inf
				elif (self.TypeCode == 'd') and val < self.MinVal:
					pass
				else:
					val = (val - (self.MinVal - 1)) + self. MaxVal
		return seq


	########################################################
	def test_count_nonfinite_01(self):
		"""Test count in array code  %(typecode)s - Test for NaN for start.
		"""
		expected = self.PyCount(self.data, math.nan, 1.0)

		arrayfunc.count(self.data, math.nan, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_nonfinite_02(self):
		"""Test count in array code  %(typecode)s - Test for inf for start.
		"""
		expected = self.PyCount(self.data, math.inf, 1.0)

		arrayfunc.count(self.data, math.inf, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_nonfinite_03(self):
		"""Test count in array code  %(typecode)s - Test for -inf for start.
		"""
		expected = self.PyCount(self.data, -math.inf, 1.0)

		arrayfunc.count(self.data, -math.inf, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_nonfinite_04(self):
		"""Test count in array code  %(typecode)s - Test for nan for step.
		"""
		expected = self.PyCount(self.data, 0.0, math.nan)

		arrayfunc.count(self.data, 0.0, math.nan)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_nonfinite_05(self):
		"""Test count in array code  %(typecode)s - Test for inf for step.
		"""
		expected = self.PyCount(self.data, 0.0, math.inf)

		arrayfunc.count(self.data, 0.0, math.inf)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_count_nonfinite_06(self):
		"""Test count in array code  %(typecode)s - Test for -inf for step.
		"""
		expected = self.PyCount(self.data, 0.0, -math.inf)

		arrayfunc.count(self.data, 0.0, -math.inf)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	# This is not really a non-finite test, but it is convenient to put
	# it here as it is for floating point only.
	def test_count_nonfinite_07(self):
		"""Test count in array code  %(typecode)s - start from 0, count up by a small increment.
		"""
		expected = self.PyCount(self.data, 0.0, 0.1)

		arrayfunc.count(self.data, 0.0, 0.1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

'''

# ==============================================================================

count_overflow_template = '''
##############################################################################
class count_overflow_%(typecode)s(unittest.TestCase):
	"""Test for overflow count function.
	count_overflow_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.%(typecode)s_max
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min


		# Create the overflow value for this data type.
		if '%(typecode)s' in ('f', 'd'):
			self.Overflow = self.MaxVal * 1.1
			self.Underflow = self.MinVal * 1.1
			self.StepOverflow = arrayfunc.arraylimits.%(maxsteptypecode)s_max * 1.1
			self.StepUnderflow = arrayfunc.arraylimits.%(maxsteptypecode)s_min * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1
			self.StepOverflow = arrayfunc.arraylimits.%(maxsteptypecode)s_max + 1
			self.StepUnderflow = arrayfunc.arraylimits.%(maxsteptypecode)s_min - 1


		self.data = array.array('%(typecode)s', [0] * self.ArrayLength)


	########################################################
	def test_count_ovfl_01(self):
		"""Test count overflow operation in array code  %(typecode)s - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Overflow, 1%(zeropad)s)


	########################################################
	def test_count_ovfl_02(self):
		"""Test count overflow operation in array code  %(typecode)s - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0%(zeropad)s, self.StepOverflow)


	########################################################
	def test_count_ovfl_03(self):
		"""Test count overflow operation in array code  %(typecode)s - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, self.Underflow, -1%(zeropad)s)


	########################################################
	def test_count_ovfl_04(self):
		"""Test count overflow operation in array code  %(typecode)s - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.count(self.data, 0%(zeropad)s, self.StepUnderflow)


##############################################################################

'''


# ==============================================================================


# ==============================================================================

cycle_param_template = '''
##############################################################################
class cycle_param_%(typecode)s(unittest.TestCase):
	"""Test for basic cycle parameter tests.
	cycle_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = '%(typecode)s'

		self.data = array.array(self.TypeCode, itertools.repeat(0%(zeropad)s, 512))

		self.MaxVal = arrayfunc.arraylimits.%(typecode)s_max
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min

		self.zerodata = array.array(self.TypeCode, [])



	########################################################
	def test_cycle_param_01(self):
		"""Test cycle in array code  %(typecode)s - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.cycle(self.zerodata, 0%(zeropad)s, 100%(zeropad)s, 100%(zeropad)s)


	########################################################
	def test_cycle_param_02(self):
		"""Test cycle in array code  %(typecode)s - Missing start parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle()


	########################################################
	def test_cycle_param_03(self):
		"""Test cycle in array code  %(typecode)s - Too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(self.data, 0%(zeropad)s, 100%(zeropad)s, 1%(zeropad)s, 1%(zeropad)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle([1, 2, 3, 4], [1, 2, 3, 4])


	########################################################
	def test_cycle_param_04(self):
		"""Test cycle in array code  %(typecode)s - Invalid param type for array.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 0%(zeropad)s, 100%(zeropad)s, 1%(zeropad)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)


	########################################################
	def test_cycle_param_05(self):
		"""Test cycle in array code  %(typecode)s - Invalid param type for start.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.cycle(1, 'a', 100%(zeropad)s, 1%(zeropad)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.cycle(99)



##############################################################################


'''

# ==============================================================================

# ==============================================================================

cycle_op_template = '''
##############################################################################
class cycle_%(typecode)s(unittest.TestCase):
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = '%(typecode)s'

		self.ArrayLength = 512

		self.data = array.array(self.TypeCode, itertools.repeat(0%(zeropad)s, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.%(typecode)s_max
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min


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
		"""Test cycle in array code  %(typecode)s - start from 0, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0%(zeropad)s, 100%(zeropad)s, 1%(zeropad)s)

		arrayfunc.cycle(self.data, 0%(zeropad)s, 100%(zeropad)s)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_02(self):
		"""Test cycle in array code  %(typecode)s - start from 10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10%(zeropad)s, 100%(zeropad)s, 1%(zeropad)s)

		arrayfunc.cycle(self.data, 10%(zeropad)s, 100%(zeropad)s)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_03(self):
		"""Test cycle in array code  %(typecode)s - start from 0, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 0%(zeropad)s, 100%(zeropad)s, 7%(zeropad)s)

		arrayfunc.cycle(self.data, 0%(zeropad)s, 100%(zeropad)s, 7%(zeropad)s)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_04(self):
		"""Test cycle in array code  %(typecode)s - start from 10, count up by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10%(zeropad)s, 100%(zeropad)s, 7%(zeropad)s)

		arrayfunc.cycle(self.data, 10%(zeropad)s, 100%(zeropad)s, 7%(zeropad)s)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_05(self):
		"""Test cycle in array code  %(typecode)s - start from 10, count down by 1, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10%(zeropad)s, 125%(zeropad)s, 1%(zeropad)s)

		arrayfunc.cycle(self.data, 10%(zeropad)s, 125%(zeropad)s)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_06(self):
		"""Test cycle in array code  %(typecode)s - start from 10, count down by 7, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125%(zeropad)s, 10%(zeropad)s, 7%(zeropad)s)

		arrayfunc.cycle(self.data, 125%(zeropad)s, 10%(zeropad)s, 7%(zeropad)s)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)




##############################################################################

'''

# ==============================================================================

cycle_op_signed_template = '''
##############################################################################
class cycle_op_signed_%(typecode)s(unittest.TestCase):
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.TypeCode = '%(typecode)s'

		self.ArrayLength = 512

		self.data = array.array(self.TypeCode, itertools.repeat(0%(zeropad)s, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.%(typecode)s_max
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min


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
		"""Test cycle in array code  %(typecode)s - start from 10, count down by 1 using a negative step, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 125%(zeropad)s, 10%(zeropad)s, -1%(zeropad)s)

		arrayfunc.cycle(self.data, 125%(zeropad)s, 10%(zeropad)s, -1%(zeropad)s)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_op_signed_02(self):
		"""Test cycle in array code  %(typecode)s - start from -10, count up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, -10%(zeropad)s, 100%(zeropad)s, 1%(zeropad)s)

		arrayfunc.cycle(self.data, -10%(zeropad)s, 100%(zeropad)s, 1%(zeropad)s)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_op_signed_03(self):
		"""Test cycle in array code  %(typecode)s - start from 10, down up by one, and proceed to end without limit.
		"""
		expected = self.PyCycle(self.data, 10%(zeropad)s, 100%(zeropad)s, -1%(zeropad)s)

		arrayfunc.cycle(self.data, 10%(zeropad)s, 100%(zeropad)s, -1%(zeropad)s)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

'''

# ==============================================================================

cycle_nonfinite_template = '''
##############################################################################
class cycle_nonfinite_%(typecode)s(unittest.TestCase):
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.ArrayLength = 512

		self.TypeCode = '%(typecode)s'

		self.data = array.array(self.TypeCode, itertools.repeat(0.0, self.ArrayLength))

		self.MaxVal = arrayfunc.arraylimits.%(typecode)s_max
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min


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
		"""Test cycle in array code  %(typecode)s - Invalid param nan for start.
		"""
		expected = self.PyCycle(self.data, math.nan, 1000.0, 1.0)

		arrayfunc.cycle(self.data, math.nan, 1000.0, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_02(self):
		"""Test cycle in array code  %(typecode)s - Invalid param inf for start.
		"""
		expected = self.PyCycle(self.data, math.inf, 1000.0, 1.0)

		arrayfunc.cycle(self.data, math.inf, 1000.0, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_03(self):
		"""Test cycle in array code  %(typecode)s - Invalid param -inf for start.
		"""
		expected = self.PyCycle(self.data, -math.inf, 1000.0, 1.0)

		arrayfunc.cycle(self.data, -math.inf, 1000.0, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_04(self):
		"""Test cycle in array code  %(typecode)s - Invalid param nan for stop.
		"""
		expected = self.PyCycle(self.data, 0.0, math.nan, 1.0)

		arrayfunc.cycle(self.data, 0.0, math.nan, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_05(self):
		"""Test cycle in array code  %(typecode)s - Invalid param inf for stop.
		"""
		expected = self.PyCycle(self.data, 0.0, math.inf, 1.0)

		arrayfunc.cycle(self.data, 0.0, math.inf, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_06(self):
		"""Test cycle in array code  %(typecode)s - Invalid param -inf for stop.
		"""
		expected = self.PyCycle(self.data, 0.0, -math.inf, 1.0)

		arrayfunc.cycle(self.data, 0.0, -math.inf, 1.0)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_07(self):
		"""Test cycle in array code  %(typecode)s - Invalid param nan for step.
		"""
		expected = self.PyCycle(self.data, 0.0, 1000.0, math.nan)

		arrayfunc.cycle(self.data, 0.0, 1000.0, math.nan)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_08(self):
		"""Test cycle in array code  %(typecode)s - Invalid param inf for step.
		"""
		expected = self.PyCycle(self.data, 0.0, 1000.0, math.inf)

		arrayfunc.cycle(self.data, 0.0, 1000.0, math.inf)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_cycle_nonfinite_09(self):
		"""Test cycle in array code  %(typecode)s - Invalid param -inf for step.
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
		"""Test cycle in array code  %(typecode)s - start from 0, count up by a small increment.
		"""
		expected = self.PyCycle(self.data, 0.0, 100.0, 0.1)

		arrayfunc.cycle(self.data, 0.0, 100.0, 0.1)

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

'''


# ==============================================================================

# ==============================================================================


cycle_overflow_template = '''
##############################################################################
class cycle_overflow_%(typecode)s(unittest.TestCase):
	"""Test for overflow cycle function.
	cycle_overflow_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.%(typecode)s_max
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min


		# Create the overflow value for this data type.
		if '%(typecode)s' in ('f', 'd'):
			self.Overflow = self.MaxVal * 1.1
			self.Underflow = self.MinVal * 1.1
			self.StepOverflow = arrayfunc.arraylimits.%(typecode)s_max * 1.1
			self.StepUnderflow = arrayfunc.arraylimits.%(typecode)s_min * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1
			self.StepOverflow = arrayfunc.arraylimits.%(typecode)s_max + 1
			self.StepUnderflow = arrayfunc.arraylimits.%(typecode)s_min - 1


		self.data = array.array('%(typecode)s', [0] * self.ArrayLength)


	########################################################
	def test_cycle_ovfl_01(self):
		"""Test cycle overflow operation in array code  %(typecode)s - Test for overflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Overflow, 100%(zeropad)s, 1%(zeropad)s)


	########################################################
	def test_cycle_ovfl_02(self):
		"""Test cycle overflow operation in array code  %(typecode)s - Test for overflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100%(zeropad)s, self.Overflow, 1%(zeropad)s)


	########################################################
	def test_cycle_ovfl_03(self):
		"""Test cycle overflow operation in array code  %(typecode)s - Test for overflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0%(zeropad)s, 100%(zeropad)s, self.StepOverflow)


	########################################################
	def test_cycle_ovfl_04(self):
		"""Test cycle overflow operation in array code  %(typecode)s - Test for underflow in start.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, self.Underflow, 100%(zeropad)s, 1%(zeropad)s)


	########################################################
	def test_cycle_ovfl_05(self):
		"""Test cycle overflow operation in array code  %(typecode)s - Test for underflow in stop.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 100%(zeropad)s, self.Underflow, 1%(zeropad)s)


	########################################################
	def test_cycle_ovfl_06(self):
		"""Test cycle overflow operation in array code  %(typecode)s - Test for underflow in step.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.cycle(self.data, 0%(zeropad)s, 100%(zeropad)s, self.StepUnderflow)


##############################################################################

'''


# ==============================================================================

# ==============================================================================


repeat_param_template = '''
##############################################################################
class repeat_params_%(typecode)s(unittest.TestCase):
	"""Test for repeat parameter function.
	repeat_param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('%(typecode)s', [0] * self.ArrayLength)
		self.emptydata = array.array('%(typecode)s', [])



	########################################################
	def test_repeat_param_01(self):
		"""Test repeat in array code  %(typecode)s - Zero length array.
		"""
		with self.assertRaises(IndexError):
			arrayfunc.count(self.emptydata, 0%(zeropad)s)


	########################################################
	def test_repeat_param_02(self):
		"""Test repeat in array code  %(typecode)s - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 'a')


	########################################################
	def test_repeat_param_03(self):
		"""Test repeat in array code  %(typecode)s - Test for invalid repeat value type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 10%(invalidzeropad)s)


	########################################################
	def test_repeat_param_04(self):
		"""Test repeat in array code  %(typecode)s - Test for invalid array parameter type.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat('a', 0%(zeropad)s)


	########################################################
	def test_repeat_param_05(self):
		"""Test repeat in array code  %(typecode)s - Test for missing all parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_06(self):
		"""Test repeat in array code  %(typecode)s - Test for missing one parameter.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat()


	########################################################
	def test_repeat_param_07(self):
		"""Test repeat in array code  %(typecode)s - Test for too many parameters.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.repeat(self.data, 0%(zeropad)s, 0%(zeropad)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = itertools.repeat(0, 3, 3)



##############################################################################

'''

# ==============================================================================

repeat_op_template = '''
##############################################################################
class repeat_op_%(typecode)s(unittest.TestCase):
	"""Test for basic repeat function.
	repeat_op_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.ArrayLength = 512

		self.data = array.array('%(typecode)s', [10] * self.ArrayLength)

		self.MaxVal = arrayfunc.arraylimits.%(typecode)s_max
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min


	########################################################
	def test_repeat_op_01(self):
		"""Test repeat operation in array code  %(typecode)s - Test for zero.
		"""
		arrayfunc.repeat(self.data, 0%(zeropad)s)

		expected = [0%(zeropad)s] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_02(self):
		"""Test repeat operation in array code  %(typecode)s - Test for max value.
		"""
		arrayfunc.repeat(self.data, self.MaxVal)

		expected = [self.MaxVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_op_03(self):
		"""Test repeat operation in array code  %(typecode)s - Test for min value.
		"""
		arrayfunc.repeat(self.data, self.MinVal)

		expected = [self.MinVal] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

'''


# ==============================================================================

repeat_nonfinite_template = '''
##############################################################################
class repeat_nonfinite_%(typecode)s(unittest.TestCase):
	"""Test for nonfinite repeat function.
	repeat_nonfinite_template
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
				raise self.failureException('%%0.3f != %%0.3f' %% (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		# This is active for float numbers only. 
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.ArrayLength = 512

		self.data = array.array('%(typecode)s', [10] * self.ArrayLength)


	########################################################
	def test_repeat_nan_01(self):
		"""Test repeat non-finite operation in array code  %(typecode)s - Test for NaN.
		"""
		arrayfunc.repeat(self.data, math.nan)

		expected = [math.nan] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_inf_02(self):
		"""Test repeat non-finite operation in array code  %(typecode)s - Test for Inf value.
		"""
		arrayfunc.repeat(self.data, math.inf)

		expected = [math.inf] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_repeat_ninf_03(self):
		"""Test repeat non-finite operation in array code  %(typecode)s - Test for Neg Inf value.
		"""
		arrayfunc.repeat(self.data, -math.inf)

		expected = [-math.inf] * self.ArrayLength

		for dataoutitem, expecteditem in zip(list(self.data), expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

'''

# ==============================================================================


repeat_overflow_template = '''
##############################################################################
class repeat_overflow_%(typecode)s(unittest.TestCase):
	"""Test for overflow repeat function.
	repeat_overflow_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.ArrayLength = 512

		self.MaxVal = arrayfunc.arraylimits.%(typecode)s_max
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min


		# Create the overflow value for this data type.
		if '%(typecode)s' in ('f', 'd'):
			self.Overflow = self.MaxVal * 1.1
			self.Underflow = self.MinVal * 1.1
		else:
			self.Overflow = self.MaxVal + 1
			self.Underflow = self.MinVal - 1

		self.data = array.array('%(typecode)s', [0] * self.ArrayLength)


	########################################################
	def test_repeat_ovfl_01(self):
		"""Test repeat overflow operation in array code  %(typecode)s - Test for overflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Overflow)


	########################################################
	def test_repeat_ovfl_02(self):
		"""Test repeat overflow operation in array code  %(typecode)s - Test for underflow.
		"""
		with self.assertRaises(OverflowError):
			arrayfunc.repeat(self.data, self.Underflow)



##############################################################################

'''


# ==============================================================================

# The functions which are implemented by this program.
completefuncnames = ('count', 'cycle', 'repeat')


# Select the parameter test templates.
paramtemplates = {'count' : count_param_template, 
				'cycle' : cycle_param_template, 
				'repeat' : repeat_param_template
				}

# Select the operation test templates.
optemplates = {'count' : count_op_template, 
				'cycle' : cycle_op_template, 
				'repeat' : repeat_op_template
				}

# This is for count and cycle only.
opsignedtemplates = {'count' : count_op_signed_template, 
				'cycle' : cycle_op_signed_template
				}


# Select the non-finite test templates.
nonfinitetemplates = {'count' : count_nonfinite_template, 
				'cycle' : cycle_nonfinite_template, 
				'repeat' : repeat_nonfinite_template
				}


# Select the overflow test templates.
overflowtemplates = {'count' : count_overflow_template, 
				'cycle' : cycle_overflow_template, 
				'repeat' : repeat_overflow_template
				}


# This adds decimal point values for test values used in templates.
zeropad = dict.fromkeys(codegen_common.arraycodes, '')
zeropad['f'] = '.0'
zeropad['d'] = '.0'

invalidzeropad = dict.fromkeys(codegen_common.arraycodes, '.0')
invalidzeropad['f'] = ''
invalidzeropad['d'] = ''


# The maximum step to take, as defined for each array code type by 
# the corresponding array code type.
maxsteptypecode = {'b' : 'b',
					'B' : 'b',
					'h' : 'h',
					'H' : 'h',
					'i' : 'i',
					'I' : 'i',
					'l' : 'l',
					'L' : 'l',
					'q' : 'q',
					'Q' : 'q',
					'f' : 'f',
					'd' : 'd'}

# ==============================================================================

for funcname in completefuncnames:


	# Data for the copyright header files.
	headerdate = codegen_common.FormatHeaderData('test_%s' % funcname, '11-Jun-2014', funcname)


	with open('test_%s.py' % funcname, 'w') as f:
		# The copyright header.
		f.write(codegen_common.HeaderTemplate % headerdate)

		# Output the generated code for basic parameter tests.
		for arraycode in codegen_common.arraycodes:
			f.write(paramtemplates[funcname] % {'typecode' : arraycode,
												'zeropad' : zeropad[arraycode],
												'invalidzeropad' : invalidzeropad[arraycode]})

		# Output the generated code for basic operation tests.
		for arraycode in codegen_common.arraycodes:
			f.write(optemplates[funcname] % {'typecode' : arraycode,
												'zeropad' : zeropad[arraycode],
												'maxsteptypecode' : maxsteptypecode[arraycode]})

		# This test is for "count" and "cycle" only.
		if funcname in ('count', 'cycle'):
			# This is for signed arrays only.
			for arraycode in (codegen_common.signedint + codegen_common.floatarrays):
				f.write(opsignedtemplates[funcname] % {'typecode' : arraycode,
												'zeropad' : zeropad[arraycode]})


		# Output the generated code for non-finite operation tests.
		for arraycode in codegen_common.floatarrays:
			f.write(nonfinitetemplates[funcname] % {'typecode' : arraycode})


		# Output the generated code for overflow tests.
		for arraycode in codegen_common.arraycodes:
			# We can't detect overflows in some array types.
			if arraycode not in ('L', 'Q', 'd'):
				f.write(overflowtemplates[funcname] % {'typecode' : arraycode,
												'zeropad' : zeropad[arraycode],
												'maxsteptypecode' : maxsteptypecode[arraycode]})


		#####
		# The code which initiates the unit test.

		f.write(codegen_common.testendtemplate % funcname)


# ==============================================================================
