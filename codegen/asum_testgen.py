#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for asum.
# Language: Python 3.4
# Date:     13-Jun-2014
#
###############################################################################
#
#   Copyright 2014 - 2016    Michael Griffin    <m12.griffin@gmail.com>
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

signedtestdata = {'gentest' : 'itertools.chain(range(1,10,2), range(11,-88,-3))',
			'maxval' : 'itertools.chain(range(1,10,2), [self.MaxVal] * 10, range(11,-88,-3))',
			'minval' : 'itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10)'}

unsignedtestdata = {'gentest' : 'itertools.chain(range(1,10,2), range(88,12,-3))',
			'maxval' : 'itertools.chain(range(1,10,2), [self.MaxVal] * 10, range(88,12,-3))',
			'minval' : 'itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10)'}

floattestdata = {'gentest' : '[float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))]',
			'maxval' : '[float(x) for x in itertools.chain(range(1,10,2), [self.MaxVal] * 10, range(11,-88,-3))]',
			'minval' : '[float(x) for x in itertools.chain([self.MinVal] * 10, range(1,10,2), [self.MinVal] * 10)]'}

testdata = {
	'b' : signedtestdata, 'B' : unsignedtestdata,
	'h' : signedtestdata, 'H' : unsignedtestdata,
	'i' : signedtestdata, 'I' : unsignedtestdata,
	'l' : signedtestdata, 'L' : unsignedtestdata,
	'q' : copy.copy(signedtestdata), 'Q' : copy.copy(unsignedtestdata),
	'f' : floattestdata, 'd' : floattestdata,
	}



# This is used to insert code to convert the test data to bytes type. 
bytesconverter = 'data = bytes(data)'

# This defines how to test with and without SIMD.
simdon = {'simdlabel' : 'with_SIMD', 'simdstatus' : 'with', 'simdtest' : ''}
simdoff = {'simdlabel' : 'without_SIMD', 'simdstatus' : 'without SIMD', 'simdtest' : ', nosimd=True'}
simdtests = [simdoff, simdon]
simdnone = {'simdlabel' : '', 'simdstatus' : '', 'simdtest' : ''}

# ==============================================================================

# The basic template for testing each array type for operator function.
op_template = '''
##############################################################################
class asum_operator_%(typelabel)s_%(simdlabel)s(unittest.TestCase):
	"""Test for basic operator function.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.TypeCode = '%(typecode)s'

		self.MaxVal = arrayfunc.arraylimits.%(typecode)s_max
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min


	########################################################
	def test_function_01(self):
		"""Test asum  - Array code %(typelabel)s. General test %(simdstatus)s.
		"""
		data = array.array('%(typecode)s', %(gentest)s)
		%(bytesconverter)s
		result = arrayfunc.asum(data %(simdtest)s)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_02(self):
		"""Test asum  - Array code %(typelabel)s. General test with overflow checking on %(simdstatus)s.
		"""
		data = array.array('%(typecode)s', %(gentest)s)
		%(bytesconverter)s
		result = arrayfunc.asum(data, disovfl=False %(simdtest)s)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_03(self):
		"""Test asum  - Array code %(typelabel)s. General test with overflow checking off %(simdstatus)s.
		"""
		data = array.array('%(typecode)s', %(gentest)s)
		%(bytesconverter)s
		result = arrayfunc.asum(data, disovfl=True %(simdtest)s)
		self.assertEqual(result, sum(data))


	########################################################
	def test_function_04(self):
		"""Test asum  - Array code %(typelabel)s. General test with array limit applied %(simdstatus)s.
		"""
		data = array.array('%(typecode)s', %(gentest)s)
		%(bytesconverter)s
		result = arrayfunc.asum(data, maxlen=10 %(simdtest)s)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_05(self):
		"""Test asum  - Array code %(typelabel)s. General test with array limit applied and overflow checking on %(simdstatus)s.
		"""
		data = array.array('%(typecode)s', %(gentest)s)
		%(bytesconverter)s
		result = arrayfunc.asum(data, disovfl=False, maxlen=10 %(simdtest)s)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_06(self):
		"""Test asum  - Array code %(typelabel)s. General test with array limit applied and overflow checking off %(simdstatus)s.
		"""
		data = array.array('%(typecode)s', %(gentest)s)
		%(bytesconverter)s
		result = arrayfunc.asum(data, disovfl=True, maxlen=10 %(simdtest)s)
		self.assertEqual(result, sum(data[:10]))


	########################################################
	def test_function_07(self):
		"""Test asum  - Array code %(typelabel)s. Test invalid parameter type for array data %(simdstatus)s.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(1 %(simdtest)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(1)

	########################################################
	def test_function_08(self):
		"""Test asum  - Array code %(typelabel)s. Test invalid parameter type for overflow flag %(simdstatus)s.
		"""
		data = array.array('%(typecode)s', %(gentest)s)
		%(bytesconverter)s
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, disovfl='a' %(simdtest)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')

	########################################################
	def test_function_09(self):
		"""Test asum  - Array code %(typelabel)s. Test invalid parameter type for limit %(simdstatus)s.
		"""
		data = array.array('%(typecode)s', %(gentest)s)
		%(bytesconverter)s
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, maxlen='a' %(simdtest)s)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum([1, 2, 3], disovfl='a')


	########################################################
	def test_function_10(self):
		"""Test asum  - Array code %(typelabel)s. Test no parameters.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.asum()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum()


	########################################################
	def test_function_11(self):
		"""Test asum  - Array code %(typelabel)s. Test too many (five) parameters.
		"""
		data = array.array('%(typecode)s', %(gentest)s)
		%(bytesconverter)s
		with self.assertRaises(TypeError):
			result = arrayfunc.asum(data, False, 2, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = sum(data, 0, 2)


'''


