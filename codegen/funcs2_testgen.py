#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Purpose:  Generate the unit tests for math functions which use two 
#           input parameters.
# Language: Python 3.5
# Date:     08-Dec-2017
#
###############################################################################
#
#   Copyright 2014 - 2017    Michael Griffin    <m12.griffin@gmail.com>
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



# This template is for operators which use a second numeric parameter.
test_template = '''

##############################################################################
class %(funclabel)s_general_%(typelabel)s(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data %(test_op_y)s.
	test_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
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
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


	########################################################
	def test_%(funclabel)s_basic_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for basic function - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])

				expected = [%(pyoperator)s(x, testval) for x in data1]

				arrayfunc.%(funcname)s(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for basic function with matherrors=True - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])

				expected = [%(pyoperator)s(x, testval) for x in data1]

				arrayfunc.%(funcname)s(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_num_none_a3(self):
		"""Test %(funclabel)s as *array-num-none* for basic function with array limit - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])

				limited = len(data1) // 2

				pydataout = [%(pyoperator)s(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.%(funcname)s(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_num_none_a4(self):
		"""Test %(funclabel)s as *array-num-none* for basic function with matherrors=True and with array limit - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])

				limited = len(data1) // 2

				pydataout = [%(pyoperator)s(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.%(funcname)s(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_basic_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for basic function - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])
				dataout = array.array('%(typecode)s', [0]*len(data1))

				expected = [%(pyoperator)s(x, testval) for x in data1]

				arrayfunc.%(funcname)s(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for basic function with matherrors=True - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])
				dataout = array.array('%(typecode)s', [0]*len(data1))

				expected = [%(pyoperator)s(x, testval) for x in data1]

				arrayfunc.%(funcname)s(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_num_array_b3(self):
		"""Test %(funclabel)s as *array-num-array* for basic function with array limit - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])
				dataout = array.array('%(typecode)s', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [%(pyoperator)s(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.%(funcname)s(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_num_array_b4(self):
		"""Test %(funclabel)s as *array-num-array* for basic function with matherrors=True and with array limit - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])
				dataout = array.array('%(typecode)s', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [%(pyoperator)s(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.%(funcname)s(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_basic_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for basic function - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])

				expected = [%(pyoperator)s(testval, x) for x in data1]

				arrayfunc.%(funcname)s(testval, data1)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_num_array_none_c2(self):
		"""Test %(funclabel)s as *num-array-none* for basic function with matherrors=True - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])

				expected = [%(pyoperator)s(testval, x) for x in data1]

				arrayfunc.%(funcname)s(testval, data1, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_num_array_none_c3(self):
		"""Test %(funclabel)s as *num-array-none* for basic function with array limit - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])

				limited = len(data1) // 2

				pydataout = [%(pyoperator)s(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.%(funcname)s(testval, data1, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_num_array_none_c4(self):
		"""Test %(funclabel)s as *num-array-none* for basic function with matherrors=True and with array limit - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])

				limited = len(data1) // 2

				pydataout = [%(pyoperator)s(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.%(funcname)s(testval, data1, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_basic_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for basic function - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])
				dataout = array.array('%(typecode)s', [0]*len(data1))

				expected = [%(pyoperator)s(testval, x) for x in data1]

				arrayfunc.%(funcname)s(testval, data1, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_num_array_array_d2(self):
		"""Test %(funclabel)s as *num-array-array* for basic function with matherrors=True - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])
				dataout = array.array('%(typecode)s', [0]*len(data1))

				expected = [%(pyoperator)s(testval, x) for x in data1]

				arrayfunc.%(funcname)s(testval, data1, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_num_array_array_d3(self):
		"""Test %(funclabel)s as *num-array-array* for basic function with array limit - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])
				dataout = array.array('%(typecode)s', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [%(pyoperator)s(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.%(funcname)s(testval, data1, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_num_array_array_d4(self):
		"""Test %(funclabel)s as *num-array-array* for basic function with matherrors=True and with array limit - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('%(typecode)s', [%(test_op_x)s])
				dataout = array.array('%(typecode)s', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [%(pyoperator)s(testval, x) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.%(funcname)s(testval, data1, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_basic_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for basic function - Array code %(typelabel)s.
		"""
		data1 = array.array('%(typecode)s', [%(test_op_x)s])
		data2 = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), data1)])

		expected = [%(pyoperator)s(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.%(funcname)s(data1, data2)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for basic function with matherrors=True - Array code %(typelabel)s.
		"""
		data1 = array.array('%(typecode)s', [%(test_op_x)s])
		data2 = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), data1)])

		expected = [%(pyoperator)s(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.%(funcname)s(data1, data2, matherrors=True)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_array_none_e3(self):
		"""Test %(funclabel)s as *array-array-none* for basic function with array limit - Array code %(typelabel)s.
		"""
		data1 = array.array('%(typecode)s', [%(test_op_x)s])
		data2 = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), data1)])

		limited = len(data1) // 2

		pydataout = [%(pyoperator)s(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.%(funcname)s(data1, data2, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_array_none_e4(self):
		"""Test %(funclabel)s as *array-array-none* for basic function with matherrors=True and with array limit - Array code %(typelabel)s.
		"""
		data1 = array.array('%(typecode)s', [%(test_op_x)s])
		data2 = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), data1)])

		limited = len(data1) // 2

		pydataout = [%(pyoperator)s(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(data1)[limited:]

		arrayfunc.%(funcname)s(data1, data2, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(data1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_array_array_e5(self):
		"""Test %(funclabel)s as *array-array-array* for basic function - Array code %(typelabel)s.
		"""
		data1 = array.array('%(typecode)s', [%(test_op_x)s])
		data2 = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), data1)])
		dataout = array.array('%(typecode)s', [0]*len(data1))

		expected = [%(pyoperator)s(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.%(funcname)s(data1, data2, dataout)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_basic_array_array_array_e6(self):
		"""Test %(funclabel)s as *array-array-array* for basic function - Array code %(typelabel)s.
		"""
		data1 = array.array('%(typecode)s', [%(test_op_x)s])
		data2 = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), data1)])
		dataout = array.array('%(typecode)s', [0]*len(data1))

		expected = [%(pyoperator)s(x, y) for (x, y) in zip(data1, data2)]
		arrayfunc.%(funcname)s(data1, data2, dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_basic_array_array_array_e7(self):
		"""Test %(funclabel)s as *array-array-array* for basic function - Array code %(typelabel)s.
		"""
		data1 = array.array('%(typecode)s', [%(test_op_x)s])
		data2 = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), data1)])
		dataout = array.array('%(typecode)s', [0]*len(data1))

		limited = len(data1) // 2

		pydataout = [%(pyoperator)s(x, y) for (x, y) in zip(data1, data2)]
		expected = pydataout[0:limited] + list(dataout)[limited:]

		arrayfunc.%(funcname)s(data1, data2, dataout, matherrors=True, maxlen=limited)

		for dataoutitem, expecteditem in zip(dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



##############################################################################

'''

