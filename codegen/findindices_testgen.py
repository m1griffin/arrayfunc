#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the C code for findindices.
# Language: Python 3.5
# Date:     21-Jun-2014
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


# This template is for findindices operations.
op_template = ''' 

##############################################################################
class findindices_operator_%(typecode)s(unittest.TestCase):
	"""Test for basic operator function.
	op_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = '%(typecode)s'
		self.TestData = [97%(zeropad)s, 97%(zeropad)s, 97%(zeropad)s, 98%(zeropad)s, 99%(zeropad)s, 101%(zeropad)s, 101%(zeropad)s, 102%(zeropad)s, 95%(zeropad)s, 103%(zeropad)s]
		self.zerofill = 0%(zeropad)s

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
		"""Test eq  - Array code %(typecode)s.
		"""
		param = 97%(zeropad)s
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gt_01(self):
		"""Test gt  - Array code %(typecode)s.
		"""
		param = 96%(zeropad)s
		result = arrayfunc.findindices('>', self.data, self.dataout, param)
		expected, explength = self.Findindices('>', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_gte_01(self):
		"""Test gte  - Array code %(typecode)s.
		"""
		param = 96%(zeropad)s
		result = arrayfunc.findindices('>=', self.data, self.dataout, param)
		expected, explength = self.Findindices('>=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lt_01(self):
		"""Test lt  - Array code %(typecode)s.
		"""
		param = 98%(zeropad)s
		result = arrayfunc.findindices('<', self.data, self.dataout, param)
		expected, explength = self.Findindices('<', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_lte_01(self):
		"""Test lte  - Array code %(typecode)s.
		"""
		param = 98%(zeropad)s
		result = arrayfunc.findindices('<=', self.data, self.dataout, param)
		expected, explength = self.Findindices('<=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_ne_01(self):
		"""Test ne  - Array code %(typecode)s.
		"""
		param = 98%(zeropad)s
		result = arrayfunc.findindices('!=', self.data, self.dataout, param)
		expected, explength = self.Findindices('!=', self.data, param)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)
		

	########################################################
	def test_operator_maxlen_01(self):
		"""Test array maxlen  - Array code %(typecode)s.
		"""
		param = 97%(zeropad)s
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=len(self.data)//2)
		expected, explength = self.Findindices('==', self.data, param, maxlen=len(self.data)//2)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_operator_maxlen_02(self):
		"""Test array maxlen  - Array code %(typecode)s.
		"""
		param = 97%(zeropad)s
		result = arrayfunc.findindices('==', self.data, self.dataout, param, maxlen=-1)
		expected, explength = self.Findindices('==', self.data, param, maxlen=-1)

		# Check the test to make sure it is working as intended.
		self.assertTrue((result > 0) and (result < len(self.data)))
		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

'''


# ==============================================================================


# The template used to generate the parameter tests.
param_template = '''
##############################################################################
class findindices_params_%(typecode)s(unittest.TestCase):
	"""Test for basic parameter function.
	param_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = '%(typecode)s'
		self.TestData = [97%(zeropad)s, 97%(zeropad)s, 97%(zeropad)s, 98%(zeropad)s, 99%(zeropad)s, 101%(zeropad)s, 101%(zeropad)s, 102%(zeropad)s, 102%(zeropad)s, 103%(zeropad)s]
		self.zerofill = 0%(zeropad)s

		self.data = array.array(self.TypeCode, self.TestData)

		self.dataout = array.array('q', itertools.repeat(0, len(self.data)))


		# This is used in testing parameters.
		self.dataempty = array.array(self.TypeCode)
		self.dataemptyout = array.array('q')


	########################################################
	def test_param_no_params(self):
		"""Test exception when no parameters passed  - Array code %(typecode)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter()


	########################################################
	def test_param_one_params(self):
		"""Test exception when one parameter passed  - Array code %(typecode)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_two_params(self):
		"""Test exception when two parameters passed  - Array code %(typecode)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_three_params(self):
		"""Test exception when three parameters passed  - Array code %(typecode)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1)


	########################################################
	def test_param_six_params(self):
		"""Test exception when too many (six) parameters passed  - Array code %(typecode)s.
		"""
		param = 101%(zeropad)s
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, param, 3, maxlen=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [1, 2, 3, 4], 3)



	########################################################
	def test_param_invalid_keyword_params(self):
		"""Test exception with invalid keyword parameters passed  - Array code %(typecode)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100%(zeropad)s, xx=2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], xx=2)


	########################################################
	def test_param_invalid_keyword_param_type(self):
		"""Test exception with invalid keyword parameter type passed  - Array code %(typecode)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100%(zeropad)s, maxlen='x')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, [0, 1, 2, 3, 4], maxlen='x')


	########################################################
	def test_param_invalid_opcode_param_value(self):
		"""Test exception with invalid first parameter value  - Array code %(typecode)s.
		"""
		with self.assertRaises(ValueError):
			result = arrayfunc.findindices('!', self.data, self.dataout, 100%(zeropad)s)


	########################################################
	def test_param_invalid_opcode_param_type(self):
		"""Test exception with invalid first parameter type  - Array code %(typecode)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices(62, self.data, self.dataout, 100%(zeropad)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = list(filter('a', [0, 1, 2, 3, 4]))


	########################################################
	def test_param_invalid_input_array_param_value(self):
		"""Test exception with invalid array input parameter value  - Array code %(typecode)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', 99, self.dataout, 100%(zeropad)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_output_array_param_value(self):
		"""Test exception with invalid array output parameter type  - Array code %(typecode)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, 99, 100%(zeropad)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_input_array_param_length(self):
		"""Test exception with empty input array parameter type  - Array code %(typecode)s.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.dataempty, self.dataout, 100%(zeropad)s)


	########################################################
	def test_param_invalid_output_array_param_length(self):
		"""Test exception with empty output array parameter type  - Array code %(typecode)s.
		"""
		with self.assertRaises(IndexError):
			result = arrayfunc.findindices('==', self.data, self.dataemptyout, 100%(zeropad)s)


	########################################################
	def test_param_invalid_array_param_type_01(self):
		"""Test exception with invalid compare parameter type  - Array code %(typecode)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 'e')

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_array_param_type_02(self):
		"""Test exception with invalid compare parameter type  - Array code %(typecode)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100%(invalidzeropad)s)


		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = filter(lambda x: x < 1, 99)


	########################################################
	def test_param_invalid_outputarray_type_01(self):
		"""Test exception with invalid output array type  - Array code %(typecode)s.
		"""
		# The list of array types should have all supported types other than 'q'.
		for testval in ('b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'Q', 'f', 'd'):
			with self.subTest(msg='Failed with parameter', testval = testval):
		
				badarray = array.array(testval, itertools.repeat(0, len(self.data)))

				with self.assertRaises(TypeError):
					result = arrayfunc.findindices('==', self.data, badarray)


##############################################################################

'''