# Overflow check for positive numbers. Smaller numbers cannot overflow in a reasonable amount of RAM.
maxovlf_template = '''
	########################################################
	def test_function_12(self):
		"""Test asum  - Array code %(typelabel)s. Arithmetic positive overflow expected.
		"""
		data = array.array('%(typecode)s', %(maxval)s)
		%(bytesconverter)s
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(data %(simdtest)s)

'''


# Overflow check for negative numbers. Smaller numbers cannot overflow in a reasonable amount of RAM.
minovlf_template = '''
	########################################################
	def test_function_13(self):
		"""Test asum  - Array code %(typelabel)s. Arithmetic overflow expected for negative numbers.
		"""
		data = array.array('%(typecode)s', %(minval)s)
		%(bytesconverter)s
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(data %(simdtest)s)

'''


endclass_template = '''
##############################################################################
'''


# ==============================================================================


# The basic template for testing floating point arrays with nan, inf, -inf.
nan_template = '''
##############################################################################
class asum_nan_%(typelabel)s(unittest.TestCase):
	"""Test with floating point nan inf, and -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.MaxVal = arrayfunc.arraylimits.%(typecode)s_max
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min

		self.data_nan = array.array('%(typecode)s', [-1.0, 0.0, 1.0, float('nan'), self.MaxVal, self.MinVal, 100.5] * 10)
		self.data_inf = array.array('%(typecode)s', [-1.0, 0.0, 1.0, float('inf'), self.MaxVal, self.MinVal, 100.5] * 10)
		self.data_ninf = array.array('%(typecode)s', [-1.0, 0.0, 1.0, float('-inf'), self.MaxVal, self.MinVal, 100.5] * 10)


	########################################################
	def test_nan_01(self):
		"""Test array with nan - Array code %(typelabel)s, default SIMD state.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_nan)

	########################################################
	def test_nan_02(self):
		"""Test array with infinity - Array code %(typelabel)s, default SIMD state.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_inf)

	########################################################
	def test_nan_03(self):
		"""Test array with negative infinity - Array code %(typelabel)s, default SIMD state.
		"""
		with self.assertRaises(OverflowError):
			result = arrayfunc.asum(self.data_ninf)

	########################################################
	def test_nan_04(self):
		"""Test array with nan - Array code %(typelabel)s, overflow disabled.
		"""
		expected = sum(self.data_nan)
		result = arrayfunc.asum(self.data_nan, disovfl=True)

		# NaN cannot be compared using normal means.
		if math.isnan(expected):
			self.assertTrue(math.isnan(result))
		elif math.isnan(result):
			self.assertTrue(math.isnan(expected))
		# Inf or -inf can be compared using an exact match.
		elif (not math.isfinite(result)) or (not math.isfinite(expected)):
			self.assertEqual(result, expected)
		# Anything else can be compared normally.
		else:
			deltaval = min((abs(expected), abs(result))) / 100.0
			self.assertAlmostEqual(result, expected, delta=deltaval)

	########################################################
	def test_nan_05(self):
		"""Test array with infinity - Array code %(typelabel)s, overflow disabled.
		"""
		expected = sum(self.data_inf)
		result = arrayfunc.asum(self.data_inf, disovfl=True)

		# NaN cannot be compared using normal means.
		if math.isnan(expected):
			self.assertTrue(math.isnan(result))
		elif math.isnan(result):
			self.assertTrue(math.isnan(expected))
		# Inf or -inf can be compared using an exact match.
		elif (not math.isfinite(result)) or (not math.isfinite(expected)):
			self.assertEqual(result, expected)
		# Anything else can be compared normally.
		else:
			deltaval = min((abs(expected), abs(result))) / 100.0
			self.assertAlmostEqual(result, expected, delta=deltaval)

	########################################################
	def test_nan_06(self):
		"""Test array with negative infinity - Array code %(typelabel)s, overflow disabled.
		"""
		expected = sum(self.data_ninf)
		result = arrayfunc.asum(self.data_ninf, disovfl=True)

		# NaN cannot be compared using normal means.
		if math.isnan(expected):
			self.assertTrue(math.isnan(result))
		elif math.isnan(result):
			self.assertTrue(math.isnan(expected))
		# Inf or -inf can be compared using an exact match.
		elif (not math.isfinite(result)) or (not math.isfinite(expected)):
			self.assertEqual(result, expected)
		# Anything else can be compared normally.
		else:
			deltaval = min((abs(expected), abs(result))) / 100.0
			self.assertAlmostEqual(result, expected, delta=deltaval)

	########################################################
	def test_nan_07(self):
		"""Test array with nan - Array code %(typelabel)s, overflow and SIMD disabled.
		"""
		expected = sum(self.data_nan)
		result = arrayfunc.asum(self.data_nan, nosimd=True, disovfl=True)

		# NaN cannot be compared using normal means.
		if math.isnan(expected):
			self.assertTrue(math.isnan(result))
		elif math.isnan(result):
			self.assertTrue(math.isnan(expected))
		# Inf or -inf can be compared using an exact match.
		elif (not math.isfinite(result)) or (not math.isfinite(expected)):
			self.assertEqual(result, expected)
		# Anything else can be compared normally.
		else:
			deltaval = min((abs(expected), abs(result))) / 100.0
			self.assertAlmostEqual(result, expected, delta=deltaval)

	########################################################
	def test_nan_08(self):
		"""Test array with infinity - Array code %(typelabel)s, overflow and SIMD disabled.
		"""
		expected = sum(self.data_inf)
		result = arrayfunc.asum(self.data_inf, nosimd=True, disovfl=True)

		# NaN cannot be compared using normal means.
		if math.isnan(expected):
			self.assertTrue(math.isnan(result))
		elif math.isnan(result):
			self.assertTrue(math.isnan(expected))
		# Inf or -inf can be compared using an exact match.
		elif (not math.isfinite(result)) or (not math.isfinite(expected)):
			self.assertEqual(result, expected)
		# Anything else can be compared normally.
		else:
			deltaval = min((abs(expected), abs(result))) / 100.0
			self.assertAlmostEqual(result, expected, delta=deltaval)

	########################################################
	def test_nan_09(self):
		"""Test array with negative infinity - Array code %(typelabel)s, overflow and SIMD disabled.
		"""
		expected = sum(self.data_ninf)
		result = arrayfunc.asum(self.data_ninf, nosimd=True, disovfl=True)

		# NaN cannot be compared using normal means.
		if math.isnan(expected):
			self.assertTrue(math.isnan(result))
		elif math.isnan(result):
			self.assertTrue(math.isnan(expected))
		# Inf or -inf can be compared using an exact match.
		elif (not math.isfinite(result)) or (not math.isfinite(expected)):
			self.assertEqual(result, expected)
		# Anything else can be compared normally.
		else:
			deltaval = min((abs(expected), abs(result))) / 100.0
			self.assertAlmostEqual(result, expected, delta=deltaval)


##############################################################################

'''