# ==============================================================================


# The template used to generate the tests for testing invalid parameter types.
param_invalid_template = '''

##############################################################################
class %(funclabel)s_param_errors_%(typelabel)s(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.floatarray1 = array.array('%(typecode)s', [%(test_op_x)s])
		self.floatarray2 = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), self.floatarray1)])

		arraysize =  len(self.floatarray1)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray1 = array.array('i', [int(x) for x in self.floatarray1])
		self.intarray2 = array.array('i', [int(x) for x in self.floatarray2])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_%(funclabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for integer array - Array code %(typelabel)s.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(floatarray1, testfloat)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(intarray1, testfloat)


	########################################################
	def test_%(funclabel)s_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for integer number - Array code %(typelabel)s.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(floatarray1, testfloat)

				floatarray1 = copy.copy(self.floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(floatarray1, testint)


	########################################################
	def test_%(funclabel)s_array_num_none_a3(self):
		"""Test %(funclabel)s as *array-num-none* for integer number and array - Array code %(typelabel)s.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(floatarray1, testfloat)

				intarray1 = copy.copy(self.intarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(intarray1, testint)


	########################################################
	def test_%(funclabel)s_array_num_none_a4(self):
		"""Test %(funclabel)s as *array-num-none* for errors='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(floatarray1, testfloat, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(floatarray1, testfloat, errors='a')


	########################################################
	def test_%(funclabel)s_array_num_none_a5(self):
		"""Test %(funclabel)s as *array-num-none* for maxlen='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.%(funcname)s(floatarray1, testfloat, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(floatarray1, testfloat, maxlen='a')



	########################################################
	def test_%(funclabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for integer array - Array code %(typelabel)s.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(intarray1, testfloat, self.dataout)


	########################################################
	def test_%(funclabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for integer number - Array code %(typelabel)s.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(self.floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(self.floatarray1, testint, self.dataout)


	########################################################
	def test_%(funclabel)s_array_num_array_b3(self):
		"""Test %(funclabel)s as *array-num-array* for integer output array - Array code %(typelabel)s.
		"""
		for testfloat in self.floatarray2:
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(floatarray1, testfloat, self.intdataout)


	########################################################
	def test_%(funclabel)s_array_num_array_b4(self):
		"""Test %(funclabel)s as *array-num-array* for integer number and array - Array code %(typelabel)s.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(self.floatarray1, testfloat, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(self.intarray1, testint, self.intdataout)


	########################################################
	def test_%(funclabel)s_array_num_array_b5(self):
		"""Test %(funclabel)s as *array-num-array* for errors='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(floatarray1, testfloat, self.dataout, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(floatarray1, testfloat, self.dataout, errors='a')


	########################################################
	def test_%(funclabel)s_array_num_array_b6(self):
		"""Test %(funclabel)s as *array-num-array* for maxlen='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.%(funcname)s(floatarray1, testfloat, self.dataout, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(floatarray1, testfloat, self.dataout, maxlen='a')



	########################################################
	def test_%(funclabel)s_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for integer array - Array code %(typelabel)s.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testfloat, floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testfloat, intarray1)


	########################################################
	def test_%(funclabel)s_num_array_none_c2(self):
		"""Test %(funclabel)s as *num-array-none* for integer number - Array code %(typelabel)s.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testfloat, floatarray1)

				floatarray1 = copy.copy(self.floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testint, floatarray1)


	########################################################
	def test_%(funclabel)s_num_array_none_c3(self):
		"""Test %(funclabel)s as *num-array-none* for integer number and array - Array code %(typelabel)s.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testfloat, floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testint, intarray1)


	########################################################
	def test_%(funclabel)s_num_array_none_c4(self):
		"""Test %(funclabel)s as *num-array-none* for errors='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(testfloat, floatarray1, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(testfloat, floatarray1, errors='a')


	########################################################
	def test_%(funclabel)s_num_array_none_c5(self):
		"""Test %(funclabel)s as *num-array-none* for maxlen='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testfloat = self.floatarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.%(funcname)s(testfloat, floatarray1, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(testfloat, floatarray1, maxlen='a')



	########################################################
	def test_%(funclabel)s_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for integer array - Array code %(typelabel)s.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testfloat, self.intarray1, self.dataout)


	########################################################
	def test_%(funclabel)s_num_array_array_d2(self):
		"""Test %(funclabel)s as *num-array-array* for integer number - Array code %(typelabel)s.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testfloat, self.intarray1, self.dataout)


	########################################################
	def test_%(funclabel)s_num_array_array_d3(self):
		"""Test %(funclabel)s as *num-array-array* for integer output array - Array code %(typelabel)s.
		"""
		for testfloat in self.floatarray2:
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testfloat, self.floatarray1, self.intdataout)


	########################################################
	def test_%(funclabel)s_num_array_array_d4(self):
		"""Test %(funclabel)s as *num-array-array* for integer number and array - Array code %(typelabel)s.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testfloat, self.floatarray1, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.%(funcname)s(testint, self.intarray1, self.intdataout)


	########################################################
	def test_%(funclabel)s_num_array_array_d5(self):
		"""Test %(funclabel)s as *num-array-array* for errors='a' - Array code %(typelabel)s.
		"""
		testfloat = self.floatarray2[0]

		# This version is expected to pass.
		arrayfunc.%(funcname)s(testfloat, self.floatarray1, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(testfloat, self.intarray1, self.dataout, errors='a')


	########################################################
	def test_%(funclabel)s_num_array_array_d6(self):
		"""Test %(funclabel)s as *num-array-array* for maxlen='a' - Array code %(typelabel)s.
		"""
		testfloat = self.floatarray2[0]
		testmaxlen = len(self.floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.%(funcname)s(testfloat, self.floatarray1, self.dataout, maxlen=testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(testfloat, self.intarray1, self.dataout, maxlen='a')



	########################################################
	def test_%(funclabel)s_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for integer array - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This version is expected to pass.
		arrayfunc.%(funcname)s(floatarray1, self.floatarray2)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(floatarray1, self.intarray2)


	########################################################
	def test_%(funclabel)s_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for integer array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.floatarray1, self.floatarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.intarray1, self.floatarray2)


	########################################################
	def test_%(funclabel)s_array_array_none_e3(self):
		"""Test %(funclabel)s as *array-array-none* for all integer array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.floatarray1, self.floatarray2)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.intarray1, self.intarray2)


	########################################################
	def test_%(funclabel)s_array_array_none_e4(self):
		"""Test %(funclabel)s as *array-array-none* for errors='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This version is expected to pass.
		arrayfunc.%(funcname)s(floatarray1, self.floatarray2, matherrors=True)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(floatarray1, self.floatarray2, errors='a')


	########################################################
	def test_%(funclabel)s_array_array_none_e5(self):
		"""Test %(funclabel)s as *array-array-none* for maxlen='a' - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.%(funcname)s(floatarray1, self.floatarray2, maxlen=testmaxlen)

		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(floatarray1, self.floatarray2, maxlen='a')



	########################################################
	def test_%(funclabel)s_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for integer array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.floatarray1, self.intarray2, self.dataout)


	########################################################
	def test_%(funclabel)s_array_array_array_f2(self):
		"""Test %(funclabel)s as *array-array-array* for integer array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.intarray1, self.floatarray2, self.dataout)


	########################################################
	def test_%(funclabel)s_array_array_array_f3(self):
		"""Test %(funclabel)s as *array-array-array* for integer output array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.floatarray1, self.floatarray2, self.intdataout)


	########################################################
	def test_%(funclabel)s_array_array_array_f4(self):
		"""Test %(funclabel)s as *array-array-array* for all integer array - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.floatarray1, self.floatarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.intarray1, self.intarray2, self.intdataout)


	########################################################
	def test_%(funclabel)s_array_array_array_f5(self):
		"""Test %(funclabel)s as *array-array-array* for errors='a' - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.floatarray1, self.floatarray2, self.dataout, matherrors=True)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.floatarray1, self.floatarray2, self.dataout, errors='a')


	########################################################
	def test_%(funclabel)s_array_array_array_f6(self):
		"""Test %(funclabel)s as *array-array-array* for maxlen='a' - Array code %(typelabel)s.
		"""
		testmaxlen = len(self.floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.floatarray1, self.floatarray2, self.dataout, maxlen=testmaxlen)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s(self.floatarray1, self.floatarray2, self.dataout, maxlen='a')


	########################################################
	def test_%(funclabel)s_no_params_g1(self):
		"""Test %(funclabel)s with no parameters - Array code %(typelabel)s.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.%(funcname)s()



##############################################################################

'''