# ==============================================================================


# Overflow testing. This can't be used with all types.
overflow_template = '''
##############################################################################
class findindices_paramovfl_%(typecode)s(unittest.TestCase):
	"""Test for testing parameter overflow.
	overflow_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = '%(typecode)s'
		self.zerofill = 0%(zeropad)s

		# These values are used for testing parameter overflows.
		self.dataovfl = array.array(self.TypeCode, range(97, 107))
		self.dataoutovfl = array.array('q', itertools.repeat(0, len(self.dataovfl)))

		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min
		self.Maxval = arrayfunc.arraylimits.%(typecode)s_max


	########################################################
	def test_overflow_min(self):
		"""Test parameter overflow min  - Array code %(typecode)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal %(overflowdec)s)


	########################################################
	def test_overflow_max(self):
		"""Test parameter overflow max  - Array code %(typecode)s.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval %(overflowinc)s)


	########################################################
	def test_overflow_ok(self):
		"""Test no overflow. These should not overflow  - Array code %(typecode)s.
		"""
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.MinVal)
		result = arrayfunc.findindices('==', self.dataovfl, self.dataoutovfl, self.Maxval)



##############################################################################

'''


# ==============================================================================


# The template used to generate the tests for nan, inf, -inf.
nonfinite_template = '''
##############################################################################
class findindices_nonfinite_%(typecode)s(unittest.TestCase):
	"""Test for nan, inf, -inf.
	nonfinite_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.data = array.array('%(typecode)s', [100.0] * 10)
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
		"""Test for param of nan  - Array code %(typecode)s.
		"""
		param = math.nan
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_nonfinite_02(self):
		"""Test for param of inf  - Array code %(typecode)s.
		"""
		param = math.inf
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_nonfinite_03(self):
		"""Test for param of -inf  - Array code %(typecode)s.
		"""
		param = -math.inf
		result = arrayfunc.findindices('==', self.data, self.dataout, param)
		expected, explength = self.Findindices('==', self.data, param)

		self.assertEqual(result, explength)
		for dataoutitem, expecteditem in zip(list(self.dataout), expected):
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_nonfinite_04(self):
		"""Test for maxlen of nan  - Array code %(typecode)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.0, maxlen=math.nan)


	########################################################
	def test_nonfinite_05(self):
		"""Test for maxlen of inf  - Array code %(typecode)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.0, maxlen=math.inf)


	########################################################
	def test_nonfinite_06(self):
		"""Test for maxlen of -inf  - Array code %(typecode)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.findindices('==', self.data, self.dataout, 100.0, maxlen=-math.inf)


##############################################################################

'''


# ==============================================================================

# ==============================================================================

funcname = 'findindices'

filenamebase = 'test_' + funcname
filename = filenamebase + '.py'
headerdate = codegen_common.FormatHeaderData(filenamebase, '21-Jun-2014', funcname)


with open(filename, 'w') as f:
	# The copyright header.
	f.write(codegen_common.HeaderTemplate % headerdate)

	#####
	# Basic tests.

	# Check each array type.
	for arraycode in codegen_common.arraycodes:

		if arraycode in codegen_common.floatarrays:
			zeropad = '.0'
			invalidzeropad = ''
			overflowinc = '* 1.1'
			overflowdec = '* 1.1'
		else:
			zeropad = ''
			invalidzeropad = '.5'
			overflowinc = '+ 1'
			overflowdec = '- 1'

		opdata = {'funcname' : funcname,
				'typecode' : arraycode,
				'zeropad' : zeropad,
				'invalidzeropad' : invalidzeropad,
				'overflowinc' : overflowinc,
				'overflowdec' : overflowdec,
				}

		f.write(op_template % opdata)
		f.write(param_template % opdata)

		# Parameter overflow tests do not work with all array types.
		if arraycode not in ('L', 'Q', 'd'):
			f.write(overflow_template % opdata)


	# Non finite tests for parameter tests for floating point arrays.
	for arraycode in codegen_common.floatarrays:
		opdata = {'funcname' : funcname,
				'typecode' : arraycode,
				}

		f.write(nonfinite_template % opdata)


	#####
	# The code which initiates the unit test.

	f.write(codegen_common.testendtemplate % funcname)


# ==============================================================================
