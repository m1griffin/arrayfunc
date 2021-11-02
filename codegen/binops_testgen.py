#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for integer binary operations.
# Language: Python 3.5
# Date:     05-Apr-2018
#
###############################################################################
#
#   Copyright 2014 - 2018    Michael Griffin    <m12.griffin@gmail.com>
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

# This template is for binary operations (e.g. and_, or_, xor, etc.).
test_template_binop_andorxor = ''' 

##############################################################################
class %(funcname)s_general_%(arrayevenodd)s_arraysize_%(simdpresent)s_simd_%(typecode)s(unittest.TestCase):
	"""Test %(funcname)s for basic general function operation .
	test_template_binop_andorxor
	"""



	########################################################
	def setUp(self):
		"""Initialise.
		"""

		if '%(arrayevenodd)s' == 'even':
			testdatasize = 320

		if '%(arrayevenodd)s' == 'odd':
			testdatasize = 319

		paramitersize = 5

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.%(typecode)s_min
		maxval = arrayfunc.arraylimits.%(typecode)s_max

		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1


		# A list of numbers, but in reverse order to that used for 'x'.
		ydata = list(itertools.islice(itertools.cycle(range(maxval, minval, -dstep)), testdatasize))
		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		ydata[-5] = maxval
		ydata[5] = 0
		ydata[6] = 1
		if minval < 0:
			ydata[4] = -1


		self.data1 = array.array('%(typecode)s', xdata)
		self.data2 = array.array('%(typecode)s', ydata)
		self.dataout = array.array('%(typecode)s', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_%(funcname)s_basic_array_num_none_a1(self):
		"""Test %(funcname)s as *array-num-none* for basic function - Array code %(typecode)s.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x %(pyoperator)s testval for x in datax]

				arrayfunc.%(funcname)s(datax, testval %(nosimd)s)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funcname)s_basic_array_num_none_a2(self):
		"""Test %(funcname)s as *array-num-none* for basic function with array limit - Array code %(typecode)s.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x %(pyoperator)s testval for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.%(funcname)s(datax, testval, maxlen=self.limited %(nosimd)s)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funcname)s_basic_array_num_array_b1(self):
		"""Test %(funcname)s as *array-num-array* for basic function - Array code %(typecode)s.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [x %(pyoperator)s testval for x in datax]

				arrayfunc.%(funcname)s(datax, testval, self.dataout %(nosimd)s)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funcname)s_basic_array_num_array_b2(self):
		"""Test %(funcname)s as *array-num-array* for basic function with array limit - Array code %(typecode)s.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [x %(pyoperator)s testval for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.%(funcname)s(datax, testval, self.dataout, maxlen=self.limited %(nosimd)s)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funcname)s_basic_num_array_none_c1(self):
		"""Test %(funcname)s as *num-array-none* for basic function - Array code %(typecode)s.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval %(pyoperator)s x for x in datay]

				arrayfunc.%(funcname)s(testval, datay %(nosimd)s)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funcname)s_basic_num_array_none_c2(self):
		"""Test %(funcname)s as *num-array-none* for basic function with array limit - Array code %(typecode)s.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval %(pyoperator)s x for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.%(funcname)s(testval, datay, maxlen=self.limited %(nosimd)s)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funcname)s_basic_num_array_array_d1(self):
		"""Test %(funcname)s as *num-array-array* for basic function - Array code %(typecode)s.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [testval %(pyoperator)s x for x in datay]

				arrayfunc.%(funcname)s(testval, datay, self.dataout %(nosimd)s)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funcname)s_basic_num_array_array_d2(self):
		"""Test %(funcname)s as *num-array-array* for basic function with array limit - Array code %(typecode)s.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [testval %(pyoperator)s x for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout)[self.limited:]

				arrayfunc.%(funcname)s(testval, datay, self.dataout, maxlen=self.limited %(nosimd)s)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funcname)s_basic_array_array_none_e1(self):
		"""Test %(funcname)s as *array-array-none* for basic function - Array code %(typecode)s.
		"""
		expected = [x %(pyoperator)s y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.%(funcname)s(self.data1, self.data2 %(nosimd)s)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funcname)s_basic_array_array_none_e2(self):
		"""Test %(funcname)s as *array-array-none* for basic function with array limit - Array code %(typecode)s.
		"""
		pydataout = [x %(pyoperator)s y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.%(funcname)s(self.data1, self.data2, maxlen=self.limited %(nosimd)s)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funcname)s_basic_array_array_array_e3(self):
		"""Test %(funcname)s as *array-array-array* for basic function - Array code %(typecode)s.
		"""
		expected = [x %(pyoperator)s y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.%(funcname)s(self.data1, self.data2, self.dataout %(nosimd)s)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

'''

