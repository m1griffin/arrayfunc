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
test_template_binop = ''' 

##############################################################################
class %(funclabel)s_general_%(arrayevenodd)s_arraysize_%(simdpresent)s_simd_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for basic general function operation using numeric 
	data %(test_op_y)s.
	test_template_binop
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

		if '%(arrayevenodd)s' == 'even':
			testdatasize = 160
		if '%(arrayevenodd)s' == 'odd':
			testdatasize = 159
		paramitersize = 5


		xdata = [x for x,y in zip(itertools.cycle([%(test_op_x)s]), range(testdatasize))]
		ydata = [x for x,y in zip(itertools.cycle([%(test_op_y)s]), range(testdatasize))]

		self.data1 = array.array('%(typecode)s', xdata)
		self.data2 = array.array('%(typecode)s', ydata)
		self.dataout = array.array('%(typecode)s', [0]*len(self.data1))

		self.limited = len(self.data1) // 2

		# This is used for testing with single parameters. We use a limited
		# data set to avoid excessive numbers of sub-tests.
		self.data1param = self.data1[:paramitersize]
		self.data2param = self.data2[:paramitersize]


	########################################################
	def test_%(funclabel)s_basic_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for basic function - Array code %(typelabel)s.
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
	def test_%(funclabel)s_basic_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for basic function with array limit - Array code %(typelabel)s.
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
	def test_%(funclabel)s_basic_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for basic function - Array code %(typelabel)s.
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
	def test_%(funclabel)s_basic_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for basic function with array limit - Array code %(typelabel)s.
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
	def test_%(funclabel)s_basic_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for basic function - Array code %(typelabel)s.
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
	def test_%(funclabel)s_basic_num_array_none_c2(self):
		"""Test %(funclabel)s as *num-array-none* for basic function with array limit - Array code %(typelabel)s.
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
	def test_%(funclabel)s_basic_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for basic function - Array code %(typelabel)s.
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
	def test_%(funclabel)s_basic_num_array_array_d2(self):
		"""Test %(funclabel)s as *num-array-array* for basic function with array limit - Array code %(typelabel)s.
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
	def test_%(funclabel)s_basic_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for basic function - Array code %(typelabel)s.
		"""
		expected = [x %(pyoperator)s y for (x, y) in zip(self.data1, self.data2)]

		arrayfunc.%(funcname)s(self.data1, self.data2 %(nosimd)s)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for basic function with array limit - Array code %(typelabel)s.
		"""
		pydataout = [x %(pyoperator)s y for (x, y) in zip(self.data1, self.data2)]
		expected = pydataout[0:self.limited] + list(self.data1)[self.limited:]

		arrayfunc.%(funcname)s(self.data1, self.data2, maxlen=self.limited %(nosimd)s)

		for dataoutitem, expecteditem in zip(self.data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_array_array_e3(self):
		"""Test %(funclabel)s as *array-array-array* for basic function - Array code %(typelabel)s.
		"""
		expected = [x %(pyoperator)s y for (x, y) in zip(self.data1, self.data2)]
		arrayfunc.%(funcname)s(self.data1, self.data2, self.dataout %(nosimd)s)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

'''

# ==============================================================================



