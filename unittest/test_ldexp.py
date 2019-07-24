#!/usr/bin/env python3
##############################################################################
# Project:  arrayfunc
# Module:   test_ldexp.py
# Purpose:  arrayfunc unit test.
# Language: Python 3.4
# Date:     09-Dec-2017.
# Ver:      06-Apr-2019.
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
"""This conducts unit tests for ldexp.
"""

##############################################################################
import sys

import array
import itertools
import math
import operator
import platform
import copy

import unittest

import arrayfunc

##############################################################################

##############################################################################

# The following code is all auto-generated.




##############################################################################
class ldexp_general_f(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data -2, -1, 0, 1, 2.
	test_template_ldexp
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


	########################################################
	def test_ldexp_basic_array_num_none_a1(self):
		"""Test ldexp as *array-num-none* for basic function - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.ldexp(x, testval) for x in data1]

				arrayfunc.ldexp(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ldexp_basic_array_num_none_a2(self):
		"""Test ldexp as *array-num-none* for basic function with matherrors=True - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.ldexp(x, testval) for x in data1]

				arrayfunc.ldexp(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ldexp_basic_array_num_none_a3(self):
		"""Test ldexp as *array-num-none* for basic function with array limit - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.ldexp(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.ldexp(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ldexp_basic_array_num_none_a4(self):
		"""Test ldexp as *array-num-none* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.ldexp(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.ldexp(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_ldexp_basic_array_num_array_b1(self):
		"""Test ldexp as *array-num-array* for basic function - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				expected = [math.ldexp(x, testval) for x in data1]

				arrayfunc.ldexp(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ldexp_basic_array_num_array_b2(self):
		"""Test ldexp as *array-num-array* for basic function with matherrors=True - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				expected = [math.ldexp(x, testval) for x in data1]

				arrayfunc.ldexp(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ldexp_basic_array_num_array_b3(self):
		"""Test ldexp as *array-num-array* for basic function with array limit - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.ldexp(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.ldexp(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ldexp_basic_array_num_array_b4(self):
		"""Test ldexp as *array-num-array* for basic function with matherrors=True and with array limit - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('f', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.ldexp(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.ldexp(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class ldexp_param_errors_f(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.floatarray1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.floatarray2 = array.array('f', [x for (x,y) in zip(itertools.cycle([-2, -1, 0, 1, 2]), self.floatarray1)])

		arraysize =  len(self.floatarray1)

		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray1 = array.array('i', [int(x) for x in self.floatarray1])
		self.intarray2 = array.array('i', [int(x) for x in self.floatarray2])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_ldexp_array_num_none_a1(self):
		"""Test ldexp as *array-num-none* for integer array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.ldexp(floatarray1, testint)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.ldexp(intarray1, testint)


	########################################################
	def test_ldexp_array_num_none_a2(self):
		"""Test ldexp as *array-num-none* for float number - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.ldexp(floatarray1, testint)

				floatarray1 = copy.copy(self.floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.ldexp(floatarray1, testfloat)


	########################################################
	def test_ldexp_array_num_none_a3(self):
		"""Test ldexp as *array-num-none* for integer number and array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.ldexp(floatarray1, testint)

				intarray1 = copy.copy(self.intarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.ldexp(intarray1, testint)


	########################################################
	def test_ldexp_array_num_none_a4(self):
		"""Test ldexp as *array-num-none* for matherrors='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testint = self.intarray1[0]

		# This version is expected to pass.
		arrayfunc.ldexp(floatarray1, testint, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ldexp(floatarray1, testint, matherrors='a')


	########################################################
	def test_ldexp_array_num_none_a5(self):
		"""Test ldexp as *array-num-none* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testint = self.intarray1[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.ldexp(floatarray1, testint, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ldexp(floatarray1, testint, maxlen='a')



	########################################################
	def test_ldexp_array_num_array_b1(self):
		"""Test ldexp as *array-num-array* for integer array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.ldexp(floatarray1, testint, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.ldexp(intarray1, testint, self.dataout)


	########################################################
	def test_ldexp_array_num_array_b2(self):
		"""Test ldexp as *array-num-array* for float number - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.ldexp(self.floatarray1, testint, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.ldexp(self.floatarray1, testfloat, self.dataout)


	########################################################
	def test_ldexp_array_num_array_b3(self):
		"""Test ldexp as *array-num-array* for integer output array - Array code f.
		"""
		for testint in self.intarray2:
			with self.subTest(msg='Failed with parameter', testint = testint):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.ldexp(floatarray1, testint, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.ldexp(floatarray1, testint, self.intdataout)


	########################################################
	def test_ldexp_array_num_array_b4(self):
		"""Test ldexp as *array-num-array* for integer number and array - Array code f.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.ldexp(self.floatarray1, testint, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.ldexp(self.intarray1, testint, self.intdataout)


	########################################################
	def test_ldexp_array_num_array_b5(self):
		"""Test ldexp as *array-num-array* for matherrors='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testint = self.intarray2[0]

		# This version is expected to pass.
		arrayfunc.ldexp(floatarray1, testint, self.dataout, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ldexp(floatarray1, testint, self.dataout, matherrors='a')


	########################################################
	def test_ldexp_array_num_array_b6(self):
		"""Test ldexp as *array-num-array* for maxlen='a' - Array code f.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testint = self.intarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.ldexp(floatarray1, testint, self.dataout, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ldexp(floatarray1, testint, self.dataout, maxlen='a')



	########################################################
	def test_ldexp_array_num_array_c1(self):
		"""Test ldexp as *array* for missing numeric parameter - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.ldexp(self.floatarray1)


	########################################################
	def test_ldexp_array_num_array_c2(self):
		"""Test ldexp as *num* for missing array parameter - Array code f.
		"""
		testint = self.intarray2[0]
		with self.assertRaises(TypeError):
			arrayfunc.ldexp(testint)


	########################################################
	def test_ldexp_array_num_array_c3(self):
		"""Test ldexp as *array* for missing numeric parameter with maxlen - Array code f.
		"""
		testmaxlen = len(self.floatarray1) // 2
		with self.assertRaises(TypeError):
			arrayfunc.ldexp(self.floatarray1, maxlen=testmaxlen)


	########################################################
	def test_ldexp_array_num_array_c4(self):
		"""Test ldexp as *num* for missing array parameter with maxlen - Array code f.
		"""
		testmaxlen = len(self.floatarray1) // 2
		testint = self.intarray2[0]
		with self.assertRaises(TypeError):
			arrayfunc.ldexp(testint, maxlen=testmaxlen)



	########################################################
	def test_ldexp_no_params_d1(self):
		"""Test ldexp with no parameters - Array code f.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.ldexp()



##############################################################################



##############################################################################
class ldexp_NaN_errors_f(unittest.TestCase):
	"""Test for basic general function operation using parameter nan.
	nan_data_error_ldexp_template
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

		arraysize =  len(self.dataok1)


		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('nan')] * arraysize)


		self.expectedep = [math.ldexp(x, y) for x,y in zip(self.errordata, itertools.cycle([-2, -1, 0, 1, 2]))]


	########################################################
	def test_ldexp_NaN_array_num_none_a1(self):
		"""Test ldexp as *array-num-none* for nan - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.ldexp(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.ldexp(errordata, testval)


	########################################################
	def test_ldexp_NaN_array_num_none_a2(self):
		"""Test ldexp as *array-num-none* for nan with error check off - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expectedep = [math.ldexp(x, testval) for x in self.errordata]

				arrayfunc.ldexp(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_ldexp_NaN_array_num_array_b1(self):
		"""Test ldexp as *array-num-array* for nan - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.ldexp(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.ldexp(errordata, testval, self.dataout)


	########################################################
	def test_ldexp_NaN_array_num_array_b2(self):
		"""Test ldexp as *array-num-array* for nan with error check off - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedep = [math.ldexp(x, testval) for x in self.errordata]

				arrayfunc.ldexp(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class ldexp_inf_errors_f(unittest.TestCase):
	"""Test for basic general function operation using parameter inf.
	nan_data_error_ldexp_template
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

		arraysize =  len(self.dataok1)


		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('inf')] * arraysize)


		self.expectedep = [math.ldexp(x, y) for x,y in zip(self.errordata, itertools.cycle([-2, -1, 0, 1, 2]))]


	########################################################
	def test_ldexp_inf_array_num_none_a1(self):
		"""Test ldexp as *array-num-none* for inf - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.ldexp(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.ldexp(errordata, testval)


	########################################################
	def test_ldexp_inf_array_num_none_a2(self):
		"""Test ldexp as *array-num-none* for inf with error check off - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expectedep = [math.ldexp(x, testval) for x in self.errordata]

				arrayfunc.ldexp(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_ldexp_inf_array_num_array_b1(self):
		"""Test ldexp as *array-num-array* for inf - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.ldexp(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.ldexp(errordata, testval, self.dataout)


	########################################################
	def test_ldexp_inf_array_num_array_b2(self):
		"""Test ldexp as *array-num-array* for inf with error check off - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedep = [math.ldexp(x, testval) for x in self.errordata]

				arrayfunc.ldexp(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class ldexp_ninf_errors_f(unittest.TestCase):
	"""Test for basic general function operation using parameter -inf.
	nan_data_error_ldexp_template
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('f', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

		arraysize =  len(self.dataok1)


		self.dataout = array.array('f', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('f', [float('-inf')] * arraysize)


		self.expectedep = [math.ldexp(x, y) for x,y in zip(self.errordata, itertools.cycle([-2, -1, 0, 1, 2]))]


	########################################################
	def test_ldexp_ninf_array_num_none_a1(self):
		"""Test ldexp as *array-num-none* for -inf - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.ldexp(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.ldexp(errordata, testval)


	########################################################
	def test_ldexp_ninf_array_num_none_a2(self):
		"""Test ldexp as *array-num-none* for -inf with error check off - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expectedep = [math.ldexp(x, testval) for x in self.errordata]

				arrayfunc.ldexp(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_ldexp_ninf_array_num_array_b1(self):
		"""Test ldexp as *array-num-array* for -inf - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.ldexp(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.ldexp(errordata, testval, self.dataout)


	########################################################
	def test_ldexp_ninf_array_num_array_b2(self):
		"""Test ldexp as *array-num-array* for -inf with error check off - Array code f.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedep = [math.ldexp(x, testval) for x in self.errordata]

				arrayfunc.ldexp(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class ldexp_general_d(unittest.TestCase):
	"""Test for basic general function operation using numeric 
	data -2, -1, 0, 1, 2.
	test_template_ldexp
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))


	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)


	########################################################
	def test_ldexp_basic_array_num_none_a1(self):
		"""Test ldexp as *array-num-none* for basic function - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.ldexp(x, testval) for x in data1]

				arrayfunc.ldexp(data1, testval)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ldexp_basic_array_num_none_a2(self):
		"""Test ldexp as *array-num-none* for basic function with matherrors=True - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				expected = [math.ldexp(x, testval) for x in data1]

				arrayfunc.ldexp(data1, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ldexp_basic_array_num_none_a3(self):
		"""Test ldexp as *array-num-none* for basic function with array limit - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.ldexp(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.ldexp(data1, testval, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ldexp_basic_array_num_none_a4(self):
		"""Test ldexp as *array-num-none* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

				limited = len(data1) // 2

				pydataout = [math.ldexp(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(data1)[limited:]

				arrayfunc.ldexp(data1, testval, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(data1, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_ldexp_basic_array_num_array_b1(self):
		"""Test ldexp as *array-num-array* for basic function - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				expected = [math.ldexp(x, testval) for x in data1]

				arrayfunc.ldexp(data1, testval, dataout)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ldexp_basic_array_num_array_b2(self):
		"""Test ldexp as *array-num-array* for basic function with matherrors=True - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				expected = [math.ldexp(x, testval) for x in data1]

				arrayfunc.ldexp(data1, testval, dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ldexp_basic_array_num_array_b3(self):
		"""Test ldexp as *array-num-array* for basic function with array limit - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.ldexp(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.ldexp(data1, testval, dataout, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)


	########################################################
	def test_ldexp_basic_array_num_array_b4(self):
		"""Test ldexp as *array-num-array* for basic function with matherrors=True and with array limit - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				data1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
				dataout = array.array('d', [0]*len(data1))

				limited = len(data1) // 2

				pydataout = [math.ldexp(x, testval) for x in data1]
				expected = pydataout[0:limited] + list(dataout)[limited:]

				arrayfunc.ldexp(data1, testval, dataout, matherrors=True, maxlen=limited)

				for dataoutitem, expecteditem in zip(dataout, expected):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class ldexp_param_errors_d(unittest.TestCase):
	"""Test for invalid parameters.
	param_invalid_template
	"""


	########################################################
	def setUp(self):
		"""Initialise.
		"""

		self.floatarray1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])
		self.floatarray2 = array.array('d', [x for (x,y) in zip(itertools.cycle([-2, -1, 0, 1, 2]), self.floatarray1)])

		arraysize =  len(self.floatarray1)

		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		# Create some integer array equivalents.
		self.intarray1 = array.array('i', [int(x) for x in self.floatarray1])
		self.intarray2 = array.array('i', [int(x) for x in self.floatarray2])

		self.intdataout = array.array('i', [int(x) for x in self.dataout])


	########################################################
	def test_ldexp_array_num_none_a1(self):
		"""Test ldexp as *array-num-none* for integer array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.ldexp(floatarray1, testint)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.ldexp(intarray1, testint)


	########################################################
	def test_ldexp_array_num_none_a2(self):
		"""Test ldexp as *array-num-none* for float number - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.ldexp(floatarray1, testint)

				floatarray1 = copy.copy(self.floatarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.ldexp(floatarray1, testfloat)


	########################################################
	def test_ldexp_array_num_none_a3(self):
		"""Test ldexp as *array-num-none* for integer number and array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.ldexp(floatarray1, testint)

				intarray1 = copy.copy(self.intarray1)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.ldexp(intarray1, testint)


	########################################################
	def test_ldexp_array_num_none_a4(self):
		"""Test ldexp as *array-num-none* for matherrors='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testint = self.intarray1[0]

		# This version is expected to pass.
		arrayfunc.ldexp(floatarray1, testint, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ldexp(floatarray1, testint, matherrors='a')


	########################################################
	def test_ldexp_array_num_none_a5(self):
		"""Test ldexp as *array-num-none* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testint = self.intarray1[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.ldexp(floatarray1, testint, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ldexp(floatarray1, testint, maxlen='a')



	########################################################
	def test_ldexp_array_num_array_b1(self):
		"""Test ldexp as *array-num-array* for integer array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.ldexp(floatarray1, testint, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.ldexp(intarray1, testint, self.dataout)


	########################################################
	def test_ldexp_array_num_array_b2(self):
		"""Test ldexp as *array-num-array* for float number - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# Copy the array so we don't change the original data.
				intarray1 = copy.copy(self.intarray1)

				# This version is expected to pass.
				arrayfunc.ldexp(self.floatarray1, testint, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.ldexp(self.floatarray1, testfloat, self.dataout)


	########################################################
	def test_ldexp_array_num_array_b3(self):
		"""Test ldexp as *array-num-array* for integer output array - Array code d.
		"""
		for testint in self.intarray2:
			with self.subTest(msg='Failed with parameter', testint = testint):

				# Copy the array so we don't change the original data.
				floatarray1 = copy.copy(self.floatarray1)

				# This version is expected to pass.
				arrayfunc.ldexp(floatarray1, testint, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.ldexp(floatarray1, testint, self.intdataout)


	########################################################
	def test_ldexp_array_num_array_b4(self):
		"""Test ldexp as *array-num-array* for integer number and array - Array code d.
		"""
		for testfloat, testint in zip(self.floatarray2, self.intarray2):
			with self.subTest(msg='Failed with parameter', testfloat = testfloat):

				# This version is expected to pass.
				arrayfunc.ldexp(self.floatarray1, testint, self.dataout)

				# This is the actual test.
				with self.assertRaises(TypeError):
					arrayfunc.ldexp(self.intarray1, testint, self.intdataout)


	########################################################
	def test_ldexp_array_num_array_b5(self):
		"""Test ldexp as *array-num-array* for matherrors='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testint = self.intarray2[0]

		# This version is expected to pass.
		arrayfunc.ldexp(floatarray1, testint, self.dataout, matherrors=True)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ldexp(floatarray1, testint, self.dataout, matherrors='a')


	########################################################
	def test_ldexp_array_num_array_b6(self):
		"""Test ldexp as *array-num-array* for maxlen='a' - Array code d.
		"""
		# Copy the array so we don't change the original data.
		floatarray1 = copy.copy(self.floatarray1)
		testint = self.intarray2[0]
		testmaxlen = len(floatarray1) // 2

		# This version is expected to pass.
		arrayfunc.ldexp(floatarray1, testint, self.dataout, maxlen=testmaxlen)

		floatarray1 = copy.copy(self.floatarray1)

		# This is the actual test.
		with self.assertRaises(TypeError):
			arrayfunc.ldexp(floatarray1, testint, self.dataout, maxlen='a')



	########################################################
	def test_ldexp_array_num_array_c1(self):
		"""Test ldexp as *array* for missing numeric parameter - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.ldexp(self.floatarray1)


	########################################################
	def test_ldexp_array_num_array_c2(self):
		"""Test ldexp as *num* for missing array parameter - Array code d.
		"""
		testint = self.intarray2[0]
		with self.assertRaises(TypeError):
			arrayfunc.ldexp(testint)


	########################################################
	def test_ldexp_array_num_array_c3(self):
		"""Test ldexp as *array* for missing numeric parameter with maxlen - Array code d.
		"""
		testmaxlen = len(self.floatarray1) // 2
		with self.assertRaises(TypeError):
			arrayfunc.ldexp(self.floatarray1, maxlen=testmaxlen)


	########################################################
	def test_ldexp_array_num_array_c4(self):
		"""Test ldexp as *num* for missing array parameter with maxlen - Array code d.
		"""
		testmaxlen = len(self.floatarray1) // 2
		testint = self.intarray2[0]
		with self.assertRaises(TypeError):
			arrayfunc.ldexp(testint, maxlen=testmaxlen)



	########################################################
	def test_ldexp_no_params_d1(self):
		"""Test ldexp with no parameters - Array code d.
		"""
		with self.assertRaises(TypeError):
			arrayfunc.ldexp()



##############################################################################



##############################################################################
class ldexp_NaN_errors_d(unittest.TestCase):
	"""Test for basic general function operation using parameter nan.
	nan_data_error_ldexp_template
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

		arraysize =  len(self.dataok1)


		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('nan')] * arraysize)


		self.expectedep = [math.ldexp(x, y) for x,y in zip(self.errordata, itertools.cycle([-2, -1, 0, 1, 2]))]


	########################################################
	def test_ldexp_NaN_array_num_none_a1(self):
		"""Test ldexp as *array-num-none* for nan - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.ldexp(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.ldexp(errordata, testval)


	########################################################
	def test_ldexp_NaN_array_num_none_a2(self):
		"""Test ldexp as *array-num-none* for nan with error check off - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expectedep = [math.ldexp(x, testval) for x in self.errordata]

				arrayfunc.ldexp(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_ldexp_NaN_array_num_array_b1(self):
		"""Test ldexp as *array-num-array* for nan - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.ldexp(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.ldexp(errordata, testval, self.dataout)


	########################################################
	def test_ldexp_NaN_array_num_array_b2(self):
		"""Test ldexp as *array-num-array* for nan with error check off - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedep = [math.ldexp(x, testval) for x in self.errordata]

				arrayfunc.ldexp(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class ldexp_inf_errors_d(unittest.TestCase):
	"""Test for basic general function operation using parameter inf.
	nan_data_error_ldexp_template
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

		arraysize =  len(self.dataok1)


		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('inf')] * arraysize)


		self.expectedep = [math.ldexp(x, y) for x,y in zip(self.errordata, itertools.cycle([-2, -1, 0, 1, 2]))]


	########################################################
	def test_ldexp_inf_array_num_none_a1(self):
		"""Test ldexp as *array-num-none* for inf - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.ldexp(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.ldexp(errordata, testval)


	########################################################
	def test_ldexp_inf_array_num_none_a2(self):
		"""Test ldexp as *array-num-none* for inf with error check off - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expectedep = [math.ldexp(x, testval) for x in self.errordata]

				arrayfunc.ldexp(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_ldexp_inf_array_num_array_b1(self):
		"""Test ldexp as *array-num-array* for inf - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.ldexp(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.ldexp(errordata, testval, self.dataout)


	########################################################
	def test_ldexp_inf_array_num_array_b2(self):
		"""Test ldexp as *array-num-array* for inf with error check off - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedep = [math.ldexp(x, testval) for x in self.errordata]

				arrayfunc.ldexp(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



##############################################################################



##############################################################################
class ldexp_ninf_errors_d(unittest.TestCase):
	"""Test for basic general function operation using parameter -inf.
	nan_data_error_ldexp_template
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
				raise self.failureException('%0.3f != %0.3f' % (expecteditem, dataoutitem))



	########################################################
	def setUp(self):
		"""Initialise.
		"""
		self.addTypeEqualityFunc(float, self.FloatassertEqual)

		self.dataok1 = array.array('d', [0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0])

		arraysize =  len(self.dataok1)


		self.dataout = array.array('d', itertools.repeat(0.0, arraysize))

		self.errordata = array.array('d', [float('-inf')] * arraysize)


		self.expectedep = [math.ldexp(x, y) for x,y in zip(self.errordata, itertools.cycle([-2, -1, 0, 1, 2]))]


	########################################################
	def test_ldexp_ninf_array_num_none_a1(self):
		"""Test ldexp as *array-num-none* for -inf - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.ldexp(dataok1, testval)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.ldexp(errordata, testval)


	########################################################
	def test_ldexp_ninf_array_num_none_a2(self):
		"""Test ldexp as *array-num-none* for -inf with error check off - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				errordata = copy.copy(self.errordata)

				expectedep = [math.ldexp(x, testval) for x in self.errordata]

				arrayfunc.ldexp(errordata, testval, matherrors=True)

				for dataoutitem, expecteditem in zip(errordata, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



	########################################################
	def test_ldexp_ninf_array_num_array_b1(self):
		"""Test ldexp as *array-num-array* for -inf - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				# Copy the array so we don't change the original data.
				dataok1 = copy.copy(self.dataok1)
				errordata = copy.copy(self.errordata)

				# This version is expected to pass.
				arrayfunc.ldexp(dataok1, testval, self.dataout)

				# This is the actual test.
				with self.assertRaises(ArithmeticError):
					arrayfunc.ldexp(errordata, testval, self.dataout)


	########################################################
	def test_ldexp_ninf_array_num_array_b2(self):
		"""Test ldexp as *array-num-array* for -inf with error check off - Array code d.
		"""
		for testval in [-2, -1, 0, 1, 2]:
			with self.subTest(msg='Failed with parameter', testval = testval):

				expectedep = [math.ldexp(x, testval) for x in self.errordata]

				arrayfunc.ldexp(self.errordata, testval, self.dataout, matherrors=True)

				for dataoutitem, expecteditem in zip(self.dataout, expectedep):
					# The behavour of assertEqual is modified by addTypeEqualityFunc.
					self.assertEqual(dataoutitem, expecteditem)



##############################################################################


##############################################################################
if __name__ == '__main__':

	# Check to see if the log file option has been selected. This is an option
	# which we have added in order to decide where to output the results.
	if '-l' in sys.argv:
		# Remove the option from the argument list so that "unittest" does 
		# not complain about unknown options.
		sys.argv.remove('-l')

		with open('arrayfunc_unittest.txt', 'a') as f:
			f.write('\n\n')
			f.write('ldexp\n\n')
			trun = unittest.TextTestRunner(f)
			unittest.main(testRunner=trun)
	else:
		unittest.main()

##############################################################################