# ==============================================================================


# ==============================================================================

# This template is for binary operations (e.g. lshift, rshift.).
test_template_binop_shift = ''' 

##############################################################################
class %(funcname)s_general_%(arrayevenodd)s_arraysize_%(simdpresent)s_simd_%(typecode)s(unittest.TestCase):
	"""Test %(funcname)s for basic general function operation.
	test_template_binop_shift
	"""


	########################################################
	def pyshift(self, lop, rop):
		"""Perform a shift operation in Python which produces the same 
		results as native shift operations.
		x86 CPUs do shifts rather peculiarly. For 32 bit arrays and
		smaller, only first 5 bits are used as the amount to shift for
		non-SIMD instructions. This means the shift "rolls over" after 32. 
		For 64 bit arrays, this is 64 bits or larger.
		However, x86 SIMD instructions do not follow this, and ARM is
		different as well.
		As a result of this, this shift function does not attempt to produce
		valid results outside of shift values (rop) beyond the bit length.
		(e.g. 0 - 7, 0 - 15, 0 - 31, 0 - 64)
		"""
		sresult = (lop %(pyoperator)s rop) & self.exmask
		if sresult > arrayfunc.arraylimits.%(typecode)s_max:
			sresult = sresult - (self.exmask + 1)
		return sresult


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		if '%(arrayevenodd)s' == 'even':
			testdatasize = 320

		if '%(arrayevenodd)s' == 'odd':
			testdatasize = 319

		paramitersize = 25

		decentre = testdatasize // 2

		minval = arrayfunc.arraylimits.%(typecode)s_min
		maxval = arrayfunc.arraylimits.%(typecode)s_max

		# Calculate our interval, while making sure that it is not zero.
		dstep = max((maxval - minval) // testdatasize, 1)

		# Generate test data over the full data type range.
		xdata = list(itertools.islice(itertools.cycle(range(minval, maxval, dstep)), testdatasize))

		# Make sure the last value is the largest number in the range and
		# that we have 0, 1, and -1 in the signed data samples as well.
		xdata[-1] = maxval
		xdata[decentre] = 0
		xdata[decentre + 1] = 1
		if minval < 0:
			xdata[decentre - 1] = -1

		# The number of bits in a word.
		bitmax = {
			'b' : arrayfunc.arraylimits.B_max.bit_length(),
			'B' : arrayfunc.arraylimits.B_max.bit_length(),
			'h' : arrayfunc.arraylimits.H_max.bit_length(),
			'H' : arrayfunc.arraylimits.H_max.bit_length(),
			'i' : arrayfunc.arraylimits.I_max.bit_length(),
			'I' : arrayfunc.arraylimits.I_max.bit_length(),
			'l' : arrayfunc.arraylimits.L_max.bit_length(),
			'L' : arrayfunc.arraylimits.L_max.bit_length(),
			'q' : arrayfunc.arraylimits.Q_max.bit_length(),
			'Q' : arrayfunc.arraylimits.Q_max.bit_length(),
		}
		self.bitlength = bitmax['%(typecode)s']

		# All the amounts to shift the first parameter by, limited
		# the the number of bits in the word. We don't test for what
		# happens when we exceed this, as the results on x86 are irregular.
		ydata = list(range(self.bitlength))
		# This provides the equivalent in the same length as the x array
		# to allow for tests with two input arrays.
		ydatax = list(itertools.islice(itertools.cycle(ydata), testdatasize))

		self.data1 = array.array('%(typecode)s', xdata)
		self.data2 = array.array('%(typecode)s', ydata)
		self.data3 = array.array('%(typecode)s', ydatax)
		self.dataout1 = array.array('%(typecode)s', [0]*len(self.data1))
		self.dataout2 = array.array('%(typecode)s', [0]*len(self.data2))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = ydata


		intmasks = {
			'b' : arrayfunc.arraylimits.B_max,
			'B' : arrayfunc.arraylimits.B_max,
			'h' : arrayfunc.arraylimits.H_max,
			'H' : arrayfunc.arraylimits.H_max,
			'i' : arrayfunc.arraylimits.I_max,
			'I' : arrayfunc.arraylimits.I_max,
			'l' : arrayfunc.arraylimits.L_max,
			'L' : arrayfunc.arraylimits.L_max,
			'q' : arrayfunc.arraylimits.Q_max,
			'Q' : arrayfunc.arraylimits.Q_max,
		}

		# Make sure the Python shifts do not go out of the range of the 
		# integer type.
		self.exmask = intmasks['%(typecode)s']


	########################################################
	def test_%(funcname)s_basic_array_num_none_a1(self):
		"""Test %(funcname)s as *array-num-none* for basic function - Array code %(typecode)s.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [self.pyshift(x, testval) for x in datax]

				arrayfunc.%(funcname)s(datax, testval %(nosimd)s)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funcname)s_basic_array_num_none_a2(self):
		"""Test %(funcname)s as *array-num-none* for basic function with array limit - Array code %(typecode)s.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [self.pyshift(x, testval) for x in datax]
				expected = pydataout[0:self.limited] + list(datax)[self.limited:]

				arrayfunc.%(funcname)s(datax, testval, maxlen=self.limited %(nosimd)s)

				for dataoutitem, expecteditem in zip(datax, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funcname)s_basic_array_num_array_b1(self):
		"""Test %(funcname)s as *array-num-array* for basic function - Array code %(typecode)s.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				expected = [self.pyshift(x, testval) for x in datax]

				arrayfunc.%(funcname)s(datax, testval, self.dataout1 %(nosimd)s)

				for dataoutitem, expecteditem in zip(self.dataout1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funcname)s_basic_array_num_array_b2(self):
		"""Test %(funcname)s as *array-num-array* for basic function with array limit - Array code %(typecode)s.
		"""
		for testval in self.data2param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datax = copy.copy(self.data1)

				pydataout = [self.pyshift(x, testval) for x in datax]
				expected = pydataout[0:self.limited] + list(self.dataout1)[self.limited:]

				arrayfunc.%(funcname)s(datax, testval, self.dataout1, maxlen=self.limited %(nosimd)s)

				for dataoutitem, expecteditem in zip(self.dataout1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funcname)s_basic_num_array_none_c1(self):
		"""Test %(funcname)s as *num-array-none* for basic function - Array code %(typecode)s.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [self.pyshift(testval, x) for x in datay]

				arrayfunc.%(funcname)s(testval, datay %(nosimd)s)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funcname)s_basic_num_array_none_c2(self):
		"""Test %(funcname)s as *num-array-none* for basic function with array limit - Array code %(typecode)s.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [self.pyshift(testval, x) for x in datay]
				expected = pydataout[0:self.limited] + list(datay)[self.limited:]

				arrayfunc.%(funcname)s(testval, datay, maxlen=self.limited %(nosimd)s)

				for dataoutitem, expecteditem in zip(datay, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funcname)s_basic_num_array_array_d1(self):
		"""Test %(funcname)s as *num-array-array* for basic function - Array code %(typecode)s.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				expected = [self.pyshift(testval, x) for x in datay]

				arrayfunc.%(funcname)s(testval, datay, self.dataout2 %(nosimd)s)

				for dataoutitem, expecteditem in zip(self.dataout2, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funcname)s_basic_num_array_array_d2(self):
		"""Test %(funcname)s as *num-array-array* for basic function with array limit - Array code %(typecode)s.
		"""
		for testval in self.data1param:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				datay = copy.copy(self.data2)

				pydataout = [self.pyshift(testval, x) for x in datay]
				expected = pydataout[0:self.limited] + list(self.dataout2)[self.limited:]

				arrayfunc.%(funcname)s(testval, datay, self.dataout2, maxlen=self.limited %(nosimd)s)

				for dataoutitem, expecteditem in zip(self.dataout2, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funcname)s_basic_array_array_none_e1(self):
		"""Test %(funcname)s as *array-array-none* for basic function - Array code %(typecode)s.
		"""
		expected = [self.pyshift(x, y) for (x, y) in zip(self.data1, self.data3)]

		arrayfunc.%(funcname)s(self.data1, self.data3 %(nosimd)s)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funcname)s_basic_array_array_none_e2(self):
		"""Test %(funcname)s as *array-array-none* for basic function with array limit - Array code %(typecode)s.
		"""
		pydataout = [self.pyshift(x, y) for (x, y) in zip(self.data1, self.data3)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.%(funcname)s(self.data1, self.data3, maxlen=self.limited %(nosimd)s)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funcname)s_basic_array_array_array_e3(self):
		"""Test %(funcname)s as *array-array-array* for basic function - Array code %(typecode)s.
		"""
		expected = [self.pyshift(x, y) for (x, y) in zip(self.data1, self.data3)]
		arrayfunc.%(funcname)s(self.data1, self.data3, self.dataout1 %(nosimd)s)

		for dataoutitem, expecteditem in zip(self.dataout1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

'''