# ==============================================================================


# The template used to generate the tests for nan, inf, -inf in data arrays
# when exceptions are expected.
nan_data_error_template = '''

##############################################################################
class %(funclabel)s_%(errorlabel)s_errors_%(typelabel)s(unittest.TestCase):
	"""Test for basic general function operation using parameter %(errordata)s.
	nan_data_error_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
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
	def PyOp(self, x, y, default):
		"""Handle exceptions due to math domain errors when calling the math
		library function. If an exception occurs, return the default value
		instead.
		"""
		try:
			return %(pyoperator)s(x, y)
		except:
			return default


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('%(typecode)s', [%(test_op_x)s])
		self.dataok2 = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), self.dataok1)])

		arraysize =  len(self.dataok1)


		self.dataout = array.array('%(typecode)s', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('%(typecode)s', [float('%(errordata)s')] * arraysize)


		self.expectedep = [self.PyOp(x, y, float('%(test_nan_default)s')) for x,y in zip(self.errordata, self.dataok2)]
		self.expectedpe = [self.PyOp(y, x, float('%(test_nan_default)s')) for x,y in zip(self.errordata, self.dataok1)]


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(errordata, testval)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expectedep = [self.PyOp(x, testval, float('%(test_nan_default)s')) for x in self.errordata]

				arrayfunc.%(funcname)s(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(errordata, testval, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedep = [self.PyOp(x, testval, float('%(test_nan_default)s')) for x in self.errordata]

				arrayfunc.%(funcname)s(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testval, dataok1)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(testval, errordata)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_c2(self):
		"""Test %(funclabel)s as *num-array-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expectedpe = [self.PyOp(testval, x, float('%(test_nan_default)s')) for x in self.errordata]

				arrayfunc.%(funcname)s(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testval, self.dataok1, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(testval, self.errordata, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_d2(self):
		"""Test %(funclabel)s as *num-array-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedpe = [self.PyOp(testval, x, float('%(test_nan_default)s')) for x in self.errordata]

				arrayfunc.%(funcname)s(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.%(funcname)s(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(dataok1, self.errordata)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.dataok1, self.dataok2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(self.dataok1, self.errordata, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_f2(self):
		"""Test %(funclabel)s as *array-array-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

'''