# The template used to generate the tests for testing invalid array and
# numeric parameter types.
param_invalid_template = '''

##############################################################################
class %(funclabel)s_param_errors_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for invalid array and numeric parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		testdata1 = [%(test_op_x)s]
		testdata2 = [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), testdata1)]

		arraysize = len(testdata1)

		self.testarray1 = array.array('%(typecode)s', testdata1)
		self.testarray2 = array.array('%(typecode)s', testdata2)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0, arraysize))


		# Create some data array equivalents with an incompatible type.
		self.badarray1 = array.array('d', [float(x) for x in testdata1])
		self.badarray2 = array.array('d', [float(x) for x in testdata2])

		self.baddataout = array.array('d', [float(x) for x in self.dataout])


	########################################################
	def test_%(funclabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for invalid type of array - Array code %(typelabel)s.
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
	def test_%(funclabel)s_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for invalid type of number - Array code %(typelabel)s.
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
	def test_%(funclabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for invalid type of array - Array code %(typelabel)s.
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
	def test_%(funclabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for invalid type of number - Array code %(typelabel)s.
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
	def test_%(funclabel)s_array_num_array_b3(self):
		"""Test %(funclabel)s as *array-num-array* for invalid type of output array - Array code %(typelabel)s.
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
	def test_%(funclabel)s_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for invalid type of array - Array code %(typelabel)s.
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
	def test_%(funclabel)s_num_array_none_c2(self):
		"""Test %(funclabel)s as *num-array-none* for invalid type of number - Array code %(typelabel)s.
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
	def test_%(funclabel)s_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for invalid type of array - Array code %(typelabel)s.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_%(funclabel)s_num_array_array_d2(self):
		"""Test %(funclabel)s as *num-array-array* for invalid type of number - Array code %(typelabel)s.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testvalue, self.badarray2, self.dataout)


	########################################################
	def test_%(funclabel)s_num_array_array_d3(self):
		"""Test %(funclabel)s as *num-array-array* for invalid type of output array - Array code %(typelabel)s.
		"""
		for testvalue in self.testarray1:
			with self.subTest(msg='Failed with parameter', testvalue = testvalue):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testvalue, self.testarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testvalue, self.testarray2, self.baddataout)



	########################################################
	def test_%(funclabel)s_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for invalid type of array - Array code %(typelabel)s.
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
	def test_%(funclabel)s_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for invalid type of array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.testarray1, self.testarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.badarray1, self.testarray2)



	########################################################
	def test_%(funclabel)s_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for invalid type of array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.testarray1, self.badarray2, self.dataout)


	########################################################
	def test_%(funclabel)s_array_array_array_f2(self):
		"""Test %(funclabel)s as *array-array-array* for invalid type of array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.badarray1, self.testarray2, self.dataout)


	########################################################
	def test_%(funclabel)s_array_array_array_f3(self):
		"""Test %(funclabel)s as *array-array-array* for invalid type of output array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.testarray1, self.testarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.testarray1, self.testarray2, self.baddataout)


	########################################################
	def test_%(funclabel)s_no_params_g1(self):
		"""Test %(funclabel)s with no parameters - Array code %(typelabel)s.
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
class %(funclabel)s_opt_param_errors_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for invalid maxlen parameter.
	param_invalid_opt_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [%(test_op_x)s]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.testmaxlen = len(self.inpdata1a) // 2
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('%(typecode)s', self.inpdata1a)
		self.inparray2a = array.array('%(typecode)s', self.inpdata2a)
		self.dataout = array.array('%(typecode)s', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_%(funclabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for maxlen='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, maxlen='a')


	########################################################
	def test_%(funclabel)s_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for matherrors=True (unsupported option) - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, matherrors=True)


	########################################################
	def test_%(funclabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for maxlen='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue, self.dataout, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, self.dataout, maxlen='a')


	########################################################
	def test_%(funclabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for matherrors=True (unsupported option) - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue, self.dataout)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, self.dataout, matherrors=True)


	########################################################
	def test_%(funclabel)s_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for maxlen='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a, maxlen=self.testmaxlen)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, maxlen='a')


	########################################################
	def test_%(funclabel)s_num_array_none_c2(self):
		"""Test %(funclabel)s as *num-array-none* for matherrors=True (unsupported option) - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, matherrors=True)


	########################################################
	def test_%(funclabel)s_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for maxlen='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_%(funclabel)s_num_array_array_d2(self):
		"""Test %(funclabel)s as *num-array-array* for matherrors=True (unsupported option) - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, self.dataout, matherrors=True)


	########################################################
	def test_%(funclabel)s_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for maxlen='a' - Array code %(typelabel)s.
		"""

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.inparray2b, maxlen='a')


	########################################################
	def test_%(funclabel)s_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for matherrors=True (unsupported option) - Array code %(typelabel)s.
		"""

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.inparray2b, matherrors=True)


	########################################################
	def test_%(funclabel)s_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for maxlen='a' - Array code %(typelabel)s.
		"""

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, self.dataout, maxlen=self.testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.inparray2b, self.dataout, maxlen='a')


	########################################################
	def test_%(funclabel)s_array_array_array_f2(self):
		"""Test %(funclabel)s as *array-array-array* for matherrors=True (unsupported option) - Array code %(typelabel)s.
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
class %(funclabel)s_opt_nosimd_param_errors_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for invalid nosimd parameter.
	param_invalid_opt_nosimd_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [%(test_op_x)s]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('%(typecode)s', self.inpdata1a)
		self.inparray2a = array.array('%(typecode)s', self.inpdata2a)
		self.dataout = array.array('%(typecode)s', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)


	########################################################
	def test_%(funclabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for nosimd='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, nosimd='a')


	########################################################
	def test_%(funclabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for nosimd='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue, self.dataout, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, self.dataout, nosimd='a')


	########################################################
	def test_%(funclabel)s_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for nosimd='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a, nosimd=True)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, nosimd='a')


	########################################################
	def test_%(funclabel)s_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for nosimd='a' - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a, self.dataout, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, self.dataout, nosimd='a')


	########################################################
	def test_%(funclabel)s_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for nosimd='a' - Array code %(typelabel)s.
		"""

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, nosimd=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.inparray2b, nosimd='a')


	########################################################
	def test_%(funclabel)s_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for nosimd='a' - Array code %(typelabel)s.
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

# The template used to generate the tests for testing invalid parameter types
# for nosimd when it should not be present.
param_invalid_opt_nosimd_notpresent_template = '''