# ==============================================================================


# The template used to generate the tests for testing invalid array and
# numeric parameter types.
param_invalid_template = '''

##############################################################################
class %(funcname)s_param_errors_%(typecode)s(unittest.TestCase):
	"""Test %(funcname)s for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		testdata1 = [100,101,102,103,104,105,106,107,108,109]
		testdata2 = [x for (x,y) in zip(itertools.cycle([0,1,2,3,4,5]), testdata1)]

		arraysize = len(testdata1)

		self.testarray1 = array.array('%(typecode)s', testdata1)
		self.testarray2 = array.array('%(typecode)s', testdata2)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0, arraysize))


		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in testdata1])
		self.badarray2 = array.array('d', [float(x) for x in testdata2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_%(funcname)s_array_num_none_a1(self):
		"""Test %(funcname)s as *array-num-none* for invalid type of array - Array code %(typecode)s.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testarray1, testvalue)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(badarray1, testvalue)


	########################################################
	def test_%(funcname)s_array_num_none_a2(self):
		"""Test %(funcname)s as *array-num-none* for invalid type of number - Array code %(typecode)s.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testarray1, testvalue)

				testarray1 = copy.copy(self.testarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testarray1, badvalue)



	########################################################
	def test_%(funcname)s_array_num_array_b1(self):
		"""Test %(funcname)s as *array-num-array* for invalid type of array - Array code %(typecode)s.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(badarray1, testvalue, self.dataout)


	########################################################
	def test_%(funcname)s_array_num_array_b2(self):
		"""Test %(funcname)s as *array-num-array* for invalid type of number - Array code %(typecode)s.
		"""
		for testvalue, badvalue in zip(self.testarray2, self.badarray2):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				badarray1 = copy.copy(self.badarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(self.testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(self.testarray1, badvalue, self.dataout)


	########################################################
	def test_%(funcname)s_array_num_array_b3(self):
		"""Test %(funcname)s as *array-num-array* for invalid type of output array - Array code %(typecode)s.
		"""
		for testvalue in self.testarray2:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray1 = copy.copy(self.testarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testarray1, testvalue, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testarray1, testvalue, self.baddataout)



	########################################################
	def test_%(funcname)s_num_array_none_c1(self):
		"""Test %(funcname)s as *num-array-none* for invalid type of array - Array code %(typecode)s.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)
				badarray2 = copy.copy(self.badarray2)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testvalue, testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testvalue, badarray2)


	########################################################
	def test_%(funcname)s_num_array_none_c2(self):
		"""Test %(funcname)s as *num-array-none* for invalid type of number - Array code %(typecode)s.
		"""
		for testvalue, badvalue in zip(self.testarray1, self.badarray1):
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# Copy the array so we don't change the original data.
				testarray2 = copy.copy(self.testarray2)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testvalue, testarray2)

				testarray2 = copy.copy(self.testarray2)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(badvalue, testarray2)



	########################################################
	def test_%(funcname)s_num_array_array_d1(self):
		"""Test %(funcname)s as *num-array-array* for invalid type of array - Array code %(typecode)s.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_%(funcname)s_num_array_array_d2(self):
		"""Test %(funcname)s as *num-array-array* for invalid type of number - Array code %(typecode)s.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_%(funcname)s_num_array_array_d3(self):
		"""Test %(funcname)s as *num-array-array* for invalid type of output array - Array code %(typecode)s.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_%(funcname)s_array_array_none_e1(self):
		"""Test %(funcname)s as *array-array-none* for invalid type of array - Array code %(typecode)s.
		"""
		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This version is expected to pass.
		arrayfunc.%(funcname)s(testarray1, self.testarray2)

		# Copy the array so we don't change the original data.
		testarray1 = copy.copy(self.testarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(testarray1, self.badarray2)


	########################################################
	def test_%(funcname)s_array_array_none_e2(self):
		"""Test %(funcname)s as *array-array-none* for invalid type of array - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.badarray1, self.testarray2)



	########################################################
	def test_%(funcname)s_array_array_array_f1(self):
		"""Test %(funcname)s as *array-array-array* for invalid type of array - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_%(funcname)s_array_array_array_f2(self):
		"""Test %(funcname)s as *array-array-array* for invalid type of array - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_%(funcname)s_array_array_array_f3(self):
		"""Test %(funcname)s as *array-array-array* for invalid type of output array - Array code %(typecode)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_%(funcname)s_no_params_g1(self):
		"""Test %(funcname)s with no parameters - Array code %(typecode)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s()


##############################################################################

'''