# ==============================================================================

# The template used to generate the tests for nan, inf, -inf in data arrays
# when exceptions are not expected.
nan_data_noerror_template = '''

##############################################################################
class %(funclabel)s_%(errorlabel)s_noerrors_%(typelabel)s(unittest.TestCase):
	"""Test for basic general function operation using parameter %(errordata)s.
	nan_data_noerror_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
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
	def PyOp(self, x, y, default):
		"""Handle exceptions due to math domain errors when calling the math
		library function. If an exception occurs, return the default value
		instead.
		"""
		try:
			return %(pyoperator)s(x, y)
		except:
			return default


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		self.dataok1 = array.array('%(typecode)s', [%(test_op_x)s])
		self.dataok2 = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), self.dataok1)])

		arraysize =  len(self.dataok1)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('%(typecode)s', [float('%(errordata)s')] * arraysize)


		self.expectedep = [self.PyOp(x, y, float('%(test_nan_default)s')) for x,y in zip(self.errordata, self.dataok2)]
		self.expectedpe = [self.PyOp(y, x, float('%(test_nan_default)s')) for x,y in zip(self.errordata, self.dataok1)]


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.%(funcname)s(errordata, testval)

				for dataoutitem, expecteditem in zip(errordata, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.%(funcname)s(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.%(funcname)s(self.errordata, testval, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.%(funcname)s(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.%(funcname)s(testval, errordata)

				for dataoutitem, expecteditem in zip(errordata, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_c2(self):
		"""Test %(funclabel)s as *num-array-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				arrayfunc.%(funcname)s(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.%(funcname)s(testval, self.errordata, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_d2(self):
		"""Test %(funclabel)s as *num-array-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.%(funcname)s(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.dataok1, self.errordata)

		for dataoutitem, expecteditem in zip(self.dataok1, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.dataok1, self.errordata, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_f2(self):
		"""Test %(funclabel)s as *array-array-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

'''