##############################################################################
class %(funclabel)s_opt_nosimd_param_errors_%(typelabel)s(unittest.TestCase):
	"""Test %(funclabel)s for invalid nosimd parameter.
	param_invalid_opt_nosimd_notpresent_template
	"""

	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.inpdata1a = [%(test_op_x)s]
		self.inpdata2a = [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), self.inpdata1a)]

		arraysize = len(self.inpdata1a)
		self.outpdata = itertools.repeat(0, arraysize)


		self.inparray1a = array.array('%(typecode)s', self.inpdata1a)
		self.inparray2a = array.array('%(typecode)s', self.inpdata2a)
		self.dataout = array.array('%(typecode)s', self.outpdata)


		self.inparray1b = copy.copy(self.inparray1a)
		self.inparray2b = copy.copy(self.inparray2a)



	########################################################
	def test_%(funclabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for nosimd=True (unsupported option) - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, nosimd=True)


	########################################################
	def test_%(funclabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for nosimd=True (unsupported option) - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		inpvalue = self.inparray2a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, inpvalue, self.dataout)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, inpvalue, self.dataout, nosimd=True)


	########################################################
	def test_%(funclabel)s_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for nosimd=True (unsupported option) - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a)


		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, nosimd=True)


	########################################################
	def test_%(funclabel)s_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for nosimd=True (unsupported option) - Array code %(typelabel)s.
		"""
		inpvalue = self.inparray1a[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(inpvalue, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(inpvalue, self.inparray2b, self.dataout, nosimd=True)


	########################################################
	def test_%(funclabel)s_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for nosimd=True (unsupported option) - Array code %(typelabel)s.
		"""

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.inparray2b, nosimd=True)


	########################################################
	def test_%(funclabel)s_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for nosimd=True (unsupported option) - Array code %(typelabel)s.
		"""

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.inparray1a, self.inparray2a, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.inparray1b, self.inparray2b, self.dataout, nosimd=True)



##############################################################################

'''

# ==============================================================================


# This is a list of which of the functions implements SIMD.
HasSIMD = ('and_', 'or_', 'xor')


# ==============================================================================

# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.

funclist = [x for x in oplist if x['test_op_templ'] in ('test_template_binop', 'test_template_binop2')]


# ==============================================================================

for func in funclist:

	funcname = func['funcname']
	filenamebase = 'test_' + funcname
	filename = filenamebase + '.py'
	headerdate = codegen_common.FormatHeaderData(filenamebase, '05-Apr-2018', funcname)

	# One function (one output file). 
	with open(filename, 'w') as f:
		# The copyright header.
		f.write(codegen_common.HeaderTemplate % headerdate)


		# Check each array type.
		for functype in codegen_common.intarrays:

			funcdata = {'funclabel' : func['funcname'], 'funcname' : 
				funcname, 'pyoperator' : func['pyoperator'],
				'typelabel' : functype, 'typecode' : functype, 
				'test_op_x' : func['test_op_x'],
				'test_op_y' : func['test_op_y']}

				
			# Test for basic operation.

			# Not all functions support SIMD operations.
			if funcname in HasSIMD:
				# With SIMD, even data arra size.
				funcdata['simdpresent'] = 'with'
				funcdata['nosimd'] = ''
				funcdata['arrayevenodd'] = 'even'
				f.write(test_template_binop % funcdata)

				# With SIMD, odd data array size.
				funcdata['simdpresent'] = 'with'
				funcdata['nosimd'] = ''
				funcdata['arrayevenodd'] = 'odd'
				f.write(test_template_binop % funcdata)

				# Without SIMD.
				funcdata['simdpresent'] = 'without'
				funcdata['nosimd'] = ', nosimd=True'
				funcdata['arrayevenodd'] = 'even'
				f.write(test_template_binop % funcdata)
			else:
				# Without SIMD.
				funcdata['simdpresent'] = 'without'
				funcdata['nosimd'] = ''
				funcdata['arrayevenodd'] = 'even'
				f.write(test_template_binop % funcdata)


			#####

			# Test for invalid parameters. One template should work for all 
			# functions of this style.
			f.write(param_invalid_template % funcdata)

			#####

			# Test for invalid optional parameters such as maxlen.
			f.write(param_invalid_opt_template % funcdata)

			#####

			# Test for invalid nosimd parameters. One version handles 
			# the test for functions which use this parameter, and the
			# other handles functions which do not have nosimd
			if funcname in HasSIMD:
				f.write(param_invalid_opt_nosimd_template % funcdata)
			else:
				f.write(param_invalid_opt_nosimd_notpresent_template % funcdata)


		f.write(codegen_common.testendtemplate % funcname)

# ==============================================================================