# ==============================================================================

# ==============================================================================

# The template used to generate the tests for testing invalid parameter types
# for maxlen.
param_invalid_opt_template = '''

##############################################################################
class %(funcname)s_opt_param_errors_%(typecode)s(unittest.TestCase):
	"""Test %(funcname)s for invalid maxlen parameter.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [100,101,102,103,104,105,106,107,108,109	]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0,1,2,3,4,5]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.testmaxlen = len(self.inpdata1a) // 2
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('%(typecode)s', self.inpdata1a)
		self.inparray2a = array.array('%(typecode)s', self.inpdata2a)
		self.dataout = array.array('%(typecode)s', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_%(funcname)s_array_num_none_a1(self):
		"""Test %(funcname)s as *array-num-none* for maxlen='a' - Array code %(typecode)s.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_%(funcname)s_array_num_none_a2(self):
		"""Test %(funcname)s as *array-num-none* for matherrors=True (unsupported option) - Array code %(typecode)s.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, matherrors=True)


	########################################################
	def test_%(funcname)s_array_num_array_b1(self):
		"""Test %(funcname)s as *array-num-array* for maxlen='a' - Array code %(typecode)s.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_%(funcname)s_array_num_array_b2(self):
		"""Test %(funcname)s as *array-num-array* for matherrors=True (unsupported option) - Array code %(typecode)s.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue, self.dataout)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, self.dataout, matherrors=True)


	########################################################
	def test_%(funcname)s_num_array_none_c1(self):
		"""Test %(funcname)s as *num-array-none* for maxlen='a' - Array code %(typecode)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_%(funcname)s_num_array_none_c2(self):
		"""Test %(funcname)s as *num-array-none* for matherrors=True (unsupported option) - Array code %(typecode)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, matherrors=True)


	########################################################
	def test_%(funcname)s_num_array_array_d1(self):
		"""Test %(funcname)s as *num-array-array* for maxlen='a' - Array code %(typecode)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_%(funcname)s_num_array_array_d2(self):
		"""Test %(funcname)s as *num-array-array* for matherrors=True (unsupported option) - Array code %(typecode)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, self.dataout, matherrors=True)


	########################################################
	def test_%(funcname)s_array_array_none_e1(self):
		"""Test %(funcname)s as *array-array-none* for maxlen='a' - Array code %(typecode)s.
		"""

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_%(funcname)s_array_array_none_e2(self):
		"""Test %(funcname)s as *array-array-none* for matherrors=True (unsupported option) - Array code %(typecode)s.
		"""

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.inparray2b, matherrors=True)


	########################################################
	def test_%(funcname)s_array_array_array_f1(self):
		"""Test %(funcname)s as *array-array-array* for maxlen='a' - Array code %(typecode)s.
		"""

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_%(funcname)s_array_array_array_f2(self):
		"""Test %(funcname)s as *array-array-array* for matherrors=True (unsupported option) - Array code %(typecode)s.
		"""

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.inparray2b, self.dataout, matherrors=True)



##############################################################################

'''