# ==============================================================================


# The template used to generate the tests forinf, -inf in data arrays
# when exceptions are expected. This is a special version for fmod.
nan_data_fmod_inf_template = '''

##############################################################################
class %(funclabel)s_%(errorlabel)s_noerrors_%(typelabel)s(unittest.TestCase):
	"""Test for fmod(x, y) operation using parameter %(errordata)s.
	For math.fmod:
	if x=nan, the result is always nan
	if y=nan, the result is always nan
	if x=inf or -inf, the result is always err
	if y=inf or -inf, the result is OK
	For our purposes here, we treat a "NaN" output as an error even if 
	"math.fmod" does not.
	nan_data_fmod_inf_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
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
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


		# A "1" suffix means the data is meant for the first parameter. 
		# A "2" suffix means the data is meant for the second parameter.
		self.okarray1 = array.array('%(typecode)s', [%(test_op_x)s])
		self.okarray2 = array.array('%(typecode)s', [x for x,y in zip(itertools.cycle([%(test_op_y)s]), self.okarray1)])


		# This is how long the test arrays should be.
		testarraysize = len(self.okarray1)

		self.dataout = array.array('%(typecode)s', itertools.repeat(0.0, testarraysize))

		self.errorarray = array.array('%(typecode)s', [float('%(errordata)s')] * testarraysize)
		self.errorparam = float('%(errordata)s')

		# When error data is calculated with error checking off, the result is
		# always NaN.
		self.nanresult = [float('nan')] * testarraysize



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for error array with error check on - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errorarray = copy.copy(self.errorarray)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(okarray1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(errorarray, testval)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for error array with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errorarray = copy.copy(self.errorarray)

				# The output goes into the first array.
				arrayfunc.%(funcname)s(errorarray, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errorarray, self.nanresult):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_a3(self):
		"""Test %(funclabel)s as *array-num-array* for error array with error check on - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errorarray = copy.copy(self.errorarray)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(okarray1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(errorarray, testval, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_a4(self):
		"""Test %(funclabel)s as *array-num-array* for error array with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				arrayfunc.%(funcname)s(self.errorarray, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, self.nanresult):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a5(self):
		"""Test %(funclabel)s as *array-num-none* for error number with error check on - Array code %(typelabel)s.
		"""
		expected = [%(pyoperator)s(x, self.errorparam) for x in self.okarray1]

		# The output goes into the first array.
		arrayfunc.%(funcname)s(self.okarray1, self.errorparam)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a6(self):
		"""Test %(funclabel)s as *array-num-none* for error number with error check off - Array code %(typelabel)s.
		"""
		expected = [%(pyoperator)s(x, self.errorparam) for x in self.okarray1]

		# The output goes into the first array.
		arrayfunc.%(funcname)s(self.okarray1, self.errorparam, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_a7(self):
		"""Test %(funclabel)s as *array-num-array* for error number with error check on - Array code %(typelabel)s.
		"""
		expected = [%(pyoperator)s(x, self.errorparam) for x in self.okarray1]

		arrayfunc.%(funcname)s(self.okarray1, self.errorparam, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_a8(self):
		"""Test %(funclabel)s as *array-num-array* for error number with error check off - Array code %(typelabel)s.
		"""
		expected = [%(pyoperator)s(x, self.errorparam) for x in self.okarray1]

		arrayfunc.%(funcname)s(self.okarray1, self.errorparam, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_b1(self):
		"""Test %(funclabel)s as *num-array-none* for error number with error check on - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray2 = copy.copy(self.okarray2)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testval, okarray2)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(self.errorparam, okarray2)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_b2(self):
		"""Test %(funclabel)s as *num-array-none* for error number with error check off - Array code %(typelabel)s.
		"""
		# The output goes into the first array.
		arrayfunc.%(funcname)s(self.errorparam, self.okarray2, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray2, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_b3(self):
		"""Test %(funclabel)s as *num-array-array* for error number with error check on - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testval, self.okarray2, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(self.errorparam, self.okarray2, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_b4(self):
		"""Test %(funclabel)s as *num-array-array* for error number with error check off - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.errorparam, self.okarray2, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_b5(self):
		"""Test %(funclabel)s as *num-array-none* for error array with error check on - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errorarray = copy.copy(self.errorarray)

				expected = [%(pyoperator)s(testval, x) for x in self.errorarray]

				# The output goes into the first array.
				arrayfunc.%(funcname)s(testval, errorarray)

				for dataoutitem, expecteditem in zip(errorarray, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_b6(self):
		"""Test %(funclabel)s as *num-array-none* for error array with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errorarray = copy.copy(self.errorarray)

				expected = [%(pyoperator)s(testval, x) for x in self.errorarray]

				# The output goes into the first array.
				arrayfunc.%(funcname)s(testval, errorarray, matherrors=True)

				for dataoutitem, expecteditem in zip(errorarray, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_b7(self):
		"""Test %(funclabel)s as *num-array-array* for error array with error check on - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [%(pyoperator)s(testval, x) for x in self.errorarray]

				arrayfunc.%(funcname)s(testval, self.errorarray, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_b8(self):
		"""Test %(funclabel)s as *num-array-array* for error array with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [%(pyoperator)s(testval, x) for x in self.errorarray]

				arrayfunc.%(funcname)s(testval, self.errorarray, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_c1(self):
		"""Test %(funclabel)s as *array-array-none* for error array with error check on - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.okarray1, self.okarray2)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(self.errorarray, self.okarray2)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_c2(self):
		"""Test %(funclabel)s as *array-array-none* for error array with error check off - Array code %(typelabel)s.
		"""
		# The output goes into the first array.
		arrayfunc.%(funcname)s(self.errorarray, self.okarray2, matherrors=True)

		for dataoutitem, expecteditem in zip(self.errorarray, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_c3(self):
		"""Test %(funclabel)s as *array-array-array* for error array with error check on - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.okarray1, self.okarray2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(self.errorarray, self.okarray2, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_c4(self):
		"""Test %(funclabel)s as *array-array-array* for error array with error check off - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.errorarray, self.okarray2, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.nanresult):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_c5(self):
		"""Test %(funclabel)s as *array-array-none* for error array with error check on - Array code %(typelabel)s.
		"""
		expected = [%(pyoperator)s(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		# The output goes into the first array.
		arrayfunc.%(funcname)s(self.okarray1, self.errorarray)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_c6(self):
		"""Test %(funclabel)s as *array-array-none* for error array with error check off - Array code %(typelabel)s.
		"""
		expected = [%(pyoperator)s(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		# The output goes into the first array.
		arrayfunc.%(funcname)s(self.okarray1, self.errorarray, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_c7(self):
		"""Test %(funclabel)s as *array-array-array* for error array with error check on - Array code %(typelabel)s.
		"""
		expected = [%(pyoperator)s(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		arrayfunc.%(funcname)s(self.okarray1, self.errorarray, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_c8(self):
		"""Test %(funclabel)s as *array-array-array* for error array with error check off - Array code %(typelabel)s.
		"""
		expected = [%(pyoperator)s(x, y) for x,y in zip(self.okarray1, self.errorarray)]

		arrayfunc.%(funcname)s(self.okarray1, self.errorarray, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

'''


