#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for amin.
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
			'increasing' : 'range(1,100)',
			'decreasing' : 'range(100,1,-1)',
			'maxval' : 'itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3))',
			'minval' : 'itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10)'}

unsignedtestdata = {'gentest' : 'itertools.chain(range(1,10,2), range(88,12,-3))',
			'increasing' : 'range(1,100)',
			'decreasing' : 'range(100,1,-1)',
			'maxval' : 'itertools.chain(range(1,10,2), [self.MaxVal], range(88,12,-3))',
			'minval' : 'itertools.chain([self.MinVal] * 10, range(1,20), [self.MinVal] * 10)'}

floattestdata = {'gentest' : '[float(x) for x in itertools.chain(range(1,10,2), range(11,-88,-3))]',
			'increasing' : '[float(x) for x in range(1,100)]',
			'decreasing' : '[float(x) for x in range(100,1,-1)]',
			'maxval' : '[float(x) for x in itertools.chain(range(1,10,2), [self.MaxVal], range(11,-88,-3))]',
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


# ==============================================================================

# The basic template for testing each array type for operator function.
op_template = '''

##############################################################################
class amin_operator_%(typelabel)s(unittest.TestCase):
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
		"""Test amin  - Array code %(typelabel)s. General test with SIMD.
		"""
		data = array.array('%(typecode)s', %(gentest)s)
		%(bytesconverter)s
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_02(self):
		"""Test amin  - Array code %(typelabel)s. General test without SIMD.
		"""
		data = array.array('%(typecode)s', %(gentest)s)
		%(bytesconverter)s
		result = arrayfunc.amin(data, nosimd=True)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_03(self):
		"""Test amin  - Array code %(typelabel)s. Test increasing values with SIMD.
		"""
		data = array.array('%(typecode)s', %(increasing)s)
		%(bytesconverter)s
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_04(self):
		"""Test amin  - Array code %(typelabel)s. Test increasing values without SIMD.
		"""
		data = array.array('%(typecode)s', %(increasing)s)
		%(bytesconverter)s
		result = arrayfunc.amin(data, nosimd=True)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_05(self):
		"""Test amin  - Array code %(typelabel)s. Test decreasing values with SIMD.
		"""
		data = array.array('%(typecode)s', %(decreasing)s)
		%(bytesconverter)s
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_06(self):
		"""Test amin  - Array code %(typelabel)s. Test decreasing values without SIMD.
		"""
		data = array.array('%(typecode)s', %(decreasing)s)
		%(bytesconverter)s
		result = arrayfunc.amin(data, nosimd=True)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_07(self):
		"""Test amin  - Array code %(typelabel)s. Test finding min for data type with SIMD.
		"""
		data = array.array('%(typecode)s', %(maxval)s)
		%(bytesconverter)s
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_08(self):
		"""Test amin  - Array code %(typelabel)s. Test finding min for data type without SIMD.
		"""
		data = array.array('%(typecode)s', %(maxval)s)
		%(bytesconverter)s
		result = arrayfunc.amin(data, nosimd=True)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_09(self):
		"""Test amin  - Array code %(typelabel)s. Test finding value from array that contains min for data type with SIMD.
		"""
		data = array.array('%(typecode)s', %(minval)s)
		%(bytesconverter)s
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_10(self):
		"""Test amin  - Array code %(typelabel)s. Test finding value from array that contains min for data type without SIMD.
		"""
		data = array.array('%(typecode)s', %(minval)s)
		%(bytesconverter)s
		result = arrayfunc.amin(data, nosimd=True)
		self.assertEqual(result, min(data))


	########################################################
	def test_function_11(self):
		"""Test amin  - Array code %(typelabel)s. Test optional lim parameter with SIMD.
		"""
		data = array.array('%(typecode)s', %(maxval)s)
		%(bytesconverter)s
		result = arrayfunc.amin(data, maxlen=5)
		self.assertEqual(result, min(data[:5]))


	########################################################
	def test_function_12(self):
		"""Test amin  - Array code %(typelabel)s. Test optional lim parameter without SIMD.
		"""
		data = array.array('%(typecode)s', %(maxval)s)
		%(bytesconverter)s
		result = arrayfunc.amin(data, maxlen=5, nosimd=True)
		self.assertEqual(result, min(data[:5]))


	########################################################
	def test_function_13(self):
		"""Test amin  - Array code %(typelabel)s. Test invalid parameter type with SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(1)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(1)


	########################################################
	def test_function_14(self):
		"""Test amin  - Array code %(typelabel)s. Test invalid parameter type without SIMD.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(1, nosimd=True)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(1)


	########################################################
	def test_function_15(self):
		"""Test amin  - Array code %(typelabel)s. Test missing parameter.
		"""
		with self.assertRaises(TypeError):
			result = arrayfunc.amin()

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min()


	########################################################
	def test_function_16(self):
		"""Test amin  - Array code %(typelabel)s. Test excess parameters.
		"""
		data = array.array('%(typecode)s', %(gentest)s)
		%(bytesconverter)s
		with self.assertRaises(TypeError):
			result = arrayfunc.amin(data, 5, 2, 2)

		# Check that the exception raised corresponds to the native Python behaviour.
		with self.assertRaises(TypeError):
			result = min(data, 2)


##############################################################################

'''


# ==============================================================================

# The basic template for testing floating point arrays with nan, inf -inf.
nan_template = '''
##############################################################################
class amin_nan_%(typelabel)s(unittest.TestCase):
	"""Test with floating point nan, inf -inf.
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.MaxVal = arrayfunc.arraylimits.%(typecode)s_max
		self.MinVal = arrayfunc.arraylimits.%(typecode)s_min

		self.data_nan = array.array('%(typecode)s', [-10.0, -1000.0, -1.0, 0.0, 1.0, float('nan'), self.MaxVal, self.MinVal, 100.5, 100.1, 100.1])
		self.data_inf = array.array('%(typecode)s', [-10.0, -1000.0, -1.0, 0.0, 1.0, float('inf'), self.MaxVal, self.MinVal, 100.5, 100.1, 100.1])
		self.data_ninf = array.array('%(typecode)s', [-10.0, -1000.0, -1.0, 0.0, 1.0, float('-inf'), self.MaxVal, self.MinVal, 100.5, 100.1, 100.1])
		self.data_mixed = array.array('%(typecode)s', [-10.0, -1000.0, float('inf'), 0.0, float('-inf'), float('nan'), self.MaxVal, self.MinVal, 100.5, 100.1, 100.1])


	########################################################
	def rottest(self, x, rotplaces):
		"""Modify the test data by shifting the data in the array.
		"""
		return x[rotplaces:] + x[:rotplaces]

'''


# The basic template for individual tests with floating point arrays with nan, inf -inf.
inftest_template = '''
	########################################################
	def test_%(testarray)s_SIMD_%(testseq)s(self):
		"""Test array with %(testarray)s - Array code %(typelabel)s with SIMD.
		"""
		data = self.rottest(self.data_%(testarray)s, %(testseq)s)
		result = arrayfunc.amin(data)
		self.assertEqual(result, min(data))


	########################################################
	def test_%(testarray)s_NOSIMD_%(testseq)s(self):
		"""Test array with %(testarray)s - Array code %(typelabel)s without SIMD.
		"""
		data = self.rottest(self.data_%(testarray)s, %(testseq)s)
		result = arrayfunc.amin(data, nosimd=True)
		self.assertEqual(result, min(data))

'''

nantest_template = '''
	########################################################
	def test_%(testarray)s_SIMD_%(testseq)s(self):
		"""Test array with %(testarray)s - Array code %(typelabel)s with SIMD.
		"""
		data = self.rottest(self.data_%(testarray)s, %(testseq)s)
		result = arrayfunc.amin(data)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.


	########################################################
	def test_%(testarray)s_NOSIMD_%(testseq)s(self):
		"""Test array with %(testarray)s - Array code %(typelabel)s without SIMD.
		"""
		data = self.rottest(self.data_%(testarray)s, %(testseq)s)
		result = arrayfunc.amin(data, nosimd=True)
		# We don't actually test the result as there is no meaningful order
		# comparison with NaN.

'''



# ==============================================================================

testclose = '''
##############################################################################
'''

# ==============================================================================

# Data for the copyright header files.
headerdate = codegen_common.FormatHeaderData('test_amin', '11-Jun-2014', 'amin')


with open('test_amin.py', 'w') as f:
	# The copyright header.
	f.write(codegen_common.HeaderTemplate % headerdate)

	# Output the generated code for basic operator tests.
	for funtypes in codegen_common.arraycodes:
		datarec = testdata[funtypes]
		datarec['typecode'] = funtypes
		datarec['typelabel'] = funtypes
		datarec['bytesconverter'] = ''
		f.write(op_template % datarec)



	# Do the tests for bytes.
	datarec = testdata['B']
	datarec['typecode'] = 'B'
	datarec['typelabel'] = 'bytes'
	datarec['bytesconverter'] = bytesconverter
	f.write(op_template % datarec)


	# Output the generated code for nan and inf.
	datarec = {}
	for funtypes in codegen_common.floatarrays:
		datarec['typecode'] = funtypes
		datarec['typelabel'] = funtypes
		f.write(nan_template % datarec)


	# Output the generated code for nan and inf.
	datarec = {}
	for funtypes in codegen_common.floatarrays:
		datarec['typecode'] = funtypes
		datarec['typelabel'] = funtypes
		f.write(nan_template % datarec)

		# Add tests for each special data type. 
		for testarray in ('inf', 'ninf'):
			# Add a test to rotate through the data.
			for testseq in range(0, 11):
				f.write(inftest_template % {'testarray' : testarray, 'testseq' : testseq, 'typelabel' : funtypes})

		for testarray in ('nan', 'mixed'):
			# Add a test to rotate through the data.
			for testseq in range(0, 11):
				f.write(nantest_template % {'testarray' : testarray, 'testseq' : testseq, 'typelabel' : funtypes})


		# Close off the test.
		f.write(testclose)

	# End of the tests.
	f.write(codegen_common.testendtemplate % 'amin')