# ==============================================================================


# ==============================================================================

# The template used to generate the tests for testing invalid parameter types
# for nosimd where expected.
param_invalid_opt_nosimd_template = '''

##############################################################################
class %(funcname)s_opt_nosimd_param_errors_%(typecode)s(unittest.TestCase):
	"""Test %(funcname)s for invalid nosimd parameter.
	param_invalid_opt_nosimd_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [100,101,102,103,104,105,106,107,108,109]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([0,1,2,3,4,5]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('%(typecode)s', self.inpdata1a)
		self.inparray2a = array.array('%(typecode)s', self.inpdata2a)
		self.dataout = array.array('%(typecode)s', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_%(funcname)s_array_num_none_a1(self):
		"""Test %(funcname)s as *array-num-none* for nosimd='a' - Array code %(typecode)s.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, nosimd='a')


	########################################################
	def test_%(funcname)s_array_num_array_b1(self):
		"""Test %(funcname)s as *array-num-array* for nosimd='a' - Array code %(typecode)s.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue, self.dataout, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, self.dataout, nosimd='a')


	########################################################
	def test_%(funcname)s_num_array_none_c1(self):
		"""Test %(funcname)s as *num-array-none* for nosimd='a' - Array code %(typecode)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, nosimd='a')


	########################################################
	def test_%(funcname)s_num_array_array_d1(self):
		"""Test %(funcname)s as *num-array-array* for nosimd='a' - Array code %(typecode)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, self.dataout, nosimd='a')


	########################################################
	def test_%(funcname)s_array_array_none_e1(self):
		"""Test %(funcname)s as *array-array-none* for nosimd='a' - Array code %(typecode)s.
		"""

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.inparray2b, nosimd='a')


	########################################################
	def test_%(funcname)s_array_array_array_f1(self):
		"""Test %(funcname)s as *array-array-array* for nosimd='a' - Array code %(typecode)s.
		"""

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.inparray2b, self.dataout, nosimd='a')



##############################################################################

'''