# ==============================================================================

# Used for pow only.
nan_data_powerror_template = '''

##############################################################################
class %(funclabel)s_%(errorlabel)s_errors_%(typelabel)s(unittest.TestCase):
	"""Test for pow using parameter %(errordata)s.
	nan_data_powerror_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
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
	def PyOp(self, x, y, default):
		"""Handle exceptions due to math domain errors when calling the math
		library function. If an exception occurs, return the default value
		instead.
		"""
		try:
			return %(pyoperator)s(x, y)
		except:
			return default


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('%(typecode)s', [%(test_op_x)s])
		self.dataok2 = array.array('%(typecode)s', [x for (x,y) in zip(itertools.cycle([%(test_op_y)s]), self.dataok1)])

		arraysize =  len(self.dataok1)


		self.dataout = array.array('%(typecode)s', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('%(typecode)s', [float('%(errordata)s')] * arraysize)


		self.expectedep = [self.PyOp(x, y, float('%(test_nan_default)s')) for x,y in zip(self.errordata, self.dataok2)]
		self.expectedpe = [self.PyOp(y, x, float('%(test_nan_default)s')) for x,y in zip(self.errordata, self.dataok1)]


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(dataok1, testval)

				# This is the actual test. When the test value parameter is 0, 
				# no error is expected. Any other value should raise an error.
				if testval != 0.0:
					with self.assertRaises(ArithmeticError):
						arrayfunc.%(funcname)s(errordata, testval)
				else:
					arrayfunc.%(funcname)s(errordata, testval)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expectedep = [self.PyOp(x, testval, float('%(test_nan_default)s')) for x in self.errordata]

				arrayfunc.%(funcname)s(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(dataok1, testval, self.dataout)

				# This is the actual test. When the test value parameter is 0, 
				# no error is expected. Any other value should raise an error.
				if testval != 0.0:
					with self.assertRaises(ArithmeticError):
						arrayfunc.%(funcname)s(errordata, testval, self.dataout)
				else:
					arrayfunc.%(funcname)s(errordata, testval, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedep = [self.PyOp(x, testval, float('%(test_nan_default)s')) for x in self.errordata]

				arrayfunc.%(funcname)s(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testval, dataok1)

				# This is the actual test. When testing for errors, the result 
				# will depend upon whether the test is for nan or inf, and 
				# what numeric values are involved. 
				# The template auto-generating this unit test is re-used for
				# different test values, so we need a conditional test for this.
				if '%(errordata)s' == 'nan' and testval != 1.0:
					with self.assertRaises(ArithmeticError):
						arrayfunc.%(funcname)s(testval, errordata)
				elif '%(errordata)s' == 'inf' and ((testval < -1.0) or (testval > 1.0)):
					with self.assertRaises(ArithmeticError):
						arrayfunc.%(funcname)s(testval, errordata)
				elif '%(errordata)s' == '-inf' and ((testval > -1.0) and (testval < 1.0)):
					with self.assertRaises(ArithmeticError):
						arrayfunc.%(funcname)s(testval, errordata)
				else:
					arrayfunc.%(funcname)s(testval, errordata)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_c2(self):
		"""Test %(funclabel)s as *num-array-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)
				expectedpe = [self.PyOp(testval, x, float('%(test_nan_default)s')) for x in self.errordata]

				arrayfunc.%(funcname)s(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_y)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# This version is expected to pass.
				arrayfunc.%(funcname)s(testval, self.dataok1, self.dataout)

				# This is the actual test. When testing for errors, the result 
				# will depend upon whether the test is for nan or inf, and 
				# what numeric values are involved. 
				# The template auto-generating this unit test is re-used for
				# different test values, so we need a conditional test for this.
				if '%(errordata)s' == 'nan' and testval != 1.0:
					with self.assertRaises(ArithmeticError):
						arrayfunc.%(funcname)s(testval, self.errordata, self.dataout)
				elif '%(errordata)s' == 'inf' and ((testval < -1.0) or (testval > 1.0)):
					with self.assertRaises(ArithmeticError):
						arrayfunc.%(funcname)s(testval, self.errordata, self.dataout)
				elif '%(errordata)s' == '-inf' and ((testval > -1.0) and (testval < 1.0)):
					with self.assertRaises(ArithmeticError):
						arrayfunc.%(funcname)s(testval, self.errordata, self.dataout)
				else:
					arrayfunc.%(funcname)s(testval, self.errordata, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_d2(self):
		"""Test %(funclabel)s as *num-array-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in [%(test_op_x)s]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedpe = [self.PyOp(testval, x, float('%(test_nan_default)s')) for x in self.errordata]

				arrayfunc.%(funcname)s(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedpe):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)
		dataok2 = copy.copy(self.dataok2)

		# This version is expected to pass.
		arrayfunc.%(funcname)s(dataok1, dataok2)

		# Copy the array so we don't change the original data.
		dataok1 = copy.copy(self.dataok1)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(dataok1, self.errordata)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.dataok1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataok1, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		# This version is expected to pass.
		arrayfunc.%(funcname)s(self.dataok1, self.dataok2, self.dataout)

		# This is the actual test.
		with self.assertRaises(ArithmeticError):
			arrayfunc.%(funcname)s(self.dataok1, self.errordata, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_f2(self):
		"""Test %(funclabel)s as *array-array-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		arrayfunc.%(funcname)s(self.dataok1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, self.expectedpe):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)

'''