# ==============================================================================

# Data for the copyright header files.
headerdate = codegen_common.FormatHeaderData('test_asum', '11-Jun-2014', 'asum')


with open('test_asum.py', 'w') as f:
	# The copyright header.
	f.write(codegen_common.HeaderTemplate % headerdate)

	# Output the generated code for basic operator tests.
	for funtypes in codegen_common.arraycodes:
		datarec = copy.deepcopy(testdata[funtypes])
		datarec['typecode'] = funtypes
		datarec['typelabel'] = funtypes
		datarec['bytesconverter'] = ''
		# SIMD is only implemented for floating point, turn it off.
		if funtypes in codegen_common.floatarrays:
			datarec.update(simdoff)
			f.write(op_template % datarec)
		else:
			datarec.update(simdnone)
			f.write(op_template % datarec)

		# Smaller numbers cannot overflow in a reasonable amount of RAM.
		# Overflow for positive numbers.
		if funtypes in ('l', 'L', 'q', 'Q', 'f', 'd'):
			f.write(maxovlf_template % datarec)


		# Overflow for negative numbers.
		if funtypes in ('l', 'q', 'f', 'd'):
			f.write(minovlf_template % datarec)


		f.write(endclass_template)


	# Repeat for SIMD enabled.
	for funtypes in codegen_common.floatarrays:
		datarec = copy.deepcopy(testdata[funtypes])
		datarec['typecode'] = funtypes
		datarec['typelabel'] = funtypes
		datarec['bytesconverter'] = ''
		datarec.update(simdon)
		f.write(op_template % datarec)
		f.write(endclass_template)


	# Do the tests for bytes.
	datarec = testdata['B']
	datarec['typecode'] = 'B'
	datarec['typelabel'] = 'bytes'
	datarec['bytesconverter'] = bytesconverter
	datarec.update(simdnone)
	f.write(op_template % datarec)


	# Output the generated code for nan and inf.
	datarec = {}
	for funtypes in codegen_common.floatarrays:
		datarec['typecode'] = funtypes
		datarec['typelabel'] = funtypes
		f.write(nan_template % datarec)


	f.write(codegen_common.testendtemplate % 'asum')