# ==============================================================================

# ==============================================================================


def makedata():
	'''Make the combinations of data options for tests.
	'''
	typecode = [('typecode', x) for x in codegen_common.intarrays]
	arrayevenodd = (('arrayevenodd', 'even'), ('arrayevenodd', 'odd'))
	simdpresent = (('simdpresent', 'nosimd'), ('simdpresent', 'withsimd'))

	# This creates all the combinations of test data.
	combos = [dict(x) for x in itertools.product(typecode, arrayevenodd, simdpresent)]

	nosimd = {'nosimd' : {'nosimd' : ', nosimd=True'}, 'withsimd' : {'nosimd' : ''}}

	# Update with the test data. These values don't represent independent combinations,
	# but rather just additional data that goes along with other items already present.
	for x in combos:
		x.update(nosimd[x['simdpresent']])

	return combos

# ==============================================================================


# This is a list of which of the functions implements SIMD.
HasSIMD = ('and_', 'or_', 'xor', 'lshift', 'rshift')


test_template_binop = {
	'and_' : test_template_binop_andorxor, 
	'or_' : test_template_binop_andorxor, 
	'xor' : test_template_binop_andorxor, 
	'lshift' : test_template_binop_shift, 
	'rshift' : test_template_binop_shift
}


# ==============================================================================


# Read in the op codes.
opdata = codegen_common.ReadINI('affuncdata.ini')

# Filter out the desired math functions.
funclist = [(x,dict(y)) for x,y in opdata.items() if y.get('test_op_templ') in ('test_template_binop', 'test_template_binop2')]


# ==============================================================================

# This defines the module name.
modulename = 'arrayfunc'
# Import the array module for testing.
arrayimport = 'import array'


for funcname, func in funclist:

	filenamebase = 'test_' + funcname
	filename = filenamebase + '.py'
	headerdate = codegen_common.FormatHeaderData(filenamebase, '05-Apr-2018', funcname)

	# Add additional header data.
	headerdate['modulename'] = modulename
	headerdate['arrayimport'] = arrayimport


	basictemplate = test_template_binop[funcname]

	# One function (one output file). 
	with open(filename, 'w') as f:
		# The copyright header.
		f.write(codegen_common.HeaderTemplate % headerdate)


		# Test for basic operation.
		for funcdata in makedata():
			funcdata['funcname'] = funcname
			funcdata['pyoperator'] = func['pyoperator']

			f.write(basictemplate % funcdata)


		# Check each array type.
		for typecode in codegen_common.intarrays:
			funcdata = {'funcname' : funcname,
						'pyoperator' : func['pyoperator'],
						'typecode' : typecode
						}


			#####

			# Test for invalid parameters. One template should work for all 
			# functions of this style.
			f.write(param_invalid_template % funcdata)

			#####

			# Test for invalid optional parameters such as maxlen.
			f.write(param_invalid_opt_template % funcdata)

			#####

			# Test for invalid nosimd parameters. 
			f.write(param_invalid_opt_nosimd_template % funcdata)


		f.write(codegen_common.testendtemplate % {'funcname' : funcname, 'testprefix' : 'af'})

# ==============================================================================