##############################################################################


# ==============================================================================


# The template used to generate the tests for nan, inf, -inf in data arrays
# specifically for copysign.
nan_data_copysign_template = '''

##############################################################################
class %(funclabel)s_%(errorlabel)s_errors_%(typelabel)s(unittest.TestCase):
	"""Test for copysign function operation using parameter %(errordata)s.
	nan_data_copysign_template
	"""


	##############################################################################
	def FloatassertEqual(self, expecteditem, dataoutitem, msg=None):
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
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.okarray1 = array.array('%(typecode)s', [%(test_op_y)s])
		# This is the same data, but with signs reversed.
		self.okarray2 = array.array('%(typecode)s', [-x for x in [%(test_op_y)s]])

		arraysize =  len(self.okarray1)


		self.dataout = array.array('%(typecode)s', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('%(typecode)s', [float('%(errordata)s')] * arraysize)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a1(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(okarray1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(errordata, testval)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_none_a2(self):
		"""Test %(funclabel)s as *array-num-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.%(funcname)s(x, testval) for x in errordata]

				arrayfunc.%(funcname)s(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b1(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.%(funcname)s(okarray1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.%(funcname)s(errordata, testval, self.dataout)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_num_array_b2(self):
		"""Test %(funclabel)s as *array-num-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.%(funcname)s(x, testval) for x in self.errordata]

				arrayfunc.%(funcname)s(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_c1(self):
		"""Test %(funclabel)s as *num-array-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				okarray1 = copy.copy(self.okarray1)
				errordata = copy.copy(self.errordata)

				expected = [math.%(funcname)s(testval, x) for x in errordata]

				arrayfunc.%(funcname)s(testval, errordata)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_none_c2(self):
		"""Test %(funclabel)s as *num-array-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expected = [math.%(funcname)s(testval, x) for x in errordata]

				arrayfunc.%(funcname)s(testval, errordata, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_d1(self):
		"""Test %(funclabel)s as *num-array-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.%(funcname)s(testval, x) for x in self.errordata]

				arrayfunc.%(funcname)s(testval, self.errordata, self.dataout)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_num_array_array_d2(self):
		"""Test %(funclabel)s as *num-array-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		for testval in self.okarray2:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expected = [math.%(funcname)s(testval, x) for x in self.errordata]

				arrayfunc.%(funcname)s(testval, self.errordata, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_e1(self):
		"""Test %(funclabel)s as *array-array-none* for %(errordata)s - Array code %(typelabel)s.
		"""
		expected = [math.%(funcname)s(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.%(funcname)s(self.okarray1, self.errordata)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_none_e2(self):
		"""Test %(funclabel)s as *array-array-none* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		expected = [math.%(funcname)s(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.%(funcname)s(self.okarray1, self.errordata, matherrors=True)

		for dataoutitem, expecteditem in zip(self.okarray1, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_f1(self):
		"""Test %(funclabel)s as *array-array-array* for %(errordata)s - Array code %(typelabel)s.
		"""
		expected = [math.%(funcname)s(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.%(funcname)s(self.okarray1, self.errordata, self.dataout)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_%(funclabel)s_%(errorlabel)s_array_array_array_f2(self):
		"""Test %(funclabel)s as *array-array-array* for %(errordata)s with error check off - Array code %(typelabel)s.
		"""
		expected = [math.%(funcname)s(x, y) for x,y in zip(self.okarray1, self.errordata)]

		arrayfunc.%(funcname)s(self.okarray1, self.errordata, self.dataout, matherrors=True)

		for dataoutitem, expecteditem in zip(self.dataout, expected):
			# The behavour of assertEqual is modified by addTypeEqualityFunc.
			self.assertEqual(dataoutitem, expecteditem)


##############################################################################

'''


# ==============================================================================

# ==============================================================================

# These are all the test code templates. 
test_templates = {'test_template' : test_template,
			'nan_data_error_template' : nan_data_error_template,
			'nan_data_noerror_template' : nan_data_noerror_template,
			'nan_data_powerror_template' : nan_data_powerror_template,
			'nan_data_fmod_inf_template' : nan_data_fmod_inf_template,
			'nan_data_copysign_template' : nan_data_copysign_template,
}


# ==============================================================================

# Read in the op codes.
oplist = codegen_common.ReadCSVData('funcs.csv')


# Filter out the desired math functions.
funclist = [x for x in oplist if x['test_op_templ'] == 'test_template']

# ==============================================================================



for func in funclist:

	funcname = func['funcname']
	filenamebase = 'test_' + funcname
	filename = filenamebase + '.py'
	headerdate = codegen_common.FormatHeaderData(filenamebase, '09-Dec-2017', funcname)

	# One function (one output file). 
	with open(filename, 'w') as f:
		# The copyright header.
		f.write(codegen_common.HeaderTemplate % headerdate)


		# Check each array type.
		for functype in codegen_common.floatarrays:
			testtemplate = test_templates[func['test_op_templ']]
			# Basic tests.
			funcdata = {'funclabel' : func['funcname'], 'funcname' : funcname, 'pyoperator' : func['pyoperator'],
				'typelabel' : functype, 'typecode' : functype, 'test_op_x' : func['test_op_x'],
				'test_op_y' : func['test_op_y']}

			f.write(testtemplate % funcdata)

			# Test for invalid parameters. One template should work for all 
			# functions of this style.
			f.write(param_invalid_template % funcdata)

			# NaN, inf, -inf tests.
			funcdata = {'funclabel' : func['funcname'], 'funcname' : funcname, 'pyoperator' : func['pyoperator'],
				'typelabel' : functype, 'typecode' : functype, 'test_op_x' : func['test_op_x'],
				'test_op_y' : func['test_op_y'],
				'test_nan_default' : func['test_nan_default']
				}

			# NaN
			testtemplate = test_templates[func['test_nan_data_template']]
			funcdata['errorlabel'] = 'NaN'
			funcdata['errordata'] = 'nan'
			f.write(testtemplate % funcdata)

			# inf
			testtemplate = test_templates[func['test_inf_data_template']]
			funcdata['errorlabel'] = 'inf'
			funcdata['errordata'] = 'inf'
			f.write(testtemplate % funcdata)

			# -inf
			testtemplate = test_templates[func['test_ninf_data_template']]
			funcdata['errorlabel'] = 'ninf'
			funcdata['errordata'] = '-inf'
			f.write(testtemplate % funcdata)


		f.write(codegen_common.testendtemplate % funcname)

# ==============================================================================

